---
name: 09-ux-content-and-form-specification
description: Produce UX content, microcopy, form, validation, error-state, empty-state, accessibility, and completion-metric specifications for web, mobile, SaaS, AI, public-sector, and premium product interfaces. Use when wording, form flow, labels, help text, confirmation, errors, and content quality must become testable requirements.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# UX Content And Form Specification

<!-- dual-compat-start -->
## Use When

- The UX specification needs detailed content, microcopy, form, validation, and error-state requirements.
- A product has onboarding, signup, checkout, application, claim, request, reporting, or public-sector forms.
- Completion rate, accessibility, user trust, error prevention, or premium interface quality matters.

## Do Not Use When

- The interface has no meaningful text, form, validation, notification, or user guidance surface.
- The task is only visual layout; use `05-ux-specification` instead.
- Legal, compliance, or brand content must be approved by humans and no review path exists.

## Required Inputs

- UX specification, user stories/SRS, personas, accessibility constraints, content inventory, existing screens/forms, brand voice, and support/error evidence.
- Form analytics, drop-off data, usability findings, or support tickets where available.

## Workflow

1. Inventory content surfaces: titles, labels, buttons, links, descriptions, empty states, inputs, help, loading, confirmations, notifications, errors, and support text.
2. Define voice and content principles tied to user goals and organisational goals.
3. Specify form structure, labels, fields, actions, help text, validation timing, errors, success states, and unnecessary-input removals.
4. Define accessibility and comprehension gates for every content and form pattern.
5. Define measurement: completion, correction, abandonment, support contact, task success, and content comprehension.
6. Produce implementation-ready content and form requirements using `references/ux-content-and-form-quality-gates.md`.

## Quality Standards

- Every text requirement must help the user move forward, prevent error, recover from error, or understand status.
- Every form field must justify why it is needed, when it is requested, and how the user recovers from invalid input.
- Error states must explain what happened, what to do next, and whether data was saved.

## Anti-Patterns

- Treating microcopy as decorative writing.
- Asking for data before the user has sufficient trust or context.
- Showing validation too early, too late, or without recovery guidance.
- Measuring only clicks and ignoring completion, correction, and support burden.

## Outputs

- UX content and form specification.
- Field inventory and removal candidates.
- Error, empty, loading, confirmation, and notification state matrix.
- Content and form quality gate results.

## References

- `references/ux-content-and-form-quality-gates.md`
<!-- dual-compat-end -->

## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/UX_Content_And_Form_Specification.md` with content principles, content inventory, form requirements, validation matrix, state copy matrix, accessibility gate, and measurement plan.

