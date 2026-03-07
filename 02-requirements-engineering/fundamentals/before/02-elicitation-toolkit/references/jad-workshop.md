# Joint Application Development (JAD) Workshop Guide

## Purpose

This reference provides a facilitation guide for conducting JAD workshops as a requirements elicitation technique. JAD brings stakeholders together in structured sessions to collaboratively define requirements, resolve conflicts, and build consensus.

## Reference Standard

- IEEE 29148-2018 Section 6.3: Collaborative elicitation techniques
- Wiegers Practice 4: Workshop facilitation

## When to Use JAD

| Condition | Suitability |
|-----------|-------------|
| Multiple stakeholders with competing priorities | Excellent |
| Complex domain requiring cross-functional input | Excellent |
| Requirements are greenfield and need rapid discovery | Excellent |
| Stakeholders are co-located or can attend synchronously | Required |
| Stakeholder availability is low or asynchronous only | Poor |

## Participant Roles

| Role | Responsibility | Selection Criteria |
|------|----------------|--------------------|
| **Facilitator** | Guides discussion, manages time, ensures participation | Neutral party, not a stakeholder |
| **Scribe** | Records decisions, action items, and requirements | Detail-oriented, fast note-taker |
| **Sponsor** | Opens session, confirms scope, resolves escalations | From "Manage Closely" quadrant |
| **Subject Matter Experts** | Provide domain knowledge and validate feasibility | From "Keep Informed" quadrant |
| **User Representatives** | Represent end-user needs and workflows | Primary/Secondary users from register |
| **Technical Representative** | Assess feasibility and identify constraints | Developer or architect |

**Minimum viable attendance**: 1 Facilitator + 1 Scribe + 1 Sponsor + 2 User Representatives + 1 Technical Representative.

## Workshop Agenda Template

### Pre-Workshop (1 week before)

- [ ] Define workshop objectives and scope boundaries
- [ ] Select and invite participants (reference stakeholder register)
- [ ] Distribute pre-read materials: `vision.md` summary, `features.md` summary
- [ ] Prepare facilitation materials: whiteboard/digital board, sticky notes, voting dots
- [ ] Book venue or video conference with recording capability
- [ ] Send agenda to all participants

### Session Structure (4-6 hours)

| Time Block | Duration | Activity | Deliverable |
|------------|----------|----------|-------------|
| Opening | 30 min | Welcome, objectives, ground rules | Shared understanding of scope |
| Current State | 45 min | Walk through existing workflows and pain points | As-is process documentation |
| Feature Discovery | 60 min | Brainstorm features and capabilities needed | Feature candidate list |
| Break | 15 min | -- | -- |
| Requirements Definition | 60 min | Define requirements for each feature candidate | Draft requirement statements |
| Prioritization | 45 min | Dot voting or MoSCoW classification | Prioritized requirement list |
| Conflict Resolution | 30 min | Address disagreements, document dissenting views | Consensus log |
| Closure | 15 min | Summarize decisions, assign action items | Action item list |

### Ground Rules

Present these at the opening and enforce throughout:

1. Every participant has equal voice regardless of organizational rank
2. Criticize ideas, not people
3. One conversation at a time
4. Decisions are made by consensus; dissenting views are recorded, not suppressed
5. The facilitator may table discussions that exceed the allocated time
6. All decisions are provisional until documented and reviewed

## Consensus Techniques

### Dot Voting

1. Each participant receives 5 dots (physical or digital)
2. Participants place dots on features/requirements they consider most important
3. Tally votes to establish priority ranking
4. Features with zero votes are candidates for "Out of Scope"

### Fist of Five

1. Facilitator states a proposed requirement
2. Each participant holds up 0-5 fingers:
   - 5: Strongly agree
   - 4: Agree
   - 3: Neutral, will support
   - 2: Reservations, need discussion
   - 1: Strongly disagree
   - 0: Block -- cannot proceed without resolution
3. If any participant shows 0 or 1, the item requires further discussion

### Parking Lot

1. Items that cannot be resolved in the session go to the "Parking Lot"
2. Each parking lot item is assigned an owner and a resolution deadline
3. Parking lot items are reviewed at the next session or via follow-up

## Workshop Deliverables

After the workshop, the facilitator and scribe shall produce:

1. **Requirements List**: All requirements identified, with IDs and priority
2. **Consensus Log**: Decisions made and the consensus level achieved
3. **Dissent Record**: Any unresolved disagreements with stakeholder positions
4. **Parking Lot**: Deferred items with owners and deadlines
5. **Action Items**: Follow-up tasks with assignees and due dates

## Recording Format

For each finding from the workshop:

```
#### EL-XXX: [Finding Title]

- **Source**: JAD Workshop -- [Participant IDs who contributed]
- **Technique**: JAD Workshop
- **Consensus Level**: Unanimous | Majority | Contested
- **Statement**: "[Agreed requirement statement]"
- **Dissenting View**: "[If contested, record the opposing position]"
- **Derived Requirement**: The system shall [requirement].
- **Type**: Functional | Non-Functional | Constraint | Assumption
- **Confidence**: Confirmed | Likely | Uncertain
- **Priority**: [As determined by dot voting or consensus]
```

## Post-Workshop Procedures

1. Distribute workshop notes to all participants within 48 hours
2. Allow 5 business days for review and corrections
3. Schedule follow-up sessions for parking lot items
4. Integrate confirmed findings into the elicitation log
5. Update the stakeholder register if new stakeholders were identified during the workshop
