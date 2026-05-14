## Why

Paper-reading skill 的 Chapter Reading 操作假设一次会话能读完整章所有扫描页面，但实际中大章节（如 70 页）远超单次会话的上下文窗口容量。需要引入多会话分批阅读机制，使大章节可以跨会话逐步完成，并在最终会话合并为统一的 chapter-notes 文件。

## What Changes

- 新增多会话分批阅读流程：当扫描章节页数超过 15 页时自动触发
- 新增预渲染规范：整章页面一次性渲染到 `temp_ch<N>/page_<NNN>.png`
- 新增中间产物格式：每批阅读结果存入 `wiki/ch<N>-parts/ch<N>-part<M>.md`
- 新增合并会话逻辑：读取所有 parts → 去重合并 → 写最终 `ch<N>-<slug>.md`
- 新增跨会话续接机制：检测已有 parts 自动确定下一批页面范围
- 修改清理规则：最终笔记写完后删除 `temp_ch<N>/` 和 `wiki/ch<N>-parts/`
- 修改 Ingest Phase 0 的扫描件临时文件存放规范（统一到子文件夹）

## Capabilities

### New Capabilities
- `batch-chapter-reading`: 大章节多会话分批阅读机制，包括预渲染、分批精读、中间产物格式、合并、续接和清理的完整流程

### Modified Capabilities
- `scanned-pdf-reading`: 临时文件存放路径从散落根目录改为统一子文件夹（`temp_scan/` 用于普通论文 Ingest，`temp_ch<N>/` 用于 Chapter Reading）；增加对超大文档的分批提示

## Impact

- 文件修改：`.codemaker/skills/paper-reading/skill/skill.md`（主 skill 文件）
- 无新依赖引入
- 向后兼容：短章节（≤15页）仍走原有单会话流程，无 breaking change
