# System Reconstruction

## What This Repository Actually Is

This repository is a **stateless documentation engine** intended to sit beside client projects and generate project-specific SDLC artifacts from structured context plus domain defaults. Its operating model is:

1. Initialize a project workspace
2. Select methodology
3. Populate project context
4. Run phase skills in sequence or in defined subsets
5. Generate markdown artifacts
6. Optionally stitch them to `.docx`
7. Run quality, traceability, audit, compliance, and risk reviews

The engine itself is committed. Client documentation is expected to live under `projects/<ProjectName>/` and stay untracked.

## Core Operating Model

### 1. Phase Structure

The repository is organized into phases:

- `00-meta-initialization`
- `01-strategic-vision`
- `02-requirements-engineering`
- `03-design-documentation`
- `04-development-artifacts`
- `05-testing-documentation`
- `06-deployment-operations`
- `07-agile-artifacts`
- `08-end-user-documentation`
- `09-governance-compliance`

This is the control spine of the engine.

### 2. Context Injection

The intended source of truth is project context under `projects/<ProjectName>/_context/`, but many individual skills still reference legacy `../project_context/` and `../output/` paths. Operationally, the system depends on:

- `vision.md`
- `features.md`
- `tech_stack.md`
- `business_rules.md`
- `quality_standards.md`
- `glossary.md`
- plus additional artifacts such as `stakeholders.md`, `personas.md`, `metrics.md`, `quality-log.md`

The quality of the engine is explicitly tied to context density. This is a strength and a weakness:

- Strength: outputs are meant to be grounded
- Weakness: missing context frequently causes skill failure or inference pressure

### 3. Output Generation

Generated artifacts are expected to be written into project phase directories and/or output locations, then stitched to `.docx` via `scripts/build-doc.sh`.

`build-doc.sh` is one of the few genuinely executable engine components:

- reads a target document directory
- uses `manifest.md` if present, otherwise alphabetical fallback
- runs Pandoc with a Word reference template

This means the final packaging layer is real, but the generation and validation layers are still mostly instruction-driven.

## Real Project Flow

### Step A: Project Initialization

Two related mechanisms exist:

- `00-meta-initialization/SKILL.md` selects methodology and generates a documentation roadmap
- `00-meta-initialization/new-project/SKILL.md` scaffolds a project workspace

The new-project scaffold is substantial. It creates:

- `projects/<ProjectName>/`
- `_context/`
- phase directories
- export scripts
- `DOCUMENTATION-STATUS.md`
- domain profile injection

This is one of the strongest pieces of the engine because it frames a project as an evolving documentation program rather than isolated document prompts.

### Step B: Methodology Selection

Methodology handling is explicit:

- Waterfall for formal SRS-driven work
- Agile for story-driven work
- Hybrid for mixed documentation modes

Phase `00` attempts recommendation based on:

- regulatory signals
- project maturity
- workflow indicators
- repository characteristics

`CLAUDE.md` adds a more specific hybrid heuristic around Water-Scrum-Fall patterns.

This is conceptually strong, but practically shallow in one respect: Hybrid is mostly a routing idea, not a deeply modeled artifact synchronization strategy.

### Step C: Strategic Vision

Phase `01` generates upstream business and product framing:

- vision statement
- PRD
- business case
- lean canvas

These are meant to define the intent that downstream requirements and governance will trace back to. In system terms, these are the first major "source artifacts."

### Step D: Requirements Engineering

This is the heart of the engine.

There are three layers:

- `fundamentals/`
- `waterfall/`
- `agile/`

#### Waterfall Track

The Waterfall pipeline is a sequential SRS generator:

1. Initialize SRS
2. Context engineering
3. Descriptive modeling
4. Interface specification
5. Feature decomposition
6. Logic modeling
7. Attribute mapping
8. Semantic auditing
9. Use case modeling

This is the most "engine-like" subsystem because it includes real Python scripts for several stages. However, those scripts reveal a key issue: the implementation is partly mechanical and sometimes simplistic relative to the enterprise claims.

Examples:

- `feature_decomposition.py` turns feature rows into requirement-like text, but uses generic transformations and canned error behavior
- `semantic_auditing.py` performs useful structural checks, weak-word detection, section presence checks, and some traceability logic, but it is not a full semantic verifier
- `context_engineering.py` includes hard-coded assumptions such as default project naming and domain-specific framing that can leak into unrelated projects

#### Agile Track

The Agile track is prompt-led:

- user story generation
- acceptance criteria
- story mapping
- backlog prioritization

This is usable and reasonably well specified, but lighter than the Waterfall pipeline. It is more a disciplined prompt workflow than a strongly enforced artifact compiler.

#### Fundamentals Layer

The fundamentals layer wraps both methods:

- stakeholder analysis
- elicitation
- BRD
- analysis
- conceptual data modeling
- requirements patterns
- validation
- management
- traceability engineering
- metrics
- reuse

This layer matters because it defines much of the engine’s actual quality standard. The most important skill here is `10-requirements-metrics`, which acts as the closest thing to a formal quality gate.

### Step E: Design Documentation

Phase `03` consumes requirements and generates:

- HLD
- LLD
- API specification
- database design
- UX specification
- infrastructure design

This phase is well structured and has strong traceability intent. HLD is defined as the bridge from requirements to architecture, with Mermaid-based visualizations and requirement linkage. It is one of the engine’s strongest authoring phases, but it still relies on model compliance rather than deterministic diagram or dependency validation.

### Step F: Development, Testing, Deployment, User Documentation

Phases `04`, `05`, `06`, and `08` extend the documentation chain beyond design:

- technical specification, coding guidelines, environment setup, contribution guide
- test strategy, test plan, test report
- deployment guide, runbook, monitoring, infrastructure docs
- user manual, installation guide, FAQ, release notes

This is where the repository distinguishes itself from narrower SRS generators. It aims to create a full documentation estate, not just requirements documents.

### Step G: Agile Operational Artifacts

Phase `07` adds:

- sprint planning
- definition of done
- definition of ready
- retrospective template

This phase supports real team operation, especially for Hybrid programs where formal upstream docs coexist with agile execution artifacts.

### Step H: Governance and Validation

Phase `09` is the terminal assurance phase:

- traceability matrix
- audit report
- compliance documentation
- risk assessment

This is where the engine claims audit readiness.

In theory, this phase closes the loop from:

- business goals
- requirements
- design
- tests
- compliance obligations

In practice, this phase is strong in structure and weak in enforcement depth. It can produce audit-shaped artifacts, but it does not yet prove that the links are correct with the rigor expected in enterprise governance tooling.

## What Defines the Standard vs What Generates vs What Validates

### Skills That Define the Standard

These are the normative control documents:

- `CLAUDE.md`
- `README.md`
- `skill_overview.md`
- `00-meta-initialization/*`
- `02-requirements-engineering/fundamentals/*`
- domain `INDEX.md` files and domain defaults

These documents define:

- acceptable methods
- standards references
- pathing conventions
- quality rules
- expected outputs
- audit vocabulary

### Skills That Actually Generate Outputs

Primary generators include:

- Phase `01` strategic docs
- Phase `02` waterfall/agile requirements skills
- Phase `03` design skills
- Phase `04` implementation-facing docs
- Phase `05` test docs
- Phase `06` deployment/ops docs
- Phase `07` agile delivery docs
- Phase `08` end-user docs

The generation implementation is mixed:

- some phases use detailed SKILL instructions only
- some phases use `logic.prompt`
- some Waterfall skills use Python scripts

### Skills That Validate Outputs

Validation is spread across:

- `02-requirements-engineering/waterfall/08-semantic-auditing`
- `02-requirements-engineering/fundamentals/during/07-requirements-validation`
- `02-requirements-engineering/fundamentals/after/09-traceability-engineering`
- `02-requirements-engineering/fundamentals/after/10-requirements-metrics`
- `09-governance-compliance/*`

This is a good architecture pattern. The issue is not absence of validation stages. The issue is that many checks are still rhetorical rather than machine-enforced.

## Domain Influence

Domains are injected through:

- `domains/INDEX.md`
- per-domain `INDEX.md`
- `references/nfr-defaults.md`
- regulations, security baselines, architecture patterns, and feature modules

This gives the engine a vertical-specific grounding mechanism. For example:

- healthcare adds HIPAA/FHIR-oriented defaults
- finance adds PCI/SOX framing
- Uganda adds DPPA/public-sector specific concerns

This is useful and important. However, domain influence currently looks strongest at the default requirement and advisory layer, not as a full regulatory control model with evidence obligations and testable control mappings.

## Actual System Characterization

The most accurate reconstruction is:

- It is **not** a simple markdown repository.
- It **is** a multi-phase documentation operating model.
- It **does** support real project flow from initialization to governance.
- It **does not yet** provide world-class enforcement, consistency control, or audit-grade deterministic validation.

The repo has the shape of an enterprise documentation engine. The next maturity step is turning its prose-based discipline into executable discipline.
