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
- OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications 2026 (verified 2026-09-24 at genai.owasp.org; an "OWASP GenAI LLM Top 10 2026" resource was published 2026-08-03 but its identifiers are `NOT_ASSESSED` - keep LLMxx:2025 IDs until re-mapped)
