# Reorder Management

## 7.1 Overview

Reorder management monitors stock levels against configured thresholds and triggers purchasing actions to prevent stockouts. Thresholds operate at either the item level or the item-warehouse level, depending on tenant configuration.

## 7.2 Functional Requirements — Reorder Management

**FR-INV-080:** The system shall evaluate the stock balance of every item against its configured `reorder_point` after every outbound movement is posted, and shall trigger a reorder alert when the resulting balance is less than or equal to `reorder_point`.

**FR-INV-081:** The system shall deliver the reorder alert as an in-app notification to all users holding the `purchasing_officer` role within the tenant, within 60 seconds of the triggering movement being posted, specifying the item, warehouse, current balance, and reorder point.

**FR-INV-082:** The system shall evaluate the stock balance against the `min_stock_level` threshold separately from the `reorder_point` evaluation, and shall deliver a `critical_stock` in-app notification to the `purchasing_manager` role when the balance falls below `min_stock_level`.

**FR-INV-083:** The system shall automatically generate a draft Purchase Requisition (PR) referencing the item's `preferred_supplier_id`, `reorder_quantity`, and `purchase_uom_id` when the `auto_generate_pr` flag is set to `true` for that item and the reorder point is breached.

**FR-INV-084:** The system shall suppress duplicate reorder alerts for the same item-warehouse combination for 24 hours after an alert has been triggered, unless the stock balance falls below `min_stock_level`, in which case a `critical_stock` alert is always generated regardless of suppression.

**FR-INV-085:** The system shall produce a Reorder Report listing all items whose current balance is at or below `reorder_point`, grouped by warehouse, showing `item_code`, `item_name`, `warehouse`, `qty_on_hand`, `reorder_point`, `reorder_quantity`, and `preferred_supplier` when the user generates the report.

**FR-INV-086:** The system shall calculate the Days of Supply (DOS) for each item using the formula $DOS = \frac{QtyOnHand}{AvgDailyConsumption}$ where `AvgDailyConsumption` is computed from posted outbound movements over the last 90 days, and shall display DOS per item on the Reorder Report.

**FR-INV-087:** The system shall display a projected stockout date for each item on the Reorder Report, calculated as $StockoutDate = Today + DOS$, to enable purchasing officers to prioritise replenishment actions.
