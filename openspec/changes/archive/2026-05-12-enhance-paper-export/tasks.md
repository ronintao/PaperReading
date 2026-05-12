## 1. md-to-mht Skill 创建

- [x] 1.1 创建 skill 目录结构 `.codemaker/skills/md-to-mht/skill/SKILL.md`
- [x] 1.2 编写 SKILL.md：定义 skill 元数据、触发词、操作流程（调用 `scripts/md_to_mht.py`）
- [x] 1.3 完善 `scripts/md_to_mht.py`：添加 MiKTeX PATH 自动检测逻辑
- [x] 1.4 在 `scripts/md_to_mht.py` 中增加 YAML frontmatter 处理（提取标题作为文档标题，无 frontmatter 时 fallback 到文件名）

## 2. paper-reading Skill 增强：Topic Extract

- [x] 2.1 在 `SKILL.md` 中添加 Topic Extract 操作节（触发词、Phase 1-3 流程描述）
- [x] 2.2 创建 topic 文档模板 `skill/templates/topic.md`（4 段式：问题描述、符号定义、关键推导、核心公式）
- [x] 2.3 在 `SKILL.md` 的 Index 页规则中添加 `## Topic 专题` 分区规范
- [x] 2.4 在 `SKILL.md` 的 Conventions 中添加 topic 文件命名规则（`topic-<slug>.md`）

## 3. 验证

- [x] 3.1 用现有约束力论文笔记测试 Topic Extract：生成一个子问题专题文档
- [x] 3.2 用生成的 topic 文档测试 md-to-mht 导出
- [x] 3.3 确认 MHT 文件可在 WizNote 中正常导入和显示
