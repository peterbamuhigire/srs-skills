# Purchase Orders

## 4.1 PO Creation and Approval

**FR-PROC-017** — When a user creates a Purchase Order (PO), the system shall assign a unique identifier in the format `PO-YYYY-NNNN`, record supplier, line items with item code, description, ordered quantity, agreed unit price, currency, and expected delivery date.

**FR-PROC-018** — When a PO is submitted for approval, the system shall enforce the tenant-configured multi-level approval matrix based on PO value; the system shall lock the PO for editing until the approval process completes.

**FR-PROC-019** — When an approver approves a PO, the system shall stamp the approval with the approver identity, role, and timestamp; when all required approval levels confirm, the system shall transition the PO status to "Approved" and permit issuance to the supplier.

**FR-PROC-020** — When a user issues an approved PO to the supplier, the system shall generate a PDF Local Purchase Order (LPO) branded with the tenant logo and transmit it via email; the LPO shall display all line items, agreed prices, delivery address, and authorised signatory.

## 4.2 PO Amendment

**FR-PROC-021** — When a user amends an issued PO (quantity or price change), the system shall create a new PO revision, increment the revision counter, and re-route the amended PO through the full approval workflow before re-issuing.

**FR-PROC-022** — The system shall maintain a complete revision history for every PO, recording each version's line items, values, approvals, and issuance timestamps; this history shall be read-only and non-deletable.

## 4.3 PO Closure

**FR-PROC-023** — When a PO reaches fully received status (all line quantities receipted via GRN), the system shall automatically transition the PO status to "Closed" and prevent further goods receipt entries against it.

**FR-PROC-024** — When a user manually closes a partial PO, the system shall record the closure reason and the unreceived quantity against each line and flag the closure in the audit log.
