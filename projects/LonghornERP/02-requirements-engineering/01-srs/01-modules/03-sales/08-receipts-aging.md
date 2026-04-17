# Receipts and Debtors Aging Requirements

## 8.1 Overview

The Receipts and Debtors Aging sub-module records customer payments, allocates receipts to open invoices, and provides aging analysis to support cash collection. Overdue alerts automate follow-up communication. This sub-module posts to the accounts receivable ledger; the Accounting module governs bank reconciliation.

## 8.2 Functional Requirements

### 8.2.1 Payment Receipts

**FR-SALES-081:** The system shall create a payment receipt capturing customer, receipt date, amount received, currency, payment method (Cash, Bank Transfer, Mobile Money, or Cheque), payment reference number, and internal notes, when a user with the `sales.receipt.create` permission saves the receipt form.

**FR-SALES-082:** The system shall assign a system-generated receipt number using a tenant-configurable prefix and auto-incrementing sequence (e.g., `RCT-000001`), guaranteeing uniqueness within the tenant, when the receipt is confirmed.

**FR-SALES-083:** The system shall allow the user to allocate a receipt amount to one or more open invoices for the same customer at the time of receipt creation or subsequently, specifying the amount to apply to each selected invoice, where the total allocation may not exceed the receipt amount.

**FR-SALES-084:** The system shall reduce the outstanding balance of each invoice by the amount allocated to it when the receipt allocation is confirmed, and shall post the corresponding credit entry to the customer's accounts receivable ledger account in the Accounting module.

**FR-SALES-085:** The system shall hold any unallocated portion of a receipt as an unapplied credit on the customer's account when the receipt is saved with a total allocation less than the receipt amount, and shall display the unallocated balance on the customer record detail view.

**FR-SALES-086:** The system shall allow a user with the `sales.receipt.allocate` permission to retrospectively allocate an unallocated receipt balance to open invoices for the same customer at any time after the receipt is posted.

**FR-SALES-087:** The system shall prevent reversal of a receipt that has been fully allocated to closed (fully paid) invoices unless the user holds the `sales.receipt.reverse` permission and provides a reversal reason.

### 8.2.2 Debtors Aging

**FR-SALES-088:** The system shall generate a debtors aging report classifying all outstanding invoice balances by the number of days elapsed since each invoice's due date into 5 buckets: 0–30 days, 31–60 days, 61–90 days, 91–120 days, and 120+ days, when a user with the `sales.report.aging` permission runs the report.

**FR-SALES-089:** The system shall allow the user to filter the debtors aging report by one or more of: individual customer, customer category, and assigned sales representative, producing a subtotalled output per selected dimension.

**FR-SALES-090:** The system shall produce the debtors aging report within 8 seconds at P95 when run across all active customers for a tenant.

**FR-SALES-091:** The system shall display, per customer row on the aging report, the customer name, credit limit, total outstanding balance, and the balance distributed across each aging bucket, together with a column showing the balance as a percentage of the credit limit.

**FR-SALES-092:** The system shall allow the user to export the debtors aging report to PDF and to Microsoft Excel (.xlsx) format from the report view.

### 8.2.3 Overdue Alerts

**FR-SALES-093:** The system shall flag an invoice as "Overdue" when the current date exceeds the invoice due date and the invoice has an outstanding balance greater than zero.

**FR-SALES-094:** The system shall send an automated email reminder to the customer's registered email address when an invoice becomes overdue, including the invoice reference, original due date, outstanding amount, and a link to the customer portal (if enabled), subject to the tenant's overdue alert configuration being active.

**FR-SALES-095:** The system shall allow a tenant administrator with the `sales.alerts.configure` permission to configure the overdue alert schedule — specifying the number of days after the due date before the first alert is sent, the interval between subsequent reminders, and the maximum number of reminders per invoice.

**FR-SALES-096:** The system shall record each overdue alert sent against the invoice record — capturing the alert date, recipient email address, and delivery status (Sent or Failed) — to provide an auditable communication history.
