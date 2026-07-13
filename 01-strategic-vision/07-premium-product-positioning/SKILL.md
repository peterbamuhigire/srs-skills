---
name: 07-premium-product-positioning
description: Use when a commercial product, client-facing system, SaaS, app or executive workflow must justify premium pricing through buyer trust, proof, service quality and materially better experience; use vision-statement for broad direction and UX specification for interface detail.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# Premium Product Positioning
<!-- dual-compat-start -->
## Use When

- Premium buyers, enterprise decision-makers or high-value users require explicit value, proof and experience requirements.

## Do Not Use When

- Do not use to decorate a commodity offer or invent prestige claims unsupported by delivery capability.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Target buyer, buying context and alternatives | Approved research and commercial owner | Required | Stop if the buyer or premium alternative is undefined. |
| Proof, service and experience evidence | Delivery, sales and customer evidence | Required | Qualify missing proof and exclude fabricated claims. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the Premium positioning requirements and gate result through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the Premium positioning requirements and gate result to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Premium positioning requirements and gate result | PRD, SRS, UX, sales and proposal authors | Each premium claim maps to buyer evidence, product requirement, service promise or measurable experience standard. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified Premium positioning requirements and gate result draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Premium value is observable and supportable | Encode it in requirements and proof | Pricing has credible justification |
| Claim exceeds evidence or service capacity | Narrow or remove the claim | Prestige language creates trust debt |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Replacing value with luxury adjectives. Fix: name the buyer outcome and proof.
- Copying mass-market feature parity into a premium package. Fix: specify differentiated service or decision quality.
- Inventing testimonials or logos. Fix: use verified buyer evidence only.
- Treating visual polish as the whole premium experience. Fix: include reliability, onboarding, support and reporting.
- Promising white-glove service without capacity. Fix: define service level, owner and operating limit.

## References

- [Premium requirements gate](references/premium-product-requirements-gate.md)
- [UX specification neighbour](../../03-design-documentation/05-ux-specification/SKILL.md)
<!-- dual-compat-end -->





## Premium positioning gate (added 2026-05-04 from Synechron Enterprise UX)

Canonical reference: `docs/ux-foundations.md` Section 3 (5 outcomes + 5-level UX maturity).

Premium-pricing claims must pass two gates: outcomes (launch gate) and maturity (process gate). Both are required; neither alone is sufficient.

### Gate 1 — Five Outcomes (launch gate)

A premium positioning document must declare evidence-based pass on ALL FIVE outcomes:

| Outcome | Evidence required |
|---|---|
| **Useful** | Persona-validated; tested against documented goals |
| **Easy to use** | First-task success in usability test without coaching |
| **Efficient** | Task time benchmarked against competitor or prior baseline |
| **Pleasing** | Subjective rating ≥ 4/5 on initial-impression test |
| **Accessible** | ADA / Section 508 / WCAG 2.1 AA verified |

**4-of-5 disqualifies premium pricing.** Drop the positioning to standard tier and re-engage when the missing outcome has evidence.

### Gate 2 — UX Maturity Level (process gate)

A premium claim must operate at UX Maturity Level 3 (UX Design) minimum. Top-tier (luxury, regulated, mission-critical) requires Level 4 (Experience Design).

Required documented activities at Level 3:
- Problem definition + business objective
- Stakeholder discussions (interview notes)
- Success criteria (signed)
- User research (qualitative + quantitative)
- Competitor analysis matrix
- Personas (named, with goals + pain points)
- User journeys (per primary persona)
- Information architecture (sitemap + navigation flow)
- Wireframes (low-fi + high-fi)
- Clickable prototype (per crucial scenarios)
- Heuristic evaluation report
- Visual design mockups
- ADA / Section 508 verification

Level 4 additionally requires: experience maps, mood boards, usability testing, test cases & scenarios.

### Cross-engine references

- Website engine `design-quality-score` — Category 8 (UX Maturity) scores the same gate independently per artefact. Same project may carry separate scores in each engine.
- Website engine `premium-ui-ux-design` reference `enterprise-five-outcomes.md` — same outcomes, applied to website templates.

### Procedure when either gate fails

Do not re-position the product as premium. Either:
1. Close the gap (add the missing evidence or activities) and re-engage, OR
2. Re-position at a lower tier (standard / mid-tier) honestly

Premium claims that fail either gate damage credibility on first audit.
