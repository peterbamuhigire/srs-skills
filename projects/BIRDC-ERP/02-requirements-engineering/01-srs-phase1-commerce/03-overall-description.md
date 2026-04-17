# 2. Overall Description

## 2.1 Product Perspective

The BIRDC ERP system is a new, standalone, single-tenant system replacing all manual spreadsheets and registers currently used at BIRDC/PIBID. It is not a module of any existing ERP suite. Phase 1 modules interact with the Phase 2 General Ledger (F-005) module through defined GL auto-posting interfaces. All GL posting calls from Phase 1 modules write to the `tbl_gl_entries` table and are consumed by the General Ledger module when Phase 2 is deployed.

The system interfaces with three external systems:

1. **URA EFRIS API** — real-time fiscal document submission for every commercial invoice and POS receipt (`[CONTEXT-GAP: GAP-001]` — sandbox credentials pending).
2. **MTN MoMo Business API** — mobile money payment collection and remittance processing (`[CONTEXT-GAP: GAP-002]`).
3. **Airtel Money API** — mobile money payment collection, dual-provider redundancy (`[CONTEXT-GAP: GAP-003]`).

## 2.2 Product Functions

Phase 1 delivers four primary functional areas:

1. **Sales and Distribution (F-001):** Complete order-to-cash lifecycle — invoice creation through payment collection — with EFRIS fiscal compliance and GL auto-posting.
2. **Point of Sale (F-002):** Three POS contexts (factory gate, distribution centre, agent checkout) with offline capability, multi-payment, and EFRIS receipts.
3. **Inventory and Warehouse Management (F-003):** Multi-location stock management with batch/expiry tracking, FEFO enforcement, and dual-track inventory separation.
4. **Agent Distribution Management (F-004):** 1,071-agent field network management with virtual stock stores, real-time cash balance tracking, and FIFO remittance allocation.

## 2.3 User Classes and Characteristics

| User Class | Count | Technical Literacy | Primary Phase 1 Interaction |
|---|---|---|---|
| Sales Manager | 1 | Proficient | Invoice approval, credit override, sales reports |
| Cashier (factory gate / distribution centre) | ~5 | Basic | POS — cash sales, receipt printing |
| Accounts Assistant | ~8 | Basic-Proficient | Invoice creation, credit note workflow |
| Store Manager | 1 | Basic | Stock issuance, transfers, agent stock |
| Warehouse Staff | ~15 | Basic | Stock receipt, physical count, transfers |
| Field Sales Agent | 1,071 | Smartphone-literate | Sales Agent App — POS, remittance, commission |
| Sales and Marketing Manager | 1 | Proficient | Performance reports, agent management |
| Finance Director | 1 | Proficient | GL posting review, commission approval |
| BIRDC Director | 1 | Basic smartphone | Executive dashboard, daily sales notification |

**DC-001 constraint:** Prossy (factory gate cashier, S4 education, basic smartphone user) must complete a cash sale from product search to printed receipt in under 90 seconds on first use, with no training.

## 2.4 Operating Environment

| Component | Specification |
|---|---|
| Server | On-premise, BIRDC Nyaruzinga, Bushenyi, Uganda |
| Web server | Apache / Nginx, HTTPS |
| Database | MySQL 9.1 InnoDB, utf8mb4 |
| Backend | PHP 8.3+, `declare(strict_types=1)`, PSR-4/PSR-12 |
| Frontend | Bootstrap 5, Tabler admin UI, jQuery, Alpine.js |
| Mobile | Android 8.0 (API 26) minimum, Kotlin, Jetpack Compose |
| Offline storage | Android Room (SQLite), WorkManager background sync |
| Connectivity | LAN-wired for office terminals; 3G/4G for mobile; intermittent Bushenyi rural connectivity is the baseline assumption |

## 2.5 Design and Implementation Constraints

The following Design Covenants (DC-001 through DC-007) are binding on all Phase 1 requirements. No requirement may be designed or implemented in a way that violates any Design Covenant without written sign-off from the Finance Director and BIRDC Director.

| Constraint ID | Summary |
|---|---|
| **DC-001** | Zero mandatory training for routine operations — every daily-use screen is self-discoverable |
| **DC-002** | All business rules configurable via UI — no developer involvement for PAYE bands, commission rates, price lists, FEFO thresholds |
| **DC-003** | Every financial transaction creates an immutable audit trail automatically; 7-year retention enforced |
| **DC-004** | Dual-mode accounting — PIBID parliamentary and BIRDC IFRS simultaneously |
| **DC-005** | Offline-first where it matters — factory gate POS, Warehouse App, Sales Agent App must function fully offline |
| **DC-006** | Data sovereignty — all data stored on BIRDC's own servers; no SaaS vendor dependency |
| **DC-007** | Replicable by design — all BIRDC-specific rules in configuration tables, not code |

## 2.6 Assumptions and Dependencies

1. The Phase 2 General Ledger module (F-005) will be deployed in sequence. Phase 1 GL posting calls write to a staging table; the GL module activates them on Phase 2 deployment.
2. EFRIS API sandbox credentials (**GAP-001**) will be provided by BIRDC IT before Phase 1 integration testing begins.
3. MTN MoMo and Airtel Money API credentials (**GAP-002**, **GAP-003**) will be provided before payment integration testing.
4. 80mm thermal receipt printers are available at all POS terminals and compatible with ESC/POS protocol.
5. BIRDC's existing Chart of Accounts structure is available for GL account mapping (**GAP-012**).
6. The legacy accounting data migration strategy (**GAP-014**) is resolved before go-live.

## 2.7 Business Rules Summary

The following immutable business rules govern Phase 1 module behaviour. Violation of any rule by any system component is a critical defect.

| Rule ID | Summary | Modules Affected |
|---|---|---|
| **BR-001** | Dual-Track Inventory Separation — warehouse and agent stock never merged | F-003, F-004 |
| **BR-002** | FIFO Remittance Allocation — stored procedure `sp_apply_remittance_to_invoices` | F-004 |
| **BR-003** | Segregation of Duties — enforced at API layer | F-001, F-002, F-003, F-004 |
| **BR-006** | Agent Stock Float Limit — issuance blocked if limit exceeded | F-003, F-004 |
| **BR-007** | FEFO Enforcement — automatic earliest-expiry batch selection | F-001, F-002, F-003 |
| **BR-009** | Sequential Numbering and Gap Detection — invoices, receipts, JEs | F-001, F-002 |
| **BR-013** | GL Hash Chain Integrity | F-001, F-002, F-003, F-004 |
| **BR-015** | Commission on Verified Sales Only | F-004 |
