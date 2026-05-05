# UX Content And Form Quality Gates

## Source Grounding

Derived from local HTML extractions:

- `strategic-writing-for-ux/toc.ncx`, `index_split_000.html` and `index_split_001.html`: user and organisational goals, voice charts, content-first conversation, titles, commands, descriptions, empty states, labels, controls, text inputs, confirmations, notifications, errors, editing, measurement, content operations.
- `web-form-design/toc.ncx`, `index_split_000.html` through `index_split_003.html`: form organisation, path to completion, labels, input fields, actions, help text, errors/success, inline validation, unnecessary inputs, selection-dependent inputs, gradual engagement.
- `articulating-design-decisions/toc.ncx`: decision communication and agreement capture for design reviews.

This file converts those concepts into original SDLC quality gates.

## Content Surface Inventory

| Surface | Required Specification | Failure Signal |
|---|---|---|
| Title/header | User goal and page purpose | User cannot predict task outcome |
| Button/link | Verb-led action and destination/result | User hesitates or clicks wrong action |
| Label | Field meaning in user language | Wrong or inconsistent input |
| Help text | Only appears where it prevents real uncertainty | Users skip it or still fail |
| Empty state | Cause, value, next action | User abandons or calls support |
| Loading state | Progress, wait expectation, safe cancel/retry | Repeat submissions |
| Confirmation | What happened, proof, next step | User doubts completion |
| Notification | Priority, ownership, persistence rule | Important messages missed |
| Error | Cause, correction, preservation of data | Repeated same error |

## Form Field Gate

Each field must pass all checks:

1. The field is necessary for immediate task completion, compliance, fraud control, personalisation, or downstream service delivery.
2. The user can reasonably know the answer at this point.
3. The field label uses the user's vocabulary.
4. The input type matches the expected data.
5. Validation rule and error message are documented.
6. Optional fields are justified or removed.
7. Sensitive fields explain why the data is needed.
8. The field has accessibility labels, keyboard support, and clear focus state.

## Validation Timing Matrix

| Validation Type | Use When | Requirement |
|---|---|---|
| Inline on entry | Formatting can be corrected immediately | Show after enough input exists to judge validity. |
| On blur | Field-level rule can be checked independently | Keep focus movement natural and preserve entered data. |
| On submit | Cross-field or server-side rule is needed | Provide summary and anchor links to fields. |
| Confirmation step | Irreversible, financial, legal, or public-sector submission | Show reviewable data and explicit final action. |

## Error Requirement Pattern

```text
ERR-UX-###: When [condition] prevents [task], the interface shall state [plain-language cause], preserve [user-entered data], focus [recovery target], and provide [next action] within [time/interaction threshold].
```

## Measurement Gate

Define at least 4 measures for major forms:

| Metric | Meaning |
|---|---|
| Completion rate | Percent of started forms submitted successfully. |
| Field correction rate | Percent of users correcting each field after validation. |
| Abandonment stage | Step where users exit before completion. |
| Support contact rate | Support requests per completed or abandoned form. |
| Time to complete | Median and P90 duration from start to success. |
| Accessibility pass rate | WCAG and assistive-tech checks passed. |
| Comprehension score | Users can explain what will happen after submission. |

## Review Gate

Reject the UX content/form spec if:

- buttons use vague text such as "Submit" where the outcome is not obvious
- error text names a rule but not a recovery action
- forms ask for data that is not used in a documented process
- required and optional fields are unclear
- success messages lack proof, next step, or saved-state confirmation
- no metric exists for completion or error recovery

