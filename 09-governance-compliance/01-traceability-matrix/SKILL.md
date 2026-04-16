---
name: "Traceability Matrix"
description: "Generate a bidirectional requirements traceability matrix mapping every requirement to its source, design element, test case, and implementation status per IEEE 1012-2016."
metadata:
  use_when: "Use when the task matches traceability matrix skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Traceability Matrix Skill

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
