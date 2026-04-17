# Quotations and Sales Orders Requirements

## 4.1 Overview

The Quotations and Sales Orders sub-module manages the pre-invoicing stage of the sales cycle. Quotations capture commercial offers to customers. Accepted quotations convert to Sales Orders (SOs), which trigger stock reservation and govern partial fulfilment and back-order management.

## 4.2 Functional Requirements

### 4.2.1 Quotations

**FR-SALES-026:** The system shall create a quotation capturing a system-generated reference number, quotation date, valid-until date, customer, one or more lines (each with item, quantity, UOM, unit price, discount percentage, tax code, and line total), a subtotal, total tax, and grand total, when a user with the `sales.quotation.create` permission saves the form.

**FR-SALES-027:** The system shall assign a quotation to one of the following statuses — Draft, Sent, Accepted, Rejected, or Expired — and shall automatically transition the status to Expired when the current date exceeds the valid-until date and the quotation has not been accepted or rejected.

**FR-SALES-028:** The system shall record the date and user when a quotation status changes to Sent, Accepted, or Rejected, storing this history against the quotation record.

**FR-SALES-029:** The system shall prevent editing of a quotation that has a status of Accepted, Rejected, or Expired, and shall display the message "This quotation is locked. Create a new version to make changes." when an edit is attempted.

**FR-SALES-030:** The system shall generate a PDF of the quotation — including tenant logo, quotation reference, customer details, line items, totals, valid-until date, and payment terms — when the user selects the "Generate PDF" action on a Sent or Draft quotation.

### 4.2.2 Convert to Sales Order

**FR-SALES-031:** The system shall convert an Accepted quotation to a Sales Order in a single user action, pre-populating all Sales Order fields from the quotation (customer, lines, prices, tax codes, and terms) and allowing the user to edit quantities, prices, and delivery terms before confirming, when the user selects "Convert to Sales Order" on an Accepted quotation.

**FR-SALES-032:** The system shall set the originating quotation status to "Accepted" and link the resulting Sales Order reference back to the quotation when the conversion is confirmed.

### 4.2.3 Sales Orders

**FR-SALES-033:** The system shall create a Sales Order capturing a system-generated reference number, order date, requested delivery date, customer, lines (item, quantity ordered, quantity delivered, quantity invoiced, UOM, unit price, discount %, tax code, line total), subtotal, total tax, and grand total, when a user with the `sales.order.create` permission confirms the order.

**FR-SALES-034:** The system shall reserve the ordered quantity of each stocked item in the specified warehouse at the time the Sales Order is confirmed, reducing the available-to-promise quantity in the Inventory module by the reserved amount.

**FR-SALES-035:** The system shall enforce a configurable approval workflow on Sales Orders — requiring sign-off from a user with the `sales.order.approve` permission before the order is confirmed and stock is reserved — when the tenant has enabled order approval in their configuration settings.

**FR-SALES-036:** The system shall track, per Sales Order line, the quantity ordered, quantity delivered across all associated Delivery Notes, and quantity invoiced across all associated invoices, updating these figures in real time as delivery and invoice events occur.

**FR-SALES-037:** The system shall display a fulfilment status per Sales Order line as one of: Pending, Partially Delivered, Fully Delivered, Partially Invoiced, or Fully Invoiced, derived from the ratio of delivered and invoiced quantities to the ordered quantity.

**FR-SALES-038:** The system shall create a back-order Sales Order for the remaining undelivered quantity of each line when a Delivery Note is posted with a quantity less than the outstanding order quantity, linking the back-order to the originating Sales Order by reference.

**FR-SALES-039:** The system shall allow a user with the `sales.order.cancel` permission to cancel a Sales Order that has not been fully delivered or invoiced, releasing all outstanding stock reservations in the Inventory module and setting the order status to Cancelled.

**FR-SALES-040:** The system shall prevent invoicing a quantity greater than the confirmed Sales Order quantity for a given line without an explicit override by a user with the `sales.order.override` permission, and shall display the message "Invoice quantity [N] exceeds order quantity [M] for item [Item Name]. An override is required." when the limit is reached.
