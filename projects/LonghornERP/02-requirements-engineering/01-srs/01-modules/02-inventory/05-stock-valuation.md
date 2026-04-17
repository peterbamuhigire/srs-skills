# Stock Valuation

## 5.1 Overview

Stock valuation determines the monetary amount at which inventory is carried on the balance sheet, in compliance with IAS 2 — Inventories. The system supports two IAS 2-approved cost-flow assumptions: First In, First Out (FIFO) and Weighted Average Cost (WAC). Net Realisable Value (NRV) write-downs and cost revaluations are also governed by this section.

## 5.2 Functional Requirements — Stock Valuation

**FR-INV-056:** The system shall allow the valuation method (`FIFO` or `weighted_average`) to be set at the item level or at the tenant level when the item is created or the tenant default is configured, with the item-level setting taking precedence over the tenant default.

**FR-INV-057:** The system shall block any change to an item's `valuation_method` after the first stock movement has been posted for that item, returning an HTTP 422 error with the message "Valuation method cannot be changed after stock movements have been recorded."

**FR-INV-058:** The system shall maintain a FIFO cost layer table per item per warehouse, where each row records `layer_id`, `receipt_movement_id`, `receipt_date`, `expiry_date` (nullable), `quantity_received`, `quantity_remaining`, and `unit_cost`, when a goods receipt is posted for a FIFO-valued item.

**FR-INV-059:** The system shall consume FIFO cost layers in ascending order of `receipt_date` (or ascending `expiry_date` when FEFO applies) when calculating the Cost of Goods Sold (COGS) for an outbound movement, reducing `quantity_remaining` on each layer until the movement quantity is fully allocated.

**FR-INV-060:** The system shall calculate COGS for a sales delivery as $COGS = \sum_{i=1}^{n}(LayerQtyConsumed_i \times LayerUnitCost_i)$ and shall post this amount to the COGS account in the integrated accounting module when the delivery movement is finalised.

**FR-INV-061:** The system shall recalculate the WAC after every goods receipt for WAC-valued items using the formula stated in **FR-INV-038** and shall store the new WAC value in the item-warehouse balance record immediately after the receipt is posted.

**FR-INV-062:** The system shall use the WAC at the time of issue as the unit cost for COGS calculation when an outbound movement is posted for a WAC-valued item.

**FR-INV-063:** The system shall allow an authorised user (holding the `nrv_write_down` permission) to record an NRV write-down for a specific item-warehouse combination when the user submits a write-down form specifying the `new_nrv_per_unit` and a justification, and shall reject the write-down if `new_nrv_per_unit` ≥ the current carrying cost per unit.

**FR-INV-064:** The system shall post an NRV write-down journal entry debiting the Inventory Write-Down expense account and crediting the Stock — Provision account by the amount $WriteDown = QtyOnHand \times (CarryingCost - NRV)$ when the write-down is approved.

**FR-INV-065:** The system shall allow an authorised user (holding the `cost_revaluation` permission) to update the standard cost of a FIFO-valued item by creating a revaluation movement that adjusts the `unit_cost` of all open (non-zero `quantity_remaining`) cost layers proportionally, and shall post a cost variance journal entry for the total revaluation amount.

**FR-INV-066:** The system shall display the current carrying value of stock per item per warehouse on the Stock Valuation Report, showing `qty_on_hand`, `unit_cost`, and `total_value`, filtered by valuation date, when the report is generated.

**FR-INV-067:** The system shall include landed cost components in the unit cost stored in each FIFO layer or in the WAC recalculation when landed costs are allocated to a GRN line, so that the carrying value reflects the full cost of acquisition as required by IAS 2.
