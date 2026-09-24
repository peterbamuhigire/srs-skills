## Objective

Produce the Multi-Agent Coordination Spec: topology, roles, scratchpad isolation, supervision policy, message-bus contract, and failure-mode handling for any feature where more than one agent participates in a single user task.

## Execution Steps

1. Verify `AI_Agent_Architecture_Spec.md`, `AI_Agent_Feature_PRD_Spec.md`, `Action_Catalogue_Spec.md` exist.
2. Invoke `logic.prompt`.
3. Review with the AI lead, architect, and security lead. Promote topology ADR via the agent ADR catalogue.

## Standards

- OWASP Top 10 for LLM Applications 2026 (published 2026-08-03; LLM01:2026-LLM10:2026 verified 2026-09-24 against the edition PDF at genai.owasp.org/resource/owasp-genai-llm-top-10-2026) and OWASP Top 10 for Agentic Applications 2026. Cite 2026 IDs; add the LLMxx:2025 ID only where an existing control set still uses it (2025-to-2026 map: `05-ai-red-team-test-plan/references/red-team-scenario-library.md`)
- Anthropic agent-engineering patterns
- ISO/IEC 42001
