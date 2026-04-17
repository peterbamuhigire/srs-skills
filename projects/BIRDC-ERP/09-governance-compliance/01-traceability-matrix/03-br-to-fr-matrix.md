# Section 2: Business Rules to Functional Requirements Matrix

Each business rule (BR-001 through BR-018) must be enforced by at least one functional requirement. This table records every FR that implements each rule. A BR with no enforcing FR is a compliance gap.

| BR ID | Business Rule Summary | Enforcing FRs | Enforcement Status |
|---|---|---|---|
| BR-001 | Dual-Track Inventory Separation — warehouse and agent stock are permanently separate ledgers | FR-INV-001, FR-INV-012, FR-POS-009, FR-AGT-001, FR-AGT-007 | Fully covered |
| BR-002 | FIFO Remittance Allocation — via `sp_apply_remittance_to_invoices`; no manual invoice selection | FR-AGT-003, FR-AR-002 | Fully covered |
| BR-003 | Segregation of Duties — creator ≠ approver/verifier, enforced at API layer | FR-AGT-004, FR-FIN-005, FR-INV-008, FR-SYS-001, FR-SYS-002 | Fully covered |
| BR-004 | QC Gate on Production Output — finished goods blocked until QC status = "Approved" and CoA issued | FR-MFG-005, FR-QC-004, FR-QC-009 | Fully covered |
| BR-005 | PPDA Procurement Approval Matrix — category-dependent approval authority; payment blocked without required documents | FR-PRO-001, FR-PRO-002, FR-PRO-003, FR-ADM-001, FR-ADM-002 | Fully covered |
| BR-006 | Agent Stock Float Limit — issuance blocked when float limit would be exceeded | FR-AGT-001, FR-AGT-006 | Fully covered |
| BR-007 | FEFO Enforcement — earliest-expiry batch selected first; manual FEFO violation blocked | FR-INV-005, FR-POS-011 | Fully covered |
| BR-008 | Circular Economy Mass Balance — Total Input = Products + By-products + Scrap (±2%); production order cannot close if unbalanced | FR-MFG-003, FR-MFG-010 | Fully covered |
| BR-009 | Sequential Numbering and Gap Detection — invoice, receipt, and JE numbers are sequential and gap-free; gaps trigger alert | FR-SAL-001, FR-SAL-009, FR-FIN-004 | Fully covered |
| BR-010 | Payroll Immutability — approved payroll run is permanently locked; corrections via adjustment run only | FR-PAY-007 | Fully covered |
| BR-011 | Individual Farmer Contribution Tracking — batch cannot advance to Stock Receipt until every kg is allocated to a specific farmer | FR-PRO-008, FR-PRO-009 | Fully covered |
| BR-012 | Three-Way Matching — no vendor payment without PO + GRN match; price variance > 5% or quantity variance > 2% flagged | FR-AP-001, FR-AP-002, FR-PRO-006 | Fully covered |
| BR-013 | GL Hash Chain Integrity — cryptographic hash chain on every GL entry; tampering is detectable | FR-FIN-007, FR-EFR-004 | Fully covered |
| BR-014 | Parliamentary Budget Vote Alert — alert at 80% and 95% of vote; Director override required to exceed 100% | FR-BUD-004, FR-BUD-005, FR-BUD-006 | Fully covered |
| BR-015 | Commission on Verified Sales Only — commission accrues on verified remittances only | FR-AGT-005 | Fully covered |
| BR-016 | Biometric Attendance Authority — ZKTeco records are authoritative; manual overrides require Finance Manager approval and audit trail entry | FR-HR-003, FR-HR-004 | Fully covered [CONTEXT-GAP: GAP-005] |
| BR-017 | Export CoA Requirements — export batch must have export-grade CoA with destination market parameters; domestic-approved batch blocked on export order | FR-QC-005, FR-QC-006 | Fully covered [CONTEXT-GAP: GAP-010] |
| BR-018 | Imprest Account Control — disbursement blocked if it would reduce imprest below zero; replenishment requires Finance Manager approval | FR-FIN-002, FR-FIN-006 | *Partially covered — a dedicated FR for imprest disbursement blocking is recommended. Flag for SRS review.* |

**Anomaly Note — BR-018:** The imprest workflow is described in the feature register (F-005) but no dedicated FR with an explicit blocking condition and GL posting requirement has been specified. A remediation FR should be added: "When a disbursement from an imprest account would reduce the imprest balance below zero, the system shall reject the disbursement and display the current balance and the requested amount."
