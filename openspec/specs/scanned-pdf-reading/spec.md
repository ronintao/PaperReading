## ADDED Requirements

### Requirement: Detect scanned PDF
系统 SHALL 在读取 PDF 前自动检测其是否为扫描件（无文本层）。

#### Scenario: PDF with text layer
- **WHEN** 使用 PyMuPDF 对 PDF 每页执行 `page.get_text()`，大多数页面返回文本长度 >= 50 字符
- **THEN** 判定为有文本层 PDF，使用 read_file 直接读取

#### Scenario: Scanned PDF without text layer
- **WHEN** 使用 PyMuPDF 对 PDF 每页执行 `page.get_text()`，大多数页面返回文本长度 < 50 字符
- **THEN** 判定为扫描件，触发图片渲染 + LLM 视觉读取流程

### Requirement: Render scanned pages as images
对于扫描件 PDF，系统 SHALL 使用 PyMuPDF 将每页渲染为 PNG 图片。

#### Scenario: Page rendering parameters
- **WHEN** 渲染扫描件 PDF 页面
- **THEN** 使用 `page.get_pixmap(dpi=200)` 渲染，保存为 PNG 格式

#### Scenario: Render all pages
- **WHEN** 检测到扫描件 PDF
- **THEN** 渲染 PDF 的所有页面为图片

### Requirement: LLM vision reading of rendered pages
渲染后的页面图片 SHALL 通过 read_file 工具逐页读取，利用 LLM 视觉能力理解内容。

#### Scenario: Sequential page reading
- **WHEN** 扫描件 PDF 的所有页面已渲染为图片
- **THEN** 使用 read_file 逐页读取图片，LLM 综合所有页面内容进行理解和分析

#### Scenario: Content comprehension including formulas and tables
- **WHEN** LLM 通过视觉读取扫描件页面
- **THEN** SHALL 能理解页面中的文字、数学公式、表格和图表内容

### Requirement: Cleanup temporary rendered images
渲染产生的临时页面图片 SHALL 在解读完成后清理。

#### Scenario: Temporary images deleted after ingest
- **WHEN** 扫描件 PDF 的解读流程完成（wiki md 文件已写入）
- **THEN** 删除渲染产生的临时 PNG 文件；论文的 figures（由 paper_extract_figures.py 提取）不受影响

### Requirement: No additional dependencies
扫描件处理 SHALL NOT 引入 PyMuPDF 之外的新依赖。

#### Scenario: Dependency check
- **WHEN** 审查扫描件处理功能的依赖
- **THEN** 仅依赖 PyMuPDF (fitz)（已有依赖）和 LLM read_file 工具的视觉能力
