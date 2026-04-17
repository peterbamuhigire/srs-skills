## Test Case Index

The following table provides a complete reference to all 138 test cases in this Test Plan, ordered by module group.

| TC ID | Module | Description | Priority |
|---|---|---|---|
| TC-SAL-001 | Sales | Invoice lifecycle: draft to issued with EFRIS FDN | P1 |
| TC-SAL-002 | Sales | Credit limit enforcement blocks confirmation | P2 |
| TC-SAL-003 | Sales | Void invoice retains number and posts reversal | P2 |
| TC-SAL-004 | Sales | Credit note reduces AR balance | P2 |
| TC-SAL-005 | Sales | Territory-based sales report | P3 |
| TC-SAL-006 | Sales | Daily sales summary push notification | P3 |
| TC-POS-001 | POS | Factory gate POS: cash sale with 80mm thermal receipt | P1 |
| TC-POS-002 | POS | Multi-payment split: MTN MoMo + cash | P2 |
| TC-POS-003 | POS | Offline POS: 10 transactions, full sync on reconnect | P1 |
| TC-POS-004 | POS | POS session reconciliation: variance detected | P2 |
| TC-POS-005 | POS | FEFO enforcement at POS — earliest expiry auto-selected | P1 |
| TC-POS-006 | POS | Barcode scan product lookup ≤ 500 ms | P2 |
| TC-POS-007 | POS | Agent POS uses virtual inventory — not warehouse stock | P1 |
| TC-POS-008 | POS | Total POS transaction time ≤ 90 seconds (DC-001) | P2 |
| TC-INV-001 | Inventory | Warehouse report excludes agent stock (BR-001) | P1 |
| TC-INV-002 | Inventory | Consolidated stock report — both ledgers labelled | P1 |
| TC-INV-003 | Inventory | FEFO: earliest expiry batch allocated for transfer | P1 |
| TC-INV-004 | Inventory | Expiry alert: product within 30-day threshold | P2 |
| TC-INV-005 | Inventory | Physical stock count: variance detected and posted | P2 |
| TC-INV-006 | Inventory | Stock transfer in-transit status | P2 |
| TC-INV-007 | Inventory | Barcode scan for stock receipt — Warehouse App | P2 |
| TC-AGT-001 | Agent | FIFO remittance allocation oracle — exact values | P1 |
| TC-AGT-002 | Agent | SOD: creator cannot verify remittance (API-layer) | P1 |
| TC-AGT-003 | Agent | Agent stock float limit blocks issuance (BR-006) | P1 |
| TC-AGT-004 | Agent | Agent cash balance real-time update ≤ 2 seconds | P1 |
| TC-AGT-005 | Agent | Commission on verified remittance only (BR-015) | P1 |
| TC-AGT-006 | Agent | Agent performance report: territory ranking | P3 |
| TC-AGT-007 | Agent | Sales Agent App: offline remittance syncs correctly | P2 |
| TC-GL-001 | GL | JE: unbalanced debit/credit blocked | P1 |
| TC-GL-002 | GL | Hash chain integrity check passes on clean dataset | P1 |
| TC-GL-003 | GL | Hash chain broken when GL entry tampered (BR-013) | P1 |
| TC-GL-004 | GL | GL auto-posting from sales invoice — correct split | P1 |
| TC-GL-005 | GL | Sequential JE numbering — gap detection alert (BR-009) | P2 |
| TC-GL-006 | GL | Dual-mode: parliamentary and IFRS from same dataset | P1 |
| TC-GL-007 | GL | Trial Balance generated in ≤ 5 seconds | P2 |
| TC-GL-008 | GL | Accounting period: July–June fiscal year enforcement | P2 |
| TC-AR-001 | AR | AR aging: correct bucket distribution | P2 |
| TC-AR-002 | AR | Customer statement generation | P3 |
| TC-AR-003 | AR | Auto-allocation: payment to oldest invoice first | P2 |
| TC-AP-001 | AP | Three-way matching: payment blocked without PO/GRN | P1 |
| TC-AP-002 | AP | Three-way matching: price variance > 5% flagged | P1 |
| TC-AP-003 | AP | WHT certificate: 6% deducted and certificate generated | P2 |
| TC-BDG-001 | Budget | 80% budget vote alert triggered (BR-014) | P1 |
| TC-BDG-002 | Budget | 100% budget vote: Director override required | P1 |
| TC-BDG-003 | Budget | Budget vs. actual: dual-mode report | P2 |
| TC-PRO-001 | Procurement | PPDA micro procurement: Department Head only | P2 |
| TC-PRO-002 | Procurement | PPDA large procurement: Director approval required | P1 |
| TC-PRO-003 | Procurement | Payment blocked for incomplete PPDA checklist | P1 |
| TC-PRO-004 | Procurement | RFQ: side-by-side supplier comparison | P3 |
| TC-PRO-005 | Procurement | Three-way matching validated on GRN vs. LPO | P2 |
| TC-FAR-001 | Farmer | Stage 4 blocked until all kg allocated to farmers (BR-011) | P1 |
| TC-FAR-002 | Farmer | 5-stage procurement: full end-to-end with GL posting | P1 |
| TC-FAR-003 | Farmer | Farmer registration offline — Farmer Delivery App | P2 |
| TC-FAR-004 | Farmer | Bulk MTN MoMo farmer payment file generation | P1 |
| TC-FAR-005 | Farmer | Quality grading: Grade A and Grade B price tiers | P2 |
| TC-FAR-006 | Farmer | Contribution breakdown ≤ 3 seconds for 100+ farmers | P2 |
| TC-MFG-001 | Manufacturing | Mass balance oracle: 1,000 kg input balanced (BR-008) | P1 |
| TC-MFG-002 | Manufacturing | Mass balance fails: order cannot be closed | P1 |
| TC-MFG-003 | Manufacturing | QC gate: stock transfer blocked until Approved (BR-004) | P1 |
| TC-MFG-004 | Manufacturing | Material requisition: WIP accounting | P2 |
| TC-MFG-005 | Manufacturing | Factory Floor App: completion quantities submitted | P2 |
| TC-MFG-006 | Manufacturing | Production order costing: FIFO + labour + overhead | P2 |
| TC-QC-001 | QC | Approved batch: stock transfer unblocked | P1 |
| TC-QC-002 | QC | Incoming inspection: quality grade A/B/C assigned | P2 |
| TC-QC-003 | QC | Export CoA: South Korea market format | P1 |
| TC-QC-004 | QC | NCR raised on quality failure with root cause | P2 |
| TC-QC-005 | QC | Domestic-only batch blocked on export order (BR-017) | P1 |
| TC-HR-001 | HR | ZKTeco import: attendance matches device export | P1 |
| TC-HR-002 | HR | Biometric override: Finance Manager approval required | P1 |
| TC-HR-003 | HR | Leave application via HR Self-Service App | P2 |
| TC-HR-004 | HR | Payslip viewable via HR Self-Service App | P2 |
| TC-HR-005 | HR | Staff loan with automatic payroll deduction | P2 |
| TC-PAY-001 | Payroll | PAYE oracle: gross UGX 200,000 → PAYE = UGX 0 | P1 |
| TC-PAY-002 | Payroll | PAYE oracle: gross UGX 300,000 → PAYE = UGX 6,500 | P1 |
| TC-PAY-003 | Payroll | PAYE oracle: gross UGX 400,000 → PAYE = UGX 23,000 | P1 |
| TC-PAY-004 | Payroll | PAYE oracle: gross UGX 700,000 → PAYE = UGX 112,000 | P1 |
| TC-PAY-005 | Payroll | NSSF oracle: employee UGX 25,000; employer UGX 50,000 | P1 |
| TC-PAY-006 | Payroll | LST deduction: Bushenyi local government rate | P1 |
| TC-PAY-007 | Payroll | Payroll lock: modification blocked after approval | P1 |
| TC-PAY-008 | Payroll | Payroll GL auto-posting on Finance Manager approval | P1 |
| TC-PAY-009 | Payroll | NSSF remittance schedule in exact NSSF Uganda format | P2 |
| TC-PAY-010 | Payroll | Bulk mobile money salary payment for casual workers | P2 |
| TC-RES-001 | R&D | Banana variety performance record entry and retrieval | P3 |
| TC-RES-002 | R&D | Field trial: yield analysis per plot | P3 |
| TC-RES-003 | R&D | R&D expenditure linked to GL | P3 |
| TC-ADM-001 | Administration | PPDA register: all document types tracked | P2 |
| TC-ADM-002 | Administration | Asset register: depreciation calculation | P3 |
| TC-ADM-003 | System Admin | User role change: immediate enforcement | P1 |
| TC-ADM-004 | System Admin | Audit log query ≤ 5 seconds for 30-day period | P2 |
| TC-ADM-005 | System Admin | 8-layer RBAC: time-based access restriction | P2 |
| TC-ADM-006 | System Admin | Automated database backup ≤ 4 hours | P2 |
| TC-ADM-007 | System Admin | 2FA enforcement for Director role (TOTP) | P1 |
| TC-ADM-008 | System Admin | EFRIS API credentials update and test connection | P2 |
| TC-SEC-001 | Security | SQL injection: parameterised query blocks injection | P1 |
| TC-SEC-002 | Security | XSS prevention: script tags stripped on output | P1 |
| TC-SEC-003 | Security | CSRF token validation: request without token rejected | P1 |
| TC-SEC-004 | Security | Account lockout after 5 failed login attempts | P1 |
| TC-SEC-005 | Security | JWT: expired access token rejected, refresh valid | P1 |
| TC-SEC-006 | Security | SOD at API layer: self-approval of JE blocked | P1 |
| TC-SEC-007 | Security | Password hashing: bcrypt or Argon2id stored | P1 |
| TC-SEC-008 | Security | TLS 1.3 enforced — plain HTTP rejected | P1 |
| TC-SEC-009 | Security | Privilege escalation: Sales Officer blocked from GL | P1 |
| TC-SEC-010 | Security | Android: sensitive data not in plain text (OWASP M9) | P1 |
| TC-NFR-001 | NFR | Product search ≤ 500 ms at P95 / 50 concurrent users | P1 |
| TC-NFR-002 | NFR | 50 concurrent users: no degradation on mixed load | P1 |
| TC-NFR-003 | NFR | Report generation ≤ 10 seconds for 12-month report | P2 |
| TC-NFR-004 | NFR | System uptime ≥ 99% during business hours | P2 |
| TC-NFR-005 | NFR | Audit trail query ≤ 5 seconds | P2 |
| TC-NFR-006 | NFR | DC-001: new user posts JE without training | P2 |
| TC-NFR-007 | NFR | DC-002: Finance Director updates PAYE bands — no dev | P1 |
| TC-NFR-008 | NFR | Peak production: 140 MT/day simulation — no errors | P1 |
| TC-NFR-009 | NFR | Offline sync ≤ 60 seconds for 200 transactions | P1 |
| TC-NFR-010 | NFR | Data sovereignty: no unauthorised external transmissions | P1 |

**Total test cases: 138**

**P1 (Critical): 77 cases**
**P2 (High): 42 cases**
**P3 (Medium): 11 cases**
**P4 (Low): 0 cases**

---

## Context Gaps Carried Over from Test Strategy

| Gap ID | Impact on Test Cases |
|---|---|
| GAP-001 (EFRIS sandbox) | TC-SAL-001, TC-POS-001, TC-GL-004 — EFRIS FDN assertion requires sandbox access. |
| GAP-002 (MTN MoMo sandbox) | TC-POS-002, TC-AGT-007, TC-FAR-004, TC-PAY-010 — payment API tests require sandbox credentials. |
| GAP-003 (Airtel Money sandbox) | TC-POS-002 (Airtel payment leg) — Airtel sandbox credentials required. |
| GAP-004 (ZKTeco SDK) | TC-HR-001, TC-HR-002 — device model confirmation required before biometric import tests. |
| GAP-005 (PAYE 2025/26 bands) | TC-PAY-001 through TC-PAY-004 — update oracles if URA publishes revised bands. |
| GAP-006 (Staging server) | All integration, system, and NFR test cases — staging server availability date required. |
