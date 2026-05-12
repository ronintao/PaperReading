## Why

Paper-reading skill 当前产出的是按论文组织的 reading note（8 段式结构），但用户的实际认知需求往往是**按问题组织**的——从已有笔记中提取和综合某个子问题的推导脉络。此外，wiki 中的 markdown 笔记缺乏便携的导出格式，用户需要将笔记导出为 MHT 单文件以便在 WizNote 中管理和离线查看。

## What Changes

- **paper-reading skill 新增 Topic Extract 操作**：从已有 source 笔记中提取子问题相关内容，生成 `type: topic` 的专题文档（问题描述、符号定义、关键推导、核心公式），存放于论文的 `wiki/` 目录下
- **新建 md-to-mht skill**：独立的文档格式转换能力，将任意 markdown 文件（含 LaTeX 公式、图片、表格、代码块）转换为 MHT 单文件，公式渲染为 PNG 图片内嵌
- **wiki/index.md 新增 Topic 分区**：导航页增加 `## Topic 专题` 区块，列出所有 topic 文档

## Capabilities

### New Capabilities
- `topic-extract`: 从已有论文 reading notes 中提取子问题，生成 4 段式专题文档（问题描述、符号定义、关键推导、核心公式）
- `md-to-mht`: 将 markdown 文件转换为 MHT 格式，支持 LaTeX 公式渲染为 PNG 内嵌、图片/表格/代码块/callout 样式保留

### Modified Capabilities
- （无既有 spec 需要修改）

## Impact

- **paper-reading skill**（`.codemaker/skills/paper-reading/skill/SKILL.md`）：新增 Topic Extract 操作节、topic 文档模板、index.md Topic 分区规则
- **新 skill 目录**（`.codemaker/skills/md-to-mht/`）：新建 skill 定义和转换脚本
- **转换脚本**（`scripts/md_to_mht.py`）：已有原型，需完善为 skill 可调用的工具
- **依赖**：MiKTeX（LaTeX 渲染）、matplotlib、python-docx（可选）、Pillow——均已安装
