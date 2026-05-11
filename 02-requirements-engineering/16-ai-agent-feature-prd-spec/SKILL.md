---
name: "ai-agent-feature-prd-spec"
description: "Generate the AI Agent Feature PRD Spec: IEEE 830-form requirements for every agentic feature, with task scope, autonomy level, action-catalogue summary, intervention triggers, success metrics, max-step / max-cost / wallclock budgets, abstain criteria, and irreversible-action gates anchored to the agent eval and red-team registries."
metadata:
  use_when: "Use for every feature classified as an agent by the AI Agent Strategy Doc (L0..L4). Addendum to the AI Feature PRD Spec."
  do_not_use_when: "Do not use for direct-LLM or RAG features that do not call write or external tools; cover those with `ai-feature-prd-spec` alone."
  required_inputs: "AI_Agent_Strategy_Doc.md, AI_Feature_PRD_Spec.md, AI_Feature_Strategy_Doc.md, Multi_Tenancy_Architecture_Spec.md, pricing & packaging spec."
  workflow: "Inventory agent-powered FRs, attach the agent clauses to each, define intervention triggers, define budget caps, define irreversible-action gates, define acceptance gates against the agent eval rig, write the AI_Agent_Feature_PRD_Spec.md."
  quality_standards: "Every agent FR shall declare: task scope boundary, autonomy level, action-catalogue reference, intervention triggers, max-step / max-cost / max-wallclock budgets, abstain criteria, and the irreversible-action gating rule. Every acceptance gate shall be a numeric threshold backed by the agent eval rig."
  anti_patterns: "Do not approve an agent FR without budget caps. Do not allow an agent FR to call any tool not enumerated in the action catalogue. Do not mark an L2+ FR as requirements-complete without a named human approver role and a kill-switch reference."
  outputs: "AI_Agent_Feature_PRD_Spec.md."
  references: "Use references/ai-agent-feature-prd-spec-template.md."
---

# AI Agent Feature PRD Spec Skill

## Overview

Produces the agent-feature complement to `ai-feature-prd-spec`. Every agent FR carries seven mandatory agent clauses that the AI feature PRD does not collect. The acceptance gates point at the agent eval rig and the agent red-team plan.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `AI_Agent_Strategy_Doc.md`, `AI_Feature_PRD_Spec.md`, `AI_Feature_Strategy_Doc.md`, `Multi_Tenancy_Architecture_Spec.md`, pricing & packaging spec |
| **Output** | `AI_Agent_Feature_PRD_Spec.md` |
| **Standard** | IEEE 830-1998, NIST AI RMF MAP/MEASURE, EU AI Act Art. 13 + Art. 14 |

## Core Instructions

### Step 1: Inventory agent-powered functional requirements

List every FR whose execution involves a plan, a tool call beyond retrieval, or an action with a write side-effect.

### Step 2: Attach the seven agent clauses to each FR

For each agent FR the spec MUST capture:

| Clause | Form | Example |
|--------|------|---------|
| Task scope boundary | inputs in / outputs out / explicit non-goals | "scope: customer inbox triage; non-goal: composing customer-bound outbound emails" |
| Autonomy level | L0..L4 with human role | "L2 — approve plan; admin approves once per inbox-batch" |
| Action-catalogue reference | named subset of the action catalogue | "catalogue rows: `email.label`, `email.archive`, `email.draft.create`" |
| Intervention triggers | rule that forces human-in-the-loop mid-run | "intervention required when proposed action class = irreversible OR estimated cost > $0.50" |
| Budget caps | max-step / max-cost / max-wallclock | "max-step 25; max-cost $0.25/run; max-wallclock 120 s; on overrun: abort + alert" |
| Abstain criteria | rule that ends the run cleanly | "abstain when planner returns no plan that satisfies the policy envelope; produce explanation payload" |
| Irreversible-action gate | the explicit gating rule for the irreversible class | "any tool with reversibility=irreversible requires admin confirmation per call; no batch approval" |

### Step 3: Define success metrics per agent FR

Choose metrics from:

- Task success rate on the agent golden-task set.
- Step efficiency (mean steps per successful run vs the gold trajectory).
- Tool-choice quality (% of tool calls that match the gold tool at the gold step).
- Hallucinated-argument rate (tool calls with at least one fabricated argument).
- Intervention rate (% of runs that required mid-run human intervention).
- Irreversible-action-incident rate (irreversible actions later flagged as incorrect by the user).

Each metric has a numeric threshold backed by the agent eval rig.

### Step 4: Define human-in-the-loop placement explicitly

For each agent FR state:

- Who approves (role).
- What is shown at the approval moment (the plan, the diff, the action arguments).
- What undo / revert is available after the fact.
- How a user contests an action that already executed.

Reference EU AI Act Art. 14 (human oversight) where the feature is high-risk.

### Step 5: Define rollout posture per agent FR

Initial rollout for every agent FR begins in shadow mode (agent proposes; human acts). Promotion stages: shadow → canary at L1 → L2 → L3 if applicable. Reference the agent rollout runbook for stage gates.

### Step 6: Define acceptance tests against the agent eval rig

Every agent FR has a row in the agent eval rig with:

- Golden-task set ID.
- Replay-set ID.
- Adversarial-set ID (links to the agent red-team plan).
- Pass thresholds per metric.
- CI gate definition.

### Step 7: Write the spec

`AI_Agent_Feature_PRD_Spec.md` sections: 1) Agent FR Inventory, 2) Per-FR Agent Clauses, 3) Success Metrics, 4) Human-in-the-Loop Placement, 5) Rollout Posture, 6) Eval & Red-Team Acceptance Gates, 7) Traceability to PRD, AI Feature PRD, and to agent eval / red-team IDs.

## Standards

- IEEE 830-1998
- NIST AI RMF MAP / MEASURE
- EU AI Act Art. 13 (transparency), Art. 14 (human oversight)
- OWASP LLM Top 10 (agentic addendum)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-feature-prd-spec-template.md`.
