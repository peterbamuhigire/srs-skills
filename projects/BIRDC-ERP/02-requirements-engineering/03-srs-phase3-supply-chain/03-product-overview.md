# 2. Product Overview

## 2.1 Product Perspective

The BIRDC ERP system is a single-tenant, on-premise web application deployed on BIRDC-owned hardware at Nyaruzinga, Bushenyi. Phase 3 modules operate within the same system boundary as Phases 1 and 2, sharing the MySQL 9.1 database, authentication subsystem, and General Ledger auto-posting infrastructure.

The Farmer Delivery Android application is a satellite client that operates independently in offline mode and synchronises to the central server via a REST API over HTTPS when connectivity is available. It is architecturally separate from the web application but shares the same business rule enforcement layer at the API level.

Phase 3 produces inventory that feeds Phase 4 (Manufacturing). The procurement GL postings feed Phase 2 (Financial Accounting). This document does not re-specify requirements already covered in Phases 1 and 2; it references them by identifier.

## 2.2 Product Functions Summary

Phase 3 delivers the following primary capabilities:

**F-009 — Procurement & Purchasing:**

- Purchase Request creation and PPDA-compliant approval workflow
- Request for Quotation issuance and supplier response management
- Local Purchase Order generation in Uganda standard format
- Goods Receipt Note creation with three-way matching enforcement (BR-012)
- 5-stage cooperative farmer procurement workflow (BR-011)
- Vendor directory management, separate from cooperative farmer records
- Landed cost allocation for imported inputs
- Purchase returns processing with GL reversal

**F-010 — Farmer & Cooperative Management:**

- Farmer registration with NIN, GPS, biometric photo, mobile money details
- Farm profiling with GPS polygon boundary and banana variety inventory
- Cooperative hierarchy management (farmer → primary cooperative → zone → BIRDC network)
- Farmer delivery history and account statement generation
- Extension services tracking: training, input loans, officer visit logs
- Farmer performance analysis and ranking tools
- Bulk mobile money payment scheduling with MTN MoMo / Airtel Money API integration
- Farmer Delivery Android app for offline field data collection

## 2.3 User Classes and Characteristics

| User Class | Module Access | Technical Proficiency | Volume |
|---|---|---|---|
| Procurement Manager (Robert) | F-009 full access | Proficient | 1 |
| Finance Manager | PR approval, payment authorisation, three-way match review | Proficient | 1 |
| Department Heads | PR creation, budget checking | Basic | ~8 |
| Store Manager (David) | GRN creation, stock receipt | Basic | 1 |
| Procurement Officer | RFQ, LPO management | Proficient | ~3 |
| Field Collection Officers (Patrick) | Farmer Delivery App | Basic smartphone | ~20 |
| Farmers | Farmer portal (future phase) | Basic feature phone / smartphone | 6,440+ |
| Finance Director (Grace) | AP payments, farmer payment approval | Proficient | 1 |
| IT Administrator | System configuration | Advanced | 1 |

## 2.4 Operating Environment

- **Web application:** PHP 8.3+, MySQL 9.1, Apache/Nginx on BIRDC on-premise server, Bushenyi, Uganda.
- **Web browsers:** Chrome 110+, Firefox 110+, Edge 110+.
- **Android app:** Kotlin, Jetpack Compose, Room (SQLite), WorkManager. Minimum Android 8.0 (API 26).
- **Connectivity:** Intermittent 3G/4G in Bushenyi and rural collection points. The Farmer Delivery App must function fully offline (DC-005).
- **Printing:** Bluetooth 80mm ESC/POS thermal printers at field collection points.
- **Weighing:** Bluetooth digital weighing scales at cooperative collection points [CONTEXT-GAP: GAP-011].

## 2.5 Design Constraints

All requirements in this document are subject to the 7 binding Design Covenants (DC-001 through DC-007) defined in `_context/vision.md`. The constraints most relevant to Phase 3 are:

- **DC-002 (Configuration over code):** All PPDA procurement threshold values, quality grade pricing schedules, and cooperative levy rates must be configurable via the administration UI without developer involvement.
- **DC-003 (Audit readiness):** Every procurement transaction — from PR through payment — creates an immutable, timestamped audit trail entry recording the actor, action, and data state before and after.
- **DC-005 (Offline-first):** The Farmer Delivery App must function completely without server connectivity. All field data collected offline must be preserved and synchronised without data loss on reconnection.
- **DC-006 (Data sovereignty):** All farmer personal data — NIN, GPS coordinates, photos, mobile money numbers — is stored exclusively on BIRDC's on-premise server. No farmer data is transmitted to or stored by any cloud SaaS vendor.

## 2.6 Assumptions and Dependencies

1. Phase 1 (F-003: Inventory & Warehouse Management) is deployed and the stock item catalogue is populated before Phase 3 goods receipt functions are activated.
2. Phase 2 (F-005: Financial Accounting) is deployed and the Chart of Accounts is configured before Phase 3 GL auto-posting is activated.
3. The PPDA procurement threshold values (UGX amounts) will be confirmed by BIRDC Administration before the approval matrix is configured [CONTEXT-GAP: GAP-007].
4. MTN MoMo Business API and Airtel Money API sandbox credentials will be provided before farmer payment integration testing [CONTEXT-GAP: GAP-002, GAP-003].
5. A legal review of farmer personal data collection under the Uganda Data Protection and Privacy Act 2019 will be completed before go-live [CONTEXT-GAP: GAP-004].
6. The model and Bluetooth SDK of weighing scales deployed at collection points will be confirmed before Farmer Delivery App hardware integration is finalised [CONTEXT-GAP: GAP-011].
7. All 6,440+ existing farmers must be imported via bulk import or data entry before the system goes live.
