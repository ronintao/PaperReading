## Why

《Computer Aided Kinematics and Dynamics of Mechanical Systems》第四章 "Numerical Methods in Kinematics" 是全书从理论到实现的桥梁章节（book pp.118-152，共 36 页扫描版）。Ch.3 建立了约束方程库和运动学三级分析框架，但只预告了 Newton-Raphson 等数值方法；Ch.4 则展开四种运动学计算模式（Assembly、Position、Velocity、Acceleration Analysis）的完整数值实现，以及 DADS 代码的计算组织架构。目前 Ch.1-3 笔记已完成，Ch.4 是下一个自然阅读目标。

## What Changes

- 分 3 批阅读 `temp_ch4/` 中 36 页扫描图片（page_130 ~ page_164），每批约 12-15 页
- 每批产出中间 part 文件至 `wiki/ch4-parts/`
- 全部批次完成后合并为最终章节笔记 `wiki/ch4-numerical-methods-kinematics.md`
- 更新 `wiki/index.md` 添加 Ch.4 笔记条目
- 清理 `temp_ch4/` 和 `wiki/ch4-parts/`

## Capabilities

### New Capabilities
- `ch4-reading`: Chapter 4 逐章精读笔记的分批阅读、中间文件管理和最终合并流程

### Modified Capabilities

（无——本次变更仅增加新的章节笔记，不修改已有笔记内容）

## Impact

- 新增文件：`wiki/ch4-parts/ch4-part1.md`, `ch4-part2.md`, `ch4-part3.md`（临时），最终 `wiki/ch4-numerical-methods-kinematics.md`
- 修改文件：`wiki/index.md`（添加 Ch.4 条目）
- 删除文件：`temp_ch4/`（渲染的 PNG 临时文件），`wiki/ch4-parts/`（中间 part 文件）
