## Objective

Produce the AI Agent Coding Guidelines Addendum: schema discipline, irreversibility annotations, blast-radius caps, deterministic state, idempotency keys, error/timeout policy, and the test contract for agent-runtime code.

## Execution Steps

1. Verify `Coding_Guidelines.md`, `AI_Agent_Architecture_Spec.md`, `Action_Catalogue_Spec.md` exist.
2. Invoke `logic.prompt`.
3. Review with the AI lead, platform lead, and engineering leads of the back-end systems whose tools are wrapped.

## Standards

- OWASP Top 10 for LLM Applications 2026 (published 2026-08-03; LLM01:2026-LLM10:2026 verified 2026-09-24 against the edition PDF at genai.owasp.org/resource/owasp-genai-llm-top-10-2026) and OWASP Top 10 for Agentic Applications 2026. Cite 2026 IDs; add the LLMxx:2025 ID only where an existing control set still uses it (2025-to-2026 map: `05-ai-red-team-test-plan/references/red-team-scenario-library.md`)
- Anthropic agent-engineering patterns
- IEEE 1016-2009 §5
