---
name: textbook-derivation-notes
description: >
  Turn a section or chapter of a textbook PDF into a detailed, step-by-step derivation study
  note in Markdown. Use this whenever the user asks to "详细阅读 XX 书的 XX 章/节",
  "OCR 这一节/这一章", "导出第X节为笔记", "把书页 A~B 整理成 markdown", "公式推导列详细一些/不要跳步骤",
  "把教材某节做成带推导的笔记", or otherwise wants a math-heavy textbook section converted into
  prose-plus-derivation notes. Works for both scanned (image-only) PDFs and PDFs with a text
  layer — OCR is only needed for scanned sources. The defining trait of a good result is
  complete, no-skipped-steps formula derivations alongside explanatory prose. Prefer this
  skill over plain paper-reading when the deliverable is a single detailed derivation document
  for a specific book section or chapter.
category: documentation
display_name: "Textbook Derivation Notes"
tags:
  - pdf
  - ocr
  - math
  - study-notes
version: 1.1.0
status: published
changelog: "1.1.0: add mandatory figure crop+embed step (3.5) matching the 3.x/4.x note convention. 1.0.0: initial scanned/text-layer textbook section export with step-by-step derivations."
---

# Textbook Derivation Notes

## What this skill is for

The user owns a scanned textbook PDF (image-only, no text layer) and wants a **specific
section or page range** turned into a high-quality Markdown study note. The defining
characteristic of a good result here is threefold:

1. **Complete derivations** — every formula is derived step by step, no jumps. When a step
   uses the chain rule, product rule, a transpose identity, or term regrouping, that move is
   shown explicitly.
2. **Prose + formulas together** — the note is not a bare wall of equations. Each subsection
   opens with a short "思路/intuition" paragraph explaining *what problem is being solved and
   why*, then carries the reader through the math.
3. **Figures cropped and embedded** — every figure the section references is cropped from the
   rendered pages into the shared `wiki/figures/<book-main-slug>/` folder and embedded at its
   first citation (see Step 3.5). A derivation note without its figures is incomplete.

This skill captures a workflow that was validated end-to-end on a multibody-dynamics
textbook. Follow it, but adapt page offsets and structure to the book at hand.

## Where to write the note

If the workspace already follows the paper-reading wiki layout (a `wiki/` folder next to the
PDF), write the note there as `wiki/<section-slug>.md` and add a `chapter-notes` YAML
frontmatter block (see template below). Otherwise write it next to the PDF with a clear
filename like `<book-slug>-sec-<N>.md`. Ask the user only if the location is genuinely
ambiguous.

## Workflow

Both rendering steps are scripted in `scripts/render_pages.py` (needs `pip install pymupdf`).
Prefer the script over hand-writing inline PyMuPDF code — it handles the offset arithmetic,
out-of-range guards, and consistent file naming for you.

### Step 0 — Pin down the page range

You need a concrete page (or chapter→page) range before doing anything else.

- **User gave a page range** (e.g. "书页 218~229") → use it directly, go to Step 1.
- **User named a section/chapter but no pages** (e.g. "详细阅读 XX 书的第 6 章") → ask the user
  for the page range first. Don't guess — the wrong range wastes a lot of OCR.
- **User then asks you to find it from the table of contents** → only now scan the TOC: try
  PDF bookmarks (`doc.get_toc()`) first; if there are none, render the TOC pages (usually
  near the front, probe a handful) and read them to map the chapter/section to its book-page
  range. Confirm the resulting range with the user before rendering the whole thing.

### Step 1 — Locate the PDF and decide whether OCR is needed

First check whether the PDF has a usable text layer — this decides the whole path:

```python
import fitz
doc = fitz.open(pdf_path)
lengths = [len(doc[i].get_text()) for i in range(doc.page_count)]
scanned = sum(1 for L in lengths if L < 50) > 0.5 * len(lengths)
```

- **Text-layer PDF** (`scanned` is False) → **skip OCR entirely.** Read the pages' text
  directly (via `read_file` on the PDF with page offsets, or `doc[i].get_text()`), then jump
  straight to Step 4. No rendering, no vision pass needed.
- **Scanned / image-only PDF** (`scanned` is True) → continue with the offset probe and
  rendering below, then OCR via vision in Step 3.

**Map book pages to PDF pages (scanned path).** Scanned books almost always have a
**front-matter offset**: book page 213 might be PDF page 225. Never assume it. Probe with the
script (give it 1-based PDF page numbers to sample):

```bash
python scripts/render_pages.py probe "book.pdf" --pdf-pages 225 236 -o temp_probe
```

Read the probe images, note the printed book-page number in the header/footer, and compute
`offset = (1-based pdf page) - (printed book page)`. Verify with a second page so you're sure
it's constant. (In the validated case the offset was +12: book 218 → PDF 230.)

### Step 2 — Render the target pages (scanned path only)

Render the inclusive **book-page** range at 200 dpi (good balance of legibility for
subscripts/primes and speed); files are named by book page so they're easy to reference:

```bash
python scripts/render_pages.py render "book.pdf" --book-range 218 229 --offset 12 -o temp_sec
```

(If you'd rather drive it by raw 1-based PDF indices, use `--pdf-range 230 241` instead.)

**Keep these images by default.** The user found them useful to keep around for re-checking
OCR. Only delete the temp folder if the user explicitly asks.

### Step 3 — Read the pages with vision (scanned path only)

Read the rendered PNGs in small batches (about 3 images per turn keeps things reliable).
Capture every equation, its equation number, surrounding prose, figure captions, and section
headings. Pay special attention to:

- subscripts/superscripts, primes (`x'`), bold (vectors/matrices) vs italic (scalars)
- equation numbers like `(6.3.16)` — preserve them exactly, the user navigates by them
- transposes, dots (time derivatives), and hats — easy to lose in OCR

If the requested range spans more than ~15 pages, read in multiple batches and assemble
incrementally.

### Step 3.5 — Crop and embed the section's figures (do NOT skip)

A derivation note **without figures is incomplete**. Every figure the section references
(`Fig. 6.1.2`, `图 3.6.1`, tables that are drawn as figures, etc.) must be cropped from the
rendered pages and embedded at the point it is first cited. This is the convention the user
converged on across the 3.x / 4.x / 6.x notes — match it exactly.

**1. Where figures live.** Keep one **shared** figure folder for the whole book, named by the
book's main wiki slug, not one folder per section:

```
wiki/figures/<book-main-slug>/fig_<chap>_<sec>_<idx>_<short-slug>.png
```

Examples (real): `fig_3_6_1_block_sliding.png`, `fig_4_5_1_newton_raphson.png`,
`fig_6_1_2_tractor.png`. The `<chap>_<sec>_<idx>` mirrors the book's figure number
(`Fig. 6.1.2` → `6_1_2`); `<short-slug>` is a 1–3 word English description.

**2. How to crop.** Write a tiny per-section PIL script next to the PDF named
`crop_figs_<sec>.py` (e.g. `crop_figs_61.py`) using fractional bounding boxes over the
rendered `temp_sec*/book_XXX.png` pages. This is the exact helper the existing scripts use —
reuse it verbatim:

```python
from PIL import Image
import os

base = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(base, 'wiki', 'figures', '<book-main-slug>')
os.makedirs(out, exist_ok=True)


def crop(src, box, name):
    im = Image.open(os.path.join(base, src))
    w, h = im.size
    l, t, r, b = box                       # fractional (left, top, right, bottom) in [0,1]
    im.crop((int(l * w), int(t * h), int(r * w), int(b * h))).save(os.path.join(out, name))
    print('wrote', name)


# read the rendered page first to eyeball the figure's fractional box, then:
crop('temp_sec61/book_205.png', (0.20, 0.55, 0.85, 0.92), 'fig_6_1_2_tractor.png')
```

Determine each box by **reading the rendered page image** and estimating where the figure
sits (top/bottom halves are common; a full-width figure is roughly `l≈0.18, r≈0.86`). One
`crop(...)` call per figure. Run the script with `python crop_figs_<sec>.py`.

**3. How to embed.** Standard markdown embed (NOT Obsidian `![[...]]`), placed **right where
the figure is first referenced** — typically just after the example's one-line `> setup`
blockquote and before the equations:

```markdown
![图 6.1.2 拖拉机平面运动](figures/<book-main-slug>/fig_6_1_2_tractor.png)
```

- Alt text = `图 <N.M.k> <中文标题>` (or `Fig. <N.M.k> <中文标题>`), matching the book caption.
- For **conceptual** figures (geometry, convergence behaviour, etc.), follow the image with a
  bold caption-explanation line, e.g. `**图 4.5.2（拐点 inflection point）**：当解恰是曲线的
  拐点时，切线交点在解两侧来回振荡……`. For plain **setup** figures (a mechanism sketch), the
  embed alone is enough — no separate caption line needed.
- A figure that combines two book figures can share one crop + one alt (e.g.
  `图 3.7.1 锁死构型 / 图 3.7.2 分岔构型`).

**Verify** every embedded path resolves to a file that the crop script actually wrote before
declaring the note done.

### Step 4 — Write the derivation note

**Before writing, consult the terminology glossary.** If a `wiki/glossary.md` (`type: glossary`)
exists next to the note, **read it first** and follow its fixed Chinese translations exactly —
first occurrence annotates the English term (e.g. `构型（configuration）`, `关节（joint）`), later
occurrences use Chinese only. Whenever you introduce a new key term that is not yet listed,
**add it** to the appropriate category in `wiki/glossary.md` and bump its `last_updated`. If the
glossary doesn't exist yet but the book has a stable set of recurring terms, offer to create one
(grouped tables with columns `| English | 中文（统一译名） | 备注 |` plus a "维护说明" footer
saying the glossary wins over any conflicting note). The glossary always wins over an individual
note — if they disagree, fix the note.

Use this structure. It is the format the user converged on after iterating.

````markdown
---
type: chapter-notes
parent: <book-main-slug>
chapter: <N>
title: "<Section number> <Section Title>"
pages: <start>-<end>           # BOOK pages, not PDF indices
sections:
  - "<N.M> <Subsection Title>"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# <Section number> <中文标题>

> 来源：*<Book Title>*，第 <N> 章，<section> 节（书页 <start>–<end>）。
> 本文以"文字讲解 + 逐式详细推导"组织，公式推导不跳步骤。

## 引言：本节要解决什么
<2-5 句话：本节在全书/全章中的位置，要解决的问题，主线逻辑的编号列表>

## <N.M> <Subsection Title>
### 思路
<prose: what is being set up and why>
### <derivation>
<step-by-step equations, each non-trivial move explained>

## 例 <N.M.k>：<Example name>
> <one-line figure/setup description>
![图 <N.M.k> <中文标题>](figures/<book-main-slug>/fig_<chap>_<sec>_<idx>_<slug>.png)
<full derivation by default>
````

### Derivation conventions (the heart of this skill)

- **Never skip a step.** If you write `d/dt(ℓ cos φ) = -ℓ sin φ · φ̇`, that's good. If you
  jump from a constraint to its second derivative in one line, that's bad — show the first
  derivative, then the second, applying product/chain rule term by term.
- **数学推导用公式说话，不用文字。** 除非概念特别复杂、或定理代入特别繁琐确需文字点明，否则推导
  的每一步都应以公式表达：定义式 → 代入 → 化简 → 结果，链式写成一条长公式（如
  `\ddot{q} = \Phi_q^{-1}[\dots] = [\dots] = [\dots]`）。**禁止**用 `\underbrace{...}_{\text{...}}`
  在式中标注来源，也**禁止**"注意/逐项说明/自下而上回代/一气呵成"之类的散文式说明替代公式。
- **Explain the "why" in prose**, not only the algebra. A line like "物理上，$\Phi_q^T\lambda$
  正是被消去的约束力以乘子形式重新出现" is worth more than another equation.
- **When a step looks like a trick, give the general method too.** If a hand derivation
  "happens to" produce a clean form, add the systematic derivation that shows it isn't luck
  (e.g. deriving the acceleration equation both by direct double-differentiation *and* by the
  general formula $\Phi_q\ddot q = -(\Phi_q\dot q)_q\dot q$). This is exactly what the user
  asked for when a step felt too slick.
- **Examples: full by default.** Reproduce the example's setup, the applied-force vector, the
  mass matrix, the constraint and its Jacobian, etc., with the same step-by-step rigor.
  Only condense examples to a "简述" bullet if the user explicitly says examples can be brief.
- **Math syntax:** inline `$...$`, block `$$...$$`. Vectors/matrices bold (`\mathbf{}`),
  keep original equation numbers via `\tag{6.3.16}`. Box key results with `\boxed{}`.
  Inside Markdown table cells, never use raw `|` (e.g. absolute-value bars) — it breaks the
  table; write `\lvert ... \rvert` (or `\bigl\lvert ... \bigr\rvert`) instead.

### Scope discipline

Honor the user's stated boundary precisely. If they ask for "6.3 节", include only 6.3 even
if the page range you OCR'd bleeds into 6.2's tail or 6.4's head — drop the out-of-scope
material. A page range and a section name can disagree; when they do, ask or follow the
section name, and note the discrepancy.

### Physical interpretation & cross-references

Where the text states a physical meaning (why constraint virtual work vanishes, what a
multiplier represents), fold it into the prose. Reference other equations and sections by
their original numbers so the note stands on its own.

## Iterating with the user

Common follow-up requests and how to handle them:

- *"太短了 / 增加内容但保留推导"* → you over-condensed examples. Restore full example
  derivations while keeping the added prose. Length should come from completeness, not filler.
- *"这一步怎么来的"* → expand that single step into its own labeled mini-derivation, and
  consider adding it into the note (not just answering in chat) if the user asks.
- *"去掉非 X 节内容"* → trim scope, keep everything within X at full detail.

## Cleanup

Leave the rendered page images in place unless asked to remove them. If the user does ask,
delete only the temp render folder you created (e.g. `temp_sec/`, `probe_*.png`) — never the
source PDF, the note, the `crop_figs_<sec>.py` scripts, or anything under `wiki/figures/`.
