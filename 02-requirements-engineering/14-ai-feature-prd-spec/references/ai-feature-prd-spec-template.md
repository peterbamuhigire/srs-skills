# AI Feature PRD Spec Template

## 1. AI FR Inventory

| AI-FR-ID | Parent FR | Feature | AI Component | Pricing Tier |
|----------|-----------|---------|---------------|--------------|
| AI-FR-001 | FR-014 | AI Summary | LLM (hosted general) | Starter+ |
| AI-FR-002 | FR-022 | AI Composer | LLM + tone prompt | Pro+ |
| AI-FR-003 | FR-031 | AI Analyst | LLM + RAG over warehouse | Business+ |
| AI-FR-004 | FR-041 | AI Agent | LLM + tools | Enterprise |

## 2. Per-FR AI Clauses

### AI-FR-001 AI Summary

| Clause | Value |
|--------|-------|
| Hallucination tolerance | factuality >= 0.92 on golden-200; abstain otherwise |
| Latency budget P95 | <= 1500 ms; timeout 6000 ms |
| $/call ceiling | <= $0.01; per-tenant ceiling $5/day; throttle on breach |
| Abstain criteria | abstain when source thread < 100 chars or > 32k tokens |
| Citation policy | not required (input is the user's own thread) |
| Consent / opt-in | on by default; workspace admin can disable |
| Training-data exclusion | provider configured with no-training endpoint; verified per quarterly audit |

### AI-FR-002 AI Composer

| Clause | Value |
|--------|-------|
| Hallucination tolerance | factuality >= 0.90 on golden-150; tone match >= 0.85 (judge-LLM) |
| Latency budget P95 | <= 2500 ms |
| $/call ceiling | <= $0.03 |
| Abstain criteria | abstain when source thread lacks the answer signal (retrieval confidence < 0.5) |
| Citation policy | every factual claim cites a source span |
| Consent / opt-in | opt-in per user (privacy notice on first use) |
| Training-data exclusion | yes |

### AI-FR-003 AI Analyst

| Clause | Value |
|--------|-------|
| Hallucination tolerance | factuality >= 0.95 on numeric answers; numeric mismatch = hard fail |
| Latency budget P95 | <= 5000 ms (warehouse hop dominates) |
| $/call ceiling | <= $0.20 per question; per-tenant $50/day default, configurable |
| Abstain criteria | abstain when SQL plan empty or semantic-layer term ambiguous |
| Citation policy | every fact cites a row-range + SQL fingerprint |
| Consent / opt-in | workspace-admin opt-in; per-dataset opt-in |
| Training-data exclusion | yes; SQL fingerprints never leave the gateway |

### AI-FR-004 AI Agent

| Clause | Value |
|--------|-------|
| Hallucination tolerance | tool-arg correctness >= 0.98 on golden; abstain otherwise |
| Latency budget P95 | <= 30 s end-to-end; per-step <= 5 s |
| $/call ceiling | <= $1 per agent run; per-tenant $200/day |
| Abstain criteria | abstain when planned action not in approved-actions catalogue |
| Citation policy | every output cites tool calls used |
| Consent / opt-in | feature-flag per workspace; per-action user approval |
| Training-data exclusion | yes |

## 3. Structured Output Requirements

| AI-FR | Output schema | Free-form section | Guard |
|-------|----------------|---------------------|-------|
| AI-FR-001 | `{ summary: string<=600, bullets: string[<=5] }` | summary text | length, banned-terms |
| AI-FR-002 | `{ subject: string, body: string, citations: Citation[] }` | body | tone classifier, PII filter |
| AI-FR-003 | `{ answer: string, sql: string, rows: Row[], citations: Citation[] }` | answer | numeric verifier |
| AI-FR-004 | `ToolCall[]` then `{ outcome, log, citations }` | n/a | only approved-action enum allowed |

## 4. Safety and Content Rules

| Rule | Applies to | Verification |
|------|------------|--------------|
| No medical advice | all | red-team scenario RT-S-MED-* |
| No legal advice | all | RT-S-LEGAL-* |
| No investment advice | all | RT-S-FIN-* |
| No PII generation | all | RT-S-PII-* |
| No protected-class judgement | AI Composer, AI Analyst | RT-S-FAIR-* |
| No execution of unapproved actions | AI Agent | RT-S-AGENT-* |

## 5. Human-in-the-Loop and Contestability

| AI-FR | Decision | HITL | EU AI Act tier | Contest mechanism |
|-------|----------|------|----------------|--------------------|
| AI-FR-001 | summary content | none | limited-risk | regenerate, dismiss |
| AI-FR-002 | draft reply | user sends | limited-risk | edit, regenerate |
| AI-FR-003 | data answer | analyst review on numeric | limited-risk | "show SQL", "show rows", flag |
| AI-FR-004 | agent action | per-action approval; bulk-approve forbidden | high-risk (case-by-case) | reject, rollback |

## 6. Rollout Posture

| AI-FR | Initial cohort | Promotion gate | Rollback trigger |
|-------|----------------|----------------|-------------------|
| AI-FR-001 | internal staff + 3 design partners | golden >= 92% for 7 d | -- |
| AI-FR-002 | internal staff + opt-in beta | red-team pass; hallucination SLO met 14 d | factuality drop > 5 pp |
| AI-FR-003 | 5 enterprise design partners | numeric error rate < 2% 30 d | numeric error spike |
| AI-FR-004 | 2 enterprise pilots | SEV1-clean 60 d; bias eval pass | unauthorised action emitted |

## 7. Eval Acceptance Gates

| AI-FR | Golden set ID | Pass threshold | Adversarial set ID | Pass threshold |
|-------|----------------|----------------|---------------------|----------------|
| AI-FR-001 | EVAL-SUM-200 | 92% | RT-SUM-50 | 90% |
| AI-FR-002 | EVAL-COMP-150 | 90% factuality, 85% tone | RT-COMP-60 | 90% |
| AI-FR-003 | EVAL-ANL-300 | 95% numeric | RT-ANL-80 | 95% |
| AI-FR-004 | EVAL-AGT-100 | 98% tool-arg | RT-AGT-50 | 95% |

## 8. Traceability

| AI-FR | PRD FR | Eval ID | Red-team ID | Model Card | ADR |
|-------|--------|---------|--------------|-------------|-----|
| AI-FR-001 | FR-014 | EVAL-SUM-200 | RT-SUM-50 | MC-SUM-v1 | ADR-AI-002 |
| AI-FR-002 | FR-022 | EVAL-COMP-150 | RT-COMP-60 | MC-COMP-v1 | ADR-AI-003 |
| AI-FR-003 | FR-031 | EVAL-ANL-300 | RT-ANL-80 | MC-ANL-v1 | ADR-AI-004 |
| AI-FR-004 | FR-041 | EVAL-AGT-100 | RT-AGT-50 | MC-AGT-v1 | ADR-AI-005 |
