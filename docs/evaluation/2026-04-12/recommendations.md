# Recommendations

## System-Level Priorities

### 1. Build a Canonical Artifact Graph

Create a project-wide metadata model that tracks:

- artifact type
- artifact ID
- source inputs
- downstream dependencies
- version/baseline
- methodology applicability
- review status
- trace links

This should become the engine’s control plane. Every generated artifact should register into this graph.

Why this matters:

- enables deterministic traceability
- supports change impact analysis
- allows gate enforcement across phases
- makes Hybrid execution real instead of conceptual

### 2. Replace Advisory Quality Gates with Enforced Gates

Current gates are mostly prose. Convert them into executable checks:

- required section validation
- placeholder/TBD detection
- glossary consistency checks
- identifier uniqueness checks
- trace coverage thresholds
- NFR measurability checks
- threshold conflict detection
- missing dependency detection

Gate outputs should be machine-readable and block downstream progression unless explicitly waived.

### 3. Unify the Pathing Model

Pick one canonical runtime model and continue refactoring skill-local assets toward it.

Recommended model:

- `projects/<ProjectName>/_context/`
- `projects/<ProjectName>/<phase>/<document>/`
- `projects/<ProjectName>/artifacts/metadata/`
- `projects/<ProjectName>/build/`

Current status:

- root docs and repository protocols now treat this as the canonical model
- legacy `../project_context/` and `../output/` references are now explicitly documented as compatibility aliases

Next update targets:

- all SKILL files
- scripts
- helper prompts and templates that still imply the legacy model

This remains foundational. The ambiguity is reduced, but full automation and trust still require skill-level cleanup and stronger runtime abstraction.

### 4. Create a Single Validation Kernel

Consolidate assurance logic currently scattered across:

- semantic auditing
- requirements validation
- traceability engineering
- requirements metrics
- phase 09 governance

into a shared validation engine with pluggable rules per artifact type.

Recommended outputs:

- `validation-report.json`
- `validation-report.md`
- `gate-status.json`
- `waivers.md`

## Skill-Level Improvements

### 1. Strengthen Requirements Generation

For Waterfall and Agile alike:

- require stable identifiers at first creation
- add explicit source references for every requirement
- require inline acceptance/test oracle stubs
- require rationale for priority and scope classification
- detect compound requirements automatically

### 2. Strengthen Design Generation

Update HLD and LLD to require:

- architecture decision records
- rejected alternatives
- design rationale blocks
- interface responsibility mapping
- testability and operability considerations per design component

### 3. Strengthen Testing Documentation

Phase 05 now follows ISO/IEC/IEEE 29119-3 with deterministic gate checklists, incident logs, and completion reports, but the rest of the engine needs similar clause-level proof. Build on the existing improvements by:

- formalizing technique selection and tracing it to the deterministic checklist
- documenting regression, UAT, and Test Data Management sections per 29119-3
- embedding incident reporting and test completion reporting templates inside every project workspace
- codifying explicit environment/automation fidelity controls linked to the strategy

### 4. Strengthen Compliance Documentation

Compliance docs should map:

- obligation
- control
- requirement
- design element
- verification/test evidence
- operational evidence owner

Without this, compliance output remains mostly narrative.

### 5. Strengthen End-User Documentation

Add stronger operating rules for:

- information architecture
- persona-specific onboarding
- task-first organization
- procedure verification walk-throughs
- release-to-user-doc consistency checks

## New Skills to Add

### 1. ADR Tracking

Purpose:

- record architecture decisions, alternatives, trade-offs, approval state, and impacted artifacts

Why:

- essential for enterprise architecture and regulated design review

### 2. Change Impact Analysis

Purpose:

- evaluate the downstream impact of requirement, design, or compliance changes

Why:

- critical for maintenance, governance, and audit defensibility

### 3. Requirements-to-Code Traceability

Purpose:

- map requirement IDs to implementation modules, APIs, schema objects, tests, and deployment controls

Why:

- closes the biggest current enterprise traceability gap

### 4. Documentation Consistency Engine

Purpose:

- scan the entire artifact set for terminology drift, conflicting thresholds, duplicate requirements, broken links, and missing references

Why:

- this is required for repeatable enterprise quality

### 5. Compliance Control Library

Purpose:

- provide reusable, domain-specific control catalogs and evidence expectations

Suggested domains:

- healthcare
- finance
- government/public sector
- privacy/data protection

### 6. Formal Review Pack Generator

Purpose:

- assemble PSR/CSR/release-review evidence packs including findings, waivers, signatures, open risks, and trace summaries

Why:

- directly supports regulated and enterprise governance workflows

### 7. Baseline and Delta Comparator

Purpose:

- compare document versions, show semantic changes, update impacted trace links, and preserve approved history

Why:

- world-class documentation systems are iterative, not one-shot

## System Redesign Recommendations

### 1. Move from Prompt-Centric to Model-Centric Generation

Introduce structured intermediate representations for:

- requirements
- interfaces
- controls
- tests
- risks

Generate final documents from these models rather than composing everything directly from prose prompts.

### 2. Introduce Artifact Schemas

Define schemas for each artifact type so the engine can validate:

- mandatory fields
- identifier patterns
- allowed statuses
- required links
- phase-specific entry and exit criteria

### 3. Add Waiver and Exception Management

Any enterprise-grade system needs formal handling for:

- accepted deficiencies
- deferred controls
- partial compliance
- risk ownership

### 4. Add Methodology Synchronization Rules

For Hybrid delivery, define exactly how:

- PRD objectives feed backlog epics
- formal requirements map to user stories
- agile increments update design baselines
- governance consumes both formal and agile artifacts

### 5. Add Evidence-Oriented Domain Packages

Each regulated domain should include:

- control catalog
- required artifacts
- required review gates
- test obligations
- audit evidence checklist
- common failure patterns

## Implementation Order

1. Unify paths and runtime model
2. Build canonical artifact graph
3. Build shared validation kernel
4. Add consistency engine and delta comparison
5. Add ADR, change impact, and code-traceability skills
6. Deepen regulated-domain control libraries

That sequence turns the repository from a strong documentation framework into a true documentation intelligence platform.
