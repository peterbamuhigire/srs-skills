# Hybrid Traceability — DoR and DoD pointer

This file satisfies the hybrid-gate requirement that every Water-Scrum-Fall project carries a single pointer at `07-agile-artifacts/definitions/dor-dod.md` linking the Definition of Ready, Definition of Done, and the baselined requirements they trace to.

## Canonical documents

- Definition of Ready — `03-dor/01-definition-of-ready.md`
- Definition of Done — `02-dod/01-definition-of-done.md`
- Sprint planning — `01-sprint-planning/01-sprint-planning.md`
- Velocity — `velocity.md`

## Baseline traces

Every DoR criterion references at least one baselined identifier (FR-, NFR-, BG-, CTRL-) from v1.0 per `_registry/baselines.yaml`. Sprint stories are traced to baseline in `_registry/baseline-trace.yaml`.

## Hybrid cadence

- Waterfall gate: Phase 02 SRS sign-off before any Phase 07 sprint may begin.
- Agile cadence: 2-week sprints. DoR gate on entry; DoD gate on acceptance.
- Sprint outputs are traced back to the baseline via `_registry/baseline-trace.yaml`.
