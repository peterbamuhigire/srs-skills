## Objective

Produce the AI Red-Team Test Plan: adversarial scenarios + severity matrix + CI smoke + weekly full run + sign-off rules.

## Execution Steps

1. Verify AI Feature PRD Spec, AI Architecture Spec, AI Data Spec, AI Eval Harness Spec exist.
2. Invoke `logic.prompt`.
3. Review with the security lead, AI lead, and DPO. CRITICAL/HIGH findings block GA.

## Standards

- OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications 2026 (verified 2026-09-24 at genai.owasp.org; an "OWASP GenAI LLM Top 10 2026" resource was published 2026-08-03 but its identifiers are `NOT_ASSESSED` - keep LLMxx:2025 IDs until re-mapped)
- NIST AI RMF MEASURE-2
- MITRE ATLAS
