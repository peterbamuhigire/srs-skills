# 5. F-007: Accounts Payable

## 5.1 Module Overview

Module F-007 manages all money owed by BIRDC to vendors and cooperative farmers. It implements three-way matching (BR-012), farmer bulk payment via mobile money, withholding tax deduction and remittance, and AP aging with cash position-aware payment scheduling. All AP transactions post to the GL automatically. Segregation of duties (BR-003) is enforced at the API layer on all payment authorisation steps.

## 5.2 Vendor Invoice Registration

### FR-AP-001

**Stimulus:** An Accounts Assistant submits a vendor invoice for registration, specifying vendor name, invoice number, invoice date, line items (description, quantity, unit price), linked Purchase Order number, and linked GRN number.

**Response:** The system records the vendor invoice and initiates three-way matching per BR-012: (a) it retrieves the linked PO and GRN; (b) it compares the invoice quantity against the GRN received quantity — if the variance exceeds 2%, the system sets the invoice status to `quantity_variance_hold` and notifies the Finance Manager; (c) it compares the invoice unit price against the PO unit price — if the variance exceeds 5%, the system sets the invoice status to `price_variance_hold` and notifies the Finance Manager. If both checks pass, the invoice status is set to `matched` and is ready for payment authorisation. The invoice is assigned a sequential vendor invoice reference number in format `VIN-YYYY-NNNN`.

**Verification:** Register an invoice with a unit price 6% higher than the PO; confirm the invoice status is `price_variance_hold` and a Finance Manager notification is issued.

---

### FR-AP-002

**Stimulus:** The Finance Manager reviews and approves a vendor invoice that is on `price_variance_hold` or `quantity_variance_hold`, providing a written justification.

**Response:** The system records the Finance Manager's justification in the audit trail, clears the hold flag, and transitions the invoice to `matched` status, making it available for payment scheduling. The approval is logged with the Finance Manager's identity, timestamp, and the justification text.

---

### FR-AP-003

**Stimulus:** An Accounts Assistant attempts to process a payment for a vendor invoice that has not been matched to both a PO and a GRN.

**Response:** The system blocks the payment with error code `ERR_THREE_WAY_MATCH_INCOMPLETE`, displaying which of the three documents (PO, GRN, or vendor invoice) is missing or unmatched. The payment cannot be processed until all three documents are matched and the invoice status is `matched` (BR-012 enforcement at API layer).

**Verification:** Attempt to pay an invoice with no linked GRN; confirm `ERR_THREE_WAY_MATCH_INCOMPLETE` with the specific missing document identified.

---

### FR-AP-004

**Stimulus:** An Accounts Assistant requests the AP sub-ledger for a specific vendor, optionally filtered by date range or invoice status.

**Response:** The system returns all AP records for the vendor in chronological order showing invoice date, VIN reference, original amount, payments applied, outstanding balance, and due date. A summary row at the top shows total outstanding balance. Export to PDF and Excel available.

## 5.3 AP Aging

### FR-AP-005

**Stimulus:** An Accounts Assistant or Finance Manager opens the AP Aging dashboard.

**Response:** The system displays a summary aging table with one row per vendor showing: vendor name, current (not yet due), 1–30 days overdue, 31–60 days overdue, 61–90 days overdue, 91–120 days overdue, 120+ days overdue, and total outstanding. Aging is calculated against each invoice's due date as of the current date. Column totals are shown at the bottom. Click-through from any cell to the vendor AP detail view.

---

### FR-AP-006

**Stimulus:** A Finance Manager requests the Payment Due Report for a specified future date range (e.g., next 30 days).

**Response:** The system returns all matched and unpaid vendor invoices with due dates within the specified range, sorted by due date ascending. The report shows: vendor name, VIN reference, invoice amount, UGX outstanding, due date, and payment method preference. A total payable amount for the period is shown at the bottom. Export to Excel and PDF available for cash flow planning.

## 5.4 Vendor Payments

### FR-AP-007

**Stimulus:** An Accounts Assistant initiates a vendor payment specifying the vendor invoice(s) to pay, payment method (bank transfer, mobile money, or cheque), payment amount, and payment date.

**Response:** The system creates a payment voucher in `draft` status, calculates WHT deduction if applicable per FR-AP-016, shows the net payment amount, and presents the voucher for Finance Manager authorisation. The payment is not processed until authorisation is received.

---

### FR-AP-008

**Stimulus:** The Finance Manager authorises a vendor payment voucher that is awaiting approval.

**Response:** The system validates: (a) the authorising user is not the same user who created the voucher (BR-003 — enforced at API layer); (b) the payment amount does not exceed the authorisation threshold for the Finance Manager's role (threshold configurable via UI per DC-002). On success, the system marks the voucher `authorised`. If the payment amount exceeds the Finance Manager's authorisation threshold, the system escalates to Director authorisation before processing.

---

### FR-AP-009

**Stimulus:** An authorised payment voucher is confirmed for processing.

**Response:** The system: (a) records the payment against the vendor invoice(s), reducing the outstanding AP balance; (b) auto-posts to GL per FR-GL-015 (DR Accounts Payable / CR Bank or Cash, and DR WHT Payable if applicable); (c) assigns a sequential payment voucher number in format `PMT-YYYY-NNNN` (BR-009 gap-free series); (d) generates a printable payment voucher PDF (mPDF) for physical signature. For partial payment, the invoice outstanding balance is reduced by the paid amount, and the invoice status is set to `partially paid`.

---

### FR-AP-010

**Stimulus:** An Accounts Assistant records a vendor credit note, specifying the vendor, credit note reference number, amount, and reason.

**Response:** The system creates the credit note record, increases the vendor's AP credit balance by the credit note amount, and makes the credit available for application against future vendor payments. The credit is tracked in the vendor AP sub-ledger and is visible in the vendor AP detail view.

---

### FR-AP-011

**Stimulus:** An Accounts Assistant applies a vendor credit note against an outstanding invoice during payment processing.

**Response:** The system reduces the invoice outstanding balance by the credit note amount, updates the credit note balance (reducing it by the applied amount), and records the application in the audit trail. The net payment amount is adjusted accordingly.

## 5.5 Farmer Payment System

### FR-AP-012

**Stimulus:** The Finance Manager initiates a farmer payment run for a specified cooperative and delivery period, providing the total cooperative batch amount.

**Response:** The system retrieves all individual farmer contribution records for the specified cooperative and period (Stage 3 records from the 5-stage procurement workflow). It validates that every kilogramme in the batch has been allocated to a specific farmer (BR-011 — if any unallocated kg exist, the payment run is blocked with `ERR_INCOMPLETE_CONTRIBUTION_BREAKDOWN`). The system calculates each farmer's gross payable: $\text{Gross Payable} = \text{Weight (kg)} \times \text{Grade Unit Price (UGX/kg)}$.

[CONTEXT-GAP: GAP-002] — MTN MoMo Business API sandbox credentials are required before farmer bulk payment end-to-end testing can be completed.

[CONTEXT-GAP: GAP-003] — Airtel Money API sandbox credentials are required before dual-provider farmer payment testing.

---

### FR-AP-013

**Stimulus:** The farmer payment run has calculated gross payables per farmer. The system applies deductions.

**Response:** For each farmer, the system applies configured deductions in the following order: (a) input loan repayment instalment (from the farmer's active loan schedule in F-010 Farmer Management); (b) cooperative levy (configurable percentage per cooperative); (c) transport and handling charge (configurable rate per kg or flat fee per delivery). Deductions cannot reduce a farmer's net payment below zero — if the sum of deductions exceeds the gross payable, the system caps deductions at the gross payable amount and flags the farmer record for manual review. The net payable is: $\text{Net Payable} = \text{Gross Payable} - \text{Loan Repayment} - \text{Cooperative Levy} - \text{Transport Charge}$.

---

### FR-AP-014

**Stimulus:** The Finance Manager reviews and approves the farmer payment summary, confirming deductions per farmer.

**Response:** The system generates a bulk payment file for MTN MoMo Business API and/or Airtel Money API containing each farmer's name, mobile money number (from the farmer registry in F-010), and net payable amount. The file format matches the API specification for the respective provider. Farmers with no mobile money number registered are separated into a `manual_payment_required` list. The total of all individual payments in the file is verified to equal the approved cooperative net total before the file is submitted.

---

### FR-AP-015

**Stimulus:** The farmer bulk payment file is submitted to the MTN MoMo Business API or Airtel Money API.

**Response:** The system submits the payment file and records the API response for each individual farmer payment: `success` (with transaction ID) or `failed` (with failure reason). Failed payments are queued in a retry list. The system sends an SMS payment confirmation to each farmer whose payment succeeded, per the MTN MoMo or Airtel Money API's messaging capability. All payment outcomes are logged in the audit trail. The GL auto-post is triggered per FR-GL-016 for the total amount of successful payments.

**Verification (requires GAP-002 resolution):** Submit a test payment file to the MTN MoMo sandbox; confirm individual transaction IDs are returned; confirm SMS notifications are triggered; confirm GL posting equals the sum of successful payments only.

## 5.6 Withholding Tax

### FR-AP-016

**Stimulus:** An Accounts Assistant registers a vendor invoice from a local service supplier that is subject to Withholding Tax.

**Response:** The system checks whether the vendor is flagged as WHT-applicable in the vendor record. If WHT applies, the system automatically calculates WHT at the configured rate (current Uganda Income Tax Act rate: 6%) applied to the invoice gross amount: $\text{WHT Amount} = \text{Invoice Gross} \times 0.06$. The system records the WHT amount against the invoice and pre-populates the payment voucher showing: gross invoice amount, WHT deduction, and net payment to vendor. The WHT rate is stored in the configuration table and is updateable by the Finance Director without code changes (DC-002).

---

### FR-AP-017

**Stimulus:** A vendor payment including WHT deduction is processed.

**Response:** The system posts to GL: DR Accounts Payable (gross invoice amount) / CR Bank or Cash (net payment amount) / CR WHT Payable (WHT amount). The WHT Payable account accumulates all deducted WHT until remittance to URA.

---

### FR-AP-018

**Stimulus:** The Finance Director requests a URA WHT Certificate for a specific vendor for a specified period.

**Response:** The system generates a WHT Certificate in the format required by URA, showing: BIRDC name and TIN, vendor name and TIN, payment date(s), gross amount paid, WHT rate, WHT deducted, and net amount paid. The certificate is generated as a PDF (mPDF). The certificate reference number is assigned sequentially per the annual WHT certificate series.

---

### FR-AP-019

**Stimulus:** The Finance Manager initiates the monthly WHT remittance to URA.

**Response:** The system aggregates all WHT Payable amounts posted during the month, generates a WHT remittance schedule listing each vendor, payment date, gross amount, and WHT deducted. On confirmation of remittance to URA, the system posts: DR WHT Payable / CR Bank (remittance amount), and clears the WHT Payable balance for the month. The remittance is recorded in the audit trail with the payment reference.

## 5.7 Payment Scheduling

### FR-AP-020

**Stimulus:** The Finance Manager schedules a payment run for a specified future date, selecting one or more vendor invoices to be paid.

**Response:** The system creates a payment schedule record listing the selected invoices, total amount scheduled, scheduled date, and payment method. Before saving, the system performs a cash position check: it compares the scheduled payment total against the current available cash balance across all bank and cash accounts. If the scheduled total exceeds 80% of available cash, the system displays a warning (not a block) identifying the shortfall risk. The Finance Manager can proceed with acknowledgement.

---

### FR-AP-021

**Stimulus:** A scheduled payment run date arrives.

**Response:** The system sends a reminder notification to the Finance Manager listing all payments due today, the total amount, and the current cash balance. The Finance Manager must manually trigger each payment voucher — the system does not auto-disburse without human confirmation (audit and oversight requirement for PPDA compliance).

## 5.8 AP Reconciliation

### FR-AP-022

**Stimulus:** The Finance Manager requests an AP reconciliation report for a specific period.

**Response:** The system generates a report reconciling the AP sub-ledger total to the AP control account balance in the GL. The report shows: AP sub-ledger total, GL AP control account balance, variance. A non-zero variance is flagged as `RECONCILIATION_BREAK` and triggers an alert to the Finance Director.

---

### FR-AP-023

**Stimulus:** An Accounts Assistant requests a Vendor Statement for a specified vendor and date range.

**Response:** The system generates a vendor statement showing opening balance, all invoices, payments, and credit notes within the date range, and closing outstanding balance. The statement can be sent to the vendor via email or exported as PDF.

---

### FR-AP-024

**Stimulus:** The Finance Director requests an AP summary report by expense category and department.

**Response:** The system aggregates all AP invoices for the specified period by expense account and cost centre, showing total invoiced, total paid, and outstanding by category. Export to Excel and PDF available.

---

### FR-AP-025

**Stimulus:** An Accounts Assistant requests a Goods Received Not Invoiced (GRNI) report.

**Response:** The system returns all GRNs that have been received into inventory but have not yet been matched to a vendor invoice, showing GRN number, date, vendor, items received, PO reference, and the number of days since receipt. Items outstanding beyond 30 days are highlighted. The GRNI balance in the GL equals the total value of unmatched GRNs.

---

### FR-AP-026

**Stimulus:** The Finance Director requires the AP module to track imprest accounts (petty cash floats) per BR-018.

**Response:** The system maintains each imprest account as a sub-ledger under Cash and Bank. A disbursement that would reduce the imprest balance below zero is blocked with error code `ERR_IMPREST_INSUFFICIENT`. All imprest disbursements require a receipt reference and are individually posted to the GL (DR relevant expense account / CR Imprest Cash). Replenishment transactions require Finance Manager approval and are logged in the audit trail.

---

### FR-AP-027

**Stimulus:** An Accounts Assistant requests the Farmer Deduction Report for a specified cooperative and payment period.

**Response:** The system returns an itemised report showing each farmer's gross payable, loan repayment deducted, cooperative levy deducted, transport charge deducted, and net amount paid. The report distinguishes farmers paid via mobile money (with transaction ID) from those on the manual payment list. Export to PDF (mPDF, formatted for cooperative records) and Excel available.

---

### FR-AP-028

**Stimulus:** The Finance Manager requests a Vendor Performance Report for a specified period.

**Response:** The system generates a report per vendor showing: number of invoices received, number of price variances flagged (>5%), number of quantity variances flagged (>2%), average days from GRN to invoice receipt, total value paid, and total WHT deducted. This report feeds the vendor management and procurement evaluation functions in Phase 3 (F-009 Procurement).

---

### FR-AP-029

**Stimulus:** The Finance Director configures a payment authorisation threshold matrix specifying maximum payment amounts per role (Accounts Assistant, Finance Manager, Director) and payment method.

**Response:** The system saves the threshold configuration in `tbl_payment_authorisation_config` and applies it immediately to all subsequent payment vouchers. Payments within the Accounts Assistant's threshold require only Finance Manager approval; payments above the Finance Manager's threshold require Director approval; no payment may proceed without the required level of authorisation. The configuration is updateable by the Finance Director without code changes (DC-002).

---

### FR-AP-030

**Stimulus:** The Finance Director requests a cash flow forecast report for a specified date range.

**Response:** The system generates a cash flow forecast combining: (a) scheduled AP payments from the payment schedule (FR-AP-020); (b) expected AR receipts based on invoice due dates; (c) scheduled farmer payment runs. The forecast shows projected daily closing cash balance across all accounts. The Finance Director uses this to identify cash gap periods and plan for working capital.
