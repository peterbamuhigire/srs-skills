# AI Feature Strategy Doc Template

## 1. AI Feature Inventory

| Feature | User-visible behaviour | Primary persona | Buyer outcome |
|---------|------------------------|------------------|---------------|
| AI Summary | one-paragraph thread summary | end user | reduces triage time |
| AI Composer | drafts replies from context | end user | reduces handle time |
| AI Analyst | answers natural-language data questions | analyst / exec | reduces SQL time |
| AI Agent | executes multi-step approved workflow | ops user | removes manual steps |

## 2. Differentiation Map

| Feature | Class | Competitor parity (vendor, status) | Notes |
|---------|-------|------------------------------------|-------|
| AI Summary | table-stakes | Vendor A, B, C all have | build to parity, do not over-invest |
| AI Composer | differentiating | Vendor A weak, B absent | invest in tone-control and citation |
| AI Analyst | differentiating | Vendor B absent | moat is data-model coverage |
| AI Agent | experimental | nobody ships yet | optionality |

## 3. Tier Placement

| Feature | Free | Starter | Pro | Business | Enterprise |
|---------|------|---------|-----|----------|------------|
| AI Summary | limited | yes | yes | yes | yes |
| AI Composer | -- | -- | yes | yes | yes |
| AI Analyst | -- | -- | -- | yes | yes |
| AI Agent | -- | -- | -- | -- | yes |

## 4. Build-vs-Buy Verdicts

| Feature | Verdict | Model class | Rejected alternatives | Cost profile |
|---------|---------|--------------|------------------------|--------------|
| AI Summary | buy | hosted general | self-host (ops burden), fine-tune (no benefit) | $/M tokens, capped |
| AI Composer | buy + prompt-engineer | hosted general | fine-tune (next year) | $/M tokens, premium model on Pro+ |
| AI Analyst | buy + RAG | hosted general + vector store | classical ML (insufficient flexibility) | $/M tokens + vector ops |
| AI Agent | buy + custom orchestration | hosted general + tools | open-weights (eval gap), fine-tune (premature) | $/M tokens + tool invocations |

## 5. Moat Declaration

| Feature | Moat asset | Evidence |
|---------|------------|----------|
| AI Summary | none -- table-stakes | n/a |
| AI Composer | proprietary tone/style dataset; eval suite | 12k labelled examples; 240 regression cases |
| AI Analyst | integration depth into customer data sources | 60+ adapters; warehouse-native |
| AI Agent | operational learning from approved-workflow telemetry | rollouts after each cohort tune the agent policy |

## 6. Sequencing Roadmap

| Quarter | Feature | Dependencies | Exit gate |
|---------|---------|--------------|-----------|
| Q1 | AI Summary GA | eval harness, model gateway | citation rate >= 90% on golden |
| Q2 | AI Composer GA | tone dataset, prompt registry | red-team pass; hallucination SLO met for 30 d |
| Q3 | AI Analyst Beta | RAG store, semantic layer, billing event | per-tenant cost ceiling validated |
| Q4 | AI Agent Limited Availability | approved-action catalogue, human-approval UI | SEV1-clean for 60 d in pilot cohort |

## 7. Risk and Dependency Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|
| Model provider price increase | M | M | dual-provider gateway + open-weights fallback path | CTO |
| EU AI Act high-risk classification of AI Agent | M | H | scope agent to non-high-risk uses; human-in-the-loop on every action | DPO + Legal |
| Eval suite drift after model upgrade | H | M | regression on every model bump; promote only on green | AI Lead |
| Per-tenant cost runaway on AI Analyst | M | M | per-tenant ceiling, throttle, escalate | FinOps |
| Cross-tenant leak via shared embeddings | L | H | per-tenant index, isolation evidence pack | Security |

## 8. Glossary

- **Moat asset** — the resource a competitor cannot replicate by buying the same hosted model.
- **Differentiating** — buyer chooses us because of this.
- **Table-stakes** — buyer rejects us without this; parity-build only.
- **Experimental** — present for optionality, not sold yet.
