# System Reconstruction

## What This Repository Actually Is

This repository is a **dual-purpose SDLC system**:

1. a portable skill catalog for Claude Code and Codex
2. an executable SDLC documentation validation engine

It is not just a markdown collection. It contains a runtime kernel under `engine/`, a large skill catalog under `skills/skills/`, domain packs under `domains/`, and project workspaces under `projects/`.

## Current Operating Model

The intended flow is:

1. Select methodology and domain context.
2. Scaffold or prepare a `projects/<ProjectName>/` workspace.
3. Populate `_context/` with project truth.
4. Generate or curate phase artifacts.
5. Sync `_registry/` data.
6. Validate with `engine.cli`.
7. Record waivers and sign-offs.
8. Create baselines and evidence packs.
9. Export or deliver documents.

This is a coherent operating model, but the current checkout does not yet prove it cleanly end to end.

## Core Components

### 1. Phase Spine

The repository includes the lifecycle phases:

- `01-strategic-vision`
- `02-requirements-engineering`
- `03-design-documentation`
- `04-development-artifacts`
- `05-testing-documentation`
- `06-deployment-operations`
- `07-agile-artifacts`
- `08-end-user-documentation`
- `09-governance-compliance`

The skill catalog also includes `00-meta-initialization` for project and methodology selection.

### 2. Runtime Kernel

The `engine/` package provides:

- CLI commands
- workspace loading
- artifact graph construction
- phase gate registry
- checks under `engine/checks`
- phase gates under `engine/gates`
- identifier and glossary registries
- waiver handling
- sign-off handling
- baseline snapshot and diff
- sync
- evidence-pack assembly
- Markdown, JUnit, and SARIF reporting
- doctor diagnostics

This is the strongest evidence that the project has crossed from guidance into executable governance.

### 3. Skill Catalog

The catalog contains 240 `SKILL.md` entrypoints. Most are under `skills/skills/`, while a few remain at the first `skills/` level.

The catalog covers:

- software engineering baseline
- architecture
- databases
- testing
- deployment
- reliability
- observability
- security
- UX and product
- AI systems
- mobile
- SaaS and ERP
- language and framework skills
- SDLC documentation skills

Current state:

- 225 of 240 pass quick validation
- 15 fail and need normalization
- contract gate reports 0 errors but 17 warnings

### 4. Domain Packs

Domain packs exist for:

- agriculture
- automotive
- education
- finance
- government
- healthcare
- logistics
- retail
- Uganda

They provide domain context, feature expectations, controls, obligations, evidence expectations, and NFR/security defaults. They are useful context packs, not yet complete compliance rule engines.

### 5. Project Workspaces

Current visible workspaces:

- `AcademiaPro`
- `BIRDC-ERP`
- `LonghornERP`
- `Maduuka`
- `Medic8`

The previously claimed `_demo-hybrid-regulated` proof workspace is not present. This is the largest mismatch between documentation, tests, and repository state.

## What Defines, Generates, and Validates

### Defines Standards

- `CLAUDE.md`
- `AGENTS.md`
- `README.md`
- `skill_overview.md`
- `docs/pathing-model.md`
- `docs/standards-clause-registry.md`
- phase and domain documentation

### Generates Outputs

- portable skills
- phase skills
- domain references
- templates and scripts
- project-specific context and artifacts

### Validates Outputs

- `engine/`
- quick skill validator
- contract gate
- engine tests
- project validation commands
- evidence-pack generation

## Actual System Characterization

The repository is:

- a serious SDLC documentation engine
- a broad portable skill catalog
- a strong internal consulting accelerator
- a validation-backed governance system

The repository is not yet:

- a fully self-proving audit platform
- a cleanly packaged product distribution
- a fully normalized skill system
- a requirements-to-code-to-runtime assurance engine
- a green end-to-end proof system from current checkout

## Reconstruction Conclusion

The system architecture is strong. The current weakness is evidence discipline. To become world-class, the repository must make its best claims reproducible: green tests, green proof workspace, clean skill validation, clean realistic project validation, and traceability beyond documents into implementation and runtime reality.
