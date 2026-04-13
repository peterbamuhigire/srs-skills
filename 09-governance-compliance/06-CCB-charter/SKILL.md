---
name: "CCB Charter"
phase: "09-governance-compliance"
description: "Generate a Change Control Board (CCB) Charter governing all changes to baselined project artifacts per PMBOK 6th Ed. Book of Forms and ISO 14764."
standard: "PMBOK 6th Ed. (Book of Forms), ISO 14764 (Software Maintenance)"
metadata:
  use_when: "Use when the task matches skill: ccb charter and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use sibling files in this directory when deeper detail is needed."
---

# Skill: CCB Charter

## Source

PMBOK 6th Edition — Book of Forms; ISO 14764:2006 (Software Engineering — Software Life Cycle Processes — Maintenance), Section 7.2 (Change Management).

## Purpose

Generate a Change Control Board Charter that governs all changes to baselined project artifacts after formal approval. No baselined artifact may be modified without CCB approval. The charter establishes board composition, meeting cadence, decision authority thresholds, and the change request process.

## When to Use This Skill

- At project initiation, when the first baseline is established
- When transitioning from requirements gathering to design (SRS baseline)
- When a project lacks a formal change governance process
- When preparing for an audit or contractual review requiring evidence of change control
- When onboarding a new sponsor or client representative who must participate in CCB

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Input** | vision.md, stakeholders.md |
| **Output** | CCB_Charter.md |
| **Standard** | PMBOK 6th Ed., ISO 14764:2006 |
| **Estimated Time** | 10-20 minutes |

## Core Instructions

1. Read `projects/<ProjectName>/_context/vision.md` for project name, scope, and methodology. If the file is missing, halt and report.
2. Read `projects/<ProjectName>/_context/stakeholders.md` for CCB member names and roles. If the file is missing, generate the charter with `[TBD]` placeholders and flag each with `[CONTEXT-GAP]`.
3. Determine quorum size based on the stakeholder list (default: minimum 3 voting members).
4. Populate the budget threshold for Moderate/Major change types from the project context; if absent, flag `[CONTEXT-GAP: Budget threshold not defined]`.
5. Set meeting cadence based on the project methodology (Agile: weekly; Waterfall: bi-weekly; flag if ambiguous).
6. Generate `CCB_Charter.md` to `projects/<ProjectName>/09-governance-compliance/06-CCB-charter/CCB_Charter.md`.
7. After generating, present the document for human review per the Human Review Gate protocol in CLAUDE.md.

## CCB Charter Template

Generate the following document, substituting project-specific values:

---

```markdown
# Change Control Board Charter

**Document ID:** CCB-CHARTER-[ProjectName]-v[version]
**Project:** [ProjectName]
**Effective Date:** [YYYY-MM-DD]

## 1. Purpose

The Change Control Board (CCB) governs all changes to baselined project artifacts
after formal approval. No baselined artifact may be modified without CCB approval.

## 2. Scope

All changes to:
- Requirements baseline (SRS)
- Architecture baseline (SDD)
- Test baseline (STP)
- Production code baseline

## 3. CCB Composition

| Role | Name | Authority | Required for Quorum? |
|------|------|-----------|---------------------|
| CCB Chair (Project Manager) | | Approve/Reject | Yes |
| Technical Lead | | Recommend | Yes |
| QA Lead | | Recommend | Yes |
| Product Owner / Client Rep | | Approve scope changes | Yes |
| Domain Expert | | Advisory | No |

## 4. Meeting Cadence

- Regular: [Weekly / Bi-weekly] during active development
- Emergency: Within 24 hours for P1 change requests
- Quorum: Minimum [3] voting members required

## 5. Change Request Process

1. Requester submits Change Request form (CR-[ID])
2. CCB Chair triages within [2] business days
3. Technical Lead performs impact analysis
4. CCB reviews at next scheduled meeting (or emergency session)
5. Decision: Approve / Reject / Defer / Approve with conditions
6. If approved: baseline updated, version incremented, stakeholders notified
7. If rejected: requester notified with documented rationale

## 6. Approval Thresholds

| Change Type | Authority |
|-------------|-----------|
| Minor (no scope/schedule/budget impact) | Technical Lead alone |
| Moderate (schedule impact ≤ 5 days OR cost ≤ [budget threshold]) | CCB majority vote |
| Major (scope change OR schedule > 5 days OR cost > threshold) | CCB + Sponsor approval |
| Emergency (P1 system outage) | CCB Chair unilaterally, ratified at next meeting |

## 7. Documentation Requirements

- Every CCB decision recorded in the Change Log with: CR-ID, Decision, Date, Rationale, Approvers
- Approved changes trigger version increment of affected baseline document
- Rejected changes retain the CR with rationale for audit trail

## 8. Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|----------------|
| 1.0 | [YYYY-MM-DD] | | Initial charter |
```

---

## Verification Checklist

- [ ] Project name and Document ID populated
- [ ] All CCB roles identified with named individuals (or `[TBD]` with `[CONTEXT-GAP]` flag)
- [ ] Quorum count is explicit and ≥ 3 for projects with ≥ 4 stakeholders
- [ ] Budget threshold for Moderate/Major boundary is defined (not `[TBD]`)
- [ ] Meeting cadence matches the project methodology (Agile: weekly; Waterfall: bi-weekly)
- [ ] Change Request process has 7 numbered steps
- [ ] All four approval threshold rows are populated
- [ ] Documentation requirements reference the Change Log artifact

## Common Pitfalls

- Creating a CCB Charter after baselines have already been changed informally — go back and retroactively log those changes in the Change Log
- Omitting the budget threshold, which creates an ambiguous boundary between Moderate and Major changes
- Setting quorum to 1 or 2 — this undermines the governance control; enforce a minimum of 3
- Failing to include the Product Owner / Client Rep, who must approve scope changes per PMBOK 6th Ed.
- Confusing the CCB Charter (the governing document) with the Change Log (the operational record)

## Integration

- **Upstream:** Consumes project context from `_context/vision.md` and `_context/stakeholders.md`.
- **Downstream:** The CCB Charter governs all artifact changes across all phases. It must be referenced in the SRS, SDD, and STP as the change authority. The Change Log produced by CCB decisions feeds into `02-audit-report`.

## Standards Compliance

| Standard | Governs |
|----------|---------|
| PMBOK 6th Ed. (Book of Forms) | CCB composition, change request process, approval thresholds |
| ISO 14764:2006 §7.2 | Change management process for software maintenance baselines |
| IEEE 828-2012 | Software Configuration Management Plan (complements CCB governance) |

## Resources

- PMBOK 6th Edition: Project Management Body of Knowledge, Book of Forms
- ISO 14764:2006: Software Engineering — Software Life Cycle Processes — Maintenance
- IEEE 828-2012: Standard for Software Configuration Management Plans
- CLAUDE.md: Human Review Gate protocol (mandatory post-generation step)
