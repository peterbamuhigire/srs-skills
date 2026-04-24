# System Reconstruction

## What This Repository Actually Is

This repository is now best described as a **phase-based SDLC documentation platform with a validation kernel**.

Its current operating model is:

1. Scaffold a project workspace
2. Select methodology and domain context
3. Populate project context under `projects/<ProjectName>/_context/`
4. Generate or curate phase artifacts
5. Sync registries and validate the project workspace
6. Record waivers/sign-off where needed
7. Assemble evidence packs and downstream document outputs

That is materially stronger than the earlier picture of a mainly stateless prompt system.

## Core Operating Model

### 1. Phase Structure

The repository still uses the same phase spine:

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

The difference is that this phase model is now connected to executable gates in the `engine/` package.

### 2. Runtime Kernel

The `engine/` package now acts as the repository's control plane.

Current implemented capabilities include:

- artifact graph construction
- phase gate registry
- workspace loading
- registry sync for identifiers and glossary terms
- hybrid synchronization checks
- waiver loading and expiry enforcement
- sign-off ledger handling
- baseline snapshot and diff support
- evidence-pack ZIP assembly
- doctor diagnostics
- markdown, JUnit, and SARIF reporting

The presence of `python -m engine.cli` is the clearest sign that the repository has crossed from guidance into runtime enforcement.

### 3. Context Injection

The source of truth is the project workspace:

- `projects/<ProjectName>/_context/`
- `projects/<ProjectName>/_registry/`
- project-local phase directories

The root documentation now aligns more clearly with this model, even though some skill-local assets still preserve legacy compatibility assumptions.

### 4. Validation Flow

The current validation flow is roughly:

1. Load a project workspace
2. Build an artifact graph from markdown artifacts
3. Run kernel checks and phase gates
4. Apply hybrid checks where applicable
5. Apply waivers
6. Emit blocking or passing status
7. Optionally render markdown/JUnit/SARIF results

This is a genuine validation kernel, even if its reasoning depth is still bounded.

## Real Project Flow

### Step A: Project Initialization

Project initialization now has a stronger runtime path because scaffolding is exposed through the engine CLI, not only through skills.

### Step B: Methodology Selection

Methodology branching still supports:

- Waterfall
- Agile
- Hybrid

Hybrid is also now reflected in explicit validation logic rather than being only a routing concept.

### Step C: Content Generation Across Phases

The skill system still generates the majority of the actual document content. That has not changed. What has changed is that generated artifacts now sit inside a more coherent validation and governance environment.

### Step D: Registry and Governance Operations

The repository now has a real `_registry/` operating model, including:

- identifier registry
- glossary registry
- waivers
- sign-off ledger
- baseline data
- ADR catalogues and change-impact support where present

This substantially improves consistency management and governance repeatability.

### Step E: Packaging and Review

The engine can now assemble evidence packs and emit validation reports, while the existing document-build layer still supports final packaging such as `.docx` workflows.

## What Defines the Standard vs What Generates vs What Validates

### What Defines the Standard

The normative layer still lives primarily in:

- `CLAUDE.md`
- `AGENTS.md`
- `README.md`
- `skill_overview.md`
- the phase skills
- domain materials

### What Generates Outputs

The skills remain the main content generators across phases `01` through `09`.

### What Validates Outputs

This is the biggest change in the reconstruction. Validation is no longer only dispersed inside skills. It is now centralized substantially in `engine/`, especially through:

- the CLI
- the gate registry
- the artifact graph
- checks under `engine/checks`
- gates under `engine/gates`
- registry schemas
- pack/reporting workflows

## Actual System Characterization

The most accurate reconstruction now is:

- It is **not** a simple markdown repository.
- It **is** a multi-phase documentation operating model.
- It **does** support real project flow from initialization to governance.
- It **does** contain a real validation kernel with deterministic checks.
- It **does not yet** provide full semantic or audit-grade assurance across every phase and domain.

The repository now has the shape and much of the machinery of an enterprise documentation engine. The next maturity step is not inventing the engine. It is deepening the assurance model already in place.
