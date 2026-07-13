---
name: 02-audit-report
description: Use when independently assessing controls or delivery evidence and issuing read-only findings, severity, scope limits, and corrective actions. Use risk-assessment for prospective risk analysis and compliance-documentation to author control artefacts.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Audit Report Skill

<!-- dual-compat-start -->

## Use When

- Use when independently assessing controls or delivery evidence and issuing read-only findings, severity, scope limits, and corrective actions. Use risk-assessment for prospective risk analysis and compliance-documentation to author control artefacts.

## Do Not Use When

- Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Audit scope, criteria, period, control register, evidence index, prior findings, sampling basis, and responsible owners | Audit sponsor and independent evidence custodians | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Execute only non-mutating validation when authorised; editing remediation, publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Required evidence is missing or inaccessible | Mark the check not assessed, state impact, and stop any pass decision | False assurance from an incomplete review |
| Evidence supports the stated criterion | Record the finding and traceable rationale without mutating sources | Unrepeatable review conclusions |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Audit Report | Accountable reviewer, control owner, auditor, or release authority | Every finding cites criterion and evidence, distinguishes not-assessed checks, states severity rationale, and preserves reviewer independence. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Audit Report evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Audit Report from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if required evidence is missing or inaccessible, mark the check not assessed, state impact, and stop any pass decision. Record the evidence and result in the validation record; this avoids false assurance from an incomplete review.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

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
| `projects/<ProjectName>/<phase>/<document>/Traceability_Matrix.md` | Traceability data and coverage metrics for audit assessment | Yes |
| `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` | Primary document under audit for correctness and completeness | Yes |
| `projects/<ProjectName>/_context/quality_standards.md` | Quality benchmarks and acceptance criteria for compliance assessment | No |
| `projects/<ProjectName>/<phase>/<document>/HLD.md` | Design documentation for consistency cross-check | No |
| `projects/<ProjectName>/<phase>/<document>/LLD.md` | Detailed design documentation for consistency cross-check | No |

## Output Files

| File | Description |
|------|-------------|
| `projects/<ProjectName>/<phase>/<document>/Audit_Report.md` | Complete V&V audit report with findings and recommendations |

## Core Instructions

1. The skill SHALL read `projects/<ProjectName>/<phase>/<document>/Traceability_Matrix.md` and `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`. If either file is missing, halt execution and report the error.

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
