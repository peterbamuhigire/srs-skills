# Runbook — Academia Pro

> Top-of-phase operations runbook. Detailed per-service runbooks live in `02-runbook/`. This file is the escalation reference required by `phase06.runbook_has_escalation`.

## On-Call Rotation

- Primary: weekly rotation; see PagerDuty schedule `academiapro-oncall`.
- Secondary: same rotation, one slot behind.
- Manager-on-call: Peter Bamuhigire.

## Escalation Tree

```
       Incident detected (Sev-1 / Sev-2)
                    |
                    v
        Primary on-call (paged 0 min)
         |            |             |
  ACK in 5 min   ACK in 15 min  Not ACK in 15 min
        |                            |
        v                            v
  Primary works   ---------->   Secondary paged
        |                            |
  Sev-1 or scope > 30 min            v
        |                    Manager on-call paged (Peter)
        v                            |
  Manager on-call paged              v
        |                    CTO and Sponsor paged
        v
  Incident commander assigned
        |
        v
  War room in #incident-<date> channel
```

| Severity | First responder | Escalation trigger | Comms SLA |
|---|---|---|---|
| Sev-1 (outage) | Primary on-call | Not ACK in 5 min -> Secondary; not resolved in 30 min -> CTO | 15-minute updates in #incident |
| Sev-2 (degradation) | Primary on-call | Not ACK in 15 min -> Secondary; scope > 1 hour -> Manager | 30-minute updates |
| Sev-3 (minor) | Primary on-call | None within business day | Daily update |
| Sev-4 (cosmetic) | Queue for next sprint | — | Sprint review |

## Incident Response

See `incident-response/01-severity-matrix.md` for the severity taxonomy and `incident-response/02-escalation-tree.md` for the full org chart.

## Playbooks (per-service)

- Application OOM — `02-runbook/01-app-oom.md`
- MySQL replication lag — `02-runbook/01-mysql-replication.md`
- Redis unavailable — `02-runbook/01-redis-down.md`
- MoMo / Airtel / SchoolPay upstream outage — `02-runbook/01-payments-outage.md`
- UNEB export failure — `02-runbook/01-uneb-export.md`
