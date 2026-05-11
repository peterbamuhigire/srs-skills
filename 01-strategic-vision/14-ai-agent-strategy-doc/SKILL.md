---
name: "ai-agent-strategy-doc"
description: "Generate the AI Agent Strategy Doc: when to use an agent vs a workflow or a single LLM call, agent capability ladder by pricing tier, autonomy-level taxonomy (suggest / approve-each / approve-batch / autonomous), proprietary action catalogue and tool-telemetry moat, and the agent-feature sequencing roadmap."
metadata:
  use_when: "Use whenever a SaaS roadmap contains one or more agentic features — features where an LLM plans, calls tools, and acts on behalf of the user or tenant across multiple steps."
  do_not_use_when: "Do not use for products that ship only direct-LLM or RAG features without tool-using planners; cover those with `ai-feature-strategy-doc` alone."
  required_inputs: "AI_Feature_Strategy_Doc.md, PRD.md, pricing & packaging spec, competitor scan, AI Economic Value Brief for each candidate agent feature."
  workflow: "Apply the agent-vs-workflow gate per candidate feature, classify each agent feature by autonomy level, place on the agent capability ladder by tier, declare the agent moat asset, write the sequencing roadmap, write the AI_Agent_Strategy_Doc.md."
  quality_standards: "Every agentic feature shall pass the agent-vs-workflow gate before being included. Every agent feature shall declare an autonomy level, a tier placement, a moat asset, and the irreversibility profile of its action catalogue at the strategic level."
  anti_patterns: "Do not classify a deterministic workflow as an agent because it uses an LLM. Do not place an autonomous-tier agent feature in a Free tier. Do not declare an agent moat without naming the asset (proprietary action catalogue, action telemetry, eval-set, integration depth)."
  outputs: "AI_Agent_Strategy_Doc.md."
  references: "Use references/ai-agent-strategy-doc-template.md."
---

# AI Agent Strategy Doc Skill

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
