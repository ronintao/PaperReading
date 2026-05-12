"""
md_to_mht.py - Convert markdown file to MHT (MHTML) single-file format.
Handles: headings, bold/italic, LaTeX formulas (inline & block),
         tables, code blocks, images, blockquotes/callouts, lists.
Compatible with WizNote import.
"""
import re
import os
import sys
import glob
import hashlib
import shutil
import tempfile
import base64
import random
from pathlib import Path


def _ensure_miktex_path():
    """Auto-detect MiKTeX and add to PATH if not already available."""
    if shutil.which('latex'):
        return  # already in PATH

    # Common MiKTeX install locations on Windows
    candidates = [
        os.path.expandvars(r'%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64'),
        os.path.expandvars(r'%PROGRAMFILES%\MiKTeX\miktex\bin\x64'),
        os.path.expandvars(r'%PROGRAMFILES(X86)%\MiKTeX\miktex\bin\x64'),
        r'C:\MiKTeX\miktex\bin\x64',
    ]
    # Also search user-specific installs
    local_programs = os.path.expandvars(r'%LOCALAPPDATA%\Programs')
    if os.path.isdir(local_programs):
        for d in glob.glob(os.path.join(local_programs, 'MiKTeX*', 'miktex', 'bin', 'x64')):
            candidates.insert(0, d)

    for path in candidates:
        if os.path.isfile(os.path.join(path, 'latex.exe')):
            os.environ['PATH'] = path + os.pathsep + os.environ.get('PATH', '')
            print(f'  MiKTeX found: {path}')
            return

    print('  WARNING: MiKTeX not found. LaTeX formulas may fail to render.')


_ensure_miktex_path()

import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = (
    r'\usepackage{amsmath}'
    r'\usepackage{amssymb}'
    r'\usepackage{bm}'
)
import matplotlib.pyplot as plt
from PIL import Image


# ============================================================
#  LaTeX Rendering
# ============================================================

TEMP_DIR = tempfile.mkdtemp(prefix='latex_mht_')
RENDER_COUNT = 0


def render_latex(latex_str, display=False, fontsize=14, dpi=200):
    """Render LaTeX string to a PNG file. Returns filepath."""
    global RENDER_COUNT
    key = hashlib.md5(f"{latex_str}|{display}|{fontsize}|{dpi}".encode()).hexdigest()
    filepath = os.path.join(TEMP_DIR, f"f_{key}.png")

    if os.path.exists(filepath):
        return filepath

    fig = plt.figure(figsize=(0.01, 0.01))
    wrapped = f'$\\displaystyle {latex_str}$' if display else f'${latex_str}$'
    fig.text(0, 0, wrapped, fontsize=fontsize)
    fig.savefig(filepath, format='png', dpi=dpi, bbox_inches='tight',
                pad_inches=0.06, facecolor='white', edgecolor='none')
    plt.close(fig)
    RENDER_COUNT += 1
    return filepath


# ============================================================
#  Markdown Parser  (shared logic with md_to_docx.py)
# ============================================================

def strip_frontmatter(text, fallback_title='Document'):
    """Extract metadata from YAML frontmatter. Falls back to fallback_title if no frontmatter."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if m:
        fm = m.group(1)
        # Title: try aliases first, then title field
        title = None
        title_m = re.search(r'aliases:\s*\n\s*-\s*(.*)', fm)
        if title_m:
            title = title_m.group(1).strip()
        if not title:
            title_m = re.search(r'^title:\s*(.*)', fm, re.MULTILINE)
            if title_m:
                title = title_m.group(1).strip().strip('"').strip("'")
        if not title:
            title = fallback_title
        # Authors
        authors = []
        authors_m = re.findall(r'authors:\s*\n((?:\s*-\s*.*\n)*)', fm)
        if authors_m:
            authors = [a.strip().lstrip('- ') for a in authors_m[0].strip().split('\n')]
        # URL
        url_m = re.search(r'^url:\s*(.+)', fm, re.MULTILINE)
        url = url_m.group(1).strip() if url_m else ''
        return title, authors, url, text[m.end():]
    return fallback_title, [], '', text


def parse_blocks(text):
    blocks = []
    lines = text.split('\n')
    n = len(lines)
    i = 0

    while i < n:
        line = lines[i]

        if '<!--' in line.strip():
            while i < n and '-->' not in lines[i]:
                i += 1
            i += 1
            continue

        if not line.strip():
            i += 1
            continue

        if line.strip().startswith('```'):
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if i < n:
                i += 1
            blocks.append(('code', '\n'.join(code_lines), lang))
            continue

        hm = re.match(r'^(#{1,6})\s+(.*)', line)
        if hm:
            blocks.append(('heading', hm.group(2).strip(), len(hm.group(1))))
            i += 1
            continue

        if line.strip().startswith('$$'):
            latex_parts = []
            content = line.strip()[2:]
            if content.endswith('$$') and content != '':
                latex_parts.append(content[:-2])
            else:
                if content:
                    latex_parts.append(content)
                i += 1
                while i < n and not lines[i].strip().endswith('$$'):
                    latex_parts.append(lines[i])
                    i += 1
                if i < n:
                    last = lines[i].strip()
                    if last != '$$':
                        latex_parts.append(last[:-2])
            i += 1
            blocks.append(('latex_block', '\n'.join(latex_parts).strip()))
            continue

        if re.match(r'^\s*\|', line):
            table_lines = []
            while i < n and re.match(r'^\s*\|', lines[i]):
                table_lines.append(lines[i])
                i += 1
            blocks.append(('table', table_lines))
            continue

        img_m = re.match(r'^\s*!\[([^\]]*)\]\(([^)]+)\)', line)
        if img_m:
            blocks.append(('image', img_m.group(2), img_m.group(1)))
            i += 1
            continue

        if line.lstrip().startswith('>'):
            quote_lines = []
            while i < n and lines[i].lstrip().startswith('>'):
                stripped = re.sub(r'^>\s?', '', lines[i], count=1)
                quote_lines.append(stripped)
                i += 1
            blocks.append(('blockquote', '\n'.join(quote_lines)))
            continue

        if re.match(r'^(\s*)[-*+]\s', line):
            items = []
            while i < n:
                lm = re.match(r'^(\s*)[-*+]\s(.*)', lines[i])
                if lm:
                    indent = len(lm.group(1))
                    items.append((indent, lm.group(2)))
                    i += 1
                elif lines[i].strip() == '':
                    if i + 1 < n and re.match(r'^(\s*)[-*+]\s', lines[i + 1]):
                        i += 1
                        continue
                    else:
                        break
                elif lines[i].startswith('  ') and items:
                    prev_indent, prev_text = items[-1]
                    items[-1] = (prev_indent, prev_text + ' ' + lines[i].strip())
                    i += 1
                else:
                    break
            blocks.append(('list', items))
            continue

        para_lines = [line]
        i += 1
        while i < n and lines[i].strip() \
                and not lines[i].strip().startswith('#') \
                and not lines[i].strip().startswith('```') \
                and not lines[i].strip().startswith('$$') \
                and not lines[i].lstrip().startswith('>') \
                and not re.match(r'^\s*\|', lines[i]) \
                and not re.match(r'^\s*[-*+]\s', lines[i]) \
                and not re.match(r'^\s*!\[', lines[i]):
            para_lines.append(lines[i])
            i += 1
        blocks.append(('paragraph', ' '.join(l.strip() for l in para_lines)))

    return blocks


# ============================================================
#  HTML Generation
# ============================================================

# Collect all images: list of (filename, bytes)
_images = []
_img_counter = 0


def _register_image(filepath_or_bytes, prefix='img'):
    """Register an image and return its MHT-local filename."""
    global _img_counter
    _img_counter += 1
    name = f"{prefix}_{_img_counter:04d}.png"

    if isinstance(filepath_or_bytes, (str, Path)):
        with open(filepath_or_bytes, 'rb') as f:
            data = f.read()
    else:
        data = filepath_or_bytes

    _images.append((name, data))
    return name


def _html_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _render_inline_text(text):
    """Convert inline markdown (LaTeX, bold, italic, links) to HTML."""
    # Step 1: protect inline LaTeX by replacing with placeholders
    latex_map = {}
    counter = [0]

    def _latex_replace(m):
        latex_str = m.group(1)
        counter[0] += 1
        key = f'\x00LATEX{counter[0]}\x00'
        try:
            fpath = render_latex(latex_str, display=False, fontsize=12, dpi=200)
            img_name = _register_image(fpath, prefix='f')
            latex_map[key] = f'<img src="{img_name}" style="vertical-align:middle;height:1.3em;">'
        except Exception:
            latex_map[key] = f'<code style="color:#800000">${_html_escape(latex_str)}$</code>'
        return key

    text = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', _latex_replace, text)

    # Step 2: escape HTML in remaining text
    # But we need to preserve our placeholders, so escape around them
    parts = re.split(r'(\x00LATEX\d+\x00)', text)
    result_parts = []
    for p in parts:
        if p in latex_map:
            result_parts.append(latex_map[p])
        else:
            # escape, then handle markdown formatting
            p = _html_escape(p)
            # bold
            p = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p)
            # italic
            p = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', p)
            # links [text](url)
            p = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                       r'<a href="\2" style="color:#2E75B6;text-decoration:underline">\1</a>', p)
            result_parts.append(p)

    return ''.join(result_parts)


CALLOUT_COLORS = {
    'abstract': '#4472C4',
    'note': '#70AD47',
    'info': '#5B9BD5',
    'warning': '#ED7D31',
}

CSS = """
body {
    font-family: 'Microsoft YaHei', 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 12pt;
    line-height: 1.8;
    color: #333;
    padding: 24px 48px;
    max-width: 860px;
    margin: 0 auto;
}
h1 {
    font-size: 1.7em;
    color: #1a1a1a;
    border-bottom: 2px solid #4472C4;
    padding-bottom: 8px;
    margin-top: 0.8em;
}
h2 {
    font-size: 1.35em;
    color: #2E75B6;
    border-bottom: 1px solid #ddd;
    padding-bottom: 4px;
    margin-top: 1.6em;
}
h3 {
    font-size: 1.15em;
    color: #404040;
    margin-top: 1.3em;
}
h4 { font-size: 1.05em; color: #555; }
p, div.para { margin: 8px 0; }
strong { font-weight: bold; }
em { font-style: italic; }
a { color: #2E75B6; text-decoration: underline; }

pre {
    background: #f5f5f5;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 12px 16px;
    font-family: Consolas, 'Courier New', monospace;
    font-size: 9pt;
    line-height: 1.5;
    overflow-x: auto;
    white-space: pre;
}

table {
    border-collapse: collapse;
    margin: 12px 0;
    width: auto;
}
th, td {
    border: 1px solid #a7afbc;
    padding: 6px 12px;
    text-align: left;
    font-size: 10.5pt;
}
th {
    background: #f0f4f8;
    font-weight: bold;
}

.callout {
    border-left: 4px solid #5B9BD5;
    padding: 8px 16px;
    margin: 10px 0 10px 12px;
    background: #fafcfe;
    font-size: 11pt;
}
.callout-abstract { border-left-color: #4472C4; background: #f5f8fc; }
.callout-note { border-left-color: #70AD47; background: #f6faf3; }
.callout-info { border-left-color: #5B9BD5; background: #f5fafd; }
.callout-warning { border-left-color: #ED7D31; background: #fef8f3; }

.formula-block {
    text-align: center;
    margin: 16px 0;
}
.figure {
    text-align: center;
    margin: 16px 0;
}
.figure img {
    max-width: 90%;
}
.caption {
    text-align: center;
    font-size: 9pt;
    color: #888;
    font-style: italic;
    margin-top: 4px;
}
.meta {
    color: #666;
    font-size: 10pt;
    margin-bottom: 16px;
}
ul { padding-left: 2em; }
ul ul { padding-left: 1.5em; }
li { margin: 4px 0; }
"""


def blocks_to_html(title, authors, url, blocks, wiki_dir):
    """Convert parsed blocks to HTML string. Returns (html, images_list)."""
    global _images, _img_counter
    _images = []
    _img_counter = 0

    parts = []

    # Metadata
    meta_parts = []
    if authors:
        meta_parts.append(f'Authors: {", ".join(authors)}')
    if url:
        meta_parts.append(f'<a href="{url}">{_html_escape(url)}</a>')
    if meta_parts:
        parts.append(f'<div class="meta">{" &nbsp;|&nbsp; ".join(meta_parts)}</div>')

    for block in blocks:
        btype = block[0]

        if btype == 'heading':
            text, level = block[1], block[2]
            tag = f'h{min(level, 4)}'
            parts.append(f'<{tag}>{_render_inline_text(text)}</{tag}>')

        elif btype == 'paragraph':
            parts.append(f'<div class="para">{_render_inline_text(block[1])}</div>')

        elif btype == 'latex_block':
            latex = block[1]
            try:
                fpath = render_latex(latex, display=True, fontsize=16, dpi=250)
                img_name = _register_image(fpath, prefix='eq')
                parts.append(f'<div class="formula-block"><img src="{img_name}"></div>')
            except Exception as e:
                parts.append(f'<div class="formula-block"><code>[Formula error: {_html_escape(str(e))}]</code></div>')

        elif btype == 'code':
            code_text = block[1]
            parts.append(f'<pre>{_html_escape(code_text)}</pre>')

        elif btype == 'table':
            table_lines = block[1]
            rows = []
            for tl in table_lines:
                cells = [c.strip() for c in tl.strip().strip('|').split('|')]
                rows.append(cells)
            data_rows = [r for r in rows
                         if not all(re.match(r'^[-:]+$', c) for c in r if c)]
            if not data_rows:
                continue

            html_table = ['<table>']
            for ri, row in enumerate(data_rows):
                html_table.append('<tr>')
                tag = 'th' if ri == 0 else 'td'
                for cell in row:
                    html_table.append(f'<{tag}>{_render_inline_text(cell)}</{tag}>')
                html_table.append('</tr>')
            html_table.append('</table>')
            parts.append('\n'.join(html_table))

        elif btype == 'image':
            img_rel_path, alt = block[1], block[2]
            full_path = os.path.normpath(os.path.join(wiki_dir, img_rel_path))
            if os.path.exists(full_path):
                img_name = _register_image(full_path, prefix='fig')
                parts.append(f'<div class="figure"><img src="{img_name}"></div>')
                if alt:
                    parts.append(f'<div class="caption">{_html_escape(alt)}</div>')
            else:
                parts.append(f'<div class="figure" style="color:red">[Image not found: {_html_escape(img_rel_path)}]</div>')

        elif btype == 'blockquote':
            raw = block[1]
            callout_m = re.match(r'^\[!(\w+)\]\s*(.*)', raw, re.DOTALL)
            if callout_m:
                ctype = callout_m.group(1).lower()
                content = callout_m.group(2).strip()
                cls = f'callout callout-{ctype}'
            else:
                content = raw
                cls = 'callout'

            inner = []
            for qline in content.split('\n'):
                if qline.strip():
                    inner.append(f'<div>{_render_inline_text(qline.strip())}</div>')
            parts.append(f'<div class="{cls}">{"".join(inner)}</div>')

        elif btype == 'list':
            items = block[1]
            parts.append(_render_list_items(items))

    # Wrap in full HTML
    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{_html_escape(title)}</title>
<style>
{CSS}
</style>
</head>
<body>
<h1>{_html_escape(title)}</h1>
{''.join(parts)}
</body>
</html>"""

    return full_html, _images


def _render_list_items(items):
    """Render a flat list of (indent, text) into nested <ul> HTML."""
    if not items:
        return ''

    html = []
    stack = []  # stack of indent levels

    for indent, content in items:
        level = indent // 2

        while len(stack) > level + 1:
            html.append('</li></ul>')
            stack.pop()

        if not stack or level > stack[-1]:
            html.append('<ul>')
            stack.append(level)
        else:
            html.append('</li>')

        html.append(f'<li>{_render_inline_text(content)}')

    while stack:
        html.append('</li></ul>')
        stack.pop()

    return '\n'.join(html)


# ============================================================
#  MHT Packaging
# ============================================================

def build_mht(html, images, title, output_path):
    """Package HTML + images into a single MHT (MHTML) file."""
    boundary_outer = f"----=_NextPart_{random.randint(1000000000,9999999999):010d}.{random.randint(100,999)}"

    with open(output_path, 'wb') as f:
        # --- MIME headers (WizNote compatible) ---
        title_b64 = base64.b64encode(title.encode('utf-8')).decode('ascii')
        f.write(f'From: <Saved by CodeMaker>\r\n'.encode('ascii'))
        f.write(f'Subject: =?utf-8?B?{title_b64}?=\r\n'.encode('ascii'))
        f.write(f'MIME-Version: 1.0\r\n'.encode('ascii'))
        f.write(f'Content-Type: multipart/related;\r\n'.encode('ascii'))
        f.write(f'\ttype="text/html";\r\n'.encode('ascii'))
        f.write(f'\tboundary="{boundary_outer}"\r\n'.encode('ascii'))
        f.write(b'\r\n')

        # --- HTML part ---
        f.write(f'--{boundary_outer}\r\n'.encode('ascii'))
        f.write(f'Content-Type: text/html;\r\n'.encode('ascii'))
        f.write(f'\tcharset="utf-8"\r\n'.encode('ascii'))
        f.write(f'Content-Transfer-Encoding: base64\r\n'.encode('ascii'))
        f.write(b'\r\n')

        html_b64 = base64.b64encode(html.encode('utf-8')).decode('ascii')
        for i in range(0, len(html_b64), 76):
            f.write(html_b64[i:i + 76].encode('ascii'))
            f.write(b'\r\n')

        # --- Image parts ---
        for img_name, img_data in images:
            f.write(b'\r\n')
            f.write(f'--{boundary_outer}\r\n'.encode('ascii'))
            f.write(f'Content-Type: image/png;\r\n'.encode('ascii'))
            f.write(f'\tname="{img_name}"\r\n'.encode('ascii'))
            f.write(f'Content-Transfer-Encoding: base64\r\n'.encode('ascii'))
            f.write(f'Content-Location: {img_name}\r\n'.encode('ascii'))
            f.write(b'\r\n')

            img_b64 = base64.b64encode(img_data).decode('ascii')
            for i in range(0, len(img_b64), 76):
                f.write(img_b64[i:i + 76].encode('ascii'))
                f.write(b'\r\n')

        # --- End ---
        f.write(f'\r\n--{boundary_outer}--\r\n'.encode('ascii'))

    print(f'\nSaved: {output_path}')
    size_kb = os.path.getsize(output_path) / 1024
    print(f'Size: {size_kb:.0f} KB')
    print(f'Images embedded: {len(images)}')
    print(f'Formulas rendered: {RENDER_COUNT}')


# ============================================================
#  Main
# ============================================================

def main():
    if len(sys.argv) < 2:
        print('Usage: python md_to_mht.py <input.md> [output.mht]')
        sys.exit(1)

    md_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        # Default: output/ folder as sibling to the md file's parent directory
        md_abs = os.path.abspath(md_path)
        md_dir = os.path.dirname(md_abs)
        parent_dir = os.path.dirname(md_dir)
        output_dir = os.path.join(parent_dir, 'output')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, Path(md_path).stem + '.mht')
    wiki_dir = os.path.dirname(os.path.abspath(md_path))

    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Derive fallback title from filename (without extension)
    fallback_title = Path(md_path).stem.replace('-', ' ').replace('_', ' ').title()
    title, authors, url, body = strip_frontmatter(text, fallback_title=fallback_title)
    print(f'Title: {title}')
    print(f'Authors: {", ".join(authors)}')
    print(f'Parsing markdown...')
    blocks = parse_blocks(body)
    print(f'Blocks: {len(blocks)}')

    print(f'Generating HTML + rendering formulas with LaTeX...')
    html, images = blocks_to_html(title, authors, url, blocks, wiki_dir)

    print(f'Packaging MHT...')
    build_mht(html, images, title, output_path)


if __name__ == '__main__':
    main()
