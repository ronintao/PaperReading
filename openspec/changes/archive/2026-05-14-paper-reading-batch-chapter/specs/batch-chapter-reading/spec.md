## ADDED Requirements

### Requirement: Detect large chapter requiring multi-session reading
系统 SHALL 在 Chapter Reading Phase 0 中检测扫描章节的页面数量，若超过 15 页则自动进入多会话分批模式。

#### Scenario: Small chapter stays single-session
- **WHEN** 扫描章节总页面数 ≤ 15
- **THEN** 使用现有单会话流程完成阅读，不创建中间产物

#### Scenario: Large chapter triggers batch mode
- **WHEN** 扫描章节总页面数 > 15
- **THEN** 进入多会话分批模式，每批处理约 15 页（按 section 边界 ±2 页容差对齐）

### Requirement: Pre-render all chapter pages upfront
系统 SHALL 在首次会话中一次性渲染整章所有扫描页面为 PNG 图片，存入专用文件夹。

#### Scenario: Render to dedicated temp folder
- **WHEN** 开始大章节阅读的首次会话
- **THEN** 使用 PyMuPDF 以 dpi=200 渲染章节所有页面，保存为 `<Book-Folder>/temp_ch<N>/page_<NNN>.png`，其中 NNN 为 PDF 页码（零填充三位）

#### Scenario: Skip rendering if temp folder already exists
- **WHEN** `temp_ch<N>/` 文件夹已存在且包含预期数量的 PNG 文件
- **THEN** 跳过渲染步骤，直接进入阅读

### Requirement: Produce intermediate part files per batch
每次分批阅读会话 SHALL 产出一个结构化中间产物文件。

#### Scenario: Part file location and naming
- **WHEN** 完成一批页面的阅读
- **THEN** 写入 `wiki/ch<N>-parts/ch<N>-part<M>.md`，其中 M 为批次序号（从 1 开始）

#### Scenario: Part file metadata header
- **WHEN** 创建 part 文件
- **THEN** 文件开头 SHALL 包含 HTML 注释形式的元信息：Part 序号、页面范围（文件名）、书中页码范围、覆盖的 section 编号

#### Scenario: Part file content structure
- **WHEN** 写入 part 文件内容
- **THEN** SHALL 使用与最终 chapter-notes 模板相同的 section 结构（`## 概念定义`、`## 符号定义`、`## 核心论点`、`## 工程应用与实例`），但省略 YAML frontmatter、`## 章节定位`和`## 与全书的关系`

### Requirement: Cross-session continuation
系统 SHALL 支持跨会话续接，自动检测上次读到的位置。

#### Scenario: Detect existing parts and determine next batch
- **WHEN** 用户在新会话中触发 Chapter Reading（如"继续读第3章"）
- **THEN** 系统检查 `wiki/ch<N>-parts/` 中已有的 part 文件，读取最后一个 part 的元信息确定已读到的最后页码，从下一页开始计算本次批次范围

#### Scenario: All pages covered triggers merge
- **WHEN** 检测到已有 parts 覆盖了章节所有页面
- **THEN** 自动进入合并流程，不再创建新的 part 文件

### Requirement: Merge all parts into final chapter note
系统 SHALL 在所有批次完成后，将中间产物合并为符合 chapter-notes 模板的单一最终文件。

#### Scenario: Merge session reads all parts
- **WHEN** 进入合并流程
- **THEN** 读取 `wiki/ch<N>-parts/` 下所有 part 文件（纯文本），按批次序号排序

#### Scenario: Final file includes all template sections
- **WHEN** 写入最终 `wiki/ch<N>-<slug>.md`
- **THEN** 包含完整 YAML frontmatter 和所有 6 个标准 section（章节定位、概念定义、符号定义、核心论点、工程应用与实例、与全书的关系），其中"章节定位"和"与全书的关系"在合并时基于全章信息新写

#### Scenario: Deduplication during merge
- **WHEN** 合并概念定义和符号定义
- **THEN** SHALL 按页码排序，去除跨 part 边界产生的重复条目

#### Scenario: Update index after merge
- **WHEN** 最终 chapter note 写入完成
- **THEN** 更新 `wiki/index.md` 的逐章精读笔记列表

### Requirement: Cleanup after completion
系统 SHALL 在最终 chapter note 确认写入后清理所有临时文件和中间产物。

#### Scenario: Delete pre-rendered images
- **WHEN** 最终 chapter note 已写入且用户确认
- **THEN** 删除 `<Book-Folder>/temp_ch<N>/` 整个文件夹

#### Scenario: Delete intermediate part files
- **WHEN** 最终 chapter note 已写入且用户确认
- **THEN** 删除 `wiki/ch<N>-parts/` 整个文件夹

### Requirement: Batch boundary alignment with section titles
分批边界 SHALL 优先对齐到章节 section 标题处。

#### Scenario: Split at section boundary
- **WHEN** 计算批次的结束页码
- **THEN** 优先选择最近的 section 标题所在页作为切分点（容差 ±2 页）

#### Scenario: Cross-boundary section notation
- **WHEN** 某个 section 横跨批次边界
- **THEN** 下一批的 part 文件 SHALL 在元信息中标注"续上一批 §X.Y"，并在内容中延续该 section 的笔记
