## Objective

Produce the AI Agent Red-Team Test Plan: agent-specific adversarial categories, scenario catalogue, severity matrix, CI smoke / weekly cadence, sign-off rules.

## Execution Steps

1. Verify `AI_Agent_Feature_PRD_Spec.md`, `Action_Catalogue_Spec.md`, `AI_Agent_Architecture_Spec.md`, `AI_Red_Team_Test_Plan.md`, and the agent threat model exist.
2. Invoke `logic.prompt`.
3. Review with the security lead, AI lead, and the back-end owner of every called system.

## Standards

- OWASP Top 10 for LLM Applications 2026 (published 2026-08-03; LLM01:2026-LLM10:2026 verified 2026-09-24 against the edition PDF at genai.owasp.org/resource/owasp-genai-llm-top-10-2026) and OWASP Top 10 for Agentic Applications 2026. Cite 2026 IDs; add the LLMxx:2025 ID only where an existing control set still uses it (2025-to-2026 map: `05-ai-red-team-test-plan/references/red-team-scenario-library.md`)
- NIST AI RMF MEASURE-2
- ISO/IEC 42001
- MITRE ATLAS
