# Approval enforcement adapter

The SRS engine declares its lifecycle controls in
[`approval-adapter.json`](approval-adapter.json) and uses the shared contract
from `skills-web-dev/docs/approval-contract.md`.

## Lifecycle gate

The permitted lifecycle is `draft -> review -> resolve -> approve -> baseline`.
Any change to an approved requirement, architecture decision, test waiver,
release decision, or AI policy returns to review and requires a new immutable
preview. The drafting agent cannot approve its own output.

## Required preview

Show the proposed delta, affected requirements, acceptance oracles, standards
evidence, security/privacy impact, open findings, named reviewer, expiry,
rollback/reversion path, and exact baseline hash. Missing evidence, an
unassessed evaluation, or unresolved critical/high red-team result blocks the
gate.

## Stop conditions

Do not baseline, waive, release, change policy, or close an incident when the
reviewer identity, evidence bundle, traceability, approval scope, or rollback
path is missing. A document or agent statement saying “approved” is not an
approval event. The host must route the lifecycle mutation through the shared
dispatcher and record the approval before writing the new baseline.

## Acceptance boundary

The engine may draft specifications and test plans. It may not commit a
baseline, waive a critical control, approve a release, or close a material
incident without a fresh authorised approval after the final preview.
