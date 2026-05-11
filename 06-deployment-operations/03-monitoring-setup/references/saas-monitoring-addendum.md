# SaaS Monitoring Setup Addendum

Supplements the generic `03-monitoring-setup` skill when the project is a SaaS.

## A. Mandatory dashboards

1. **Per-tenant operational dashboard** — for each tenant: error rate, P95 latency, request volume, recent incidents, support tickets, health score. Accessible to CSMs and SRE.
2. **Control-plane vs application-plane separation** — distinct dashboards. Control-plane outage has higher blast radius — page differently.
3. **KPI-catalogue dashboard** — ARR, MRR, churn, expansion, activation rate, retention curves, CAC payback per cohort. Refreshed daily.
4. **Per-tier SLO dashboard** — error-budget burn per tier per SLO; visible cross-team.
5. **Per-tenant cost dashboard** — gross margin per tenant, top 10 cost-attribution tenants, anomaly alerts.
6. **Billing & metering dashboard** — meter ingestion lag, reconciliation deviation, dunning queue depth, payment-failure rate.
7. **Trust & security dashboard** — pen-test status, vuln scan findings, cert expiry, key rotation, sub-processor status.

## B. Mandatory log tagging

Every log line for tenant-scoped operations MUST carry `tenant_id`. Lint at log-emit boundary.

## C. Mandatory alerts

- Burn-rate alerts per SLO (see SLO doc).
- Per-tenant anomaly (5× normal error rate).
- Metering pipeline lag > N minutes.
- Reconciliation deviation > 0.1%.
- Cross-tenant access attempt detected (security alert SEV1).
- Dunning queue overflow.

## D. Retention

- Metrics: 13 months at minute resolution + 7 years aggregate.
- Traces: 14 days hot + 90 days cold.
- Logs: 13 months minimum; PII logs scrubbed at 30 days.

## E. Cross-links

- `SLO_And_Error_Budget_Doc.md`
- `IR_and_Postmortem.md`
- `Billing_And_Metering_Spec.md`
- `Multi_Tenancy_Architecture_Spec.md`
- SaaS Metric & KPI Catalogue (Phase 01 ref)
