## Context

*Computer Aided Kinematics and Dynamics of Mechanical Systems, Vol.I* 是一本扫描版教材（无 OCR 文字层）。Chapter 6 "Dynamics of Planar Systems" 共 44 页（书页 p.199–242，PDF 页 211–254）。已在 explore 阶段完成：
- 扫描检测：44/44 页无文字（纯扫描）
- 预渲染：44 张 PNG（DPI=200）已存放于 `temp_ch6/`（page_211.png ~ page_254.png）
- 章节边界确认：首页 §6.1，末页 §6.6 习题

已有 Ch.1–Ch.5 的完整阅读笔记，遵循 paper-reading skill v2.4.0 的 chapter-notes 格式。

## Goals / Non-Goals

**Goals:**
- 分 3 批（每批 ~15 页）通过 LLM Vision 读取扫描页面
- 每批生成一个中间 part 文件（`wiki/ch6-parts/ch6-partM.md`）
- 批次结束边界优先对齐小节分界（±2 页容差）
- 全部批次完成后合并为最终章节笔记 `wiki/ch6-planar-dynamics.md`
- 更新 `wiki/index.md`

**Non-Goals:**
- 不读取 Ch.6 习题的详细解答（只记录习题结构）
- 不提取图片到 `wiki/figures/`（扫描质量不适合直接复用）
- 不与 Related 论文做交叉分析（留到合并后单独进行）

## Decisions

### 批次划分策略
采用 ~15 页/批，估算 3 批。实际执行时根据小节边界微调（±2 页），在每个 part 文件的 `<!-- Next batch starts -->` 元数据中记录下一批的精确起点。

### 文件命名
- 中间产物：`wiki/ch6-parts/ch6-part1.md`, `ch6-part2.md`, `ch6-part3.md`
- 最终笔记：`wiki/ch6-planar-dynamics.md`（与 Ch.5 的 `ch5-planar-kinematic-modeling.md` 保持命名风格一致）

### 读取节奏
每轮读取 2 张 PNG（LLM Vision），提取概念定义、符号定义、核心论点、工程应用与实例。

## Risks / Trade-offs

- **[扫描质量]** 部分页面公式可能模糊 → 遇到不确定的符号在笔记中标注 `[?]`，合并时人工复核
- **[批次边界]** 某个小节可能跨批次被拆分 → part 文件用 `Continues from previous` 元数据标记，合并时拼接
- **[上下文长度]** 每批 15 页 × Vision 读取可能接近上下文限制 → 已按 skill 规范控制在 15 页以内
