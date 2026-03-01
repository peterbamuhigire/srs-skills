---
name: Audit Report
description: Generate a verification and validation audit report assessing completeness, consistency, correctness, and traceability of all project documentation per IEEE 1012-2016.
---

# Audit Report Skill

## Overview

This skill generates a formal Verification and Validation (V&V) audit report that systematically evaluates all project documentation against IEEE 1012-2016 criteria. The report assesses completeness, consistency, correctness, and traceability, producing categorized findings with severity levels and actionable remediation recommendations. The audit concludes with a formal recommendation of Pass, Conditional Pass, or Fail.

## When to Use This Skill

- After the traceability matrix has been generated and reviewed
- When preparing for external regulatory or client audits
- When a project milestone requires formal V&V sign-off
- When stakeholders request evidence of documentation quality
- When transitioning between major project phases
- When anomalies have been reported and require systematic investigation

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Input** | Traceability_Matrix.md, SRS_Draft.md, quality_standards.md |
| **Output** | Audit_Report.md |
| **Standard** | IEEE 1012-2016 |
| **Estimated Time** | 20-40 minutes |

## Input Files

| File | Purpose | Required? |
|------|---------|-----------|
| `../output/Traceability_Matrix.md` | Traceability data and coverage metrics for audit assessment | Yes |
| `../output/SRS_Draft.md` | Primary document under audit for correctness and completeness | Yes |
| `../project_context/quality_standards.md` | Quality benchmarks and acceptance criteria for compliance assessment | No |
| `../output/HLD.md` | Design documentation for consistency cross-check | No |
| `../output/LLD.md` | Detailed design documentation for consistency cross-check | No |

## Output Files

| File | Description |
|------|-------------|
| `../output/Audit_Report.md` | Complete V&V audit report with findings and recommendations |

## Core Instructions

1. The skill SHALL read `../output/Traceability_Matrix.md` and `../output/SRS_Draft.md`. If either file is missing, halt execution and report the error.

2. The skill SHALL define the audit scope, listing every document reviewed, the standards applied, and the methodology used (IEEE 1012-2016 V&V framework).

3. The skill SHALL assess **Correctness** by verifying that each requirement accurately reflects stakeholder intent as documented in upstream artifacts. Flag deviations as findings.

4. The skill SHALL assess **Completeness** by checking that every business goal has at least one corresponding requirement, every requirement has a test case, and no sections contain TBD or placeholder content.

5. The skill SHALL assess **Consistency** by cross-referencing terminology, data types, and logical structures across all reviewed documents. Flag contradictions or ambiguities.

6. The skill SHALL assess **Traceability** by analyzing the Traceability Matrix for coverage gaps, orphan items, and broken links.

7. The skill SHALL categorize every finding by severity:
   - **Critical:** Renders the system unsafe, non-compliant, or fundamentally broken
   - **Major:** Significant gap that must be resolved before release
   - **Minor:** Cosmetic or low-impact issue that should be addressed
   - **Observation:** Improvement suggestion with no compliance impact

8. The skill SHALL generate a Remediation Plan with specific corrective actions, responsible parties (where identifiable), and priority ordering.

9. The skill SHALL produce a Compliance Assessment Matrix mapping each IEEE 1012-2016 clause to its compliance status (Compliant/Partially Compliant/Non-Compliant).

10. The skill SHALL conclude with an Audit Summary and formal Recommendation:
    - **Pass:** All critical and major findings resolved; documentation meets standards
    - **Conditional Pass:** No critical findings; major findings have approved remediation plans
    - **Fail:** Critical findings present or excessive major findings without remediation

11. The skill SHALL tag any finding requiring immediate action with `[V&V-FAIL]` and reference the originating document and section.

## Output Format Specification

The generated `Audit_Report.md` SHALL contain the following sections:

```
# Verification & Validation Audit Report
## 1. Document Information
## 2. Audit Scope & Methodology
## 3. Documents Reviewed
## 4. Compliance Assessment Matrix
## 5. Findings
### 5.1 Critical Findings
### 5.2 Major Findings
### 5.3 Minor Findings
### 5.4 Observations
## 6. Correctness Analysis
## 7. Completeness Analysis
## 8. Consistency Analysis
## 9. Traceability Analysis
## 10. Remediation Plan
## 11. Audit Summary & Recommendation
## 12. Revision History
```

## Common Pitfalls

- Producing findings without actionable remediation steps
- Conflating severity levels (e.g., marking cosmetic issues as Critical)
- Omitting the formal Pass/Conditional Pass/Fail recommendation
- Auditing only the SRS without cross-referencing design and test artifacts
- Using subjective language ("seems incomplete") instead of specific evidence
- Failing to reference the exact document section where a finding originates

## Verification Checklist

1. All four V&V dimensions (correctness, completeness, consistency, traceability) are assessed.
2. Every finding has a severity level, description, affected artifact, and remediation action.
3. The Compliance Assessment Matrix covers all applicable IEEE 1012-2016 clauses.
4. The audit concludes with a formal Pass/Conditional Pass/Fail recommendation.
5. `[V&V-FAIL]` tags are applied to all findings requiring immediate action.
6. The Documents Reviewed section lists every artifact examined during the audit.
7. Findings reference specific document sections, not just document names.
8. The Remediation Plan prioritizes corrective actions by severity.

## Integration

- **Upstream:** Requires the traceability matrix from 01-traceability-matrix and all documentation artifacts from prior phases.
- **Downstream:** Feeds 03-compliance-documentation and 04-risk-assessment. Audit findings may trigger re-execution of upstream skills.

## Standards Compliance

| Standard | Governs |
|----------|---------|
| IEEE 1012-2016 | V&V audit methodology, finding classification, and compliance assessment |
| IEEE 830-1998 | SRS quality criteria (correct, unambiguous, complete, consistent) |

## Resources

- IEEE 1012-2016: Standard for System, Software, and Hardware Verification and Validation
- IEEE 830-1998: Recommended Practice for Software Requirements Specifications
- CLAUDE.md: V&V Standard Operating Procedure and Failure Protocols
