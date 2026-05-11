---
name: "ai-agent-slo-doc"
description: "Generate the AI Agent SLO Doc: SLIs for task success, step efficiency, intervention rate, irreversible-action-incident rate, agent-task availability, and agent-cost-per-run; per-feature SLO targets by tier; error budgets; multi-burn-rate alerts; freeze and pause rules; mapping to customer-facing agent commitments."
metadata:
  use_when: "Use whenever a SaaS ships one or more agent features at L1+ and commits to agent-task quality in customer contracts or trust statements."
  do_not_use_when: "Do not use for L0 (suggest-only) agents with no committed customer SLA. Cover those under the AI Hallucination SLO Doc."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, AI_Agent_Eval_Spec.md, AI_Hallucination_SLO_Doc.md, SLO_And_Error_Budget_Doc.md, Monitoring_Setup.md, pricing & packaging spec."
  workflow: "Inventory agent SLIs, set per-feature SLO targets by tier, compute error budgets, define multi-burn-rate alerts, define freeze and pause rules, map agent SLOs to customer commitments, write the doc."
  quality_standards: "Every agent feature shall have task success, intervention, irreversible-action-incident, agent-availability, and agent-cost-per-run SLIs with documented measurement sources. The irreversible-action-incident SLO shall be zero with zero error budget."
  anti_patterns: "Do not set the irreversible-action-incident budget above zero. Do not write a task-success SLO without a production sampling procedure beyond the eval rig. Do not omit the cost-per-run SLO; agents make cost runaway a safety incident."
  outputs: "AI_Agent_SLO_Doc.md."
  references: "Use references/ai-agent-slo-template.md."
---

# AI Agent SLO Doc Skill

## Overview

The agent-specific complement to `ai-hallucination-slo-doc` and the parent SaaS SLO doc. Treats agent task success, intervention rate, irreversible-action incidents, agent-task availability, and agent-cost-per-run as first-class SLIs.

## Core Instructions

### Step 1: Inventory SLIs per agent feature

Required SLIs:

- **Task success SLI** — % of agent runs marked successful by the production-sample replay through the judge-LLM (or by user-confirmed completion where available).
- **Step efficiency SLI** — mean step count of successful runs vs gold-trajectory step count.
- **Intervention SLI** — % of runs that required mid-run human intervention.
- **Irreversible-action-incident SLI** — count per million runs of irreversible actions later confirmed incorrect by the user.
- **Agent-task availability SLI** — % of starts that reach a terminal state within the run's max-wallclock budget (not aborted by infra failure).
- **Agent-cost-per-run SLI** — mean and P95 USD cost per run, against the per-tenant budget envelope.
- **Tool-error rate SLI** — % of tool calls that return non-retryable or safety errors.

### Step 2: Measurement procedure

For each SLI declare source + sampling:

- Task success: nightly production-sample replayed through the judge-LLM. Sample rate per feature.
- Intervention: emitted by the orchestrator on every run; aggregated per feature.
- Irreversible-action-incident: counted at user-flag time (user marks "this was wrong"); also at admin-review time.
- Availability: emitted by the orchestrator.
- Cost: emitted by the dispatcher (LLM + external API cost rolled up).

### Step 3: Per-feature SLO targets by tier

| Tier | Task success | Intervention | Irreversible incidents | Availability | Cost-per-run |
|------|---------------|---------------|--------------------------|---------------|----------------|
| Pro | >= 0.90 | <= 20% | 0 (zero budget) | >= 0.99 | within feature cap |
| Enterprise | >= 0.95 | <= 10% | 0 (zero budget) | >= 0.995 | within feature cap |

### Step 4: Error budgets

Standard formula: `error_budget = (1 - SLO) × runs_in_window`. Irreversible-action incidents: zero budget; any breach is SEV1 plus per-tenant kill-switch for the feature.

### Step 5: Multi-burn-rate alerts

| Alert | Burn rate | Window | Threshold |
|-------|-----------|--------|-----------|
| Fast burn (task success) | 14x | 1 h | 2% of monthly budget |
| Medium burn | 6x | 6 h | 5% |
| Slow burn | 1x | 3 d | 10% |
| Intervention surge | 3x baseline | 1 h | any feature |
| Irreversible incident | n/a | 0 | any |
| Cost overshoot | per-tenant 200% of envelope | 1 h | throttle then pause |

### Step 6: Freeze and pause rules

- Task-success error budget exhausted: freeze planner / catalogue changes; require executive approval for further model bumps.
- Intervention rate up > 50% in 7 d: roll back the last planner/prompt change; SEV2.
- Irreversible-action incident: per-tenant feature kill-switch; SEV1; postmortem; admin notification.
- Cost overshoot: per-tenant throttle then per-tenant pause; SEV2.

### Step 7: Customer-facing commitments

Per tier define what is contractually committed. Likely:

- Agent-task availability (numeric).
- Notification of any irreversible-action incident within 24 h.
- A user-facing "this action was performed by an agent" notification standard.
- The user's right to request human handling for any task class.

### Step 8: Write the doc

`AI_Agent_SLO_Doc.md` sections: 1) Agent SLI Inventory, 2) Measurement Procedure, 3) Per-feature SLO Targets, 4) Error Budgets, 5) Burn-Rate Alerts, 6) Freeze & Pause Rules, 7) Customer-Facing Commitments, 8) Review Cadence.

## Standards

- Google SRE applied to agents
- ISO/IEC 25010 (functional correctness)
- ISO/IEC 42001 Clause 9
- NIST AI RMF MEASURE

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-slo-template.md`.
