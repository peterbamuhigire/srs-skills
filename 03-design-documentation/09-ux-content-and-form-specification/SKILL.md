---
name: 09-ux-content-and-form-specification
description: Use when a UX specification needs testable labels, microcopy, forms, validation, errors, empty states, accessibility and completion measures; use UX specification for journeys and interaction structure, and content strategy for broader editorial work.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# UX Content And Form Specification
<!-- dual-compat-start -->
## Use When

- A user-facing form or workflow needs exact content and validation behaviour before implementation.

## Do Not Use When

- Do not use for visual styling, marketing copy or backend-only validation design.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Approved journey, fields and business rules | UX specification, SRS and domain owners | Required | Stop where a field purpose or rule is unknown. |
| Voice, language and accessibility requirements | Content/design system and user evidence | Required | Label unapproved wording as draft; do not invent legal text. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the UX Content and Form Specification through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the UX Content and Form Specification to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| UX Content and Form Specification | Design, frontend, backend, accessibility and test teams | Every field has purpose, label, input rule, inline error, recovery, accessibility name and completion event; copy is approved or clearly provisional. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified UX Content and Form Specification draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Error can be prevented before submit | Use constraint and inline guidance | Users avoid recoverable failure |
| Rule depends on server state | Preserve input and return a specific recoverable error | Submission failure does not erase work |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Using placeholder text as a label. Fix: provide persistent visible labels.
- Writing `Invalid input`. Fix: state what failed and how to correct it.
- Clearing a form after server error. Fix: preserve safe values and focus the error summary.
- Inventing consent language. Fix: route it to the authorised legal/privacy owner.
- Measuring page views instead of completion. Fix: define start, success, abandonment and error events.

## References

- [Content and form quality gates](references/ux-content-and-form-quality-gates.md)
- [UX Specification neighbour](../05-ux-specification/SKILL.md)
<!-- dual-compat-end -->





## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/UX_Content_And_Form_Specification.md` with content principles, content inventory, form requirements, validation matrix, state copy matrix, accessibility gate, and measurement plan.

