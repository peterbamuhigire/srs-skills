# SaaS Incident Response & Postmortem Template

## 1. Severity matrix (severity × tenant scope)

| Severity | Single tenant | Tenant cohort | Platform-wide |
|----------|---------------|---------------|---------------|
| SEV1 | Enterprise customer down or data-impacting | Pod or region down | All-tenant outage / data corruption |
| SEV2 | Gold customer down | Multiple Gold tenants degraded | Major feature degraded for most |
| SEV3 | Silver/Bronze down | Cohort degraded | Minor feature degraded |
| SEV4 | Cosmetic | Cosmetic | Cosmetic |

## 2. IR phases & time targets

| Phase | SEV1 | SEV2 | SEV3 | SEV4 |
|-------|------|------|------|------|
| Triage | 5 min | 15 min | 1 h | NBD |
| Customer comms | 15 min | 30 min | 4 h | release-notes only |
| Mitigation target | 1 h | 4 h | 1 d | sprint |
| Postmortem published | 5 BD | 10 BD | optional | none |

## 3. Customer-comms templates

```
[SEV1 — Initial ack within 15 min]
Subject: [Status] Incident affecting {scope} — investigating
Body: We've detected an issue affecting {scope}. Our team is engaged.
Next update by {time + 30 min}. Status page: {url}.

[SEV1 — Status update every 30 min]
Subject: [Status] Update on incident affecting {scope}
Body: {what we know} | {what we're doing} | {next update}.

[SEV1 — Resolution]
Subject: [Status] Incident resolved
Body: Resolved at {time UTC}. Total duration {N min}. Detailed postmortem in 5 business days.

[SEV1 — Postmortem published]
Subject: Postmortem: {incident name}
Body: We've published a full postmortem with root cause and action items: {url}.
```

## 4. Status-page protocol

- Components: per region × per service (control plane, application plane, billing, identity).
- States: Operational / Degraded / Partial Outage / Major Outage / Maintenance.
- Post when: any SEV1; SEV2 lasting > 15 min; any scheduled maintenance.
- Authors: on-call SRE or comms-on-call.
- Subscriber notification: email + webhook + RSS.

## 5. Postmortem template

```
# Postmortem: <title>

- Incident ID:
- Date / time (UTC):
- Severity (final):
- Tenant scope:
- Duration:
- Author:
- Status: draft / under review / published / closed

## Summary
One paragraph.

## Impact
- Tenants affected: count + list (named for Enterprise).
- Duration: HH:MM
- Error-budget burn: minutes / % of monthly budget per affected SLO
- Financial impact (estimate): service credits + lost ARR risk
- Support load: ticket count, peak concurrent

## Timeline (UTC)
| Time | Event | Source |

## Root cause (5 whys)
1. Why? ...
2. Why? ...

## What went well

## What went poorly

## Contributing factors
- Process / Technical / Organisational

## Action items
| ID | Description | Owner | Severity | Due | Status |
```

## 6. Action-item tracking

- System: <ticketing tool>.
- Cadence: weekly burn-down.
- Closure: incident closes when mitigated; postmortem closes when all SEV-high action items are done.
