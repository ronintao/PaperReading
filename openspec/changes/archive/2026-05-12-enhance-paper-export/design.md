## Context

paper-reading skill 管理 `<Paper Title>/wiki/` 下的论文阅读笔记，每篇论文一个 `type: source` 的 markdown 文件。当前缺少两个能力：
1. **子问题提取**：用户关心论文中的特定子问题，需要从已有 source 笔记中提取和综合
2. **MHT 导出**：用户使用 WizNote 管理知识，需要将 markdown 转为 MHT 单文件（含内嵌公式图片）

已有原型脚本 `scripts/md_to_mht.py` 验证了技术可行性：LaTeX 公式通过 matplotlib + MiKTeX usetex 渲染为 PNG，HTML + 图片打包为 MIME multipart/related 格式。

## Goals / Non-Goals

**Goals:**
- paper-reading skill 新增 Topic Extract 操作，生成 `type: topic` 专题文档
- 创建独立的 md-to-mht skill，将任意 markdown 转换为 WizNote 可导入的 MHT 文件
- Topic Extract 和 MHT 导出是两个独立步骤，用户按需分别调用

**Non-Goals:**
- 不做 Word (.docx) 导出（已验证，但 WizNote 兼容性不如 MHT）
- 不做 MHT → markdown 反向转换
- 不自动在 ingest 流程中触发导出
- topic 文档不递归——不从 topic 中再提取 sub-topic

## Decisions

### D1: Topic 文档结构为 4 段式
**选择**: 问题描述 → 符号定义 → 关键推导 → 核心公式
**理由**: 对比 source 笔记的 8 段式（Essence/Factors/Architecture/...），topic 文档面向具体问题，需要更紧凑、推导导向的结构。符号定义单独列出确保推导过程可自包含。
**替代方案**: 复用 source 笔记的 8 段式 → 过于臃肿，不适合聚焦子问题

### D2: 符号定义采用逐行列表格式
**选择**: `- $symbol$：定义描述` 的列表格式
**理由**: 比表格更灵活，公式可以任意复杂（如带分数线的定义），且 MHT 导出时每行公式独立渲染
**替代方案**: Markdown 表格 → 行内公式与表格单元格配合拥挤

### D3: md-to-mht 作为独立 skill
**选择**: 独立于 paper-reading，新建 `.codemaker/skills/md-to-mht/` skill
**理由**: 文档格式转换是通用能力，不应耦合到论文阅读。其他 skill 或手写 markdown 也可能需要 MHT 导出
**替代方案**: 内嵌为 paper-reading 的一个操作 → 不可复用

### D4: LaTeX 渲染引擎选择 matplotlib + usetex
**选择**: `matplotlib.rcParams['text.usetex'] = True` + MiKTeX
**理由**: 已验证可渲染复杂公式（上下标、希腊字母、矩阵等），输出质量达出版级。MiKTeX 已安装且开启了自动安装宏包
**替代方案**: mathtext（不支持 `\boldsymbol` 等高级命令）、网络 API（需联网）

### D5: Topic slug 统一加 `topic-` 前缀
**选择**: `wiki/topic-<slug>.md`
**理由**: 一眼区分 source 笔记和 topic 专题

## Risks / Trade-offs

- **[公式渲染失败]** → 某些 LaTeX 命令可能不被 MiKTeX 默认宏包支持。缓解：已启用 MiKTeX 自动安装宏包；渲染失败时 fallback 为纯文本显示
- **[MHT 兼容性]** → 不同版本 WizNote 对 MHT 的支持可能有差异。缓解：已用 WizNote 实际测试验证原型
- **[行内公式基线对齐]** → HTML 中 `<img>` 行内图片与文字的垂直对齐可能不完美。缓解：使用 `vertical-align:middle` CSS，可在实际使用中微调
