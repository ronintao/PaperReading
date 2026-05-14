## MODIFIED Requirements

### Requirement: Render scanned pages as images
对于扫描件 PDF，系统 SHALL 使用 PyMuPDF 将每页渲染为 PNG 图片，存入专用子文件夹（而非散落在项目根目录）。

#### Scenario: Page rendering parameters
- **WHEN** 渲染扫描件 PDF 页面
- **THEN** 使用 `page.get_pixmap(dpi=200)` 渲染，保存为 PNG 格式

#### Scenario: Render all pages
- **WHEN** 检测到扫描件 PDF
- **THEN** 渲染 PDF 的所有相关页面为图片

#### Scenario: Temp folder for Ingest operation
- **WHEN** 在 Ingest 操作中渲染普通论文的扫描页面
- **THEN** 存入 `<Paper-Folder>/temp_scan/page_<NNN>.png`，其中 NNN 为 PDF 页码（零填充三位）

#### Scenario: Temp folder for Chapter Reading operation
- **WHEN** 在 Chapter Reading 操作中渲染章节的扫描页面
- **THEN** 存入 `<Book-Folder>/temp_ch<N>/page_<NNN>.png`，其中 N 为章节号，NNN 为 PDF 页码（零填充三位）

### Requirement: Cleanup temporary rendered images
渲染产生的临时页面图片 SHALL 在解读完成后清理。

#### Scenario: Temporary images deleted after ingest
- **WHEN** 扫描件 PDF 的 Ingest 解读流程完成（wiki md 文件已写入）
- **THEN** 删除 `<Paper-Folder>/temp_scan/` 整个文件夹；论文的 figures（由 paper_extract_figures.py 提取）不受影响

#### Scenario: Temporary images deleted after chapter reading
- **WHEN** Chapter Reading 的最终 chapter note 已写入
- **THEN** 删除 `<Book-Folder>/temp_ch<N>/` 整个文件夹

#### Scenario: Large chapter cleanup includes intermediate parts
- **WHEN** 大章节的多会话分批阅读完成且最终 chapter note 已写入
- **THEN** 同时删除 `wiki/ch<N>-parts/` 文件夹和 `temp_ch<N>/` 文件夹
