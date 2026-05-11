# SaaS SLO & Error-Budget Template

## 1. SLI inventory

| Service | SLI | Definition | Source | Sampling window | Exclusions |
|---------|-----|------------|--------|-----------------|------------|
| | Availability | successful_requests / valid_requests | Prometheus `http_requests_total` | 1 min | planned maintenance with > 14 d notice |
| | Latency P95 | 95th percentile end-to-end | distributed-tracing | 1 min | health checks |
| | Latency P99 | 99th percentile | distributed-tracing | 1 min | |
| | Correctness | `billing_events_emitted / metering_events_processed` | metering pipeline | 5 min | |
| | Freshness | replication lag P95 | DB metric | 30 s | |

## 2. Per-tier SLO targets

| Tier | Availability | P95 | P99 | Support response | Notes |
|------|--------------|-----|-----|------------------|-------|
| Bronze | 99.5% | 800 ms | 2000 ms | NBD | shared pool |
| Silver | 99.9% | 400 ms | 1000 ms | 4 h | shared pool w/ reserved capacity |
| Gold | 99.95% | 200 ms | 500 ms | 1 h | pod-isolated |
| Enterprise | 99.99% | 150 ms | 300 ms | 15 min, CSM | silo |

## 3. Error-budget math

`error_budget_minutes = (1 - SLO) × period_minutes`

| Tier | 30-day budget | 90-day budget |
|------|---------------|---------------|
| Bronze | 216 min | 648 min |
| Silver | 43.2 min | 130 min |
| Gold | 21.6 min | 65 min |
| Enterprise | 4.32 min | 13 min |

## 4. Burn-rate alerts

| Alert | Severity | Burn rate | Window | Threshold | Owner | Runbook |
|-------|----------|-----------|--------|-----------|-------|---------|
| Fast burn | SEV2 | 14.4× | 1 h | 2% monthly | on-call SRE | runbook/alert-fast-burn.md |
| Medium burn | SEV3 | 6× | 6 h | 5% monthly | on-call SRE | runbook/alert-medium-burn.md |
| Slow burn | SEV4 | 1× | 3 d | 10% monthly | service owner | runbook/alert-slow-burn.md |

## 5. Freeze rules

- Error budget remaining < 25% → only low-risk deploys allowed.
- Error budget remaining ≤ 0% → deploy freeze on the affected service except rollbacks and security fixes.
- Two consecutive 30-day breaches → executive postmortem mandatory.

## 6. Customer-SLA mapping & service credits

| Tier | Customer SLA (contracted) | Internal SLO (target) | Headroom |
|------|---------------------------|-----------------------|----------|
| Bronze | 99.0% | 99.5% | 0.5% |
| Silver | 99.5% | 99.9% | 0.4% |
| Gold | 99.9% | 99.95% | 0.05% |
| Enterprise | 99.95% | 99.99% | 0.04% |

Service-credit schedule (example, override per contract):

| Monthly availability | Credit |
|----------------------|--------|
| ≥ SLA | 0% |
| SLA - 0.5% | 10% |
| SLA - 1% | 25% |
| < SLA - 2% | 50% |

Exclusions: planned maintenance with ≥ 14 d notice; force majeure; customer-induced (admin error, custom-script failure); third-party dependencies declared upstream.

Measurement: 5-minute success-ratio rollup, monthly aggregate. Credit request: customer submits via support portal within 30 days of incident.

## 7. Review cadence

- Monthly: SLO compliance review, error-budget snapshot per service, action items for breaches.
- Quarterly: SLO target review, possible tightening or relaxation, customer-SLA negotiation review.
- Annually: SLI catalogue refresh, retire stale SLIs.
