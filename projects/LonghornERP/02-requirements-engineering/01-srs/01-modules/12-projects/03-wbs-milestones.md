# WBS Tasks and Milestones

## 3.1 Overview

The Work Breakdown Structure (WBS) decomposes a project into hierarchical tasks. Milestones mark the completion of significant deliverables and can be linked to billing events. This section specifies the requirements for WBS creation, task dependencies, milestone definition, and milestone billing triggers.

## 3.2 WBS Task Management

**FR-PROJ-015:** When a user with the `projects.edit` permission adds a task to a project's WBS, the system shall create the task record and display it in the WBS list. Each task record shall store:

- Task Name (string, 2–200 characters, required)
- Parent Task (lookup to existing task within the same project; null for root-level tasks)
- Assigned To (lookup to HR employee; optional at creation)
- Start Date (date; optional)
- Due Date (date; must be ≥ Start Date if both are provided)
- Estimated Hours (numeric, ≥ 0; optional)
- Status (enumeration: Not Started, In Progress, Completed, Cancelled; default: Not Started)
- Description (text; optional)

**FR-PROJ-016:** The system shall support a maximum of 4 levels of task nesting within a WBS (root → sub-task → sub-sub-task → leaf task). Any attempt to create a task at a 5th nesting level shall be rejected with HTTP 422 and the error "Maximum WBS depth of 4 levels exceeded."

**FR-PROJ-017:** When a user marks a parent task as Completed, the system shall verify that all child tasks within that parent have a status of Completed or Cancelled. If any child task has status Not Started or In Progress, the system shall display a modal warning: "N child task(s) are not yet complete. Mark parent complete anyway?" The user must confirm to proceed.

**FR-PROJ-018:** When a user marks a task as Cancelled, the system shall set all timesheet lines that reference this task and have status Draft to Cancelled, and shall display a count: "N timesheet line(s) have been cancelled."

**FR-PROJ-019:** When a user with `projects.edit` permission reorders WBS tasks via drag-and-drop or explicit sequence update, the system shall persist the new sort order and display tasks in the updated order on all subsequent page loads and exports.

## 3.3 Task Dependencies

**FR-PROJ-020:** The system shall allow users to define Finish-to-Start dependencies between WBS tasks within the same project. A dependency record shall store the predecessor task and the successor task. Circular dependencies (Task A → Task B → Task A) shall be rejected with HTTP 422 and the error "Circular dependency detected."

**FR-PROJ-021:** When a predecessor task's Due Date is extended to a date later than the successor task's Start Date, the system shall display an inline warning on the successor task: "Start Date conflicts with predecessor due date." The system shall not block saving but shall log the conflict in the project health indicators.

## 3.4 Milestone Definition

**FR-PROJ-022:** When a user with `projects.edit` permission creates a milestone on a project, the system shall create the milestone record and link it to the project. Each milestone record shall store:

- Milestone Name (string, 2–200 characters, required)
- Due Date (date, required)
- Description (text; optional)
- Billing Milestone (boolean; default: false)
- Billing Amount (numeric, ≥ 0; required when Billing Milestone = true)
- Status (enumeration: Pending, Achieved, Missed; default: Pending)
- Linked WBS Tasks (multi-select lookup to tasks within the same project; optional)

**FR-PROJ-023:** When a user marks a milestone's Status as Achieved and Billing Milestone = true, the system shall:

1. Create a billing event record linked to the milestone.
2. Display a prompt: "This milestone is billable. Generate invoice now or queue for next billing run?"
3. If the user selects "Generate invoice now," initiate the billing workflow per FR-PROJ-043.
4. If the user selects "Queue," set the billing event status to Queued and include it in the next billing run.

**FR-PROJ-024:** When a milestone Due Date passes without its Status being set to Achieved, the system shall automatically set the milestone Status to Missed and shall create a project health alert visible on the project detail screen and the portfolio dashboard.

**FR-PROJ-025:** The system shall display a milestone timeline on the project detail screen, ordered chronologically by Due Date, showing the milestone name, due date, status (with colour coding: Pending = grey, Achieved = green, Missed = red), and billing amount (if applicable).
