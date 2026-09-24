## Objective

Produce the AI Agent Architecture Spec: runtime decomposition, loop and state machine, memory tiers, planner, dispatcher, supervisor (if multi-agent), durability and resumability, kill-switch wiring, and per-tenant isolation.

## Execution Steps

1. Verify `AI_Architecture_Spec.md`, `AI_Agent_Feature_PRD_Spec.md`, `Action_Catalogue_Spec.md`, `Multi_Tenancy_Architecture_Spec.md`, and tech-stack inputs exist.
2. Invoke `logic.prompt`.
3. Review with the architect, AI lead, platform lead, and security lead. Promote ADR seeds via the agent ADR catalogue.

## Standards

- OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications 2026 (verified 2026-09-24 at genai.owasp.org; an "OWASP GenAI LLM Top 10 2026" resource was published 2026-08-03 but its identifiers are `NOT_ASSESSED` - keep LLMxx:2025 IDs until re-mapped)
- NIST AI RMF
- ISO/IEC 42001
- AWS Well-Architected ML/AI Lens
