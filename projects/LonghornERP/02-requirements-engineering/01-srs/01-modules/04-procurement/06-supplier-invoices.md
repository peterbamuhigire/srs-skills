# Supplier Invoices and Three-Way Matching

## 6.1 Invoice Capture

**FR-PROC-032** — When a user captures a supplier invoice, the system shall require linkage to one or more approved POs; the system shall pre-populate line items from the PO and allow the user to confirm the invoiced quantities and unit prices supplied by the vendor.

**FR-PROC-033** — When a supplier invoice is saved, the system shall assign a unique internal identifier in the format `SINV-YYYY-NNNN` and record supplier TIN, invoice number as stated by the supplier, invoice date, due date derived from supplier payment terms, currency, and line-level VAT.

## 6.2 Three-Way Match

**FR-PROC-034** — When a supplier invoice is submitted for matching, the system shall perform a three-way match: (a) compare invoice unit prices against the approved PO, (b) compare invoiced quantities against confirmed GRN quantities, and (c) compare invoice total against PO total including approved amendments. If any variance exceeds the configurable tolerance (default: 0%), the system shall flag the mismatch, prevent payment, and notify the procurement manager.

**FR-PROC-035** — When a three-way match discrepancy is detected, the system shall display a side-by-side comparison of PO value, GRN quantity, and invoice value per line, colour-code mismatched lines in red, and require a named approver to override before proceeding to payment.

## 6.3 WHT Deduction

**FR-PROC-036** — When a supplier invoice is approved for payment and the supplier is marked as subject to WHT, the system shall calculate and display the withholding tax amount: $WHT = InvoiceNet \times WHTRate$ where the default rate is 6% for service suppliers not registered for VAT; the WHT amount shall be deducted from the payment disbursement and posted as a liability to the WHT payable account.

## 6.4 Credit Notes

**FR-PROC-037** — When a user records a supplier credit note, the system shall link it to the originating supplier invoice, reduce the outstanding payable balance, and reverse the corresponding GL debit by posting a credit to the relevant expense or stock account.
