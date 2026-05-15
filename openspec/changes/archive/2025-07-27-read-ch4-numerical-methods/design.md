## Context

本书 *Computer Aided Kinematics and Dynamics of Mechanical Systems* (Haug, 1989) 的逐章精读项目已完成 Ch.1-3 笔记。第四章 "Numerical Methods in Kinematics"（book pp.118-152）是扫描版 PDF，已预渲染为 `temp_ch4/page_129.png` ~ `page_165.png`。其中 page_129 属于 Ch.3 习题，page_165 属于 Ch.5 标题页，Ch.4 有效范围为 page_130 ~ page_164（36 页）。

已有 Ch.3 笔记提供了约束方程库、Jacobian、Newton-Raphson 等前置概念。Ch.4 将这些理论转化为可执行的计算流程。

## Goals / Non-Goals

**Goals:**
- 按 paper-reading skill 的 chapter-notes 模板完成 Ch.4 精读笔记
- 提取所有概念定义（英文原文+中文翻译）、符号定义、核心论点
- 以 ~15 页为单位分批阅读扫描图片，每批产出 part 文件
- 最终合并为标准格式的 `wiki/ch4-numerical-methods-kinematics.md`

**Non-Goals:**
- 不修改 Ch.1-3 的已有笔记
- 不提取章节中的习题（Problems section）
- 不对章节内容做超出原文的延伸研究

## Decisions

### D1: 分批策略 — 3 批，按章节边界对齐

**选择**: 将 36 页分为 3 批，每批 ~12 页，在 section 边界处切分（±2 页容差）。

**理由**: 36 页超过单次会话的 15 页阅读上限。3 批比 2 批更灵活，可在阅读时根据 section 边界微调。实际切分点将在阅读时确定。

**预估切分**:
- Batch 1: page_130 ~ page_142（~13 页）— 引言 + §4.1 + §4.2 前半
- Batch 2: page_143 ~ page_154（~12 页）— §4.2 后半 + §4.3 + §4.4
- Batch 3: page_155 ~ page_164（~10 页）— §4.5 + §4.6 + 剩余

**备选**: 2 批（每批 18 页，超出推荐上限）或 4 批（过于碎片化）。

### D2: Part 文件存储位置

**选择**: `wiki/ch4-parts/ch4-part<N>.md`

**理由**: 与 Ch.3 笔记的 paper-reading skill 约定一致。Part 文件是临时中间产物，合并完成后删除。

### D3: 最终文件命名

**选择**: `wiki/ch4-numerical-methods-kinematics.md`

**理由**: 遵循已有命名模式（`ch1-elements-of-cakd.md`, `ch3-planar-cartesian-kinematics.md`），用 `ch<N>-<slug>` 格式。

## Risks / Trade-offs

- **[Section 边界不确定]** → 预估的批次切分点可能需要在阅读时调整。缓解：允许 ±2 页容差，batch 间在 part 文件 metadata 中记录 `Next batch starts`。
- **[扫描质量]** → 个别页面的公式或图表可能因扫描质量不佳而难以辨认。缓解：在笔记中标注 `[扫描不清]` 并尽力推断。
- **[page_129 误包含]** → `temp_ch4/` 中 page_129 实际属于 Ch.3 习题。缓解：Batch 1 从 page_130 开始，跳过 page_129。
