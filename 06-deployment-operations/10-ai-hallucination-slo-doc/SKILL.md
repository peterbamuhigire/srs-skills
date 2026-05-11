---
name: "ai-hallucination-slo-doc"
description: "Generate the AI Hallucination SLO Doc: SLIs for factuality, citation accuracy, and abstention; per-feature SLO targets; error budgets; multi-burn-rate alerts; freeze rules; and the mapping from internal AI SLOs to customer-facing AI-quality commitments."
metadata:
  use_when: "Use whenever a SaaS commits to AI-feature quality in a customer contract or trust statement and operates AI features in production."
  do_not_use_when: "Do not use for internal-only AI experiments without customer-facing commitments."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Eval_Harness_Spec.md, Monitoring_Setup.md, SLO_And_Error_Budget_Doc.md (parent SaaS SLO doc), pricing & packaging spec."
  workflow: "Inventory AI SLIs, set per-feature SLO targets, compute error budgets, define multi-burn-rate alerts, define freeze and rollback rules, map AI SLOs to customer-facing commitments, write the AI_Hallucination_SLO_Doc.md."
  quality_standards: "Every AI feature shall have factuality, citation accuracy, abstention precision, and safety-violation SLIs with measurement sources. Every SLI shall be sampled in production, not only in the eval harness."
  anti_patterns: "Do not write a hallucination SLO without a measurement procedure that runs in production traffic. Do not set the safety violation budget above zero."
  outputs: "AI_Hallucination_SLO_Doc.md."
  references: "Use references/ai-hallucination-slo-template.md."
---

# AI Hallucination SLO Doc Skill

## Overview

The AI complement to the SaaS SLO doc. Treats hallucination, citation, abstention, and safety violations as first-class SLIs with their own error budgets and rollback rules.

## Core Instructions

### Step 1: SLI inventory per AI feature

Required SLIs:

- **Factuality SLI** — % of responses on a production-sample where judge-LLM marks all claims as supported.
- **Citation accuracy SLI** (RAG only) — % of citations matching source spans within tolerance.
- **Abstention precision SLI** — % of abstain responses that correctly should have abstained.
- **Abstention recall SLI** — % of should-abstain inputs that did abstain.
- **Safety violation SLI** — count of outputs hitting content-policy or PII filters per million calls.
- **Latency SLI** (already in parent SLO doc, restated for AI clarity).
- **Cost-per-call SLI** (cross-link to cost runbook).

### Step 2: Measurement procedure

For each SLI state the measurement source and sample method:

- Factuality and citation: production-sample replayed through the judge-LLM nightly. Sample rate per feature.
- Abstention: classify production responses by abstain-payload; spot-check by humans monthly to verify abstain correctness.
- Safety violation: counted at content-filter; alarmed on each event.

### Step 3: Set per-feature SLO targets

Per feature × tier:

| Tier | Factuality | Citation | Abstention precision | Safety violations |
|------|-----------|----------|-----------------------|--------------------|
| Free | >= 0.85 | n/a or >= 0.85 | >= 0.70 | 0 |
| Pro | >= 0.92 | >= 0.90 | >= 0.80 | 0 |
| Enterprise | >= 0.95 | >= 0.95 | >= 0.85 | 0 |

### Step 4: Error budgets

Standard formula: `error_budget = (1 - SLO) × calls_in_window`. Safety violations: zero-budget; any breach is SEV1.

### Step 5: Multi-burn-rate alerts

| Alert | Burn rate | Window | Threshold |
|-------|-----------|--------|-----------|
| Fast burn | 14× | 1 h | 2% of monthly budget |
| Medium burn | 6× | 6 h | 5% |
| Slow burn | 1× | 3 d | 10% |
| Safety | n/a | 0 | any |

### Step 6: Freeze and rollback rules

- Error budget exhausted: freeze prompt and model changes; eval bumps require executive approval.
- Citation accuracy drop > 5 pp in 24 h: auto-rollback to last green prompt tag.
- Safety violation: pause feature; SEV1; postmortem; provider escalation if upstream.

### Step 7: Customer-facing AI-quality commitments

Mirror the parent SLO doc pattern. Per tier, define what is contractually committed (likely abstention behaviour and uptime; not numerical factuality, since per-output verifiability remains imperfect). Define how customers report a perceived hallucination (flag button -> ticket -> review).

### Step 8: Write the doc

`AI_Hallucination_SLO_Doc.md` sections: 1) AI SLI Inventory, 2) Measurement Procedure, 3) Per-Feature SLO Targets, 4) Error Budgets, 5) Burn-Rate Alerts, 6) Freeze & Rollback Rules, 7) Customer-Facing AI Commitments, 8) Review Cadence.

## Standards

- Google SRE applied to AI features
- ISO/IEC 25010 (functional correctness)
- ISO/IEC 42001 Clause 9 (performance evaluation)
