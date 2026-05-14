## ADDED Requirements

### Requirement: Explore mode reads only for structure
当用户在 explore 模式下触发 Chapter Reading 时，系统 SHALL 仅读取结构性信息（目录、章节首尾页）来确定章节范围，不进行内容阅读或笔记撰写。

#### Scenario: Read TOC and chapter boundaries
- **WHEN** 用户在 explore 模式下请求分析某章节
- **THEN** 系统读取 PDF 目录（书签或目录页）确定章节页码范围，读取章节首页确认标题，读取章节末页确认结束位置

#### Scenario: Scanned chapter rendering
- **WHEN** 用户在 explore 模式下请求分析某章节，且该章节为扫描版 PDF
- **THEN** 系统渲染该章节所有页面为 PNG 保存至 `temp_ch<N>/`，但不读取 PNG 内容（首尾页除外，用于确认边界）

#### Scenario: Skip rendering if already done
- **WHEN** `temp_ch<N>/` 已存在且包含预期数量的 PNG
- **THEN** 跳过渲染步骤

### Requirement: Explore mode reports batch estimate
系统 SHALL 在 explore 准备完成后向用户报告章节概况和预估批次信息。

#### Scenario: Report for new chapter
- **WHEN** explore 准备完成，且无已有进度
- **THEN** 系统报告：章节标题、章节编号、PDF 页码范围、总页数、是否扫描版、预估批次数，并提示可用 `/opsx:ff` 创建阅读计划或直接开始阅读

#### Scenario: Report with existing progress
- **WHEN** explore 准备完成，且 `wiki/ch<N>-parts/` 中已有 part 文件
- **THEN** 系统额外报告：已完成的批次数、已读页数、剩余页数和预估剩余批次数

### Requirement: OpenSpec FF creates batch-based tasks
当用户在 FF/New 模式下创建章节阅读的 OpenSpec change 时，系统 SHALL 使用 Phase 0-E 的产出生成包含分批阅读任务的 OpenSpec artifacts。

#### Scenario: Create proposal and tasks for chapter reading
- **WHEN** 用户使用 `/opsx:ff` 为章节阅读创建 change
- **THEN** 系统创建 proposal（描述书名、章节、页码范围、阅读策略）和 tasks（每个 batch 一个 task，含估计页码范围），不启动实际阅读

#### Scenario: Tasks structure
- **WHEN** 创建 tasks.md
- **THEN** tasks SHALL 包含三组：准备（渲染）、分批阅读（每 ~15 页一个 task）、合并与收尾（合并 part 文件、更新 index、清理临时文件）

### Requirement: OpenSpec Apply executes batch tasks
当用户在 Apply 模式下执行章节阅读的 OpenSpec change 时，系统 SHALL 按 tasks.md 中的批次顺序逐个执行。

#### Scenario: Execute one batch per apply session
- **WHEN** 用户使用 `/opsx:apply` 执行章节阅读 change
- **THEN** 系统找到 tasks.md 中第一个未完成的 batch task，执行该批次的阅读，写入 part 文件，标记 task 完成

#### Scenario: Adjust batch boundary and update tasks
- **WHEN** 实际阅读中因 section 边界调整了批次范围
- **THEN** 系统更新当前 task 的描述为实际页码范围，并调整下一个 batch task 的估计起点
