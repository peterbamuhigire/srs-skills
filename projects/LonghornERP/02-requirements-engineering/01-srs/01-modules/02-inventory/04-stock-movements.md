# Stock Movements

## 4.1 Overview

A stock movement is any transaction that increases or decreases the quantity of an item in a warehouse. The system records every movement as an immutable ledger entry; corrections are made by posting reversing or adjusting movements, never by editing posted records.

## 4.2 Movement Types

The system shall support the following named movement types:

- `goods_receipt` — inbound stock from a Purchase Order or standalone GRN.
- `goods_issue` — outbound stock issued internally (e.g., to production or expense).
- `sales_delivery` — outbound stock fulfilled against a sales order.
- `purchase_return` — outbound stock returned to a supplier.
- `sales_return` — inbound stock returned by a customer.
- `internal_transfer` — movement between warehouses or bins within the same tenant.
- `stock_adjustment` — write-up or write-down of quantity or value with authorisation.
- `opening_balance` — initial stock entry at system go-live.

## 4.3 Functional Requirements — Stock Movements

**FR-INV-036:** The system shall record every stock movement as an immutable ledger entry containing `movement_type`, `item_id`, `quantity`, `uom_id`, `warehouse_id`, `bin_id` (if bin tracking is enabled), `movement_date`, `reference_document_type`, `reference_document_id`, `narration`, and `created_by` when any movement-triggering event occurs.

**FR-INV-037:** The system shall create a First In, First Out (FIFO) cost layer record containing `receipt_date`, `quantity_received`, `quantity_remaining`, and `unit_cost` when a `goods_receipt` movement is posted for an item whose valuation method is `FIFO`.

**FR-INV-038:** The system shall update the Weighted Average Cost (WAC) of an item using the formula $WAC_{new} = \frac{(QtyOnHand \times WAC_{prev}) + (QtyReceived \times UnitCost)}{QtyOnHand + QtyReceived}$ immediately when a `goods_receipt` movement is posted for an item whose valuation method is `weighted_average`.

**FR-INV-039:** The system shall apply the First Expired, First Out (FEFO) picking strategy — consuming the cost layer with the earliest `expiry_date` first — when a `goods_issue` or `sales_delivery` movement is posted for any item where `shelf_life_days > 0`.

**FR-INV-040:** The system shall return an HTTP 422 Unprocessable Entity error with the message "Insufficient stock: available quantity is [X]" when a user attempts to post an outbound movement whose quantity exceeds the available stock and the tenant's `allow_negative_stock` flag is set to `false`.

**FR-INV-041:** The system shall allow outbound movement quantities to reduce the item's warehouse balance below zero when the tenant's `allow_negative_stock` flag is set to `true`, and shall display negative balances in red on all stock balance screens.

**FR-INV-042:** The system shall require a `stock_adjustment` movement to carry a non-empty `narration` and an approval from a user holding the `inventory_adjustment_approver` role before the movement is posted when the absolute value of the adjustment exceeds the tenant-configured threshold.

**FR-INV-043:** The system shall post a `stock_adjustment` movement as a write-up (positive quantity delta) or write-down (negative quantity delta) and shall simultaneously create an accounting journal entry debiting or crediting the Stock Adjustment expense account defined in the tenant's chart of accounts when the movement is approved.

**FR-INV-044:** The system shall create an `opening_balance` movement type for each item-warehouse combination and shall restrict posting of additional `opening_balance` movements once the first financial period is closed for a tenant.

**FR-INV-045:** The system shall allocate landed costs (freight, insurance, customs duties) entered on a Goods Receipt Note (GRN) across all line items in that GRN using either a value-proportional or quantity-proportional method as selected by the user, and shall update each line item's effective unit cost before posting the FIFO layer or WAC recalculation.

**FR-INV-046:** The system shall record the landed cost allocation method (`by_value` or `by_quantity`), the total landed cost amount, and the per-line allocated amount in the GRN document when landed costs are applied.

**FR-INV-047:** The system shall prevent editing or deletion of any posted stock movement record, and shall require a reversing movement to be posted when a correction is needed, preserving the original record and the reversal record in the ledger.

**FR-INV-048:** The system shall automatically generate the corresponding outbound `purchase_return` movement for a Supplier Return document when the Supplier Return is confirmed, decrementing the item's stock balance in the originating warehouse by the returned quantity.

**FR-INV-049:** The system shall automatically generate the corresponding inbound `sales_return` movement for a Customer Return document when the Customer Return is confirmed, incrementing the item's stock balance in the receiving warehouse by the returned quantity and reversing the original cost-of-goods-sold entry.

**FR-INV-050:** The system shall display a paginated movement history for any item-warehouse combination, ordered by `movement_date` descending, with running balance per row, when the user opens the item ledger inquiry screen.

**FR-INV-051:** The system shall convert the movement quantity from the transaction UOM to the item's `base_uom` using the stored conversion factor before writing the ledger entry when a movement is posted in a non-base UOM.

**FR-INV-052:** The system shall assign a unique, auto-incremented `movement_id` to every posted movement record and shall expose this identifier in all movement-related reports and API responses.

**FR-INV-053:** The system shall record `created_at` and `posted_at` timestamps on every movement record and shall differentiate between draft movements (created but not yet approved) and posted movements in the movement list view.

**FR-INV-054:** The system shall notify the warehouse manager via in-app notification within 30 seconds when an outbound movement reduces any item's stock balance below its configured `min_stock_level`.

**FR-INV-055:** The system shall support batch/lot number recording on movement lines when the tenant's `batch_tracking_enabled` flag is set to `true`, storing `batch_number`, `batch_expiry_date`, and `batch_quantity` per movement line.
