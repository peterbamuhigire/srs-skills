# SDD Phase-Boundary Contract

This contract adds deterministic controls for Spec-Driven Development feature
workspaces. It complements the standards-driven SRS lifecycle; it does not
replace IEEE/ISO requirements validation, traceability, or sign-off gates.

## Boundaries

| Boundary | Required evidence | Blocking failures |
|---|---|---|
| Spec → Plan | P1 requirements, coverage-map rows, implementation files, symbols/APIs | missing requirement coverage, empty file/symbol mapping |
| Plan → Tasks | every P1 requirement tagged, sequential task IDs, valid dependencies | untasked P1 requirement, missing dependency, cycle, oversized task file |
| Tasks → Implement | task state is authoritative; deferred work is explicit | `.completed` while active tasks remain |
| Implement → QC | implementation completion plus QC report | `.qc-passed` without a report containing a PASS verdict |

## Deterministic runner

Run from the engine root:

```powershell
python scripts/validate_sdd_phase_boundaries.py --feature-dir projects/<Project>/feature
```

Use `--stage spec-plan`, `--stage plan-tasks`, `--stage tasks-implement`, or
`--stage implement-qc` to run one boundary. Add `--json` for CI or an evidence
manifest. A missing required artifact is a failure, not an unassessed pass.

## Agent and hook integration

Agents may explain or repair a finding, but they cannot manufacture a PASS.
The validator is the preflight/release hook for environments without native
hooks. Native hooks should invoke the same command at plan, task, completion,
and release events. Persist overrides in the project evidence record with an
owner, reason, expiry, scope, and rollback; never record a gate bypass only in
conversation.
