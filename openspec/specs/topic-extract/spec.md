## ADDED Requirements

### Requirement: Topic Extract generates a 4-section topic document from existing source notes
AI SHALL read all `type: source` reading notes in the paper's `wiki/` directory, extract content relevant to the user's sub-question, and generate a `type: topic` markdown document with exactly 4 sections: 问题描述、符号定义、关键推导、核心公式.

#### Scenario: User requests a topic extraction
- **WHEN** user describes a sub-question (e.g., "帮我整理一下约束力和 Lagrange 乘子的关系")
- **THEN** AI reads all source notes in `wiki/`, identifies relevant sections, and generates `wiki/topic-<slug>.md`

#### Scenario: Topic document has correct frontmatter
- **WHEN** a topic document is generated
- **THEN** the YAML frontmatter SHALL contain `type: topic`, `id: topic-<slug>`, `source_papers` listing all referenced source note IDs, `created` and `last_updated` dates

#### Scenario: Topic document has exactly 4 body sections
- **WHEN** a topic document is generated
- **THEN** the body SHALL contain exactly these H2 sections in order: `## 问题描述`, `## 符号定义`, `## 核心公式`, `## 关键推导`

### Requirement: Symbol definitions use line-by-line list format
Each symbol definition SHALL be a list item with inline LaTeX followed by a colon and its description. No tables.

#### Scenario: Symbol definition format
- **WHEN** the 符号定义 section is written
- **THEN** each symbol SHALL appear as `- $<LaTeX>$：<description>` on its own line

### Requirement: Topic slug uses topic- prefix
All topic document filenames SHALL use the format `topic-<descriptive-slug>.md`.

#### Scenario: Topic file naming
- **WHEN** a topic about constraint force calculation is generated
- **THEN** the file SHALL be named like `wiki/topic-constraint-force-calc.md`

### Requirement: Index page updated with Topic section
After generating a topic document, `wiki/index.md` SHALL be updated to include a `## Topic 专题` section listing the new topic.

#### Scenario: Index page has Topic section
- **WHEN** a topic document is created
- **THEN** `wiki/index.md` SHALL contain a `## Topic 专题` heading with an entry like `- topic-<slug>: <brief description>`

#### Scenario: Topic section added to existing index
- **WHEN** `wiki/index.md` already exists but has no `## Topic 专题` section
- **THEN** the section SHALL be appended after the existing sections

### Requirement: Topic content is extracted and synthesized from source notes
The topic document content SHALL be derived from existing source reading notes, not from re-reading the PDF. The AI SHALL reorganize the extracted content around the sub-question's logical structure.

#### Scenario: Content sourced from existing notes
- **WHEN** a topic is generated
- **THEN** the 关键推导 and 核心公式 sections SHALL contain content traceable to the source notes' Architecture and Evidence sections

#### Scenario: Symbols are self-consistent
- **WHEN** a topic is generated
- **THEN** every symbol used in 关键推导 and 核心公式 SHALL be defined in 符号定义
