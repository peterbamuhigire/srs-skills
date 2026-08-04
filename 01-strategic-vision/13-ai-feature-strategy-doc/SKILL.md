---
name: 13-ai-feature-strategy-doc
description: Use when a SaaS or digital product needs to choose, tier and sequence AI features, separate table stakes from differentiation, decide build versus buy, and define an AI moat; use AI economic value brief for a single initiative's value proof and AI architecture spec for implementation.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# AI Feature Strategy Doc Skill
<!-- dual-compat-start -->
## Use When

- Product leadership must select an AI portfolio and go-to-market position before feature PRDs.

## Do Not Use When

- Do not use to approve an AI feature without workflow value, data readiness, evaluation ownership or operating-cost evidence.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Product strategy, ICP and candidate AI uses | Vision, PRD and customer evidence | Required | Stop if features cannot be tied to user jobs. |
| Data, evaluation, model and cost constraints | AI, data, finance and risk owners | Required | Mark unavailable evidence as a sequencing blocker. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the AI Feature Strategy Document through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the AI Feature Strategy Document to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Feature Strategy Document | Product, commercial, PRD and AI architecture teams | Every selected feature has user value, tier, differentiation role, build/buy choice, evaluation owner, prerequisite and sequence gate. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified AI Feature Strategy Document draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Feature has distinctive data/workflow advantage | Prioritise as differentiation | Investment supports positioning |
| Feature is table stakes with mature supply | Buy or integrate behind a controlled gateway | Team rebuilds commodity capability |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Starting with a model catalogue. Fix: start with user jobs and economic outcomes.
- Calling every AI feature differentiating. Fix: compare table stakes and proprietary advantage.
- Choosing build for prestige. Fix: score control, data, cost, speed and switching risk.
- Tiering AI without cost guardrails. Fix: map usage limits and unit economics.
- Sequencing features before data and evaluation readiness. Fix: make prerequisites release gates.

## References

- [AI feature strategy template](references/ai-feature-strategy-doc-template.md)
- [AI economic value neighbour](../06-ai-economic-value-brief/SKILL.md)
- [AI architecture neighbour](../../03-design-documentation/11-ai-architecture-spec/SKILL.md)
<!-- dual-compat-end -->




## Overview

Use a problem-first decision: compare AI with a non-AI alternative, map the
human/system/model/data layers, and sequence offline evaluation, shadow, human-
supervised, canary, and wider release. Each strategic AI bet needs a value
hypothesis, guardrails, owner, rollback and post-launch drift review.

Produces the strategic spine of an AI-feature SaaS: which AI features exist, who pays for them, what the moat is, and which models the company builds versus buys. Sits between the AI Economic Value Brief (per-feature) and the AI Feature PRD Spec (per-feature requirements).

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `Vision_Statement.md`, `PRD.md`, pricing & packaging spec, competitor scan, per-feature AI economic-value briefs |
| **Output** | `AI_Feature_Strategy_Doc.md` |
| **Standard** | NIST AI RMF GOVERN; ISO/IEC 42001 Clause 6 (planning) |

## Core Instructions

### Step 1: Inventory AI features

List every AI-powered feature in roadmap. For each: feature name, user-visible behaviour, buyer outcome (what the buyer can claim after deploying it).

### Step 2: Classify differentiating vs table-stakes

Per Christensen's jobs-to-be-done framing and Wardley-mapping practice: features become table-stakes as the category matures. Classify each:

- **Differentiating** — buyers will choose us over competitor because of this feature.
- **Table-stakes** — buyers will reject us if this feature is absent. Build to parity, not beyond.
- **Experimental** — included for strategic optionality; not sold or marketed yet.

Every "differentiating" claim cites a competitor row that lacks the feature.

### Step 3: Tier placement

Map each feature to a pricing tier from the pricing & packaging spec. Patterns:

- AI summarisation often free / Starter — table-stakes.
- AI assistants / copilots usually Professional / Business tier.
- Domain-specific agents and analytics often Enterprise — high cost, high differentiation.

### Step 4: Build-vs-buy per model

For each feature, choose the model class:

| Choice | When | Cost profile | Risk |
|--------|------|--------------|------|
| Hosted general-purpose (Claude, GPT, Gemini) | fastest TTM, general tasks | $/token, variable | model-provider dependency, training-data terms |
| Hosted specialised (vertical models) | regulated domain, retrieval-heavy | $/token, lower | smaller ecosystem |
| Open-weights self-hosted | data-sovereignty, predictable cost | $/compute hour | ops burden, eval gap |
| Fine-tune of hosted base | repetitive narrow task, cost reduction | base + fine-tune | training-data governance |
| Classical ML | structured prediction, low latency | $/compute | data labelling cost |

State the verdict per feature with the rejected alternatives.

### Step 5: Moat declaration

For each differentiating feature, name the moat asset:

- **Proprietary data** — what data, why competitors cannot replicate it.
- **Distribution** — channels, integration partners, lock-in.
- **Integration depth** — which systems we ingest from / write to.
- **Fine-tune / eval suite** — the regression-tested prompt and dataset is itself an asset.
- **Operational learning** — telemetry feedback loop improves the model.

A feature with no named moat is at best table-stakes; relabel it.

### Step 6: Sequencing roadmap

Order features by: revenue lift × confidence ÷ cost-to-build. Place each in a quarter. Mark dependencies (eval harness, data foundation, content store, billing changes).

### Step 7: Risk and dependency register

Single-table register: model-provider risk, regulatory risk, dataset risk, eval-gap risk, cost-volatility risk. Each row has mitigation and owner.

### Step 8: Write the doc

`AI_Feature_Strategy_Doc.md` sections: 1) AI Feature Inventory, 2) Differentiation Map, 3) Tier Placement, 4) Build-vs-Buy Verdicts, 5) Moat Declaration, 6) Sequencing Roadmap, 7) Risk & Dependency Register, 8) Glossary.

## Standards

- NIST AI RMF GOVERN
- ISO/IEC 42001 Clause 6
- Wardley Mapping for tech evolution

## Resources

- `logic.prompt`, `README.md`, `references/ai-feature-strategy-doc-template.md`.
