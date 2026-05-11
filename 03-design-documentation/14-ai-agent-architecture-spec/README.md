## Objective

Produce the AI Agent Architecture Spec: runtime decomposition, loop and state machine, memory tiers, planner, dispatcher, supervisor (if multi-agent), durability and resumability, kill-switch wiring, and per-tenant isolation.

## Execution Steps

1. Verify `AI_Architecture_Spec.md`, `AI_Agent_Feature_PRD_Spec.md`, `Action_Catalogue_Spec.md`, `Multi_Tenancy_Architecture_Spec.md`, and tech-stack inputs exist.
2. Invoke `logic.prompt`.
3. Review with the architect, AI lead, platform lead, and security lead. Promote ADR seeds via the agent ADR catalogue.

## Standards

- OWASP LLM Top 10 (agentic addendum)
- NIST AI RMF
- ISO/IEC 42001
- AWS Well-Architected ML/AI Lens
