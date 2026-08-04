<!-- Source basis: XP 2026; Platform Enterprise early release chapters 1-2; Designing for AI early release chapters 1-4; MSC Software Magazine Winter 2019; Applying the Kaizen in Africa (2018). -->

# SRS Product Audit Evidence Matrix

| Dimension | Evidence to inspect | Release consequence when missing |
|---|---|---|
| Purpose/value | Problem, users, alternatives, outcome hypothesis | Do not call the product validated |
| Requirements | Requirement, owner, source, acceptance oracle, change status | Block untraceable requirements |
| Architecture | Context, decision, data/state ownership, uncertainty, failure/recovery | Block unresolved critical design risk |
| AI control | Model/system/input/output, human review, correction, consent, drift | Keep safest path; do not certify readiness |
| Game/player | Narrative state, player verbs, AI fairness, playtest and accessibility | Block greenlight for untested critical experience |
| Test | Normal, edge, adversarial, failed-path, regression and evidence identity | Mark unassessed; no implicit pass |
| Release/ops | Exact artefact, checksum, rollout, monitoring, owner, rollback rehearsal | Hold promotion |
| Handoff/learning | Support, training, incident, retrospective, standardisation and next cycle | Do not close the improvement |

Report `min(raw_score, 65)`. The plan must target 95/100 and name the gap,
root cause, experiment, owner, measure, risk, rollback and acceptance evidence.
