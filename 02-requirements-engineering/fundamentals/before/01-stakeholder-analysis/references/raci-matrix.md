# RACI Matrix Template and Usage Guide

## Purpose

This template provides a standardized RACI (Responsible, Accountable, Consulted, Informed) matrix for mapping stakeholder roles to requirements engineering activities. The RACI matrix ensures clear accountability and prevents role ambiguity during requirements elicitation, validation, and approval.

## Reference Standard

- IEEE 29148-2018 Section 6.2: Stakeholder roles in requirements processes
- PMI PMBOK Guide: Responsibility Assignment Matrix

## RACI Role Definitions

| Role | Symbol | Definition | Obligation |
|------|--------|------------|------------|
| **Responsible** | R | Performs the work to complete the activity | Must complete the deliverable |
| **Accountable** | A | Owns the decision; ultimate authority for the activity | Exactly one per activity row |
| **Consulted** | C | Provides input before the decision is made | Two-way communication required |
| **Informed** | I | Notified after the decision is made | One-way communication sufficient |

## Constraint Rules

1. Every activity row shall have exactly one **A** (Accountable) assignment
2. Every activity row shall have at least one **R** (Responsible) assignment
3. A single stakeholder may hold both **A** and **R** for the same activity
4. Minimize the number of **C** assignments to avoid decision paralysis
5. Flag any row with zero **R** assignments as `[RACI-FAIL: No responsible party]`
6. Flag any row with multiple **A** assignments as `[RACI-FAIL: Multiple accountable parties]`

## Matrix Template

### Requirements Engineering Activities

| Activity | Sponsor | Product Owner | Primary Users | Business Analyst | Developers | Testers | Regulators | Operators |
|----------|---------|---------------|---------------|------------------|------------|---------|------------|-----------|
| Stakeholder Identification | I | A/R | I | R | I | I | I | I |
| Requirements Elicitation | I | A | R | R | C | I | C | I |
| Requirements Analysis | I | A | C | R | C | C | I | I |
| Requirements Validation | A | R | R | R | C | C | C | I |
| Requirements Specification | I | A | C | R | C | I | I | I |
| Requirements Approval | A | R | C | I | I | I | C | I |
| Change Request Initiation | I | A | R | R | C | C | C | I |
| Change Impact Assessment | I | A | C | R | R | C | C | C |
| Acceptance Test Definition | I | A | R | R | C | R | C | I |
| Deployment Sign-off | A | I | I | I | R | C | I | R |

### How to Read the Matrix

- Read **columns** to understand a stakeholder's full set of responsibilities across all activities
- Read **rows** to understand who is involved in each specific activity
- A stakeholder with many **R** assignments has a heavy workload -- consider redistribution
- A stakeholder with many **C** assignments may become a bottleneck -- consider downgrading some to **I**

## Extended Activities (Optional)

For projects requiring additional governance activities:

| Activity | Sponsor | PM | BA | Dev Lead | QA Lead | Security | Compliance |
|----------|---------|----|----|----------|---------|----------|------------|
| Risk Assessment | A | R | C | C | C | C | C |
| Compliance Review | I | I | C | I | I | R | A |
| Security Review | I | I | I | C | C | A/R | C |
| Architecture Review | I | I | I | A/R | C | C | I |
| Release Planning | A | R | C | C | C | I | I |
| Post-Deployment Review | I | A/R | C | R | R | C | C |

## Validation Procedure

After constructing the RACI matrix, verify:

1. **Accountability Check**: Every row has exactly one A
   ```
   For each activity:
     count_A = count of 'A' assignments
     IF count_A != 1 THEN flag [RACI-FAIL: {activity} has {count_A} accountable parties]
   ```

2. **Responsibility Check**: Every row has at least one R
   ```
   For each activity:
     count_R = count of 'R' assignments
     IF count_R == 0 THEN flag [RACI-FAIL: {activity} has no responsible party]
   ```

3. **Overload Check**: No stakeholder has R or A in more than 60% of activities
   ```
   For each stakeholder:
     load = count of 'R' or 'A' assignments / total activities
     IF load > 0.6 THEN flag [RACI-WARN: {stakeholder} may be overloaded at {load}%]
   ```

4. **Consultation Bottleneck Check**: No stakeholder has C in more than 70% of activities
   ```
   For each stakeholder:
     consult_load = count of 'C' assignments / total activities
     IF consult_load > 0.7 THEN flag [RACI-WARN: {stakeholder} consulted too frequently]
   ```

## Common Anti-Patterns

| Anti-Pattern | Description | Resolution |
|--------------|-------------|------------|
| **Consensus Trap** | Every stakeholder is C or A on every activity | Reduce C assignments; trust delegated authority |
| **Orphan Activity** | Activity has no R assignment | Assign a responsible party or remove the activity |
| **Dual Accountability** | Two stakeholders share A on one activity | Designate one A; move the other to C |
| **Invisible Stakeholder** | A stakeholder column is entirely I | Confirm the stakeholder is correctly identified; consider removal |
| **Hero Pattern** | One stakeholder is R on every activity | Redistribute responsibilities to prevent single point of failure |

## Usage Notes

- Populate the matrix during or immediately after stakeholder analysis
- Review and update the matrix when stakeholders change or project scope shifts
- Use this matrix as an input to the Communication Plan (ensures the right people are engaged at the right time)
- Store the completed matrix in the stakeholder register output file
