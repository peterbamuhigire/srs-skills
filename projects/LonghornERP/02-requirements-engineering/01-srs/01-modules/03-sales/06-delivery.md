# Delivery Requirements

## 6.1 Overview

The Delivery sub-module manages the physical dispatch of goods to customers. A Delivery Note (DN) records what was dispatched, from which warehouse and bin location, and links to the originating Sales Order or invoice. Posting a Delivery Note reduces inventory and triggers the corresponding stock movement in the Inventory module. Proof of delivery (POD) capture is supported for mobile and document-upload workflows.

## 6.2 Functional Requirements

**FR-SALES-059:** The system shall create a Delivery Note from 2 source types — (1) a confirmed Sales Order or (2) a confirmed Standard Invoice — pre-populating the customer, lines, items, and outstanding quantities, when a user with the `sales.delivery.create` permission initiates the creation.

**FR-SALES-060:** The system shall allow the user to enter, per Delivery Note line, the quantity to dispatch (which may be less than or equal to the outstanding ordered quantity), the source warehouse, and the source bin location, before the Delivery Note is posted.

**FR-SALES-061:** The system shall post a Delivery Note by reducing the on-hand inventory quantity of each dispatched item in the specified warehouse and bin by the dispatched quantity, and by creating a corresponding outbound stock movement record in the Inventory module, when the user with the `sales.delivery.post` permission confirms the posting.

**FR-SALES-062:** The system shall prevent posting of a Delivery Note if the quantity to dispatch for any line exceeds the on-hand quantity in the specified warehouse and bin, and shall display the message "Insufficient stock for [Item Name] in [Warehouse] / [Bin]. Available: [N], Required: [M]." when the check fails.

**FR-SALES-063:** The system shall create a back-order for the undelivered quantity of each Sales Order line when the Delivery Note is posted with a quantity less than the full outstanding order quantity, linking the back-order to the originating Sales Order, consistent with FR-SALES-038.

**FR-SALES-064:** The system shall generate a printable PDF of the Delivery Note — including tenant name, delivery note number, delivery date, customer name, delivery address, line items (item, quantity, UOM), driver name field, and customer signature field — within 3 seconds at P95 when the user selects "Generate PDF".

**FR-SALES-065:** The system shall allow a user to record proof of delivery by one of 2 methods: (1) capturing a customer signature via mobile device touch input directly in the Longhorn ERP mobile application, or (2) uploading a scanned POD document (PDF or image file ≤ 10 MB), attaching the proof to the Delivery Note record.

**FR-SALES-066:** The system shall display the proof-of-delivery status — Not Captured, Signature Captured, or Document Uploaded — on the Delivery Note detail view and on the Sales Order delivery summary.

**FR-SALES-067:** The system shall assign a system-generated Delivery Note number using a tenant-configurable prefix and auto-incrementing sequence (e.g., `DN-000001`), guaranteeing uniqueness within the tenant, when the Delivery Note is saved.

**FR-SALES-068:** The system shall link each posted Delivery Note to its source Sales Order or invoice, and shall reflect the cumulative delivered quantities on the Sales Order fulfilment status per FR-SALES-036 in real time after posting.

**FR-SALES-069:** The system shall allow a user with the `sales.delivery.cancel` permission to cancel a Delivery Note that has not yet been used to generate an invoice, reversing the associated stock movement in the Inventory module and restoring the on-hand and reserved quantities to their pre-posting values.

**FR-SALES-070:** The system shall prevent cancellation of a Delivery Note that has already been fully or partially invoiced, and shall display the message "Delivery note [DN reference] has associated invoices. Cancel the invoices before cancelling this delivery." when cancellation is attempted.
