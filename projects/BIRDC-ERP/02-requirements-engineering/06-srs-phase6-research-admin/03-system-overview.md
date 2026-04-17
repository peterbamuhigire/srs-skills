# 2. Overall Description

## 2.1 System Context

The Phase 6 modules operate within three application panels of the BIRDC ERP:

- **Main ERP Workspace** (`/public/`): Research Coordinator (F-015), Administration Officer (F-016), and all staff functions
- **System Administration Panel** (`/public/admin/`): IT Administrator functions — user management, role matrix, audit logs, backup, integration configuration, and system health (F-017)

Phase 6 modules interact with:

- **Phase 2 (F-005 General Ledger):** R&D expenditures post to the GL Research cost centre. Asset depreciation posts as monthly journal entries. PPDA procurement payments are blocked until all PPDA document checklist items are complete (BR-005).
- **Phase 3 (F-009 Procurement & F-010 Farmer Management):** Procurement register (F-016) draws from F-009 procurement transactions. R&D variety data (F-015) cross-references farmer farm profiles and banana varieties from F-010.
- **All 17 modules:** F-017 System Administration governs user accounts, permissions, audit logs, backups, and integration credentials for the entire ERP system.
- **External integrations managed in F-017:** EFRIS API, MTN MoMo API, Airtel Money API, ZKTeco biometric devices, PHPMailer SMTP, Africa's Talking SMS gateway.

## 2.2 User Classes and Characteristics

| User Class | Module Access | Key Actions |
|---|---|---|
| Research Coordinator (STK-013) | F-015 full access | Variety database, field trials, product development register, R&D expenditure |
| Administration Officer (STK-014) | F-016 full access | PPDA register, document store, asset register, vehicle logbook, contract register |
| IT Administrator (STK-003) | F-017 full access (admin panel) | User management, role matrix, audit log, backup, integration config, system health |
| Finance Director (STK-002) | F-016 read; F-015 R&D GL; F-017 audit log read | R&D cost review, PPDA compliance oversight, audit log review |
| BIRDC Director (STK-001) | F-015 read; F-016 read | R&D performance reporting, asset register review |
| Finance Manager | F-016 — asset depreciation approval, contract approval | Asset register approval, PPDA payment clearance |
| Procurement Manager (STK-007) | F-016 PPDA register | Document status management per procurement transaction |

## 2.3 Operating Environment

All Phase 6 modules run on the on-premise BIRDC server at Nyaruzinga, Bushenyi. There are no offline requirements for Phase 6 modules (unlike Phase 1 POS and Phase 3 Farmer Delivery App). The administration panel (`/public/admin/`) is restricted to LAN or VPN access; it shall not be accessible from the public internet.

## 2.4 Design and Implementation Constraints

- **DC-002:** All PPDA threshold values, asset depreciation methods, document checklist items, and report schedules are configurable via the UI by the IT Administrator or Finance Director without developer involvement.
- **DC-003:** Every document access, user account change, permission modification, and backup event creates an immutable audit trail. 7-year retention enforced.
- **DC-006:** All BIRDC data — R&D records, asset records, configuration — stored on BIRDC's own server. No third-party SaaS holds configuration data.
- **DC-007:** Phase 6 modules are designed so that PPDA threshold values, procurement categories, and system integration credentials are isolated in configuration tables, enabling redeployment for another government entity.
- **BR-005:** No payment for any procurement transaction is processed unless all required PPDA documents are recorded in the procurement document checklist for that transaction.

## 2.5 Assumptions and Dependencies

- PPDA exact threshold values (UGX) applicable to BIRDC/PIBID as a government entity will be confirmed by BIRDC Administration before the procurement approval matrix is configured. `[CONTEXT-GAP: GAP-007]`
- Server hardware specifications at BIRDC Nyaruzinga will be confirmed by BIRDC IT before the deployment guide and system health dashboard baseline thresholds are set. `[CONTEXT-GAP: GAP-013]`
