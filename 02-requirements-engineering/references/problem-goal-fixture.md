# Problem-to-goal fixture

Use this synthetic fixture before a requirement is accepted into a baseline. It
keeps the user outcome separate from a proposed solution and leaves an
inspectable trace from the problem to the goal and its measure.

## Source and currentness

This reference is an independent synthesis of the B10-A01 action card. The
book-derived input supplies a durable elicitation pattern; it is not authority
for a project fact, policy, clinical rule, or current standard. `NO_TIME_SENSITIVE_CLAIMS`
is admitted for this reference. Project evidence, the decision owner, and the
review date remain required inputs.

## Contract

| Field | Required content | Failure status |
| --- | --- | --- |
| `fixture_id` | Stable identifier for the case | `NOT_ASSESSED` if absent |
| `request_type` | Outcome/problem, goal, or solution proposal | `BLOCKED` for solution-only input |
| `actor_event` | Actor and observable trigger | `BLOCKED` if the trigger is vague |
| `problem` | Current user or business difficulty, with evidence source | `NOT_ASSESSED` if unsupported |
| `purpose` | Change the actor needs to achieve | `BLOCKED` if it names only a feature |
| `advantage` | Expected value if the purpose is met | `NOT_ASSESSED` if it is an unmeasured claim |
| `measure` | Observable unit, baseline, target, and review window | `BLOCKED` if no oracle can be defined |
| `domain_invariant` | Rule that must remain true | `BLOCKED` when omitted for a controlled flow |
| `missing_capability` | Gap between current and desired behaviour | `NOT_ASSESSED` if inferred without evidence |
| `prior_behaviour` | Existing path and its known exception | `NOT_ASSESSED` if not observed or supplied |
| `expected_improvement` | Bounded change linked to the measure | `NOT_ASSESSED` if it is only an adjective |
| `trace_links` | Goal, requirement, test or review identifiers | `BLOCKED` if the requirement is baselined without links |
| `unknowns_and_rights` | Unknown facts, data scope, and decision rights | `BLOCKED` when the scope affects protected data |
| `acceptance_oracle` | Deterministic test or named human review | `BLOCKED` when no result can be checked |

## Valid fixture

```yaml
fixture_id: PG-001
request_type: outcome-problem
actor_event: support analyst receives a duplicate service request
problem: duplicate requests are manually merged and the original owner is lost
purpose: preserve ownership while preventing duplicate work
advantage: one accountable queue item remains visible to the requester
measure:
  unit: percentage of duplicate pairs retaining the original owner
  baseline: to be measured from the approved sample
  target: 100% in the pilot sample
  review_window: named pilot period
domain_invariant: every active request has one accountable owner
missing_capability: duplicate detection does not preserve the source owner
prior_behaviour: analyst merges records manually; merge evidence is inconsistent
expected_improvement: the merge records source id, target id, owner, timestamp, and reason
trace_links: [GOAL-001, REQ-001, TEST-001]
unknowns_and_rights: project owner confirms data scope and merge authority
acceptance_oracle: replay TEST-001 and inspect the merge evidence record
status: ready-for-review
```

## Failure fixtures

| Input | Expected result | Why it cannot pass |
| --- | --- | --- |
| `request_type: solution` and `purpose: add a duplicate button` | `BLOCKED` | A feature name does not state the outcome, measure, or invariant. |
| A goal with `measure: faster` | `BLOCKED` | Unit, baseline, target, and review window are missing. |
| A protected-data flow with no `unknowns_and_rights` | `BLOCKED` | Scope and decision authority are unresolved. |
| A requirement with no `trace_links` | `BLOCKED` at baseline | Reviewers cannot replay the source-to-test chain. |

## Review record

The reviewer records `fixture_id`, sources inspected, decision owner,
`pass`, `fail`, or `NOT_ASSESSED`, the failed field (if any), and the next
evidence needed. A valid fixture proves fit for review; it does not approve a
requirement or certify a live system.

