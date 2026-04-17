# 6. F-008: Budget Management

## 6.1 Module Overview

Module F-008 provides simultaneous parliamentary budget vote management (PIBID, July–June fiscal year) and commercial budget management (BIRDC IFRS, January–December). Both budget modes draw actual expenditure data directly from GL postings — there is no separate expenditure data entry. Budget vs. actual variance is available on demand at any moment, not only at period-end. The module enforces the three-tier alert system mandated by BR-014 and provides audit-logged Director override for budget ceiling breaches.

## 6.2 Parliamentary Budget Vote Management

### FR-BDG-001

**Stimulus:** The Finance Director imports the approved PIBID parliamentary budget for a new fiscal year (July 1 — June 30) from an Excel template using PhpSpreadsheet.

**Response:** The system reads the Excel file and creates or updates budget vote records for each row, mapping: vote code, vote name, department, approved amount (UGX), and fiscal year. It validates that: (a) every vote code matches an existing vote code in the vote code configuration table; (b) no row has a blank or zero approved amount; (c) the total of all vote amounts balances to the total appropriation figure on the summary tab of the Excel template (if present). On successful import, the system displays an import summary: total votes imported, total UGX appropriated, and any rows with validation errors. Errors are listed with row numbers for Finance Director correction and re-import.

---

### FR-BDG-002

**Stimulus:** The Finance Director creates or edits a parliamentary vote code configuration record, specifying vote code, vote name, responsible department, and linked GL cost centre.

**Response:** The system saves the vote code configuration. The vote code is made available as a budget line item for the annual budget import and as a cost centre segment for GL dual-mode posting (per FR-GL-005). The Finance Director may deactivate a vote code; deactivated codes cannot receive new budget allocations but remain visible in historical reports.

---

### FR-BDG-003

**Stimulus:** An Accounts Assistant or Finance Manager requests the Parliamentary Budget Utilisation report for a specified vote code and period.

**Response:** The system retrieves: (a) the approved budget for the vote code from the budget table; (b) the actual expenditure by summing all GL postings to cost centres linked to the vote code within the period. The report displays: vote code, vote name, approved budget (UGX), actual expenditure (UGX), remaining budget (UGX), and utilisation percentage ($\text{Utilisation \%} = \frac{\text{Actual Expenditure}}{\text{Approved Budget}} \times 100\%$). The report is generated in real time from posted GL data. Export to PDF and Excel available.

---

### FR-BDG-004

**Stimulus:** A journal entry is posted to a GL account that is linked to a parliamentary vote code.

**Response:** The system automatically updates the vote code's accumulated expenditure total in the budget utilisation table within the same database transaction as the GL posting. No separate budget expenditure entry is required. The utilisation percentage is recalculated and stored immediately after posting.

---

### FR-BDG-005

**Stimulus:** The cumulative expenditure against a parliamentary budget vote reaches 80% of the approved vote amount.

**Response:** The system sends an automated email notification to the Finance Director (STK-002) and the BIRDC Director (STK-001) identifying: vote code, vote name, approved amount (UGX), cumulative expenditure (UGX), remaining balance (UGX), utilisation percentage, and fiscal year. The notification is also displayed as a persistent alert on the Finance Director's dashboard. The alert is logged in the audit trail with the vote code, threshold crossed, and timestamp (BR-014).

**Verification:** Set a vote budget to UGX 1,000,000; post GL transactions totalling UGX 800,001; confirm email notifications are sent and the dashboard alert is displayed.

---

### FR-BDG-006

**Stimulus:** The cumulative expenditure against a parliamentary budget vote reaches 95% of the approved vote amount.

**Response:** The system sends an additional escalation notification to the Finance Director and Director (same recipients as FR-BDG-005). The escalation notification is distinguished from the 80% alert by a different subject line and urgency flag. The Finance Director's dashboard displays a `HIGH ALERT` indicator for the vote code (BR-014).

---

### FR-BDG-007

**Stimulus:** A GL posting would cause cumulative expenditure against a parliamentary budget vote to exceed 100% of the approved vote amount.

**Response:** The system does not automatically block the posting. Instead, it triggers a Director override workflow: (a) it notifies the Director (STK-001) and Finance Director (STK-002) in real time via email and dashboard alert that a budget ceiling breach is about to occur; (b) the posting is held in `pending_override` status; (c) the Director must log in and provide a written justification in the override screen; (d) upon Director confirmation, the system proceeds with the posting, records the override in the audit trail with: Director identity, justification text, vote code, breach amount, timestamp (BR-014). If the Director does not act within 24 hours, the Finance Director is re-notified.

**Verification:** Post transactions to exhaust a vote to 99%; confirm `pending_override` status on the next posting attempt; log in as Director and confirm; verify the audit trail entry contains the justification.

---

### FR-BDG-008

**Stimulus:** The Finance Director submits a budget revision (amendment) request for an approved vote, specifying the vote code, revised amount, and justification.

**Response:** The system creates a budget revision record in `draft` status, records the original approved amount, requested revised amount, and justification. The revision follows a configured approval workflow (Finance Director drafts; Director approves). On Director approval, the system updates the approved budget amount for the vote, triggers recalculation of all utilisation percentages for the vote, and logs the revision in the audit trail with original amount, revised amount, approver identity, and timestamp. The vote utilisation alerts are re-evaluated against the new budget amount.

## 6.3 Commercial Budget Management

### FR-BDG-009

**Stimulus:** The Finance Director creates or imports the BIRDC commercial budget for a fiscal year (January 1 — December 31), specifying account code, cost centre, and monthly or annual budgeted amount.

**Response:** The system creates commercial budget records linking each budget line to a specific GL account and cost centre. Monthly phasing is recorded individually — the Finance Director may enter a single annual amount (system divides evenly across 12 months) or enter monthly amounts individually. The total commercial budget for a fiscal year is displayable as a summary. PhpSpreadsheet handles the Excel import using the same import mechanism as parliamentary budget import (FR-BDG-001).

---

### FR-BDG-010

**Stimulus:** A GL posting is made to an account that has a commercial budget record for the current period.

**Response:** The system updates the commercial budget utilisation for the linked account and cost centre within the same database transaction as the GL posting. The updated utilisation is immediately visible in all commercial budget reports without requiring a refresh or batch calculation.

---

### FR-BDG-011

**Stimulus:** A Finance Manager requests the Commercial Budget vs. Actual report for a specified account, cost centre, and period (monthly, quarterly, or year-to-date).

**Response:** The system displays: GL account, cost centre, budgeted amount for the period, actual expenditure (sum of posted GL transactions for the account and cost centre within the period), variance (budget minus actual), and variance percentage. Favourable variances (actual < budget for expenses) are shown in green; unfavourable variances (actual > budget for expenses) are shown in red. Export to Excel and PDF available.

---

### FR-BDG-012

**Stimulus:** A Finance Manager requests the full commercial Budget vs. Actual summary for the current fiscal year to date.

**Response:** The system generates a full P&L-structured budget vs. actual report showing, for every revenue and expense account: annual budget, year-to-date actual, year-to-date variance, and full-year forecast (annualised actual). Export to Excel and PDF available. Response time ≤ 5,000 ms at P95 for a full-year 1,307-account report.

## 6.4 Dual-Mode Budget Reporting

### FR-BDG-013

**Stimulus:** The Finance Director requests a Dual-Mode Budget Report for a specified period.

**Response:** The system generates a side-by-side report showing: (a) PIBID parliamentary vote utilisation by vote code (approved, actual, remaining, % utilised) for the PIBID July–June fiscal year; and (b) BIRDC commercial budget utilisation by account and cost centre for the BIRDC January–December fiscal year. Both columns derive actual expenditure from the same posted GL transactions via the dual-mode account mapping (FR-GL-005, DC-004). A consolidated summary total is shown at the bottom. Export to Excel and PDF available.

---

### FR-BDG-014

**Stimulus:** The Director opens the Executive Dashboard Android app.

**Response:** The app calls the REST API and displays budget variance alerts: top 3 vote codes or commercial budget accounts with highest utilisation percentage, highlighting any above 80%. Push notifications are delivered when any budget crosses the 80% or 95% thresholds (complementing the email alerts from FR-BDG-005 and FR-BDG-006). The app data is read-only and requires JWT authentication.

## 6.5 Budget Alerts and Controls

### FR-BDG-015

**Stimulus:** The Finance Director configures budget alert thresholds for commercial budget accounts (in addition to the mandatory parliamentary vote thresholds from BR-014).

**Response:** The system saves the threshold configuration (default: 80% warning, 95% high alert, 100% override required) per cost centre or per account group. Alert recipients are configurable: Finance Director always included; additional recipients configurable by the Finance Director without developer involvement (DC-002).

---

### FR-BDG-016

**Stimulus:** The Finance Director requests a Budget Alert History report for a specified period.

**Response:** The system returns a log of all budget alerts issued, showing: alert date/time, vote code or account, threshold crossed (80%, 95%, or 100%), approved budget amount, actual amount at alert time, utilisation percentage at alert time, and whether a Director override was invoked (with override justification if applicable). Export to PDF available for audit evidence.

## 6.6 Budget Period Management

### FR-BDG-017

**Stimulus:** The Finance Director opens or closes a parliamentary budget period (typically monthly within the July–June fiscal year).

**Response:** The system sets the period status (`open` or `closed`) for the parliamentary fiscal calendar. Closing a period does not prevent GL postings to accounts within that period (GL period management is governed by FR-GL-023 and FR-GL-024); it freezes the budget utilisation snapshot for reporting, allowing the Finance Director to generate a final budget vs. actual for a closed period without ongoing postings changing the figures.

---

### FR-BDG-018

**Stimulus:** A user requests the Budget Period Status overview.

**Response:** The system displays a calendar view of all periods in the current fiscal year (parliamentary and commercial), showing status (open or closed), total budgeted amount per period, total actual expenditure per period, and utilisation percentage per period.

## 6.7 Budget Import and Configuration

### FR-BDG-019

**Stimulus:** The Finance Director downloads the budget import Excel template from the system.

**Response:** The system generates and serves a PhpSpreadsheet-formatted Excel template with: pre-populated headers (vote code, vote name, department, approved amount columns for parliamentary; account code, cost centre, monthly amount columns × 12 for commercial), data validation dropdowns for vote code and cost centre fields, and a sample data row demonstrating the required format. The template version matches the current fiscal year label.

---

### FR-BDG-020

**Stimulus:** The Finance Director configures a new vote code or GL account as a budget-tracked item mid-year.

**Response:** The system creates the budget record from the current period forward, populating the year-to-date approved amount on a pro-rata basis ($\text{Pro-Rata Amount} = \frac{\text{Annual Budget} \times \text{Remaining Periods}}{\text{Total Periods in Year}}$) or requiring the Finance Director to manually enter a remaining-year allocation. Retrospective actual expenditure from the start of the fiscal year is applied against the annual budget total regardless of when the budget record was created, so the utilisation percentage is accurate from day one.

---

### FR-BDG-021

**Stimulus:** The Finance Director requests a Budget Revision History report for a specified vote code or commercial account and fiscal year.

**Response:** The system returns all approved revisions for the specified budget item, showing: original approved amount, each revision (date, revised amount, justification, approver identity), and current approved amount. The revision history is exportable to PDF for audit evidence.
