# Agent Cost Dimensions Cross-Link

The AI Cost Runbook covers per-call token cost, per-feature cost ceiling, and per-tenant cost runaway. For agent features, the cost surface decomposes into **four dimensions** rather than one.

## Agent cost decomposition

Per agent run:

| Dimension | Source | Typical share |
|------------|--------|----------------|
| Steps | orchestrator emits cost-per-step | varies |
| Tools | dispatcher cost meter; per-tool USD (LLM judge + tool cost) | typically dominant for retrieval-heavy agents |
| LLM | model gateway cost meter; tokens-in + tokens-out × model price | typically dominant for plan-heavy agents |
| External | per-tool external-API cost (search, vendor APIs) | varies; can spike per task |

Per run: `cost = LLM_planner + sum(LLM_tool + external_tool_cost for tool in run)`.

## Per-tenant envelope

The cost runbook's per-tenant envelope is extended for agent features by the agent-cost envelope per feature (max-cost per run, per-tenant per-day cap). On overshoot:

1. Throttle the dispatcher for the tenant.
2. If persists 1 h: per-tenant pause; SEV2.
3. Notify tenant admin.

## Reporting

Per-tenant agent cost report (monthly): cost by feature × dimension; flag tenants approaching envelope; flag runs at P95+ of cost distribution for review.

## Cross-link

- `13-ai-agent-slo-doc` — cost-per-run SLO.
- `19-ai-agent-adr-catalogue` — ADR-AGT-012 cost envelope per feature.
- `02-requirements-engineering/16-ai-agent-feature-prd-spec` — budget caps per FR.
