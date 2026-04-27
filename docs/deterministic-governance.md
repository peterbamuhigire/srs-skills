# Deterministic Governance

This document is the repo-level index for the executable gate model implemented in `engine/`.

## Purpose

Use this file to understand which deterministic gate documents describe the runtime contract:

- `deterministic-gate-phase01.md`
- `deterministic-gate-phase02.md`
- `deterministic-gate-phase03.md`
- `deterministic-gate-phase04.md`
- `deterministic-gate-phase05.md`
- `deterministic-gate-phase06.md`
- `deterministic-gate-phase07.md`
- `deterministic-gate-phase08.md`
- `deterministic-gate-phase09.md`
- `deterministic-gate-hybrid.md`

## Runtime Contract

The canonical validation path is:

1. Load a workspace under `projects/<ProjectName>/`
2. Build the artifact graph
3. Run kernel and phase gates
4. Run the Hybrid gate when methodology is `hybrid`
5. Apply waivers
6. Emit blocking findings or pass status

## Gate Coverage

### Phase 01

See `deterministic-gate-phase01.md` for canonical context inputs and feature-to-stakeholder checks.

### Phase 02

See `deterministic-gate-phase02.md` for requirement-quality, stimulus-response, identifier, and glossary checks.

### Phase 03

See `deterministic-gate-phase03.md` for design sufficiency, ADR, interface, data-model, NFR-linkage, and threat-model checks.

### Phase 04

See `deterministic-gate-phase04.md` for development-standards, environment-setup, contribution-guide, and FR-linked technical-spec checks.

### Phase 05

See `deterministic-gate-phase05.md` for test structure, oracle quality, evidence, coverage, and completion checks.

### Phase 06

See `deterministic-gate-phase06.md` for deployment rollback, runbook escalation, monitoring, infrastructure, go-live, and change-window checks.

### Phase 07

See `deterministic-gate-phase07.md` for DoR/DoD, sprint-artifact IDs, retro action ownership, and velocity-history checks.

### Phase 08

See `deterministic-gate-phase08.md` for user-manual screenshots, release-note traceability, and FAQ completeness checks.

### Phase 09

See `deterministic-gate-phase09.md` for governance traceability, audit, risk, waivers, controls, obligations, ADR catalogue, change-impact, baseline, sign-off, and evidence-pack checks.

### Hybrid

See `deterministic-gate-hybrid.md` for Water-Scrum-Fall synchronisation checks built on baseline traces and coupled DoR/DoD references.

## Related Contracts

- `hybrid-operating-model.md`
- `regulated-evidence-model.md`
- `standards-clause-registry.md`

## Validation Commands

- `python -m engine.cli validate projects/<ProjectName>`
- `python -m engine.cli sync projects/<ProjectName>`
- `python -m engine.cli baseline snapshot projects/<ProjectName> --label <label>`
- `python -m engine.cli pack projects/<ProjectName> --out <zip-path>`
