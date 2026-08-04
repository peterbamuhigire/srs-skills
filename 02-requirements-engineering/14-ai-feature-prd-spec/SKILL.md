---
name: 14-ai-feature-prd-spec
description: "Use when converting an approved AI feature strategy into testable PRD requirements for quality, latency, cost, abstention, citations, consent, and evaluation; use ai-feature-strategy-doc for portfolio choices."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# AI Feature PRD Spec Skill

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- converting an approved AI feature strategy into testable PRD requirements for quality, latency, cost, abstention, citations, consent, and evaluation; use ai-feature-strategy-doc for portfolio choices.
- Use this procedure when the required source artefacts are available and `AI feature PRD specification` is the next lifecycle deliverable.

## Do Not Use When

- Use `ai-feature-strategy-doc` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Approved AI feature strategy, users, data constraints, and evaluation targets | Product owner and AI governance owner | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `AI feature PRD specification`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| AI feature PRD specification | AI architecture, evaluation, safety, and delivery teams | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `AI feature PRD specification` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A model behaviour has no measurable evaluation oracle | Mark it blocked and define the dataset, metric, threshold, and owner. | An AI claim that cannot be tested or governed. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `AI feature PRD specification` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `AI feature PRD specification` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `ai-feature-strategy-doc` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
- [Ai Agent Feature Addendum Crosslink](references/ai-agent-feature-addendum-crosslink.md)
- [Ai Feature Prd Addendum](references/ai-feature-prd-addendum.md)
- [Ai Feature Prd Spec Template](references/ai-feature-prd-spec-template.md)
- [AI system and human-control contract](references/ai-system-human-control-contract.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

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

Also attach the model/system/input/output map, human oversight, correction,
contest, undo or safe fallback, consent/notice, drift signal, and rollback
acceptance evidence from `references/ai-system-human-control-contract.md`.

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
