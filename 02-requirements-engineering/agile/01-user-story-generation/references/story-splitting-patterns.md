# Story Splitting Patterns

Parent skill: [01-user-story-generation](../SKILL.md). Load it when a story
fails the Small or Independent test in `invest-criteria.md`, when a
rewrite or migration looks all-or-nothing, or when a backlog is flat and
cannot be tied to business impact. It complements the vertical-slicing rule
already in `invest-criteria.md`; it does not replace it.

## 1. Start from impact, not from the story list

1. Name the business goal and the behaviour change wanted from one actor
   segment (the impact). Stakeholders choose the next impact; the team then
   chooses the stories that serve it within the budget.
2. Keep the backlog hierarchical: goal, impact, story, task. A story with no
   impact above it is either gold-plating or a missing impact.
3. Dependencies between stories are resolved at impact level by sequencing
   or by splitting further, never by bundling stories together.

## 2. Choose a splitting pattern

Try the patterns roughly in this order; the earlier ones keep more user
value per slice.

| Pattern | Use when | Example (school-fees portal, Kampala) |
|---|---|---|
| Narrow the segment | One user group can be fully served with far less complexity | Day-school parents paying by MTN MoMo first; boarding fees and bank transfers later |
| Slice by useful outcome | A large rebuild or migration looks indivisible | First deliver the fee-balance statement parents already ask for, read from the legacy system |
| Start with outputs | A rewrite would otherwise start with data entry screens | Deliver the bursar's daily collections report before rebuilding student registration |
| Lower capacity first | Scale drives most of the architecture cost | One school, 800 pupils, one term; multi-school tenancy in a later story |
| Fixed data before live data | Reference data sits in a system not yet accessible | Hard-code the term's fee schedule; connect to the finance system later |
| Simplify outputs | The final destination or format is expensive | Export reconciliations to CSV before the ERP posting interface |
| Utility before ease | Internal users need the task possible now | Manual trigger of the payment-matching job before scheduled automation |
| Learning spike | The team lacks information to plan | Time-boxed investigation of the bank's callback format, with a stated decision it must enable |

Constraints on the lower-value patterns:

- "Simplify outputs" must not drop security, privacy or statutory controls
  for real personal or financial data. Deferring encryption or masking is
  acceptable only with synthetic data and a signed risk acceptance.
- "Utility before ease" suits internal staff tools, never consumer or
  premium-positioned journeys, and the stakeholder must be told in writing
  that the first slice trades usability for speed.
- A learning spike is not a user story. Its acceptance condition is the
  information delivered and the decision it enables, inside a fixed time box.

## 3. When nothing splits: layer the options

For an all-or-nothing flow, list the components it passes through (capture,
validation, storage, notification, reporting). For each, list options at
different quality levels (manual, simple, full). Remove unacceptable options,
then pick one option per component to form the thinnest end-to-end slice.
Later stories raise one component at a time.

## 4. What does not belong in stories

Infrastructure, library upgrades, pipeline work and refactoring are managed
through an explicit team capacity allocation, not written as "As a developer
I want" stories that compete with user value. Record them as technical
backlog items with their own acceptance checks.

## 5. Sizing and planning

- Prefer non-numeric sizes (small, medium, large, or comparison with a
  reference story) for near-term planning. Do not sum story points into
  long-range delivery commitments without a stated confidence interval.
- For fixed dates, ask for the budget and the least valuable outcome that
  still makes the release worthwhile, then design the slice to fit.

## Quality gate

- Each resulting story still delivers observable value to a named actor.
- Each slice is independently demonstrable and testable.
- Deferred controls carry an owner, a story ID and a risk record.
- Every story traces to an impact and a goal.

## Anti-patterns

- Horizontal splits (database story, API story, UI story). Fix: slice end to
  end through all layers.
- "As a user" with no segment. Fix: name the segment the slice serves.
- Solution dictated in the "I want" clause. Fix: state the need; leave the
  mechanism to design unless it is a stakeholder constraint.
- Flat backlog of fifty ranked stories. Fix: rank impacts, then select stories.
- Story whose outcome sits outside the team's control ("increase enrolment by
  10%"). Fix: move the outcome to the impact; the story delivers the
  capability that influences it.

## Sources and currentness

Independent synthesis informed by Adzic and Evans, *Fifty Quick Ideas to
Improve Your User Stories*, and Adzic, *Impact Mapping*; examples are
original. Evidence/currentness (2026-09-24): `NO_TIME_SENSITIVE_CLAIMS`.
