## 1. 创建新 Skill 目录结构

- [x] 1.1 创建 `.codemaker/skills/paper-reading/skill/` 目录结构（含 `templates/`）
- [x] 1.2 从 `paper-wiki` 复制 `scripts/paper_extract_figures.py` 到 `paper-reading/scripts/`，调整输出路径参数使其支持 `wiki/figures/<slug>/` 目标路径
- [x] 1.3 从 `paper-wiki` 复制 `scripts/paper_search.py` 到 `paper-reading/scripts/`，调整 `--out` 默认路径参数

## 2. 重写 SKILL.md

- [x] 2.1 编写新的 frontmatter：`name: paper-reading`，更新 description 和触发词（去掉 wiki/Obsidian 相关，增加 paper reading/论文阅读 相关）
- [x] 2.2 编写新的 Architecture 章节：描述以论文标题为文件夹、内含 `wiki/` + `Related/` + `wiki/figures/` 的目录结构（替代 `raw/` + `kb/` + Three-Tree Mirroring）
- [x] 2.3 编写新的 Page Formats 章节：描述解读页 8 sections（Essence → Open Questions）、标准 markdown（无 wikilinks）、瘦身后的 YAML frontmatter
- [x] 2.4 编写新的 Ingest 操作流程：Phase -1（Paper Acquisition，含 Sci-Hub 动态发现）→ Phase 0（Full-Text Reading，含扫描件检测与视觉直读）→ Phase 1-2（分析与汇报）→ Phase 3（图片提取到 `wiki/figures/<slug>/`）→ Phase 4（写解读页到 `wiki/`，更新 `wiki/index.md`）→ Phase 5（Auto-Expand，下载到 `Related/`）
- [x] 2.5 编写新的 Search 操作流程：调整下载目标路径为 `Related/`
- [x] 2.6 编写新的 Query 操作流程：简化为读 `wiki/index.md` → 读 `wiki/*.md` → 综合回答
- [x] 2.7 编写新的 Lint 操作：简化为 wiki/ 内部一致性检查（pdf_path 指向存在的文件、figures 路径有效、index.md 与实际 md 文件一致）
- [x] 2.8 编写 Conventions 章节：保留 wiki_language、kebab-case slug、ISO 日期等，删除 Obsidian/wikilink/Graph View 相关规则

## 3. 更新模板文件

- [x] 3.1 重写 `templates/paper.md`：更新 YAML frontmatter（`pdf_path` 替代 `raw_path`，删除 `milestone`），body 保留 8 sections，删除 Feeds 和 Cognitive Shifts，图片引用改为 `figures/<slug>/figure_N.png`
- [x] 3.2 删除 `templates/topic.md`（不再需要 topic 模板）
- [x] 3.3 删除 `templates/journal.md`（不再需要 journal 模板）

## 4. Sci-Hub 下载能力

- [x] 4.1 在 SKILL.md 的 Phase -1 中编写 Sci-Hub 动态发现流程：搜索引擎搜 "sci-hub" → 提取前 5 个候选 URL → 依次尝试 `<url>/<DOI>` → 验证 PDF（>1KB + %PDF 文件头）
- [x] 4.2 在 SKILL.md 的 Phase -1 中编写 DOI 直接输入支持：用户提供 `10.xxxx/...` 格式 DOI → S2 openAccessPdf → Sci-Hub fallback
- [x] 4.3 在 SKILL.md 的 Phase -1 中更新完整下载优先级链：arXiv → S2 openAccessPdf → Sci-Hub → 手动

## 5. 扫描件 PDF 支持

- [x] 5.1 在 SKILL.md 的 Phase 0 中编写扫描件检测逻辑：PyMuPDF `page.get_text()` 文本量 < 50 字符阈值判定
- [x] 5.2 在 SKILL.md 的 Phase 0 中编写渲染流程：`page.get_pixmap(dpi=200)` → PNG → read_file 逐页视觉读取
- [x] 5.3 在 SKILL.md 的 Phase 0 中编写临时文件清理规则：解读完成后删除渲染图片

## 6. 迁移现有数据

- [x] 6.1 将 `Constraint Reaction Forces.../sources/` 下的 md 文件移动到 `wiki/` 下，更新 YAML frontmatter（删除 milestone，raw_path → pdf_path）
- [x] 6.2 将 `IntermediateDynamics.pdf` 移动到 `Related/`
- [x] 6.3 重写 `wiki/index.md` 为新格式（导航入口，列出主论文和 Related 解读）
- [x] 6.4 更新解读页中的图片引用路径为 `figures/<slug>/figure_N.png`
- [x] 6.5 删除旧的 `topics/`、`journal/`（空）、`log.md`、`sources/` 目录
- [x] 6.6 删除解读页中的 `## Feeds` 和 `## Cognitive Shifts` sections，将 `[[wikilinks]]` 替换为标准 markdown 链接或纯文本

## 7. 清理与验证

- [x] 7.1 删除旧的 `.codemaker/skills/paper-wiki/` 目录
- [x] 7.2 验证新 skill 的 SKILL.md 能被 CodeMaker 正确加载（检查 frontmatter 格式）
- [x] 7.3 验证迁移后的论文文件夹结构符合新设计（wiki/、Related/、figures/ 齐全，无残留旧文件）
