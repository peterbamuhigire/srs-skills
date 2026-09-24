# Scenario Quality Rules for Acceptance Criteria

Parent skill: [02-acceptance-criteria](../SKILL.md). Load it when writing or
reviewing Given-When-Then criteria, when criteria must cover non-functional
thresholds, or when test scenarios must stay traceable after delivery.

## 1. Structure rules

| Rule | Pass condition | Tag on failure |
|---|---|---|
| One trigger | Exactly one When per scenario; a second action means a second scenario | `[V&V-FAIL: multiple triggers]` |
| State, not navigation | Givens describe business state ("an invoice of UGX 450,000 is 31 days overdue"), not clicks or screens | `[V&V-FAIL: procedural Given]` |
| Observable outcome | Thens assert an externally observable result (record, message, balance, event), not an internal variable or log line | `[VERIFIABILITY-FAIL: internal assertion]` |
| No implementation | No table names, class names or UI widget types unless they are the contract | `[V&V-FAIL: implementation detail]` |
| Named data class | Each example names the equivalence class it represents (valid, boundary, invalid, empty, maximum) | `[V&V-FAIL: unclassified example]` |

## 2. Coverage per story

Each story carries at least: the main success path, each business-rule
boundary (at, just below, just above), each distinct error response, and a
**Must not** line where security, privacy, tenancy or money is involved.
Replace a long list of similar scenarios with one scenario outline and a
table of examples, one row per data class.

## 3. Collaborative review

Criteria are drafted before build and reviewed by three roles together:
the business owner (is this the rule?), a developer (can this be built as
stated?) and a tester (can this be checked deterministically?). The story is
ready when all three can describe the demonstration that would prove it.
Record who reviewed and when.

## 4. Non-functional criteria as ranges

Quality needs rarely have one correct number. For each performance, capacity
or availability criterion record:

- the **utility point**: below it the feature is not worth releasing;
- the **target**: the level committed for this release;
- the **saturation point**: beyond it users perceive no further benefit;
- the **known barrier**: the level at which the current architecture would
  need significant new investment.

Example: search response at P95 on the Kampala data centre link. Utility
3 s, target 1 s, saturation 0.3 s, barrier 0.5 s (needs a search index).
The acceptance criterion tests the target; the other points guide trade-offs.

## 5. Traceability after delivery

- Every scenario carries its requirement ID and story ID.
- After release, file scenarios under the functional area they describe
  (billing, enrolment, payroll), not under the sprint or ticket. The living
  specification is then readable as system documentation.
- Version control is the audit trail; do not keep parallel spreadsheets.

## 6. Done means outcome checked

A story is done when every scenario passes and, for stories tied to an
impact, the intended behaviour change has a measurement plan with a date
and owner.

## Anti-patterns

- Scenarios that restate the UI script. Fix: rewrite Givens as state.
- A single "happy path" criterion. Fix: add boundary, error and Must not cases.
- Coverage percentage used as the goal. Fix: cover each rule and data class.
- Shared mutable test data across scenarios. Fix: each scenario sets up its
  own state.
- NFR written as "should be fast". Fix: record utility, target, saturation
  and barrier, then test the target.

## Sources and currentness

Independent synthesis informed by Adzic and Evans, *Fifty Quick Ideas to
Improve Your Tests*, and the QUPER quality-requirements model (Regnell and
colleagues); examples are original. Evidence/currentness (2026-09-24):
`NO_TIME_SENSITIVE_CLAIMS`.
