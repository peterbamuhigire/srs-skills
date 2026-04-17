---
title: "SRS Phase 3b -- Advanced Inventory: Functional Requirements"
project: "Maduuka"
version: "1.0"
date: "2026-04-05"
status: "Draft"
---

# Section 2: Functional Requirements -- Advanced Inventory (F-014)

All requirements in this section extend Phase 1 F-002. Unless stated otherwise, every requirement applies to both the Android application and the web application. Requirements follow stimulus-response format per IEEE 830.

---

## 2.1 Multi-Warehouse Management

### 2.1.1 Warehouse Definitions

**FR-AINV-001:** When a user with Branch Manager or Business Owner role creates a warehouse, the system shall accept: warehouse name (required), physical address (required), warehouse type (storage / transit / returns; required), and an optional description. The system shall impose no upper limit on the number of warehouses per branch.

**FR-AINV-002:** When a user edits a warehouse record, the system shall update the name, address, type, and description fields immediately. Changing warehouse type shall not affect existing stock movement records linked to that warehouse.

**FR-AINV-003:** When a user deactivates a warehouse, the system shall prevent new stock movements from being posted to that warehouse and display a deactivation warning if the warehouse holds stock with a quantity greater than zero.

### 2.1.2 Per-Warehouse Stock Levels

**FR-AINV-004:** When any stock movement occurs (sale, purchase receipt, transfer, adjustment, production), the system shall record the movement against the specific warehouse where the movement originated or was received, maintaining an independent stock balance per warehouse per product.

**FR-AINV-005:** When a user requests the stock level for a product at a specific warehouse, the system shall return the current on-hand quantity, reserved quantity (allocated to open production orders), and available quantity (on-hand minus reserved) for that warehouse.

### 2.1.3 Cross-Warehouse Availability

**FR-AINV-006:** When a user queries cross-warehouse availability for a product, the system shall return the sum of available quantities across all active warehouses in the tenant's account, together with a per-warehouse breakdown, within 500 ms for tenants with up to 50 active warehouses.

**FR-AINV-007:** When a POS cashier searches for a product and the product has zero stock at the current session's warehouse, the system shall display a cross-warehouse availability indicator showing the total available quantity across all other warehouses, without requiring the cashier to navigate away from the POS screen.

### 2.1.4 Stock Transfers Between Warehouses

**FR-AINV-008:** When a user initiates a stock transfer, the system shall require: source warehouse, destination warehouse, product, quantity, and an optional reference note. The system shall decrement available stock at the source warehouse and place the quantity in `in_transit` status (extending FR-INV-008), creating an immutable transfer-out movement record.

**FR-AINV-009:** When the receiving user at the destination warehouse confirms receipt of the transferred stock, the system shall increment stock at the destination warehouse, clear the `in_transit` quantity, and create an immutable transfer-in movement record linked to the originating transfer-out record.

**FR-AINV-010:** When a transfer is cancelled before the destination user confirms receipt, the system shall return the `in_transit` quantity to available stock at the source warehouse and create an immutable transfer-cancel movement record.

### 2.1.5 Warehouse-Level Stock Count

**FR-AINV-011:** When a user initiates a physical stock count scoped to a specific warehouse, the system shall freeze stock movements for the products selected for counting at that warehouse only. Other warehouses shall remain operational. The count workflow (count entry, variance calculation, manager approval) shall follow FR-INV-014.

### 2.1.6 Per-Warehouse Reorder Points

**FR-AINV-012:** When a user configures reorder settings for a product at a specific warehouse, the system shall store an independent reorder level and reorder quantity for that product-warehouse combination. When the product's stock at that warehouse falls to or below its warehouse-specific reorder level, the system shall generate an alert per FR-INV-007, identifying both the product and the warehouse.

---

## 2.2 Serial Number Tracking

### 2.2.1 Serial Number Assignment

**FR-AINV-013:** When goods are received for a serialised product (a product with serial tracking enabled), the system shall require entry of one serial number per unit in the goods receipt. Serial numbers may be entered by barcode scan or manual keyboard input. The goods receipt shall not be confirmed until all units have serial numbers assigned.

**FR-AINV-014:** When a serial number is submitted during goods receipt, the system shall validate that the serial number is unique within the product's serial number registry for the current tenant. If the serial number already exists within the tenant, the system shall reject the entry and display an error identifying the duplicate.

*Note:* [CONTEXT-GAP: unique scope] -- The requirement to enforce serial number uniqueness globally across all tenants (not per-tenant) has not been confirmed in `_context/`. The current specification enforces uniqueness per tenant. If cross-tenant uniqueness is required (e.g., for manufacturer-assigned serial numbers), the data model and validation logic must be revised before implementation.

**FR-AINV-015:** When serial tracking is enabled on a product, the system shall prevent deletion of the serial tracking flag if any serial number records exist for the product.

### 2.2.2 Serial Number History

**FR-AINV-016:** When a serialised item is sold, transferred, adjusted, or returned, the system shall create a serial movement record linking the serial number to the movement type, date, user, source warehouse, destination warehouse (for transfers), and -- for sales -- the customer and receipt number.

**FR-AINV-017:** When a user requests the full history of a serial number, the system shall return all serial movement records for that serial number in chronological order, showing: event type, date, warehouse, user, and the associated transaction reference.

### 2.2.3 Serial Number Search

**FR-AINV-018:** When a user enters a serial number in the serial number search field, the system shall retrieve the matching serial number record and its complete movement history within 300 ms of query submission. If no match is found, the system shall display a "serial number not found" message.

**FR-AINV-019:** When a user views a serial number record, the system shall display: product name, SKU, purchase date, supplier, original goods receipt reference, current warehouse location, sale date (if sold), customer name (if sold), and warranty expiry date (if configured).

### 2.2.4 Warranty Management

**FR-AINV-020:** When a user configures a serialised product for warranty tracking, the system shall accept a warranty duration in months. On goods receipt, the system shall calculate the warranty expiry date for each serial number as: $WarrantyExpiry = GoodsReceiptDate + WarrantyDurationMonths$.

**FR-AINV-021:** When a serial number's warranty expiry date is within 30 days (configurable per product), the system shall add the item to the warranty expiry alert list and display it in the dashboard alerts panel.

**FR-AINV-022:** When a sold serial number's warranty expiry date has passed, the system shall mark the serial number status as `warranty_expired` in the serial number registry. No automated action shall be taken on the customer's account without explicit user instruction.

---

## 2.3 Batch Traceability

### 2.3.1 Batch Creation

**FR-AINV-023:** When goods are received for a batch-tracked product, the system shall require: batch number (required), manufacturing date (optional), and expiry date (required for products with FEFO enabled). The batch shall be assigned to the receiving warehouse and linked to the goods receipt record.

### 2.3.2 Forward Trace

**FR-AINV-024:** When a user requests a forward trace on a batch, the system shall identify all sales transactions, transfers, and adjustments that consumed stock from that batch, returning: transaction type, date, quantity consumed, destination (customer or warehouse), and transaction reference. The trace shall cover all movements from the batch creation date to the present.

**FR-AINV-025:** When a batch's stock balance reaches zero and all movements are traced, the system shall mark the batch status as `fully_consumed`. The batch record and all its movement links shall remain permanently accessible for audit purposes.

### 2.3.3 Backward Trace

**FR-AINV-026:** When a user requests a backward trace starting from a specific sale line item, the system shall return the batch number, goods receipt date, supplier, and purchase order reference from which the sold item was drawn. If FEFO batch selection was overridden for the transaction, the override record shall be included in the trace result.

### 2.3.4 Product Recall

**FR-AINV-027:** When a user flags a batch as recalled, the system shall immediately mark the batch status as `recalled` and prevent any further stock movements from that batch until the recall is lifted or the batch is written off.

**FR-AINV-028:** When a batch is flagged as recalled, the system shall generate a recall notification list identifying all customers who received items from the recalled batch. The list shall include: customer name, phone number, sale date, quantity received, and receipt number, and shall be generated within 5 seconds for up to 10,000 affected transactions.

**FR-AINV-029:** When a recall notification list is generated, the system shall present an option to dispatch the list to the Maduuka bulk SMS/WhatsApp dispatch interface (Africa's Talking, per F-010 configuration), pre-populating the recipient list and a default recall message template. Dispatch requires explicit user confirmation.

**FR-AINV-030:** When remaining stock from a recalled batch exists in any warehouse, the system shall display a recall inventory report showing: warehouse, quantity on hand, and total estimated cost value, to support the write-off decision.

### 2.3.5 Profitability by Batch

**FR-AINV-031:** When a user requests the profitability report for a batch, the system shall calculate and display: total purchase cost of the batch (including any allocated landed costs), total revenue from all sales drawing from the batch, gross margin (Revenue - Cost), and gross margin percentage, for the portion of the batch that has been sold.

**FR-AINV-032:** When a batch contains items allocated a landed cost, the system shall include the allocated landed cost per unit in the batch cost calculation for FR-AINV-031.

---

## 2.4 Landed Cost Allocation

### 2.4.1 Landed Cost Record

**FR-AINV-033:** When a user creates a landed cost record, the system shall require: the linked purchase order or goods receipt number (GRN), at least one cost line with a cost type (freight / import duty / insurance / clearing / handling), and the amount for each cost line in the tenant's functional currency.

**FR-AINV-034:** When a landed cost record is saved, the system shall display the total landed cost value (sum of all cost lines) and the list of products in the linked GRN before the user triggers allocation.

### 2.4.2 Allocation Methods

**FR-AINV-035:** When a user selects the allocation method for a shipment, the system shall offer four methods:

- **By value:** Each product's share = $\frac{ProductCostInShipment}{TotalShipmentCost} \times TotalLandedCost$
- **By weight:** Each product's share = $\frac{ProductWeightInShipment}{TotalShipmentWeight} \times TotalLandedCost$
- **By quantity:** Each product's share = $\frac{ProductQuantityInShipment}{TotalShipmentQuantity} \times TotalLandedCost$
- **By volume:** Each product's share = $\frac{ProductVolumeInShipment}{TotalShipmentVolume} \times TotalLandedCost$

The method is configurable per shipment. When "by weight" or "by volume" is selected and weight or volume is not recorded on the GRN line, the system shall flag the missing data and prevent allocation until the data is supplied.

**FR-AINV-036:** When the user confirms allocation, the system shall distribute the landed cost to each product line in the GRN using the selected method, calculating the allocated cost per unit as: $AllocatedCostPerUnit = \frac{ProductAllocatedShare}{ReceivedQuantity}$.

### 2.4.3 Cost Price Update

**FR-AINV-037:** When a landed cost allocation is confirmed, the system shall update the effective landed cost price for each affected product in the GRN. The updated cost price shall be used in all subsequent FIFO valuation calculations for stock received in that GRN.

**FR-AINV-038:** When a landed cost allocation is confirmed, the system shall create an immutable landed cost allocation record linked to the GRN and each product, recording: allocation method, total landed cost, allocated amount per product, and allocated cost per unit.

**FR-AINV-039:** When a user attempts to edit a confirmed landed cost allocation, the system shall reject the edit and require the user to create a landed cost adjustment record instead, preserving the audit trail.

### 2.4.4 Landed Cost Reporting

**FR-AINV-040:** When a user requests the landed cost report for a shipment, the system shall display: GRN reference, supplier, receipt date, total purchase cost, each cost type and amount, total landed cost, allocation method, and each product's allocated cost and allocated cost per unit.

**FR-AINV-041:** When a user requests the landed cost report for a period, the system shall aggregate all landed cost records within the date range and display: total freight cost, total import duty, total insurance, total clearing costs, total landed costs, and the top 10 products by total landed cost allocated.

**FR-AINV-042:** When a user requests the landed cost report filtered by product, the system shall display all landed cost allocations for that product across all shipments in the selected period, with a total allocated landed cost and a total effective cost price (weighted average across allocations).

---

## 2.5 Bill of Materials and Production Orders

### 2.5.1 BOM Definition

**FR-AINV-043:** When a user creates a Bill of Materials for a finished product, the system shall require: the finished product SKU (must be an existing product in the catalogue), at least one raw material line (raw material SKU, quantity per unit of finished product, UOM), and a theoretical yield percentage (default 100%).

**FR-AINV-044:** When a user adds a raw material line to a BOM, the system shall validate that the raw material SKU exists in the product catalogue. The system shall not allow a finished product to reference itself as a raw material in its own BOM (circular reference check).

**FR-AINV-045:** When a user saves a BOM, the system shall version it with a sequential version number and a creation timestamp. Editing an existing active BOM shall require the user to create a new BOM version; the previous version shall be retained for traceability against historical production orders.

**FR-AINV-046:** When a user configures the UOM conversion matrix for a product used in a BOM (either as a raw material or as a finished good), the system shall store all defined unit conversion factors and apply the correct factor when calculating material requirements in production orders.

### 2.5.2 Production Orders

**FR-AINV-047:** When a user creates a production order, the system shall require: finished product SKU, BOM version to use, target quantity to produce, and target warehouse for finished goods.

**FR-AINV-048:** When a production order is created, the system shall calculate the required raw material quantities as: $RequiredQty_{material} = \frac{TargetFinishedQty \times MaterialQtyPerUnit}{TheoreticalYield\%}$ and display the requirement list before the user confirms the order.

**FR-AINV-049:** When a production order is submitted for confirmation, the system shall check that each raw material has sufficient available stock across all warehouses assigned to the production order. If any material is short, the system shall display the shortfall quantity per material and prevent confirmation until the shortfall is resolved or a manager override is applied with a reason.

**FR-AINV-050:** When a user confirms a production order, the system shall place the required raw material quantities into `reserved_for_production` status, reducing available stock without yet creating a consumption movement.

### 2.5.3 Production Completion

**FR-AINV-051:** When a user marks a production order as complete, the system shall require entry of the actual quantity of finished goods produced and the actual quantities of each raw material consumed.

**FR-AINV-052:** When a production order is marked as complete, the system shall:

1. Create immutable `production_consumption` movement records for each raw material, decrementing stock at the source warehouse.
2. Create an immutable `production_output` movement record, incrementing finished goods stock at the target warehouse.
3. Release any remaining `reserved_for_production` quantities that were not consumed.

**FR-AINV-053:** When a production order is completed, the system shall calculate the cost of the produced finished goods as: $FinishedGoodCost = \sum(RawMaterialCost \times ActualQtyConsumed)$, and record this as the cost price for the production lot.

### 2.5.4 Yield Management

**FR-AINV-054:** When a production order is marked as complete, the system shall calculate the actual yield percentage as: $ActualYield\% = \frac{ActualFinishedGoodsQty}{TheoreticalFinishedGoodsQty} \times 100$.

**FR-AINV-055:** When the actual yield percentage deviates from the BOM theoretical yield by more than the configurable variance threshold (default: 5%), the system shall flag the production order with a yield variance alert and require the user to enter a variance reason before the order can be closed.

**FR-AINV-056:** When a user requests the yield variance report for a period, the system shall list all production orders in the period with: finished product, BOM version, target quantity, actual quantity, theoretical yield %, actual yield %, variance %, and variance reason (if provided).

### 2.5.5 Material Availability Summary

**FR-AINV-057:** When a user views the production order list, the system shall display a material availability indicator per order: green (all materials available), amber (all materials available but below reorder trigger), or red (one or more materials are short).

**FR-AINV-058:** When a user requests the raw material requirements report across all open production orders, the system shall consolidate material requirements, net them against current available stock per warehouse, and display the net shortfall per material for procurement planning.

---

## 2.6 Demand Forecasting

### 2.6.1 Days of Stock Remaining

**FR-AINV-059:** When a user views the demand forecast dashboard, the system shall calculate the days of stock remaining per product as: $DaysRemaining = \frac{CurrentStock}{AverageDailySales_{30d}}$ where $AverageDailySales_{30d}$ is the rolling 30-calendar-day average of units sold. If $AverageDailySales_{30d} = 0$, the system shall display "No recent sales" rather than a calculated figure.

**FR-AINV-060:** When a user requests the days of stock remaining per warehouse, the system shall calculate the metric independently for each warehouse using the sales attributable to that warehouse's POS sessions.

### 2.6.2 Reorder Quantity Recommendation

**FR-AINV-061:** When a user views the reorder recommendation for a product, the system shall calculate the recommended reorder quantity as: $ReorderQty = (AverageDailySales_{30d} \times LeadTimeDays) + SafetyStock - CurrentStock$ where `LeadTimeDays` and `SafetyStock` are configurable per product. If $ReorderQty \leq 0$, the system shall display "Sufficient stock for lead time" and suppress the recommendation.

**FR-AINV-062:** When a user updates the lead time or safety stock configuration for a product, the system shall recalculate the reorder quantity recommendation immediately and display the updated value.

### 2.6.3 Reorder Alerts

**FR-AINV-063:** When a product's days of stock remaining falls below the configured reorder trigger (in days, configurable per product with a default of 7 days), the system shall generate a reorder alert and display it in the dashboard low-stock alert panel alongside the existing FR-INV-007 reorder level alerts.

**FR-AINV-064:** When a reorder alert is generated for a product that already has an open purchase order for that product, the system shall display the existing open PO reference alongside the alert to prevent duplicate ordering.

### 2.6.4 Demand Forecast Report

**FR-AINV-065:** When a user requests the demand forecast report, the system shall list the top 20 products by 30-day sales velocity (units sold), displaying for each: product name, SKU, current stock, average daily sales (30d), days of stock remaining, lead time days, safety stock, and recommended reorder quantity.

**FR-AINV-066:** When a user applies a warehouse filter to the demand forecast report, the system shall restrict the velocity and stock figures to the selected warehouse only.

**FR-AINV-067:** When a user exports the demand forecast report, the system shall generate a CSV file containing all products (not just the top 20) with all fields from FR-AINV-065, available for download within 30 seconds for product catalogues of up to 10,000 SKUs.

---

## 2.7 Compliance Audit Report

### 2.7.1 High-Value Movement Report

**FR-AINV-068:** When a user runs the high-value movement report for a period, the system shall list all stock movements (receipts, sales, adjustments, transfers) where the movement value (quantity × cost price at time of movement) exceeds the configurable high-value threshold (default: UGX 500,000 per movement line). Each row shall show: date, movement type, product, quantity, unit cost, total value, warehouse, and user who created the movement.

### 2.7.2 After-Hours Movement Report

**FR-AINV-069:** When a user runs the after-hours movement report for a period, the system shall list all stock movements created outside the business's configured operating hours (configurable: default 07:00-22:00 per branch). Each row shall show: movement date and time, movement type, product, quantity, value, warehouse, and the user who created the movement.

**FR-AINV-070:** When business hours are not configured for a branch, the system shall use the global default (07:00-22:00) for that branch's after-hours report and display a configuration reminder in the report header.

### 2.7.3 Unusual Pattern Detection

**FR-AINV-071:** When a user runs the unusual pattern report for a period, the system shall identify and list stock movements matching any of the following patterns:

- Same-day receive-and-transfer: a product received in a GRN and transferred out of the receiving warehouse on the same calendar day.
- Negative adjustment exceeding threshold: a negative stock adjustment where the absolute value (quantity × cost price) exceeds the configurable unusual-adjustment threshold (default: UGX 200,000).

Each flagged movement shall show: the pattern type detected, date, product, quantity, value, warehouse, and user.

**FR-AINV-072:** When an unusual pattern is detected for a movement that already has an approved manager override on record, the system shall still include it in the report but mark it as `approved_override` to distinguish reviewed patterns from unreviewed ones.

### 2.7.4 Audit Report Export

**FR-AINV-073:** When a user exports any compliance audit report (high-value, after-hours, or unusual pattern), the system shall generate the report in both PDF and CSV formats. PDF format shall include the business name, branch, report type, report period, generation date, and the generating user's name in the report header.

**FR-AINV-074:** When a user schedules an audit report for automatic delivery, the system shall send the selected report type as a PDF to the configured email address at the configured frequency (daily, weekly, or monthly), following the scheduling rules in FR-REP-010.
