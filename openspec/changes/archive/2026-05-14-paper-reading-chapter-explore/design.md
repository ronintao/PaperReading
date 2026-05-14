## Context

paper-reading skill 是一个 Markdown 指令文件（`skill.md`），指导 AI 助手如何进行论文/书籍的阅读和笔记整理。其中 Chapter Reading 操作支持多会话分批阅读大章节（>15页扫描版），通过中间产物文件（part files）的 metadata 注释跟踪跨会话状态。

当前 Chapter Reading 操作不区分 explore/apply 模式，触发后立即开始逐页阅读。Part metadata 记录了已读范围和覆盖的 section，但不记录下一批次应从何处开始的前瞻信息。

## Goals / Non-Goals

**Goals:**
- Chapter Reading 在 explore 模式下仅执行准备工作（渲染页面）并报告批次估计，不进行实际阅读
- Part metadata 增加 `Next batch starts` 字段，在跨会话续接时提供精确的起点信息
- 向后兼容已有的不含新字段的 part 文件

**Non-Goals:**
- 不引入独立的 plan 文件（状态完全由 temp 文件夹 + part metadata 承载）
- 不记录用户的软性决策（如阅读偏好、section 优先级）
- 不改变单会话模式（≤15页）的任何行为
- 不改变合并阶段（Phase 0-D）和最终 chapter-notes 的格式

## Decisions

### Decision 1: Explore 模式通过模式检测分支，不引入新命令

**选择**: 在 Chapter Reading 操作的入口处检测当前是否处于 explore 模式，若是则走轻量分支（渲染 + 报告），否则走现有完整流程。

**替代方案**: 定义独立的 "Chapter Reading Plan" 操作。
**理由**: 不值得为此增加一个新操作，explore/apply 是模式而非操作，在同一个操作内分支更自然。

### Decision 2: `Next batch starts` 作为 Part Metadata 的新增行

**选择**: 在 part 文件的 HTML 注释 metadata 中新增一行 `<!-- Next batch starts: page_NNN.png, §X.Y Title -->`。

**格式示例**:
```markdown
<!-- Part 1 of Chapter 4 -->
<!-- Pages: page_131.png ~ page_143.png (book pp.119-131) -->
<!-- Sections covered: §4.1, §4.2 -->
<!-- Continues from previous: no -->
<!-- Next batch starts: page_144.png, §4.3 Minimization Methods -->
```

**替代方案**: 用独立的 plan.md 文件记录批次状态。
**理由**: Part metadata 已经是跨会话状态的载体，增加一个字段比引入新文件更简单，且保持了"无额外状态文件"的设计原则。

### Decision 3: 跨会话续接优先读 `Next batch starts`，回退到 last page + 1

**选择**: Phase 0-C 检测到已有 part 文件时，先检查最后一个 part 是否有 `Next batch starts` 行。若有，以该行指定的页码和 section 为起点；若无（旧 part 文件），回退到现有的 "最后一页 + 1" 逻辑。

**理由**: 向后兼容。已有的 part 文件不需要修改即可继续工作。

## Risks / Trade-offs

- **[Risk] Explore 模式判定不准确** → 由 skill 指令中明确的触发条件控制：当用户在 explore 模式（`/opsx:explore`）下触发 Chapter Reading 时走轻量分支。不依赖启发式推断。
- **[Risk] `Next batch starts` 信息可能在阅读时还不确定** → 当批次末尾恰好在 section 中间，先写一个基于当前位置的最佳估计（如 "page_144.png, continuation of §4.2"），下一批次启动时可验证和调整。
- **[Trade-off] 不记录软性决策** → 接受。章节精读场景下按顺序通读即可，无需持久化阅读策略。
