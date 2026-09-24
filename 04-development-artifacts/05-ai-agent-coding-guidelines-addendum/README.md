## Objective

Produce the AI Agent Coding Guidelines Addendum: schema discipline, irreversibility annotations, blast-radius caps, deterministic state, idempotency keys, error/timeout policy, and the test contract for agent-runtime code.

## Execution Steps

1. Verify `Coding_Guidelines.md`, `AI_Agent_Architecture_Spec.md`, `Action_Catalogue_Spec.md` exist.
2. Invoke `logic.prompt`.
3. Review with the AI lead, platform lead, and engineering leads of the back-end systems whose tools are wrapped.

## Standards

- OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications 2026 (verified 2026-09-24 at genai.owasp.org; an "OWASP GenAI LLM Top 10 2026" resource was published 2026-08-03 but its identifiers are `NOT_ASSESSED` - keep LLMxx:2025 IDs until re-mapped)
- Anthropic agent-engineering patterns
- IEEE 1016-2009 §5
