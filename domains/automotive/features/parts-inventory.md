# Feature: Parts & Inventory

## Purpose

Track parts from supplier to installation with branch-level stock-on-hand, reservation vs issue semantics, and valuation that feeds the general ledger.

## Core Entities

- **Part** — SKU with tenant-scoped catalogue entry. Attributes: code, description, category, vehicle-fitment tags, barcodes (primary + alternates), unit of measure, condition enum {new, reman, used, oem, aftermarket}, warranty period, preferred supplier, average cost, standard cost, list price.
- **Stock Location** — a branch plus optional sub-location (bay shelf, van stock). Owns stock-on-hand per part.
- **Stock Movement** — append-only ledger of every receive, issue, return, transfer, adjust, and cycle-count reconciliation.
- **Purchase Order** — tenant-scoped order to a supplier; receipt creates stock movements.
- **Reservation** — holding quantity against a job card; converts to issue on technician consumption; auto-expires on job cancellation.

## Valuation Methods

- FIFO (default), weighted average, or standard cost — tenant-selectable at onboarding and stable thereafter.
- Revaluation events write explicit GL adjustment entries.

## Key Workflows

1. **Receive from supplier.** Storekeeper scans delivery; PO is matched; stock movements commit; GL posts accounts-payable against inventory.
2. **Reserve for job.** On estimate approval, reservation rows are created for each parts line.
3. **Issue to job.** Technician scans part barcode at the bay; reservation converts to issue; stock-on-hand decrements; job cost roll-up updates.
4. **Return to stock.** If a reserved/issued part is not used, return reverses the reservation or issue with a reason.
5. **Cycle count.** Periodic count produces variance report; variances beyond NFR-AUTO-014 threshold require branch-manager-approved adjustment entries.

## Interfaces

- Workshop operations and inspection feed part recommendations.
- Accounting receives inventory valuation, COGS, and adjustment postings.
- Supplier integrations — optional catalogue sync and stock-level checks.
- Barcode scanning — primary workflow driver on the mobile app.

## Non-Functional Expectations

Inherit NFR-AUTO-001, NFR-AUTO-014.

## Edge Cases

- Partial kits — a single SKU breaks down into sub-parts when issued; the ledger tracks at the SKU level, the job card line notes the breakdown.
- Core charges — remanufactured parts often carry a returnable core. The platform SHOULD track core exchange separately.
- Cross-branch transfer — source decrements, destination increments; in-transit state accounts for multi-hour/multi-day transfers.
- Hazardous parts — airbags, batteries, fuel pumps; chain-of-custody logging per security baseline.
