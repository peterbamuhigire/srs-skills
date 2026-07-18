---
name: 01-traceability-matrix
description: Use when mapping requirements to designs, tests, evidence, releases, and approvals so gaps and orphan artefacts are visible. Use baseline-delta for version-to-version changes and evidence-pack-builder to package proof.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Traceability Matrix Skill

<!-- dual-compat-start -->

## Use When

- Use when mapping requirements to designs, tests, evidence, releases, and approvals so gaps and orphan artefacts are visible. Use baseline-delta for version-to-version changes and evidence-pack-builder to package proof.

## Do Not Use When

- Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Approved requirements baseline; design and interface identifiers; test cases and results; risk and control records; release and approval evidence | Requirements, architecture, QA, governance, and release owners | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
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
| Traceability Matrix | Accountable reviewer, control owner, auditor, or release authority | Every in-scope requirement has forward and backward links or an explicit gap; duplicates and orphan evidence are visible. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Traceability Matrix evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Traceability Matrix from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

This skill generates a Requirements Traceability Matrix (RTM) that establishes bidirectional links between every requirement and its originating business goal, design artifact, test case, and implementation status. The RTM serves as the foundational governance artifact that enables audit readiness and ensures no requirement is orphaned or untested. All traceability links SHALL conform to IEEE 1012-2016 verification and validation requirements.

## When to Use This Skill

- When preparing for a formal V&V audit or external review
- When the SRS draft has stabilized and design/test artifacts exist
- When stakeholders require evidence that all business goals have corresponding requirements
- When detecting orphan requirements (no tests) or orphan tests (no requirements)
- When transitioning from development to acceptance testing
- When regulatory or contractual obligations mandate traceability documentation

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Input** | SRS_Draft.md, vision.md, HLD.md, LLD.md, user_stories.md |
| **Output** | Traceability_Matrix.md |
| **Standard** | IEEE 1012-2016 |
| **Estimated Time** | 15-30 minutes |

## Input Files

| File | Purpose | Required? |
|------|---------|-----------|
| `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` | Source of all functional and non-functional requirements | Yes |
| `projects/<ProjectName>/_context/vision.md` | Business goals and stakeholder needs for backward traceability | Yes |
| `projects/<ProjectName>/<phase>/<document>/HLD.md` | High-level design elements for design-to-requirement mapping | No |
| `projects/<ProjectName>/<phase>/<document>/LLD.md` | Low-level design elements for detailed traceability | No |
| `projects/<ProjectName>/<phase>/<document>/user_stories.md` | User stories for requirement-to-story mapping | No |

## Output Files

| File | Description |
|------|-------------|
| `projects/<ProjectName>/<phase>/<document>/Traceability_Matrix.md` | Complete bidirectional traceability matrix with gap analysis |

## Core Instructions

1. The skill SHALL read `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` and extract every requirement with its unique identifier (e.g., FR-001, NFR-001). If the file is missing, halt execution and report the error.

2. The skill SHALL read `projects/<ProjectName>/_context/vision.md` and extract every business goal and stakeholder need, assigning identifiers if none exist (e.g., BG-001, SN-001).

3. The skill SHALL read optional design artifacts (`HLD.md`, `LLD.md`) and extract design element identifiers for forward traceability mapping.

4. The skill SHALL read optional test artifacts and extract test case identifiers for requirement-to-test mapping.

5. The skill SHALL construct a Forward Traceability Table mapping each requirement to its downstream design element, test case, and implementation status.

6. The skill SHALL construct a Backward Traceability Table mapping each design element and test case back to its originating requirement and business goal.

7. The skill SHALL perform Orphan Detection, identifying:
   - Requirements with no linked test case
   - Requirements with no linked design element
   - Test cases with no linked requirement
   - Design elements with no linked requirement

8. The skill SHALL calculate Coverage Metrics:
   - $CoveragePercent = \frac{LinkedRequirements}{TotalRequirements} \times 100$
   - Report separate coverage for test, design, and source linkages.

9. The skill SHALL generate a Gap Analysis section listing every traceability gap with its severity (Critical/Major/Minor) and recommended remediation.

10. The skill SHALL tag any requirement failing traceability with `[V&V-FAIL]` and append the specific missing link.

## RTM Table Template

The Requirements Traceability Matrix table SHALL use the following column structure:

```markdown
| Req ID | Requirement Summary | Source | Priority | Test Case ID(s) | Verification Method | Status | Regulatory Reference |
|--------|--------------------|----|----------|-----------------|--------------------|----|---------------------|
| FR-001 | | | | TC-001 | Test | Pass | [Standard clause or "N/A"] |
```

**Regulatory Reference column guidance:** The Regulatory Reference column cites the specific standard clause that mandates this requirement (e.g., `ISO 27001:2022 §A.8.2`, `GDPR Art. 17`, `PCI DSS Req. 6.4`). Enter `N/A` for requirements not driven by regulation. This column enables compliance auditors to trace from standard clause to implemented feature.

## Output Format Specification

The generated `Traceability_Matrix.md` SHALL contain the following sections:

```
# Requirements Traceability Matrix
## 1. Document Information
## 2. Traceability Matrix Table
## 3. Coverage Summary
## 4. Forward Traceability (Requirements to Implementation)
## 5. Backward Traceability (Implementation to Requirements)
## 6. Gap Analysis
## 7. Orphan Detection Report
## 8. Traceability Metrics
## 9. Remediation Recommendations
## 10. Revision History
```

## Final Step: Write `manifest.md`

After generating all section files, create (or overwrite) `manifest.md` in this document's directory listing the section files in the correct assembly order:

```markdown
# Document Manifest — Traceability Matrix
# Generated by traceability-matrix. Edit to reorder or exclude sections before building.
01-document-information.md
02-traceability-table.md
03-coverage-summary.md
04-forward-traceability.md
05-backward-traceability.md
06-gap-analysis.md
07-orphan-detection.md
08-metrics.md
09-remediation.md
10-revision-history.md
```

This ensures `scripts/build-doc.sh` assembles sections in the intended order rather than alphabetical fallback.

## Common Pitfalls

- Generating a matrix without unique identifiers on every requirement, making links ambiguous
- Omitting backward traceability and only mapping requirements forward
- Failing to detect orphan test cases that have no parent requirement
- Using inconsistent requirement ID formats across the SRS and the matrix
- Ignoring non-functional requirements in the traceability mapping
- Counting partial links as complete coverage, inflating metrics

## Verification Checklist

1. Every requirement in the SRS has a corresponding row in the matrix.
2. Every business goal in vision.md has at least one linked requirement.
3. Orphan detection has been performed for requirements, tests, and design elements.
4. Coverage metrics are computed and reported with correct denominators.
5. All traceability gaps are classified by severity.
6. `[V&V-FAIL]` tags are applied to every requirement with a missing critical link.
7. The matrix uses consistent identifier formats throughout.
8. Forward and backward traceability tables are both present.
9. Every compliance-driven requirement has a Regulatory Reference entry.

## Integration

- **Upstream:** Consumes artifacts from Phase 02 (Requirements), Phase 03 (Design), Phase 05 (Testing), and all preceding phases.
- **Downstream:** Feeds directly into 02-audit-report. The traceability matrix is a prerequisite for audit execution.

## Standards Compliance

| Standard | Governs |
|----------|---------|
| IEEE 1012-2016 | V&V traceability requirements and bidirectional link mandates |
| IEEE 830-1998 | Requirement identifier structure and SRS section mapping |

## Resources

- IEEE 1012-2016: Standard for System, Software, and Hardware Verification and Validation
- IEEE 830-1998: Recommended Practice for Software Requirements Specifications
- CLAUDE.md: Project-level V&V Standard Operating Procedure
