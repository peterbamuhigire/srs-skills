# Traceability Matrix — Advanced Inventory

## 9.1 Functional Requirements to Business Goals

| Requirement ID | Requirement Summary | Business Goal |
|---|---|---|
| FR-ADVINV-001–008 | Multi-location warehousing, bin management | BG-003 |
| FR-ADVINV-009–015 | Batch tracking, batch ledger, agro fields | BG-002, BG-003 |
| FR-ADVINV-016–021 | Serial number tracking and ledger | BG-003 |
| FR-ADVINV-022–028 | FEFO picking, expiry alerts, POS expiry gate | BG-002 |
| FR-ADVINV-029–035 | Inter-branch transfers, landed cost | BG-001 |
| FR-ADVINV-036–038 | Stock reservation and ATP | BG-001 |
| FR-ADVINV-039–041 | Recall management and trace reporting | BG-003 |
| FR-ADVINV-042–044 | Cold chain, temperature tracking, UNBS | BG-001, BG-004 |

## 9.2 Dependency on Core Inventory

All `FR-ADVINV-*` requirements depend on `FR-INV-*` from the Core Inventory SRS. Advanced Inventory functionality shall not be deployed without the Core Inventory module fully implemented and tested.

## 9.3 Open Verification Notes

- NFR-ADVINV-001 (recall report within 120 seconds) must be validated by a load test using a seeded dataset of 5 years of sales history prior to UAT sign-off.
- FR-ADVINV-027 (auto-quarantine on expiry) must be implemented as a scheduled background job; the exact scheduling frequency (default: nightly at 00:00) must be confirmed during implementation.
- FR-ADVINV-043 (cold chain temperature excursion) IoT sensor integration is a future enhancement; the initial implementation shall support manual temperature entry only.
