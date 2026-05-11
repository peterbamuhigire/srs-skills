## Objective

Produce the Action Catalogue Spec: the enumerated tool surface available to the agent, with schema, side-effect class, reversibility class, tier availability, audit fields, rate-limit class, and kill-switch behaviour.

## Execution Steps

1. Verify `AI_Agent_Feature_PRD_Spec.md`, `AI_Architecture_Spec.md`, and the multi-tenancy spec exist. Pull API specs for any back-end the agent will call.
2. Invoke `logic.prompt`.
3. Review with the platform lead, security lead, and the back-end owner of every called system. Promote per-tool ADRs via the agent ADR catalogue.

## Standards

- OWASP LLM Top 10 (agentic addendum)
- Anthropic tool-use guide
- NIST AI RMF MEASURE-2
