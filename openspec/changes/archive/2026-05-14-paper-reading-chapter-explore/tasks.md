## 1. Explore 模式分支

- [x] 1.1 在 skill.md 的 Chapter Reading 操作开头增加 explore/apply 模式分支判断逻辑
- [x] 1.2 编写 explore 分支：渲染准备（复用现有 Phase 0 渲染逻辑）+ 批次估计报告
- [x] 1.3 编写 explore 分支报告模板：含章节标题、总页数、扫描版标识、预估批次数、已有进度（如有）

## 2. Part Metadata 增强

- [x] 2.1 在 Phase 0-B 第3步的 part 文件 metadata 模板中增加 `<!-- Next batch starts: ... -->` 行
- [x] 2.2 在 Phase 0-B 的批次结束逻辑中增加：确定下一批起始页和 section 信息，写入 `Next batch starts` 字段
- [x] 2.3 处理最后一个批次的特殊情况：写入 `<!-- Next batch starts: none (chapter complete) -->`

## 3. 跨会话续接逻辑调整

- [x] 3.1 修改 Phase 0-C 第1步：优先读取最后一个 part 的 `Next batch starts` 字段确定下一批起点
- [x] 3.2 增加回退逻辑：当 `Next batch starts` 字段不存在时，回退到现有的 "last page + 1" 计算方式
- [x] 3.3 增加合并触发条件：当 `Next batch starts` 值为 `none (chapter complete)` 时进入合并流程

## 4. Explore 模式修正（读结构不读内容）

- [x] 4.1 修改 Phase 0-E：改为读 TOC + 首尾页确定范围，而非"不读任何内容"
- [x] 4.2 更新报告提示：从"退出 explore 模式后可开始阅读"改为"可用 /opsx:ff 创建阅读计划"

## 5. OpenSpec FF 集成（Phase 0-F）

- [x] 5.1 新增 Phase 0-F：FF/New 模式下用 explore 产出创建 OpenSpec artifacts
- [x] 5.2 编写 tasks 模板：准备→分批阅读→合并收尾 三组任务结构

## 6. OpenSpec Apply 集成（Phase 0-G）

- [x] 6.1 新增 Phase 0-G：Apply 模式下从 tasks.md 读取并执行下一个 batch task
- [x] 6.2 编写批次完成后的 task 更新逻辑（打勾 + 调整下一批次估计范围）
