---
name: md-to-mht
display_name: "Markdown to MHT Export"
description: "Use when the user asks to export, convert, or save a markdown file as MHT format. Activates for: '导出成mht', '转换成mht', 'export to mht', 'convert to mht', '导出笔记', 'export note', '生成mht', 'save as mht', or any task involving converting markdown to MHT/MHTML format for WizNote or offline viewing. If the user mentions exporting a .md file to a single-file format with embedded images and formulas, use this skill."
category: documentation
tags:
  - export
  - mht
  - markdown
  - wiznote
  - document-conversion
version: 1.0.1
status: published
---

# Markdown to MHT Export

Convert any markdown file to a self-contained MHT (MHTML) file with LaTeX formulas rendered as PNG images, figures embedded, and full styling preserved. Output is compatible with WizNote import.

## Architecture

```
.codemaker/skills/md-to-mht/
├── skill/
│   └── SKILL.md          ← this file
└── scripts/
    └── md_to_mht.py      ← conversion script (Python)
```

## Environment Setup

Before first use, ensure the following dependencies are installed. This is a one-time setup.

### 1. MiKTeX (LaTeX distribution)

MiKTeX provides `latex` and `dvipng` for rendering LaTeX formulas to PNG.

**Install via winget:**
```bash
winget install MiKTeX.MiKTeX --accept-package-agreements --accept-source-agreements
```

**Enable auto-install of LaTeX packages** (so missing packages are downloaded on demand):
```bash
initexmf --set-config-value=[MPM]AutoInstall=1
```

**Default install path:** `C:\Users\<username>\AppData\Local\Programs\MiKTeX\miktex\bin\x64`

The conversion script auto-detects MiKTeX location. If MiKTeX is installed elsewhere, ensure the `miktex\bin\x64` directory is in the system PATH.

### 2. Python packages

```bash
pip install matplotlib pillow
```

- `matplotlib` — renders LaTeX to PNG via `usetex=True` mode
- `Pillow` — image processing (reading dimensions for sizing)

### Verification

Run a quick test to confirm the environment works:
```bash
python -c "import matplotlib; matplotlib.use('Agg'); matplotlib.rcParams['text.usetex']=True; import matplotlib.pyplot as plt; fig=plt.figure(figsize=(4,0.6)); fig.text(0.5,0.5,r'$F = ma$',fontsize=16,ha='center',va='center'); fig.savefig('test_latex.png',dpi=150,bbox_inches='tight'); print('OK')"
```
If this prints `OK` and produces a `test_latex.png` with a rendered formula, the environment is ready.

## Operation: Export

**Trigger phrases:** "导出成 mht", "转换成 mht", "export to mht", "导出这个笔记"

When the user requests MHT export:

### Phase 1 — Identify the input file

1. Determine which `.md` file to export. The user may:
   - Provide a file path directly
   - Reference a file by name/slug (e.g., "导出 topic-constraint-force-calc")
   - Say "导出这个" when a specific file is in context

2. Confirm the file exists and announce: "将导出 `<filename>.md` → `<filename>.mht`"

### Phase 2 — Run the conversion

Execute the conversion script (located inside this skill's directory):

```bash
python <Skill-Root>/scripts/md_to_mht.py "<input.md>" "<output.mht>"
```

Where `<Skill-Root>` is the skill's installation directory (`.codemaker/skills/md-to-mht`). Resolve to the absolute path at runtime.

The script auto-detects MiKTeX in common install locations and adds it to PATH if needed. It handles:
- **YAML frontmatter** → extracts title (from `aliases` or `title` field), authors, URL for document header; falls back to filename if no frontmatter
- **LaTeX formulas** → `$inline$` and `$$block$$` rendered to PNG via matplotlib + usetex
- **Images** → `![alt](path)` resolved relative to the markdown file's directory
- **Tables** → HTML tables with borders and bold headers
- **Code blocks** → monospace font (Consolas) with gray background
- **Callouts** → `> [!note]`, `> [!abstract]` etc. with colored left border
- **Lists** → nested bullet lists with proper indentation
- **Bold/italic/links** → standard HTML formatting

### Phase 3 — Report result

Report to the user:
- Output file path
- File size
- Number of formulas rendered
- Number of images embedded

## Conventions

- Output file is placed in an **`output/` folder** as sibling to the markdown file's parent directory:
  - `<Paper Title>/wiki/topic-xxx.md` → `<Paper Title>/output/topic-xxx.mht`
  - `<Project>/docs/notes.md` → `<Project>/output/notes.mht`
- If `output/` doesn't exist, it is created automatically
- Output filename matches input stem: `<name>.md` → `<name>.mht`
- The output path can be overridden via the second CLI argument
- MHT uses UTF-8 encoding for HTML content
- All images (formulas + figures) are base64-encoded as MIME parts
- If a LaTeX formula fails to render, it falls back to styled inline code text
- If a referenced image file is missing, a red error placeholder appears in the output
