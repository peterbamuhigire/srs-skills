# AI Monitoring Addendum

When the system under operation includes AI features, the monitoring setup MUST capture the AI-specific signals below. They sit alongside the generic application metrics, not in place of them.

## Required AI signals

| Metric | Source | Cardinality | Sample | Retention | Alert |
|--------|--------|-------------|--------|-----------|-------|
| tokens_in / tokens_out | Model Gateway | per (tenant, feature, model) | every request | 13 mo | none (cost) |
| model_latency_ms | gateway | per (provider, model) | every request | 13 mo | P95 > 200% target |
| fallback_rate | gateway | per feature | 1 min | 13 mo | > 5% sustained 1 h |
| abstention_rate | service | per feature | 1 min | 13 mo | change > 5 pp in 24 h |
| citation_rate | service | per feature | 1 min | 13 mo | drop > 5 pp in 24 h |
| judge_llm_score | eval runner | per feature | per run | 13 mo | drop > 3 pp |
| factuality_score | nightly judge | per feature | nightly | 24 mo | drop > 3 pp |
| cost_usd | gateway | per (tenant, feature) | every request | 24 mo | per cost runbook |
| content_filter_trips | gateway | per filter | every trip | 13 mo | any spike > 3 sigma |
| red_team_smoke_pass | CI | per PR | per PR | 24 mo | any CRITICAL/HIGH |
| unauthorised_action_attempts | agent service | per tenant | every event | 24 mo | any non-zero |
| cross_tenant_retrieval_403 | gateway | per tenant | every event | 24 mo | any non-zero |

## Dashboards

1. **AI Quality dashboard** — factuality, citation, abstention, judge score per feature, by tier.
2. **AI Reliability dashboard** — fallback rate, model latency, content-filter trips, eval CI status.
3. **AI Cost dashboard** — cost per tenant per feature, top spenders, per-call cost trend.
4. **AI Security dashboard** — red-team status, unauthorised action attempts, cross-tenant retrieval blocks, prompt-injection probe rates.

## Alerting baseline

- Safety violations: zero-tolerance; SEV1 on any event.
- Hallucination SLO burn: per the hallucination SLO doc.
- Cost anomaly: per the cost runbook.
- Auto-rollback: citation drop > 5 pp 24 h triggers prompt-tag rollback automatically.

## Sampling and replay

- 1% of production requests are sampled for nightly judge replay; sample is tenant-stratified.
- All abstain payloads are captured (no sampling).
- All content-filter trips captured.
- All unauthorised-action attempts captured (zero retention loss).

## PII at the metric layer

- Token counts and metric labels do not contain PII.
- The conversation log (separate store, tenant-partitioned) holds bodies; metrics never join with the log on a PII key.
