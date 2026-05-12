## ADDED Requirements

### Requirement: Convert any markdown file to MHT format
The skill SHALL convert a markdown file (with LaTeX formulas, images, tables, code blocks, callouts) to a single MHT file with all resources embedded.

#### Scenario: Basic markdown to MHT conversion
- **WHEN** user requests MHT export of a markdown file (e.g., "导出成 mht", "export to mht")
- **THEN** the skill SHALL generate a `.mht` file in the same directory as the input `.md` file

#### Scenario: Output file naming
- **WHEN** input file is `wiki/topic-constraint-force-calc.md`
- **THEN** output file SHALL be `wiki/topic-constraint-force-calc.mht`

### Requirement: LaTeX formulas rendered as PNG images
All LaTeX formulas (inline `$...$` and block `$$...$$`) SHALL be rendered to PNG images using matplotlib with usetex=True and embedded in the MHT file.

#### Scenario: Block formula rendering
- **WHEN** markdown contains `$$F^C = -\phi_r^T \lambda$$`
- **THEN** the MHT SHALL contain a centered PNG image of the rendered formula

#### Scenario: Inline formula rendering
- **WHEN** markdown contains text like `约束力 $F^C$ 与乘子 $\lambda$`
- **THEN** inline formulas SHALL be rendered as small PNG images with `vertical-align:middle` and height matching surrounding text

#### Scenario: Formula render failure fallback
- **WHEN** a LaTeX formula fails to render
- **THEN** the formula source text SHALL be displayed as inline code with a distinct color

### Requirement: Images embedded in MHT
All referenced images (figures, formula PNGs) SHALL be base64-encoded and included as MIME parts in the MHT file.

#### Scenario: Figure image embedding
- **WHEN** markdown contains `![alt](figures/slug/figure_1.png)`
- **THEN** the image SHALL be embedded as a MIME part with Content-Transfer-Encoding: base64

#### Scenario: Missing image handling
- **WHEN** a referenced image file does not exist
- **THEN** a visible error placeholder SHALL appear in the MHT output

### Requirement: MHT structure is WizNote compatible
The MHT file SHALL use MIME multipart/related structure with UTF-8 HTML content and base64-encoded image parts.

#### Scenario: WizNote can import the MHT
- **WHEN** the generated MHT file is imported into WizNote
- **THEN** it SHALL display with proper formatting including headings, styles, formulas, and images

#### Scenario: MHT MIME headers
- **WHEN** an MHT file is generated
- **THEN** it SHALL contain: MIME-Version 1.0, Content-Type multipart/related, UTF-8 charset for HTML part, base64 encoding for all image parts

### Requirement: Markdown elements preserved in HTML
The conversion SHALL handle: headings (H1-H6), bold, italic, markdown links, tables with borders, fenced code blocks with monospace font and background, blockquote/callout blocks with colored left border, and bullet lists with nesting.

#### Scenario: Code block styling
- **WHEN** markdown contains a fenced code block
- **THEN** the MHT SHALL render it with monospace font (Consolas) and light gray background

#### Scenario: Callout styling
- **WHEN** markdown contains `> [!note]` or `> [!abstract]`
- **THEN** the MHT SHALL render it with a colored left border (green for note, blue for abstract)

#### Scenario: Table rendering
- **WHEN** markdown contains a pipe table
- **THEN** the MHT SHALL render it as an HTML table with borders and bold header row

### Requirement: Skill operates independently of paper-reading
The md-to-mht skill SHALL work on any markdown file, not limited to paper reading notes. It SHALL have no dependency on the paper-reading skill.

#### Scenario: Convert arbitrary markdown
- **WHEN** user provides any `.md` file path
- **THEN** the skill SHALL convert it to MHT regardless of whether it has paper-reading YAML frontmatter

### Requirement: MiKTeX PATH handling
The conversion script SHALL automatically locate MiKTeX binaries if not in system PATH.

#### Scenario: MiKTeX installed but not in PATH
- **WHEN** MiKTeX is installed at the default location but not in system PATH
- **THEN** the script SHALL detect and add the MiKTeX bin directory to the process PATH
