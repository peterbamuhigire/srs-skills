# Project Costs, Billing, and P&L

## 5.1 Overview

This section specifies requirements for aggregating costs from multiple source modules (Procurement POs, HR/Payroll timesheets, and expense claims) into a unified project cost view, generating project invoices via T&M and milestone billing methods, and computing the project Profit and Loss statement.

## 5.2 Cost Aggregation

**FR-PROJ-041:** The system shall aggregate actual project costs from 3 source modules into the project cost ledger:

1. **Procurement costs:** Approved PO lines tagged with a `project_id` matching this project shall be pulled into the cost ledger with cost category "Materials" or the category assigned on the PO line.
2. **Payroll timesheet costs:** Approved timesheet lines for this project shall be costed at the employee's cost rate (internal cost per hour, sourced from HR payroll) and posted with cost category "Labour."
3. **Expense claims:** Approved expense claim lines tagged to this project shall be pulled with their expense category mapped to the nearest project cost category.

**FR-PROJ-042:** When a source module document (PO, payroll run, or expense claim) is reversed or cancelled after its costs have been pulled into the project cost ledger, the system shall automatically reverse the corresponding cost ledger entry and update the project's total actual cost within 60 seconds of the source reversal being confirmed.

**FR-PROJ-043:** The system shall display the project cost summary in a table grouped by cost category, showing for each category: Budgeted Amount, Actual Cost to Date, Committed Cost (approved but not yet paid POs), Remaining Budget, and Budget Utilisation %. Formulae:

$$ActualCost_{total} = \sum_{i} ActualCost_i$$

$$RemainingBudget = BudgetedAmount - ActualCost_{total} - CommittedCost$$

$$BudgetUtilisation\% = \frac{ActualCost_{total} + CommittedCost}{BudgetedAmount} \times 100$$

## 5.3 Time-and-Materials Billing

**FR-PROJ-044:** When a user with `projects.billing` permission initiates a T&M billing run for a project, the system shall:

1. Retrieve all Approved timesheet lines for the project with Billable = true and status not yet billed.
2. Apply the applicable billing rate per employee per timesheet date (per FR-PROJ-035 and FR-PROJ-036).
3. Compute the billing amount: $TnMBilling = \sum_{i} (Hours_i \times Rate_i)$
4. Present a preview invoice showing each timesheet line as a line item with employee name, date, task, hours, rate, and amount.
5. Allow the user to exclude individual lines from the billing run before confirming.

**FR-PROJ-045:** When the user confirms the T&M billing preview, the system shall:

1. Create a billing request record with status Pending Invoice.
2. Send the billing request to the Sales module to generate a draft invoice.
3. Mark all included timesheet lines as status Billed, recording the invoice reference.
4. Return the user to the project billing screen with a confirmation banner showing the invoice draft reference.

**FR-PROJ-046:** The system shall prevent the same timesheet line from being included in 2 billing runs. Any attempt to include an already-billed timesheet line in a new billing run shall be silently excluded from the run, with the excluded count displayed in the billing preview summary.

## 5.4 Milestone Billing

**FR-PROJ-047:** When the user selects "Generate invoice now" at milestone achievement (per FR-PROJ-023), the system shall create a billing request record for the milestone amount, send it to the Sales module to generate a draft invoice with the milestone name as the line item description, and mark the milestone billing event as status Invoiced, recording the invoice reference.

**FR-PROJ-048:** The system shall display a **Billing Schedule** view on the project detail screen listing all billing milestones in chronological order with columns: Milestone Name, Due Date, Billing Amount, Status (Pending, Invoiced, Paid), and Invoice Reference (hyperlinked to the Sales module invoice).

## 5.5 Project P&L

**FR-PROJ-049:** The system shall compute and display the Project P&L using the formula:

$$ProjectPL = Revenue - \sum Costs$$

Where:
- $Revenue$ = sum of all confirmed (non-draft, non-cancelled) invoice amounts linked to the project in the Sales module.
- $\sum Costs$ = total actual costs from the project cost ledger (FR-PROJ-041).

**FR-PROJ-050:** The system shall display the Project P&L as a structured summary with rows:

- Contract/Billing Value (total agreed value)
- Revenue Recognised (invoices confirmed)
- Labour Costs
- Materials Costs
- Subcontractor Costs
- Equipment Costs
- Travel Costs
- Overhead Costs
- Other Costs
- Total Costs
- **Gross Project Profit/(Loss)**
- Gross Margin %: $GrossMargin\% = \frac{Revenue - \sum Costs}{Revenue} \times 100$

**FR-PROJ-051:** The Project P&L shall refresh automatically whenever a new cost entry, invoice, or reversal is posted to the project. The P&L screen shall display the timestamp of the last refresh.

**FR-PROJ-052:** The system shall provide a Project P&L Report exportable to Excel (.xlsx) and PDF. The export shall include project name, project code, client, project manager, date range, and all P&L rows with amounts.
