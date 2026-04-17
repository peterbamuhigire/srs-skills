---
title: "User Stories -- Finance, HR, and Reporting (F-005, F-006, F-007, F-008)"
project: "Maduuka"
module: "Finance / HR / Reporting"
version: "1.0"
date: "2026-04-05"
---

# User Stories: Finance, HR, and Reporting (F-005, F-006, F-007, F-008)

These stories express financial, HR, and reporting requirements from the perspective of three roles: Accountant (Grace), HR Manager (Amara), and Business Owner (Robert).

---

## Expenses and Petty Cash (F-005)

**US-EXP-001:** As an accountant, I want to record an expense with a receipt photo attached so that the documentation is captured at the point of entry and linked to the financial record.

**Acceptance Criteria:**

- Given the accountant is on the Android expense entry screen, when they photograph the receipt, then the system attempts OCR extraction of the total amount and vendor name and pre-populates those fields.
- Given the OCR extraction is complete, then the accountant can correct the pre-populated values before saving.
- Given the expense is saved, then the receipt photo is stored and visible on the expense record.

**FR Reference:** FR-EXP-001, FR-EXP-002

**Priority:** Must Have

---

**US-EXP-002:** As an accountant, I want expenses above a configured threshold to require manager approval before posting so that large or unusual expenses are reviewed before they affect account balances.

**Acceptance Criteria:**

- Given an expense amount exceeds the configured approval threshold, when the expense is saved, then the status is set to "pending_approval" and a push notification is sent to the designated approver.
- Given the expense is pending approval, then it is not posted to the financial accounts.
- Given the manager approves the expense, then the amount is posted to the payment account specified in the expense record.

**FR Reference:** FR-EXP-003, FR-EXP-004

**Priority:** Must Have

---

## Financial Accounts and Cash Flow (F-006)

**US-FIN-001:** As an accountant, I want to perform bank reconciliation so that I can identify transactions in the system that do not appear on the bank statement and vice versa.

**Acceptance Criteria:**

- Given the accountant initiates bank reconciliation for an account and a period, when the reconciliation screen opens, then the system presents the account's transaction log for the period.
- Given the accountant imports a CSV bank statement, then the system attempts automatic matching by amount and date.
- Given automatic matching is complete, then matched transactions are pre-checked and unmatched transactions on either side are highlighted for manual review.

**FR Reference:** FR-FIN-004, FR-FIN-005

**Priority:** Must Have

---

**US-FIN-002:** As an accountant, I want to view the daily financial summary for each payment account so that I can confirm opening balances, inflows, outflows, and closing balances at the end of each day.

**Acceptance Criteria:**

- Given the accountant requests the daily summary for a date, when the report loads, then it displays for each payment account: opening balance, total inflows, total outflows, and closing balance.

**FR Reference:** FR-FIN-007

**Priority:** Must Have

---

## Sales Reporting and Analytics (F-007)

**US-REP-001:** As a business owner, I want to view a gross margin trend report so that I can monitor whether margins are improving or deteriorating over time.

**Acceptance Criteria:**

- Given the business owner requests sales by product for a date range, when the report loads, then it shows per product: quantity sold, revenue, cost, and gross margin.
- Given the business owner selects a trend view, then the system displays margin over time with a period-over-period comparison.

**FR Reference:** FR-REP-003

**Priority:** Must Have

---

**US-REP-002:** As a business owner, I want to schedule a daily report to be sent to my email automatically so that I receive the business summary without logging in.

**Acceptance Criteria:**

- Given the business owner configures a scheduled report with a specified email address and frequency (daily), when the configured time is reached, then the system sends the report as a PDF to the specified email.
- Given the scheduled report is sent, then no manual action is required from the business owner.

**FR Reference:** FR-REP-010

**Priority:** Should Have

---

**US-REP-003:** As a business owner, I want to export any report as CSV or PDF so that I can share data with my accountant or perform further analysis.

**Acceptance Criteria:**

- Given the business owner requests a report export, when the export is initiated, then the system generates the file in the requested format (CSV or PDF) within 30 seconds for periods up to 12 months of data.
- Given the export is ready, then a download or share option is presented.

**FR Reference:** FR-REP-009

**Priority:** Must Have

---

## HR and Payroll (F-008)

**US-HR-001:** As an HR manager, I want to process a monthly payroll run so that all staff receive their correct net pay with statutory deductions automatically calculated.

**Acceptance Criteria:**

- Given the HR manager initiates a payroll run for the current month, when the calculation is triggered, then the system computes gross pay, PAYE (per current Uganda tax bands), NSSF employee deduction (5%), other deductions, and net pay for each staff member.
- Given the payroll covers up to 100 staff, then the calculation completes within 60 seconds.
- Given the calculation is complete, then the HR manager can review each staff member's breakdown before approving.

**FR Reference:** FR-HR-011, FR-HR-012

**Priority:** Must Have

---

**US-HR-002:** As an HR manager, I want to approve a payroll run so that payslip amounts are locked and no further changes can be made.

**Acceptance Criteria:**

- Given the HR manager reviews the payroll run and approves it, when approval is confirmed, then all payslip amounts for that run are locked.
- Given a payslip is locked, then no modification is permitted to that payslip.
- Given a correction is needed, then the system requires a reversal in the subsequent payroll period.

**FR Reference:** FR-HR-013

**Priority:** Must Have

---

**US-HR-003:** As an HR manager, I want to send payslips to all staff via WhatsApp after payroll approval so that staff receive their payslips without printing or physical distribution.

**Acceptance Criteria:**

- Given the payroll run is approved and payslips are generated, when the HR manager triggers payslip delivery, then the system sends each staff member their payslip as a PDF via WhatsApp to their registered phone number.
- Given a staff member's WhatsApp delivery fails, then the system falls back to an SMS notification with a download link.

**FR Reference:** FR-HR-014, FR-HR-015

**Priority:** Must Have

---

**US-HR-004:** As an HR manager, I want to process a leave request submitted by a staff member so that the request is reviewed and the outcome is communicated automatically.

**Acceptance Criteria:**

- Given a staff member submits a leave application through the app, when the submission is made, then the system notifies the HR manager via push notification within 1 minute.
- Given the HR manager approves the request, then the system notifies the staff member via push notification, records the decision with the manager's name and timestamp, and deducts the approved days from the staff member's leave balance.
- Given the HR manager rejects the request, then the staff member is notified and the leave balance is unchanged.

**FR Reference:** FR-HR-005, FR-HR-006

**Priority:** Must Have

---

**US-HR-005:** As an accountant, I want to generate the NSSF schedule after payroll approval so that I can submit it to the NSSF Uganda employer portal without retyping data.

**Acceptance Criteria:**

- Given the accountant requests the NSSF schedule after a payroll run is approved, when the schedule is generated, then it lists each employee's name, NIN, gross salary, employee NSSF contribution (5%), employer NSSF contribution (10%), and total contribution.
- Given the schedule is generated, then it is formatted for upload to the NSSF Uganda employer portal.

**FR Reference:** FR-HR-016

**Priority:** Must Have

---

**US-HR-006:** As an accountant, I want to generate the PAYE return after payroll approval so that I can submit accurate tax data to URA without manual extraction.

**Acceptance Criteria:**

- Given the accountant requests the PAYE return for a month, when the return is generated, then it lists each employee, their gross salary, taxable income, PAYE deducted, and cumulative PAYE for the year to date, formatted per URA requirements.

**FR Reference:** FR-HR-017

**Priority:** Must Have

---

**US-HR-007:** As a business owner, I want to view the business health score on the dashboard so that I can assess financial health at a glance without running individual reports.

**Acceptance Criteria:**

- Given the business owner views the business health score, when the score is displayed, then the system shows a RAG (Red/Amber/Green) composite indicator derived from: gross margin %, expense-to-revenue ratio, stock turnover rate, and credit collection rate.
- Given a metric falls in the Red band, then the system highlights which metric is causing the red status.
- Given the business owner wants to adjust scoring bands, then the system allows configuration of the bands per metric.

**FR Reference:** FR-DASH-007

**Priority:** Should Have
