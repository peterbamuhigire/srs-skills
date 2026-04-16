# Water-Scrum-Fall Operating Patterns

This reference summarises the three Hybrid patterns described in `docs/hybrid-operating-model.md`. Each pattern is a legitimate configuration of Waterfall governance and Agile execution; choose the one that best matches the project's risk profile.

## Pattern A: Formal Core, Agile Edge

Waterfall requirements govern the stable core (data model, APIs, compliance, security, reporting) while Agile stories deliver the volatile edge (UI flow, onboarding, dashboards, lower-risk enhancements). Baseline items and sprint stories are linked through shared FR-/NFR- identifiers.

- **When to use:** Regulated backends paired with fast-moving user interfaces, or contractually fixed data contracts surrounded by negotiable UX.

## Pattern B: Baseline Then Iterate

A full PRD, core SRS, architecture, and initial test strategy are signed off as a baseline. Execution then shifts into Agile sprints whose Definitions of Ready and Done reference baseline IDs verbatim. Change control routes every deviation back through requirements management.

- **When to use:** Contractual scope baselines with iterative release slicing, or enterprise programs that require up-front approval before execution can begin.

## Pattern C: Release Train with Governance Gates

Agile increments set the delivery cadence, but Phase 05, Phase 06, and Phase 09 gates must pass before any release. The baseline does not freeze every feature — it freezes the audit evidence chain and release-approval criteria.

- **When to use:** Continuous delivery in regulated industries, SAFe-style release trains, or programs where release approval is the primary compliance artifact.

## Source

Derived from `docs/hybrid-operating-model.md` (Recommended Operating Patterns).
