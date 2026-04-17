# Non-Functional Requirements — Inventory Management

## 8.1 Overview

The non-functional requirements (NFRs) in this section define measurable quality constraints that the Inventory Management module must satisfy. Each NFR is expressed as a verifiable threshold; no NFR uses subjective qualifiers without an associated IEEE-982.1 metric.

## 8.2 Performance

**NFR-INV-001:** The system shall return the stock level query result for any single item across all warehouses within 2 seconds at the 95th percentile (P95) under a concurrent load of 200 active users.

**NFR-INV-002:** The system shall complete the posting of a Goods Receipt Note (GRN) containing up to 100 line items — including FIFO layer creation or WAC recalculation and journal entry generation — within 3 seconds at P95 under a concurrent load of 200 active users.

**NFR-INV-003:** The system shall generate the stock take variance report for a warehouse containing up to 10,000 distinct item-bin combinations within 5 seconds at P95.

**NFR-INV-004:** The system shall generate the Reorder Report for a tenant with up to 50,000 active SKUs within 8 seconds at P95.

## 8.3 Data Integrity and Correctness

**NFR-INV-005:** The system shall prevent stock going negative when the tenant's `allow_negative_stock` flag is set to `false`; any outbound movement that would cause a negative balance shall be rejected with HTTP 422 and the response body shall include the field `available_qty` showing the current balance.

**NFR-INV-006:** The system shall block any change to an item's `valuation_method` after the first stock movement is posted for that item; an attempt to change the method shall return HTTP 422 with the message "Valuation method cannot be changed after stock movements have been recorded."

**NFR-INV-007:** The system shall ensure that the sum of all FIFO layer `quantity_remaining` values for an item-warehouse combination equals the item's recorded `qty_on_hand` for that warehouse at all times; a background reconciliation job shall run every 6 hours and raise a system alert if any discrepancy exceeds 0 units.

## 8.4 Availability and Reliability

**NFR-INV-008:** The Inventory Management module shall maintain an uptime of ≥ 99.5% per calendar month, measured at the API gateway, excluding scheduled maintenance windows communicated at least 24 hours in advance.

**NFR-INV-009:** The system shall complete a full data backup of the inventory ledger and item master tables within 15 minutes of the scheduled daily backup window, with a Recovery Point Objective (RPO) of ≤ 1 hour and a Recovery Time Objective (RTO) of ≤ 4 hours.

## 8.5 Security and Access Control

**NFR-INV-010:** The system shall enforce role-based access control (RBAC) on all Inventory Management API endpoints such that any request from a user who lacks the required permission returns HTTP 403 Forbidden within 200 ms.

**NFR-INV-011:** All stock movement and item master data transmitted between the client and the server shall be encrypted using TLS 1.2 or higher; connections using TLS 1.1 or earlier shall be rejected.

## 8.6 Scalability

**NFR-INV-012:** The system shall support an item master of up to 500,000 active SKUs per tenant without degradation of query response times beyond the thresholds stated in **NFR-INV-001** and **NFR-INV-002**.

**NFR-INV-013:** The inventory ledger table shall support storage of up to 100,000,000 movement records per tenant without requiring schema changes, through a partitioning strategy defined in the physical database design.

## 8.7 Usability

**NFR-INV-014:** The stock balance inquiry screen shall load and render all items for the default warehouse within 3 seconds at P95 on a device with a minimum 10 Mbps internet connection.

**NFR-INV-015:** The mobile count entry interface for stock takes shall be operable with single-handed thumb navigation on screens ≥ 4.7 inches, meeting WCAG 2.1 Level AA touch-target size requirements (minimum 44 × 44 CSS pixels per interactive element).
