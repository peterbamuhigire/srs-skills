## Objective

Produce the AI Red-Team Test Plan: adversarial scenarios + severity matrix + CI smoke + weekly full run + sign-off rules.

## Execution Steps

1. Verify AI Feature PRD Spec, AI Architecture Spec, AI Data Spec, AI Eval Harness Spec exist.
2. Invoke `logic.prompt`.
3. Review with the security lead, AI lead, and DPO. CRITICAL/HIGH findings block GA.

## Standards

- OWASP Top 10 for LLM Applications 2026 (published 2026-08-03; LLM01:2026-LLM10:2026 verified 2026-09-24 against the edition PDF at genai.owasp.org/resource/owasp-genai-llm-top-10-2026) and OWASP Top 10 for Agentic Applications 2026. Cite 2026 IDs; add the LLMxx:2025 ID only where an existing control set still uses it (2025-to-2026 map: `05-ai-red-team-test-plan/references/red-team-scenario-library.md`)
- NIST AI RMF MEASURE-2
- MITRE ATLAS
