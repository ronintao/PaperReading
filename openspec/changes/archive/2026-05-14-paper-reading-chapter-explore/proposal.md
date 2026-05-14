## Why

当前 paper-reading skill 的 Chapter Reading 操作只有一种模式：直接开始逐页阅读。当用户处于 explore 模式（思考/规划阶段）时，skill 也会立刻开始读 PDF 页面并写笔记，这与 explore 模式"只想不做"的定位冲突。同时，跨批次续接时，part 文件的 metadata 只记录了"读到哪"，没有记录"下一批应该从哪个节开始"，导致节感知的批次切分信息在跨会话时丢失。

## What Changes

- 在 Chapter Reading 操作中增加 **explore 模式分支**：当处于 explore 模式时，只执行渲染准备和批次估计报告，不进行实际阅读
- 增强 **Part Metadata**：在中间产物文件的 HTML 注释头中增加 `Next batch starts` 字段，记录下一批次的起始页码和对应的 section 信息
- 调整 **Phase 0-C 跨会话续接逻辑**：优先从最后一个 part 的 `Next batch starts` 字段确定下一批起点，无此字段时回退到现有的 "last page + 1" 逻辑

## Capabilities

### New Capabilities
- `chapter-reading-explore`: Chapter Reading 在 explore 模式下的行为——仅渲染页面和报告批次估计，不执行阅读

### Modified Capabilities
- `batch-chapter-reading`: 增强 Part Metadata 格式（新增 `Next batch starts` 字段）和跨会话续接逻辑（优先读取该字段）

## Impact

- 受影响文件：`.codemaker/skills/paper-reading/skill/skill.md`（skill 指令文件）
- 无 API 或依赖变化
- 向后兼容：已有的不含 `Next batch starts` 字段的 part 文件仍可正常续接（回退逻辑）
