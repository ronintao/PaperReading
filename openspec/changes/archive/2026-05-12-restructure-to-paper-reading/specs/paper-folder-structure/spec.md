## ADDED Requirements

### Requirement: Paper folder as organizational unit
每篇被阅读的论文 SHALL 拥有一个以论文标题命名的顶层文件夹，作为该论文所有内容的唯一容器。

#### Scenario: New paper ingest creates folder structure
- **WHEN** 用户要求阅读一篇新论文
- **THEN** 系统创建 `<论文标题>/` 文件夹，内含 `wiki/`、`wiki/figures/`、`Related/` 三个子目录，并将主论文 PDF 放在文件夹根目录

#### Scenario: Folder naming convention
- **WHEN** 创建论文文件夹时
- **THEN** 文件夹名 SHALL 使用论文的完整标题（允许适当缩写过长标题），不使用 kebab-case slug

### Requirement: Wiki directory for reading notes
论文文件夹内的 `wiki/` 目录 SHALL 存放该论文及其 Related 论文的所有解读 markdown 文件。

#### Scenario: Main paper reading note
- **WHEN** 完成主论文的解读
- **THEN** 在 `wiki/` 下创建 `<main-slug>.md`，包含 8 个标准 sections：Essence, Factors, Architecture, Evidence, Critical Analysis, Relations, Transferable Inspirations, Open Questions

#### Scenario: Related paper reading note
- **WHEN** 完成一篇 Related 论文的解读
- **THEN** 在 `wiki/` 下创建 `<related-slug>.md`，使用与主论文相同的 8 sections 规格

#### Scenario: Wiki index as navigation entry
- **WHEN** 论文文件夹的 wiki/ 创建或更新时
- **THEN** `wiki/index.md` SHALL 存在并列出所有已解读的论文（主论文和 Related），包含 slug、作者、年份、出处

### Requirement: Related directory for reference PDFs only
`Related/` 目录 SHALL 仅存放相关论文的 PDF 文件，不包含任何解读内容或子目录。

#### Scenario: Auto-Expand downloads to Related
- **WHEN** Auto-Expand 推荐的 Related 论文被确认下载
- **THEN** PDF 下载到 `Related/<slug>.pdf`

#### Scenario: No nested structure in Related
- **WHEN** 检查 `Related/` 目录
- **THEN** SHALL 只包含 `.pdf` 文件，不包含任何子目录

### Requirement: Figures organized by paper slug
从 PDF 提取的图片 SHALL 按论文 slug 分子目录存放在 `wiki/figures/` 下。

#### Scenario: Extract figures for main paper
- **WHEN** 提取主论文的图片
- **THEN** 图片保存到 `wiki/figures/<main-slug>/figure_N.png`

#### Scenario: Extract figures for related paper
- **WHEN** 提取 Related 论文的图片
- **THEN** 图片保存到 `wiki/figures/<related-slug>/figure_N.png`

#### Scenario: Image reference path in reading notes
- **WHEN** 解读页引用论文图片
- **THEN** 使用相对路径 `figures/<slug>/figure_N.png`

### Requirement: Simplified YAML frontmatter
解读页的 YAML frontmatter SHALL 使用瘦身后的字段集。

#### Scenario: Main paper frontmatter
- **WHEN** 创建主论文解读页
- **THEN** YAML 包含 `type: source`、`id`、`pdf_path: ../<slug>.pdf`、`tags`、`created`、`last_updated`、`authors`、`aliases`，不包含 `milestone` 或 `raw_path`

#### Scenario: Related paper frontmatter
- **WHEN** 创建 Related 论文解读页
- **THEN** YAML 的 `pdf_path` SHALL 为 `../Related/<slug>.pdf`

### Requirement: No topics, journal, or log
新结构 SHALL NOT 包含 `topics/`、`journal/`、`log.md` 或 `index.md`（全局级别）。

#### Scenario: Ingest does not create topic or journal files
- **WHEN** 完成一篇论文的完整 ingest
- **THEN** 不创建任何 topic 文件、journal 文件或 log.md

### Requirement: Standard markdown only
所有解读页 SHALL 使用标准 markdown 语法，不使用 Obsidian wikilinks。

#### Scenario: Cross-reference between papers
- **WHEN** 解读页引用同一 wiki/ 下的另一篇论文
- **THEN** 使用标准 markdown 链接 `[text](filename.md)` 或纯文本 slug，不使用 `[[wikilink]]`
