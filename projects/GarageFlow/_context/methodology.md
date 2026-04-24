---
methodology: hybrid
domain: automotive
---

# Methodology — GarageFlow

methodology: hybrid

## Rationale

Hybrid (Water-Scrum-Fall) is chosen because GarageFlow is a multi-tenant SaaS platform with a regulated scope (PCI, data protection, tax e-invoicing) and requires a baselined SRS for audit. Once the SRS is signed off, implementation runs Agile sprints against a prioritised backlog, with release-train gates at each phase boundary.

## Waterfall portion

- Phases 01 → 06 of the skill suite produce a signed-off SRS, SDD, and V&V plan.
- `hybrid-synchronization` skill invoked after Phase 02 sign-off.

## Agile portion

- Phase 07 onward runs sprints of 2 weeks.
- Release-train gates at each phase closure use `python -m engine baseline snapshot`.
- Change Impact Analysis required for every baselined-FR change.

## Team

- Size: 2 (Peter Bamuhigire + 1).
- Peter handles architecture, skills orchestration, and hands-on engineering.

## Hybrid synchronisation gate

The kernel will block Phase 07 outputs until `python -m engine validate projects/GarageFlow` passes the `hybrid` gate.

## Cadence

- Daily standup (async acceptable for a 2-person team).
- Weekly planning.
- Phase-closure retro aligned with baseline snapshot.
