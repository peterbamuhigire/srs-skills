# Scenario Spine and the Requirement Contract

Parent skill: [09-traceability-engineering](../SKILL.md). Also loaded by
`01-prd-generation`, `05-system-overview`, `07-requirements-validation` and
`10-requirements-metrics`. Load it when a PRD, overview or SRS must be built
around a small set of realistic scenarios and every load-bearing requirement
must carry a complete, testable contract and a controlled change path.

## 1. Build from North Star scenarios, not feature lists

1. Select three to seven scenarios that together cover user value, operator
   responsibility and the most costly failure. Each names a real actor, a
   trigger, the state the actor starts in and the outcome that counts as done.
2. Decompose each scenario into use cases, requirements, user flows, data and
   API contracts, explicit non-goals and one prioritised milestone.
3. Walk the scenario again after the flows are validated. When evidence
   exposes a better understanding, change the requirement through change
   control (section 4), not silently in design.

Worked example: "A Mbarara agro-dealer (actor) receives a mobile-money
payment at 18:40 on a Friday while the shop tablet is offline (state). The
sale is recorded locally, reconciled within 5 minutes of reconnection and the
receipt number matches the provider callback (outcome)." That single scenario
yields offline-capture, reconciliation, idempotency and audit requirements
that a feature list ("support mobile money") never surfaces.

## 2. The contract every load-bearing requirement carries

| Field | Rule | Fails when |
|---|---|---|
| Identifier | Stable, never reused, registered in `_registry/identifiers.yaml` | IDs renumbered after a merge |
| Source | Stakeholder, regulation, scenario or decision record | "Best practice" with no owner |
| Rationale | Why the need exists and what breaks without it | Rationale restates the requirement |
| Priority and stability | Ranked, with the volatility expected before release | Everything is "High" |
| Acceptance condition | Deterministic oracle: input, state, observable result, threshold | "Works correctly", "fast", "secure" |
| Verification method | Test, analysis, inspection or demonstration, named | Method left blank |
| Trace links | Up to goal/scenario; down to design, test and evidence | One-way links only |

Classify every statement as fact, assumption, decision, open question or
derived constraint. An assumption without an owner and a validation date is a
risk, not a requirement. A quality word (fast, secure, scalable, reliable) is
incomplete until context, measure, threshold, test method and owner are named.

## 3. Model behaviour, not only features

For each critical flow record: actors, states and transitions, invariants,
data ownership, trust boundaries, dependencies, consistency needs, latency
and availability budgets, failure modes, operator action, rollback and the
signal an operator uses to see it. Where an interface crosses a boundary,
state schema evolution, versioning, idempotency and deprecation expectations
as requirements. Leave the choice of mechanism to design: the SRS states the
guarantee ("a repeated payment callback shall not create a second receipt"),
not the implementation.

## 4. Change control is part of requirement quality

- Baseline approved scope with `python -m engine baseline snapshot`.
- Any change to a baselined FR, NFR or control needs a change-impact entry
  covering requirements, architecture, UX, tests, delivery, cost, operations
  and acceptance evidence, plus a rollback plan.
- Ambiguity found during build returns to the requirement owner; it is never
  resolved by an implementer's guess.
- Use prototypes, scenario walkthroughs and stakeholder review to turn
  unknowns into recorded decisions.

## Quality gate

- Every scenario traces to at least one requirement and one acceptance test.
- Every load-bearing requirement has all seven contract fields.
- No requirement contains a design decision the stakeholders did not mandate.
- Open questions and assumptions carry an owner and due date.

## Anti-patterns

- Scenario written as a persona biography with no trigger or outcome.
  Fix: state actor, trigger, starting state and measurable end state.
- Requirement cites a scenario but no test. Fix: add the oracle and the test ID.
- NFR copied from another project. Fix: derive the threshold from this
  project's scenario and load profile, or mark `[CONTEXT-GAP]`.
- Change absorbed in a pull request. Fix: raise a change-impact entry first.

## Sources and currentness

Independent synthesis of: Hoskins, *The Product-Minded Engineer*; Holt,
*Modern Data Systems*; Nordic APIs, *Identity and APIs*. Requirement
contract fields align with ISO/IEC/IEEE 29148:2018 requirement attributes.
Evidence/currentness (accessed 2026-09-24): ISO/IEC/IEEE 29148:2018 remains
the current edition; a revision (IEEE P29148, PAR approved 2025-09-10; ISO DIS
29148 ed. 2) is in progress (standards.ieee.org; iso.org). Re-check before
citing clause numbers of the new edition. Publication years of the books
above were not re-verified: `NOT_ASSESSED`.
