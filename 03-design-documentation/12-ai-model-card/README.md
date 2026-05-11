## Objective

Produce a model card per deployed (feature, model, prompt, retrieval) tuple. The card is the buyer-, auditor-, and Responsible-AI-committee-facing artefact.

## Execution Steps

1. Verify AI_Feature_PRD_Spec.md and AI_Architecture_Spec.md exist plus the latest eval and red-team reports.
2. Invoke `logic.prompt` once per AI feature.
3. Publish each card to the trust center and link from the AI Responsible AI Declaration.

## Standards

- Mitchell et al. (2019)
- EU AI Act Annex IV
- NIST AI RMF MEASURE
- ISO/IEC 42001
