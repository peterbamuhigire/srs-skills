# Finished Goods Receipt and By-products

## 6.1 Finished Goods Receipt

**FR-MFG-029** — When a production order passes its final QC checkpoint, the system shall prompt the user to record the actual finished goods output quantity; the system shall post a stock receipt of the finished goods item to the production warehouse, crediting the WIP account and debiting the Finished Goods stock account.

**FR-MFG-030** — When a batch-tracked finished goods item is received into stock, the system shall require batch number assignment for the new production batch; the batch record shall carry: production order reference, production date, batch quantity, QC inspector identity, and expiry date (computed from the item's configurable shelf life).

**FR-MFG-031** — The system shall compute the actual finished goods unit cost as: $ActualCost = (TotalWIPCost - ByProductValue) \div ActualOutputQty$ and shall update the weighted average cost for the finished goods item using this value.

## 6.2 By-products and Co-products

**FR-MFG-032** — When a BOM includes by-product lines, the system shall receive each by-product into stock at the completion of the production order, crediting the WIP account for the by-product's net realisable value and reducing the effective finished goods cost accordingly.

**FR-MFG-033** — When a production run yields zero by-products where the BOM specifies by-products, the system shall flag the variance and require the production supervisor to record a disposal reason before closing the production order.

**FR-MFG-034** — The system shall produce a by-products report per production order showing planned by-product quantities, actual quantities, variance, and the net realisable value applied to the finished goods cost calculation.
