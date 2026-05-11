---
name: "ai-cost-runbook"
description: "Generate the AI Cost Runbook: per-tenant cost monitoring, per-feature ceilings, spend anomaly response, throttle and pause rules, model-fallback policy on cost overrun, FinOps cadence, and the per-tenant billing event reconciliation for AI usage."
metadata:
  use_when: "Use for any AI feature that incurs per-call cost (token-priced model, vector ops, agent steps). Mandatory before GA."
  do_not_use_when: "Do not use for AI features running on amortised owned compute with no per-call billing exposure."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Architecture_Spec.md, Billing_And_Metering_Spec.md, pricing & packaging spec, Monitoring_Setup.md."
  workflow: "Inventory cost-generating components, set per-tenant and per-feature ceilings, define spend-anomaly detection, define throttle / pause / model-fallback rules, define FinOps cadence, define billing-event reconciliation, write the runbook."
  quality_standards: "Every AI feature shall have a per-call ceiling and a per-tenant daily ceiling. Spend anomalies shall be detected at 2x baseline within 1 h. Every cost-generating event shall emit a billing event for metering."
  anti_patterns: "Do not assume the model provider's spend cap is sufficient. Do not let cost overrun be discovered at end-of-month invoice. Do not throttle without notifying the tenant admin."
  outputs: "AI_Cost_Runbook.md."
  references: "Use references/ai-cost-runbook-template.md."
---

# AI Cost Runbook Skill

## Core Instructions

### Step 1: Cost-generating component inventory

For each AI feature list every cost-bearing component: model calls (provider $/M tokens), embedding calls, vector ops (per-query, per-storage), reranker, judge-LLM, content-filter, agent tool invocations (third-party APIs), egress.

### Step 2: Per-call and per-tenant ceilings

Set per-(feature, tenant, day) and per-(feature, tenant, month) ceilings. Ceilings are tier-defaulted; admins can request higher.

### Step 3: Spend anomaly detection

Per-tenant baseline computed over the last 14 d. Alert at 2x baseline within 1 h; 3x within 5 min for Enterprise tier.

### Step 4: Throttle / pause / fallback rules

- 100% of ceiling: throttle (slow path, larger batch sizes, smaller model).
- 150% of ceiling: hard throttle (queue, with user-visible message).
- 200% of ceiling: pause feature for the tenant; CSM contact within 15 min.
- Cost > 130% of per-call ceiling: route to cheaper model (state which model).
- Anomaly above 5x baseline: pause and SEV1; possible abuse / misconfig.

### Step 5: Model-fallback policy

Define the fallback ladder per feature: primary -> cheaper-but-comparable -> abstain.

### Step 6: FinOps cadence

- Daily: cost dashboards reviewed by FinOps + AI lead.
- Weekly: per-feature, per-tier cost-per-call trend.
- Monthly: per-tenant top spenders + outliers; renewal-risk flags to CSM.
- Quarterly: cost-vs-pricing-tier reconciliation.

### Step 7: Billing-event reconciliation

Every cost-bearing AI call emits a billing event (cross-link `02-requirements-engineering/13-saas-billing-and-metering-spec` AI usage-metering events). The reconciliation job matches gateway logs against billing-event store nightly; missing events trigger a SEV3.

### Step 8: Write the runbook

`AI_Cost_Runbook.md` sections: 1) Cost-Generating Components, 2) Per-Tenant & Per-Feature Ceilings, 3) Spend Anomaly Detection, 4) Throttle / Pause / Fallback Rules, 5) Model-Fallback Policy, 6) FinOps Cadence, 7) Billing-Event Reconciliation, 8) On-Call Procedure.

## Standards

- FinOps Foundation framework
- Provider FinOps playbooks (OpenAI, Anthropic enterprise)
- ISO/IEC 42001 Clause 8 (operation)
