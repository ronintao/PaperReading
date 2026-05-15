## ADDED Requirements

### Requirement: 分批阅读扫描页面
系统 SHALL 将 temp_ch5/ 中的 46 张 PNG 页面图片分为 4 个批次进行视觉阅读，每批约 12-15 页，在章节/小节边界处对齐切分（±2 页容差）。

#### Scenario: 正常批次阅读
- **WHEN** 执行某一批次的阅读任务
- **THEN** 逐张读取该批次范围内的所有 PNG 图片，提取概念定义、符号定义、核心论点和工程实例

#### Scenario: 批次边界调整
- **WHEN** 预估的批次结束页恰好处于一个小节的中间
- **THEN** 将批次边界向前或向后调整最多 2 页，使其对齐到小节边界

---

### Requirement: 中间 part 文件生成
每批阅读完成后 SHALL 生成一个中间文件 `wiki/ch5-parts/ch5-partN.md`（N 为批次序号），包含该批次提取的所有结构化内容和元数据注释。

#### Scenario: part 文件结构完整
- **WHEN** 一批阅读完成
- **THEN** 生成的 part 文件 SHALL 包含：HTML metadata 注释（页面范围、覆盖节次、续读信息）、概念定义节、符号定义节、核心论点节、工程应用与实例节

#### Scenario: 续读元数据正确
- **WHEN** 一批阅读完成且后续仍有未读页面
- **THEN** part 文件的 metadata 注释 SHALL 包含 `<!-- Next batch starts: page_NNN.png, §X.Y Section Title -->` 指明下一批的起始位置

#### Scenario: 末批标记
- **WHEN** 最后一批阅读完成
- **THEN** part 文件的 metadata 注释 SHALL 包含 `<!-- Next batch starts: none (chapter complete) -->`

---

### Requirement: 合并为最终章节笔记
所有 part 文件完成后 SHALL 合并为最终文件 `wiki/ch5-planar-kinematic-modeling.md`，格式与现有 Ch.1-4 笔记一致。

#### Scenario: 合并内容完整
- **WHEN** 执行合并任务
- **THEN** 最终笔记 SHALL 包含完整的 YAML frontmatter（type: chapter-notes）、章节定位、概念定义（按页码排序去重）、符号定义（按上下文分组去重）、核心论点（按章节顺序组织）、工程应用与实例（合并为一张表）、与全书的关系

#### Scenario: 格式与前四章一致
- **WHEN** 合并完成
- **THEN** 最终笔记的 YAML frontmatter 字段、section 标题、概念定义格式、符号表格式 SHALL 与 `ch4-numerical-methods-kinematics.md` 保持一致

---

### Requirement: 索引更新
合并完成后 SHALL 更新 `wiki/index.md`，在"逐章精读笔记"部分添加第五章条目。

#### Scenario: 索引条目格式
- **WHEN** 索引更新完成
- **THEN** 新条目 SHALL 遵循格式 `- [Ch.5 Planar Kinematic Modeling and Analysis](ch5-planar-kinematic-modeling.md) — <一行摘要>`

---

### Requirement: 临时文件清理
最终笔记确认满意后 SHALL 清理所有临时文件。

#### Scenario: 清理范围
- **WHEN** 用户确认最终笔记满意
- **THEN** SHALL 删除 `temp_ch5/` 目录（渲染的 PNG 图片）和 `wiki/ch5-parts/` 目录（中间 part 文件）
