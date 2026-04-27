# Hybrid Operating Model

This document defines the canonical Water-Scrum-Fall contract for this repository.

## Purpose

Use this model when a project baselines requirements formally, executes incrementally through agile delivery, and returns to formal governance for release and audit control.

## Core Principle

Hybrid is not "some waterfall docs plus some sprints". It is a controlled handshake between:

- formal baseline scope
- sprint execution
- change control
- compliance and release governance

## Canonical Workspace Model

Hybrid projects live under `projects/<ProjectName>/`.

Required roots:

- `projects/<ProjectName>/_context/`
- `projects/<ProjectName>/_registry/`
- `projects/<ProjectName>/02-requirements-engineering/`
- `projects/<ProjectName>/07-agile-artifacts/`
- `projects/<ProjectName>/09-governance-compliance/`

## Minimum Hybrid Contract

### 1. Baseline Before Sprint Execution

Before sprint execution begins:

- Phase 02 requirements are reviewed and signed off
- the baseline is snapshotted
- `_registry/baselines.yaml` identifies the current baseline
- `_registry/baseline-trace.yaml` is created for waterfall-to-agile trace links

### 2. Agile Artefacts Must Stay Coupled to the Baseline

Sprint execution must not float free from the baseline.

At minimum:

- DoR references `BG-*`, `FR-*`, `F-*`, or `NFR-*` identifiers
- DoD references `CTRL-*` or named quality/compliance constraints
- sprint backlog items carry stable IDs
- `_registry/baseline-trace.yaml` maps baseline items to stories

### 3. Change Control Still Applies

When scope changes:

- baseline impact is recorded
- downstream design, testing, and governance artefacts are updated
- change-impact records and waivers are used where applicable

### 4. Governance Closes the Loop

Before release:

- sign-off records are captured
- audit and risk artefacts are updated
- an evidence pack can be built

## Required Hybrid Artefacts

- `_context/methodology.md`
- `_registry/baseline-trace.yaml`
- `_registry/baselines.yaml`
- `07-agile-artifacts/definitions/dor-dod.md`
- sprint artefacts under `07-agile-artifacts/`
- governance artefacts under `09-governance-compliance/`

## Supported Hybrid Patterns

### Pattern 1: Water-Scrum-Fall

- formal Phase 02 baseline
- agile execution in Phase 07
- formal release and governance closure in Phases 06 and 09

### Pattern 2: Baseline-With-Controlled-Increments

- stable high-level baseline
- increment-level change control for selected FR and NFR items

### Pattern 3: Regulated Agile Delivery

- agile execution allowed
- control, evidence, and sign-off requirements remain mandatory at each release boundary

## Validation Relationship

The runtime model is enforced through:

- `deterministic-gate-phase07.md`
- `deterministic-gate-phase09.md`
- `deterministic-gate-hybrid.md`
- `regulated-evidence-model.md`

## Anti-Patterns

Do not treat a project as valid Hybrid execution if:

- sprints do not reference the formal baseline
- baseline items have no implementing stories
- governance records are updated only after delivery is complete
- release evidence is detached from requirement and control IDs
