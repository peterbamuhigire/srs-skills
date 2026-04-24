# Traceability Matrix - Supply Chain Planning

## 7.1 Functional Requirements to Business Goals

| Requirement ID | Requirement Summary | Business Goal |
|---|---|---|
| FR-SCP-001-008 | Demand planning and consensus-demand governance | BG-SCP-001, BG-SCP-004 |
| FR-SCP-009-016 | Supply and replenishment planning | BG-SCP-002, BG-SCP-004 |
| FR-SCP-017-022 | Inventory optimization and policy governance | BG-SCP-003, BG-SCP-005 |
| FR-SCP-023-030 | S&OP / IBP, scenarios, and financial translation | BG-SCP-004, BG-SCP-005 |

## 7.2 Context Gaps

| Gap ID | Topic | Impact |
|---|---|---|
| GAP-SCP-001 | Promotion and event-data source model not yet finalised | FR-SCP-001, FR-SCP-005 |
| GAP-SCP-002 | Supplier-capacity and manufacturing-capacity feed granularity not yet confirmed | FR-SCP-011, FR-SCP-014 |
| GAP-SCP-003 | Financial translation granularity for margin and procurement exposure not yet confirmed | FR-SCP-025 |

## 7.3 Open Verification Notes

- FR-SCP-004 and FR-SCP-008 must be tested with at least 3 demand segments: stable demand, intermittent demand, and high-override demand.
- FR-SCP-015 and NFR-SCP-005 must be verified by forcing release retries and confirming no duplicate downstream recommendations are published.
- FR-SCP-019 must be tested in both modes: with `ADV_INVENTORY` active and without it active, to confirm the fallback from multi-echelon to single-echelon planning.
- FR-SCP-025 must be validated against manually calculated financial projections for at least 2 scenarios with materially different supply assumptions.
