# Responsible AI Declaration

Last reviewed: YYYY-MM-DD
Next review: YYYY-MM-DD
Owner: <AI Lead>
Sign-off: AI Lead, DPO, Security Lead, Legal

## 1. Summary

<Product> uses artificial intelligence in <N> features to help users <buyer outcome>. AI is used to assist humans, not to replace human judgement on consequential decisions. Customers control whether AI is on, what data it can see, and how its outputs are used.

## 2. Where AI Appears

| Feature | What the AI does | What the AI does NOT do | Human control |
|---------|--------------------|---------------------------|------------------|
| AI Summary | drafts a short summary of a thread you already have access to | does not retrieve content from other workspaces; does not give legal, medical, financial advice | regenerate, edit, dismiss |
| AI Composer | drafts a reply you can edit and send | does not send messages on your behalf; does not contact people outside your workspace | edit and send, regenerate, discard |
| AI Analyst | answers questions about your own data with citations | does not access other tenants' data; does not provide regulated advice | view SQL, view rows, flag |
| AI Agent (Enterprise) | proposes multi-step actions from an approved-actions catalogue and asks you to approve each step | does not execute unapproved actions; does not run irreversible actions without per-step approval | per-step approve / reject; full audit log |

## 3. Human Oversight and Contestability

- Every AI output is labelled (icon + tooltip) so you can tell AI produced it.
- You can regenerate, edit, or reject any AI output.
- You can flag a perceived inaccuracy ("Report inaccurate" button). Flagged outputs are reviewed by our team within 1-5 business days depending on plan.
- You can escalate to a human reviewer at any time.
- You can request human-only handling on your workspace; admins can disable any AI feature.

## 4. Data Use and Training

- Your data is sent to model providers only to process your requests.
- Model providers shall NOT use your data to train their general models. We have contract language and product configurations enforcing this.
- We do not currently fine-tune models on your customer-private data without your separate written consent.
- Prompt and response logs are retained on a per-tenant partition for 90 days hot and 13 months cold; you can request earlier deletion.
- Your data is encrypted at rest and in transit. Per-tenant key on Enterprise tier.

## 5. Model Providers and Sub-processors

| Provider | Used for | Data classes | Training exclusion | Region |
|----------|----------|----------------|---------------------|--------|
| <Provider A> | primary models for all AI features | request text, retrieved chunks, response text | yes (contract + endpoint) | EU / US |
| <Provider B> | fallback models | as above | yes | EU / US |
| <Reranker> | retrieval reranking | retrieved chunks | yes | EU / US |
| <Judge> | nightly eval | sample of production responses, redacted | yes | EU / US |

Cross-link: full sub-processor list in the Trust Center.

## 6. Regulatory Posture per Feature

| Feature | EU AI Act tier | US sectoral | African DPA notes |
|---------|------------------|---------------|----------------------|
| AI Summary | limited-risk | n/a | KE/NG/ZA consent notice |
| AI Composer | limited-risk | n/a | KE/NG/ZA consent notice |
| AI Analyst | limited-risk | not used for lending / hiring / housing / insurance underwriting | KE/NG/ZA consent notice |
| AI Agent | case-by-case; high-risk for some workflows; per-step approval keeps risk in check | not used for credit, hiring | KE/NG/ZA consent notice |

## 7. Incident Disclosure

If we discover a material AI-quality incident (mass-scale hallucination, bias incident in a regulated decision, jailbreak that exposes system content, cross-tenant data leak), we will:

- Acknowledge the incident on the status page within 1 hour for SEV1.
- Notify affected customer admins within 4 hours for SEV1.
- Publish a postmortem within 5 business days for SEV1.
- Update affected model cards and this declaration within 10 business days.

## 8. Version History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | YYYY-MM-DD | initial publication |
| 1.1 | YYYY-MM-DD | added AI Agent; updated model providers |
