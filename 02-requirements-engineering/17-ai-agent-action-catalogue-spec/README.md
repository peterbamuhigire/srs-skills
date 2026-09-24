## Objective

Produce the Action Catalogue Spec: the enumerated tool surface available to the agent, with schema, side-effect class, reversibility class, tier availability, audit fields, rate-limit class, and kill-switch behaviour.

## Execution Steps

1. Verify `AI_Agent_Feature_PRD_Spec.md`, `AI_Architecture_Spec.md`, and the multi-tenancy spec exist. Pull API specs for any back-end the agent will call.
2. Invoke `logic.prompt`.
3. Review with the platform lead, security lead, and the back-end owner of every called system. Promote per-tool ADRs via the agent ADR catalogue.

## Standards

- OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications 2026 (verified 2026-09-24 at genai.owasp.org; an "OWASP GenAI LLM Top 10 2026" resource was published 2026-08-03 but its identifiers are `NOT_ASSESSED` - keep LLMxx:2025 IDs until re-mapped)
- Anthropic tool-use guide
- NIST AI RMF MEASURE-2
