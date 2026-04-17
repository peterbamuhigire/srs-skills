# Stock Take (Physical Inventory Count)

## 6.1 Overview

A stock take is the process of physically counting items in a warehouse to verify that the system's recorded quantities match actual on-hand quantities. Variances discovered during a stock take are resolved by posting adjustment movements, which in turn generate the necessary accounting journal entries.

## 6.2 Functional Requirements — Stock Take

**FR-INV-068:** The system shall allow a user to initiate a stock take of type `full_count` (all items in a warehouse) or `cycle_count` (a subset of items selected by ABC classification or category) when the user creates a new stock take document and selects the scope.

**FR-INV-069:** The system shall set the stock take status to `in_progress` and freeze all stock movements for the items and warehouse(s) in scope by blocking the posting of any movement whose `item_id` and `warehouse_id` match the stock take scope, returning HTTP 409 with the message "Item is locked by stock take [ST-NNN]" when a freeze is active.

**FR-INV-070:** The system shall generate printable count sheets in PDF format, listing each item in scope with its `item_code`, `item_name`, `bin_location` (if applicable), and a blank `physical_count` column, when the user requests count sheets for a stock take.

**FR-INV-071:** The system shall allow physical count quantities to be entered via the mobile interface or the web interface, recording `counter_user_id` and `count_timestamp` for each line, and shall support entry in the item's `base_uom`.

**FR-INV-072:** The system shall support a double-blind count workflow where 2 independent counters enter quantities for the same items without visibility of each other's entries, and shall flag any line where the 2 entries differ by more than the tenant-configured tolerance (default: 0 units) as requiring reconciliation.

**FR-INV-073:** The system shall calculate the variance for each item line as $Variance = PhysicalCount - SystemCount$ and shall display positive variances (surplus) and negative variances (shortage) in the stock take variance report when the count is submitted for review.

**FR-INV-074:** The system shall display the financial impact of all variances on the stock take variance report as $VarianceValue = |Variance| \times UnitCost$ using the item's current carrying cost, before the variance is approved.

**FR-INV-075:** The system shall require approval from a user holding the `stock_take_approver` role before posting stock take adjustment movements, and shall prevent the stock take from being finalised without this approval.

**FR-INV-076:** The system shall automatically create stock adjustment movements for all non-zero variance lines and post the corresponding inventory adjustment journal entries when the stock take is approved, using the valuation cost applicable at the time of approval.

**FR-INV-077:** The system shall release the movement freeze for all items in scope when the stock take status transitions to `completed`, restoring normal movement posting for those items.

**FR-INV-078:** The system shall maintain a stock take history record for every completed stock take, including the `initiated_by`, `approved_by`, `completion_date`, total lines counted, total variance lines, and the net financial impact of all adjustments posted.

**FR-INV-079:** The system shall provide an ABC classification report that ranks items by total consumption value over a configurable period (default: 12 months), categorising the top 80% of value as Class A, the next 15% as Class B, and the bottom 5% as Class C, to support cycle count scheduling.
