# Non-Functional Requirements — Advanced Inventory

## 8.1 Performance

**NFR-ADVINV-001** — The recall trace report (`FR-ADVINV-039`) shall generate within 120 seconds for a dataset covering ≤ 5 years of sales history and ≤ 500,000 delivery note line records.

**NFR-ADVINV-002** — The batch ledger enquiry for a single batch shall return results within 1 second for a batch with ≤ 10,000 movement records.

**NFR-ADVINV-003** — The FEFO batch selection algorithm (`FR-ADVINV-022`) shall resolve the correct batch within 500 ms for an item with ≤ 1,000 active batches.

## 8.2 Reliability

**NFR-ADVINV-004** — All stock movements that update batch balances, bin balances, and branch balances shall execute within a single atomic database transaction; a failure at any step shall roll back all balance updates to prevent split-brain stock data.

## 8.3 Security

**NFR-ADVINV-005** — Batch QC status overrides (releasing quarantined batches) shall require the `inventory.batch.qc_override` permission; every override shall be recorded in the audit log with the approver identity, reason, and UTC timestamp.

**NFR-ADVINV-006** — Recall initiation shall require the `inventory.recall.initiate` permission, which shall be restricted to the quality manager and system administrator roles by default.

## 8.4 Compliance

**NFR-ADVINV-007** — Batch and serial number records shall be retained for a minimum of 10 years from the date the batch/serial is fully consumed, in compliance with Uganda Food and Drugs Authority record-keeping requirements for food and pharmaceutical products.

**NFR-ADVINV-008** — The expiry date enforcement at POS (`FR-ADVINV-028`) shall have no exceptions for items in the pharmaceutical category; the system shall block the sale and shall not provide a supervisor override for expired pharmaceutical items.
