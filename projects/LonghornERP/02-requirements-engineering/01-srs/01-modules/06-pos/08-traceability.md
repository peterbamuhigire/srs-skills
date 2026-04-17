# Traceability Matrix — Point of Sale

## 8.1 Functional Requirements to Business Goals

| Requirement ID | Requirement Summary | Business Goal |
|---|---|---|
| FR-POS-001–012 | Terminal registration, multi-terminal, restaurant/table mode | BG-001, BG-002 |
| FR-POS-013–029 | Sales transactions, basket, item lookup, stock posting, GL posting | BG-001, BG-003 |
| FR-POS-030–040 | Payment methods, split payments, mobile money, reversals | BG-001 |
| FR-POS-041–051 | Till management, session open/close, X-report, Z-report, handover | BG-002 |
| FR-POS-052–061 | Offline mode, local cache, sync, conflict resolution | BG-004 |

## 8.2 Context Gaps

| Gap ID | Topic | Impact |
|---|---|---|
| GAP-001 | EFRIS API integration specification and endpoint details | FR-POS-025, FR-POS-061, NFR-POS-012 |

## 8.3 Open Verification Notes

- FR-POS-027 (real-time stock deduction) must be tested with concurrent transactions on multiple terminals to confirm no race condition yields negative stock for items with "no negative stock" policy.
- FR-POS-045 (cash variance formula) must be reviewed by the finance product owner to confirm float handling is consistent with the GL session-level posting approach in FR-POS-028.
- NFR-POS-004 (no data loss on crash) requires a write-ahead log (WAL) mode or equivalent durability guarantee in the SQLite local database implementation, to be verified during technical review.
- NFR-POS-008 (offline database encryption) key derivation approach must be reviewed by the security architect before implementation to ensure the terminal secret is not exposed in device logs or crash reports.
