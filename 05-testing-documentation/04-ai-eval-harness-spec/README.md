## Objective

Produce the AI Eval Harness Spec: the production-grade evaluation system that gates every AI feature in CI and runs scheduled regressions.

## Execution Steps

1. Verify the AI Feature PRD Spec, AI Architecture Spec, Prompt Spec, and AI Data Spec exist.
2. Invoke `logic.prompt`.
3. Review with the AI lead, QA lead, and the security lead (for the safety metric).

## Standards

- OpenAI Evals
- promptfoo / Anthropic eval guidance
- NIST AI RMF MEASURE
- ISO/IEC 42001
