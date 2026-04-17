# Change Window Policy — Academia Pro

## Standard Change Windows

- Routine (Sev-3/Sev-4 fix) — any weekday 07:00–19:00 EAT. No PagerDuty page.
- Minor release — Thursday 19:00–22:00 EAT. PagerDuty warn.
- Major release — Friday 22:00 EAT through Saturday 02:00 EAT. PagerDuty pages primary and secondary.
- Freeze period — the last week of every UNEB exam cycle (PLE, UCE, UACE, Thematic). Deployments frozen except Sev-1 hotfixes.

## Emergency Changes

Sev-1 incident response trumps the change-window policy. The incident commander may authorise immediate deployment. A retrospective change ticket is filed within 24 hours.

## Approval Matrix

| Change class | Approver |
|---|---|
| Routine | Any engineer; PR with one review |
| Minor release | Tech lead |
| Major release | Tech lead + Product Owner |
| Emergency | Incident commander |
| Database schema change | Tech lead + DBA-of-the-day |
| Tenant-isolation change (ADR-0003) | Tech lead + Security lead (mandatory second reviewer) |
| Feature flag flip in prod | PM + Tech lead |

## Communication

- 48 hours before — announce in `#engineering`, `#support`, and via tenant email blast for major releases.
- At start — post in `#deploy` with commit SHA and release notes link.
- At end — post completion in `#deploy` with health summary.
- Post-incident — 5-why within 72 hours, filed under `09-governance-compliance/`.
