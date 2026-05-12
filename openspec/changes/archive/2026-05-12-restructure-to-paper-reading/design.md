## Context

当前 `paper-wiki` skill 建立在一个复杂的知识库架构上：`raw/` + `kb/` 二级目录、topics/milestones 三模式层级、Three-Tree Mirroring 不变量、Proactive Write-back + journal dual-write 审计机制、Obsidian wikilink/Graph View 规则。实际使用场景是逐篇论文阅读和解读，这些机制带来了不必要的复杂度。

当前唯一的 wiki 实例位于 `Constraint Reaction Forces and Lagrange Multipliers in Multi-Body Systems/`，内含 2 篇论文的解读和 2 个 PDF。

## Goals / Non-Goals

**Goals:**
- 将 skill 从"知识库维护者"转型为"论文阅读解读助手"
- 以论文标题为文件夹的简洁目录结构
- 保留高价值的论文解读 sections（Essence → Open Questions 共 8 个）
- 新增 Sci-Hub 动态发现下载
- 新增扫描件 PDF 的 LLM 视觉直读能力
- 迁移现有论文数据到新结构

**Non-Goals:**
- 不构建跨论文的知识图谱或 milestone 体系
- 不支持 Obsidian 特有功能（wikilinks、Graph View）
- 不维护审计日志（journal）或操作日志（log.md）
- 不做 OCR 文字提取（用 LLM 视觉直读替代）

## Decisions

### D1: 目录结构 — 以论文标题为文件夹根

```
e:\PaperReading\
├── <论文标题>/
│   ├── <paper>.pdf
│   ├── wiki/
│   │   ├── index.md
│   │   ├── <main-slug>.md
│   │   ├── <related-slug>.md
│   │   └── figures/
│   │       ├── <main-slug>/
│   │       └── <related-slug>/
│   └── Related/
│       └── <related>.pdf
```

**Why**: 每篇论文自成一体，直觉明确（打开文件夹就是一篇论文的所有内容）。不需要理解 `raw/` vs `kb/` 的职责分离。

**Alternative**: 保持 `raw/` + `kb/` 分离但砍掉 topics → 仍然有认知负担，且 `raw/` 对单论文场景没有意义。

### D2: Related 论文 — Model A（只存 PDF，解读归属主论文）

Related 论文的 PDF 放在 `Related/`，但解读 `.md` 文件写在主论文的 `wiki/` 下。一篇 Related 论文的解读"属于"引用它的主论文上下文。

**Why**: 避免 Related/ 下出现嵌套的 wiki 结构，保持扁平。如果某篇 Related 论文日后需要独立深入研究，直接在顶层创建它自己的论文文件夹。

**Alternative**: Related 也有自己的 wiki/ → 导致 Related/ 内出现嵌套目录，结构变复杂。

### D3: 解读页 8 sections

保留：Essence, Factors, Architecture, Evidence, Critical Analysis, Relations, Transferable Inspirations, Open Questions。

删除：Feeds（依赖 topics）、Cognitive Shifts（审计性质，非解读内容）。

**Why**: 这 8 个 section 覆盖了"论文说了什么 → 怎么做的 → 结果如何 → 批判分析 → 与其他工作的关系 → 可迁移启发 → 未解问题"的完整阅读闭环。

### D4: 下载优先级链 — arXiv → S2 openAccess → Sci-Hub → 手动

```
1. arXiv 直接下载（最可靠）
2. Semantic Scholar openAccessPdf
3. Sci-Hub（动态发现镜像）
   - 搜索引擎搜 "sci-hub"
   - 提取前 5 个候选 URL
   - 依次尝试 <url>/<DOI>
   - 验证文件 > 1KB 且文件头为 %PDF
4. 手动放 PDF（最终 fallback）
```

**Why**: Sci-Hub 域名频繁变化，硬编码镜像列表会过时。搜索引擎动态发现无需维护。

**Alternative**: 硬编码镜像列表 → 需要人工维护，域名失效后无法自动恢复。

### D5: 扫描件 PDF — PyMuPDF 渲染 + LLM 视觉

```
检测：对每页 page.get_text()，大多数页面 < 50 字符 → 扫描件
处理：page.get_pixmap(dpi=200) → 逐页保存 PNG → read_file 视觉读取
清理：渲染图片为临时中间产物，解读写完后可删除
```

**Why**: 零额外依赖（PyMuPDF 已有），LLM 视觉对公式/图表的理解优于传统 OCR。

**Alternative**: Tesseract/PaddleOCR → 需要额外安装，公式识别差。Nougat/Marker → 需要 GPU，依赖重。

### D6: YAML frontmatter 瘦身

```yaml
---
type: source
id: <slug>
pdf_path: ../<slug>.pdf           # 主论文
# 或 ../Related/<slug>.pdf       # Related 论文
tags: [<domain>, year/YYYY-MM, venue/<name>]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
authors: [...]
aliases: [...]
---
```

删除：`milestone`、`raw_path`（改为 `pdf_path`）。

### D7: wiki/index.md 格式

```markdown
---
type: index
title: <论文完整标题>
wiki_language: zh-CN
last_updated: YYYY-MM-DD
---

# 论文解读导航

## 主论文
- <main-slug> (<authors>, <year>, <venue>)

## Related 论文解读
- <related-slug-1> (<authors>, <year>, <venue>)
- <related-slug-2> (<authors>, <year>, <venue>)
```

每个论文文件夹有自己独立的 index.md，不存在全局 index。

## Risks / Trade-offs

- **[跨论文关联丢失]** 砍掉 topics 后，不同论文文件夹之间没有结构化关联 → **Mitigation**: Relations section 仍然用文本描述论文间关系；如果将来需要，可以在顶层加一个全局 index
- **[Related 解读重复]** 如果同一篇 Related 论文出现在多个主论文的 Related/ 下，可能产生重复解读 → **Mitigation**: 实际发生时，将该论文升级为独立顶层文件夹
- **[Sci-Hub 可用性]** 搜索引擎可能屏蔽 Sci-Hub 结果，或 Sci-Hub 本身不可用 → **Mitigation**: Sci-Hub 只是 fallback，失败后仍有手动放 PDF 的兜底方案
- **[视觉读取 token 消耗]** 扫描件 PDF 逐页读取会消耗大量视觉 token → **Mitigation**: 仅在检测到无文本层时触发，大多数学术论文有文本层
- **[现有数据迁移]** 需要将现有论文文件夹内容重新组织 → **Mitigation**: 只有 1 个实例，手动迁移即可

## Migration Plan

1. 创建新的 `.codemaker/skills/paper-reading/` 目录
2. 将重写后的 SKILL.md 和更新的 templates 写入新目录
3. 将 `paper_extract_figures.py` 和 `paper_search.py` 复制到新目录（调整路径参数）
4. 迁移现有数据：重新组织 `Constraint Reaction Forces...` 文件夹的内部结构
5. 删除旧的 `.codemaker/skills/paper-wiki/` 目录
6. 验证新 skill 能正常触发和执行
