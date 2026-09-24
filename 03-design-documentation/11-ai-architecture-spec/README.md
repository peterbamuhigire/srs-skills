## Objective

Produce the AI Architecture Specification: AI plane, model gateway, vector store, prompt registry, eval harness, observability bus, and security boundaries for AI features in a multi-tenant SaaS.

## Execution Steps

1. Verify HLD.md, Multi_Tenancy_Architecture_Spec.md, AI_Feature_PRD_Spec.md, AI_Data_And_Knowledge_Base_Spec.md exist.
2. Invoke `logic.prompt`.
3. Review with the architect, AI lead, and security lead. Promote ADR seeds via `09-governance-compliance/05-architecture-decision-records`.

## Standards

- AWS Well-Architected ML/AI Lens
- OWASP Top 10 for LLM Applications 2026 (published 2026-08-03; LLM01:2026-LLM10:2026 verified 2026-09-24 against the edition PDF at genai.owasp.org/resource/owasp-genai-llm-top-10-2026) and OWASP Top 10 for Agentic Applications 2026. Cite 2026 IDs; add the LLMxx:2025 ID only where an existing control set still uses it (2025-to-2026 map: `05-ai-red-team-test-plan/references/red-team-scenario-library.md`)
- NIST AI RMF
- ISO/IEC 42001
