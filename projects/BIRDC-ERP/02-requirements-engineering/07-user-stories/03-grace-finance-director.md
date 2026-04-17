# Persona 3: Grace — Finance Director

**Profile:** Age 44, CPA/MBA, proficient Excel user. Approves journal entries and payroll, monitors parliamentary budget vote expenditure, generates financial statements, prepares management reports for the Director and Parliament.

**Critical requirement:** Dual-mode accounting — parliamentary (PIBID) and IFRS commercial (BIRDC) simultaneously without reconciling separate spreadsheets.

---

## US-023: Generate a Trial Balance in Either Accounting Mode

**US-023:** As Grace, I want to generate a Trial Balance for BIRDC commercial accounts, PIBID parliamentary accounts, or a consolidated view at any time without waiting for period closing, so that I can review financial accuracy on demand.

**Acceptance criteria:**

- The Trial Balance report accepts a mode selector with three options: "BIRDC Commercial," "PIBID Parliamentary," and "Consolidated."
- The report generates within 10 seconds for any date range up to 12 months.
- The Trial Balance is always in balance (total debits = total credits); if a discrepancy exists, the system flags the out-of-balance amount and prevents report export until the discrepancy is investigated.
- The Trial Balance can be exported to PDF and Excel with BIRDC/PIBID header, report date, mode, and Grace's name as preparer.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-005-001

---

## US-024: Monitor Parliamentary Budget Vote Expenditure in Real Time

**US-024:** As Grace, I want to see the current expenditure against each parliamentary budget vote at any time, so that I can prevent over-expenditure and prepare accurate parliamentary reports.

**Acceptance criteria:**

- The Budget dashboard displays each active vote with: vote code, vote description, approved budget amount, committed (approved but unpaid) amount, expended (paid) amount, available balance, and % utilised.
- When any vote reaches 80% utilisation, the system sends an automated alert to Grace and the Director (per BR-014).
- When any vote reaches 95% utilisation, a second alert is sent to Grace and the Director (per BR-014).
- Any expenditure transaction that would cause a vote to exceed 100% of its allocated amount is blocked pending Director-level override with a written justification logged in the audit trail (per BR-014).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-008-001

---

## US-025: Approve a Journal Entry

**US-025:** As Grace, I want to review and approve journal entries prepared by accounts assistants, so that only verified, balanced entries are posted to the General Ledger.

**Acceptance criteria:**

- Grace's approval queue shows all journal entries in "pending approval" status with: JE number, preparer name, date, narration, debit total, credit total, and supporting attachment.
- Grace can open any JE to review the full line-level detail before approving or rejecting.
- Grace cannot approve a journal entry she herself created (per BR-003, segregation of duties enforced at API layer).
- When Grace approves a JE, the status changes to "Posted," the GL is updated, and the hash chain is extended (per BR-013); when she rejects, the preparer is notified with Grace's rejection reason.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-005-002

---

## US-026: Verify the GL Hash Chain Integrity

**US-026:** As Grace, I want to trigger a GL hash chain integrity check on demand, so that I can confirm to the Auditor General that no historical entries have been tampered with.

**Acceptance criteria:**

- The GL module provides a "Hash Chain Integrity Check" function accessible only to Finance Director and IT Administrator roles.
- When triggered, the system recalculates the hash chain for every account and compares each entry's stored hash against the recalculated hash; the check completes within 5 minutes for up to 5 years of data.
- If all hashes match, the system displays: "Hash chain integrity verified. No anomalies detected. [Entry count] entries checked." with the timestamp.
- If any hash mismatch is detected, the system displays the broken link(s) with account, JE number, date, and flags the record for investigation; the check result is saved to the audit log (per BR-013).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-005-003

---

## US-027: Approve and Lock the Monthly Payroll

**US-027:** As Grace, I want to review the payroll run and lock it once satisfied, so that salaries are paid from an immutable, approved record.

**Acceptance criteria:**

- Grace's payroll approval screen displays the payroll summary: period, employee count, total gross pay, total deductions (PAYE, NSSF, LST, loans), total net pay, and employer contributions.
- Grace can drill down to individual employee payslips from the summary screen.
- When Grace clicks "Approve and Lock," the system records her user ID, timestamp, and a digital approval signature; the payroll run status changes to "Locked" and no modifications are permitted (per BR-010).
- If an error is found after locking, a correction is processed as a separate adjustment run; the locked run cannot be unlocked or modified.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 5

**FR Reference:** FR-014-001

---

## US-028: Configure PAYE Tax Bands Without Developer Involvement

**US-028:** As Grace, I want to update PAYE tax bands in the system when URA publishes new rates, so that payroll calculations are immediately compliant without waiting for IT support.

**Acceptance criteria:**

- The Payroll Configuration screen has a "PAYE Tax Bands" table that Grace can edit: income threshold (lower and upper bounds), tax rate (%), and effective date.
- Grace adds a new row, sets the effective date, and saves; the system applies the new bands to all payroll runs with pay periods on or after the effective date.
- The previous band configuration is retained in history for audit purposes and payroll runs for prior periods continue to use the tax bands effective at that time.
- After saving, Grace sees a confirmation: "PAYE bands updated. New rates effective [date]. Previous configuration archived." No developer action is required (per DC-002).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 5

**FR Reference:** FR-014-002

---

## US-029: Generate a Profit and Loss Statement

**US-029:** As Grace, I want to generate a Profit and Loss statement for any period without waiting for period closing, so that I can provide management reports to the Director on demand.

**Acceptance criteria:**

- The P&L report is generated in BIRDC commercial mode or PIBID mode; the mode is selected before generation.
- The report compares the selected period against the prior-year equivalent period and the current budget, showing variance in amount and percentage.
- The P&L generates within 15 seconds for a full financial year.
- The report exports to PDF with BIRDC/PIBID letterhead and is available for immediate printing or email attachment.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-005-004

---

## US-030: Process Farmer Payments in Bulk via Mobile Money

**US-030:** As Grace, I want to approve and release bulk mobile money payments to cooperative farmers, so that thousands of farmers are paid promptly after each delivery period.

**Acceptance criteria:**

- The Farmer Payment screen displays the payment batch: cooperative name, number of farmers, total net payable (gross amount minus loan repayments and cooperative levies), and an itemised list per farmer with NIN, mobile money number, and net payment amount.
- Grace reviews the batch, and upon approval, the system generates an MTN MoMo or Airtel Money bulk payment file in the required API format and submits it.
- Each farmer receives an SMS payment confirmation from the mobile money provider once payment is processed.
- Failed payments (invalid mobile number, daily limit exceeded) are flagged individually for re-processing; the system does not cancel the entire batch due to a single failure.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-007-001

---

## US-031: Review AR Aging and Manage Credit Holds

**US-031:** As Grace, I want to review the accounts receivable aging report and place overdue accounts on credit hold, so that BIRDC's credit risk is controlled.

**Acceptance criteria:**

- The AR Aging report shows all customers and agents with outstanding balances, grouped by aging bucket: Current, 1–30 days, 31–60 days, 61–90 days, 91–120 days, 120+ days.
- Grace can place any customer on "Credit Hold" from the AR Aging screen; the system immediately blocks new credit sales and new agent stock issuances for that customer or agent.
- The credit hold is recorded in the audit log with Grace's user ID, timestamp, and the reason she entered.
- Grace can release a credit hold from the same screen; the system resumes credit for the account and logs the release.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-006-003

---

## US-032: Configure Chart of Accounts Without Developer Involvement

**US-032:** As Grace, I want to add, edit, or reclassify accounts in the Chart of Accounts through the UI, so that I can adapt the account structure to evolving reporting requirements without IT support.

**Acceptance criteria:**

- The Chart of Accounts management screen allows Grace to add a new account: specify account code, account name, account type (Asset, Liability, Equity, Revenue, Expense), parent account, currency, and parliamentary vote code (if applicable).
- Grace can edit the account name and parent classification of any account that has no posted transactions.
- Grace cannot delete an account that has posted GL transactions; the system displays: "Account has [n] transactions. Deactivate only — deletion not permitted."
- All changes to the Chart of Accounts are logged in the audit trail with Grace's user ID, timestamp, old values, and new values.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-005-005

---

## US-033: Generate the NSSF Contribution Schedule

**US-033:** As Grace, I want the system to generate the NSSF contribution schedule in the official NSSF Uganda format after each payroll run, so that I can submit it to NSSF without manual reformatting.

**Acceptance criteria:**

- After a payroll run is locked, the system generates an NSSF contribution schedule file in the format specified by NSSF Uganda (CSV or Excel, per current NSSF requirements).
- The schedule includes for each employee: NSSF membership number, employee name, NIN, gross pay, employee contribution (5%), employer contribution (10%), and total contribution.
- The grand total on the schedule matches the NSSF liability amount posted to the GL for that payroll period to within UGX 0.
- The schedule file is named `NSSF_[YYYYMM]_BIRDC.csv` and is available for download from the payroll module.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 5

**FR Reference:** FR-014-003

---

## US-034: View the Executive Financial Dashboard

**US-034:** As Grace, I want to view a real-time financial dashboard when I open the ERP, so that I have immediate visibility into cash position, revenue, and budget status without running individual reports.

**Acceptance criteria:**

- The Finance Director dashboard displays, on a single screen: today's cash and bank balances, month-to-date revenue vs. budget, outstanding AR balance, outstanding AP balance, and top 3 budget votes with highest utilisation percentage.
- All dashboard figures are live (no manual refresh required) and reflect all posted transactions up to the current minute.
- Each dashboard tile is clickable and navigates to the corresponding detailed report.
- The dashboard loads within 5 seconds of login.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-005-006

---

## US-035: Manage Imprest Accounts and Petty Cash

**US-035:** As Grace, I want to approve imprest replenishments and review imprest disbursement records, so that petty cash floats are controlled and all disbursements are receipted.

**Acceptance criteria:**

- The Imprest module displays each imprest account: holder name, authorised float amount, current balance, and a list of disbursements with receipt number, payee, amount, and purpose.
- A disbursement that would reduce any imprest balance below UGX 0 is blocked by the system with the message: "Insufficient imprest balance. Replenishment required before further disbursements." (per BR-018).
- Grace approves replenishments from the pending replenishment queue; upon approval, the imprest balance is restored and the GL is auto-posted.
- Grace can export the full imprest transaction history as a PDF for auditor review.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-005-007

---

## US-036: Receive Withholding Tax Certificates for Vendor Payments

**US-036:** As Grace, I want the system to generate WHT certificates automatically when vendor payments with withholding tax are processed, so that BIRDC meets its obligations under the Uganda Income Tax Act.

**Acceptance criteria:**

- When a vendor payment is processed and the vendor is flagged as a local service supplier subject to 6% WHT (per BR-018), the system calculates and deducts 6% WHT, posts the WHT liability to the GL, and generates a WHT certificate in the URA-prescribed format.
- The WHT certificate includes: supplier name, TIN, payment date, gross amount, WHT rate, WHT amount deducted, and BIRDC's TIN.
- The WHT certificate PDF is available for download and email delivery to the supplier immediately after payment processing.
- The system generates a monthly WHT remittance schedule summarising all WHT deducted in the period, formatted for URA submission.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-007-002
