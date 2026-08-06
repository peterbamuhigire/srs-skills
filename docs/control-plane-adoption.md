# Control-plane adoption

This engine adopts the shared ten-engine contract defined in
`C:\wamp64\www\skills-web-dev\docs\engine-control-plane.md` and registered in
`engine-control-plane.json`. SRS doctrine remains authoritative for
requirements, architecture, testing, governance, and release evidence.

## Local roles and commands

| Role | Responsibility | Boundary |
|---|---|---|
| Requirements validator | Check completeness, consistency, feasibility, and test oracles. | Does not approve its own requirement changes. |
| Traceability auditor | Reconcile requirements, design, tasks, tests, and evidence. | Reports gaps; does not silently invent coverage. |
| Standards reviewer | Verify current standards and mandated terminology. | Unverified standards claims remain `NOT ASSESSED`. |

Use the real thin command surfaces `validate`, `validate-skills`, `baseline`,
`pack`, `signoff`, and `sync`, plus `scripts/create_sdd_handoff.py` for the
`stop` hook, to route to canonical SRS skills and validators.

## Hook contract

- `preflight` confirms the feature workspace, selected SDD stage, permissions,
  and applicable cross-engine routes.
- `context` loads the authoritative specification, source register, and prior
  decisions; duplicate or stale copies are flagged.
- `before_write` checks scope, change impact, acceptance oracles, and
  persistent-waiver fields (owner, reason, expiry, scope, rollback).
- `after_write` runs the relevant validator and updates traceability and
  evidence records.
- `release` requires the SDD phase-boundary validator, tests, standards
  evidence, reviewer sign-off, and a resumable handoff.
- `stop` records the current phase, completed checks, blockers, open risks,
  and next owner; interruption is never completion.

Where native hooks are unavailable, use repository scripts, CI, or an explicit
skill step. Safety and release failures must fail closed or be `NOT ASSESSED`.
