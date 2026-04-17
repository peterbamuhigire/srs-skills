# Traceability Matrix — Procurement

## 10.1 Functional Requirements to Business Goals

| Requirement ID | Requirement Summary | Business Goal |
|---|---|---|
| FR-PROC-001 | Unique supplier validation | BG-002 |
| FR-PROC-002 | Supplier mandatory fields | BG-004 |
| FR-PROC-003 | Supplier bank accounts | BG-003 |
| FR-PROC-004 | Supplier update audit | BG-004 |
| FR-PROC-005 | Inactive supplier block | BG-001 |
| FR-PROC-006 | Supplier search performance | BG-001 |
| FR-PROC-007–008 | Supplier categories / import tag | BG-001 |
| FR-PROC-009–012 | PR creation, approval, PPDA threshold | BG-001, BG-002 |
| FR-PROC-013–016 | RFQ dispatch and comparison | BG-001 |
| FR-PROC-017–020 | PO creation, approval, issuance | BG-001, BG-002 |
| FR-PROC-021–024 | PO amendments and closure | BG-004 |
| FR-PROC-025–031 | GRN, landed cost, returns, mobile | BG-001, BG-004 |
| FR-PROC-032–037 | Invoice capture, 3-way match, WHT, credit notes | BG-001, BG-002, BG-004 |
| FR-PROC-038–045 | Payments, payment runs, aging | BG-001, BG-003 |
| FR-PROC-046–051 | PPDA compliance | BG-002, BG-004 |

## 10.2 Context Gaps

| Gap ID | Topic | Impact |
|---|---|---|
| GAP-006 | Current PPDA method-selection monetary thresholds | FR-PROC-012, FR-PROC-046 cannot specify threshold values until confirmed |

## 10.3 Open Verification Notes

- FR-PROC-034 (three-way match tolerance) requires the default 0% tolerance confirmed or overridden by the product owner before implementation.
- FR-PROC-036 (WHT rate default 6%) is per Uganda Income Tax Act; confirm that the system supports configurable rate overrides for non-Uganda tenants.
- NFR-PROC-005 (bank account masking) must be validated during security penetration testing to confirm no raw values are transmitted in API responses.
