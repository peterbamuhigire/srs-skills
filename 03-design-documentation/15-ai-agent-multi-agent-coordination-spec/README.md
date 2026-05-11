## Objective

Produce the Multi-Agent Coordination Spec: topology, roles, scratchpad isolation, supervision policy, message-bus contract, and failure-mode handling for any feature where more than one agent participates in a single user task.

## Execution Steps

1. Verify `AI_Agent_Architecture_Spec.md`, `AI_Agent_Feature_PRD_Spec.md`, `Action_Catalogue_Spec.md` exist.
2. Invoke `logic.prompt`.
3. Review with the AI lead, architect, and security lead. Promote topology ADR via the agent ADR catalogue.

## Standards

- OWASP LLM Top 10 (agentic addendum)
- Anthropic agent-engineering patterns
- ISO/IEC 42001
