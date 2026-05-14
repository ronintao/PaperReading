## 1. 更新 Ingest Phase 0 扫描件临时文件路径

- [x] 1.1 修改 skill.md 中 Ingest Phase 0 的扫描件渲染路径：从 `temp_scan_page_*.png`（散落根目录）改为 `temp_scan/page_<NNN>.png`（统一子文件夹）
- [x] 1.2 修改 Ingest Phase 0 的 cleanup 描述：从"删除 temp_scan_page_*.png"改为"删除 temp_scan/ 文件夹"

## 2. 更新 Chapter Reading Phase 0 — 预渲染规范

- [x] 2.1 修改 Chapter Reading Phase 0 的扫描件渲染路径：从 `temp_scan_page_*.png` 改为 `temp_ch<N>/page_<NNN>.png`
- [x] 2.2 添加"跳过渲染"逻辑：若 `temp_ch<N>/` 已存在且包含预期数量的 PNG 文件则跳过

## 3. 新增 Chapter Reading 多会话分批流程

- [x] 3.1 在 Phase 0 中添加阈值检测逻辑：扫描页面数 > 15 → 进入多会话分批模式
- [x] 3.2 新增"Phase 0-B: 分批精读"段落，定义每批 ~15 页（按 section 边界 ±2 页容差对齐）
- [x] 3.3 定义中间产物文件格式规范：路径 `wiki/ch<N>-parts/ch<N>-part<M>.md`、元信息注释头、section 结构
- [x] 3.4 新增"Phase 0-C: 跨会话续接"段落，定义检测已有 parts → 确定下一批范围的逻辑
- [x] 3.5 新增"Phase 0-D: 合并会话"段落，定义读取所有 parts → 去重合并 → 写最终 chapter note 的流程

## 4. 更新清理规则

- [x] 4.1 更新 Chapter Reading Phase 最后的 cleanup 描述：明确列出删除 `temp_ch<N>/` 和 `wiki/ch<N>-parts/` 两个目标
- [x] 4.2 添加清理触发条件："最终 chapter note 已写入且用户确认后"

## 5. 新增触发词

- [x] 5.1 在 Chapter Reading 的 Trigger phrases 中添加 "继续读第N章"、"continue chapter N" 作为续接触发词
