# Business Requirements Document Template

## Purpose

This template provides the complete structure for a Business Requirements Document (BRD) with section descriptions, formatting guidelines, and examples. Use this template during BRD generation to ensure consistent structure and completeness.

## Reference Standard

- IEEE 29148-2018 Section 6.4: Business requirements specification
- Business Requirements Gathering Ch.2-4

## Template Structure

```markdown
# Business Requirements Document: [Project Name]

**Version**: 1.0
**Date**: [Current Date]
**Author(s)**: [Names or AUTHOR-TBD]
**Status**: Draft
**Classification**: [Internal / Confidential / Public]

## Approval and Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor | [Name or SIGNATORY-TBD] | | |
| Business Owner | [Name or SIGNATORY-TBD] | | |
| Technical Lead | [Name or SIGNATORY-TBD] | | |

---

## 1. Executive Summary

[2-3 paragraphs covering: the business problem, the proposed solution at
a high level, expected business value, and key stakeholder groups. Use
active voice. No implementation details. No marketing language.]

**Example:**
> The organization currently processes customer orders through a manual
> workflow involving three disconnected spreadsheets and email-based
> approvals. This process results in an average order processing time of
> 4.2 business days and a 12% error rate in order fulfillment.
>
> This project proposes an integrated order management system that
> automates the end-to-end order lifecycle from submission through
> fulfillment. The system shall reduce order processing time to under
> 1 business day and reduce fulfillment errors to below 2%.
>
> The project affects four stakeholder groups: sales representatives
> (order entry), warehouse staff (fulfillment), finance (invoicing),
> and customers (order tracking).

---

## 2. Business Objectives

[For each business goal, produce a formal objective with measurable
success criteria.]

### BO-001: [Objective Title]

- **Description**: [What the business seeks to achieve]
- **Alignment**: [Strategic goal this supports]
- **Success Metric**: [Quantitative measure]
- **Target Value**: [Specific threshold]
- **Timeline**: [Target date or milestone]
- **Source**: [Stakeholder ID or context reference]

**Example:**

### BO-001: Reduce Order Processing Time

- **Description**: Decrease the average time from order submission to
  fulfillment confirmation.
- **Alignment**: Strategic Goal 2 -- Operational Efficiency
- **Success Metric**: Average order processing time (business days)
- **Target Value**: Less than 1 business day (from current 4.2 days)
- **Timeline**: Within 3 months of system launch
- **Source**: SH-001 -- VP of Operations

---

## 3. Scope Definition

### 3.1 In Scope

[List every feature included in this project phase with a one-sentence
scope statement.]

| # | Feature | Scope Statement |
|---|---------|-----------------|
| 1 | Order Entry | Capture and validate customer orders via web interface |
| 2 | Approval Workflow | Automated routing of orders requiring manager approval |

### 3.2 Out of Scope

[List exclusions with rationale.]

| # | Exclusion | Rationale |
|---|-----------|-----------|
| 1 | Mobile application | Deferred to Phase 2 per sponsor direction |
| 2 | International shipping | Current operations are domestic only |

### 3.3 Scope Assumptions

[List assumptions that, if invalidated, change the scope.]

- [ASSUMPTION] All users have access to a modern web browser (Chrome, Edge, Firefox)
- [ASSUMPTION] The existing ERP system provides a stable API for integration

---

## 4. Stakeholder Summary

### 4.1 Key Stakeholders

[Summary from stakeholder register with interests and concerns.]

### 4.2 Decision Authority

[Who approves what: scope changes, budget, timeline, requirements.]

### 4.3 Communication Summary

[High-level communication plan reference.]

---

## 5. Business Requirements

[Each requirement uses business-level language.]

### BR-001: [Requirement Title]

- **Description**: The business shall [requirement in active voice].
- **Priority**: Critical | High | Medium | Low
- **Source**: SH-XXX -- [Elicitation Finding ID]
- **Rationale**: [Why this requirement exists]
- **Acceptance Criterion**: [Measurable condition]
- **Dependencies**: [BR-YYY if any]
- **Assumptions**: [Related assumptions]

**Example:**

### BR-001: Automated Order Routing

- **Description**: The business shall route incoming orders to the
  appropriate fulfillment center based on inventory availability and
  geographic proximity.
- **Priority**: Critical
- **Source**: SH-002 -- EL-014
- **Rationale**: Manual routing causes 35% of delayed orders due to
  incorrect center assignment.
- **Acceptance Criterion**: 95% of orders are routed to the optimal
  fulfillment center within 30 seconds of submission.
- **Dependencies**: BR-003 (Real-time Inventory Visibility)
- **Assumptions**: [ASSUMPTION] All fulfillment centers maintain
  real-time inventory feeds.

---

## 6. Business Rules

### RULE-001: [Rule Name]

- **Statement**: [Formal rule]
- **Source**: [Policy, regulation, or stakeholder]
- **Type**: Constraint | Policy | Computation | Inference
- **Example**: [Concrete example]
- **Exceptions**: [When the rule does not apply]

**Example:**

### RULE-001: Order Approval Threshold

- **Statement**: Orders exceeding $10,000 shall require manager
  approval before processing.
- **Source**: Finance Policy FP-2024-003
- **Type**: Policy
- **Example**: An order totaling $12,500 is placed. The system holds
  the order and notifies the assigned manager for approval.
- **Exceptions**: Standing orders from pre-approved vendors are exempt.

### RULE-002: Late Fee Calculation

- **Statement**: Late fees shall be calculated as:
  $LateFee = Balance \times DailyRate \times DaysOverdue$
- **Source**: Accounts Receivable Policy AR-001
- **Type**: Computation
- **Example**: A $5,000 balance overdue by 10 days at a daily rate of
  0.05% yields: $LateFee = 5000 \times 0.0005 \times 10 = \$25.00$
- **Exceptions**: Accounts with a grace period agreement are exempt
  for the first 5 days.

---

## 7. Process Flows

### 7.1 Current State (As-Is)

[Numbered step sequence of the current process.]

### 7.2 Future State (To-Be)

[Numbered step sequence of the proposed process, highlighting changes.]

---

## 8. Success Criteria

| # | Criterion | Metric | Baseline | Target | Method | Review |
|---|-----------|--------|----------|--------|--------|--------|
| 1 | Processing speed | Avg days | 4.2 | <1.0 | System logs | Monthly |
| 2 | Error rate | % errors | 12% | <2% | QA audit | Monthly |

---

## 9. Assumptions and Constraints

### 9.1 Assumptions

- [ASSUMPTION] [Statement]

### 9.2 Constraints

- **Budget**: [Amount or range]
- **Timeline**: [Deadline]
- **Technology**: [Required platforms or tools]
- **Regulatory**: [Applicable regulations]

---

## 10. Glossary

| Term | Definition | Source |
|------|------------|--------|
| [Term] | [IEEE 610.12 or domain definition] | [Standard or SME] |

---

## 11. Standards Traceability

| BRD Section | IEEE 29148 Clause | Description |
|-------------|-------------------|-------------|
| 2. Business Objectives | 6.4.1 | Business purpose and scope |
| 5. Business Requirements | 6.4.2 | Business requirement statements |
| 6. Business Rules | 6.4.3 | Operational rules and policies |

---

## Appendix A: Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial draft |
```

## Section Completeness Checklist

| Section | Required Content | Complete |
|---------|-----------------|----------|
| Executive Summary | Problem, solution, value, stakeholders | [ ] |
| Business Objectives | ID, description, metric, target, timeline, source | [ ] |
| Scope - In | Feature list with scope statements | [ ] |
| Scope - Out | Exclusions with rationale | [ ] |
| Scope - Assumptions | Tagged with [ASSUMPTION] | [ ] |
| Business Requirements | ID, description, priority, source, criterion | [ ] |
| Business Rules | Statement, source, type, example, exceptions | [ ] |
| Process Flows | As-is and to-be documented | [ ] |
| Success Criteria | Metric, baseline, target, method, review frequency | [ ] |
| Glossary | All domain terms defined | [ ] |
| Standards Traceability | Mapped to IEEE 29148 clauses | [ ] |
