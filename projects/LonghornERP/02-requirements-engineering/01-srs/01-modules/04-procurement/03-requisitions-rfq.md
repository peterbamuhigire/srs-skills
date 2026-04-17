# Purchase Requisitions and Request for Quotation

## 3.1 Purchase Requisition

**FR-PROC-009** — When a user submits a Purchase Requisition (PR), the system shall assign a unique identifier in the format `PR-YYYY-NNNN`, record the requesting user, department, item descriptions, estimated quantities, required-by date, and justification narrative.

**FR-PROC-010** — When a PR is submitted, the system shall route it through the tenant-configured approval workflow; the system shall block conversion of an unapproved PR to an RFQ or Purchase Order (PO).

**FR-PROC-011** — When a PR approver approves or rejects a PR, the system shall notify the requesting user via in-app notification and email, recording the approver identity and decision timestamp in the audit log.

**FR-PROC-012** — The system shall enforce PPDA method-selection thresholds on PRs: if the estimated value exceeds the configurable direct-procurement ceiling `[CONTEXT-GAP: GAP-006 — PPDA current threshold values]`, the system shall flag the PR as requiring open tender and prevent direct supplier selection.

## 3.2 Request for Quotation

**FR-PROC-013** — When a user converts an approved PR to an RFQ, the system shall copy all line items from the PR to the RFQ, assign a unique identifier in the format `RFQ-YYYY-NNNN`, and allow the user to add or remove suppliers to receive the solicitation.

**FR-PROC-014** — When a user dispatches an RFQ, the system shall generate a PDF quotation request document branded with the tenant logo and transmit it to each selected supplier via email; the RFQ PDF shall include item descriptions, quantities, delivery location, and quotation deadline.

**FR-PROC-015** — When a supplier quotation response is captured, the system shall store unit price, currency, delivery lead time, validity period, and any supplier notes against the corresponding RFQ line.

**FR-PROC-016** — The system shall provide a side-by-side supplier comparison view that ranks all received quotations by unit price per line item, flags the lowest price, and highlights items where the price variance across suppliers exceeds a configurable threshold.
