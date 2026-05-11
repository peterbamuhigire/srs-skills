---
name: "ai-feature-strategy-doc"
description: "Generate the AI Feature Strategy Doc for a SaaS product: AI feature inventory by tier, differentiating-vs-table-stakes split, build-vs-buy decisions on models, moat analysis, sequencing, and the AI-feature go-to-market position."
metadata:
  use_when: "Use when a SaaS roadmap contains two or more AI-powered features and the product needs an explicit strategy that ties each AI feature to a pricing tier, a buyer outcome, and a model-choice rationale."
  do_not_use_when: "Do not use for a single AI experiment or a research prototype with no commercial commitment."
  required_inputs: "Vision_Statement.md, PRD.md, pricing & packaging spec, competitor scan, AI Economic Value Brief for each candidate feature."
  workflow: "Inventory candidate AI features, classify each as differentiating or table-stakes, set tier placement, pick build-vs-buy per model, declare moat assumptions, write the sequencing roadmap, write the AI_Feature_Strategy_Doc.md."
  quality_standards: "Every AI feature shall name its buyer outcome, tier placement, model class, build-vs-buy verdict, and moat dependency. Every claim of differentiation shall cite a competitor scan."
  anti_patterns: "Do not list AI features without a buyer outcome. Do not place every AI feature at the top tier by default. Do not declare moat without naming the asset (data, distribution, integration, fine-tune, eval suite)."
  outputs: "AI_Feature_Strategy_Doc.md."
  references: "Use references/ai-feature-strategy-doc-template.md."
---

# AI Feature Strategy Doc Skill

## Overview

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
