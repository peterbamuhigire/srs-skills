# Change Control Process Reference

**Purpose:** Define the standard change request template, approval workflow, and Change Control Board (CCB) roles for requirements change management.

**Standards:** IEEE 29148-2018 Sec 6.7, Wiegers Practices 15-17

---

## Change Request Template

Every change to a baselined requirement shall be submitted through a formal Change Request (CR). The following fields are mandatory.

### Mandatory Fields

| Field | Format | Description |
|-------|--------|-------------|
| CR-ID | CR-[NNN] | Unique sequential identifier assigned at submission |
| Requester | [Name, Role] | The individual initiating the change |
| Date Submitted | YYYY-MM-DD | Date the CR was formally filed |
| Affected Requirements | [REQ-xxx, REQ-yyy, ...] | List of all requirement IDs impacted by this change |
| Change Type | Add / Modify / Delete | Nature of the change |
| Description | Free text | Clear, specific description of what the change entails |
| Rationale | Free text | Business or technical justification for the change |
| Priority | Critical / High / Medium / Low | Urgency classification |
| Disposition | Pending / Approved / Rejected / Deferred / Merged | Current status of the CR |

### Priority Definitions

| Priority | Definition | Response SLA |
|----------|-----------|-------------|
| Critical | Blocks project progress or addresses safety/compliance issue | CCB review within 2 business days |
| High | Significant impact on scope, schedule, or quality | CCB review within 5 business days |
| Medium | Moderate impact, can wait for next scheduled CCB meeting | CCB review within 10 business days |
| Low | Minor improvement, no urgency | CCB review within 20 business days |

---

## Impact Analysis Template

Every CR with a disposition of Pending shall undergo impact analysis before CCB review. The analyst shall address all six dimensions.

### 1. Scope Impact

- Which requirements are directly affected?
- Which requirements are indirectly affected through dependencies?
- Does this change alter the project scope boundary?
- How many artifacts require modification?

### 2. Schedule Impact

- Estimated effort to implement the change (person-hours).
- Effect on current milestone dates.
- Does this change introduce new dependencies that affect the critical path?
- Sprint impact (Agile): which sprint(s) are affected?

### 3. Cost Impact

- Additional resource costs (development, testing, infrastructure).
- Budget impact: within contingency or requires budget increase?
- Opportunity cost of implementing this change versus other backlog items.

### 4. Risk Impact

- New risks introduced by the change.
- Existing risks modified or mitigated by the change.
- Risk to existing functionality (regression potential).
- Compliance or regulatory risk implications.

### 5. Dependency Impact

- Upstream requirements that feed into the affected requirements.
- Downstream requirements that depend on the affected requirements.
- External system interfaces affected.
- Third-party or vendor dependencies triggered.

### 6. Test Impact

- Test cases requiring creation for new requirements.
- Test cases requiring modification for changed requirements.
- Test cases requiring retirement for deleted requirements.
- Regression test scope expansion.

---

## Approval Workflow

The change control workflow has seven sequential steps. No step shall be skipped.

### Step 1: Submission

The requester fills out the CR template with all mandatory fields and submits it to the Requirements Manager. Incomplete submissions shall be returned to the requester within 1 business day.

### Step 2: Triage

The Requirements Manager:
- Assigns the CR-ID.
- Validates completeness of mandatory fields.
- Assigns initial priority.
- Routes the CR to the appropriate analyst for impact analysis.
- Logs the CR in the change request register.

### Step 3: Impact Analysis

The assigned analyst completes the six-dimension impact analysis within the SLA defined by the CR priority. The analyst shall:
- Consult with the Technical Lead for feasibility assessment.
- Consult with the QA Lead for test impact assessment.
- Document findings in the CR record.

### Step 4: CCB Review

The CCB reviews the CR with the completed impact analysis. The review shall include:
- Presentation of the change and its rationale.
- Review of the impact analysis.
- Stakeholder input (the Product Owner represents business interests).
- Discussion of alternatives.

### Step 5: Decision

The CCB records one of four dispositions:

| Disposition | Meaning | Next Action |
|-------------|---------|-------------|
| Approved | Change is accepted and authorized | Proceed to implementation |
| Rejected | Change is denied with documented rationale | CR is closed |
| Deferred | Change is valid but not for this release | CR is placed in backlog |
| Merged | Change is combined with another related CR | Merged CR proceeds |

The CCB Chair records the decision, rationale, and any conditions in the CR record. All CCB members shall sign off on the decision.

### Step 6: Implementation

For approved CRs:
- The Requirements Manager updates the affected requirements in the baseline.
- The baseline version is incremented per the versioning scheme.
- All trace links are updated in the traceability matrix.
- The version history log is updated.
- Affected stakeholders are notified.

### Step 7: Verification

After implementation:
- The QA Lead verifies that the change has been correctly incorporated.
- Test cases are executed to confirm the change meets acceptance criteria.
- The Requirements Manager confirms baseline integrity.
- The CR status is updated to "Closed."

---

## Change Control Board (CCB)

### Composition

| Role | Responsibility | Authority |
|------|---------------|-----------|
| CCB Chair | Convenes meetings, manages agenda, records decisions, ensures process compliance | Casting vote in case of tie |
| Product Owner | Represents business value, stakeholder priorities, and market requirements | Approve/reject based on business impact |
| Technical Lead | Assesses technical feasibility, architecture impact, and implementation complexity | Advise on technical viability |
| QA Lead | Evaluates test impact, verification requirements, and regression risk | Advise on quality implications |
| Requirements Manager | Maintains baseline integrity, traceability, and version control | Execute approved changes |

### Meeting Cadence

- **Scheduled meetings:** Bi-weekly (or per sprint boundary in Agile).
- **Emergency meetings:** Within the SLA for Critical-priority CRs.
- **Quorum:** At least 3 of 5 CCB members must be present, including the CCB Chair and Product Owner.

### Decision Rules

- Decisions require simple majority vote.
- The CCB Chair holds a casting vote in case of a tie.
- Any CCB member may request a 48-hour delay for additional analysis.
- Rejected CRs may be resubmitted with new evidence or modified scope.

---

## Change Request Register

Maintain a master register of all CRs with the following columns:

| CR-ID | Date | Requester | Type | Priority | Affected Reqs | Disposition | Decision Date | Implemented |
|-------|------|-----------|------|----------|---------------|-------------|---------------|-------------|
| CR-001 | YYYY-MM-DD | [Name] | Modify | High | REQ-005, REQ-012 | Approved | YYYY-MM-DD | Yes |

---

## References

- **IEEE Std 29148-2018** Section 6.7: Requirements management and change control.
- **Wiegers Practice 15:** Requirements change management.
- **Wiegers Practice 16:** Change control boards and approval workflows.
- **Wiegers Practice 17:** Requirements status tracking.
- **IEEE Std 828-2012:** Configuration management in systems and software engineering.

---
**Last Updated:** 2026-03-07
