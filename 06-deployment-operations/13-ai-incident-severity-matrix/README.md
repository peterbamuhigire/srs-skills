## Objective

Produce the AI Incident Severity Matrix: three-dimensional severity (sev x tenant scope x autonomy), per-AI-failure-class thresholds, SLA service-credit mapping, EU AI Act Art. 73 mapping.

## Execution Steps

1. Verify AI PRD, Hallucination SLO Doc, Cost Runbook, Rollout Runbook, Tenancy Spec, AI Act doc exist.
2. Invoke `logic.prompt`.
3. Review with AI lead, SRE on-call lead, customer success lead, DPO, and legal for the Art. 73 mapping.

## Standards

- NIST AI RMF MANAGE-2
- EU Reg 2024/1689 Art. 73
- ISO/IEC 42001 Clause 8.3
- Google SRE severity classification
