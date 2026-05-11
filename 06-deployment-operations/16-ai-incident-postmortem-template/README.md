## Objective

Produce the AI Incident Postmortem for a given incident: blameless, RCA-tagged, with per-tenant impact, regulator-impact assessment, and action items by class.

## Execution Steps

1. Verify Severity Matrix, Response Runbook, RCA Taxonomy, Evidence Pack Spec, incident timeline, Hallucination SLO, pricing spec exist; verify the evidence pack for this incident is preserved.
2. Invoke `logic.prompt`.
3. Review with IC, AI lead, SRE on-call lead, DPO, customer success, comms lead.

## Standards

- Google SRE blameless postmortem
- ISO/IEC 42001 Clause 10
- NIST AI RMF MANAGE-4
- EU Reg 2024/1689 Art. 73
- EU Reg 2016/679 Art. 33
