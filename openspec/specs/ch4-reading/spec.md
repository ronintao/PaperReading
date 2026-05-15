## ADDED Requirements

### Requirement: Batch reading of scanned chapter pages
The system SHALL read Ch.4 scanned pages (page_130 ~ page_164) in batches of ~12-15 pages each, producing one intermediate part file per batch.

#### Scenario: First batch reading
- **WHEN** Batch 1 is executed (page_130 ~ page_142 estimated)
- **THEN** a part file `wiki/ch4-parts/ch4-part1.md` SHALL be created with metadata headers (pages covered, sections covered, next batch start) and extracted content (概念定义, 符号定义, 核心论点, 工程应用与实例)

#### Scenario: Continuation batch reading
- **WHEN** a subsequent batch is executed
- **THEN** the part file SHALL read the previous part's `Next batch starts` metadata to determine the correct starting page

#### Scenario: Final batch completion
- **WHEN** the last batch covers page_164 (the final Ch.4 page)
- **THEN** the part file's metadata SHALL record `Next batch starts: none (chapter complete)`

### Requirement: Part file merge into final chapter note
After all batches are complete, the system SHALL merge all part files into a single `wiki/ch4-numerical-methods-kinematics.md` following the chapter-notes template.

#### Scenario: Successful merge
- **WHEN** all part files exist and the last part indicates chapter complete
- **THEN** the merged file SHALL contain: YAML frontmatter (type: chapter-notes, parent: computer-aided-kinematics-and-dynamics, chapter: 4), 章节定位, 概念定义 (sorted by page, deduplicated), 符号定义 (grouped and deduplicated), 核心论点 (reorganized by section order), 工程应用与实例, 与全书的关系

### Requirement: Index update
After the final chapter note is created, `wiki/index.md` SHALL be updated with a Ch.4 entry.

#### Scenario: Index entry added
- **WHEN** `wiki/ch4-numerical-methods-kinematics.md` is created
- **THEN** `wiki/index.md` SHALL contain an entry under 逐章精读笔记: `[Ch.4 Numerical Methods in Kinematics](ch4-numerical-methods-kinematics.md) — <one-line summary>`

### Requirement: Temporary file cleanup
After the human confirms the final note is satisfactory, temporary files SHALL be deleted.

#### Scenario: Cleanup execution
- **WHEN** the human confirms the merged chapter note
- **THEN** `temp_ch4/` (rendered PNGs) and `wiki/ch4-parts/` (intermediate part files) SHALL be deleted
