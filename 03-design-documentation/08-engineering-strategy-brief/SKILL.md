---
name: 08-engineering-strategy-brief
description: Use when major HLD, platform, SaaS, AI, public-sector or modernisation work needs a concise diagnosis, guiding policies, operating mechanisms, ADR agenda and implementation sequence; use HLD after strategy choices are approved.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# Engineering Strategy Brief
<!-- dual-compat-start -->
## Use When

- Business outcomes and technical constraints require an explicit engineering direction before detailed design.

## Do Not Use When

- Do not use as an HLD, delivery plan or generic technology wish list.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Business goals, product outcomes and architecture evidence | Approved strategy and current-system evidence | Required | Stop if the decision horizon or accountable sponsor is unknown. |
| Constraints, risks and operating capability | Engineering, security and operations owners | Required | Present bounded options when evidence is incomplete. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the Engineering Strategy Brief and ADR agenda through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the Engineering Strategy Brief and ADR agenda to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Engineering Strategy Brief and ADR agenda | Sponsor, architecture and delivery leadership | Diagnosis cites evidence; each policy has an operating mechanism, owner, decision trigger and consequence for HLD sequencing. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified Engineering Strategy Brief and ADR agenda draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Choice is directional and cross-cutting | Set policy and open ADRs | Detailed design shares one direction |
| Choice is local and reversible | Defer to HLD/LLD | Strategy avoids implementation noise |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Listing technologies without diagnosis. Fix: connect each policy to a named constraint.
- Writing goals with no operating mechanism. Fix: name cadence, owner or gate.
- Calling an aspiration a decision. Fix: state chosen direction and rejected alternative.
- Ignoring current-team capability. Fix: include adoption and ownership constraints.
- Turning the brief into a full HLD. Fix: keep component detail downstream.

## References

- [Strategy brief template](references/engineering-strategy-brief-template.md)
- [SaaS architecture assumptions](references/saas-architecture-assumptions-and-scaling-checklist.md)
- [HLD neighbour](../01-high-level-design/SKILL.md)
<!-- dual-compat-end -->





## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/Engineering_Strategy_Brief.md` with diagnosis, guiding policy, coherent actions, operating mechanisms, ADR candidates, and evidence gates.

