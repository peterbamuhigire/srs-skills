# Retention Management, NGO Donor Tracking, Gantt Chart, and Portfolio Dashboard

## 7.1 Retention Management

**FR-PROJ-062:** For projects of type Construction, when the user configures a Retention Percentage on the project record (FR-PROJ-007), the system shall apply the retention deduction to each project invoice at the time the billing request is sent to the Sales module. The retention amount per invoice shall be computed as:

$$RetentionAmount = InvoiceGross \times \frac{RetentionPct}{100}$$

The system shall pass both the gross invoice amount and the retention deduction amount to the Sales module invoice, which shall display the net payable as:

$$NetPayable = InvoiceGross - RetentionAmount$$

**FR-PROJ-063:** The system shall maintain a running Retention Ledger for each construction project tracking:

- Total Invoiced (gross)
- Total Retention Withheld: $TotalRetentionHeld = \sum RetentionAmount_i$
- Total Retention Released
- Retention Balance Outstanding: $RetentionBalance = TotalRetentionHeld - TotalRetentionReleased$

**FR-PROJ-064:** When the project is marked as Closed and the user initiates retention release, the system shall create a retention release billing request for the full Retention Balance Outstanding, route it to the Sales module for invoice generation, and update the Retention Balance to zero upon invoice confirmation.

**FR-PROJ-065:** The system shall support partial retention release. When a user with `projects.billing` permission specifies a partial release amount (≤ Retention Balance Outstanding), the system shall create a billing request for the specified amount and reduce the Retention Balance accordingly. Any attempt to release more than the Retention Balance shall be rejected with HTTP 422 and the error "Release amount exceeds retention balance."

## 7.2 NGO Donor Project Tracking

**FR-PROJ-066:** For projects of type NGO, the system shall display a Donor & Grant panel on the project detail screen populated from the NGO fields defined in FR-PROJ-007. The panel shall show: Donor Name, Grant Reference, Grant Amount, Total Expenditure to Date, Remaining Grant Balance ($GrantAmount - TotalExpenditure$), and % Utilised.

**FR-PROJ-067:** The system shall allow users to define grant budget lines for an NGO project. Each budget line shall record:

- Budget Line Name (string; required; e.g., "Staff Salaries," "Office Rent," "Field Operations")
- Budget Line Code (string, unique within the project; required)
- Approved Amount (numeric, ≥ 0; required)
- Donor Category (free text; optional — donor-specific category code for reporting)
- Notes (text; optional)

**FR-PROJ-068:** The system shall tag each project cost ledger entry for an NGO project with a grant budget line reference. When a cost is pulled from Procurement, Payroll, or Expenses, the system shall prompt the user to assign the cost to a grant budget line if the target project is of type NGO. Untagged cost entries shall be flagged with `[CONTEXT-GAP: grant budget line not assigned]` on the cost ledger screen.

**FR-PROJ-069:** The system shall generate a Donor Expenditure Report for an NGO project showing for each grant budget line: Approved Amount, Expenditure to Date, Remaining Balance, and % Utilised. The report shall be exportable to Excel (.xlsx) and PDF for donor submission. [CONTEXT-GAP: specific donor reporting template format — confirm whether any donor (e.g., USAID, EU) requires a prescribed format]

**FR-PROJ-070:** The system shall support a Logframe attachment field on the NGO project record. When Logframe Attached = true, the user shall be prompted to upload a PDF or DOCX file. The uploaded file shall be stored with the project record and accessible from the project detail screen.

## 7.3 Gantt Chart View

**FR-PROJ-071:** The system shall render a Gantt chart for each project displaying all WBS tasks as horizontal bars on a timeline. The Gantt chart shall meet the following minimum display requirements:

- Each task bar spans from task Start Date to task Due Date.
- Task completion percentage is represented by a filled portion of the bar, computed as $Completion\% = \frac{ApprovedHours}{EstimatedHours} \times 100$. If Estimated Hours = 0, the bar shall display as empty.
- Milestones are displayed as diamond markers on the timeline at their Due Date.
- Finish-to-Start dependency lines are drawn between linked task bars.
- The timeline axis is zoomable between Day, Week, Month, and Quarter granularity.
- Colour coding distinguishes task status: Not Started (grey), In Progress (blue), Completed (green), Cancelled (strikethrough, light grey), Missed Milestone (red diamond).

**FR-PROJ-072:** The system shall render the Gantt chart for a project with up to 200 tasks in ≤ 3 seconds at P95, measured from the user's request to the chart being fully painted in the browser, under a concurrent load of 30 active sessions on the same tenant.

**FR-PROJ-073:** The system shall allow a user to export the Gantt chart as a PDF. The exported PDF shall preserve the full task list and timeline in landscape orientation, paginated as needed.

## 7.4 Portfolio Dashboard

**FR-PROJ-074:** The system shall provide a Portfolio Dashboard accessible to users with the `projects.portfolio_view` permission. The dashboard shall display all active projects for the tenant in a tabular summary with the following columns:

- Project Name (hyperlinked to project detail)
- Project Type
- Client / Donor / Contracting Entity
- Start Date
- End Date
- Project Manager
- Status
- Budget Utilisation %
- Billing to Date
- P&L (Revenue − Costs)
- Health Indicator

**FR-PROJ-075:** The Health Indicator on the Portfolio Dashboard shall be computed automatically as follows:

- Green: Budget Utilisation < 80% AND no Missed Milestones AND project status Active.
- Amber: Budget Utilisation ≥ 80% AND < 100%, OR 1 or more Missed Milestones, OR project status On Hold.
- Red: Budget Utilisation > 100%, OR project End Date has passed and status is still Active.

**FR-PROJ-076:** The Portfolio Dashboard shall support filtering by: Project Type, Status, Project Manager, Client, and date range (projects active within the range). Filters shall be combinable. The filtered view shall be exportable to Excel (.xlsx).

**FR-PROJ-077:** The system shall provide a Portfolio Summary panel at the top of the Portfolio Dashboard showing aggregate figures across all displayed projects: Total Projects, Total Budget, Total Actual Cost, Total Revenue Recognised, and overall portfolio P&L.
