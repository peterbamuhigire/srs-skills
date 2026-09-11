# Domain Language and Decision Context

Maintain one project glossary/context model as load-bearing project state, not a vocabulary appendix
written after design. Create entries lazily when a term changes a requirement, boundary, rule, data
meaning, interface, test, or stakeholder decision.

## Term record

| Field | Requirement |
| --- | --- |
| Term and aliases | Canonical expression plus observed alternatives |
| Definition | Meaning in this bounded context |
| Context/owner | Where the meaning applies and who confirms it |
| State | proposed, confirmed, disputed, deprecated, or superseded |
| Examples/counterexamples | Instances that expose the boundary |
| Invariants | Rules that must remain true |
| Traces | Requirements, entities, events, ADRs, code, tests, or UI labels using it |
| Review | Effective date, reviewer, and revisit trigger |

Do not force one enterprise-wide meaning when contexts genuinely differ. Qualify the term by context
and define the translation at each seam. A proposed term may guide questions but must not silently
become approved requirement language.

## Decision interaction

Create an ADR only when a consequential option is chosen. Link the ADR to the terms, drivers,
requirements, alternatives, consequences, owner, and supersession condition it affects. When an ADR
changes meaning, update the context model and flag every dependent artefact for review.

## Consistency check

Sample the glossary, requirements, conceptual model, tickets, API/events, code identifiers, tests,
and user-facing labels. Differences are either an intentional context translation with an owner or a
defect. Record both the mismatch and the corrective owner.

This reference adapts the persistent domain-context mechanism studied in Matt Pocock's
`mattpocock/skills` repository at commit `3cca18b` and preserves SRS confirmation and traceability rules.
