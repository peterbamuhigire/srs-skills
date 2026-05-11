---
name: "ai-adr-catalogue"
description: "Generate the AI ADR Catalogue: the required architecture decision records for an AI-feature SaaS -- model choice, RAG vs fine-tune, vector store, eval threshold, abstain policy, content filter, fallback, retraining trigger, and the prompt-registry change protocol."
metadata:
  use_when: "Use as soon as the AI Architecture Spec is drafted. Each AI feature shipping to production shall have its ADR catalogue completed."
  do_not_use_when: "Do not use for projects without AI features or for one-off research prototypes."
  required_inputs: "AI_Architecture_Spec.md, AI_Feature_PRD_Spec.md, AI_Model_Card.md, AI_Eval_Harness_Spec.md, AI_Red_Team_Test_Plan.md."
  workflow: "Inventory required ADR slots, fill each ADR with context / decision / consequences / alternatives / evidence, index them in the AI ADR register, link to the central ADR catalogue, write the catalogue doc."
  quality_standards: "Every required ADR slot shall be filled or explicitly waived with an ADR-style waiver. Every decision shall cite its alternatives and the evidence that drove the choice."
  anti_patterns: "Do not record decisions without alternatives. Do not let ADRs lag behind production changes."
  outputs: "AI_ADR_Catalogue.md and ADR-AI-NNNN-<slug>.md files."
  references: "Use references/ai-adr-templates.md."
---

# AI ADR Catalogue Skill

## Required ADR slots

Every AI-feature SaaS shall have ADRs for the following decisions. Missing ADRs are blockers for GA.

1. **Model Gateway as Sole Egress** — yes/no, providers in scope, fallback policy.
2. **Primary Model per Feature** — vendor + model + version pin.
3. **Fallback Model per Feature** — vendor + conditions.
4. **RAG vs Fine-tune vs Agent per Feature** — pattern verdict with drivers.
5. **Vector Store Choice** — technology, partitioning model.
6. **Embedding Model Choice** — provider + version + cost profile.
7. **Eval Threshold per Feature** — pass threshold + regression tolerance.
8. **Abstain Policy per Feature** — threshold + payload.
9. **Content Filter Chain** — filters + order + on-trip behaviour.
10. **Prompt Registry Change Protocol** — PR / eval / sign-off / deploy.
11. **Conversation Log Retention** — hot/cold + per-tenant partition.
12. **Training-Data Exclusion Policy** — global rule + per-provider evidence.
13. **Cross-Tenant Retrieval Prohibition** — gateway enforcement mechanism.
14. **Judge-LLM Selection** — model + calibration.
15. **Cost Ceiling and Throttle Policy** — per-feature / per-tenant.
16. **Rollback Trigger Set** — auto vs manual triggers.
17. **Retraining / Re-evaluation Trigger** — model bump policy.

## Workflow

1. Read inputs.
2. For each ADR slot, generate `ADR-AI-NNNN-<slug>.md` using `references/ai-adr-templates.md`.
3. Index in `AI_ADR_Catalogue.md`.
4. Link from the central `09-governance-compliance/05-architecture-decision-records` register.
5. Sign-off per ADR: AI Lead + Architect + (DPO for compliance-touching ADRs).

## Standards

- ADR pattern (Nygard)
- ISO/IEC 42001 Clause 8 (operation)
- IEEE 1016-2009 §5 (Design viewpoints)
