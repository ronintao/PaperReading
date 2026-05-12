## Why

现有的 paper-wiki skill 定位为"LLM 维护的知识库"，围绕 topics/milestones 构建跨论文知识图谱，依赖 Obsidian wikilinks、journal 审计日志、Three-Tree Mirroring 等重型机制。实际使用中，核心需求是**逐篇论文的阅读与解读**，不需要全局知识图谱和运维开销。需要将 skill 从"知识库维护者"转型为"论文阅读解读助手"。

## What Changes

- **BREAKING** Skill 改名：`paper-wiki` → `paper-reading`，更新 description 和触发词
- **BREAKING** 文件夹结构重设计：从 `raw/` + `kb/` 两级结构改为以论文标题为文件夹、内含 `wiki/` + `Related/` 的扁平结构
- 砍掉 topics/milestone 体系：删除 `topics/`、Milestone Hierarchy、Consolidation/Promotion Rule、Three-Tree Mirroring、Classification Fitness Check
- 砍掉运维机制：删除 `journal/`、`log.md`、Proactive Write-back dual-write 规则
- 砍掉 Obsidian 相关规则：删除 wikilink 规则、Graph View hygiene、Properties Conventions
- 解读页 sections 瘦身：删除 `## Feeds`、`## Cognitive Shifts`；保留 Essence、Factors、Architecture、Evidence、Critical Analysis、Relations、Transferable Inspirations、Open Questions
- YAML frontmatter 瘦身：删除 `milestone`，`raw_path` 改为 `pdf_path`（相对路径）
- 新增 Sci-Hub 下载：通过搜索引擎动态发现 Sci-Hub 镜像，尝试前 5 个链接，作为 arXiv/Semantic Scholar 之后的兜底下载方案
- 新增扫描件 PDF 支持：检测无文本层 PDF → PyMuPDF 逐页渲染为图片 → LLM 视觉直读
- 调整 Auto-Expand：Related 论文 PDF 下载到 `Related/`，解读写到 `wiki/`
- 调整图片提取路径：输出到 `wiki/figures/<slug>/`

## Capabilities

### New Capabilities
- `paper-folder-structure`: 以论文标题为文件夹的新目录组织方式，包含 `wiki/`、`Related/`、`wiki/figures/<slug>/` 子目录
- `scihub-download`: 通过搜索引擎动态发现 Sci-Hub 镜像并下载论文 PDF 的能力
- `scanned-pdf-reading`: 检测扫描件 PDF 并通过 PyMuPDF 渲染图片 + LLM 视觉直读的能力

### Modified Capabilities

（无已有 specs 需要修改——这是全新的 skill 重构）

## Impact

- **文件变更**：`.codemaker/skills/paper-wiki/` 整个目录重命名为 `.codemaker/skills/paper-reading/`，SKILL.md 大幅重写，`templates/paper.md` 瘦身，`templates/topic.md` 和 `templates/journal.md` 删除
- **现有数据**：`Constraint Reaction Forces and Lagrange Multipliers in Multi-Body Systems/` 文件夹需要迁移到新结构
- **依赖**：PyMuPDF (fitz) 已有依赖，无新增外部依赖
- **脚本**：`paper_extract_figures.py` 输出路径调整；`paper_search.py` 下载目标路径调整
