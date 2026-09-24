## Objective

Produce the Action Catalogue Spec: the enumerated tool surface available to the agent, with schema, side-effect class, reversibility class, tier availability, audit fields, rate-limit class, and kill-switch behaviour.

## Execution Steps

1. Verify `AI_Agent_Feature_PRD_Spec.md`, `AI_Architecture_Spec.md`, and the multi-tenancy spec exist. Pull API specs for any back-end the agent will call.
2. Invoke `logic.prompt`.
3. Review with the platform lead, security lead, and the back-end owner of every called system. Promote per-tool ADRs via the agent ADR catalogue.

## Standards

- OWASP Top 10 for LLM Applications 2026 (published 2026-08-03; LLM01:2026-LLM10:2026 verified 2026-09-24 against the edition PDF at genai.owasp.org/resource/owasp-genai-llm-top-10-2026) and OWASP Top 10 for Agentic Applications 2026. Cite 2026 IDs; add the LLMxx:2025 ID only where an existing control set still uses it (2025-to-2026 map: `05-ai-red-team-test-plan/references/red-team-scenario-library.md`)
- Anthropic tool-use guide
- NIST AI RMF MEASURE-2
