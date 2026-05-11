---
name: "ai-rca-taxonomy-doc"
description: "Generate the AI RCA (Root-Cause Analysis) Taxonomy Doc: full catalogue of AI failure root causes across six families — model (regression, deprecation, fine-tune drift, distribution shift, prompt regression), retrieval (index drift, embedding-model change, citation drift), tool/agent (tool API change, schema change, vendor outage, indirect injection, action-scope expansion), eval (test-set rot, judge drift, golden-set leakage), data (training-data shift), infra (gateway routing change), commercial (provider price change, rate-limit change). Each node carries an example incident and a default mitigation pointer."
metadata:
  use_when: "Use as the shared vocabulary feeding the AI incident response runbook, postmortem template, drill catalogue, and Responsible-AI committee review. Mandatory once two or more AI features are in production."
  do_not_use_when: "Do not use as a substitute for per-incident RCA; the taxonomy provides the labels, not the analysis."
  required_inputs: "AI_Incident_Response_Runbook.md, AI_Hallucination_SLO_Doc.md, AI_Feature_Rollout_Runbook.md, AI_Cost_Runbook.md, AI_Architecture_Spec.md, AI_Eval_Harness_Spec.md, AI_Red_Team_Test_Plan.md, AI_Model_Card.md."
  workflow: "Enumerate the six families and their nodes; attach example incidents; attach default mitigation pointer; define the rule for tagging a postmortem; write the doc."
  quality_standards: "Every node shall carry at least one example. Every node shall point to a default mitigation procedure (containment mode) and the eval / red-team test that detects it pre-production. Every postmortem shall close with one or more taxonomy tags."
  anti_patterns: "Do not invent novel taxonomies per incident. Do not allow a postmortem to close without a taxonomy tag. Do not conflate model and retrieval failure modes."
  outputs: "AI_RCA_Taxonomy_Doc.md."
  references: "Use references/ai-rca-taxonomy-reference.md."
---

# AI RCA Taxonomy Doc Skill

## Overview

When a postmortem closes with a free-text root cause, the engine accumulates noise. The RCA taxonomy gives the team a shared vocabulary: every postmortem closes with one or more taxonomy tags, and the rolling Responsible-AI committee review aggregates by tag to find systemic weaknesses (e.g., 4 of the last 10 incidents were `retrieval.index-drift` — investment indicated).

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Response Runbook, Hallucination SLO, Rollout Runbook, Cost Runbook, AI Architecture, Eval Harness, Red-Team Plan, Model Card |
| **Output** | `AI_RCA_Taxonomy_Doc.md` |
| **Standards** | NIST AI RMF MAP-2; ISO/IEC 42001 Annex A.6; CAST (Causal Analysis based on Systems Theory) |

## Core Instructions

### Step 1: Six families

1. **Model** — primary or fallback foundation-model behaviour.
2. **Retrieval** — RAG index, embeddings, ranking, citations.
3. **Tool / agent** — agent tools, schemas, scopes, indirect injection.
4. **Eval** — golden sets, judge LLMs, calibration, test-set leakage.
5. **Data** — training data, ingestion, distribution shift.
6. **Infra & commercial** — gateway, routing, provider pricing, provider rate limits.

### Step 2: Enumerate nodes per family

State the canonical list per family (see `references/ai-rca-taxonomy-reference.md` for the catalogue). For each node:

- Node id (`family.node`).
- One-sentence definition.
- Example incident (synthetic or anonymised real).
- Default containment pointer (one of the six modes; per `14-ai-incident-response-runbook`).
- Pre-production detection (eval harness test, red-team test, monitoring alert).
- Durable mitigation (typical action-item class).

### Step 3: Tagging rule

Every postmortem closes with at least one tag, optionally multiple. Tags can be `primary` and `contributing`. The IC assigns; the RAI committee can re-tag during review with justification.

### Step 4: Aggregation rule

The Responsible-AI committee reviews tag frequency monthly. Investment thresholds:

- 3 or more incidents tagged the same node in a quarter -> action item escalated to road-map.
- 1 incident tagged a node with SEV1 outcome -> review the pre-production detection for that node.

### Step 5: Write the doc

`AI_RCA_Taxonomy_Doc.md` sections: 1) Families, 2) Node Catalogue, 3) Tagging Rule, 4) Aggregation & Review Cadence, 5) Cross-Refs.

## Standards

- NIST AI RMF MAP-2
- ISO/IEC 42001 Annex A.6 (incident handling and improvement)
- CAST (causal analysis based on systems theory, Leveson)
- Google SRE blameless RCA

## Resources

- `logic.prompt`, `README.md`, `references/ai-rca-taxonomy-reference.md`.
