# Invoicing Requirements

## 5.1 Overview

The Invoicing sub-module generates the financial claim against a customer for goods delivered or services rendered. It supports standard, pro-forma, and recurring invoice types. Tax calculation, EFRIS submission flagging for Uganda-profile tenants, and PDF generation are integral to this sub-module. Revenue recognition postings are governed by the Accounting module; this SRS specifies the sales-side trigger events only.

## 5.2 Functional Requirements

### 5.2.1 Invoice Types

**FR-SALES-041:** The system shall support 3 invoice types — Standard Invoice, Pro-Forma Invoice, and Recurring Invoice — selectable at the time of invoice creation, each governed by the rules specified in FR-SALES-042 through FR-SALES-058.

**FR-SALES-042:** The system shall post a Standard Invoice to the accounts receivable ledger and update the customer's outstanding balance when the invoice is approved or, if no approval workflow is configured, when the invoice is saved in "Confirmed" status.

**FR-SALES-043:** The system shall treat a Pro-Forma Invoice as a non-posting document — no ledger entry, no stock movement, and no effect on the customer balance — and shall display a watermark reading "PRO-FORMA — NOT A TAX INVOICE" on the generated PDF.

### 5.2.2 Creating an Invoice

**FR-SALES-044:** The system shall allow a user with the `sales.invoice.create` permission to create a Standard Invoice from 3 source types: (1) directly, with no source document; (2) from a confirmed Sales Order, pre-populating all matching fields; or (3) from a posted Delivery Note, pre-populating lines from the confirmed delivered quantities.

**FR-SALES-045:** The system shall capture on each invoice line: item or service description, quantity, UOM, unit price, discount percentage, tax code, and line total, where line total is calculated as:

$LineTotal = Qty \times UnitPrice \times (1 - DiscountPct \div 100)$

**FR-SALES-046:** The system shall auto-apply the VAT rate associated with the selected tax code to each invoice line, display the tax amount per line, and display a consolidated tax total on the invoice footer, when the tax code is set.

**FR-SALES-047:** The system shall assign invoice numbers using a tenant-configurable prefix concatenated with a zero-padded auto-incrementing sequence (e.g., `INV-000001`), guaranteeing uniqueness within the tenant, when a new invoice is confirmed.

**FR-SALES-048:** The system shall display the customer's credit limit and current outstanding balance on the invoice creation screen, and shall apply the credit limit check defined in FR-SALES-006 before the invoice is saved in Confirmed status.

### 5.2.3 Approval Workflow

**FR-SALES-049:** The system shall route a newly created invoice to a user with the `sales.invoice.approve` permission for approval before it is posted to the ledger, when the tenant has enabled invoice approval in their configuration settings; the invoice shall remain in "Pending Approval" status until approved or rejected.

**FR-SALES-050:** The system shall notify the approver by in-app notification and email when an invoice enters "Pending Approval" status, including the invoice reference, customer name, and total amount in the notification body.

### 5.2.4 EFRIS Integration

**FR-SALES-051:** The system shall set the `efris_submission_required` flag to `true` on every Standard Invoice created within a Uganda-profile tenant, and shall defer the actual EFRIS submission event and response handling to the Platform Integration Layer (FR-INTG series), when the invoice is confirmed.

**FR-SALES-052:** The system shall display the EFRIS submission status — Pending, Submitted, Accepted, or Failed — on the invoice detail view for Uganda-profile tenants, and shall render the EFRIS-issued QR code on the invoice PDF once the status is Accepted.

### 5.2.5 PDF Generation

**FR-SALES-053:** The system shall generate a PDF rendering of the invoice — including tenant logo, tenant name, physical address, TIN, VAT number, invoice number, invoice date, due date, customer name, customer TIN, line items (description, qty, UOM, unit price, discount, line total), tax breakdown, grand total, payment terms, and bank details — within 3 seconds at P95 when the user selects "Generate PDF" or the invoice is sent by email.

**FR-SALES-054:** The system shall embed the EFRIS QR code in the invoice PDF for Uganda-profile tenants when the EFRIS submission status is Accepted, positioned in the footer of the first page.

### 5.2.6 Recurring Invoices

**FR-SALES-055:** The system shall allow a user with the `sales.invoice.create` permission to configure a recurring invoice template specifying customer, invoice lines, frequency (weekly, monthly, quarterly, or annually), start date, and optional end date.

**FR-SALES-056:** The system shall auto-generate a Standard Invoice from a recurring template on its scheduled date, assign the next invoice number in the tenant sequence, and post the invoice to the accounts receivable ledger, without requiring manual user intervention.

**FR-SALES-057:** The system shall send the auto-generated recurring invoice to the customer's registered email address immediately after generation, when the recurring template has the "Auto-send" option enabled.

**FR-SALES-058:** The system shall create an in-app alert for the tenant administrator listing all recurring invoices generated in the past 24 hours when the daily recurring invoice job completes, so that administrators can review auto-posted invoices.
