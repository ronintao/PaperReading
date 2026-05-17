---
name: paper-reading
display_name: "Paper Reading"
description: "Use when the user asks to research, read, ingest, or analyze a paper/article, or when organizing paper reading notes. Activates for: '研究下这篇文章', '帮我看看这篇论文', '帮我读下这篇论文', '增加下这篇文章', 'add this paper', 'read this paper', paper ingest, paper reading, paper analysis, 论文阅读, figure extraction from PDFs, chapter-by-chapter reading of books/textbooks ('分析第X章', '读一下他的第N章', 'analyze chapter N', '逐章阅读'), or any task involving structured paper reading notes. If the user mentions a paper title, arXiv link, DOI, or drops a PDF for research purposes, use this skill."
category: documentation
tags:
  - paper-reading
  - research
  - academic
  - pdf-analysis
version: 2.4.0
status: published
---

# Paper Reading — 论文阅读解读助手

You help the human read, analyze, and organize papers with structured reading notes. The human curates papers and directs analysis; you read full texts, compile structured reading notes, maintain cross-references within each paper's wiki, and extract figures. For book-length works (textbooks, monographs), you also support chapter-by-chapter deep reading with dedicated chapter notes.

## Architecture

```
<Paper-Root>/                      → Project root (e.g., e:\PaperReading)
├── <Paper Title A>/               → One folder per paper being studied
│   ├── <paper-a>.pdf              → Main paper PDF
│   ├── wiki/                      → All reading notes for this paper
│   │   ├── index.md               → Navigation entry for this paper
│   │   ├── <main-slug>.md         → Main paper reading note
│   │   ├── <related-slug>.md      → Related paper reading note (same format)
│   │   ├── ch<N>-<slug>.md        → Chapter reading note (for books/textbooks)
│   │   └── figures/               → Extracted figures, grouped by paper
│   │       ├── <main-slug>/
│   │       │   ├── figure_1.png
│   │       │   └── figure_2.png
│   │       └── <related-slug>/
│   │           └── figure_1.png
│   └── Related/                   → Reference PDFs only (no subdirectories)
│       └── <related-paper>.pdf
├── <Paper Title B>/
│   └── ...
```

### Key Principles

- **Paper-centric**: Each paper folder is self-contained. No cross-folder dependencies.
- **Flat Related/**: `Related/` stores only PDF files. No nested directories, no reading notes inside it.
- **Wiki as notes**: `wiki/` holds all reading notes (main + related papers) and extracted figures.
- **Standard markdown**: All files use standard markdown syntax. No Obsidian wikilinks or special syntax.

## Page Formats

### Reading Note (source page)

Each paper's reading note is a markdown file with YAML frontmatter and 8 fixed sections.

**YAML Frontmatter:**

```yaml
---
type: source
id: <kebab-case-slug>
pdf_path: ../<slug>.pdf              # Main paper (relative to wiki/)
# or: ../Related/<slug>.pdf         # Related paper (relative to wiki/)
tags:
  - <domain-tag>
  - year/YYYY-MM
  - venue/<short-name>
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
authors:
  - <Author Name>
aliases:
  - <Full Paper Title>
---
```

**Body Sections (in order):**

| Section | Purpose |
|---------|---------|
| `## Essence` | One-sentence summary + contribution statement |
| `## Factors` | Context, Related Work, Gap, Proposal |
| `## Architecture` | Technical details, diagrams, key equations |
| `## Evidence` | Experiments, results, validation |
| `## Critical Analysis` | Novel Insight, Fundamental Limitations, Research Frontier |
| `## Relations` | Temporal context + links to other papers (builds_on, contrasts_with, complements) |
| `## Transferable Inspirations` | Ideas that can be applied beyond this paper's domain |
| `## Open Questions` | Unresolved questions after reading |

See `templates/paper.md` for the full template with formatting conventions.

### Chapter Notes (chapter-notes page)

For book-length works (textbooks, monographs), each chapter can have a dedicated reading note. Chapter notes focus on **concept definitions, symbol definitions, and key arguments** rather than the paper-level Essence/Factors/Architecture structure.

**YAML Frontmatter:**

```yaml
---
type: chapter-notes
parent: <parent-source-slug>       # slug of the book's main reading note
chapter: <N>                       # chapter number (integer)
title: "<Chapter Title>"
pages: <start>-<end>               # page range in the book (not PDF pages)
sections:
  - "<N.M> <Section Title>"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

**Body Sections (in order):**

| Section | Purpose |
|---------|---------|
| `## 章节定位` | Chapter's role within the book, what it covers and doesn't cover |
| `## 概念定义` | ALL concept definitions introduced in this chapter, with English original + Chinese translation |
| `## 符号定义` | ALL mathematical/physical symbols introduced, grouped by context |
| `## 核心论点` | Main arguments, comparisons, and conclusions |
| `## 工程应用与实例` | Worked examples, engineering applications, case studies |
| `## 与全书的关系` | How this chapter's content maps to other chapters |

**Concept definition format:**

```markdown
**<English Term>（<中文译名>）** [p.<page>]
> <Original English definition quoted from the text.>
>
> <Chinese translation of the definition.>
```

**Symbol definition format (table):**

```markdown
| 符号 | 类型 | 含义 |
|------|------|------|
| $\theta$ | 标量，角度 | 曲柄角 |
```

**Filename convention:** `ch<N>-<kebab-case-slug>.md`, e.g., `ch1-elements-of-cakd.md`, `ch3-planar-kinematics.md`

See `templates/chapter.md` for the full template with formatting conventions.

### Index Page (wiki/index.md)

```yaml
---
type: index
title: <Full Paper Title>
wiki_language: <language-code>    # en | zh-CN | zh-TW | ja | ...
last_updated: YYYY-MM-DD
---
```

```markdown
# 论文解读导航

## 主论文
- <main-slug> (<authors>, <year>, <venue>)

## Related 论文解读
- <related-slug-1> (<authors>, <year>, <venue>)
- <related-slug-2> (<authors>, <year>, <venue>)

## Topic 专题
- <topic-slug>: <brief description of the sub-question>

### 逐章精读笔记
- [Ch.<N> <Chapter Title>](ch<N>-<slug>.md) — <one-line summary>
```

## Operations

### Ingest (add a paper to the wiki)

When the human asks to add/ingest/研究 a specific paper, follow these phases:

---

**Phase -1 — Paper Acquisition (auto-locate and download if needed):**

Before reading the paper, ensure the PDF exists locally. Follow this decision tree:

1. **Check if PDF already exists** — Search the current paper folder and `Related/` for the PDF:
   ```bash
   dir /s /b "<Paper Folder>\*.pdf"
   ```
   Also check if a reading note already exists in `wiki/` (by title/slug similarity). If already fully ingested, inform the human and skip.

2. **If PDF not found — resolve the paper's identity.** The human may provide:

   - **arXiv ID** (e.g., `2604.00590`): download directly
     ```bash
     curl -L -o "<target-path>/<slug>.pdf" "https://arxiv.org/pdf/<arxiv-id>"
     ```

   - **DOI** (e.g., `10.4028/www.scientific.net/AMR.97-101.2824`): try Semantic Scholar first, then Sci-Hub
     ```bash
     curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=title,openAccessPdf,externalIds"
     ```
     If `openAccessPdf` exists → download. Otherwise → Sci-Hub (see below).

   - **URL** (arXiv, OpenReview, conference page): extract the PDF link and download. If URL contains a DOI, follow DOI path.

   - **Paper title only**: search for it:
     ```bash
     # 1) Try arXiv API (preferred — gives direct PDF link)
     curl -s "https://export.arxiv.org/api/query?search_query=ti:<url-encoded-title>&max_results=3"
     ```
     If arXiv returns a match, download the PDF. If not:
     ```bash
     # 2) Try Semantic Scholar
     curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=<url-encoded-title>&limit=3&fields=title,externalIds,openAccessPdf"
     ```
     Use `openAccessPdf.url` if available. Otherwise, extract DOI from response and try Sci-Hub.

3. **Sci-Hub fallback (via DOI)** — If arXiv and Semantic Scholar openAccessPdf both fail but a DOI is available:

   a. **Discover Sci-Hub mirrors dynamically:**
      ```bash
      # Use a search engine to find current Sci-Hub URLs
      curl -sL "https://duckduckgo.com/html/?q=sci-hub"
      ```
      Extract the first 5 URLs from search results that contain "sci-hub" in the domain.

   b. **Try each mirror in sequence:**
      For each candidate URL:
      ```bash
      curl -sL "<candidate-url>/<DOI>" -o temp_download
      ```
      - If the response is a PDF (file > 1KB and starts with `%PDF`): success, rename to target path.
      - If the response is HTML: parse for `<iframe src="...">` or `<embed src="...">` containing a PDF URL, then download that URL.
      - If neither works: try next candidate.

   c. **All mirrors fail** → proceed to step 4.

4. **If download fails** — Inform the human: "无法自动下载此论文的 PDF，请手动将 PDF 放入 `<Paper Folder>/` 或 `<Paper Folder>/Related/`。" Then stop.

5. **Verify download** — Confirm the PDF exists and is > 1KB (not an error page).

**Download priority chain:** arXiv direct → Semantic Scholar openAccessPdf → Sci-Hub via DOI → manual placement.

**Hard gate:** Do NOT proceed to Phase 0 until a valid PDF exists.

---

**Phase 0 — Full-Text Reading:**

1. **Detect if the PDF is a scanned document (no text layer):**

   Use PyMuPDF to check text content on each page:
   ```python
   import fitz
   doc = fitz.open(pdf_path)
   text_lengths = [len(doc[i].get_text()) for i in range(doc.page_count)]
   is_scanned = sum(1 for l in text_lengths if l < 50) > len(text_lengths) * 0.5
   ```
   If more than half the pages have fewer than 50 characters of extracted text, treat as a scanned PDF.

2. **If the PDF has a text layer:** use `read_file` to read the PDF directly. Read the full text.

3. **If the PDF is a scanned document:**

   a. Render each page to a PNG image in a dedicated subfolder:
      ```python
      import os
      os.makedirs("temp_scan", exist_ok=True)
      for i in range(doc.page_count):
          pix = doc[i].get_pixmap(dpi=200)
          pix.save(f"temp_scan/page_{i+1:03d}.png")
      ```

   b. Use `read_file` on each PNG image to read the content through LLM vision capabilities. The LLM can understand text, formulas, tables, and figures from the images.

   c. Synthesize content from all pages for analysis in subsequent phases.

   d. **Cleanup**: After the reading note is fully written (Phase 4 complete), delete the entire `temp_scan/` folder. These are temporary intermediates, NOT the paper's extracted figures.

   > **Note**: If the scanned PDF exceeds 15 pages, a single session may not suffice. In that case, refer to the multi-session batch approach described in the Chapter Reading operation.

4. Read the full paper text with active comprehension — identify structure, key arguments, methodology, results, and limitations.

---

**Phase 1 — Analyze:**

1. Read `wiki/index.md` (if it exists) to understand what has already been ingested for this paper.
2. Read any existing reading notes in `wiki/` to build context.
3. Analyze the paper systematically: extract essence, factors, architecture, evidence, critical analysis, relations, transferable inspirations, open questions.
4. Identify temporal positioning relative to existing related papers.

---

**Phase 2 — Report to human:**

Summarize key findings to the human before writing. Include:
- One-sentence summary
- Key contribution
- Main limitations
- Relationship to other papers already in the wiki (if any)

Wait for human confirmation before proceeding to write.

---

**Phase 3 — Extract figures:**

```bash
python scripts/paper_extract_figures.py "<pdf-path>" -o "wiki/figures/<slug>" -f json
```

Review the extracted figures. Select the most informative ones for inclusion in the reading note.

---

**Phase 4 — Write reading notes:**

1. **Create/update `wiki/<slug>.md`** using the `templates/paper.md` template. Fill in all 8 sections based on Phase 1 analysis.

2. **Image embeds**: Reference extracted figures using relative paths:
   ```markdown
   ![Figure description](figures/<slug>/figure_N.png)
   ```

3. **Cross-references**: When referencing other papers within the same `wiki/`, use standard markdown links:
   ```markdown
   See [related-paper-slug](related-paper-slug.md) for the foundational proof.
   ```
   Or use plain text slugs when formal linking is not needed.

4. **Update `wiki/index.md`**: Add the new paper to the appropriate section (主论文 or Related 论文解读). Create `index.md` if it doesn't exist yet.

   If this is the first ingest (creating a new paper folder), also set `wiki_language` in `index.md` frontmatter. Ask the human which language to use if not specified. Default to `zh-CN`.

---

**Phase 5 — Auto-Expand (discover and ingest related papers):**

After completing the main paper ingest, automatically identify up to 3 key related papers:
- Direct predecessor work
- Core comparison baseline
- Cross-domain inspiration source

For each candidate:
1. Present to the human with a brief description of why it's relevant.
2. If confirmed: download PDF to `Related/<slug>.pdf` (using the download priority chain from Phase -1).
3. Run the full ingest pipeline (Phase 0–4) for each confirmed paper, writing its reading note to `wiki/<slug>.md`.
4. **Do NOT recursively Auto-Expand** for related papers — only the main paper triggers Auto-Expand.
5. Update `wiki/index.md` with the new Related paper entries.

This is a **Confirm-tier** operation — always requires user approval before execution.

---

### Search (find papers on a topic from academic sources)

When the human wants to discover new papers on a topic, run the automated search pipeline.

**Trigger phrases:** "搜索关于X的论文", "find papers on X", "自动检索X方向的论文"

**Phase 1 — Plan search parameters:**

1. **Identify query** — Derive a concise English search query from the human's topic description (3–8 words).
2. **Identify seeds** — List any known paper names/titles in this area already in the wiki.
3. **Identify venue filter** — Default: `KDD SIGIR WWW RecSys WSDM CIKM arXiv`. Adjust if human specifies.
4. **Confirm plan with human** — Print proposed query, seeds, and venues. Wait for approval.

**Phase 2 — Execute search:**

```bash
python scripts/paper_search.py \
  --query "<derived query>" \
  --seeds "<seed paper 1>" "<seed paper 2>" \
  --venues KDD SIGIR WWW RecSys WSDM CIKM arXiv \
  --limit 30 \
  --report output/search_report.md
```

**Phase 3 — Agent review, analysis & presentation:**

After the script finishes, read `output/search_report.md` and analyze each paper:

- Skip papers already in any wiki, off-topic papers, and low-relevance Tier 3 results.
- For each remaining paper, write a structured analysis block (in wiki_language):
  ```
  ### [N] <Title>
  - 📅 Year  |  🏛 Venue  |  📊 Citations  |  🔗 [PDF](url) / no PDF
  - **主要工作：** <1-2 sentences>
  - **核心亮点：** <bullet points>
  - **与主题的关联：** <relevance>
  - **推荐优先级：** 🔴 必读 / 🟡 值得一看 / ⚪ 可选
  ```
- End with a one-paragraph synthesis.
- Ask human which papers to download.

**Phase 4 — Download selected papers:**

Download to the appropriate `Related/` directory (or create new paper folders for 🔴 必读 papers if the human wants to study them independently):

```bash
python scripts/paper_search.py \
  --query "<derived query>" \
  --download \
  --min-score 0.5 \
  --out "<Paper Folder>/Related" \
  --report output/search_report.md
```

**Phase 5 — Ingest downloaded papers** using the standard Ingest pipeline.

---

### Query (human asks a question)

1. Read `wiki/index.md` → find relevant reading notes.
2. Read relevant `wiki/*.md` pages, synthesize answer.
3. If the answer produces genuinely new cross-paper insights not already recorded, offer to update the relevant reading note's `## Critical Analysis` or `## Open Questions`.

---

### Topic Extract (extract a sub-question into a focused document)

When the human asks to extract/整理/提取 a specific sub-question from the paper's reading notes, follow these phases:

**Trigger phrases:** "帮我整理一下XXX", "提取子问题：XXX", "整理关于XXX的内容", "extract topic on XXX"

---

**Phase 1 — Understand the question:**

1. Confirm the sub-question scope with the human.
2. Determine the topic slug (kebab-case, with `topic-` prefix): e.g., `topic-constraint-force-calc`.

---

**Phase 2 — Extract and synthesize:**

1. Read all `type: source` reading notes in `wiki/`.
2. Identify relevant sections — primarily from `## Architecture`, `## Evidence`, and `## Critical Analysis`.
3. Extract and reorganize content around the sub-question's logical structure.
4. Ensure every symbol used in derivations is explicitly defined.
5. Build a coherent derivation chain, not a copy-paste collage.

---

**Phase 3 — Write topic document:**

1. Create `wiki/topic-<slug>.md` using the `templates/topic.md` template. Fill in all 4 sections:
   - `## 问题描述`: 1-3 sentences defining the sub-question
   - `## 符号定义`: Line-by-line list of all symbols used (`- $symbol$：description`)
   - `## 核心公式`: Summary of key result formulas with brief explanations, each citing source [slug, Eq.N/§N/p.N]
   - `## 关键推导`: Step-by-step derivation, reorganized for the sub-question's logic, each key step citing source [slug, Eq.N/§N/p.N]

2. Update `wiki/index.md`: Add the topic to the `## Topic 专题` section. Create the section if it doesn't exist.

---

### Chapter Reading (deep-read a chapter of a book/textbook)

When the human asks to read/analyze a specific chapter of a book-length work, follow these phases.

**Trigger phrases:** "分析第X章", "读一下第N章", "分析他的第一章", "analyze chapter N", "read chapter N", "逐章阅读", "继续读第N章", "continue chapter N"

**Applicability:** This operation is for **book-length works** (textbooks, monographs, long survey papers with distinct chapters). For regular papers (< 30 pages), use the standard Ingest operation instead.

---

**Mode branching — Explore vs. Apply:**

Before entering the reading phases, determine the current mode:

- **Explore mode** (user is in `/opsx:explore` or thinking/planning stance): Go to **Phase 0-E (Explore Preparation)**. Only read for structure (TOC, chapter boundaries), never for content.
- **OpenSpec FF/New mode** (user is creating OpenSpec artifacts for a chapter reading task): Use Phase 0-E output to help create OpenSpec `proposal.md` and `tasks.md` with batch-based tasks. Do NOT start reading.
- **OpenSpec Apply mode** (user is executing OpenSpec tasks for chapter reading): Read `tasks.md` to find the next pending batch task, execute that batch, write part file, mark task complete.
- **Apply mode** (default, no OpenSpec, user wants to directly read): Go to **Phase 0** as normal.
- **Continuation** (user says "继续读第N章"): Go to **Phase 0-C** directly.

---

**Phase 0-E — Explore preparation (explore mode only):**

This phase reads only for structure — to determine chapter boundaries and plan batches. **No content reading, no notes.** When viewing a page image to confirm boundaries, extract ONLY: chapter title, section number/title, and page number. Do NOT summarize, analyze, or interpret the chapter's subject matter, arguments, or themes from the text visible on the page. Content analysis belongs to the reading phases (Phase 0-B / Phase 1), not here.

1. **Read the book's table of contents.** Use PDF bookmarks (TOC) or `read_file` on the TOC pages to identify chapter boundaries (start/end PDF page numbers for the target chapter).

2. **Read the chapter's first page.** Extract ONLY: chapter title, first section number and title, book page number. Do not read or summarize the introductory paragraph or any body text.

3. **Read the chapter's last page** (or the page before the next chapter starts). Extract ONLY: last section number and title, book page number. Do not read or summarize problem statements or any body text.

4. **Detect if the PDF is a scanned document.** Same detection logic as Ingest Phase 0.

5. **If scanned: render ALL pages** to `temp_ch<N>/` (same as Phase 0 step 4). Skip if already rendered. This is mandatory — do NOT render only a few "preview" pages and skip the rest. The purpose is to have all pages ready for subsequent reading phases, avoiding redundant work later.

6. **Check for existing progress.** If `wiki/ch<N>-parts/` contains part files, read the last part's metadata to determine how far previous sessions got.

7. **Report to human:**
   - Chapter title and number
   - PDF page range (e.g., pages 131–165) and total page count
   - Scanned or text-layer
   - If no prior progress: estimated batch count (total pages ÷ 15, rounded up)
   - If prior progress exists: completed batches, pages read so far, remaining pages, estimated remaining batches
   - Prompt: "章节信息已确认。可使用 `/opsx:ff` 创建阅读计划，或直接开始阅读。"

8. **Stop.** Do not proceed to Phase 0-B or any reading phase.

---

**Phase 0-F — OpenSpec artifact creation (FF/New mode):**

When the user uses `/opsx:ff` or `/opsx:new` for a chapter reading task, help create OpenSpec artifacts using the information from Phase 0-E (or run Phase 0-E first if not yet done).

The **proposal** should describe:
- Which book, which chapter, chapter title
- Total pages, scanned or text-layer
- Reading strategy (batch-based for >15 scanned pages, single-session otherwise)

The **tasks** should list concrete reading batches:
```markdown
## 1. 准备

- [ ] 1.1 渲染章节页面至 temp_ch<N>/（如已渲染则跳过）

## 2. 分批阅读

- [ ] 2.1 Batch 1: page_<start> ~ page_<end>（~15页）→ 写 ch<N>-part1.md
- [ ] 2.2 Batch 2: page_<start> ~ page_<end>（~15页）→ 写 ch<N>-part2.md
- [ ] 2.3 Batch 3: page_<start> ~ page_<end>（~N页）→ 写 ch<N>-part3.md

## 3. 合并与收尾

- [ ] 3.1 合并所有 part 文件为 wiki/ch<N>-<slug>.md
- [ ] 3.2 更新 wiki/index.md
- [ ] 3.3 清理 temp_ch<N>/ 和 ch<N>-parts/
```

Batch page ranges are estimated at ~15 pages each; actual boundaries will be adjusted during apply to align with section breaks (±2 pages tolerance). When a batch finishes, update the task description with actual page range if it differs from the estimate.

**Design and specs artifacts are optional** for chapter reading tasks — the proposal and tasks are usually sufficient.

---

**Phase 0-G — OpenSpec apply (executing batch tasks):**

When the user uses `/opsx:apply` for a chapter reading change:

1. Read the change's `tasks.md` to find the next unchecked batch task.
2. Execute that batch following Phase 0-B's reading logic (read pages, extract content, write part file with metadata including `Next batch starts`).
3. After writing the part file, mark the task as complete (`- [x]`) in `tasks.md`.
4. If the actual page range differed from the estimate (due to section boundary alignment), update the task description and adjust the next batch's estimated range.
5. Report progress and stop. The next `/opsx:apply` will pick up the next batch.
6. When all batch tasks are complete, execute the merge tasks (Phase 0-D logic).

---

**Phase 0 — Locate and read the chapter:**

1. **Identify the book's PDF and existing wiki.** Read `wiki/index.md` and the main reading note to understand the book's structure (table of contents, chapter boundaries).

2. **Determine chapter page range.** The human may specify a chapter number (e.g., "第3章") or a chapter title. Map this to PDF page numbers. Account for front matter offset (e.g., book page 1 may be PDF page 14).

   If the chapter boundaries are unclear, check the table of contents or ask the human.

3. **Read all pages in the chapter.**
   - For text-layer PDFs: `read_file` on the PDF with appropriate page offsets. Read pages in batches of 2 per turn.
   - For scanned PDFs: proceed to the rendering and reading sub-steps below.

4. **Render scanned pages to a dedicated folder:**

   ```python
   import fitz, os
   doc = fitz.open(pdf_path)
   os.makedirs("temp_ch<N>", exist_ok=True)
   for i in range(start_pdf_page, end_pdf_page + 1):
       pix = doc[i].get_pixmap(dpi=200)
       pix.save(f"temp_ch<N>/page_{i+1:03d}.png")
   ```

   Replace `<N>` with the chapter number. File names use zero-padded 3-digit PDF page numbers.

   **Skip rendering** if `temp_ch<N>/` already exists and contains the expected number of PNG files (i.e., pages were pre-rendered in a prior session or manual preparation).

5. **Determine reading mode based on page count:**

   - **If total scanned pages ≤ 15:** Use **single-session mode** — read all pages via `read_file` (2 per turn), then proceed directly to Phase 1.
   - **If total scanned pages > 15:** Use **multi-session batch mode** — proceed to Phase 0-B.

---

**Phase 0-B — Multi-session batch reading (for chapters > 15 scanned pages):**

Each session reads one batch of ~15 pages and produces an intermediate part file.

1. **Determine current batch range:**
   - Check if `wiki/ch<N>-parts/` exists and contains prior part files.
   - If prior parts exist: read the last part's metadata comment to find the last processed page. Start the new batch from the next page.
   - If no prior parts exist: start from the chapter's first page.
   - Each batch targets ~15 pages, but **prefer splitting at section boundaries** (±2 pages tolerance). If a new section title is visible within 2 pages of the 15-page mark, extend or shorten the batch to align.

   When ending a batch, determine the `Next batch starts` value:
   - Identify the page and section where the next batch should begin (typically the first page after the batch's last covered section, or the start of a new section that was deferred to keep it intact).
   - Record as `<!-- Next batch starts: page_NNN.png, §X.Y Section Title -->`.
   - If this batch covers the chapter's last page, record `<!-- Next batch starts: none (chapter complete) -->` instead.

2. **Read the batch pages:**
   - Use `read_file` on each PNG in the batch (2 per turn).
   - Extract content according to Phase 1's analysis framework (concepts, symbols, arguments, examples).

3. **Write intermediate part file:**

   Create `wiki/ch<N>-parts/ch<N>-part<M>.md` (where M is the batch sequence number, starting from 1):

   ```markdown
   <!-- Part M of Chapter N -->
   <!-- Pages: page_060.png ~ page_073.png (book pp.48-61) -->
   <!-- Sections covered: §3.1, §3.2 (partial) -->
   <!-- Continues from previous: no | yes, §X.Y -->
   <!-- Next batch starts: page_074.png, §3.3 Section Title -->

   ## 概念定义

   **<English Term>（<中文译名>）** [p.<page>]
   > <Original English definition quoted from the text.>
   >
   > <Chinese translation of the definition.>

   ---

   ## 符号定义

   ### <Context Group>

   | 符号 | 类型 | 含义 |
   |------|------|------|
   | $symbol$ | type | meaning |

   ## 核心论点

   ### §X.Y <Section Title>

   <Content: prose, key arguments, equations, comparisons>

   ## 工程应用与实例

   | 图号/例题号 | 名称 | 类型 | 应用 | 关键知识点 |
   |------------|------|------|------|-----------|
   | | | | | |
   ```

   The part file uses the same section structure as the final chapter-notes template, but **omits** YAML frontmatter, `## 章节定位`, and `## 与全书的关系` (these require full-chapter perspective and are written during merge).

4. **Report progress to human:**
   - Pages processed in this batch
   - Total progress: "Part M done. Covered pages X-Y. Remaining: ~Z pages (~K more sessions)."
   - If all pages are now covered: "All pages read. Ready for merge — run '继续读第N章' or 'continue chapter N' to trigger merge."

---

**Phase 0-C — Cross-session continuation:**

When the human triggers Chapter Reading for a chapter that already has intermediate parts (e.g., "继续读第3章"):

1. **Detect state:**
   - Check `wiki/ch<N>-parts/` for existing part files.
   - Read the last part's metadata. Look for the `<!-- Next batch starts: ... -->` line:
     - If present and value is `none (chapter complete)` → all pages are covered, proceed to Phase 0-D (merge).
     - If present with a page reference (e.g., `page_074.png, §3.3 Section Title`) → use that page as the starting point for the next batch. Proceed to Phase 0-B.
     - If the `Next batch starts` line is absent (legacy part file) → fall back to reading the last part's page range metadata, compute last page + 1 as the starting point. Compare against `temp_ch<N>/` to know remaining pages.

2. **Route to appropriate action:**
   - If unread pages remain → proceed to Phase 0-B (create next batch).
   - If all pages are covered → proceed to Phase 0-D (merge).

---

**Phase 0-D — Merge session (all parts complete):**

When all chapter pages have been covered by part files:

1. **Read all part files** in `wiki/ch<N>-parts/` in sequence order (part1, part2, ...). These are pure text, so context usage is minimal compared to images.

2. **Merge into final chapter note** (`wiki/ch<N>-<slug>.md`):
   - Write complete YAML frontmatter (type, parent, chapter, title, pages, sections, dates).
   - Write `## 章节定位` — synthesize from full-chapter perspective.
   - Merge all `## 概念定义` entries: sort by page number, deduplicate any concepts that appear at part boundaries.
   - Merge all `## 符号定义` tables: combine, deduplicate, group logically.
   - Integrate all `## 核心论点` sections: reorganize into a logically coherent structure following the chapter's section order.
   - Merge all `## 工程应用与实例` tables into one.
   - Write `## 与全书的关系` — map concepts to other chapters.

3. **Update `wiki/index.md`**: Add the chapter note entry.

4. **Cleanup** (after human confirms the final note is satisfactory):
   - Delete `<Book-Folder>/temp_ch<N>/` folder (pre-rendered PNG images).
   - Delete `wiki/ch<N>-parts/` folder (intermediate part files).

---

**Phase 1 — Analyze the chapter:**

Extract the following from the chapter text:

1. **章节定位 (Chapter Positioning):**
   - What is this chapter's role in the book? (introduction, theory, application, etc.)
   - What does it cover? What does it NOT cover?
   - What prerequisites are assumed?

2. **概念定义 (Concept Definitions):**
   - Extract ALL concept definitions introduced in this chapter.
   - For each concept, capture:
     - The English term and its Chinese translation
     - The page number where it's defined
     - The original English definition (quote from the text)
     - A Chinese translation of the definition
   - Include both formal definitions and important informal ones.

3. **符号定义 (Symbol Definitions):**
   - Extract ALL mathematical/physical symbols introduced.
   - For each symbol: its notation, type (scalar/vector/matrix/point), and meaning.
   - Group symbols by context (figure, section, method).
   - Note whether symbols are formal (used throughout the book) or informal (example-only).

4. **核心论点 (Key Arguments):**
   - Main arguments, comparisons, and conclusions.
   - Side-by-side comparisons (use tables).
   - Classifications and taxonomies.

5. **工程应用与实例 (Engineering Examples):**
   - Worked examples, engineering applications, case studies.
   - For each: figure reference, name, type, application, key takeaway.

6. **与全书的关系 (Relation to Other Chapters):**
   - How concepts introduced here are developed in later chapters.
   - Prerequisites from earlier chapters.

---

**Phase 2 — Report to human:**

Present a structured summary of the chapter analysis before writing:
- Chapter positioning (1-2 sentences)
- Number of concept definitions found
- Number of symbol definitions found
- Key arguments summary
- List of engineering examples

Wait for human confirmation or corrections before writing.

---

**Phase 3 — Write chapter notes:**

1. **Create `wiki/ch<N>-<slug>.md`** using the `templates/chapter.md` template. Fill in all 6 sections based on Phase 1 analysis.

   Filename convention: `ch<N>-<slug>.md` where `<N>` is the chapter number and `<slug>` is a kebab-case abbreviation of the chapter title.

   Examples:
   - `ch1-elements-of-cakd.md`
   - `ch3-planar-cartesian-kinematics.md`
   - `ch6-planar-dynamics.md`

2. **Concept definitions** must follow the standard format — every concept gets:
   - English term with Chinese translation in parentheses
   - Page citation in brackets
   - Blockquote with original English text
   - Blockquote with Chinese translation
   - Separated by `---` between concepts

3. **Symbol definitions** use table format grouped by context. Note if symbols are formal or example-only.

4. **Update `wiki/index.md`**: Add the chapter note to the `### 逐章精读笔记` sub-section under `## Topic 专题`. Create the sub-section if it doesn't exist.

   Format:
   ```markdown
   ### 逐章精读笔记
   - [Ch.1 <Title>](ch1-<slug>.md) — <one-line summary>
   - [Ch.3 <Title>](ch3-<slug>.md) — <one-line summary>
   ```

---

### Lint (health check)

Check for consistency within a paper folder's `wiki/`:

- `pdf_path` in each reading note points to an existing PDF file
- `![...](figures/...)` image paths resolve to existing files
- `wiki/index.md` lists all `.md` files in `wiki/` (excluding itself)
- `wiki/index.md` does not list papers that have no corresponding `.md` file
- `Related/` contains only `.pdf` files (no subdirectories)
- No orphan figures directories (figures dir exists but corresponding reading note doesn't)
- Cross-references between reading notes within the same `wiki/` resolve correctly

When structural issues are detected during any operation:
- Auto-fixable issues (broken paths, missing index entries) → fix immediately
- Semantic issues (contradictions, stale claims) → report to human

## Conventions

- **Wiki language**: Configured in `wiki/index.md` frontmatter as `wiki_language` (e.g., `en`, `zh-CN`, `zh-TW`, `ja`). All reading note body content MUST be written in the configured language. Language-invariant elements remain in English: YAML field names, section headings (`## Essence`, `## Factors`, etc.), formatting labels (`**Insight**:`, `*Prior*:`, etc.), kebab-case slugs, and tag names.
- Page filenames use kebab-case slugs: `attention-is-all-you-need.md`
- **Topic filenames** use `topic-` prefix: `topic-constraint-force-calc.md` — this distinguishes topic documents from source reading notes at a glance
- **Chapter note filenames** use `ch<N>-` prefix: `ch1-elements-of-cakd.md`, `ch3-planar-kinematics.md` — this distinguishes chapter notes at a glance and preserves chapter ordering
- All dates use ISO format: `2026-04-06`
- Domain tags use kebab-case: `multibody-dynamics`
- Standard markdown only — no Obsidian wikilinks (`[[...]]`), no `![[...]]` image embeds
- Image embeds use standard markdown: `![alt](relative/path.png)`
- Cross-references within the same `wiki/` use markdown links: `[text](slug.md)` or plain text

## Bootstrapping a New Paper Folder

When the human provides a paper to read for the first time:

1. **Determine the paper title** from the PDF, URL, or human input.
2. **Ask the human** which language the reading notes should use (default: `zh-CN`).
3. **Create directory structure**:
   ```
   <Paper Title>/
   ├── <paper>.pdf
   ├── wiki/
   │   ├── index.md
   │   └── figures/
   └── Related/
   ```
4. **Create `wiki/index.md`** with language configuration in frontmatter.
5. Proceed with Ingest Phase 0.
