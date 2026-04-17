## 3.3 Module F-003: Inventory and Warehouse Management

### 3.3.1 Overview

Module F-003 manages all physical warehouse stock across unlimited named locations, enforces dual-track inventory separation (BR-001), tracks batches and expiry dates, enforces FEFO (BR-007), manages stock transfers, and supports physical stock counts. It is the stock authority that all other modules (Sales, POS, Agent Distribution, Production) query for available stock.

### 3.3.2 Functional Requirements — Inventory and Warehouse Management

---

**FR-INV-001** — Warehouse Location Management

When an IT Administrator or Store Manager creates a warehouse location, the system shall capture: location code, location name, location type (main finished goods, packaging store, cold store, returns bay, distribution staging, or custom), physical address, and whether the location holds product for sale. The system shall support an unlimited number of named locations. Each location shall maintain its own stock balance, visible independently and in aggregate.

*Traceability: BG-004 (circular economy visibility), DC-002.*

---

**FR-INV-002** — Stock Item Catalogue — Create and Manage

When a Store Manager or authorised user creates a stock item, the system shall capture: item code (unique, system-generated or manual), item name, category, base UOM, all price tiers (wholesale, retail, export, institutional), cost price, FEFO flag (yes/no), batch tracking flag (yes/no), reorder level, reorder quantity, and item status (active/discontinued). All catalogue changes shall be logged in the audit trail.

*Traceability: DC-002, DC-003.*

---

**FR-INV-003** — UOM Conversion Engine

When a stock item has multiple units of measure (e.g., a bag sold by kg), the system shall store: the base UOM, all alternative UOMs, and the conversion factor from each alternative UOM to the base UOM. All internal stock balance calculations and GL postings shall use the base UOM. Conversion factors shall be configurable by the Store Manager without developer involvement (DC-002). The UOM conversion engine shall be used consistently across all modules that reference stock quantities.

*Traceability: DC-002, BG-004.*

---

**FR-INV-004** — Dual-Track Inventory Architecture Enforcement

The system shall maintain warehouse stock exclusively in `tbl_stock_balance` (keyed by item, location, batch) and agent stock exclusively in `tbl_agent_stock_balance` (keyed by item, agent, batch). No database view, stored procedure, or application layer query shall ever join these two tables in a way that produces a merged stock balance without an explicit label identifying warehouse stock and agent stock separately. This constraint shall be enforced by a database-level check and documented in the data dictionary.

*Traceability: BR-001.*

---

**FR-INV-005** — Batch and Lot Registration

When goods are received into any warehouse location, the system shall require the following for each batch of an expiry-tracked or batch-tracked product: batch number (supplier's or system-generated), manufacturing date (if known), expiry date (mandatory for food products), supplier or production order reference, and quantity received. All subsequent stock movements for this batch shall reference the batch record by foreign key.

*Traceability: BR-007, BG-002.*

---

**FR-INV-006** — FEFO Automatic Batch Selection

When stock is allocated for a sale, POS transaction, transfer, or agent issuance involving an expiry-tracked product, the system shall automatically select the batch with the earliest expiry date at the source location. The selection logic shall be: order batches by expiry date ascending, and allocate from the first batch until exhausted before moving to the next. The allocated batch number shall be recorded against every stock movement and invoice line item. Manual batch selection that would violate FEFO order shall be rejected at the API layer.

*Traceability: BR-007.*

---

**FR-INV-007** — Expiry Date Alert: 30/60/90-Day Thresholds

When the system's daily batch job runs (scheduled at 06:00 EAT each day), the system shall identify all batches whose expiry date is within the configured alert thresholds (default: 30, 60, and 90 days), generate a dashboard widget on the Store Manager and Sales Manager's home screen listing all near-expiry batches with quantities and locations, and send an email notification to the Store Manager and Sales Manager listing the same batches. Alert thresholds shall be configurable per product category (DC-002).

*Traceability: BR-007, DC-002, DC-003.*

---

**FR-INV-008** — Expired Batch Blocking

When the system's daily batch job identifies a batch whose expiry date has passed, the system shall set the batch status to `expired`, prevent that batch from being allocated to any sale, POS transaction, or transfer, and generate an alert to the Store Manager for stock write-off action. Expired stock shall be moved to the `returns bay` location by the Store Manager and written off via a stock adjustment (FR-INV-020) with GL posting.

*Traceability: BR-007, DC-003.*

---

**FR-INV-009** — Stock Receipt into Warehouse

When a Store Manager records a stock receipt (goods arriving from production or external supplier), the system shall require: source reference (Production Order number or GRN number), receiving location, item, batch details (FR-INV-005), quantity in base UOM, and cost per unit. The system shall update `tbl_stock_balance` for the receiving location and post a GL entry (DR Inventory / CR Work-in-Progress or CR Accounts Payable as appropriate).

*Traceability: BG-001, DC-003.*

---

**FR-INV-010** — Stock Transfer Between Warehouse Locations

When a Store Manager initiates a stock transfer from one warehouse location to another, the system shall: validate sufficient stock at the source location for the specified batch; set the transferred quantity to `in transit` status (deducted from source, not yet credited to destination); record the transfer reference, initiating user, and timestamp; and require the destination Store to confirm receipt (FR-INV-011) before crediting the destination location.

*Traceability: BR-001, DC-003.*

---

**FR-INV-011** — Stock Transfer Receipt Confirmation

When the receiving store confirms a stock transfer, the system shall: credit the destination location's stock balance with the received quantity and batch details; clear the `in transit` status; record the receiving user's identity and confirmation timestamp; and generate a completed transfer record linking the dispatch and receipt events.

*Traceability: DC-003.*

---

**FR-INV-012** — In-Transit Stock Visibility

When a Store Manager or Finance Director views the stock summary, the system shall display a separate `in transit` column showing quantities in transit (dispatched but not yet confirmed at destination) for each product and batch. In-transit quantities shall not be included in either the source location balance or the destination location balance.

*Traceability: BG-001, DC-003.*

---

**FR-INV-013** — Agent Stock Issuance from Warehouse

When a Store Manager issues stock to a field sales agent, the system shall: verify the agent's current stock balance value in `tbl_agent_stock_balance`; calculate whether adding the new issuance value would exceed the agent's configured float limit (BR-006); if the float limit would be exceeded, block the issuance and display the current balance, float limit, and excess amount; if the float limit is not exceeded, deduct the quantity and value from the source warehouse location and credit `tbl_agent_stock_balance` for the receiving agent with batch information preserved.

*Traceability: BR-001, BR-006.*

---

**FR-INV-014** — Agent Stock Return to Warehouse

When an agent returns unsold stock to the warehouse, the system shall: require the Store Manager to record the returned items, quantities, and the agent's identity; verify the quantities against the agent's stock balance; deduct the returned quantity and value from `tbl_agent_stock_balance`; and credit the receiving warehouse location with the original batch information, placing the returned items in the `returns bay` location for quality inspection before re-integration.

*Traceability: BR-001, DC-003.*

---

**FR-INV-015** — Physical Stock Count Workflow: Freeze

When a Store Manager initiates a physical stock count for a selected location, the system shall set the location status to `frozen`, prevent all stock movements into or out of that location until the count is completed and approved, display a prominent `LOCATION FROZEN - COUNT IN PROGRESS` banner on the location's stock view, and record the freeze initiation timestamp and initiating user.

*Traceability: DC-003.*

---

**FR-INV-016** — Physical Stock Count Workflow: Count Entry

When a warehouse staff member enters count results for a frozen location, the system shall display each item and batch in the location with the system's recorded quantity and a field for the counted quantity. The staff member shall enter the physically counted quantity per item per batch. The system shall record counted quantities without displaying variances until count entry is complete, to prevent biased re-counting.

*Traceability: DC-003.*

---

**FR-INV-017** — Physical Stock Count Workflow: Variance Review

When all items in a frozen location have been counted, the system shall calculate the variance (counted minus system balance) for each item/batch line, display a variance report to the Store Manager showing positive and negative variances, flag all variances exceeding a configurable threshold (default: 2% of system balance) for mandatory review, and require the Store Manager to acknowledge each flagged variance before proceeding to approval.

*Traceability: DC-003.*

---

**FR-INV-018** — Physical Stock Count Workflow: Approval and Adjustment

When the Store Manager submits the physical count for approval, the system shall route the count to the Finance Director for approval (BR-003 — Store Manager cannot approve own count). Upon Finance Director approval, the system shall update `tbl_stock_balance` to match the counted quantities, post GL entries for all positive and negative variances (DR/CR Inventory Adjustment / CR/DR Stock Variance Expense), and release the location from `frozen` status.

*Traceability: BR-003, DC-003.*

---

**FR-INV-019** — Stock Adjustment with Reason Code

When a Store Manager initiates a manual stock adjustment (outside of physical count), the system shall require: reason code (configurable list, minimum: damage, theft, expiry write-off, data correction, production wastage), quantity adjustment (positive or negative), batch reference, and a text note. Adjustments of absolute value exceeding a configurable monetary threshold (default: UGX 500,000) shall require Finance Director approval before the system posts the adjustment and the associated GL entry.

*Traceability: BR-003, DC-002, DC-003.*

---

**FR-INV-020** — Stock Adjustment GL Auto-Posting

When a stock adjustment is approved and applied (FR-INV-019 or FR-INV-018), the system shall automatically post a GL journal entry: for a negative adjustment, DR Stock Adjustment Expense / CR Inventory; for a positive adjustment, DR Inventory / CR Stock Adjustment Income (or the applicable account per the chart of accounts). The adjustment reference number, reason code, and approver identity shall be recorded in the journal entry source reference.

*Traceability: BG-001, DC-003, BR-013.*

---

**FR-INV-021** — Reorder Level Alert

When the system's daily batch job runs and detects that a product's current total warehouse stock balance (across all warehouse locations, excluding agent stock per BR-001) falls at or below the product's configured reorder level, the system shall: display a reorder alert widget on the Store Manager's dashboard listing all below-reorder-level items with current stock, reorder level, and reorder quantity; and send an email notification to the Store Manager and Procurement Manager.

*Traceability: BR-001, DC-002.*

---

**FR-INV-022** — Stock Valuation: FIFO Method

When the stock valuation method for a product is set to FIFO, the system shall maintain a cost layer for each batch received, in order of receipt date. When stock is consumed (sold, transferred, or adjusted), the system shall deduct from the earliest-received cost layer first. The FIFO cost of each unit consumed shall be used for COGS calculation (FR-SAL-014 and FR-POS-018) and for the balance sheet inventory value.

*Traceability: BG-002, DC-002.*

---

**FR-INV-023** — Stock Valuation: Moving Average Method

When the stock valuation method for a product is set to Moving Average, the system shall recalculate the weighted average cost per unit after each stock receipt using the formula: $\text{New Average Cost} = \frac{(\text{Existing Quantity} \times \text{Existing Average Cost}) + (\text{Received Quantity} \times \text{Receipt Cost})}{\text{Existing Quantity} + \text{Received Quantity}}$. This average cost shall be used for COGS calculation on all subsequent sales and adjustments.

*Traceability: BG-002, DC-002.*

---

**FR-INV-024** — Balance Sheet Stock Valuation Report

When a Finance Director requests a stock valuation report as of a specified date, the system shall calculate the total inventory value at that date using the configured valuation method per product, broken down by product, location (warehouse only, per BR-001), and batch. The report shall be exportable to PDF and Excel and shall tie to the GL inventory account balance at the same date.

*Traceability: BG-002, STK-002.*

---

**FR-INV-025** — Warehouse App Integration (Android)

When a warehouse staff member uses the Warehouse Android App to scan a product barcode during stock receipt, transfer confirmation, or physical count, the system shall process the barcode scan via ML Kit, query the local cached product catalogue, and update the relevant transaction record. All Warehouse App transactions shall sync to the server via the REST API using JWT Bearer authentication. Offline operation shall follow the same queue-and-sync pattern as the POS offline mode (DC-005).

*Traceability: DC-005, STK-017.*

---

**FR-INV-026** — Stock Movement Ledger (Full Audit Trail)

The system shall maintain a stock movement ledger (`tbl_stock_movements`) recording every change to `tbl_stock_balance` or `tbl_agent_stock_balance`. Each ledger record shall contain: movement type (receipt, sale, transfer-out, transfer-in, adjustment, POS sale, agent issuance, agent return), source document reference, item, batch, location or agent, quantity (positive for in, negative for out), unit cost, movement timestamp, and user identity. This ledger is immutable — records are never updated or deleted.

*Traceability: DC-003, BR-013.*

---

**FR-INV-027** — Total Company Stock Consolidated Report

When a user with the `management` role requests a consolidated stock report, the system shall produce a report showing warehouse stock (from `tbl_stock_balance`, aggregated across all locations) and agent stock (from `tbl_agent_stock_balance`, aggregated across all agents) in separate, clearly labelled sections. A grand total row shall sum both. The report shall never present a single undifferentiated total that merges warehouse and agent stock without labelling (BR-001 compliance).

*Traceability: BR-001, STK-008.*

---

**FR-INV-028** — Product Category Management

When a Finance Director or Store Manager creates or edits a product category, the system shall capture: category code, category name, GL revenue account (mapped to the revenue account for CR on sales), GL COGS account (mapped for DR COGS on sales), GL inventory account (mapped for the balance sheet), and whether the category requires batch tracking. Category GL account mappings drive automated GL posting for all sales and stock movements in that category.

*Traceability: BG-001, DC-002.*

---

**FR-INV-029** — Cold Store Temperature Log (Configurable Attribute)

When a product is flagged as `cold store required`, the system shall associate the product with a cold store location and allow warehouse staff to record temperature readings against the location at configurable intervals. `[CONTEXT-GAP: GAP-013]` — confirm whether BIRDC's cold store has automated temperature sensors or requires manual entry.

*Traceability: BG-002, DC-002.*

---

**FR-INV-030** — Packaging Store Management

When packaging materials (bags, boxes, labels) are received into the packaging store location, the system shall track them as stock items with their own item codes, quantities, and reorder levels. When a production order requisitions packaging materials, the system shall deduct from packaging store stock and post GL entries (DR WIP or Production Cost / CR Packaging Inventory). `[CONTEXT-GAP: GAP-014]` — packaging material item codes and supplier relationships to be provided by BIRDC Procurement.

*Traceability: BG-004, BG-001.*

---

**FR-INV-031** — Distribution Staging Location Management

When goods are prepared for agent or distributor dispatch from the distribution staging location, the system shall track the stock as held in staging (not yet transferred to the agent's virtual store). Staging stock counts in the warehouse total until the agent issuance is confirmed. The staging location shall support batch picking: grouping multiple agent orders for simultaneous preparation before individual agent issuances are processed.

*Traceability: BR-001.*

---

**FR-INV-032** — Returns Bay Workflow

When returned goods (from agents or POS refunds) are placed in the returns bay location, the system shall hold them with status `pending inspection`. A QC-authorised user shall either: approve the return (move goods to a saleable location with the original batch), or reject the return (create a stock adjustment write-off). Approved returns shall not re-enter saleable stock without QC sign-off.

*Traceability: BR-004, DC-003.*

---

**FR-INV-033** — Stock Movement Search and Filter

When a Store Manager or Finance Director searches the stock movement ledger, the system shall support filtering by: date range, movement type, item, location, batch number, and source document reference. Results shall be paginated and exportable to Excel. Response time shall not exceed 2 seconds for queries spanning up to 12 months of data.

*Traceability: DC-001, DC-003.*

---

**FR-INV-034** — Low Stock Alert Dashboard Widget

When any product's warehouse stock balance falls at or below its reorder level, the system shall display a persistent low stock alert widget on the Store Manager's and Procurement Manager's dashboards. The widget shall list all below-reorder-level items, sorted by the severity of the shortfall (percentage below reorder level, descending). The widget shall clear for a product when its stock balance is restored above the reorder level.

*Traceability: DC-001, DC-002.*

---

**FR-INV-035** — Bulk Stock Item Import via Excel

When a Store Manager or IT Administrator uploads a PhpSpreadsheet-compatible Excel file for bulk stock item creation, the system shall validate each row against required fields (item code uniqueness, UOM validity, category existence), display a preview of valid and invalid rows before committing, import all valid rows, and generate an import result report showing: total rows processed, rows imported successfully, and rows rejected with reason. No partial-row imports shall occur — each row is either fully imported or fully rejected.

*Traceability: DC-002, STK-017.*

---

**FR-INV-036** — Stock Enquiry for Sales Agent (Read-Only)

When a field sales agent accesses the stock enquiry function in the Sales Agent App, the system shall display the agent's own virtual stock balance (from `tbl_agent_stock_balance`) per product with quantities and expiry dates. The agent shall have no visibility into warehouse stock balances of other locations (access control per 8-layer RBAC).

*Traceability: BR-001, STK-015.*

---

**FR-INV-037** — Goods Return from Customer (Sales Return)

When a customer returns goods against a sales invoice, the system shall record the return via the credit note workflow (FR-SAL-019) and, upon credit note approval, instruct the warehouse to receive the returned goods into the returns bay location (FR-INV-032) with the original invoice batch reference. The system shall post a GL reversal for the COGS and revenue lines of the returned items.

*Traceability: DC-003, BG-001.*
