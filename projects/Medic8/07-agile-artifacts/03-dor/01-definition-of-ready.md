# Definition of Ready: Medic8

**Document ID:** Medic8-DoR-001
**Version:** 1.0
**Date:** 2026-04-03
**Methodology:** Hybrid (Water-Scrum-Fall)
**Standards:** Scrum Guide 2020, IEEE 29148-2018, INVEST Criteria

The Definition of Ready (DoR) is the quality gate that determines whether a story or sprint is sufficiently prepared for development to begin. No story enters a sprint commitment until every applicable item is satisfied. This prevents mid-sprint discovery of missing context, ambiguous requirements, or unresolved dependencies.

---

## 1 Story Level Definition of Ready

Every user story must meet all of the following criteria before it is accepted into a sprint during Sprint Planning.

### 1.1 Story Structure

- [ ] User story follows the "As a [role] / I want to [action] / So that [benefit]" format
- [ ] The role is a specific Medic8 persona (e.g., "Receptionist," "Doctor," "Pharmacist," "Lab Technician," "Facility Admin"), not a generic "user"
- [ ] The "So that" clause states a measurable business or clinical benefit, not a restatement of the action
- [ ] Story title is concise (under 80 characters) and describes the user-visible outcome

### 1.2 Acceptance Criteria

- [ ] Acceptance criteria written in Gherkin Given/When/Then format
- [ ] Minimum 3 acceptance criteria per story (happy path, error path, edge case)
- [ ] Each acceptance criterion is independently testable with a deterministic pass/fail outcome
- [ ] No acceptance criterion uses vague adjectives ("fast," "intuitive," "reliable") without a measurable threshold (IEEE 982.1 compliant)
- [ ] Security-relevant criteria include the specific PDPA 2019 section or quality standard reference

### 1.3 Estimation and Prioritisation

- [ ] Story points estimated using Modified Fibonacci scale (1, 2, 3, 5, 8, 13)
- [ ] Stories exceeding 13 points have been decomposed into smaller stories that each deliver independent value
- [ ] Priority assigned: Critical, High, Medium, or Low
- [ ] Priority rationale documented (e.g., "Critical: blocks all downstream clinical workflows")

### 1.4 Traceability

- [ ] Business rules cross-referenced: all applicable BR- identifiers listed (e.g., BR-CLIN-004, BR-FIN-001)
- [ ] Functional requirement cross-referenced: FR- identifier linked to the SRS section where the requirement is defined
- [ ] If the story implements a regulatory requirement (PDPA, HMIS, PEPFAR): the regulatory reference is cited in the acceptance criteria

### 1.5 Dependencies

- [ ] Dependencies identified: "blocked by" and "blocks" relationships documented
- [ ] All blocking dependencies are either already completed or scheduled in a prior sprint
- [ ] External dependencies (API access, licences, hardware, third-party data) identified with current status and expected resolution date
- [ ] If the story requires a new library or package: the library has been evaluated for licence compatibility, maintenance status, and security posture

### 1.6 Design Artefacts

- [ ] UI wireframe or screen reference provided for stories with a user interface component (Tabler template page or Figma reference)
- [ ] API endpoint defined in the API specification for backend stories: route, HTTP method, request body schema, response schema, authentication requirement
- [ ] Database table and columns defined in the ERD for stories that introduce or modify data models
- [ ] If the story modifies an existing table: migration strategy documented (additive, nullable, backfill required)

### 1.7 Test Approach

- [ ] Test approach identified: unit test, integration test, end-to-end test, or combination
- [ ] Test data requirements documented: what seed data, fixtures, or factories are needed
- [ ] If the story requires external service integration (MoMo API, SMS gateway, HL7 analyser): mock or sandbox availability confirmed

---

## 2 Clinical Story Definition of Ready

These criteria apply in addition to the Story Level DoR for any story that touches clinical workflows, prescribing, CDS rules, laboratory, or patient safety logic.

### 2.1 Clinical Workflow

- [ ] Clinical workflow documented: stimulus-response pattern from the SRS functional requirements section (e.g., "When the doctor submits a prescription, the system validates Five Rights per BR-CLIN-008")
- [ ] Workflow covers the complete clinical path: initiating event, processing steps, expected outcome, and exception handling
- [ ] Role-specific permissions for the workflow are defined (who can initiate, who can approve, who can override)

### 2.2 Clinical Decision Support Rules

- [ ] CDS rules defined with full specification: trigger condition, severity level, alert message, and required action (proceed, override with reason, or hard stop)
- [ ] For drug interaction stories: the drug interaction dataset is available and the relevant drug pairs are identified
- [ ] For dosing stories: therapeutic ranges, adult ceiling doses, and weight-based calculation formulae are specified with references
- [ ] For scoring stories (NEWS2, APGAR, GCS): scoring criteria, thresholds, and escalation actions are specified with clinical references

### 2.3 Reference Ranges and Thresholds

- [ ] Reference ranges specified for all laboratory tests included in the story (normal range, abnormal flag thresholds, critical/panic value thresholds)
- [ ] Thresholds are age-group and sex-adjusted where clinically appropriate
- [ ] Critical value panic thresholds are defined per BR-CLIN-003 (e.g., potassium > 6.5 mmol/L, glucose < 2.5 mmol/L)
- [ ] Source of reference ranges documented (e.g., WHO, Uganda MoH Clinical Guidelines, facility-specific)

### 2.4 Verifiability

- [ ] Verifiability criterion from the NFR document reviewed: the story's acceptance criteria produce a deterministic test oracle, not a judgment call
- [ ] Expected numerical results documented for calculation-based stories (dosing, scoring, billing): at least 3 worked examples with inputs and expected outputs
- [ ] If the story involves clinical data display: display format specified (units, decimal places, colour coding for abnormal values)

### 2.5 Patient Safety Impact

- [ ] Patient safety impact assessment completed: what is the worst-case outcome if this story has a defect?
- [ ] Safety impact classified: None, Low (inconvenience), Medium (delayed care), High (potential harm), Critical (life-threatening)
- [ ] For High or Critical safety impact stories: the test plan includes negative testing (system prevents harm when given incorrect input) and boundary testing (system behaves correctly at threshold values)
- [ ] For stories involving medication: the story is cross-referenced against the Five Rights (BR-CLIN-008) and the applicable CDS rules (BR-CLIN-004, BR-CLIN-006)

---

## 3 Sprint Definition of Ready

The sprint itself must meet the following criteria before development begins (evaluated at the end of Sprint Planning).

### 3.1 Sprint Goal

- [ ] Sprint goal defined in one sentence that describes the user-visible outcome (e.g., "Deliver the outpatient clinical consultation workflow from queue to diagnosis")
- [ ] Sprint goal is achievable within the sprint duration (2 weeks) at the current velocity
- [ ] Sprint goal aligns with the Phase 1 Sprint Plan (`07-agile-artifacts/01-sprint-planning/01-sprint-planning.md`)

### 3.2 Capacity and Fit

- [ ] Stories prioritised by Critical > High > Medium > Low within the sprint
- [ ] Total story points fit within the team's velocity (initial estimate: 40 points; adjusted after Sprint 2)
- [ ] If total points exceed velocity by more than 10%: deferral candidates identified with documented rationale
- [ ] Buffer reserved for bug fixes from previous sprints (minimum 10% of velocity for Sprint 3 onward)

### 3.3 Blockers and Dependencies

- [ ] No unresolved blockers at sprint start
- [ ] All dependencies from the previous sprint are completed (stories marked "Done" per the DoD)
- [ ] External dependencies (API credentials, licences, test data, hardware) are resolved or have a confirmed resolution date within the first 3 days of the sprint
- [ ] If an external dependency is unresolved: a contingency plan is documented (e.g., "Use mock API; switch to live integration when credentials arrive")

### 3.4 Environment

- [ ] Test environment ready: staging server deployed with the previous sprint's increment
- [ ] Test data available: seed data, factories, and fixtures are current
- [ ] CI pipeline passing on the `develop` branch before sprint start
- [ ] No infrastructure changes required during the sprint that would cause environment downtime

---

## 4 Readiness Checklist Summary

Use this quick-reference checklist during Sprint Planning to verify readiness.

### Story Quick Check (All Stories)

| # | Criterion | Met? |
|---|---|---|
| 1 | As a / I want / So that format | [ ] |
| 2 | Gherkin acceptance criteria (minimum 3) | [ ] |
| 3 | Story points estimated (Fibonacci 1-13) | [ ] |
| 4 | Priority assigned | [ ] |
| 5 | BR- identifiers listed | [ ] |
| 6 | FR- identifier linked | [ ] |
| 7 | Dependencies identified | [ ] |
| 8 | UI wireframe or API spec provided | [ ] |
| 9 | Database schema defined (if applicable) | [ ] |
| 10 | Test approach identified | [ ] |

### Clinical Story Quick Check (Additional)

| # | Criterion | Met? |
|---|---|---|
| 11 | Clinical workflow documented (stimulus-response) | [ ] |
| 12 | CDS rules specified (severity, condition, message) | [ ] |
| 13 | Reference ranges/thresholds specified | [ ] |
| 14 | NFR verifiability reviewed | [ ] |
| 15 | Patient safety impact assessed | [ ] |

### Sprint Quick Check

| # | Criterion | Met? |
|---|---|---|
| 16 | Sprint goal defined (one sentence) | [ ] |
| 17 | Stories fit within velocity | [ ] |
| 18 | No unresolved blockers | [ ] |
| 19 | Previous sprint dependencies completed | [ ] |
| 20 | Test environment ready | [ ] |

---

## 5 Handling Stories That Are Not Ready

When a story fails the DoR check during Sprint Planning:

1. The story is returned to the backlog with a documented list of the unmet DoR criteria
2. The developer (or product owner) is responsible for resolving the gaps before the next Sprint Planning
3. The story is eligible for the next sprint once all DoR criteria are satisfied
4. A story that fails the DoR check 2 consecutive Sprint Plannings is escalated to the project owner (Peter) for re-evaluation: the story may need to be rewritten, split, or deprioritised

**No story enters a sprint commitment without passing the DoR. This is non-negotiable.**

---

## 6 Cross-References

- **Definition of Done:** `07-agile-artifacts/02-dod/01-definition-of-done.md`
- **Sprint Planning:** `07-agile-artifacts/01-sprint-planning/01-sprint-planning.md`
- **User Stories:** `02-requirements-engineering/02-user-stories/01-user-stories.md`
- **Business Rules:** `_context/business_rules.md`
- **Quality Standards:** `_context/quality_standards.md`
