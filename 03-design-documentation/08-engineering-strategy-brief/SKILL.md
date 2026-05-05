---
name: 08-engineering-strategy-brief
description: Produce an engineering strategy brief that connects business goals, product outcomes, architecture diagnosis, guiding policies, operating mechanisms, ADRs, SaaS assumptions, implementation sequencing, and governance. Use before major HLD, infrastructure, platform, AI, SaaS, public-sector, or modernization decisions.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Engineering Strategy Brief

<!-- dual-compat-start -->
## Use When

- A project needs architecture direction before HLD, infrastructure design, ADRs, or delivery planning.
- Multiple plausible technical approaches exist and the team needs diagnosis, policy, trade-offs, and operating mechanisms.
- SaaS, AI, public-sector, enterprise, platform, modernization, or high-scale systems need strategy that ties technology decisions to outcomes.

## Do Not Use When

- The decision is a small local implementation choice that belongs in a normal ADR.
- Product goals, constraints, or quality targets are absent and cannot be discovered.
- The task is only to write detailed component design after strategy is already settled.

## Required Inputs

- Vision, PRD, SRS, business case, quality standards, tech stack, constraints, risks, and current architecture evidence.
- Existing HLD, infrastructure design, ADRs, incident history, cost constraints, team capacity, and SaaS tenancy assumptions when available.

## Workflow

1. State the strategic question and decision altitude.
2. Explore context, precedents, constraints, risks, and stakeholder outcomes.
3. Diagnose the core technical problem and the forces that make it hard.
4. Define guiding policy: principles, constraints, trade-offs, and what the team will not optimise for.
5. Define coherent actions: architecture direction, sequencing, ADR triggers, enabling work, and kill/learn checkpoints.
6. Define operating mechanisms: review cadence, metrics, decision owners, exception handling, and governance linkages.
7. For SaaS/cloud systems, apply `references/saas-architecture-assumptions-and-scaling-checklist.md`.
8. Generate the brief using `references/engineering-strategy-brief-template.md`.

## Quality Standards

- Strategy must contain diagnosis, guiding policy, coherent actions, and operating mechanisms.
- Every policy must constrain future decisions; avoid generic principles that cannot reject an option.
- Link strategy to SRS requirements, quality attributes, risks, ADRs, implementation sequencing, and validation evidence.

## Anti-Patterns

- Writing architecture preference as strategy.
- Choosing technology without naming the business outcome or quality attribute it protects.
- Omitting operating mechanisms, leaving the strategy unenforced after approval.

## Outputs

- Engineering strategy brief.
- ADR candidate list.
- Architecture policy and operating mechanism table.
- Strategy-to-requirements and strategy-to-evidence trace.

## References

- `references/engineering-strategy-brief-template.md`
- `references/saas-architecture-assumptions-and-scaling-checklist.md`
<!-- dual-compat-end -->

## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/Engineering_Strategy_Brief.md` with diagnosis, guiding policy, coherent actions, operating mechanisms, ADR candidates, and evidence gates.

