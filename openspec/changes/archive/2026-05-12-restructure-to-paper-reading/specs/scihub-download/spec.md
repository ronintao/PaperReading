## ADDED Requirements

### Requirement: Dynamic Sci-Hub mirror discovery
系统 SHALL 通过搜索引擎动态发现可用的 Sci-Hub 镜像地址，而非依赖硬编码的 URL 列表。

#### Scenario: Search engine discovers mirrors
- **WHEN** 需要通过 Sci-Hub 下载论文
- **THEN** 系统使用搜索引擎（如 DuckDuckGo）搜索 "sci-hub"，从搜索结果中提取前 5 个包含 "sci-hub" 字样的候选 URL

#### Scenario: No hardcoded mirror list
- **WHEN** Sci-Hub 下载逻辑执行时
- **THEN** SHALL NOT 使用预定义的镜像地址列表，所有候选 URL 来自搜索引擎实时结果

### Requirement: Sci-Hub download via DOI
系统 SHALL 使用论文的 DOI 通过 Sci-Hub 候选镜像下载 PDF。

#### Scenario: Try mirrors in sequence
- **WHEN** 获得 5 个候选 Sci-Hub URL 和论文 DOI
- **THEN** 依次尝试 `<candidate-url>/<DOI>`，直到成功下载或全部失败

#### Scenario: Validate downloaded PDF
- **WHEN** 从 Sci-Hub 候选链接获得响应
- **THEN** 验证文件大小 > 1KB 且文件头为 `%PDF`；若返回 HTML 页面，SHALL 解析 HTML 提取 iframe/embed 中的实际 PDF 链接并下载

#### Scenario: All mirrors fail
- **WHEN** 5 个候选 URL 全部下载失败
- **THEN** 提示用户手动放置 PDF 文件

### Requirement: Sci-Hub as fallback in download priority chain
Sci-Hub SHALL 作为下载优先级链中的第三优先级，在 arXiv 和 Semantic Scholar openAccessPdf 之后。

#### Scenario: Download priority order
- **WHEN** 需要下载论文 PDF
- **THEN** 按以下顺序尝试：(1) arXiv 直接下载 (2) Semantic Scholar openAccessPdf (3) Sci-Hub via DOI (4) 提示用户手动放 PDF

#### Scenario: DOI obtained from Semantic Scholar
- **WHEN** Semantic Scholar API 返回结果中没有 openAccessPdf 但包含 DOI
- **THEN** 自动使用该 DOI 触发 Sci-Hub 下载流程

### Requirement: DOI as direct input
系统 SHALL 支持用户直接提供 DOI 作为论文标识输入。

#### Scenario: User provides DOI
- **WHEN** 用户提供格式为 `10.xxxx/...` 的 DOI
- **THEN** 先通过 Semantic Scholar 查找 openAccessPdf，若无则直接通过 Sci-Hub 下载
