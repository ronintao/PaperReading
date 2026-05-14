## MODIFIED Requirements

### Requirement: Produce intermediate part files per batch
每次分批阅读会话 SHALL 产出一个结构化中间产物文件。

#### Scenario: Part file location and naming
- **WHEN** 完成一批页面的阅读
- **THEN** 写入 `wiki/ch<N>-parts/ch<N>-part<M>.md`，其中 M 为批次序号（从 1 开始）

#### Scenario: Part file metadata header
- **WHEN** 创建 part 文件
- **THEN** 文件开头 SHALL 包含 HTML 注释形式的元信息：Part 序号、页面范围（文件名）、书中页码范围、覆盖的 section 编号，以及 `Next batch starts` 字段指明下一批次的起始页码和对应 section 信息

#### Scenario: Next batch starts field format
- **WHEN** 写入 part 文件 metadata
- **THEN** SHALL 包含一行 `<!-- Next batch starts: page_NNN.png, §X.Y Section Title -->`，其中 page_NNN.png 为下一批次的起始页面文件名，§X.Y Section Title 为该页面所属或开始的 section

#### Scenario: Last batch omits next batch field
- **WHEN** 当前批次已覆盖章节的最后一页
- **THEN** 使用 `<!-- Next batch starts: none (chapter complete) -->` 表示章节阅读完毕

#### Scenario: Part file content structure
- **WHEN** 写入 part 文件内容
- **THEN** SHALL 使用与最终 chapter-notes 模板相同的 section 结构（`## 概念定义`、`## 符号定义`、`## 核心论点`、`## 工程应用与实例`），但省略 YAML frontmatter、`## 章节定位`和`## 与全书的关系`

### Requirement: Cross-session continuation
系统 SHALL 支持跨会话续接，自动检测上次读到的位置。

#### Scenario: Detect existing parts and determine next batch via metadata
- **WHEN** 用户在新会话中触发 Chapter Reading（如"继续读第3章"）且 `wiki/ch<N>-parts/` 中有 part 文件
- **THEN** 系统读取最后一个 part 文件的 `Next batch starts` 字段，以该字段指定的页码为下一批次的起始页

#### Scenario: Fallback when Next batch starts field is absent
- **WHEN** 最后一个 part 文件不包含 `Next batch starts` 字段（旧格式 part 文件）
- **THEN** 系统回退到现有逻辑：从最后一个 part 的末页页码 + 1 开始

#### Scenario: All pages covered triggers merge
- **WHEN** 最后一个 part 的 `Next batch starts` 字段为 `none (chapter complete)`，或检测到已有 parts 覆盖了章节所有页面
- **THEN** 自动进入合并流程，不再创建新的 part 文件
