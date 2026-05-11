# Impact Map Traceability Matrix

## Source Grounding

Derived from local HTML extractions:

- `impact-mapping/toc.ncx`, `index_split_000.html`: Why, Who, How, What, measurable objectives, adaptive planning, milestone planning, alternatives, priorities, earn-or-learn.
- `crafting-engineering-strategy/toc.ncx`: policy and operating mechanisms as strategy enforcement concepts.

This reference converts impact mapping into SDLC traceability.

## Impact Map Rows

| Why | Who | How | What | Measure | Requirement Candidate | Milestone |
|---|---|---|---|---|---|---|
| measurable goal | actor | behaviour change | deliverable or experiment | actor signal + business signal | FR/NFR/UX/SUP/CTRL | earn or learn |

## Requirement Conversion Rules

1. `Why` becomes a business objective, PRD success metric, or business case outcome.
2. `Who` becomes stakeholder, persona, user class, operator, partner, regulator, or blocker.
3. `How` becomes required behaviour change or operational change.
4. `What` becomes the smallest deliverable, prototype, workflow change, content change, support action, or requirement candidate.
5. `Measure` becomes acceptance criteria, test oracle, adoption metric, or evaluation measure.

## Earn-Or-Learn Milestone

| Milestone | Purpose | Exit Decision |
|---|---|---|
| Learn | Test high-risk assumption with smallest credible evidence. | pivot, persevere, stop |
| Earn | Expand validated capability toward outcome metric. | invest, scale, harden |

## Trace Gate

Reject a feature or requirement when:

- no actor can influence the goal
- no behaviour change is specified
- the deliverable is not the smallest credible intervention
- no measure defines success
- the milestone cannot produce a decision

