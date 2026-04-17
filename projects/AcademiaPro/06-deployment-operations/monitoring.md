# Monitoring and SLOs — Academia Pro

## Service Level Objectives

| Service / Surface | Metric | SLO (target) | Error Budget (monthly) |
|---|---|---|---|
| Web app login | P95 login response time | <= 1.5 s | 1% (21.9 min/month) |
| Enrolment API | P95 response time | <= 500 ms | 1% |
| Fee payment API | P95 response time | <= 800 ms | 0.5% |
| UNEB export | batch completion < 30 min | 99% success | 1% |
| EMIS export | annual return produced on schedule | 100% (hard) | 0% |
| Multi-tenant isolation | cross-tenant leakage events | 0 per quarter | 0% (hard) |
| Overall availability | 5xx rate over 28-day rolling window | <= 0.5% | 0.5% |

## Telemetry Stack

- Metrics — Prometheus to Grafana. Dashboards in `grafana.internal/d/academiapro-overview`.
- Logs — Loki. Correlation ID propagated from API gateway through all services.
- Traces — OpenTelemetry to Tempo. 10% sampling in prod, 100% in staging.
- Alerts — Alertmanager to PagerDuty. Alert definitions in `infra/alerts/*.yml`.

## Key Alerts

| Alert | Trigger | Severity |
|---|---|---|
| `AcademiaProHighErrorRate` | 5xx rate > 1% over 5 min | Sev-2 |
| `AcademiaProDatabaseReplicationLag` | MySQL replica lag > 30 s for 5 min | Sev-2 |
| `AcademiaProTenantLeak` | cross-tenant query log entry >= 1 | Sev-1 |
| `AcademiaProPIIScrubberBypass` | `ai_audit_log.pii_scrubbed=0` count >= 1 | Sev-1 |
| `AcademiaProDeploymentRollback` | CodeDeploy rollback triggered | Sev-2 |

## Traces

- NFR-AVAIL-001, NFR-PERF-001, NFR-OBS-001.
- CTRL-ISO-A12.
