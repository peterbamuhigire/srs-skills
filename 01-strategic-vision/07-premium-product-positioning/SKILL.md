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

## Commercial promise translation (Kaizen adoption)

Translate each premium promise into a small evidence record (synthesis): promise, target user and
job, observable product or service behaviour, proof artifact, acceptance procedure, owner, and
review date. Add two challenge rows before approval:

- **Countercase:** name the user, context, failure mode, or lower-cost alternative for which the
  promise may not hold; narrow the claim or add a test.
- **AI alternative:** identify what an AI-generated or AI-assisted substitute could produce, then
  state the human, service, reliability, accessibility, privacy, or governance evidence that must
  still be demonstrated. AI output is not delivery proof by itself.

Link every accepted claim to the [premium requirements gate](references/premium-product-requirements-gate.md)
and retain failed checks as `failed` and unavailable checks as `not assessed`. Use the [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/)
(accessed 2026-09-22) for the applicable accessibility requirements; the link is a source route, not a
claim that the product conforms.

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





## Premium positioning acceptance

Use the five outcome questions as a review lens, not a validated pricing formula.
The project owner defines acceptance criteria before observing results; record
the method, participants, environment, limitations and accountable reviewer.

| Outcome | Project-specific evidence |
|---|---|
| Useful | Target users can explain the benefit and complete a relevant task |
| Easy to use | Agreed first-task and recovery scenarios, including assistance needed |
| Efficient | Task effort/time compared with an appropriate baseline or alternative |
| Appropriate visual experience | Target-buyer interpretation of the authored design, with reasons and disagreement recorded |
| Accessible | Applicable standard/version/level and scoped criteria, manual and automated evidence, unresolved defects and retest |

Do not impose a universal 4/5 aesthetic threshold or infer price acceptance from
passing four or five dimensions. Required task, accessibility or reliability
failures hold the affected release promise; they are not cured by changing a
pricing label. Missing evidence remains NOT_ASSESSED. Buyer willingness to pay
requires separate commercial evidence.

Identify jurisdiction and contractual obligations. WCAG 2.2 is a current W3C
technical reference in this audit; verify the required version and conformance
scope for the engagement. ADA and Section 508 are US-specific legal contexts,
not universal substitutes for local law or proof of accessibility.

Select discovery, research, journeys, information architecture, prototypes,
usability work, visual exploration and operational rehearsal according to the
decision and risk. Record why each activity is needed and its acceptance output.
A maturity label or a count of documents does not establish premium capability.

For visual execution, load the canonical design-system engine and its premium
UI/UX and delivery gates. For websites, load the website premium-product route.
When evidence fails, repair the product or narrow the unsupported promise and
repeat the affected assessment. Retain the original finding and its disposition.
