---
name: "ai-model-card"
description: "Generate the AI Model Card per deployed AI feature: purpose, training data summary, evaluation metrics, limitations, bias notes, intended and out-of-scope use, version pin, and the EU AI Act Annex IV technical-documentation cross-walk."
metadata:
  use_when: "Use for every AI feature that ships to production. One model card per (feature, model-version, prompt-tag) deployable."
  do_not_use_when: "Do not use for research-only or internal experiments not exposed to customers."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Architecture_Spec.md, AI_Data_And_Knowledge_Base_Spec.md, latest eval report, latest red-team report, provider model card (for hosted models)."
  workflow: "Collect model + prompt + retrieval pins, summarise training data, attach eval metrics, attach red-team summary, declare limitations and bias notes, declare intended and out-of-scope use, cross-walk to EU AI Act Annex IV, write the model card."
  quality_standards: "Every model card shall include the version pin, the eval metrics with date, the red-team summary, named limitations, named bias risks with mitigations, intended use, and prohibited use."
  anti_patterns: "Do not write a model card without limitations. Do not omit the date and version pin. Do not copy the provider's model card unchanged."
  outputs: "Model_Card_<feature>_v<version>.md."
  references: "Use references/ai-model-card-template.md."
---

# AI Model Card Skill

## Overview

Produces the per-feature model card that buyers, auditors, and Responsible-AI reviewers will read. Anchored in Mitchell et al. (2019) and the EU AI Act Annex IV technical documentation requirements.

## Core Instructions

### Step 1: Identify the artefact under cardification

A model card refers to a deployed combination: { feature, base model + version, prompt registry tag, retrieval index version, post-processing rules }. Pin all four.

### Step 2: Purpose section

Describe what the feature does, who uses it, what decisions it informs, and the buyer outcome. Reference the AI FR ID.

### Step 3: Training and grounding data summary

For hosted base models, cite the provider's training-data disclosure with a date. For our retrieval data, summarise: sources (cite the AI Data Spec), volumes, languages, freshness, exclusions. For fine-tunes, list training set, size, labelling provenance, holdout set.

### Step 4: Evaluation metrics

Attach the most recent eval report for the feature: golden-set pass rate, factuality, abstention precision, citation rate, hallucination rate, judge-LLM score, latency P95, cost per call. Each metric carries the date and the eval set ID.

### Step 5: Red-team summary

Latest red-team result by category: prompt injection, jailbreak, data exfiltration, cross-tenant leak, PII surfacing, hallucination probe, bias surfacing. Pass / fail per category; any open finding with severity and remediation date.

### Step 6: Limitations

List known limitations as concrete failure modes:

- Knowledge cutoff date for the base model.
- Languages or locales not yet evaluated.
- Domain edge cases the eval set under-represents.
- Latency degradation conditions.

### Step 7: Bias notes and mitigations

List bias risks identified (gender, race, age, disability, geography, language) and the mitigation in place (eval set composition, abstain rule, content filter, human-in-the-loop).

### Step 8: Intended use and out-of-scope use

Intended use: business contexts the feature supports. Out-of-scope: contexts where it must not be used (e.g. medical decisions, legal advice, hiring, lending). Mirror the safety rules in the PRD spec.

### Step 9: Operational pins

Model + version, prompt registry tag, retrieval index version, gateway config tag, content-filter version, eval suite tag.

### Step 10: EU AI Act Annex IV cross-walk

Map each Annex IV element to the section of this model card that satisfies it:

| Annex IV item | Where covered |
|----------------|----------------|
| General description of the AI system | Purpose |
| Elements of the AI system and process of its development | Training/Grounding + Operational Pins |
| Data sets used | Training/Grounding + AI Data Spec |
| Validation and testing procedures | Evaluation + Red-team |
| Risk management measures | Limitations + Bias + Operational Pins |
| Human oversight | Intended Use + AI FR clause |
| Changes through the lifecycle | Versioning section |

### Step 11: Write the card

`Model_Card_<feature>_v<version>.md`. Date-stamped. Owner named.

## Standards

- Mitchell et al. (2019) Model Cards for Model Reporting
- EU AI Act Annex IV
- NIST AI RMF MEASURE
- ISO/IEC 42001
