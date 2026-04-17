# Inter-Branch Transfers and Landed Cost

## 6.1 Inter-Branch Transfers

**FR-ADVINV-029** — When a user initiates an inter-branch transfer, the system shall create a transfer request record listing: source branch, destination branch, items and quantities, requested delivery date, and the requesting user.

**FR-ADVINV-030** — When the transfer request is approved by the destination branch manager, the system shall transition the source branch stock for the specified items and quantities to "In-Transit" status; the items shall no longer be available for sale or issue from the source branch but shall appear in a separate "In-Transit" stock balance visible to both branches.

**FR-ADVINV-031** — When the destination branch confirms receipt (by creating a transfer receipt note), the system shall: (a) clear the In-Transit balance from the source branch, (b) add the received quantity to the destination branch stock, and (c) post the stock movement to the stock ledger with the transfer receipt note reference.

**FR-ADVINV-032** — When a transfer is partially received, the system shall retain the unreceived quantity in In-Transit status; the system shall permit multiple partial receipts until the full transfer quantity is confirmed or the transfer is closed with variance.

## 6.2 Landed Cost Allocation

**FR-ADVINV-033** — The system shall provide a landed cost allocation function applicable to any GRN from an import supplier; the user shall enter additional costs (freight, insurance, customs duty, clearing fees, port levies) and select an allocation method: by value, by weight, or by quantity.

**FR-ADVINV-034** — When landed costs are allocated by value, the system shall distribute the additional cost to each GRN line in proportion to the line's value: $AllocatedCost_i = TotalLandedCost \times (LineValue_i \div TotalGRNValue)$.

**FR-ADVINV-035** — When a landed cost allocation is confirmed, the system shall update the unit cost of each GRN line item to include the allocated landed cost and shall re-compute the weighted average cost for those items using the adjusted cost.
