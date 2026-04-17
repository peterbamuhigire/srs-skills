# 4. F-006: Accounts Receivable

## 4.1 Module Overview

Module F-006 manages all money owed to BIRDC by customers and agents. It tracks customer AR from invoice issuance through payment, enforces credit limits, automates aging analysis, and provides real-time agent receivable balances as a distinct sub-ledger. The module integrates with F-001 (Sales and Distribution) for invoice creation, F-004 (Agent Distribution Management) for remittance allocation, and F-005 (GL) for auto-posting.

## 4.2 Customer AR Tracking

### FR-AR-001

**Stimulus:** A sales invoice is confirmed and posted in F-001 (Sales and Distribution).

**Response:** The system automatically creates an AR record in the customer's sub-ledger, recording invoice number, invoice date, due date, currency, invoice amount in UGX, outstanding balance (equal to the invoice amount at creation), and the linked GL journal entry reference. The customer's total outstanding AR balance is updated in real time. No manual AR entry is required.

**Verification:** Confirm a sales invoice in F-001; immediately query the AR sub-ledger for the customer; confirm the invoice appears with outstanding balance equal to the invoice total.

---

### FR-AR-002

**Stimulus:** A payment receipt is recorded against a customer account, specifying payment method (bank transfer, mobile money, or cheque), amount, date, and allocation preference (specific invoice selection or auto-allocate).

**Response:** The system allocates the payment: if auto-allocate is selected, the system applies the payment to the oldest outstanding invoice first (FIFO order) until the payment amount is exhausted or all invoices are cleared; if specific invoices are selected, the system allocates to those invoices in the order specified. For each fully cleared invoice, the system updates the invoice status to `paid`. For a partially cleared invoice, the system records the partial payment and leaves the invoice `partially paid` with the remaining outstanding balance. The system auto-posts to GL per FR-GL-013.

**Verification:** Record a payment less than the oldest invoice amount; confirm the oldest invoice shows `partially paid` with the correct residual balance; confirm the GL JE is posted.

---

### FR-AR-003

**Stimulus:** An Accounts Assistant requests the AR sub-ledger for a specific customer, optionally filtered by date range or invoice status.

**Response:** The system returns all AR records for the customer in chronological order showing invoice date, invoice number, original amount, payments applied, outstanding balance, and days outstanding. A summary row at the top shows total outstanding balance and count of overdue invoices. Export to PDF (mPDF, formatted as a customer statement) and Excel available.

---

### FR-AR-004

**Stimulus:** An Accounts Assistant records a credit note against a customer account, specifying the original invoice, credit reason, and credit amount.

**Response:** The system creates a credit note record, reduces the customer's outstanding AR balance by the credit amount, auto-posts to GL (DR Revenue / CR Accounts Receivable for the credit amount), and links the credit note to the original invoice. The credit note is allocated against the original invoice; if the credit exceeds the invoice balance, the excess becomes a credit on the customer account available for future allocation. The system assigns a sequential credit note number in format `CN-YYYY-NNNN`.

## 4.3 AR Aging Analysis

### FR-AR-005

**Stimulus:** An Accounts Assistant or Finance Manager opens the AR Aging dashboard.

**Response:** The system displays a summary aging table with one row per customer showing: customer name, current (not yet due), 1–30 days overdue, 31–60 days overdue, 61–90 days overdue, 91–120 days overdue, and 120+ days overdue, and total outstanding. The aging buckets are calculated as of the current date against each invoice's due date. The data is refreshed on every page load (not batch). Column totals are shown at the bottom. Click-through from any cell to the customer AR detail view.

---

### FR-AR-006

**Stimulus:** A Finance Manager applies filters to the AR Aging dashboard (by customer group, territory, or sales agent).

**Response:** The system filters the aging table to the selected scope and recalculates all bucket totals accordingly. The filtered view is exportable to Excel and PDF.

---

### FR-AR-007

**Stimulus:** An invoice's days-outstanding crosses the 30-day overdue threshold for the first time.

**Response:** The system generates an automated overdue alert sent via email to the Accounts Assistant responsible for the customer account and the Sales Manager, identifying the customer name, invoice number, original amount, due date, and days overdue. The alert is also displayed in the AR dashboard overdue alerts panel.

---

### FR-AR-008

**Stimulus:** An invoice's days-outstanding crosses the 60-day overdue threshold.

**Response:** The system escalates the alert: an additional email is sent to the Finance Director, and the invoice is flagged as `escalated` in the AR aging dashboard with a visual indicator distinguishing it from 30-day overdue items.

## 4.4 Agent Receivable Tracking

### FR-AR-009

**Stimulus:** A user requests the Agent Receivable balance for a specific agent.

**Response:** The system calculates and displays the agent's real-time receivable balance: $\text{Agent Balance} = \sum \text{Invoices issued to agent's customers on credit} - \sum \text{Verified remittances}$. The display shows: total invoices issued, total verified remittances, net outstanding balance, and a list of uncleared invoice lines with individual ages. Agent receivable balances are maintained in the agent sub-ledger, which is a separate ledger from the standard customer AR sub-ledger, reflecting the distinct accountability structure of the agent network.

---

### FR-AR-010

**Stimulus:** An agent's outstanding receivable balance exceeds the configured alert threshold for that agent.

**Response:** The system sends an automated alert to the Sales Manager identifying the agent name, territory, total outstanding balance, threshold value, and count of invoices making up the balance. The alert is also surfaced on the Sales Manager's dashboard. The Sales Manager can acknowledge the alert (which logs the acknowledgement) but cannot dismiss it until the balance falls below the threshold.

---

### FR-AR-011

**Stimulus:** A supervisor verifies a remittance submission from a field agent (per the remittance workflow in F-004).

**Response:** The system executes stored procedure `sp_apply_remittance_to_invoices` which allocates the verified remittance amount to the agent's outstanding invoices in strict FIFO order (BR-002: oldest invoice cleared first). Partial allocation is applied when the remittance is less than the oldest invoice balance. The agent's receivable balance is updated in real time. The GL auto-post is triggered per FR-GL-013. The verifier must be a different user than the remittance submitter (BR-003); the stored procedure validates this before execution and returns an error if the SOD constraint is violated.

**Verification:** Submit a remittance as User A; attempt verification as User A; confirm `ERR_SOD_VIOLATION` is returned and no allocation is applied.

---

### FR-AR-012

**Stimulus:** An Accounts Assistant requests the Agent Receivable Aging report.

**Response:** The system generates a report showing all 1,071 agents with non-zero receivable balances, aged by the same buckets as customer AR (current, 1–30, 31–60, 61–90, 91–120, 120+). The report is sortable by balance descending and by territory. Export to Excel and PDF available.

## 4.5 Customer Credit Control

### FR-AR-013

**Stimulus:** An Accounts Assistant attempts to create a new sales invoice for a customer whose total outstanding AR balance (including the proposed invoice amount) would exceed the customer's configured credit limit.

**Response:** The system blocks the invoice creation and returns error code `ERR_CREDIT_LIMIT_EXCEEDED`, displaying the customer's current outstanding balance, credit limit, and the proposed invoice amount. The invoice cannot be confirmed until the Finance Manager overrides the credit limit for this specific transaction (with override reason logged in the audit trail) or the customer's outstanding balance is reduced by payment.

**Verification:** Set a customer credit limit to UGX 500,000; create invoices totalling UGX 480,000; attempt to create a new invoice for UGX 100,000; confirm `ERR_CREDIT_LIMIT_EXCEEDED`.

---

### FR-AR-014

**Stimulus:** The Finance Manager places a credit hold on a customer account.

**Response:** The system sets the customer's status to `credit_hold`. All subsequent invoice creation attempts for this customer are blocked at the API layer with error code `ERR_CREDIT_HOLD_ACTIVE`, regardless of the outstanding balance relative to the credit limit. The Sales Manager receives an automated notification. The credit hold can only be released by the Finance Manager, and the release is logged in the audit trail with the releasing user's identity and timestamp.

---

### FR-AR-015

**Stimulus:** The Finance Director configures or updates a customer's credit limit.

**Response:** The system saves the new credit limit against the customer record, records the change in the audit trail (old limit, new limit, actor, timestamp), and applies the new limit to all subsequent invoice-creation credit checks from the moment of saving.

## 4.6 Customer Statements

### FR-AR-016

**Stimulus:** An Accounts Assistant generates a customer statement specifying customer name, statement date range, and output format (PDF or email).

**Response:** The system generates a statement showing: BIRDC header, customer name and address, statement date range, opening balance, each invoice and payment transaction within the range (date, reference, description, debit, credit, running balance), and closing outstanding balance. The statement is formatted via mPDF for print-quality output. If email is selected, the system sends the PDF as an attachment to the customer's configured email address via PHPMailer. The sending is logged in the audit trail.

---

### FR-AR-017

**Stimulus:** The system reaches the configured monthly statement generation schedule (e.g., last working day of each month).

**Response:** The system automatically generates statements for all customers with a non-zero balance and sends them to the customers' configured email addresses. Customers with no email address are queued in a physical print list for manual dispatch. A summary report of statements sent and failed deliveries is emailed to the Accounts Assistant.

## 4.7 Payment Receipts

### FR-AR-018

**Stimulus:** An Accounts Assistant records a payment receipt specifying customer, payment method (bank transfer, mobile money, cheque), amount, date, bank reference or mobile money transaction ID, and allocation method.

**Response:** The system creates a payment receipt record with a sequential receipt number in format `RCT-YYYY-NNNN`, performs invoice allocation per FR-AR-002, generates a printable PDF receipt (mPDF), and triggers GL auto-posting per FR-GL-013. The receipt number is assigned from a gap-free sequential series (BR-009).

---

### FR-AR-019

**Stimulus:** An Accounts Assistant requests a Payment Receipt report for a specified date range.

**Response:** The system returns a list of all receipts in the date range, showing receipt number, date, customer, payment method, amount, invoices allocated, and GL journal entry reference. Totals by payment method are shown. Export to Excel and PDF available.

## 4.8 AR Dashboard

### FR-AR-020

**Stimulus:** A Finance Manager opens the AR module dashboard.

**Response:** The system displays: (a) total outstanding AR balance in UGX; (b) AR aging summary bar chart (ApexCharts) showing balances by age bucket; (c) top 10 customers by outstanding balance; (d) count and value of invoices overdue by 30+ days; (e) agent receivable total balance; (f) receipts collected today. All figures are current to the last transaction, not a cached snapshot.

---

### FR-AR-021

**Stimulus:** The Finance Director opens the Executive Dashboard Android app.

**Response:** The app calls the REST API and displays AR summary: total outstanding AR, total agent receivables, and overdue invoice count. Push notification is delivered to the Director when any single customer's balance exceeds a configurable threshold amount. The app requires JWT authentication and respects the same RBAC rules as the web application.

## 4.9 AR Reconciliation

### FR-AR-022

**Stimulus:** The Finance Manager requests an AR reconciliation report for a specific period.

**Response:** The system generates a report reconciling the AR sub-ledger total to the AR control account balance in the GL. The report shows: AR sub-ledger total, GL AR control account balance, variance. A non-zero variance is flagged as `RECONCILIATION_BREAK` and triggers an alert to the Finance Director.

---

### FR-AR-023

**Stimulus:** An Accounts Assistant requests a list of unapplied payments (payments received but not yet allocated to invoices).

**Response:** The system returns all payment receipts with an unallocated balance (partial or full), showing receipt number, date, customer, total amount, allocated amount, and unallocated balance. The unallocated balance ages from the receipt date and appears in a dedicated "Unapplied Payments" panel on the AR dashboard after 7 days.

---

### FR-AR-024

**Stimulus:** The Finance Director requests a bad debt provision review report for a specified period.

**Response:** The system generates a report listing all invoices overdue by 120+ days, showing customer name, invoice number, original amount, outstanding balance, and days overdue. The report provides a total balance subject to potential provision. The Finance Director uses this to create a manual journal entry for bad debt provision; the system does not automatically create provisions without Finance Director instruction (IFRS for SMEs requires judgement-based provisioning).

---

### FR-AR-025

**Stimulus:** An Accounts Assistant requests the AR summary report by territory or sales region.

**Response:** The system aggregates AR outstanding balances by territory (as configured in the Sales module), showing total invoiced, total collected, total outstanding, and collection rate percentage ($\text{Collection Rate} = \frac{\text{Total Collected}}{\text{Total Invoiced}} \times 100$%) per territory. Export to Excel and PDF available.
