# Engineering Strategy Brief Template

## Source Grounding

Derived from local HTML extractions:

- `crafting-engineering-strategy/toc.ncx`, `index_split_000.html` through `index_split_003.html`: exploration, diagnosis, refinement, setting policy, operations, strategy altitude, written strategy, review, learning from failed strategies.
- `articulating-design-decisions/toc.ncx`, `index_split_000.html` through `index_split_002.html`: stakeholder values, meeting design, listening, response strategy, business/design/research messages, agreement, follow-up, change handling.
- `impact-mapping/toc.ncx`, `index_split_000.html`: measurable goal, actors, impacts, alternatives, milestones.

This template is original operational guidance for SDLC documentation.

## Brief Structure

```markdown
# Engineering Strategy Brief: [Project Name]

## 1. Strategic Question
- Decision altitude: portfolio | product | platform | component
- Decision deadline:
- Decision owners:
- Affected artifacts: PRD | SRS | HLD | Infrastructure | ADR | Test | Deployment | Governance

## 2. Context And Constraints
| Source | Constraint Or Fact | Impact On Strategy |
|---|---|---|

## 3. Diagnosis
State the core technical problem in 3-7 sentences.

## 4. Guiding Policy
| Policy | What It Enables | What It Rejects | Evidence Needed |
|---|---|---|---|

## 5. Coherent Actions
| Action | Owner | Sequence | Dependency | Success Signal |
|---|---|---|---|---|

## 6. Operating Mechanisms
| Mechanism | Cadence | Owner | Decision Rights | Evidence |
|---|---|---|---|---|

## 7. ADR Candidates
| ADR Candidate | Trigger | Options To Compare | Deadline |
|---|---|---|---|

## 8. Risk, Exception, And Kill Criteria
| Risk Or Assumption | Signal | Action |
|---|---|---|

## 9. Traceability
| Strategy Item | Requirement / Risk / Control | Evidence Artifact |
|---|---|---|
```

## Strategy Quality Gate

Accept the brief only if:

- the diagnosis explains why ordinary implementation will not solve the problem
- each policy can reject at least 1 plausible option
- coherent actions are sequenced, owned, and measurable
- operations define who reviews progress and how exceptions are handled
- ADR candidates identify decisions that require durable records
- strategy links to requirements, risks, quality attributes, and validation evidence

## Stakeholder Objection Handling

When objections arise, record:

| Objection | Stakeholder Value Behind It | Evidence Needed | Decision Response | Follow-Up Owner |
|---|---|---|---|---|

Use business, design, research, risk, and delivery messages as separate lenses. Do not argue aesthetics or preferences when the concern is revenue, risk, compliance, support load, or delivery capacity.

