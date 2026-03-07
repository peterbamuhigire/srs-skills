# Stakeholder Power/Interest Grid Template

## Purpose

This template provides a structured Power/Interest grid for classifying stakeholders into four engagement quadrants. Use this template during Step 3 of the Stakeholder Analysis skill to ensure consistent classification and strategy assignment.

## Reference Standard

- IEEE 29148-2018 Section 6.2: Stakeholder identification
- Mendelow's Power/Interest Matrix (1991)

## Grid Definition

```
                        INTEREST
                   Low              High
              +-----------+-------------+
        High  |   KEEP    |   MANAGE    |
              | SATISFIED |   CLOSELY   |
   POWER      |           |             |
              +-----------+-------------+
        Low   |  MONITOR  |    KEEP     |
              |           |  INFORMED   |
              |           |             |
              +-----------+-------------+
```

## Quadrant Definitions

### Quadrant 1: Manage Closely (High Power / High Interest)

**Strategy**: Active collaboration, frequent updates, decision involvement.

| Attribute | Detail |
|-----------|--------|
| Engagement Level | Daily to weekly interaction |
| Communication | Face-to-face meetings, dedicated status reports |
| Decision Role | Co-decision maker, approval authority |
| Risk if Neglected | Project derailment, scope disputes, funding withdrawal |

**Typical Stakeholders**: Project sponsors, executive sponsors, product owners, key business unit leaders.

**Example**:
> SH-001: VP of Operations -- Funds the project and approves scope changes. Requires weekly progress reports and participates in milestone reviews. Classification rationale: Controls budget allocation (High Power) and the system directly replaces their department's current workflow (High Interest).

### Quadrant 2: Keep Satisfied (High Power / Low Interest)

**Strategy**: Regular status reports, escalation channel, periodic check-ins.

| Attribute | Detail |
|-----------|--------|
| Engagement Level | Bi-weekly to monthly interaction |
| Communication | Executive summaries, dashboard reports |
| Decision Role | Escalation authority, veto power |
| Risk if Neglected | Surprise vetoes, resource reallocation, political opposition |

**Typical Stakeholders**: C-suite executives not directly involved, board members, partner organization leads.

**Example**:
> SH-005: CTO -- Has authority over technology decisions but is not involved in day-to-day requirements. Requires monthly technology alignment briefings. Classification rationale: Can override architecture decisions (High Power) but delegates daily oversight to the development lead (Low Interest).

### Quadrant 3: Keep Informed (Low Power / High Interest)

**Strategy**: Newsletters, demo invitations, feedback channels.

| Attribute | Detail |
|-----------|--------|
| Engagement Level | Bi-weekly updates, demo participation |
| Communication | Newsletters, demo sessions, feedback forms |
| Decision Role | Advisor, feedback provider |
| Risk if Neglected | Loss of valuable domain input, user adoption resistance |

**Typical Stakeholders**: End users, testers, domain experts, training staff.

**Example**:
> SH-010: Front-desk Receptionist -- Daily user of the system but has no authority over project decisions. Provides critical usability feedback. Classification rationale: Cannot influence budget or scope (Low Power) but system quality directly affects daily work (High Interest).

### Quadrant 4: Monitor (Low Power / Low Interest)

**Strategy**: Minimal engagement, periodic awareness updates.

| Attribute | Detail |
|-----------|--------|
| Engagement Level | Monthly or quarterly awareness |
| Communication | General project newsletters, intranet updates |
| Decision Role | None |
| Risk if Neglected | Minimal, but may become relevant if project scope changes |

**Typical Stakeholders**: Other department staff, external vendors with limited involvement, future user groups.

**Example**:
> SH-015: Marketing Department -- Not directly affected by the system in the current phase but may need integration in Phase 2. Classification rationale: No current decision authority (Low Power) and no immediate impact from the system (Low Interest).

## Classification Worksheet

Use this worksheet for each identified stakeholder:

```
Stakeholder ID: SH-___
Name/Role: _______________
Category: _______________

Power Assessment:
  [ ] Controls budget or funding decisions
  [ ] Has approval/veto authority over scope
  [ ] Can allocate or withdraw resources
  [ ] Has political influence over project direction
  Power Level: [ ] High  [ ] Low

Interest Assessment:
  [ ] Directly uses the system daily
  [ ] System outcomes affect their KPIs
  [ ] Has expressed active concern about requirements
  [ ] Domain expertise is critical to project success
  Interest Level: [ ] High  [ ] Low

Quadrant: _______________
Engagement Strategy: _______________
Rationale: _______________________________________________
```

## Reclassification Triggers

Stakeholder classifications are not static. Reassess when:

- Project scope changes significantly
- Organizational restructuring occurs
- A stakeholder's role or responsibilities change
- New regulatory requirements introduce new authority structures
- A previously low-interest stakeholder raises concerns or requests

## Usage Notes

- Every classification shall include a rationale grounded in evidence from project context files
- If a stakeholder falls on the boundary between quadrants, classify them in the higher-engagement quadrant to reduce risk
- Tag inferred classifications with `[INFERRED]` so they can be validated with the project team
