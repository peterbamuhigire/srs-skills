# Section 3: Design Covenants to Functional Requirements Matrix

Each Design Covenant (DC-001 through DC-007) is a binding constraint that every requirement must satisfy. This table records every FR that directly implements or satisfies each covenant.

| DC ID | Design Covenant Summary | Satisfying FRs | Satisfaction Status |
|---|---|---|---|
| DC-001 | Zero mandatory training for routine operations — every daily-use screen must be self-discoverable | FR-POS-007, FR-HR-009, FR-SEC-006 | Covered; acceptance criterion is the Prossy cashier test (≤ 90 s, first use). Verified by TC-POS-007. |
| DC-002 | Configuration over code — all business rules configurable via UI by Finance Director or IT Administrator without developer involvement | FR-FIN-012, FR-PAY-001, FR-PAY-002, FR-PAY-005, FR-SYS-007 | Covered across payroll, finance, and system administration modules. |
| DC-003 | Audit readiness by design — every financial transaction creates an immutable audit trail; 7-year retention enforced | FR-FIN-007, FR-SYS-003, FR-SYS-004, FR-ADM-006 | Covered. Hash chain integrity (FR-FIN-007) + audit trail query (FR-SYS-003) + retention enforcement (FR-SYS-004). |
| DC-004 | Dual-mode accounting — PIBID parliamentary votes and BIRDC commercial IFRS tracked simultaneously | FR-FIN-002, FR-FIN-009, FR-FIN-011, FR-BUD-001, FR-BUD-002, FR-HR-002 | Covered. Financial module separates PIBID and BIRDC modes with consolidated reporting. |
| DC-005 | Offline-first where it matters — Factory Gate POS, Farmer Delivery App, and Warehouse App must function fully offline | FR-POS-006, FR-INV-011, FR-PRO-011, FR-AGT-009, FR-MFG-009 | Covered across all four offline-critical touchpoints. |
| DC-006 | Data sovereignty — all BIRDC data stored on BIRDC's own servers in Uganda; no SaaS vendor holds data | FR-SYS-005, FR-SYS-006 | Covered. FR-SYS-006 prohibits external hosting; FR-SYS-005 ensures on-premises backup. |
| DC-007 | Replicable by design — every BIRDC-specific configuration is in configuration tables, not code | FR-FIN-012, FR-PAY-001, FR-PAY-002, FR-PAY-005, FR-SYS-007, FR-PRO-002, FR-QC-001 | Covered. Configurable PAYE bands (FR-PAY-002), configurable PPDA thresholds (FR-PRO-002), configurable inspection templates (FR-QC-001), and configurable payroll elements (FR-PAY-001) all isolate BIRDC-specific rules in configuration tables. |

## DC Coverage Assessment

All 7 Design Covenants are satisfied by at least 2 functional requirements each. DC-007 (Replicability) is the most broadly covered with 7 implementing FRs spanning payroll, procurement, QC, and system administration modules.
