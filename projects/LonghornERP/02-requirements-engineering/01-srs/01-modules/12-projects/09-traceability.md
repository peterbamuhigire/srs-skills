# Traceability Matrix — Project Management Module

## 9.1 Overview

This matrix maps every functional requirement in this SRS to at least 1 business goal defined in Section 1.6, and records the IEEE 830 verifiability criterion (the deterministic test oracle) for each requirement. All FRs without a mapping to a business goal are flagged `[TRACE-GAP]`.

## 9.2 Business Goal Reference

| ID | Business Goal |
|---|---|
| BG-PROJ-001 | Unified project planning and tracking, eliminating disconnected spreadsheets |
| BG-PROJ-002 | Real-time project P&L by aggregating costs from Procurement, Payroll, and Expenses |
| BG-PROJ-003 | Sector-specific compliance: PPDA for government, retention for construction, donor logframe for NGOs |
| BG-PROJ-004 | Automated milestone and T&M billing to reduce billing lag and improve cash collection |
| BG-PROJ-005 | Portfolio-level visibility across all projects by budget health, schedule status, and profitability |

## 9.3 Traceability Matrix

| FR ID | Section | Description Summary | Business Goal(s) | Test Oracle |
|---|---|---|---|---|
| FR-PROJ-001 | 2.2 | Create project master record with mandatory fields | BG-PROJ-001 | Submit valid form; verify project appears in project list with correct fields and status Draft. |
| FR-PROJ-002 | 2.2 | Reject duplicate Project Code | BG-PROJ-001 | Submit form with existing project code; verify HTTP 422 and error message. |
| FR-PROJ-003 | 2.2 | Reject End Date earlier than Start Date | BG-PROJ-001 | Submit form with End Date < Start Date; verify HTTP 422 and inline error. |
| FR-PROJ-004 | 2.2 | Restrict field edits after transactions are posted | BG-PROJ-001 | Attempt Project Code edit on project with posted transactions via API; verify HTTP 422. |
| FR-PROJ-005 | 2.2 | Close project with outstanding items confirmation modal | BG-PROJ-001 | Close project with open timesheets; verify modal displays outstanding count before confirming. |
| FR-PROJ-006 | 2.2 | Enforce project lifecycle state transitions | BG-PROJ-001 | Attempt invalid transition (e.g., Draft → Closed); verify HTTP 422. |
| FR-PROJ-007 | 2.3 | Display context-sensitive fields by project type | BG-PROJ-001, BG-PROJ-003 | Select project type Construction; verify Retention Percentage field appears and is required. |
| FR-PROJ-008 | 2.3 | Display PPDA informational banner for Government projects | BG-PROJ-003 | Select type Government; verify informational banner is displayed on project screen. |
| FR-PROJ-009 | 2.4 | Define project budget lines by cost category | BG-PROJ-002 | Add 3 budget lines; verify all 3 stored with correct amounts and categories. |
| FR-PROJ-010 | 2.4 | Compute and display total project budget in real time | BG-PROJ-002 | Add budget line of 1,000,000; verify total updates immediately on screen. |
| FR-PROJ-011 | 2.4 | Visual budget utilisation indicator (amber/red) | BG-PROJ-002, BG-PROJ-005 | Post costs reaching 85% of Labour budget; verify amber indicator on budget line. |
| FR-PROJ-012 | 2.4 | Full audit trail on project master record changes | BG-PROJ-001 | Edit project name; verify audit log entry with old value, new value, user, timestamp. |
| FR-PROJ-013 | 2.5 | Require active client for Commercial/Construction projects | BG-PROJ-001 | Deactivate client linked to active project; verify warning banner on project detail screen. |
| FR-PROJ-014 | 2.5 | Display Client Projects count on Sales client record | BG-PROJ-001 | Create 2 projects linked to same client; verify count = 2 on client detail screen. |
| FR-PROJ-015 | 3.2 | Create WBS task with mandatory fields | BG-PROJ-001 | Submit valid task form; verify task appears in WBS list with status Not Started. |
| FR-PROJ-016 | 3.2 | Enforce maximum 4 levels of WBS nesting | BG-PROJ-001 | Attempt creation of task at 5th nesting level; verify HTTP 422 with depth error. |
| FR-PROJ-017 | 3.2 | Warn when marking parent task complete with incomplete children | BG-PROJ-001 | Mark parent complete with 2 In Progress children; verify modal warning showing count. |
| FR-PROJ-018 | 3.2 | Cancel draft timesheets on task cancellation | BG-PROJ-001 | Cancel task with 3 Draft timesheet lines; verify all 3 lines set to Cancelled. |
| FR-PROJ-019 | 3.2 | Persist WBS task sort order after reorder | BG-PROJ-001 | Reorder tasks; reload page; verify tasks appear in new order. |
| FR-PROJ-020 | 3.3 | Define Finish-to-Start dependencies; reject circular dependencies | BG-PROJ-001 | Create A → B → A dependency chain; verify HTTP 422 with circular dependency error. |
| FR-PROJ-021 | 3.3 | Warn on predecessor/successor date conflict | BG-PROJ-001 | Extend predecessor Due Date past successor Start Date; verify inline warning on successor. |
| FR-PROJ-022 | 3.4 | Create milestone with required fields | BG-PROJ-001 | Submit milestone form with Billing Milestone = true and no Billing Amount; verify validation error. |
| FR-PROJ-023 | 3.4 | Trigger billing workflow on milestone achievement | BG-PROJ-004 | Mark billing milestone as Achieved; verify prompt to generate invoice is displayed. |
| FR-PROJ-024 | 3.4 | Auto-set milestone to Missed when Due Date passes | BG-PROJ-001, BG-PROJ-005 | Allow milestone Due Date to pass without achievement; verify status changes to Missed and health alert created. |
| FR-PROJ-025 | 3.4 | Display chronological milestone timeline | BG-PROJ-001 | Navigate to project detail; verify milestones listed in Due Date order with correct status colours. |
| FR-PROJ-026 | 4.2 | Create timesheet line with mandatory fields | BG-PROJ-001 | Submit valid timesheet line; verify record created with status Submitted. |
| FR-PROJ-027 | 4.2 | Reject timesheet lines exceeding 24 hours per day | BG-PROJ-001 | Submit line that takes daily total to 25 hours; verify HTTP 422 with daily limit error. |
| FR-PROJ-028 | 4.2 | Reject timesheet entry against Closed/Cancelled project | BG-PROJ-001 | Submit timesheet against closed project; verify HTTP 422 with project status error. |
| FR-PROJ-029 | 4.2 | Display weekly timesheet grid view | BG-PROJ-001 | Navigate to timesheet screen; verify 7-day grid with project/task rows and day columns. |
| FR-PROJ-030 | 4.3 | Route submitted timesheets to Project Manager for approval | BG-PROJ-001 | Submit timesheet line; verify Project Manager receives approval notification. |
| FR-PROJ-031 | 4.3 | Set timesheet line to Approved on Project Manager approval | BG-PROJ-002 | Approve timesheet line as Project Manager; verify status changes to Approved and line appears in cost aggregation. |
| FR-PROJ-032 | 4.3 | Reject timesheet line with mandatory reason; notify employee | BG-PROJ-001 | Reject timesheet line with reason; verify employee receives notification with reason text. |
| FR-PROJ-033 | 4.3 | Lock Draft timesheets at period end | BG-PROJ-001 | Advance period end date; verify Draft lines change to Pending Submission. |
| FR-PROJ-034 | 4.4 | Maintain employee billing rate records with effective dates | BG-PROJ-004 | Create billing rate with Effective From 2026-01-01; verify rate applies to timesheet lines dated ≥ 2026-01-01. |
| FR-PROJ-035 | 4.4 | Apply effective-date billing rate; flag missing rates | BG-PROJ-004 | Submit timesheet for date with no billing rate; verify [CONTEXT-GAP] flag and line excluded from billing. |
| FR-PROJ-036 | 4.4 | Project-level billing rate override per employee | BG-PROJ-004 | Set override rate on project; verify T&M billing uses override rate, not standard rate. |
| FR-PROJ-037 | 4.5 | Create resource allocation record with required fields | BG-PROJ-001 | Add employee allocation to project; verify record appears in project Team view. |
| FR-PROJ-038 | 4.5 | Display resource utilisation summary with % | BG-PROJ-005 | Log 40 hours against 80 planned hours; verify utilisation = 50%. |
| FR-PROJ-039 | 4.5 | Flag overlapping project allocations | BG-PROJ-005 | Allocate employee to 2 projects with overlapping date ranges; verify overlap indicator on allocation record. |
| FR-PROJ-040 | 4.6 | Resource Utilisation Report with filters and export | BG-PROJ-005 | Filter report by department; verify only that department's employees appear. Export; verify .xlsx file. |
| FR-PROJ-041 | 5.2 | Aggregate project costs from 3 source modules | BG-PROJ-002 | Approve PO, payroll timesheet, and expense claim tagged to project; verify all 3 appear in cost ledger. |
| FR-PROJ-042 | 5.2 | Reverse cost ledger entry on source document reversal | BG-PROJ-002 | Reverse PO payment; verify corresponding cost ledger entry reversed within 60 seconds. |
| FR-PROJ-043 | 5.2 | Display project cost summary by category with utilisation | BG-PROJ-002 | View cost summary; verify Budgeted, Actual, Committed, Remaining, and Utilisation% columns per category. |
| FR-PROJ-044 | 5.3 | Compute T&M billing from approved billable timesheets | BG-PROJ-004 | Initiate T&M billing run; verify billing = sum of (hours × rate) for all approved billable lines. |
| FR-PROJ-045 | 5.3 | Send confirmed T&M billing to Sales as draft invoice; mark timesheets Billed | BG-PROJ-004 | Confirm billing run; verify draft invoice created in Sales and all included lines show status Billed. |
| FR-PROJ-046 | 5.3 | Prevent double-billing of timesheet lines | BG-PROJ-004 | Initiate second billing run; verify already-billed lines are excluded with exclusion count shown. |
| FR-PROJ-047 | 5.4 | Generate milestone invoice on billing milestone achievement | BG-PROJ-004 | Achieve billing milestone and select "Generate invoice now"; verify draft invoice in Sales with milestone name as line item. |
| FR-PROJ-048 | 5.4 | Display Billing Schedule with invoice references | BG-PROJ-004 | Navigate to project Billing Schedule; verify all billing milestones listed with status and invoice hyperlinks. |
| FR-PROJ-049 | 5.5 | Compute Project P&L: Revenue − Costs | BG-PROJ-002 | Post known revenue and costs; verify P&L = Revenue − Total Costs for known test values. |
| FR-PROJ-050 | 5.5 | Display structured P&L with gross margin % | BG-PROJ-002 | View P&L screen; verify all rows present including Gross Margin % calculated correctly. |
| FR-PROJ-051 | 5.5 | Auto-refresh Project P&L on new cost/invoice/reversal | BG-PROJ-002 | Post new cost entry; verify P&L updates and timestamp refreshes within ≤ 5 seconds. |
| FR-PROJ-052 | 5.5 | Export Project P&L to Excel and PDF | BG-PROJ-002 | Export P&L; verify .xlsx and PDF files with project header, all rows, and correct amounts. |
| FR-PROJ-053 | 6.2 | Create project subcontractor record with required fields | BG-PROJ-001, BG-PROJ-003 | Add subcontractor to Government project without Contract Reference; verify field is required. |
| FR-PROJ-054 | 6.2 | Compute total subcontract value | BG-PROJ-002 | Add 2 subcontractor records; verify total = sum of both subcontract values. |
| FR-PROJ-055 | 6.3 | Link PO to subcontractor; enforce supplier match | BG-PROJ-003 | Link PO from different supplier; verify HTTP 422 with supplier mismatch error. |
| FR-PROJ-056 | 6.3 | Display subcontractor cost summary with paid/outstanding | BG-PROJ-002 | Record partial payment; verify Paid to Date and Outstanding Balance update correctly. |
| FR-PROJ-057 | 6.4 | Auto-update subcontractor Paid to Date on payment confirmation | BG-PROJ-002 | Confirm PO payment; verify subcontractor Paid to Date updates within 60 seconds. |
| FR-PROJ-058 | 6.4 | Warn when payments reach subcontract ceiling | BG-PROJ-003 | Post payments equalling subcontract value; verify ceiling warning banner displayed. |
| FR-PROJ-059 | 6.5 | Display PPDA compliance warning for Government project subcontractors | BG-PROJ-003 | Add subcontractor to Government project without PPDA Compliant flag; verify warning banner. |
| FR-PROJ-060 | 6.5 | Allow document attachments on subcontractor records | BG-PROJ-003 | Upload 25 MB PDF; verify rejection. Upload 15 MB PDF; verify successful upload with description and timestamp. |
| FR-PROJ-061 | 6.5 | Generate Subcontractor Compliance Report | BG-PROJ-003 | Generate report for Government project; verify all subcontractors listed with PPDA status. Export; verify PDF and Excel files. |
| FR-PROJ-062 | 7.1 | Compute and deduct retention per invoice | BG-PROJ-003 | Create construction project with 10% retention; generate invoice of 1,000,000; verify Net Payable = 900,000. |
| FR-PROJ-063 | 7.1 | Maintain running Retention Ledger | BG-PROJ-003 | Issue 3 invoices; verify Total Retention Held = sum of all retention deductions. |
| FR-PROJ-064 | 7.1 | Release full retention on project close | BG-PROJ-003, BG-PROJ-004 | Close project; initiate retention release; verify billing request for full Retention Balance Outstanding created. |
| FR-PROJ-065 | 7.1 | Support partial retention release | BG-PROJ-003, BG-PROJ-004 | Release partial amount ≤ balance; verify balance reduces. Attempt to release more than balance; verify HTTP 422. |
| FR-PROJ-066 | 7.2 | Display Donor & Grant panel with utilisation on NGO project | BG-PROJ-003 | Navigate to NGO project; verify grant panel shows all fields including Remaining Grant Balance. |
| FR-PROJ-067 | 7.2 | Define grant budget lines per NGO project | BG-PROJ-003 | Add 3 grant budget lines; verify all stored with unique Budget Line Codes. |
| FR-PROJ-068 | 7.2 | Tag project cost entries with grant budget line | BG-PROJ-003 | Pull cost into NGO project without tagging a budget line; verify [CONTEXT-GAP] flag on cost entry. |
| FR-PROJ-069 | 7.2 | Generate Donor Expenditure Report | BG-PROJ-003 | Generate report; verify all budget lines with Approved Amount, Expenditure, Remaining Balance, % Utilised. |
| FR-PROJ-070 | 7.2 | Support logframe document upload on NGO project | BG-PROJ-003 | Set Logframe Attached = true; verify upload prompt. Upload valid PDF; verify file stored and accessible. |
| FR-PROJ-071 | 7.3 | Render Gantt chart with tasks, milestones, dependencies | BG-PROJ-001 | Navigate to Gantt view; verify task bars span correct dates, milestones show as diamonds, dependency lines drawn. |
| FR-PROJ-072 | 7.3 | Gantt chart renders ≤ 3 seconds for 200-task project | BG-PROJ-001 | Load Gantt for project with exactly 200 tasks under 30-session load; verify render time ≤ 3 seconds at P95. |
| FR-PROJ-073 | 7.3 | Export Gantt chart to PDF | BG-PROJ-001 | Export Gantt; verify PDF in landscape orientation with all tasks and timeline visible. |
| FR-PROJ-074 | 7.4 | Display Portfolio Dashboard with all active projects | BG-PROJ-005 | Navigate to Portfolio Dashboard as user with portfolio_view permission; verify all active tenant projects listed. |
| FR-PROJ-075 | 7.4 | Compute portfolio Health Indicator per defined rules | BG-PROJ-005 | Set project budget utilisation to 105%; verify Health Indicator = Red. |
| FR-PROJ-076 | 7.4 | Filter Portfolio Dashboard and export | BG-PROJ-005 | Filter by Project Type = NGO; verify only NGO projects shown. Export; verify .xlsx file. |
| FR-PROJ-077 | 7.4 | Display Portfolio Summary aggregate figures | BG-PROJ-005 | View Portfolio Dashboard; verify Total Projects, Total Budget, Total Revenue, and P&L summary panel present. |

## 9.4 Context Gaps

The following gaps were identified during requirements authoring. Each gap must be resolved before Phase 1 sign-off.

- `[CONTEXT-GAP: grant budget line not assigned]` — NGO project cost tagging requirement (FR-PROJ-068) flags untagged entries at runtime. The specific donor reporting template format for common donors (USAID, EU, GIZ) is unconfirmed; see FR-PROJ-069.
- `[CONTEXT-GAP: PPDA eTendering integration scope]` — The depth of PPDA integration (workflow flags vs. full eTendering API) is deferred to the FR-INTG series. FR-PROJ-059 and FR-PROJ-061 implement compliance flags only.
- `[CONTEXT-GAP: expense claims module]` — FR-PROJ-041 references an expense claims module as a cost source. No SRS for an Expenses module exists at the time of writing. This dependency must be resolved before cost aggregation from expense claims can be implemented.
- `[CONTEXT-GAP: timesheet period lock automation]` — FR-PROJ-033 requires an automated period-end lock mechanism. The scheduling infrastructure (cron job vs. event-driven) for this automation is not defined in this SRS and must be specified in the platform architecture document.
