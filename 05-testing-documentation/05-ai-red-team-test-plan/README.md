## Objective

Produce the AI Red-Team Test Plan: adversarial scenarios + severity matrix + CI smoke + weekly full run + sign-off rules.

## Execution Steps

1. Verify AI Feature PRD Spec, AI Architecture Spec, AI Data Spec, AI Eval Harness Spec exist.
2. Invoke `logic.prompt`.
3. Review with the security lead, AI lead, and DPO. CRITICAL/HIGH findings block GA.

## Standards

- OWASP LLM Top 10
- NIST AI RMF MEASURE-2
- MITRE ATLAS
