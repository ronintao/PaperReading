---
type: source
id: <slug>
pdf_path: ../<slug>.pdf  # Relative to wiki/ — use ../Related/<slug>.pdf for Related papers
url: <https://arxiv.org/abs/XXXX.XXXXX>  # Permanent external URL (arXiv, conference, DOI)
tags:
  - <domain>
  - year/<YYYY-MM>  # Publication date from arXiv/conference/journal (e.g. year/2025-03)
  - venue/<venue-name>  # Publishing venue (e.g. venue/NeurIPS, venue/ICML, venue/Nature, venue/arXiv-preprint)
created: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
authors:
  - <author name>
aliases:
  - <human-readable paper title>
---

<!-- FORMATTING CONVENTIONS (apply to all reading note body content):
     Structural: **Bold key labels** in structured entries, *italic sub-field labels* as nested bullets.
     Relations: single-line — "- **source-slug** (*type*): delta text"
     Figure interpretations: blockquote below image (> interpretation)
     Cross-references: use standard markdown [text](slug.md) or plain text slugs.
     
     INLINE BOLDING (most important rule):
     Within every content field, **bold the core phrase** a scanning reader should catch.
     One bold span per sentence/bullet — target key finding, mechanism, or shift.
     Applies to: Essence, Factors, Critical Analysis, Relations, Figures, Inspirations. -->

## Essence

> [!abstract]
> **One-Sentence Summarization**: ""
> **Contribution**: "" (**bold** the core novelty within the sentence)
> (Derived from comparison — what specifically is new given the field's prior art?)

## Factors

<!-- (Author Claims from Introduction)
     Reflects ONLY what the authors claim in their Introduction — not our analysis.
     FORMATTING: Bold key terms, system names, and technical concepts for scannability. -->

### Context
{2-3 sentences. **Bold** the core research problem and key technical terms.}

### Related Work
<!-- Bold the system/paper name, then describe. -->
- **Name**: description
- **Name**: description

### Gap
{2-3 sentences. **Bold** the specific limitation that motivates this work.}

### Proposal
{2-3 sentences. **Bold** the method name and **bold** the key insight/mechanism.}

## Architecture

<!-- MANDATORY for any paper with non-trivial architecture.
     This section is the technical heart of the reading note — it must be written from
     full-text reading, not from the abstract. Aim for 80–150 lines total.

     REQUIRED sub-sections (use H3):
     1. "整体结构：Figure N 精读" — for each key figure:
        - Embed the image: ![alt](figures/<slug>/figure_N.png)
        - Follow immediately with an ASCII block diagram (``` code block ```) showing
          data flow: input → module → module → output. Label each box/arrow.
        - Then prose-describe each module and its role.
     2. One H3 per major sub-module (e.g., "### Attention Mechanism", "### MoE Branch"):
        - State the module's purpose in one sentence.
        - Give the defining formula in LaTeX block ($$...$$).
        - Use a > [!note] callout to explain the design motivation ("为什么这样设计").
     3. "### 训练目标" (Training Objective) — if applicable:
        - Full loss function formula ($$...$$) with every term explained.
        - Note any auxiliary losses and their coefficients.

     FORMATTING:
     - ASCII diagrams use ``` (fenced code block), NOT indented code.
     - LaTeX formulas: inline $...$ for variables, block $$...$$ for equations.
     - > [!note] callout explains WHY (design motivation), not WHAT (already in prose).
     - **Bold** each sub-module name on first mention.
     - Image paths are relative to wiki/: figures/<slug>/figure_N.png -->

### 整体结构：Figure 1 精读

![<descriptive-alt>](figures/<slug>/figure_1.png)

{One paragraph describing what Figure 1 shows at a high level.}

```
{ASCII data-flow diagram of the overall architecture}
输入 → [Module A] → [Module B] → 输出
```

{Prose walkthrough of each major component visible in the figure.}

### <Sub-module Name>

{One sentence: what this module does and why it exists.}

$$\text{formula}(x) = \ldots$$

> [!note] 为什么这样设计？
> {Design motivation — **bold the key insight**. Reference prior work if applicable.}

## Evidence

| 实验项 | 方法 | 结果 |
|--------|------|------|
| | | |

## Critical Analysis

### Novel Insight
<!-- What we didn't know before this paper. Each entry MUST be contrastive:
     state what the wiki's prior understanding was, then what this paper changes.
     Test: "Would a senior researcher cite this in their own paper's motivation?"
     Anti-pattern: restating the paper's claims. This must be YOUR derived insight. -->

- **Insight**: <sentence with **core finding bolded** for scanning>
  - *Prior*: <what was believed before>
  - *Update*: <how understanding changes — **bold the specific shift**>

### Fundamental Limitations
<!-- NOT "the paper didn't test enough models." These are limitations of the APPROACH
     or PROBLEM FORMULATION that affect the entire research direction.
     Test: "Would solving this limitation be a publishable contribution?" -->

- **Limitation**: <sentence with **core difficulty bolded**>
  - *Root cause*: <why this is hard — **bold the mechanism**>
  - *Also affects*: <other affected work>
  - *Implication*: <consequence — **bold the key takeaway**>

### Research Frontier
<!-- Concrete next-step problems that this paper makes tractable or newly visible.
     Test: "Could someone write a paper abstract starting from this direction?" -->

- **Direction**: <sentence with **the opportunity bolded**>
  - *Prerequisite*: <what needs to exist first>
  - *Closest attempt*: <who tried what> but **<gap remains>**

## Relations

<!-- Temporal Context: 1-3 sentences positioning this paper in its evolutionary chain(s).
     Reference specific papers with dates (YYYY-MM).
     Use standard markdown links [slug](slug.md) for papers in the same wiki/,
     or plain text for external papers not in this wiki. -->

**Temporal context:** <1-3 sentences positioning this paper in evolutionary chain(s).
Include chain notation where applicable: predecessor(date) → **this-paper(date)** → successor(date).>

- **source-slug** (*builds_on*): <delta — **bold the key difference**>

## Transferable Inspirations

- 

## Open Questions

- 
