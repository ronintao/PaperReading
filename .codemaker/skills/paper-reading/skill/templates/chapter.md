---
type: chapter-notes
parent: <parent-source-slug>
chapter: <chapter-number>
title: "<Chapter Title>"
pages: <start-page>-<end-page>
sections:
  - "<section-number> <Section Title>"
  - "<section-number> <Section Title>"
created: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
---

<!-- CHAPTER NOTES TEMPLATE
     For book-length works (textbooks, monographs) that require chapter-by-chapter reading.
     Each chapter note captures: positioning, concept definitions, symbol definitions,
     key arguments, engineering examples, and cross-references to the full book.

     FORMATTING CONVENTIONS:
     - Concept definitions: English term + Chinese translation + page citation + original quote + translation
     - Symbol definitions: table format with symbol, type, and meaning columns
     - Bold key terms on first mention within each section
     - Use > blockquote for original text citations from the book -->

# Chapter <N>: <Chapter Title>

## 章节定位

{2-5 sentences describing this chapter's role within the book. What is its purpose? What does it cover? What does it NOT cover? What prerequisite knowledge is assumed?}

---

## 概念定义

{Extract ALL concept definitions introduced in this chapter. Each definition follows this format:}

**<English Term>（<中文译名>）** [p.<page>]
> <Original English definition quoted from the text.>
>
> <Chinese translation of the definition.>

{Add clarifying notes below a definition if needed:}
{**特征/条件/备注**：supplementary explanation.}

---

{Repeat for each concept. Separate with `---` between concepts.}

---

## 符号定义

{Extract ALL mathematical/physical symbols introduced in this chapter.
 If the chapter introduces only informal/example symbols (not the book's formal system),
 note this with a callout:}

> [!note]
> {e.g., "本章符号为示例性引入，全书正式符号体系从第N章开始建立。"}

{Group symbols by context (e.g., by figure, by sub-section, by method).
 Use table format:}

### <Context Group Name>

| 符号 | 类型 | 含义 |
|------|------|------|
| $<symbol>$ | <type: 标量/向量/矩阵/点/...> | <description> |

{Add conditions or relationships below a table if needed:}
> **条件/关系**：<description>

---

## 核心论点

{Extract the chapter's main arguments, comparisons, and conclusions.
 Organize into logical sub-sections using H3.
 Use tables for side-by-side comparisons.
 Use bullet lists for enumerations.
 Bold key terms and conclusions.}

### <Argument/Comparison Title>

{Content: prose, tables, or structured comparisons.}

---

## 工程应用与实例

{If the chapter includes worked examples, engineering applications, or case studies,
 summarize them here. Use table format for multiple examples:}

| 图号/例题号 | 名称 | 类型 | 应用 | 关键知识点 |
|------------|------|------|------|-----------|
| | | | | |

{If the chapter has no examples, replace this section with:}
{本章无工程实例。}

---

## 与全书的关系

{Map this chapter's content to other chapters in the book.
 Show where concepts introduced here are developed further.}

| 本章概念 | 后续展开位置 |
|----------|------------|
| <concept> | Ch.N（<description>） |
