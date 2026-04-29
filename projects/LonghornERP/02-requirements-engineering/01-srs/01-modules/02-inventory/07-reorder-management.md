# Reorder Management

## 7.1 Overview

Reorder management monitors stock levels against configured thresholds and policy-driven demand signals to prevent stockouts without creating excess inventory. Thresholds operate at either the item level or the item-warehouse level, depending on tenant configuration. Where the Supply Chain Planning module is active, Inventory consumes approved policy outputs and recommendations; where it is inactive, Inventory uses the built-in lightweight reorder logic.

## 7.2 Functional Requirements — Reorder Management

**FR-INV-080:** The system shall evaluate the stock balance of every item against its configured `reorder_point` after every outbound movement is posted, and shall trigger a reorder alert when the resulting balance is less than or equal to `reorder_point`.

**FR-INV-081:** The system shall deliver the reorder alert as an in-app notification to all users holding the `purchasing_officer` role within the tenant, within 60 seconds of the triggering movement being posted, specifying the item, warehouse, current balance, and reorder point.

**FR-INV-082:** The system shall evaluate the stock balance against the `min_stock_level` threshold separately from the `reorder_point` evaluation, and shall deliver a `critical_stock` in-app notification to the `purchasing_manager` role when the balance falls below `min_stock_level`.

**FR-INV-083:** The system shall automatically generate a draft Purchase Requisition (PR) referencing the item's `preferred_supplier_id`, `reorder_quantity`, and `purchase_uom_id` when the `auto_generate_pr` flag is set to `true` for that item and the reorder point is breached.

**FR-INV-084:** The system shall suppress duplicate reorder alerts for the same item-warehouse combination for 24 hours after an alert has been triggered, unless the stock balance falls below `min_stock_level`, in which case a `critical_stock` alert is always generated regardless of suppression.

**FR-INV-085:** The system shall produce a Reorder Report listing all items whose current balance is at or below `reorder_point`, grouped by warehouse, showing `item_code`, `item_name`, `warehouse`, `qty_on_hand`, `reorder_point`, `reorder_quantity`, and `preferred_supplier` when the user generates the report.

**FR-INV-086:** The system shall calculate the Days of Supply (DOS) for each item using the formula $DOS = \frac{QtyOnHand}{AvgDailyConsumption}$ where `AvgDailyConsumption` is computed from posted outbound movements over the last 90 days, and shall display DOS per item on the Reorder Report.

**FR-INV-087:** The system shall display a projected stockout date for each item on the Reorder Report, calculated as $StockoutDate = Today + DOS$, to enable purchasing officers to prioritise replenishment actions.

**FR-INV-088:** The system shall calculate available stock as `qty_on_hand - qty_reserved` and shall use available stock, not gross on-hand stock, for reorder alerts and stockout-risk display.

**FR-INV-089:** The system shall compute safety stock using demand variability, configured service level, and supplier lead time where at least 90 days of clean issue history exists; otherwise the system shall label the reorder signal as `manual_policy` and require a planner or inventory manager to confirm the policy.

**FR-INV-090:** The system shall calculate recommended reorder quantity as `max(0, forecast_demand_during_horizon + safety_stock - available_stock - inbound_qty)` and shall then adjust the result for MOQ and order multiple when supplier rules exist.

**FR-INV-091:** Each reorder recommendation shall show the reason for the recommendation, including daily demand, lead time, safety stock, available stock, inbound quantity, MOQ/order multiple adjustment, and projected stockout date.

**FR-INV-092:** The system shall provide a separate excess-inventory report showing item, branch, coverage days, aged stock value, last issue date, recommended action, and owner.

**FR-INV-093:** The system shall suppress automated draft PR creation when the item has an unresolved duplicate reorder recommendation, stale stock balance, missing supplier lead time, or conflicting open inbound order.

## 7.3 Warehouse Execution and Storage Policy Extensions

**FR-INV-094:** The system shall support storage policies per item-location, including preferred zone, storage medium, temperature or handling constraint, stack limit, pallet or case configuration, and whether the item is eligible for forward-pick storage.

**FR-INV-095:** When stock is received, transferred, or produced, the system shall recommend a putaway location using item storage policy, available bin capacity, FEFO or FIFO rotation, quarantine status, hazardous or cold-chain constraints, and current congestion indicators.

**FR-INV-096:** The system shall maintain bin-level capacity by weight, volume, pallet count, and unit count where configured, and shall block putaway tasks that would exceed a hard capacity limit unless an authorised warehouse manager records an override.

**FR-INV-097:** The system shall generate replenishment tasks from reserve storage to forward-pick locations when forward-pick quantity falls below the configured trigger point, showing item, source bin, destination bin, required quantity, priority, and due time.

**FR-INV-098:** The picking workbench shall support batch picking, wave picking, zone picking, and single-order picking modes, and shall record the selected mode on each pick task for performance analysis.

**FR-INV-099:** The system shall calculate pick-path sequence using warehouse zone, aisle, bin sequence, FEFO/FIFO rule, and order priority, and shall preserve the generated sequence for audit and warehouse productivity reporting.

**FR-INV-100:** The warehouse performance dashboard shall report inventory accuracy, pick accuracy, putaway cycle time, pick cycle time, dock-to-stock time, storage utilisation, replenishment backlog, and aged staging stock by warehouse and shift.
