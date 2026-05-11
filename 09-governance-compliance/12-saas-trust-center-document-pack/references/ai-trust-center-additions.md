# AI Additions to the Trust Center Document Pack

When the SaaS ships AI features, the Trust Center pack MUST add the following items.

## 1. AI sub-processor list (extension of the sub-processor list)

| Sub-processor | Role | Data classes | Region | Training exclusion | Notice |
|---------------|------|----------------|--------|---------------------|--------|
| <Provider A> | primary LLM | prompts + responses, possibly PII | EU/US | yes (contract + endpoint) | 30 d |
| <Provider B> | fallback LLM | as above | EU/US | yes | 30 d |
| <Embedding provider> | embeddings | doc text | EU/US | yes | 30 d |
| <Reranker> | re-ranking | retrieved chunks | EU/US | yes | 30 d |
| <Judge LLM> | nightly eval | sample of redacted responses | EU/US | yes | 30 d |

## 2. Responsible AI Declaration link

Link the public Responsible AI Declaration in the Trust Center index. The declaration is owned by `09-governance-compliance/14-ai-responsible-ai-declaration/`.

## 3. Per-feature model cards

Publish each per-feature model card (or a public summary thereof) in the Trust Center. Model cards are owned by `03-design-documentation/12-ai-model-card/`.

## 4. AI Act + regulatory compliance summary

Public summary of:

- EU AI Act tier per feature.
- US sectoral applicability.
- African DPA applicability.

Full doc owned by `09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/`.

## 5. AI incident-disclosure policy

State the AI-quality incident disclosure approach (status-page acknowledgement, customer-admin notice, postmortem window). Cross-link the incident-response runbook.

## 6. Customer questionnaire pre-fills

Pre-fill AI-relevant sections of:

- CAIQ v4 AI extensions when published.
- SIG Core / Lite AI sections.
- The vendor's own AI questionnaire from common AI buyers.

## 7. AI customer-data handling addendum

Add an AI-specific row to the customer-data handling table:

| Data class | Retention default | Deletion | Export | Residency | Encryption |
|------------|-------------------|----------|--------|-----------|------------|
| Conversation logs (AI) | 90 d hot / 13 mo cold | yes on offboarding | filtered export | per region | AES-256 + per-tenant key Enterprise |
| Embeddings (AI) | life of contract | yes on offboarding | n/a (regenerable) | per region | AES-256 + per-tenant key Enterprise |

## Cross-links

- Responsible AI Declaration: `09-governance-compliance/14-ai-responsible-ai-declaration/`
- AI Act Compliance Doc: `09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/`
- Per-feature Model Cards: `03-design-documentation/12-ai-model-card/`
