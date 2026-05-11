# AI Usage Metering Events (addendum to billing & metering spec)

When the SaaS exposes AI features that are priced by usage (calls, tokens, agent runs), the metering event catalogue MUST include the AI events below.

## Event family: `ai.usage.*`

| Event | Trigger | Fields |
|-------|---------|--------|
| `ai.usage.call` | every gateway call | id, ts, tenant_id, workspace_id, user_id (hashed), feature_id, model, prompt_tag, tokens_in, tokens_out, latency_ms, cost_usd, status, abstain_flag, citation_count, idempotency_key |
| `ai.usage.embedding` | every embedding call | id, ts, tenant_id, feature_id, model, dim, tokens, cost_usd |
| `ai.usage.retrieval` | every retrieval | id, ts, tenant_id, feature_id, index, top_k, latency_ms, hit_count |
| `ai.usage.agent_step` | every agent step | id, ts, tenant_id, feature_id, run_id, step_no, tool, side_effect_class, latency_ms, cost_usd, approval_required, approval_status |
| `ai.usage.agent_run` | every agent run end | id, ts, tenant_id, feature_id, run_id, step_count, total_cost_usd, outcome, abstain_flag |
| `ai.usage.filter_trip` | content-filter trip | id, ts, tenant_id, feature_id, filter, severity |
| `ai.usage.fallback` | fallback route taken | id, ts, tenant_id, feature_id, reason, primary_model, fallback_model |

## Idempotency and de-duplication

- Each event carries `idempotency_key` and an `event_id` (UUIDv7).
- Replay-safe consumers de-duplicate by `event_id`.

## Per-tenant aggregation

Aggregator emits hourly and daily rollups per tenant per feature for the cost runbook dashboards and the billing engine.

## Privacy

- `user_id` is hashed at the gateway.
- No prompt or response body is included in metering events; bodies live in the conversation-log store with tenant-partition.

## Reconciliation

- Nightly job joins gateway request log against the metering store. Diff > 0.1% triggers SEV3.
- Monthly close requires zero unreconciled events older than 7 days.

## Billing connector

Per the billing engine's contract, the AI usage events feed:

- Included-quota counters per tier.
- Overage line items per period.
- Cost-of-revenue reporting per feature.

## Cross-links

- Cost Runbook: `06-deployment-operations/12-ai-cost-runbook/`
- Pricing & Packaging AI Tier Guidance: `01-strategic-vision/12-saas-pricing-and-packaging-spec/references/ai-tier-guidance.md`
