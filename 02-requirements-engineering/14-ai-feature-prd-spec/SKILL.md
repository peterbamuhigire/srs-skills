---
name: "ai-feature-prd-spec"
description: "Generate the AI-Feature PRD Spec: IEEE 830-form requirements for every AI-powered feature, with hallucination tolerance, latency budget, $/call ceiling, abstain criteria, citation policy, consent and training-data exclusion clauses, and acceptance tests anchored to the eval harness."
metadata:
  use_when: "Use for any feature whose behaviour is produced or modified by an LLM, vision model, embedding-based retrieval, agent, or fine-tune."
  do_not_use_when: "Do not use for deterministic features that merely call into AI infrastructure as a passive consumer (e.g. logging)."
  required_inputs: "AI_Economic_Value_Brief.md, AI_Feature_Strategy_Doc.md, PRD.md, Multi_Tenancy_Architecture_Spec.md, pricing & packaging spec."
  workflow: "Inventory AI-powered FRs, attach AI clauses to each, define acceptance gates against the eval harness, declare consent and data-use rules, write the AI_Feature_PRD_Spec.md."
  quality_standards: "Every AI-powered FR shall declare: hallucination tolerance, latency budget, $/call ceiling, abstain criteria, citation policy, consent or opt-in posture, training-data exclusion. Every acceptance gate shall be a numeric threshold backed by the eval harness."
  anti_patterns: "Do not approve an AI FR that is verifiable only by human judgement. Do not omit the abstain rule. Do not allow free-form output where structured output is feasible."
  outputs: "AI_Feature_PRD_Spec.md."
  references: "Use references/ai-feature-prd-spec-template.md and the addendum at references/ai-feature-prd-addendum.md."
---

# AI Feature PRD Spec Skill

## Overview

Produces the AI-feature complement to the generic PRD. Every AI-powered FR carries seven mandatory clauses that the generic PRD does not collect. The acceptance gates point at the eval harness as the test oracle.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `AI_Economic_Value_Brief.md`, `AI_Feature_Strategy_Doc.md`, `PRD.md`, `Multi_Tenancy_Architecture_Spec.md`, pricing & packaging spec |
| **Output** | `AI_Feature_PRD_Spec.md` |
| **Standard** | IEEE 830-1998, NIST AI RMF MAP/MEASURE |

## Core Instructions

### Step 1: Inventory AI-powered functional requirements

List every FR whose output is produced or modified by an AI component (LLM call, RAG, classifier, embedding search, agent action, fine-tune).

### Step 2: Attach the seven AI clauses to each FR

For each AI-powered FR, the spec MUST capture:

| Clause | Form | Example |
|--------|------|---------|
| Hallucination tolerance | factuality score threshold | factuality >= 0.92 on golden set; abstain otherwise |
| Latency budget | P95 target ms | P95 <= 2000 ms; timeout at 8000 ms with graceful fallback |
| $/call ceiling | USD or token cap | <= $0.04/call; throttle when tenant > $X/day |
| Abstain criteria | rule | abstain when retrieval returns < 2 relevant chunks OR confidence < 0.6 |
| Citation policy | rule | every claim about ingested document cites the source span |
| Consent / opt-in | rule | feature is opt-in per workspace admin; default off for EEA tenants |
| Training-data exclusion | rule | tenant content is not used to train the provider model; provider's no-training endpoint used |

### Step 3: Define structured output requirements

Where feasible the output is structured (JSON schema, function-call payload, enum). Free-form prose is reserved for user-visible text that has a separate guard (length, style, banned-terms list).

### Step 4: Define safety and content rules

State which content policy applies (no medical advice, no legal advice, no investment advice, no PII generation, no protected-class judgements). Cite the safety harness scenarios that verify each rule.

### Step 5: Define human-in-the-loop / contestability

Which decisions require human approval before commitment. How a user contests an output (button, reroute, escalation). Reference EU AI Act Art. 14 obligations where the feature is high-risk.

### Step 6: Define rollout posture per FR

Initial rollout (canary cohort, opt-in beta, free-tier first), promotion gates (eval pass, red-team pass, hallucination SLO met for N days), and the rollback trigger.

### Step 7: Define acceptance tests against the eval harness

Every AI FR has a row in the eval harness golden set with a pass threshold. Acceptance = "harness green for 30 d on this case set + red-team pass for the corresponding adversarial set".

### Step 8: Write the spec

`AI_Feature_PRD_Spec.md` sections: 1) AI FR Inventory, 2) Per-FR AI Clauses, 3) Structured Output Requirements, 4) Safety & Content Rules, 5) Human-in-the-Loop & Contestability, 6) Rollout Posture, 7) Eval Acceptance Gates, 8) Traceability to PRD and to eval harness IDs.

## Standards

- IEEE 830-1998
- NIST AI RMF MAP / MEASURE
- EU AI Act Art. 13 (transparency), Art. 14 (human oversight)
- OWASP LLM Top 10

## Resources

- `logic.prompt`, `README.md`, `references/ai-feature-prd-spec-template.md`, `references/ai-feature-prd-addendum.md`.
