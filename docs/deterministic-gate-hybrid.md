# Deterministic Gate: Hybrid

## Scope

The Hybrid gate validates Water-Scrum-Fall synchronisation for workspaces whose methodology is declared as `hybrid`.

## Enforced Checks

- `hybrid.traces.missing`
- `hybrid.traces.unknown_trace`
- `hybrid.traces.orphan_baseline`
- `hybrid.dor_dod_missing`
- `hybrid.dor_dod_decoupled`

## Intent

- Require `_registry/baseline-trace.yaml`
- Require every agile story to trace to a baselined requirement or control
- Require every baseline item to have implementing agile work
- Require a coupled `07-agile-artifacts/definitions/dor-dod.md`
- Require DoR/DoD references to `FR-*`, `NFR-*`, or `CTRL-*` identifiers

## Pass Condition

Formal baseline scope and agile execution remain synchronised through explicit trace files and baseline-aware ready/done criteria.
