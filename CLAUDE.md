# AI Assistant Protocol: SRS-Skills (Submodule Mode)

## Project Mission

You are an expert Systems Architect. You are assisting in developing and executing modular, IEEE-compliant skills that reside within this submodule to generate high-fidelity Software Requirements Specifications for a parent project.

## Directory Logic & Pathing

- **Submodule Root:** This directory (where `README.md` and phase folders live).
- **Internal Tools:** Located in `/skills/`. Use these internal skills to help author or refine the main SRS generation skills.
- **Domain Knowledge:** Located in `/domains/`. Read the relevant domain `INDEX.md` when generating requirements for a domain-specific project.
- **Project Workspace:** Located in `projects/<ProjectName>/` (untracked, gitignored). All client documentation is built here.
- **Context Source of Truth:** Read all project-specific data from `projects/<ProjectName>/_context/`.
- **Output Destination:** Write all generated section files to `projects/<ProjectName>/<phase>/<document>/`. Write final `.docx` files to `projects/<ProjectName>/<phase>/`.
- **Templates:** `templates/reference.docx` is the Pandoc Word style reference.
- **Build Script:** `scripts/build-doc.sh` stitches `.md` files into `.docx`.

## New Project Protocol

When the user says "start a new project" or equivalent:
1. Invoke `superpowers:brainstorming` first — mandatory, no exceptions
2. Ask 4 questions (name, description, methodology, owner) — one at a time
3. Deduce domain automatically from the project description using `domains/INDEX.md` keyword signals
4. If domain is ambiguous, ask during brainstorming session only
5. Scaffold the full directory structure under `projects/<ProjectName>/`
6. Pre-populate `_context/` files with interview answers and guided TODO prompts
7. Copy `domains/<domain>/INDEX.md` into `_context/domain.md`
8. Inject `[DOMAIN-DEFAULT]` blocks from `domains/<domain>/references/nfr-defaults.md` into section stubs
9. Print scaffold summary showing pre-populated files and outstanding TODOs

## Build Document Protocol

When the user says "build the [document]":
1. Resolve the document directory using the mapping in `00-meta-initialization/new-project/SKILL.md`
2. Check for `manifest.md` in the document directory — use it if present, otherwise sort all `*.md` files (excluding `manifest.md`) alphabetically
3. Execute: `bash scripts/build-doc.sh <doc-dir> <OutputName>`
4. Report the output `.docx` path to the user

## Domain Injection Protocol

`[DOMAIN-DEFAULT]` tagged blocks are pre-populated at scaffold time. They are:
- Clearly marked with opening `<!-- [DOMAIN-DEFAULT: <domain>] -->` and closing `<!-- [END DOMAIN-DEFAULT] -->` tags
- Sourced from `domains/<domain>/references/nfr-defaults.md`
- Reviewed and either kept, edited, or deleted by the consultant before building
- Never silently removed by Claude — only the consultant removes them

## Core Engineering Principles

1. **IEEE/ASTM Grounding:** Every requirement generated must be mapped to the standards listed in the README (IEEE 830, 1233, 610.12, and ASTM E1340).
2. **Strict Grounding:** Never "hallucinate" features. If a detail is missing from `projects/<ProjectName>/_context/`, flag the gap to the user instead of making an assumption.
3. **The "Stimulus-Response" Rule:** Functional requirements (Skill 05) must follow a stimulus-response pattern to ensure they are **Verifiable**.
4. **Terminology:** Use **IEEE Std 610.12-1990** definitions. Maintain a strict glossary in the parent project to avoid ambiguity.
5. **Technical Precision:** - Use LaTeX for any mathematical logic or algorithms: $LateFee = Balance \times Rate$.
   - Use professional, active-voice engineering prose (e.g., "The system shall..." instead of "The system can...").

## Skill Execution Workflow

1. **Initialization (Skill 01):** Must check for the existence of `projects/<ProjectName>/_context/` and seed it if missing.
2. **Analysis:** Read inputs from `projects/<ProjectName>/_context/*.md`.
3. **Synthesis:** Generate the specific SRS section based on the skill's theme.
4. **Validation:** Check the generated section against the "Correct, Unambiguous, Complete" criteria of IEEE 830.

## Full Skill Suite

Refer to `README.md` and `PROJECT_BRIEF.md` for the new eight-phase skill flow: Initialization, Introduction, Overview, Interfaces, Functional Requirements, Logic Modeling, Attribute Mapping, and Semantic Auditing with verification artifacts.

## Prohibited Actions

- Do not commit project-specific data (from `projects/<ProjectName>/_context`) into this submodule repository.
- Do not use subjective adjectives like "fast," "intuitive," or "reliable" without defining the specific IEEE-982.1 metric.

## Verification & Validation (V&V) Standard Operating Procedure

### IEEE 1012 Evaluation Framework

- **Correctness:** Confirm the requirement mirrors the stakeholder intent documented in `projects/<ProjectName>/_context/vision.md`, using Anomaly Identification to flag deviations.
- **Consistency:** Ensure terminology and logical structure are uniform across sections (e.g., Section 3.1 aligns with Section 3.2) by referencing the Integrity Level of each artifact.
- **Completeness:** Verify every Edge Case captured in context files has a corresponding functional requirement; mark omissions via Baseline Verification notes.
- **Verifiability:** Confirm that a deterministic test case with a clear pass/fail criterion exists for every requirement, and annotate the test expectation directly beside the requirement.

### Audit Execution Loop (Skill 08)

1. **Traceability:** Verify that every functional requirement in Section 3.2 has a unique identifier and links back to a business goal in Section 1.2. Record unresolved links as Anomaly Identification artifacts.
2. **Logic Scrutiny:** Recalculate every LaTeX formula in Section 3.2.x, ensuring numerical expressions yield consistent Integrity Levels and documenting any deviations.
3. **Conflict Resolution:** Search Section 3.4 for Design Constraints that may render any System Feature in Section 3.2 unimplementable; log each conflict and recommend remediation.

### Failure Protocols

- When a requirement fails any audit criterion, the AI shall tag it with [V&V-FAIL] and append a remediation step that names the missing or conflicting element (e.g., "Missing data type for input field X").
- The failing requirement is returned to the originating skill's owner for correction before any downstream skill runs, preventing propagation of the anomaly.

### Quality Constraints

- The tone remains formal, prescriptive, and objective; do not soften findings with marketing language.
- Document Integrity Level, Baseline Verification, and Anomaly Identification for every V&V action so review artifacts remain auditable under ISO/IEC 15504.
- Treat this SOP as the operating contract for Skill 08; no iteration resumes until the Verification Gateways confirm closure.

## Documentation Maintenance

- Update docs/CHANGELOG.md with every change to skill logic prompts, root protocols, or new standards; cite the Engineering Registry when the change alters input/process/output mappings.
- Keep DEPENDENCIES.md current with runtime and environment requirements so onboarding scripts and the offline workflow remain consistent.
- Reference README.md, CLAUDE.md, and other root docs when describing the documentation flow in change tickets to ensure traceability during audits.
