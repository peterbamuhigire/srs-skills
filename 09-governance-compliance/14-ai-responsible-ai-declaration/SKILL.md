---
name: "ai-responsible-ai-declaration"
description: "Generate the Responsible AI Declaration: the public-facing statement of what the product's AI does and does not do, the human-in-the-loop posture, contestability, data-use, model providers and sub-processors, and the regulatory tier assessment per feature."
metadata:
  use_when: "Use for every SaaS that ships AI features to external users. Mandatory before GA and updated quarterly."
  do_not_use_when: "Do not use for internal-only AI tools or research demonstrations."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Model_Card.md (per feature), AI_Architecture_Spec.md, AI_Act_Regulatory_Compliance_Doc.md, DPA, sub-processor list, Trust Center doc pack."
  workflow: "Inventory in-scope AI features, declare per-feature what AI does / does not, declare HITL and contestability, declare data use and training-data exclusion, list model providers and sub-processors, declare regulatory tier per feature, declare incident-disclosure approach, write the declaration."
  quality_standards: "Every AI feature shall have a does/does-not statement, an HITL statement, a data-use statement, a regulatory tier, and a model-provider declaration. Statements shall be reviewable by a layperson."
  anti_patterns: "Do not write marketing copy. Do not omit out-of-scope use. Do not claim 'safe' or 'unbiased' without naming the eval evidence."
  outputs: "Responsible_AI_Declaration.md (public) and Responsible_AI_Declaration_Internal.md (internal evidence pack)."
  references: "Use references/ai-responsible-ai-declaration-template.md."
---

# Responsible AI Declaration Skill

## Overview

The buyer-, regulator-, and user-facing statement of how the product uses AI. Anchored in Google AI Principles, Anthropic AUP/RSP, and the disclosure obligations of EU AI Act Art. 13.

## Core Instructions

### Step 1: Public summary

One paragraph: where AI appears in the product, what it does at a high level, what humans control.

### Step 2: Per-feature does / does not

For each AI feature publish:

- What the AI does (in plain language).
- What the AI does not do (limits, prohibited uses).
- What humans control (approval, contest, override).

### Step 3: Human oversight and contestability

State how a user can:

- Tell that AI produced an output.
- Regenerate, edit, or reject.
- Flag perceived inaccuracy.
- Escalate to a human reviewer.
- Request human-only handling where available.

### Step 4: Data use and training

Plain-language summary of:

- What customer data is sent to model providers.
- Whether that data is used to train provider general models (no).
- Whether it is used to train our fine-tunes (state policy).
- Retention of prompts and responses.
- Tenant isolation summary.

### Step 5: Model providers and sub-processors

List the model providers in use, the data passed to each, the contract terms (no-training, residency), and cross-link the sub-processor list.

### Step 6: Per-feature regulatory tier

For each feature declare the EU AI Act tier (prohibited / high-risk / limited-risk / minimal-risk), the US sectoral applicability, and the African DPA applicability where in scope.

### Step 7: Incident disclosure approach

State how AI-quality incidents (mass hallucinations, bias incidents, jailbreak disclosures, cross-tenant leaks) are disclosed. Tie to the SaaS incident-response runbook.

### Step 8: Review cadence

Quarterly review by the AI Lead + DPO + Security + Legal. Publish version history.

### Step 9: Write the two documents

- `Responsible_AI_Declaration.md` (public) -- plain language, no internal jargon.
- `Responsible_AI_Declaration_Internal.md` (internal) -- the evidence trail that backs every public statement.

## Standards

- EU AI Act Art. 13 (transparency)
- Google AI Principles
- Anthropic AUP / RSP
- ISO/IEC 42001 Clause 7.4 (communication)
- NIST AI RMF GOVERN
