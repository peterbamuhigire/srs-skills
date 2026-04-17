# Persona 5: David — Store Manager

**Profile:** Age 36, Diploma in Business Administration, basic tech literacy. Receives goods into main warehouse, processes transfers to distribution points, manages agent stock issuance, conducts monthly physical stock counts, monitors reorder levels.

**Critical requirement:** Dual-track inventory — warehouse stock and agent stock always clearly separated, never merged except in explicitly labelled consolidated reports.

---

## US-048: Receive Goods Into the Warehouse via Barcode Scan

**US-048:** As David, I want to use the Warehouse Android app to receive goods by scanning barcodes, so that stock receipt is fast and accurate without manual data entry.

**Acceptance criteria:**

- The Warehouse App displays pending GRNs awaiting receipt; David selects the relevant GRN, which pre-fills expected items and quantities from the linked LPO.
- David scans each item's barcode; the app increments the received quantity for the matching product and highlights any item scanned that is not on the GRN.
- When David marks the GRN as complete, the system updates `tbl_stock_balance` for the receiving warehouse location and records the batch number, manufacturing date, and expiry date (for expiry-tracked items).
- The GL is auto-posted (DR Inventory / CR Accounts Payable or DR Raw Material Inventory / CR Cooperative Payable) without any manual journal entry.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-003-001

---

## US-049: Issue Stock to a Field Sales Agent

**US-049:** As David, I want to issue stock to a field sales agent and have the system block the transfer if it would exceed the agent's float limit, so that BIRDC's stock exposure per agent is always controlled.

**Acceptance criteria:**

- David selects the agent and the products and quantities to issue; the system checks the agent's current stock balance value plus the value of the new issuance against the agent's configured float limit (per BR-006).
- If the issuance would exceed the float limit, the system blocks the transfer and displays: "Float limit exceeded. Agent [name] current balance: UGX [amount]. Float limit: UGX [amount]. Issue would exceed limit by UGX [shortfall]. Reduce quantity or contact Sales Manager."
- If the issuance is within the float limit, the system creates a stock transfer record, decrements `tbl_stock_balance` for the warehouse location, and increments `tbl_agent_stock_balance` for the agent — as separate ledger entries that cannot be merged (per BR-001).
- A stock issuance document (delivery note) is generated and can be printed from the Warehouse App or web ERP.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-008

---

## US-050: Run a Physical Stock Count and Approve Variances

**US-050:** As David, I want to run a physical stock count by scanning items and recording quantities, then submit the count for Finance Manager approval before the system is adjusted, so that stock adjustments follow a controlled process.

**Acceptance criteria:**

- David initiates a stock count for a selected location; the system freezes the stock balance for that location (no stock movements allowed during count) and generates a count sheet with expected quantities.
- David uses the Warehouse App to scan items and enter counted quantities; the app calculates the variance (counted minus expected) for each item in real time.
- When David submits the count, the system generates a variance report and routes it to the Finance Manager for approval before any GL adjustment is posted.
- Upon Finance Manager approval, the system auto-posts the stock adjustment (DR/CR Inventory Adjustment account) and the GL is updated; David receives a confirmation notification.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-003-002

---

## US-051: Monitor Product Expiry Dates and Receive Alerts

**US-051:** As David, I want to receive advance alerts when products are approaching their expiry dates, so that BIRDC can take action before selling expired product or incurring a write-off.

**Acceptance criteria:**

- The system generates expiry alerts at 90, 60, and 30 days before expiry for all expiry-tracked products; alert thresholds are configurable by the IT Administrator (per DC-002).
- Alerts are displayed on David's inventory dashboard and sent via email and system notification.
- The expiry alert list shows: product name, batch number, quantity, expiry date, and days remaining.
- FEFO is enforced automatically for all sales, transfers, and production issues — the earliest-expiry batch is always selected first; manual batch selection that violates FEFO is blocked (per BR-007).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-003-003

---

## US-052: Transfer Stock Between Warehouse Locations

**US-052:** As David, I want to transfer stock between BIRDC warehouse locations and track the in-transit status, so that inventory accuracy is maintained during transfers.

**Acceptance criteria:**

- David creates a stock transfer specifying: source location, destination location, product, batch, quantity, and transfer reason.
- When the transfer is initiated, the stock is placed in "in-transit" status: it is decremented from the source location but not yet incremented at the destination.
- The destination location must confirm receipt via the Warehouse App (barcode scan or manual confirmation) to complete the transfer; only then is the destination location balance incremented.
- The GL is auto-posted for inter-location transfers that cross accounting periods or cost centres.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-003-004

---

## US-053: View Consolidated Total Stock Including Agent-Held Inventory

**US-053:** As David, I want to view a consolidated stock report that shows warehouse stock and agent-held stock in separate columns with a clearly labelled total, so that management has a complete picture without the two ledgers being merged.

**Acceptance criteria:**

- The Consolidated Stock Report displays three clearly labelled columns for each product: "Warehouse Stock (qty + value)," "Agent-Held Stock (qty + value)," and "Total Company Stock (qty + value)."
- The warehouse and agent stock figures are sourced from `tbl_stock_balance` and `tbl_agent_stock_balance` respectively; they are never merged in a single ledger (per BR-001).
- David can filter the report by product category, location, or agent.
- The consolidated report total matches the sum of all individual warehouse location stock plus all individual agent stock balances to within 0 units.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-003-005

---

## US-054: Post a Stock Adjustment with GL Auto-Posting

**US-054:** As David, I want to record a stock adjustment (write-off or correction) after Finance Manager approval, with the GL posted automatically, so that inventory and accounting records stay in sync without manual journal entries.

**Acceptance criteria:**

- David creates a stock adjustment request specifying: item, batch, location, quantity (positive for gain, negative for loss), and adjustment reason.
- The adjustment is routed to the Finance Manager for approval; David cannot post the adjustment himself (per BR-003, segregation of duties).
- Upon Finance Manager approval, the system adjusts `tbl_stock_balance` and auto-posts the GL entry (DR/CR Stock Adjustment account vs. Inventory account) using the FIFO cost of the adjusted batch.
- David receives a notification when the adjustment is approved and posted, and can view the posted GL entry from the adjustment record.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-003-006

---

## US-055: Set and Monitor Reorder Levels

**US-055:** As David, I want to configure reorder levels for each product and receive an alert when stock falls below the reorder point, so that I can initiate replenishment before stockouts occur.

**Acceptance criteria:**

- David sets a minimum reorder quantity and a target reorder quantity for each product-location combination in the stock item catalogue.
- When the warehouse stock of any product at any location falls at or below the minimum reorder quantity, the system displays an amber alert on David's inventory dashboard and sends an email notification.
- The alert includes: product name, current quantity, reorder point, and a "Raise Purchase Request" button that pre-fills the purchase request form with the product and reorder quantity.
- Reorder alerts respect the dual-track separation: warehouse reorder alerts are triggered by `tbl_stock_balance` only; agent stock reorder alerts are tracked separately.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-003-007
