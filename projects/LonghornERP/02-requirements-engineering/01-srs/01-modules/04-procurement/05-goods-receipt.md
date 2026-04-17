# Goods Receipt

## 5.1 Goods Receipt Note

**FR-PROC-025** — When a user creates a Goods Receipt Note (GRN), the system shall require selection of the originating PO; the system shall pre-populate line items, ordered quantities, and supplier details from the PO and permit only partial or full quantity entries not exceeding the outstanding PO quantity.

**FR-PROC-026** — When a GRN is confirmed, the system shall post stock movements to the Inventory module, incrementing the on-hand quantity for each received item at the receiving branch, and shall generate the corresponding journal entry (Debit: Stock, Credit: Goods Received Not Invoiced).

**FR-PROC-027** — When a GRN is confirmed against an import supplier, the system shall provide a landed cost allocation screen where the user may distribute additional costs (freight, insurance, import duty, clearing fees) across GRN line items by weight, value, or quantity; the allocated landed cost shall be added to the per-unit stock cost.

**FR-PROC-028** — The system shall allow a standalone GRN (not linked to a PO) for emergency or unplanned receipts; the user shall be required to supply a justification reason, and the standalone GRN shall trigger a post-receipt approval notification to the procurement manager.

**FR-PROC-029** — When goods are returned to a supplier, the system shall create a Goods Return Note (GRN-R) that reverses the original GRN stock movement and the associated GL journal entry.

## 5.2 Barcode and Mobile Capture

**FR-PROC-030** — When a user scans a product barcode during GRN entry, the system shall resolve the barcode to the corresponding item record and auto-populate the item line, reducing manual data entry errors.

**FR-PROC-031** — The system shall support GRN entry on the mobile application; items scanned offline shall be queued and synchronised when network connectivity is restored, with conflict resolution based on the last-confirmed PO outstanding quantity.
