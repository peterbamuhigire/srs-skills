# Supplier Payments and Creditors Aging

## 7.1 Payment Processing

**FR-PROC-038** — When a user schedules a supplier payment, the system shall display all outstanding approved invoices for the selected supplier, allow multi-invoice selection, and confirm the net amount after deducting any pending WHT and credit notes.

**FR-PROC-039** — When a payment is confirmed, the system shall post the journal entry (Debit: Accounts Payable, Credit: Bank/Cash), update the outstanding invoice balance to zero or the remaining unpaid amount, and record payment date, amount, payment method, and the bank account debited.

**FR-PROC-040** — The system shall support the following payment methods: bank transfer (with reference number), mobile money (MTN MoMo or Airtel Money — bulk disbursement), and cash; the payment method shall be recorded on each payment record.

**FR-PROC-041** — When a payment is applied to multiple invoices, the system shall allocate the payment amount across invoices in oldest-first order (FIFO allocation) by default; users shall be permitted to override allocation manually.

## 7.2 Payment Runs

**FR-PROC-042** — The system shall provide a batch payment-run function that selects all approved invoices with a due date on or before a user-specified cut-off date, computes the total payable per supplier, and generates a payment summary report before final confirmation.

**FR-PROC-043** — When a payment run is confirmed, the system shall generate a bank payment file in the tenant's configured format and post all payment journal entries simultaneously within a single database transaction.

## 7.3 Creditors Aging

**FR-PROC-044** — The system shall provide a creditors aging report that groups outstanding payables by supplier into the following buckets: current (0–30 days), 31–60 days, 61–90 days, and > 90 days; the report shall display totals per bucket and a grand total per supplier.

**FR-PROC-045** — The creditors aging report shall be exportable as PDF and XLSX and shall reflect balances as at a user-specified report date.
