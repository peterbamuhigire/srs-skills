# Returns and Credit Notes Requirements

## 7.1 Overview

The Returns and Credit Notes sub-module manages the reversal of delivered goods and the issuance of financial credit to the customer. Every return must reference a source document. Credit notes generated from approved returns reduce the customer's outstanding balance and can be applied against open invoices or held as a credit on account. Returned stock is received back into a designated warehouse and bin.

## 7.2 Functional Requirements

**FR-SALES-071:** The system shall create a Sales Return record referencing exactly one source document — either an original Standard Invoice or a posted Delivery Note — and pre-populating the customer, return date, and returnable lines with their original quantities, when a user with the `sales.return.create` permission initiates the return.

**FR-SALES-072:** The system shall require the user to enter, per return line, the quantity being returned (which may not exceed the original quantity on the source document line), a return reason selected from a configurable list (Customer Complaint, Wrong Item Delivered, Damaged Goods, or Other), and the destination warehouse and bin for restocking.

**FR-SALES-073:** The system shall route a submitted Sales Return to a user with the `sales.return.approve` permission for approval before the return is posted, when the tenant has enabled return approval in configuration settings; the return shall remain in "Pending Approval" status until approved or rejected.

**FR-SALES-074:** The system shall auto-generate a Credit Note upon approval of a Sales Return, setting the credit note amount to the sum of the returned line totals including applicable VAT, and linking the Credit Note to the originating Sales Return and source invoice by reference.

**FR-SALES-075:** The system shall post the return stock receipt to the Inventory module — increasing the on-hand quantity of each returned item in the specified destination warehouse and bin by the approved return quantity — when the Sales Return is approved and posted.

**FR-SALES-076:** The system shall assign a system-generated Credit Note number using a tenant-configurable prefix and auto-incrementing sequence (e.g., `CN-000001`), guaranteeing uniqueness within the tenant, when the Credit Note is created.

**FR-SALES-077:** The system shall allow a user with the `sales.creditnote.apply` permission to allocate a Credit Note against one or more open invoices for the same customer, reducing the outstanding balance of each selected invoice by the allocated amount, up to the full Credit Note value.

**FR-SALES-078:** The system shall hold the unapplied balance of a Credit Note as a credit on the customer's account when the Credit Note has not been fully allocated to open invoices, and shall display the unapplied credit balance on the customer record detail view.

**FR-SALES-079:** The system shall generate a PDF of the Credit Note — including tenant name, credit note number, credit note date, reference to the originating invoice, customer name, line items (description, qty returned, unit price, line credit amount), total VAT credited, and total credit amount — within 3 seconds at P95 when the user selects "Generate PDF".

**FR-SALES-080:** The system shall post the Credit Note reversal to the accounts receivable ledger — reducing the customer's outstanding balance by the credit note total and recording the reverse revenue entry in the Accounting module — when the Credit Note is confirmed and approved.
