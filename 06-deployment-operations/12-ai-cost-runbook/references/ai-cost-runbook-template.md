# AI Cost Runbook Template

## 1. Cost-Generating Components per Feature

| Feature | Component | Unit | Provider rate (illustrative) |
|---------|-----------|------|--------------------------------|
| AI Summary | LLM call | $/M tokens | $3 in, $15 out |
| AI Composer | LLM call | $/M tokens | $3 in, $15 out |
| AI Composer | reranker | $/M tokens | $1 |
| AI Analyst | LLM call + warehouse query | $/M tokens + $/scanned-byte | model + warehouse |
| AI Analyst | embedding | $/M tokens | $0.10 |
| AI Agent | LLM planner + tool calls | $/M tokens + tool API | varies |
| All | judge-LLM (nightly) | $/M tokens | $3 in, $15 out |
| All | content filter | $/call | $0.0005 |

## 2. Ceilings

| Feature | Tier | Per-call ceiling | Per-tenant / day | Per-tenant / month | Admin request? |
|---------|------|--------------------|---------------------|-----------------------|------------------|
| AI Summary | Starter+ | $0.01 | $5 | $100 | yes |
| AI Composer | Pro | $0.03 | $20 | $400 | yes |
| AI Composer | Business+ | $0.04 | $50 | $1000 | yes |
| AI Analyst | Business | $0.20 | $50 | $1000 | yes |
| AI Analyst | Enterprise | $0.25 | $200 | $4000 | yes |
| AI Agent | Enterprise | $1.00 | $200 | $4000 | yes |

## 3. Spend Anomaly Detection

- Baseline: rolling 14-d median per (tenant, feature, day).
- Alert thresholds:
  - 2x baseline within 1 h -> SEV3 to FinOps.
  - 3x baseline within 5 min (Enterprise tier) -> SEV2 to FinOps + CSM.
  - 5x baseline -> SEV1; investigate abuse / misconfig.

## 4. Throttle / Pause / Fallback Rules

| Spend vs ceiling | Action | User-visible |
|---------------------|---------|----------------|
| 80% | soft warn admin via email | admin email |
| 100% | route to cheaper-comparable model | "slower response" hint |
| 130% | enforce smaller-context summaries | "concise mode" hint |
| 150% | hard throttle: queue requests | "high demand" message |
| 200% | pause feature for tenant; CSM contact 15 min | feature paused message |
| 5x baseline anomaly | SEV1 pause | feature paused message |

## 5. Model-Fallback Policy

| Feature | Primary | Cheaper-comparable | Last resort |
|---------|---------|----------------------|--------------|
| AI Summary | Claude 3.7 Sonnet | Claude 3.5 Haiku | abstain |
| AI Composer | Claude 3.7 Sonnet | Claude 3.5 Haiku | abstain |
| AI Analyst | Claude 3.7 Sonnet | GPT-4o-mini | abstain |
| AI Agent | Claude 3.7 Sonnet | -- (no fallback for agent) | pause |

## 6. FinOps Cadence

| Cadence | Output | Owner |
|---------|--------|-------|
| Daily | per-tenant top spend dashboard | FinOps |
| Weekly | per-feature cost-per-call trend | FinOps + AI Lead |
| Monthly | per-tenant outliers; renewal-risk flags | FinOps + CSM |
| Quarterly | cost-vs-pricing-tier reconciliation; tier-margin report | CFO + CPO |

## 7. Billing-Event Reconciliation

- Every cost-bearing call emits `ai.usage.<feature>` event (see Billing & Metering Spec AI usage events).
- Nightly job: join gateway logs vs billing-event store. Diff > 0.1% triggers SEV3 to platform on-call.
- Monthly: end-of-month close requires zero unreconciled gateway logs older than 7 d.

## 8. On-Call Procedure

When SEV3+ cost anomaly fires:

1. Confirm signal in the FinOps dashboard.
2. Identify tenant + feature.
3. Apply throttle / pause per rules above.
4. Notify CSM within 15 min (Enterprise) / 1 h (others).
5. Investigate: legitimate spike, configuration error, abuse, model regression.
6. If abuse: invoke security IR (cross-link `09-saas-incident-response-and-postmortem`).
7. If misconfig: support customer to correct.
8. Postmortem if SEV2+.
