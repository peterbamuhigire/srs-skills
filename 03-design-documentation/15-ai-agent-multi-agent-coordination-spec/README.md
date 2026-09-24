## Objective

Produce the Multi-Agent Coordination Spec: topology, roles, scratchpad isolation, supervision policy, message-bus contract, and failure-mode handling for any feature where more than one agent participates in a single user task.

## Execution Steps

1. Verify `AI_Agent_Architecture_Spec.md`, `AI_Agent_Feature_PRD_Spec.md`, `Action_Catalogue_Spec.md` exist.
2. Invoke `logic.prompt`.
3. Review with the AI lead, architect, and security lead. Promote topology ADR via the agent ADR catalogue.

## Standards

- OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications 2026 (verified 2026-09-24 at genai.owasp.org; an "OWASP GenAI LLM Top 10 2026" resource was published 2026-08-03 but its identifiers are `NOT_ASSESSED` - keep LLMxx:2025 IDs until re-mapped)
- Anthropic agent-engineering patterns
- ISO/IEC 42001
