---
name: 14-ai-agent-strategy-doc
description: Use when a product may ship tool-using AI agents and needs to decide agent versus workflow, autonomy levels, tiered capabilities, action-catalogue advantage and sequencing; use AI feature strategy for the wider AI portfolio and agent architecture after approval.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# AI Agent Strategy Doc Skill
<!-- dual-compat-start -->
## Use When

- Product and risk owners must justify agentic autonomy and define its commercial and control boundaries.

## Do Not Use When

- Do not use for a direct model call, ordinary RAG answer or deterministic automation that needs no planning or tool use.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Candidate workflows, actions and user value | Product discovery and operational owners | Required | Stop if the action catalogue or accountable user outcome is undefined. |
| Risk tolerance, approval policy and cost envelope | Security, compliance, finance and product owners | Required | Default to the lowest autonomy level until approved evidence exists. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the AI Agent Strategy Document through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the AI Agent Strategy Document to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Agent Strategy Document | Product, pricing, PRD, security and agent architecture teams | Each agent use case has agent-necessity rationale, autonomy level, allowed actions, approval boundary, tier, success measure, cost limit and sequence gate. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified AI Agent Strategy Document draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Task needs adaptive planning across bounded tools | Consider an agent with minimum autonomy | Complexity is justified |
| Task is deterministic or one-step | Use a workflow or direct call | Agent risk and cost are unnecessary |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Calling a chatbot an agent. Fix: require planning plus bounded tool action.
- Starting at autonomous mode. Fix: begin at the lowest useful approval level.
- Treating more tools as more value. Fix: bound actions to the user job and risk policy.
- Ignoring attempted-versus-completed cost. Fix: define budgets and outcome accounting.
- Claiming an action-catalogue moat without usage evidence. Fix: define telemetry and compounding learning.

## References

- [Agent strategy template](references/ai-agent-strategy-doc-template.md)
- [AI feature strategy neighbour](../13-ai-feature-strategy-doc/SKILL.md)
- [Agent architecture neighbour](../../03-design-documentation/14-ai-agent-architecture-spec/SKILL.md)
<!-- dual-compat-end -->




## Overview

Produces the strategic spine of an agent-feature SaaS. Sits between `ai-feature-strategy-doc` (covers AI features in general) and `ai-agent-feature-prd-spec` (per-feature agent requirements). Forces the team to defend every "this is an agent" claim and to place each agent feature on an explicit autonomy ladder.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `AI_Feature_Strategy_Doc.md`, `PRD.md`, pricing & packaging spec, competitor scan, per-feature AI economic-value briefs |
| **Output** | `AI_Agent_Strategy_Doc.md` |
| **Standard** | NIST AI RMF GOVERN; ISO/IEC 42001 Clause 6 (planning); EU AI Act Art. 14 (human oversight) |

## Core Instructions

### Step 1: Apply the agent-vs-workflow gate

For every candidate agent feature, answer four questions:

1. Is the task **multi-step** with branching that cannot be fully enumerated at design time?
2. Does the task require **tool use** beyond a single retrieval call (write actions, external API calls, multi-source reads)?
3. Is the success criterion **outcome-shaped** rather than a single-shot generation match?
4. Does the optimal step count vary with input?

A feature that answers "yes" to fewer than three questions is a workflow or a direct LLM call, not an agent. Reclassify and stop.

### Step 2: Classify each agent feature by autonomy level

Use this ladder. Every agent feature shall be placed on exactly one rung.

| Level | Name | Human role | Example |
|-------|------|------------|---------|
| L0 | Suggest | Human reads the plan; agent does not act | "Draft a follow-up email and the agent suggests the recipients" |
| L1 | Approve each step | Human clicks approve per tool call | "Refund-issuance assistant; each refund needs admin click" |
| L2 | Approve batch / plan | Human approves the full plan once; agent executes | "Inbox triage; one approval of the proposed plan, then the agent acts" |
| L3 | Autonomous within guardrails | Agent acts within an explicit policy envelope; human reviews after the fact | "Recurring reconciliation agent that runs nightly within a $X budget" |
| L4 | Fully autonomous | No human in the loop on a per-run basis; supervisor agent only | Rarely appropriate for buyer-facing SaaS in 2026 |

### Step 3: Place each agent feature on the capability ladder by tier

Patterns:

- Free / Starter tier — typically L0 suggest agents only; no write actions.
- Pro / Business tier — L1 or L2 with constrained action catalogue; idempotent and compensable actions only.
- Enterprise — L2 or L3 with full action catalogue including irreversible actions, gated by human approval and policy envelope.
- L4 reserved for internal-ops agents with a named owner, not for buyer-facing surfaces.

### Step 4: Declare the agent moat asset

Generic AI moat from `ai-feature-strategy-doc` applies, but agents add specific moat candidates:

- **Proprietary action catalogue** — tools that competitors do not have access to (deep integrations, partner APIs, internal data systems).
- **Action telemetry** — the corpus of agent-task traces is itself an asset for eval, fine-tuning, and product improvement.
- **Eval-set and red-team registry** — battle-tested adversarial scenarios are a moat against agent failure modes.
- **Trust / authority capital** — buyer trust to grant write access is hard-earned and slow-moving.

An agent feature with no named moat is at best parity; reclassify to table-stakes or cut.

### Step 5: Sequencing roadmap and dependency map

Order agent features by `(revenue lift × autonomy-defensibility) ÷ (irreversibility risk × build cost)`. Place each in a quarter. Mark dependencies: agent runtime, action catalogue, eval rig, audit log, kill-switch infrastructure, human-approval UI.

### Step 6: Risk and dependency register

Single-table register: irreversible-action risk, action-escalation risk, indirect-prompt-injection risk, cross-tenant action risk, supervision-cost risk, regulatory tier risk (EU AI Act high-risk if irreversible or decisional). Each row has mitigation and owner.

### Step 7: Write the doc

`AI_Agent_Strategy_Doc.md` sections: 1) Agent-vs-Workflow Verdicts, 2) Autonomy Ladder Placement, 3) Tier Placement, 4) Moat Declaration, 5) Sequencing Roadmap, 6) Risk & Dependency Register, 7) Glossary.

## Standards

- NIST AI RMF GOVERN
- ISO/IEC 42001 Clause 6 (planning)
- EU AI Act Art. 14 (human oversight) for autonomy-level placement
- Anthropic agentic-AI guidance (Building effective agents, 2024)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-strategy-doc-template.md`.
