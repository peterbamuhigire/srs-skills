## Objective

Generate the AI-Feature PRD Spec: every AI-powered FR carries hallucination tolerance, latency budget, cost ceiling, abstain criteria, citation policy, consent, and training-data exclusion.

## Execution Steps

1. Verify PRD.md exists and the AI Feature Strategy Doc names every AI feature in scope.
2. Invoke `logic.prompt`.
3. Review with the product owner, security, and DPO. Every clause must be numeric or rule-form, never aspirational.

## Standards

- ISO/IEC/IEEE 29148:2018 (requirements engineering; supersedes IEEE 830-1998)
- NIST AI RMF
- EU AI Act Art. 13 + Art. 14
- OWASP Top 10 for LLM Applications 2026 (published 2026-08-03; LLM01:2026-LLM10:2026 verified 2026-09-24 against the edition PDF at genai.owasp.org/resource/owasp-genai-llm-top-10-2026) and OWASP Top 10 for Agentic Applications 2026. Cite 2026 IDs; add the LLMxx:2025 ID only where an existing control set still uses it (2025-to-2026 map: `05-ai-red-team-test-plan/references/red-team-scenario-library.md`)
