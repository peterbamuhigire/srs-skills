# CIA-002 — Assign runbook on-call and team-lead contacts at Sprint 1 kick-off

- Status: open
- Opened: 2026-04-17
- Owner: Peter Bamuhigire

## Impact

- `06-deployment-operations/runbook.md` escalation tree currently names "Assigned at Sprint 1 kick-off" as primary and team-lead contacts.
- Without on-call assignments the Sev-1 response reduces to CTO-only and does not meet the 5-minute ACK SLA.

## Plan

1. Sprint 1 kick-off (target 2026-05-05): assign primary + secondary + team-lead.
2. Populate `_context/private/contacts.md` (gitignored).
3. Update `runbook.md §On-Call Rotation`.
4. Close CIA-002.

## Rollback

N/A — administrative change only.
