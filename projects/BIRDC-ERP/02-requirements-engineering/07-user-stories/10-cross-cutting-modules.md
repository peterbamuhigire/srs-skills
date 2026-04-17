# Cross-Cutting Module User Stories

This section captures user stories for modules not exclusively owned by a single persona: Human Resources (F-013), Payroll (F-014), Research and Development (F-015), Administration and PPDA Compliance (F-016), System Administration (F-017), and EFRIS Full Integration (F-018). These stories are authored from the perspective of the relevant functional role.

---

## HR Module (F-013) — HR Manager / All Staff

## US-085: Import Biometric Attendance Records from ZKTeco Device

**US-085:** As the HR Manager, I want to import attendance records directly from the ZKTeco biometric device, so that payroll-period attendance is authoritative and free from manual transcription.

**Acceptance criteria:**

- The HR module provides a "Import Biometric Attendance" function that connects to the ZKTeco device via direct API or file import (per the device's supported export format) and imports all attendance records for the selected date range.
- Imported biometric records are stored as authoritative; any manual override requires Finance Manager approval and a reason logged in the audit trail (per BR-016).
- The system displays a post-import summary: total records imported, employees matched, and any unmatched records (biometric ID not found in the employee register).
- Manual attendance records accepted during biometric device downtime are flagged "Manual — Pending Biometric Reconciliation" until the corresponding biometric data is imported and verified.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 5

**FR Reference:** FR-013-001

---

## US-086: Manage Employee Leave Requests via HR Self-Service App

**US-086:** As a BIRDC staff member, I want to apply for leave from the HR Self-Service Android app, so that I can submit leave requests and check my leave balance without visiting the HR office.

**Acceptance criteria:**

- The HR Self-Service App displays the employee's leave balance for each leave type (annual, sick, maternity, paternity, compassionate, study, unpaid), updated in real time.
- The employee selects leave type, start date, end date, and reason; the app submits the request and notifies the line manager for approval.
- The employee receives a push notification when the line manager approves or rejects the request; the rejection includes the line manager's reason.
- Approved leave is reflected in the payroll calculation for the relevant period: unpaid leave deducts the corresponding daily rate from gross pay.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 5

**FR Reference:** FR-013-002

---

## US-087: View Payslip from HR Self-Service App

**US-087:** As a BIRDC staff member, I want to view and download my payslip from the HR Self-Service App after each payroll run, so that I can verify my pay without collecting a paper payslip.

**Acceptance criteria:**

- The HR Self-Service App displays the current and last 12 months of payslips for the logged-in employee.
- Each payslip shows: gross pay, all deductions itemised (PAYE, NSSF, LST, loans, other), net pay, and bank account credited.
- The employee can download the payslip as a PDF or share it via email or WhatsApp from the app.
- Payslips are available on the app within 2 hours of the Finance Director locking the payroll run.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 5

**FR Reference:** FR-014-004

---

## US-088: Process a Staff Loan with Automatic Payroll Deduction

**US-088:** As the HR Manager, I want to record a staff loan and configure the monthly repayment schedule, so that deductions are applied automatically each payroll period without manual entry.

**Acceptance criteria:**

- The HR Manager creates a loan record for an employee: loan amount, disbursement date, number of repayment instalments, and monthly instalment amount.
- The system calculates and displays the repayment schedule; the loan is linked to the employee's payroll record.
- Each payroll run deducts the scheduled instalment from the employee's gross pay automatically; the loan balance is updated after each deduction.
- If an employee exits BIRDC with an outstanding loan balance, the exit clearance checklist flags the outstanding loan and the HR Manager is prompted to record the settlement arrangement.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 5

**FR Reference:** FR-013-003

---

## R&D Module (F-015) — Research Coordinator

## US-089: Record Banana Variety Field Trial Results

**US-089:** As the Research Coordinator, I want to record field trial results by plot and variety, so that BIRDC can identify the highest-yielding, best-processing banana cultivars for farmer promotion.

**Acceptance criteria:**

- The Research module allows trial plots to be registered with: plot ID, farm location (GPS), variety (cultivar name), planting date, treatment (fertiliser, irrigation, pest control), and assigned extension officer.
- At each assessment point, the Research Coordinator records: plant height, bunch weight, fingers per bunch, and harvest date; the system stores the record with the plot and assessment date.
- The system calculates average yield per variety across all trial plots and ranks varieties by: processing yield (kg flour per kg matooke), quality score, and disease resistance rating.
- The Research Coordinator can export the variety performance comparison report as a PDF for presentation at the Board.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 6

**FR Reference:** FR-015-001

---

## US-090: Track R&D Expenditure Linked to GL

**US-090:** As the Research Coordinator, I want to tag R&D project costs to specific research projects, so that the total R&D expenditure per project is visible and can be reported to funders.

**Acceptance criteria:**

- Every procurement transaction, staff cost allocation, and direct expense can be tagged with an R&D project code from a configured list.
- The R&D Expenditure report shows spending by project: budget allocated, expended to date, remaining budget, and % utilised — sourced from the GL without manual extraction.
- The R&D expenditure data is reconciled against the corresponding GL accounts; the report total matches the GL balance for the R&D expense accounts for the same period.
- The Research Coordinator can export the R&D expenditure report in a format compatible with external research funder reporting templates.

**MoSCoW Priority:** Could Have

**Delivery Phase:** Phase 6

**FR Reference:** FR-015-002

---

## Administration Module (F-016) — Administration Officer

## US-091: Maintain the Fixed Asset Register with Depreciation

**US-091:** As the Administration Officer, I want to register BIRDC's assets and have the system calculate depreciation automatically, so that the asset register is always current and the GL reflects accurate asset values.

**Acceptance criteria:**

- Each asset is registered with: asset tag number, description, category, acquisition date, acquisition cost (UGX), useful life (years), depreciation method (straight-line or reducing balance), salvage value, and physical location.
- The system calculates and posts monthly depreciation to the GL automatically on the last day of each accounting period: DR Depreciation Expense / CR Accumulated Depreciation — without manual journal entries.
- The asset register report shows: asset list, current book value, accumulated depreciation to date, and remaining useful life.
- When an asset is disposed, the Administration Officer records the disposal date and proceeds; the system posts the disposal entry and removes the asset from the active register.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 6

**FR Reference:** FR-016-002

---

## US-092: Maintain the Vehicle and Equipment Logbook

**US-092:** As the Administration Officer, I want to record vehicle trip logs and equipment usage, so that BIRDC can account for fuel costs, maintenance, and vehicle utilisation.

**Acceptance criteria:**

- Each vehicle has a logbook with: vehicle registration, driver, trip date, trip purpose, start odometer, end odometer, kilometres travelled, fuel consumed (litres), and fuel cost (UGX).
- The system calculates fuel efficiency (km per litre) per trip and displays a trend over the last 12 months.
- Maintenance records are linked to the vehicle: maintenance date, description, cost, and next service due date.
- The Administration Officer receives an alert when a vehicle approaches its next service due date (configurable: 500 km before or 30 days before).

**MoSCoW Priority:** Could Have

**Delivery Phase:** Phase 6

**FR Reference:** FR-016-003

---

## System Administration Module (F-017) — IT Administrator

## US-093: Create User Accounts and Assign Roles

**US-093:** As the IT Administrator, I want to create user accounts and assign roles with granular permissions, so that every BIRDC staff member has access only to the functions their role requires.

**Acceptance criteria:**

- The IT Administrator creates a user account by entering: full name, NIN, email, department, job title, and role(s).
- Roles are pre-configured permission bundles; the IT Administrator can assign 1 or more roles to a user.
- The permission matrix operates at 8 layers: Role → Page → API endpoint → UI element → Location → Time → Conditional rules → Object ownership; no permission can be granted outside this matrix.
- User account creation, role assignment changes, and account deactivation are all recorded in the audit log with the IT Administrator's user ID and timestamp.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 7

**FR Reference:** FR-017-001

---

## US-094: Review the System-Wide Audit Log

**US-094:** As the IT Administrator, I want to search the complete audit log by user, action type, date range, and affected table, so that any suspicious or incorrect activity can be traced immediately.

**Acceptance criteria:**

- The audit log search accepts filters: user (dropdown), action type (create / update / delete / login / export), date range, and affected database table.
- Results are displayed in chronological order with: timestamp, user ID, user name, action type, affected record ID, old value (before change), and new value (after change).
- The audit log is read-only; no user, including the IT Administrator, can delete or modify an audit log entry.
- The IT Administrator can export the filtered audit log results to a CSV file for submission to the OAG auditor.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 7

**FR Reference:** FR-017-002

---

## US-095: Schedule Automated Database Backups

**US-095:** As the IT Administrator, I want to configure automated database backup schedules with retention policies, so that BIRDC's data is protected and recoverable within the 7-year retention requirement.

**Acceptance criteria:**

- The backup management screen allows the IT Administrator to configure: backup frequency (daily, weekly, monthly), backup time, destination path, and retention period (minimum 7 years in compliance with DC-003).
- The system runs backups automatically per the configured schedule and logs each backup: start time, completion time, file size, and success/failure status.
- If a scheduled backup fails, the system sends an email and system notification to the IT Administrator within 15 minutes of the failure.
- The IT Administrator can trigger a manual backup at any time from the backup management screen; the manual backup does not affect the scheduled backup cycle.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 7

**FR Reference:** FR-017-003

---

## EFRIS Integration (F-018)

## US-096: Submit All Commercial Invoices to URA EFRIS in Real Time

**US-096:** As the Finance Director, I want every commercial invoice and POS receipt to be submitted to URA EFRIS automatically, so that BIRDC is always compliant with the URA electronic fiscal receipting requirement without manual submission.

**Acceptance criteria:**

- When a sales invoice is confirmed in the Sales module (F-001) or a POS sale is completed (F-002), the system automatically submits the fiscal document to EFRIS via the system-to-system API within 30 seconds.
- On successful EFRIS submission, the Fiscal Document Number (FDN) and QR code returned by URA are stored on the transaction record and printed on all copies of the invoice or receipt.
- If EFRIS submission fails (API error, network timeout), the transaction is added to the failed submission retry queue; the system retries every 5 minutes and sends an alert to the Finance Manager if any document remains unsubmitted for more than 60 minutes.
- The EFRIS audit log records every submission attempt with: document reference, submission timestamp, EFRIS response code, and FDN (for successful submissions).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 7

**FR Reference:** FR-018-001

---

## US-097: Process a Credit Note and Submit to EFRIS

**US-097:** As the Finance Director, I want credit notes to be submitted to EFRIS automatically when issued, so that all reversals are fiscally compliant and BIRDC's EFRIS records match its internal accounting.

**Acceptance criteria:**

- When a credit note is issued (from a void POS transaction or a sales return), the system submits the credit note to EFRIS via the API within 30 seconds, referencing the original FDN.
- EFRIS returns a Credit Note FDN; this is stored on the credit note record and printed on the credit note document.
- The credit note is posted to the GL (DR Revenue / CR AR or DR Cash / CR Revenue) automatically; no manual journal entry is required.
- Failed credit note EFRIS submissions are queued in the retry queue alongside failed invoice submissions and are treated with equal priority.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 7

**FR Reference:** FR-018-002

---

## Security and Compliance (F-019)

## US-098: Conduct System Load Testing at Peak Production Scenario

**US-098:** As the IT Administrator, I want the system to be load tested against the peak production scenario (140 MT/day throughput) before go-live, so that performance does not degrade under operational peak conditions.

**Acceptance criteria:**

- The load test simulates: 1,071 concurrent Sales Agent App sessions, 80 Factory Floor App sessions, 15 Warehouse App sessions, and 150 web ERP users simultaneously.
- Under full simulated load, all POS transaction confirmations complete within 3 seconds, all dashboard pages load within 5 seconds, and all report generations complete within 30 seconds.
- The load test report identifies any bottleneck (database query, API endpoint, or network segment) that degrades response times beyond the above thresholds.
- No data loss or transaction duplication occurs during the load test; all test transactions are verifiably recorded and reconciled.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 7

**FR Reference:** FR-019-001

---

## Consolidated and Reporting Stories

## US-099: Export Financial Statements for Parliamentary Reporting

**US-099:** As Grace, I want to generate the full set of parliamentary financial statements (Statement of Receipts and Payments, Budget vs. Actual Expenditure by Vote) for submission to Parliament, so that PIBID meets its parliamentary accountability obligations.

**Acceptance criteria:**

- The PIBID Parliamentary Reports section generates: Statement of Receipts and Payments, Budget vs. Actual by Vote Code, and a Comparative Statement against the prior parliamentary year — all in PIBID parliamentary mode.
- Reports are generated for any period within the parliamentary financial year (July–June) without requiring period closing.
- The Budget vs. Actual report reconciles to the general ledger for the same period; any variance between the report and GL is highlighted and must be zero for report export to be enabled.
- Reports export to PDF with the PIBID letterhead and are formatted according to the OAG Uganda reporting requirements.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-008-004

---

## US-100: Configure Commission Rates by Agent or Territory Without Developer Involvement

**US-100:** As the Sales and Marketing Manager, I want to configure commission rates for individual agents or by territory from the ERP UI, so that commission structures can be adjusted as business needs change without IT support.

**Acceptance criteria:**

- The Agent Configuration screen allows the Sales and Marketing Manager to set the commission rate (%) for each agent individually or apply a rate to all agents in a territory.
- Rate changes include an effective date; the system applies the new rate to sales cleared by remittances on or after the effective date (per BR-015).
- The previous commission rate is retained in history for audit and retrospective calculation purposes.
- After saving a new commission rate, the system displays a confirmation: "Commission rate for [agent/territory] updated to [rate]%, effective [date]. Verified remittances after this date will use the new rate."

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-010
