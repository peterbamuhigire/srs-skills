# Phase 09: Governance & Compliance

## Purpose

Generate governance artifacts that ensure requirements traceability, audit readiness, regulatory compliance, and systematic risk management across the project lifecycle.

## Skills in This Phase

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-traceability-matrix | Traceability_Matrix.md | IEEE 1012-2016 |
| 2 | 02-audit-report | Audit_Report.md | IEEE 1012-2016 |
| 3 | 03-compliance-documentation | Compliance_Docs.md | GDPR/HIPAA/SOC2 |
| 4 | 04-risk-assessment | Risk_Assessment.md | ISO 31000, IEEE 1012 |

## Execution Order

Run 01-traceability-matrix first as it feeds the audit report. Skills 03 and 04 are independent and can run in parallel after 01 and 02 complete.

```
01-traceability-matrix --> 02-audit-report --> [03-compliance-documentation]
                                           --> [04-risk-assessment]
```

## Integration

- **Upstream:** All prior phases (01-08) provide artifacts for traceability and auditing
- **Downstream:** Terminal phase -- outputs feed external audit processes and regulatory submissions

## Quality Gate

All governance artifacts SHALL pass the IEEE 1012 V&V criteria (correctness, completeness, consistency, traceability) before release to external stakeholders.

## AI agent compliance family (new)

The following agent-specific compliance skills extend Phase 09 with SOC 2 / ISO 27001 / HIPAA control packs, policy pack, attestation preparation, evidence pack spec, BAA / DPA language, and the multi-regulator overlap mapping. They are required when the SaaS operates one or more agent features at L1 or higher autonomy and intends to pass SOC 2 Type II, ISO 27001 certification, or HIPAA covered-entity review.

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 20 | 20-ai-agent-soc2-control-pack | AI_Agent_SOC2_Control_Pack.md | AICPA TSP 100 |
| 21 | 21-ai-agent-iso27001-control-pack | AI_Agent_ISO27001_Control_Pack.md | ISO/IEC 27001:2022 |
| 22 | 22-ai-agent-hipaa-control-pack | AI_Agent_HIPAA_Control_Pack.md | 45 CFR §164 |
| 23 | 23-ai-agent-compliance-policy-pack | AI_Agent_Compliance_Policy_Pack.md (7 policies) | SOC2 CC1; ISO A.5.1; HIPAA §164.316 |
| 24 | 24-ai-agent-attestation-preparation-spec | AI_Agent_Attestation_Preparation_Spec.md | AICPA AT-C 205; ISO/IEC 17021 |
| 25 | 25-ai-agent-evidence-pack-spec | AI_Agent_Evidence_Pack_Spec.md | AICPA TSP 100; ISO/IEC 27007 |
| 26 | 26-ai-agent-baa-and-data-processing-language | AI_Agent_BAA_Addendum.md; AI_Agent_DPA_Addendum.md | HIPAA §164.504(e); GDPR Art. 28 |
| 27 | 27-ai-agent-regulator-overlap-mapping | AI_Agent_Regulator_Overlap_Mapping.md | All listed regimes |

Operational counterpart: `06-deployment-operations/20-ai-agent-compliance-runbook` (drill, evidence-collection, control-test, audit-window operating procedure).

## Anti-AI-slop quality gate (new)

Two cross-cutting skills guard every generated artefact against AI slop — low-quality, untestable, hallucination-prone output. They are not phase-sequential; they wrap the whole engine.

| Order | Skill | Role | Output |
|-------|-------|------|--------|
| 28 | 28-anti-ai-slop | MANDATORY pre-ship guardrail on every generated SRS/spec/doc/code artefact | Ship/no-ship gate + V&V fail tags |
| 29 | 29-ai-slop-audit | AUTO-RUNS whenever the user asks to analyse/review/evaluate/audit a spec, requirement, document, or system for AI slop | Graded slop report (A–F) with evidence and fixes |

`28-anti-ai-slop` runs after the IEEE 1012 V&V audit and before any draft reaches the consultant (PRIME "Inspect" step). `29-ai-slop-audit` is the detector and feeds findings back as `[SMART-FAIL]`, `[V&V-FAIL]`, `[TRACE-GAP]`, and `[VERIFIABILITY-FAIL]` tags for remediation. Verified anchors: Merriam-Webster 2025 Word of the Year; Kommers et al. (arXiv 2601.06060); Spracklen et al. (USENIX Security 2025, 19.7% package hallucination); Veracode (45% flawed, XSS 86%, log-injection 88%); GitClear duplication 8.3%→12.3%.

## Cross-engine handoff (compliance × software-dev)

The agent compliance family **owns the artefacts**: policy text, control narratives, evidence pack layout, audit procedures, BAA/DPA language. A parallel software-dev pass **owns the machinery**: automated evidence collectors, hash-chain audit-log implementation, gap detector, integrity verifier, auditor portal. Cross-link via the evidence frequency table at `25-ai-agent-evidence-pack-spec/references/ai-agent-evidence-frequency-table.md`.
