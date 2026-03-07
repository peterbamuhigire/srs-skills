# Usability Testing Reference

## Test Planning Template

### Section 1: Test Objectives

The system shall define specific, measurable objectives for each usability test round:

| Objective ID | Hypothesis | Success Criterion | Priority |
|-------------|-----------|-------------------|----------|
| UTO-001 | Users can complete [task] without assistance | >= 85% unassisted completion rate | Critical |
| UTO-002 | Users can find [feature] within [time] | Average time <= [threshold] seconds | Major |
| UTO-003 | Users understand [terminology/label] | >= 80% correct interpretation | Major |

### Section 2: Participant Recruitment

**Minimum Sample Size:** 5 participants per distinct user segment (per Nielsen Norman Group findings that 5 users uncover approximately 85% of usability problems).

**Screening Criteria:**

| Criterion | Specification |
|-----------|--------------|
| User Segment | Match personas from `stakeholder_register.md` |
| Domain Experience | Range from novice to expert within the segment |
| Technical Proficiency | Representative of the target audience |
| Accessibility Needs | Include at least 1 participant using assistive technology per WCAG testing requirements |
| Exclusions | No participants involved in the product design or development |

### Section 3: Test Environment

| Format | Description | When to Use |
|--------|-------------|-------------|
| Moderated Remote | Facilitator guides participant via video call, screen sharing | Early-stage testing, complex tasks, when think-aloud data is critical |
| Unmoderated Remote | Participant completes tasks independently using a testing platform | Large sample sizes, benchmark testing, quantitative metrics |
| In-Person Lab | Facilitator and participant in the same room, optional observation room | High-fidelity prototype testing, accessibility testing with hardware |

## Task Scenario Writing Guide

### Principles

1. **Realistic:** The scenario shall describe a situation the user would actually encounter.
2. **Goal-Oriented:** The scenario shall state what the user wants to achieve, not how to achieve it.
3. **No Leading Language:** The scenario shall not use terminology from the interface or hint at the solution path.
4. **Contextual:** The scenario shall provide enough background for the user to understand their motivation.

### Template

> "You are **[role/context]**. You need to **[goal]**. Using the application, **[action without hinting at specific UI elements]**."

### Examples

**Good:**
> "You are a team manager who just hired a new employee. You need to make sure this person can access the project files. Using the application, set this up."

**Bad (leading language):**
> "Click on the 'Team Management' menu, then click 'Add User' to add a new team member and assign the 'Project Editor' role."

**Good:**
> "You received a notification that your monthly report is ready. You want to review the data for the Southeast region and share it with your director."

**Bad (too vague):**
> "Use the reports feature."

## Observation Recording Format

### Per-Task Observation Sheet

| Field | Description |
|-------|-------------|
| Task ID | Reference to the task scenario |
| Participant ID | Anonymized participant identifier |
| Start Time | Timestamp when the participant begins the task |
| End Time | Timestamp when the participant completes or abandons the task |
| Duration (s) | Calculated elapsed time |
| Completed | Yes / No / Partial |
| Errors | Count of incorrect actions, wrong paths, or missteps |
| Path Taken | Sequence of screens/actions the participant followed |
| Verbal Quotes | Notable think-aloud statements (verbatim) |
| Emotional Response | Observed frustration, confusion, satisfaction, or delight |
| Severity | Critical / Major / Minor / Cosmetic (if a problem was observed) |
| Notes | Additional observer commentary |

### Observation Table

| Task | Participant | Duration (s) | Completed | Errors | Path Taken | Quotes | Severity |
|------|-------------|-------------|-----------|--------|------------|--------|----------|
| T-01 | P01 | 45 | Yes | 0 | Home > List > Detail > Edit | "That was straightforward" | -- |
| T-01 | P02 | 120 | Partial | 3 | Home > Search > Wrong result > Back > List > Detail | "I expected search to filter by name" | Major |

## System Usability Scale (SUS)

### Questionnaire

The SUS questionnaire consists of 10 statements. Participants rate each on a 5-point Likert scale (1 = Strongly Disagree, 5 = Strongly Agree).

| # | Statement |
|---|-----------|
| 1 | I think that I would like to use this system frequently. |
| 2 | I found the system unnecessarily complex. |
| 3 | I thought the system was easy to use. |
| 4 | I think that I would need the support of a technical person to be able to use this system. |
| 5 | I found the various functions in this system were well integrated. |
| 6 | I thought there was too much inconsistency in this system. |
| 7 | I would imagine that most people would learn to use this system very quickly. |
| 8 | I found the system very cumbersome to use. |
| 9 | I felt very confident using the system. |
| 10 | I needed to learn a lot of things before I could get going with this system. |

### Scoring Method

1. For odd-numbered items (1, 3, 5, 7, 9): subtract 1 from the participant's response. Score = (response - 1).
2. For even-numbered items (2, 4, 6, 8, 10): subtract the participant's response from 5. Score = (5 - response).
3. Sum all 10 adjusted scores.
4. Multiply the sum by 2.5 to obtain the SUS score (range: 0--100).

### Interpretation

| SUS Score | Grade | Adjective Rating | Percentile |
|-----------|-------|-------------------|------------|
| >= 80.3 | A | Excellent | Top 10% |
| 68 -- 80.2 | B | Good | Top 30% |
| 68 | C | OK | Median |
| 51 -- 67 | D | Poor | Bottom 30% |
| <= 50 | F | Awful | Bottom 15% |

**Target:** The system shall achieve a SUS score of >= 68 (above average). Scores below 68 shall trigger a design review cycle.

## Findings-to-Requirements Traceability

### Severity Classification

| Severity | Definition | Action Required |
|----------|-----------|-----------------|
| Critical | The user cannot complete the task. Data loss or security risk. | The system shall generate a new requirement or modify an existing requirement immediately. Block release. |
| Major | The user completes the task but with significant difficulty, errors, or workarounds. | The system shall generate a requirement update. Address before next release. |
| Minor | The user notices the issue but completes the task with minimal impact. | Log for future improvement. Address within two release cycles. |
| Cosmetic | Aesthetic or preference issue with no functional impact. | Log as enhancement. Address when convenient. |

### Findings Register Template

| Finding ID | Task | Severity | Description | Affected Requirement | Action | Status |
|-----------|------|----------|-------------|---------------------|--------|--------|
| UXF-001 | T-01 | Major | Users could not locate the export function | REQ-3.2.4 | Add export button to toolbar | Open |
| UXF-002 | T-03 | Critical | Form submitted without validation, caused data error | REQ-3.2.7 | Add client-side validation | Open |

### Feedback Loop Process

1. The system shall classify each finding by severity.
2. Critical and Major findings shall be mapped to existing SRS requirements or generate new requirements.
3. Each new or modified requirement shall receive a unique identifier and traceability link to the finding.
4. The updated requirement shall re-enter the skill pipeline (Phase 02 for requirements, Phase 03 for design updates).
5. The next usability test round shall include regression tasks to verify that the finding has been resolved.
