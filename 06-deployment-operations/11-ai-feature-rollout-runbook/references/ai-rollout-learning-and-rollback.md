<!-- Source basis: Designing for AI early release chapter list and available principles; XP 2026 experimentation; Platform Enterprise early release chapters 1-2. -->

# AI Rollout Learning and Rollback

Use staged exposure: offline -> shadow -> supervised/internal -> named canary ->
limited production -> wider release. Each stage records:

- hypothesis, cohort, consent/notice, owner and observation window;
- primary outcome and safety, human-control, subgroup, accessibility, cost and
  latency guardrails;
- model/prompt/data/config identity and exact artifact;
- promotion, hold, pivot, rollback or stop decision;
- incident, user feedback, drift check and next experiment.

Rollback must disable the affected exposure at the system boundary, preserve
the evidence, notify the incident owner, and define re-promotion criteria. A
manual “we can revert” statement is not rollback evidence; rehearse it against
an action failure and an input/data-shift failure.
