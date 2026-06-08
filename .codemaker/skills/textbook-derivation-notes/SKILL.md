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
version: 1.0.0
status: published
changelog: "Initial release: scanned/text-layer textbook section export with step-by-step derivations."
---

# Textbook Derivation Notes

## What this skill is for

The user owns a scanned textbook PDF (image-only, no text layer) and wants a **specific
section or page range** turned into a high-quality Markdown study note. The defining
characteristic of a good result here is twofold:

1. **Complete derivations** — every formula is derived step by step, no jumps. When a step
   uses the chain rule, product rule, a transpose identity, or term regrouping, that move is
   shown explicitly.
2. **Prose + formulas together** — the note is not a bare wall of equations. Each subsection
   opens with a short "思路/intuition" paragraph explaining *what problem is being solved and
   why*, then carries the reader through the math.

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

### Step 4 — Write the derivation note

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
<full derivation by default>

## 公式编号速查
| 编号 | 含义 |
|------|------|
| (N.M.k) | ... |
````

### Derivation conventions (the heart of this skill)

- **Never skip a step.** If you write `d/dt(ℓ cos φ) = -ℓ sin φ · φ̇`, that's good. If you
  jump from a constraint to its second derivative in one line, that's bad — show the first
  derivative, then the second, applying product/chain rule term by term.
- **Annotate the move, not just the result.** Use `\underbrace{...}_{\text{why}}` or a short
  parenthetical to label *which* rule or identity was used (e.g. "标量等于自身转置，故可合并").
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
- **Add a `公式编号速查` table** at the end mapping every equation number to a one-line
  meaning — the user uses it to jump around.

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
source PDF or the note.
