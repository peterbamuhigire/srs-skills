# Project Register

## 2.1 Overview

The Project Register is the master data record for every project within a tenant. It stores the project's identity, classification, financial envelope, client linkage, and lifecycle status. All other Project Management sub-modules (WBS, timesheets, costs, billing) reference the project record as their parent entity.

## 2.2 Project Master Record

**FR-PROJ-001:** When a user with the `projects.create` permission submits the New Project form with all mandatory fields completed, the system shall create a project record and return the user to the project detail screen with a confirmation banner "Project created."

Mandatory fields:

- Project Name (string, 3–200 characters)
- Project Code (string, 3–20 characters, alphanumeric, unique per tenant)
- Project Type (enumeration: Commercial, Construction, NGO, Government)
- Client (lookup to the Sales module client register; required for Commercial and Construction types)
- Start Date (date)
- End Date (date; must be ≥ Start Date)
- Project Manager (lookup to HR employee register)
- Currency (default: tenant functional currency)

**FR-PROJ-002:** When a user submits the New Project form with Project Code already used by an active or archived project in the same tenant, the system shall reject the submission with HTTP 422 and display the inline error "Project Code already exists."

**FR-PROJ-003:** When a user submits the New Project form with End Date earlier than Start Date, the system shall reject the submission with HTTP 422 and display the inline error "End Date must be on or after Start Date."

**FR-PROJ-004:** When a user with the `projects.edit` permission edits a project record in Active status, the system shall allow modification of Project Name, End Date, Project Manager, and Description. The system shall prevent modification of Project Code and Project Type on any project that has posted transactions, and shall return HTTP 422 with the error "Field cannot be changed after transactions have been posted" if attempted via the API.

**FR-PROJ-005:** When a user with the `projects.close` permission sets a project's status to Closed, the system shall require confirmation via a modal dialogue that displays the project's outstanding unbilled costs and open timesheets (if any), and shall record the closing user, closing date, and confirmation timestamp in the project audit log.

**FR-PROJ-006:** The system shall enforce the following project lifecycle states and transitions:

- Draft → Active (on explicit activation by `projects.edit` user)
- Active → On Hold (on hold action by `projects.edit` user)
- On Hold → Active (on resume action by `projects.edit` user)
- Active → Closed (on close action by `projects.close` user)
- Closed → Active (on re-open action by Super Admin only, with mandatory reason)

Any transition not listed above shall be rejected with HTTP 422 and the error "Invalid status transition."

## 2.3 Project Types

**FR-PROJ-007:** The system shall display context-sensitive fields based on project type upon project creation and on the project detail screen.

- Commercial: Client (required), Sales Order reference (optional), Billing Method (T&M or Fixed Price).
- Construction: Client (required), Contract Value (required), Retention Percentage (required, 0–100%), PPDA Contract Reference (optional).
- NGO: Donor Name (required), Grant Reference (required), Grant Amount (required), Logframe Attached (boolean flag).
- Government: Contracting Entity (required), PPDA Contract Reference (required), PPDA Threshold Category (enumeration: Micro, Small, Medium, Large, Restricted Tender, Direct Procurement).

**FR-PROJ-008:** When a user selects Project Type "Government," the system shall display a non-blocking informational banner: "This project type requires PPDA compliance documentation. Ensure all procurement is raised through the Procurement module with PPDA flags enabled."

## 2.4 Budget and Cost Categories

**FR-PROJ-009:** When a project record is saved, the system shall enable the user to define project budget lines by cost category. Each budget line shall record:

- Cost Category (enumeration: Labour, Materials, Subcontractors, Equipment, Travel, Overheads, Other)
- Budgeted Amount (numeric, ≥ 0)
- Notes (optional text)

**FR-PROJ-010:** The system shall calculate and display the Total Project Budget as the sum of all budget line amounts: $TotalBudget = \sum BudgetLine_i$. This total shall update in real time as budget lines are added, edited, or removed.

**FR-PROJ-011:** When actual costs posted against a cost category exceed the budgeted amount for that category, the system shall flag the budget line with a visual indicator (amber for ≥ 80% utilisation, red for > 100% utilisation) on the project budget screen.

**FR-PROJ-012:** The system shall record a full audit trail of all changes to project master records, including field changed, old value, new value, user, and timestamp. The audit history shall be accessible from the project detail screen under an **Audit History** tab.

## 2.5 Client Linkage

**FR-PROJ-013:** When a project of type Commercial or Construction is created, the system shall require the Client field to reference an existing client record in the Sales module. If the referenced client record is deactivated after the project is created, the system shall display a warning banner on the project detail screen: "Client account is inactive. Billing operations may be affected."

**FR-PROJ-014:** The system shall display a **Client Projects** count on the Sales module client detail screen, showing the number of active projects linked to that client, with a drill-down link to the filtered project list.
