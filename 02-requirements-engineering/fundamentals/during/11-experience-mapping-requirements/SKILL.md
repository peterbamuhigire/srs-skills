---
name: 11-experience-mapping-requirements
description: Convert stakeholder journeys, customer journeys, employee journeys, ecosystem maps, and future-state experience maps into traceable SDLC requirements. Use when discovery must turn observed touchpoints, pain points, service evidence, emotions, and journey stages into PRD, SRS, backlog, UX, testing, rollout, and governance inputs.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Experience Mapping Requirements

<!-- dual-compat-start -->
## Use When

- A project needs customer journey maps, experience maps, employee journey maps, mental-model diagrams, or ecosystem maps converted into requirements.
- Stakeholder research has touchpoints, pain points, emotions, channels, failures, workarounds, or future-state opportunities that must become SRS or backlog items.
- Public-sector, SaaS, AI, website, mobile, or service-heavy systems need outcome-driven requirements beyond a feature list.

## Do Not Use When

- The task is only to draw a marketing journey map with no SDLC requirement output.
- No stakeholder, user, workflow, or touchpoint evidence exists and discovery cannot be performed.
- A service blueprint with backstage operations is the primary artifact; use `12-service-blueprint-requirements` instead.

## Required Inputs

- Project context from `projects/<ProjectName>/_context/`.
- Stakeholder register, personas, user classes, interview notes, observation notes, analytics, support logs, or service evidence.
- Existing PRD, SRS, story map, backlog, process model, or UX specification when available.

## Workflow

1. Frame the mapping scope: actor, journey boundary, start/end event, channels, outcome, and business goal.
2. Build the current-state map from evidence, not assumptions.
3. Record stages, touchpoints, user actions, thoughts, emotions, channels, systems, evidence, pain points, and opportunities.
4. Convert each high-value opportunity into a requirement candidate with source evidence, affected actor, journey stage, and measurable outcome.
5. Split candidates into functional requirements, NFRs, UX/content requirements, service/support requirements, data requirements, and governance requirements.
6. Add future-state deltas and experiment hypotheses where the correct solution is uncertain.
7. Produce a journey-to-requirements trace matrix and feed downstream skills.
8. Use `references/experience-map-to-requirement-conversion.md` before finalising outputs.

## Quality Standards

- Every requirement must trace to a journey stage, evidence item, actor, and measurable outcome.
- Do not treat emotional lows as vague UX complaints; translate them into observable task, content, feedback, support, or reliability requirements.
- Separate current-state facts from future-state proposals and validation hypotheses.

## Anti-Patterns

- Drawing a polished map without source evidence.
- Converting every pain point into a feature instead of considering process, policy, support, content, or training changes.
- Ignoring employee or backstage impacts when the journey depends on operational work.

## Outputs

- Experience map summary.
- Journey-to-requirements conversion table.
- Requirements backlog candidates with IDs and source evidence.
- Future-state requirements and validation hypotheses.
- Trace handoff to PRD, SRS, UX specification, test planning, and transition planning.

## References

- `references/experience-map-to-requirement-conversion.md`
<!-- dual-compat-end -->

## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/experience_mapping_requirements.md` with:

1. Mapping scope and evidence base.
2. Current-state journey table.
3. Opportunity and failure analysis.
4. Future-state requirement candidates.
5. Journey-to-requirements trace matrix.
6. Validation hypotheses and open research gaps.

