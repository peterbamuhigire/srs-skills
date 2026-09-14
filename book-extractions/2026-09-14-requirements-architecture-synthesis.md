# Book-informed requirements and architecture synthesis

Status: adopted on 2026-09-14.

## Practices to standardise

### Use North Star scenarios as the spine

Begin with a small set of realistic scenarios that express user value,
operator responsibility, and failure consequence. Convert each selected
scenario into use cases, requirements, user flows, data/API contracts,
non-goals, and a prioritised milestone. Revisit the scenario after flow
validation; requirements are allowed to change when evidence exposes a better
understanding.

### Make requirements testable and traceable

Every load-bearing requirement should have a stable identifier, source,
rationale, priority, acceptance conditions, and links to design,
implementation, test, and evidence. Distinguish facts, assumptions,
decisions, unresolved questions, and derived constraints. A statement such as
fast, secure, or scalable is incomplete until its context, measure, threshold,
test method, and owner are named.

### Model system behaviour, not only features

For each critical flow, record actors, states, invariants, data ownership,
trust boundaries, dependencies, consistency needs, latency/availability
budgets, failure modes, operator action, rollback, and observability. Prefer
the simplest architecture that satisfies the scenario and its future change
path. Make schema evolution, API versioning, idempotency, and deprecation
explicit where interfaces cross a boundary.

### Change control is part of requirements quality

Baseline the approved scope and record change impact across requirements,
architecture, UX, tests, delivery, cost, operations, and acceptance evidence.
Do not silently absorb ambiguity into implementation. Use prototypes,
scenario walkthroughs, and stakeholder review to turn unknowns into decisions.

## Deliberate exclusions

- Current standards, API security requirements, and platform limits require
  current primary-source verification; the books provide durable concepts only.
- The supplied books do not justify inventing domain requirements, user facts,
  or architecture choices.

## Sources

- Drew Hoskins, The Product-Minded Engineer.
- Aditya Chatterjee, Ue Kiao, Chew Chee Keng and contributors, System Design at
  Google: Engineering Peak for Interviews.
- Daniel R. Holt, Modern Data Systems: Designing Reliable, Scalable, and
  Intelligent Applications.
- Nordic APIs, Identity and APIs: Techniques to Mature Platform Security.
- Ray Rischpater, JavaScript JSON Cookbook.
