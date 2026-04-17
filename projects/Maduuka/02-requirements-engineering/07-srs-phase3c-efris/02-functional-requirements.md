---
title: "SRS Phase 3c -- EFRIS Compliance: Functional Requirements"
project: "Maduuka"
version: "1.0"
date: "2026-04-05"
status: "Draft -- BLOCKED pending GAP-005"
---

# Section 2: Functional Requirements -- EFRIS Compliance (F-015)

All requirements in this section are scoped to Phase 3c. Requirements follow stimulus-response format per IEEE 830. Requirements tagged **[BLOCKED: GAP-005]** depend on live URA EFRIS API access and shall not be implemented until URA accreditation is complete. Design, data modelling, and UI work for blocked requirements may proceed.

---

## 2.1 EFRIS Configuration

### 2.1.1 Module Activation

**FR-EFR-001:** When a Business Owner activates the EFRIS module for their tenant, the system shall require entry of: URA TIN (required, validated against the URA TIN format), EFRIS device serial number as issued by URA (required), and EFRIS API credentials (client ID and client secret) issued by URA upon accreditation (required). The system shall not allow EFRIS to be enabled without all three fields populated. **[BLOCKED: GAP-005]**

**FR-EFR-002:** When EFRIS credentials are saved, the system shall perform a connectivity test by calling the URA EFRIS API health-check endpoint. If the test succeeds, the system shall display a "Connected" status indicator. If the test fails, the system shall display the URA error code and reason and prevent EFRIS from going live until the error is resolved. **[BLOCKED: GAP-005]**

**FR-EFR-003:** When the EFRIS module is activated for a tenant, the system shall apply EFRIS submission logic to all new sales and invoices from the activation timestamp onwards. Historic transactions prior to activation shall not be retroactively submitted to URA unless explicitly triggered by the Business Owner via the reconciliation tool.

**FR-EFR-004:** When the Business Owner deactivates the EFRIS module, the system shall suspend all future URA submissions, retain all FDNs and submission records in the database, and display a deactivation warning stating that receipts issued after deactivation will not carry an FDN.

### 2.1.2 Product Catalogue Synchronisation

**FR-EFR-005:** When the EFRIS module is activated, the system shall initiate an initial product catalogue synchronisation, mapping each active Maduuka product to a commodity code in the URA EFRIS standard commodity catalogue. Products without a mapping shall be listed in a pending-mapping queue that the user must resolve before those products can be included in EFRIS-submitted invoices. **[BLOCKED: GAP-005]**

**FR-EFR-006:** When a new product is created in the Maduuka catalogue and EFRIS is active, the system shall prompt the user to map the new product to a URA EFRIS commodity code before the product can be sold through the EFRIS-enabled POS. The system shall allow the sale to proceed without a commodity code mapping only if the product is flagged as EFRIS-exempt by the Business Owner. **[BLOCKED: GAP-005]**

**FR-EFR-007:** When an existing product's name, category, or tax classification is updated, the system shall flag the product for catalogue re-synchronisation and submit the updated mapping to the URA EFRIS catalogue API within 24 hours of the change. **[BLOCKED: GAP-005]**

### 2.1.3 Tax Category Mapping

**FR-EFR-008:** When a user maps a Maduuka tax category to an EFRIS tax code, the system shall accept the following mappings and transmit the corresponding URA tax code in all EFRIS submissions for products in that category:

- VAT 18% (standard-rated) → URA EFRIS tax code for standard VAT
- Zero-rated → URA EFRIS tax code for zero-rated supply
- Exempt → URA EFRIS tax code for exempt supply

**[BLOCKED: GAP-005]** for the specific URA tax code values, which must be obtained from the URA EFRIS API specification upon accreditation.

**FR-EFR-009:** When a product has no EFRIS tax code mapping and a sale including that product is submitted to URA, the system shall block the EFRIS submission, flag the product as `[EFRIS-TAX-UNMAPPED]`, and alert the Business Owner to complete the mapping before the sale is accepted.

**FR-EFR-010:** When a user updates the tax category mapping configuration, the system shall apply the new mapping to all subsequent EFRIS submissions. Submissions already confirmed with an FDN shall not be retroactively altered.

---

## 2.2 Fiscal Invoice Generation

### 2.2.1 Submission at Point of Sale

**FR-EFR-011:** When a sale is completed at the POS (FR-POS-016 triggered), and EFRIS is active for the tenant, the system shall submit the transaction data to the URA EFRIS API before the receipt is printed or sent to the customer. The receipt shall not be issued until either an FDN is received or the transaction enters offline queue status (FR-EFR-018). **[BLOCKED: GAP-005]**

**FR-EFR-012:** When submitting a transaction to the URA EFRIS API, the system shall transmit at minimum: seller TIN, EFRIS device serial number, transaction date and time, transaction type (B2C / B2B / B2G), buyer TIN (B2B only), procurement reference (B2G only), itemised product list with commodity codes, quantities, unit prices, VAT amount per line, total amount, and payment method. **[BLOCKED: GAP-005]**

**FR-EFR-013:** When the URA EFRIS API returns a successful response, the system shall extract the FDN and QR code from the response, store them against the transaction record, and proceed to receipt generation. The FDN and QR code shall be included on every printed, PDF, WhatsApp, and SMS receipt format.

**FR-EFR-014:** When the URA EFRIS API returns an error response, the system shall display the URA error code and description to the cashier, log the failure in the failed-submission queue, and allow the cashier to retry the EFRIS submission or, with manager authorisation, issue the receipt in `EFRIS_FAILED` status with a mandatory failure reason recorded. **[BLOCKED: GAP-005]**

### 2.2.2 Transaction Types

**FR-EFR-015:** When a cashier selects the transaction type at POS as B2B, the system shall require entry of the buyer's URA TIN before the sale can be submitted to EFRIS. The TIN field shall be validated for the correct URA TIN format (numeric, correct digit count per URA specification). **[BLOCKED: GAP-005]**

**FR-EFR-016:** When a cashier selects the transaction type at POS as B2G, the system shall require entry of the government entity's procurement reference number before the sale can be submitted to EFRIS. **[BLOCKED: GAP-005]**

**FR-EFR-017:** When a cashier processes a B2C transaction, the system shall submit the sale to EFRIS without a buyer TIN. The URA EFRIS system shall be responsible for classifying the transaction as anonymous B2C per its own rules. **[BLOCKED: GAP-005]**

### 2.2.3 Offline Queuing

**FR-EFR-018:** When the URA EFRIS API is unreachable (network timeout exceeding the configured API timeout -- see NFR-EFR-P-001), the system shall:

1. Store the complete transaction payload in the local offline queue with status `PENDING_EFRIS`.
2. Issue a receipt to the customer marked with `EFRIS STATUS: PENDING -- FDN to be issued`.
3. Display a notification to the cashier that EFRIS submission is queued and the receipt is provisional.

**FR-EFR-019:** When URA EFRIS server connectivity is restored after an offline period, the system shall automatically process the offline queue in chronological order, submitting each queued transaction to URA without user intervention. The queue shall be processed within 30 seconds of connectivity restoration for queues of up to 500 transactions. **[BLOCKED: GAP-005]**

**FR-EFR-020:** When a queued transaction receives its FDN from URA upon queue processing, the system shall update the transaction record with the FDN and QR code, change the transaction status from `PENDING_EFRIS` to `CONFIRMED_EFRIS`, and send the customer an updated receipt with the FDN via SMS or WhatsApp if the customer has a registered phone number.

**FR-EFR-021:** When a transaction in the offline queue fails URA submission after 3 automatic retry attempts (configurable), the system shall move the transaction to the failed-submission queue, change its status to `EFRIS_FAILED`, and alert the Business Owner via push notification. **[BLOCKED: GAP-005]**

### 2.2.4 Credit Notes and Debit Notes

**FR-EFR-022:** When a sale that has a confirmed FDN is voided (FR-POS-024), the system shall automatically generate an EFRIS credit note referencing the original FDN and submit it to the URA EFRIS API. The credit note shall record the full reversal amount. **[BLOCKED: GAP-005]**

**FR-EFR-023:** When a partial refund is processed for a sale that has a confirmed FDN (FR-POS-025), the system shall generate an EFRIS credit note for the refunded amount, referencing the original FDN, and submit it to URA. The credit note shall record only the refunded line items and amounts. **[BLOCKED: GAP-005]**

**FR-EFR-024:** When a price adjustment upward is applied to an already-invoiced transaction with a confirmed FDN, the system shall generate an EFRIS debit note for the additional amount, referencing the original FDN, and submit it to URA. **[BLOCKED: GAP-005]**

**FR-EFR-025:** When a credit note or debit note is submitted to URA EFRIS and receives a confirmation, the system shall store the URA response reference number, link it to the original FDN, and update the transaction record status to `CREDIT_NOTE_CONFIRMED` or `DEBIT_NOTE_CONFIRMED` respectively.

---

## 2.3 EFRIS Status Dashboard

### 2.3.1 Real-Time Submission Status

**FR-EFR-026:** When a user opens the EFRIS Status Dashboard, the system shall display the following real-time counters for the current business day (refreshed every 2 minutes):

- Confirmed submissions (transactions with a confirmed FDN)
- Pending submissions (transactions in the offline queue with status `PENDING_EFRIS`)
- Failed submissions (transactions with status `EFRIS_FAILED`)
- Credit notes confirmed
- Debit notes confirmed

**FR-EFR-027:** When a user selects a date range on the EFRIS Status Dashboard, the system shall update all counters to reflect the submission status for the selected period.

### 2.3.2 Failed Submission Queue

**FR-EFR-028:** When a user views the failed submission queue on the EFRIS Status Dashboard, the system shall list all transactions with `EFRIS_FAILED` status, showing for each: transaction date and time, receipt number, transaction type, total amount, URA error code, error description, number of retry attempts, and a "Retry" button.

**FR-EFR-029:** When a user clicks "Retry" on a failed submission, the system shall resubmit the transaction payload to the URA EFRIS API immediately. If the resubmission succeeds, the system shall update the transaction status to `CONFIRMED_EFRIS` and remove it from the failed queue. If it fails again, the system shall update the retry count and display the new error. **[BLOCKED: GAP-005]**

**FR-EFR-030:** When a user applies a bulk retry to all failed submissions, the system shall process the queue in chronological order, applying the same retry logic as FR-EFR-029 for each record. **[BLOCKED: GAP-005]**

### 2.3.3 Monthly Reconciliation

**FR-EFR-031:** When a user initiates the monthly EFRIS reconciliation for a selected month, the system shall:

1. Calculate the total sales value recorded in Maduuka for the month (from confirmed sales records).
2. Retrieve the total EFRIS-submitted transaction value for the same month from the local EFRIS submission log.
3. Display both totals and the variance (Maduuka Total - EFRIS Submitted Total).

Transactions in `PENDING_EFRIS` or `EFRIS_FAILED` status shall be listed separately as unreconciled items.

**FR-EFR-032:** When the reconciliation variance is non-zero, the system shall flag each unmatched transaction category (pending, failed, voided-without-credit-note) as a reconciliation discrepancy item and provide a drill-down view listing the individual transactions contributing to the variance.

---

## 2.4 EFRIS Compliance Reports

**FR-EFR-033:** When a user requests the monthly EFRIS submission report for a selected month, the system shall list all transactions submitted to URA in the period, showing for each: date, receipt number, FDN, transaction type (B2C/B2B/B2G), total amount, VAT amount, and submission status. The report shall include totals per transaction type and an overall total.

**FR-EFR-034:** When a user requests the failed submission report, the system shall list all transactions that failed URA EFRIS submission within the selected date range, showing: transaction date, receipt number, error code, error description, retry count, and current status. Transactions that have since been successfully resubmitted shall be included but marked as `RESOLVED`.

**FR-EFR-035:** When a user requests the reconciliation report for a selected month, the system shall produce a summary document showing: total Maduuka sales value, total EFRIS-confirmed value, total pending value, total failed value, net variance, and a listing of all discrepancy items per FR-EFR-032.

**FR-EFR-036:** When a user exports any EFRIS compliance report, the system shall generate the report in PDF and CSV formats. The PDF shall include the business name, TIN, branch, report type, report period, and generation date in the header. Export shall complete within 30 seconds for periods of up to 12 months.

**FR-EFR-037:** When a user requests the credit and debit note report for a period, the system shall list all credit notes and debit notes submitted to URA, showing: original FDN, note type (credit/debit), note date, URA reference number, amount, and status.

**FR-EFR-038:** When a user configures a scheduled EFRIS submission report, the system shall automatically generate and email the monthly EFRIS submission report (FR-EFR-033) to the configured email address on the first business day of each month, covering the prior month.
