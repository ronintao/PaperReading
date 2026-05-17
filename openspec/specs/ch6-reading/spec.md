## ADDED Requirements

### Requirement: Batch reading of scanned chapter pages
系统 SHALL 将 Chapter 6 的 44 页扫描 PNG（temp_ch6/page_211.png ~ page_254.png）分 3 批读取，每批 ~15 页，批次边界 SHALL 对齐小节分界（±2 页容差）。

#### Scenario: First batch reading
- **WHEN** 执行 Batch 1 任务
- **THEN** 读取 page_211.png ~ page_225.png（约 15 页），生成 `wiki/ch6-parts/ch6-part1.md`，包含概念定义、符号定义、核心论点、工程应用与实例，并在元数据中记录 `Next batch starts`

#### Scenario: Batch boundary alignment
- **WHEN** 批次的第 15 页附近（±2 页）出现新小节标题
- **THEN** SHALL 调整批次边界对齐该小节分界，并更新后续批次的预估范围

### Requirement: Part file format compliance
每个 part 文件 SHALL 遵循 paper-reading skill 的中间 part 文件格式，包含元数据注释和四个正文节。

#### Scenario: Part file metadata
- **WHEN** 生成 part 文件
- **THEN** 文件顶部 SHALL 包含 `<!-- Part M of Chapter N -->`、`<!-- Pages: ... -->`、`<!-- Sections covered: ... -->`、`<!-- Continues from previous: ... -->`、`<!-- Next batch starts: ... -->` 五行元数据

#### Scenario: Part file body sections
- **WHEN** 生成 part 文件
- **THEN** 文件 SHALL 包含 `## 概念定义`、`## 符号定义`、`## 核心论点`、`## 工程应用与实例` 四个节

### Requirement: Merge into final chapter note
全部批次完成后，SHALL 将所有 part 文件合并为 `wiki/ch6-planar-dynamics.md`，遵循 chapter-notes 模板格式。

#### Scenario: Successful merge
- **WHEN** 所有 3 个 part 文件已完成（最后一个 part 的 `Next batch starts` 为 `none (chapter complete)`）
- **THEN** 合并生成 `wiki/ch6-planar-dynamics.md`，包含完整 YAML frontmatter 和六个正文节（章节定位、概念定义、符号定义、核心论点、工程应用与实例、与全书的关系）

#### Scenario: Deduplication during merge
- **WHEN** 同一概念或符号在多个 part 文件中出现（跨批次边界）
- **THEN** 合并时 SHALL 去重，保留最完整的定义

### Requirement: Index update
合并完成后 SHALL 更新 `wiki/index.md`。

#### Scenario: Add chapter entry to index
- **WHEN** `wiki/ch6-planar-dynamics.md` 已生成
- **THEN** 在 `wiki/index.md` 的 `### 逐章精读笔记` 节中添加 Ch.6 条目

### Requirement: Cleanup temporary files
合并并经人工确认后 SHALL 清理临时文件。

#### Scenario: Cleanup after confirmation
- **WHEN** 人工确认最终笔记满意
- **THEN** 删除 `temp_ch6/` 文件夹和 `wiki/ch6-parts/` 文件夹
