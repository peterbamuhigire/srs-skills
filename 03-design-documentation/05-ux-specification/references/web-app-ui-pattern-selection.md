# Web App UI Pattern Selection For UX Specifications

This reference is self-contained. It distills the user's supplied Design Studio UI/UX
web-app pattern article into SRS-ready pattern selection rules.

Source used:

- https://www.designstudiouiux.com/blog/web-app-ui-design-patterns/

## Pattern Rule

Every UX specification must justify patterns by user job, data shape, and recovery needs.
Do not specify cards, tabs, modals, dashboards, or AI UI because they are visually common.

## Pattern Matrix

| Screen Need | Required Pattern | SRS Acceptance Criteria |
|---|---|---|
| Compare many records | Data table with sort, filter, selection, pagination, export where needed | User can locate, compare, and act on a record set without losing position. |
| Browse visual items | Cards/grid with consistent media, status, and primary action | Cards expose enough information to choose without opening every record. |
| Long forms | Grouped sections, progressive disclosure, save/resume, inline validation | User can complete required fields, recover errors, and resume interrupted work. |
| Multi-step workflow | Stepper or wizard with progress, review, back, cancel, and draft persistence | User sees progress and can safely move backward without losing data. |
| Detail inspection | Master-detail, split pane, or drawer detail | User keeps list context while inspecting one item. |
| Empty state | Cause, next action, permissions/support route | Empty state explains whether the user lacks data, permission, setup, or filters. |
| Loading state | Skeleton matching final layout | Layout does not jump and user understands that work is ongoing. |
| Error state | Plain-language cause, retry, saved-state note, escalation path | User can recover or escalate without raw technical messages. |
| Notifications | Severity, source, time, action, read state | User can distinguish informational, warning, urgent, and completed events. |
| AI output | Streaming, evidence, confidence/uncertainty, edit/retry, approve/reject | User remains in control before AI output changes records or reaches customers. |

## Pagination Rule

Use pagination for records, search results, transactions, audit logs, approvals, reports,
and anything users may need to bookmark, export, reconcile, or revisit. Infinite scroll
is only acceptable for discovery feeds where there is no known target and no need to
return to an exact position.

## Pattern Register

Add this table to the UX specification when the product has more than five screens.

| Screen / Workflow | User Job | Data Shape | Pattern | State Requirements | Accessibility Notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Accessibility Requirements

For each pattern, specify keyboard behavior, focus order, focus indicator, screen-reader
announcements for async updates, disabled/loading state, reduced-motion behavior, and
mobile touch target sizes.
