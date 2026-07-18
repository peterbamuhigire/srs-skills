---
name: 16-ai-agent-feature-prd-spec
description: "Use when defining testable product requirements for an agent's task scope, autonomy, budgets, intervention, success, and irreversible-action gates; use ai-agent-strategy-doc for portfolio strategy."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# AI Agent Feature PRD Spec Skill

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- defining testable product requirements for an agent's task scope, autonomy, budgets, intervention, success, and irreversible-action gates; use ai-agent-strategy-doc for portfolio strategy.
- Use this procedure when the required source artefacts are available and `AI agent feature PRD specification` is the next lifecycle deliverable.

## Do Not Use When

- Use `ai-agent-strategy-doc` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Approved agent strategy, user journeys, action catalogue, and risk limits | Product owner, operator, and AI governance owner | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `AI agent feature PRD specification`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| AI agent feature PRD specification | Agent architecture, evaluation, red-team, and operations teams | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `AI agent feature PRD specification` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| An action is irreversible or high impact | Require explicit approval, evidence capture, and a tested recovery path. | Unbounded agent side effects. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `AI agent feature PRD specification` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `AI agent feature PRD specification` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `ai-agent-strategy-doc` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
- [Ai Agent Feature Prd Spec Template](references/ai-agent-feature-prd-spec-template.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

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
