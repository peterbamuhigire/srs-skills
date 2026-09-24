## Objective

Produce the AI Architecture Specification: AI plane, model gateway, vector store, prompt registry, eval harness, observability bus, and security boundaries for AI features in a multi-tenant SaaS.

## Execution Steps

1. Verify HLD.md, Multi_Tenancy_Architecture_Spec.md, AI_Feature_PRD_Spec.md, AI_Data_And_Knowledge_Base_Spec.md exist.
2. Invoke `logic.prompt`.
3. Review with the architect, AI lead, and security lead. Promote ADR seeds via `09-governance-compliance/05-architecture-decision-records`.

## Standards

- AWS Well-Architected ML/AI Lens
- OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications 2026 (verified 2026-09-24 at genai.owasp.org; an "OWASP GenAI LLM Top 10 2026" resource was published 2026-08-03 but its identifiers are `NOT_ASSESSED` - keep LLMxx:2025 IDs until re-mapped)
- NIST AI RMF
- ISO/IEC 42001
