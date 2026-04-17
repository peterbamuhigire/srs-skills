# FEFO Picking and Expiry Management

## 5.1 FEFO Picking Strategy

**FR-ADVINV-022** — When an item is configured with picking strategy "FEFO", the system shall always select the batch with the earliest expiry date to fulfil outbound stock movements (delivery picks, production issues, transfer dispatches); if two batches share the same expiry date, the system shall select the batch with the earliest receipt date (secondary sort: FIFO).

**FR-ADVINV-023** — FEFO picking shall be mandatory and non-overridable for items in the following configurable category types: food, pharmaceutical, agro-chemical, and veterinary products; a user attempting to manually override FEFO picking for these categories shall receive an HTTP 403 response.

**FR-ADVINV-024** — When an outbound movement requires more than one batch to fulfil the requested quantity, the system shall auto-split the pick across batches in FEFO order and shall display each batch allocation to the warehouse operative.

## 5.2 Expiry Alerts

**FR-ADVINV-025** — The system shall generate a daily expiry alert report listing all batch records with an expiry date within the configured alert horizon (default: 30 days); the report shall show item name, batch number, expiry date, current quantity, and current bin location.

**FR-ADVINV-026** — When a batch's expiry date falls within the alert horizon, the system shall send an in-app notification to the warehouse manager and, if configured, an email alert to the inventory email distribution list.

**FR-ADVINV-027** — When a batch's expiry date is passed and the batch still has a positive stock balance, the system shall automatically set the batch QC status to "Quarantined" (per FR-ADVINV-011) and generate a high-priority alert for the warehouse manager to initiate disposal or return.

## 5.3 Expiry at Point of Sale

**FR-ADVINV-028** — When a POS cashier adds a batch-tracked item to a sale, the system shall display the expiry date of the batch being sold; if the expiry date is within 7 days (configurable), the system shall display a yellow warning; if the expiry date is past, the system shall block the sale and display a red error.
