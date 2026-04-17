---
title: "Data Migration Plan — BIRDC ERP"
subtitle: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
status: "Draft — Pending GAP-012 and GAP-014 Resolution"
---

# Data Migration Plan — BIRDC ERP

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC
**Date:** 2026-04-05
**Version:** 1.0
**Status:** Draft — Pending GAP-012 and GAP-014 Resolution

---

## 1. Overview and Objectives

### 1.1 Purpose

This plan governs the migration of all relevant operational and financial data from BIRDC's current systems into the BIRDC ERP at each phase go-live. "Current systems" means the aggregate of Excel workbooks, manual registers, and any legacy accounting or operational software presently in use at PIBID/BIRDC, Nyaruzinga, Bushenyi.

### 1.2 Critical Dependency Notice

`[CONTEXT-GAP: GAP-014]` — The identity of BIRDC's existing accounting software (if any), the structure of its exported data, and the full scope of migrateable records are unknown at the time of writing. This plan uses reasonable assumptions based on context provided by BIRDC stakeholders. **All volume estimates and source-system references must be validated with the Finance Director (STK-002) before migration execution begins.** A discovery session covering GAP-014 is a pre-condition for executing Section 5 (Opening Balances Protocol) and Section 7 (Migration Timeline).

`[CONTEXT-GAP: GAP-012]` — It is unconfirmed whether BIRDC holds an existing Chart of Accounts with 1,307 accounts or whether this must be designed from scratch. Chart of Accounts migration (or initial load) cannot proceed until GAP-012 is resolved with the Finance Director.

### 1.3 Migration Principles

The following principles are binding. No migration step proceeds if any principle cannot be satisfied:

- **Zero financial data loss.** Every account balance, invoice, and payment recorded in the legacy system must be accounted for in the ERP before the legacy system is decommissioned.
- **Accounting period continuity.** The first ERP accounting period opens with balances that reconcile exactly to the last legacy trial balance at the cutover date.
- **Farmer records preserved.** All cooperative farmer registration data migrated from the source register into `tbl_farmers` without truncation, encoding corruption, or loss of NIN linkage (subject to GAP-004 DPPA legal review before Phase 3 cutover).
- **Agent balances reconciled.** Every agent's outstanding cash balance in the legacy register is carried forward to `tbl_agent_stock_balance` and `tbl_agent_invoices` and verified by the Sales Manager (STK-006) before go-live.

---

## 2. Migration Scope

The table below lists every data category in scope for migration, the expected source system, the target ERP table(s), estimated record volume, and migration priority.

| Data Category | Source | Destination Table(s) | Est. Volume | Priority |
|---|---|---|---|---|
| Chart of Accounts | Current CoA (Excel/legacy) [GAP-012] | `tbl_accounts` | 1,307 accounts | Critical |
| Opening GL balances | Trial balance at cutover date | `tbl_journals` (opening entries) | 1 entry per account | Critical |
| Customer accounts | Current AR ledger | `tbl_customers` | ~360 accounts | High |
| Outstanding AR invoices | Current debtor aging | `tbl_invoices` | TBD [GAP-014] | High |
| Vendor/supplier list | Current AP records | `tbl_vendors` | TBD [GAP-014] | High |
| Outstanding AP bills | Current creditor aging | `tbl_bills` | TBD [GAP-014] | High |
| Product/SKU catalogue | Current product list | `tbl_products` | 398+ SKUs | High |
| Current stock balances | Latest physical stock count | `tbl_stock_balance` | Per SKU per location | High |
| Agent list and territories | Current agent register | `tbl_agents`, `tbl_territories` | 1,071 agents | High |
| Agent outstanding balances | Current agent ledger | `tbl_agent_stock_balance`, `tbl_agent_invoices` | Per agent | High |
| Farmer register | Excel/cooperative register | `tbl_farmers`, `tbl_cooperatives` | 6,440+ farmers | Medium (Phase 3) |
| Employee records | HR files | `tbl_employees` | 150+ staff | Medium (Phase 5) |
| Parliamentary budget codes | Current vote register | `tbl_parliamentary_segments` | Per vote code | Medium (Phase 2) |
| Fixed assets register | Current asset register | `tbl_assets` | TBD [GAP-014] | Medium (Phase 6) |

> *Volumes marked "TBD" are subject to GAP-014 discovery. The Finance Director must provide record counts before migration scripts are parameterised.*

---

## 3. Migration Approach

### 3.1 Parallel Run Period

The legacy system and the BIRDC ERP run simultaneously for 1 full accounting month (the cutover month). During this period:

- All financial transactions are entered in both systems.
- At the end of the parallel run month, the Finance Director compares the trial balance from both systems.
- The legacy system is decommissioned only after the Finance Director confirms the trial balances are identical.

### 3.2 Cutover Strategy

Start-of-financial-year cutover is preferred. This minimises the volume of mid-year accruals and eliminates the need to split annual totals. The PIBID financial year begins 1 July; the commercial year may begin 1 January. If project delivery does not align with a year-start, a mid-year cutover is permitted under the following conditions:

- The legacy trial balance at the cutover date is extracted and signed off by the Finance Director before migration begins.
- All year-to-date figures are imported as opening journals dated the first day of the first ERP period, not as historical transactions.
- Comparative figures for statutory reporting are maintained in the legacy system for the remainder of the financial year.

### 3.3 Data Validation — 3-Way Reconciliation

Before any data category is accepted into production, a 3-way reconciliation is performed:

1. **Source total** — record count and financial total extracted from the legacy system/Excel export.
2. **Migration tool count** — record count and total produced by the migration script (`migrations/migrate_legacy.php`) after processing.
3. **ERP system count** — record count and total queried directly from the target ERP database table.

All 3 figures must match. Any discrepancy halts migration of that category until the root cause is identified and resolved.

### 3.4 Rollback Plan

If a critical reconciliation failure occurs after migration to production:

1. Migration is immediately halted.
2. The BIRDC ERP database is reset to the pre-migration backup taken by the IT Administrator (STK-028) before migration commenced.
3. The legacy system remains the operational system.
4. Peter Bamuhigire investigates root cause, corrects migration scripts, and re-runs the full staging dry-run before scheduling a new production migration date.

---

## 4. Migration Tools and Process

### 4.1 Primary Migration Script

The primary tool is a PHP migration script located at `migrations/migrate_legacy.php` in the ERP source code repository. This script:

- Accepts CSV or Excel exports produced by the legacy system as input.
- Validates each record against mandatory field rules (Section 6) before inserting.
- Logs every inserted, skipped, and rejected record to `migrations/logs/migration_YYYYMMDD.log`.
- Produces a reconciliation summary (record counts and financial totals) to stdout at completion.

The script is version-controlled. Each migration run uses a tagged version of the script, recorded in the change register.

### 4.2 Secondary Method — Manual Entry

For low-volume data categories where the source format does not support automated extraction (e.g., fixed assets register, parliamentary budget vote codes), records are entered manually by the Accounts Assistants (STK-018) under supervision of the Finance Director, using the ERP's standard data entry screens.

### 4.3 Staging Environment

A full migration dry-run is executed on the staging server before every production migration. The staging dry-run uses a copy of the same legacy export files that will be used in production. Staging results are reviewed and signed off by Peter Bamuhigire before the production migration is scheduled.

### 4.4 Script Storage and Version Control

All migration scripts are stored in the `/migrations/` directory of the ERP repository and are version-controlled via Git. Each script file is named `migrate_<data_category>_<version>.php`. No migration script is executed on production without first being committed to the repository and passing the staging dry-run.

---

## 5. Opening Balances Protocol

### 5.1 GL Opening Balance Import

General Ledger opening balances are imported as a single journal entry per account posted on the first day of the first ERP accounting period. Each opening journal entry is labelled with the description "OPENING BALANCE — MIGRATION" and a reference to the legacy trial balance date.

Entry structure per account:

- Accounts with a debit balance: DR `tbl_accounts.account_code` / CR `tbl_accounts.suspense_migration`
- Accounts with a credit balance: DR `tbl_accounts.suspense_migration` / CR `tbl_accounts.account_code`

After all opening entries are posted, the suspense migration account balance must equal zero (total debits = total credits). Any non-zero residual in the suspense account indicates a migration error and must be resolved before the Finance Director signs off.

### 5.2 Finance Director Sign-Off Requirement

The Finance Director must review and sign the opening trial balance print-out before any live transaction is posted in the ERP. This sign-off is a formal acceptance gate. No Phase go-live proceeds without it.

### 5.3 Parliamentary Vote Opening Balances

Parliamentary budget vote opening balances are imported to both the commercial segment and the parliamentary segment of the dual-mode chart of accounts (DC-004). The Finance Director confirms both segments independently before sign-off.

---

## 6. Data Quality Rules

The following rules are enforced by the migration script before any record is committed to the database. Records that fail validation are written to the rejection log and are not inserted.

### 6.1 Mandatory Field Validation

Every record is checked for non-null values in all fields designated NOT NULL in the database schema. Format validation is applied to:

- NIN (National Identification Number): must match Uganda NIN format.
- Mobile money numbers: must be valid MTN Uganda or Airtel Uganda format (10 digits, correct network prefix).
- Account codes: must match the chart of accounts code pattern.
- Foreign key references: parent record must exist in the target table before child records are inserted (e.g., `tbl_cooperatives` record must exist before farmer records are inserted).

### 6.2 Duplicate Detection

The migration script checks for duplicates before inserting:

- Farmers and employees: NIN must be unique across `tbl_farmers` and `tbl_employees` respectively.
- Account codes: must be unique in `tbl_accounts`.
- Agent mobile money numbers: must be unique in `tbl_agents`.
- Any duplicate detected is written to the rejection log with the conflicting existing record's ID.

### 6.3 Personal Data Encryption

Special personal data fields — mobile money numbers and salary/payroll data — are encrypted using AES-256-GCM immediately on migration insert, using the same encryption keys and key management process as the production ERP. No plaintext personal data resides in the database after migration insertion completes.

---

## 7. Migration Timeline by Phase

Migration activities are linked to the 7 ERP delivery phases. Each phase cutover is preceded by a staging dry-run and followed by the Finance Director acceptance gate.

| Phase | Go-Live Scope | Migration Activities |
|---|---|---|
| Phase 1 | Commerce Foundation | Products/SKUs, current stock balances, customers, agent list, agent outstanding balances, Chart of Accounts, GL opening balances |
| Phase 2 | Financial Core | Outstanding AR invoices (debtor aging), outstanding AP bills (creditor aging), parliamentary budget codes |
| Phase 3 | Supply Chain & Farmers | Farmer register and cooperative data (subject to GAP-004 DPPA legal review) |
| Phase 5 | People | Employee records (HR files) |
| Phase 6 | Research, Administration & Compliance | Fixed assets register, contracts, R&D baseline data |
| Phase 7 | Go-Live | Final reconciliation audit; legacy system decommission sign-off |

> *Phase 4 (Production & Quality) and Phase 7 (Integration, Hardening & Go-Live) have no primary migration loads. Phase 7 is the final verification and decommission gate.*

---

## 8. Acceptance Criteria

The migration for each phase is formally accepted when all of the following conditions are met and documented:

- The Finance Director confirms the ERP opening trial balance matches the pre-migration legacy trial balance figure (signed reconciliation form).
- AR aging totals in the ERP match the pre-migration debtor aging extract (Phase 2).
- AP aging totals in the ERP match the pre-migration creditor aging extract (Phase 2).
- Agent outstanding balances in `tbl_agent_invoices` reconcile to the pre-migration agent ledger, verified and signed by the Sales Manager (STK-006).
- Stock on-hand quantities in `tbl_stock_balance` reconcile to the pre-migration physical count, verified and signed by the Store Manager (STK-008).
- All 3-way reconciliation sign-off forms (source / migration tool / ERP) are signed for every data category migrated in the phase.
- No records remain in the migration rejection log that are unexplained and unresolved.

---

## 9. Roles and Responsibilities

| Role | Stakeholder ID | Responsibility |
|---|---|---|
| Peter Bamuhigire, ICT Consultant | — | Migration script development, staging dry-run execution, production migration execution, rejection log analysis |
| Finance Director | STK-002 | Legacy data export approval, opening trial balance sign-off, phase acceptance sign-off, dual-mode (commercial + parliamentary) balance verification |
| Store Manager | STK-008 | Stock balance verification — confirms ERP stock on-hand quantities match pre-migration physical count |
| Sales Manager | STK-006 | Agent balance verification — confirms agent outstanding balances match pre-migration agent ledger |
| Procurement Manager | STK-007 | Farmer register verification (Phase 3) — confirms farmer records are complete and correctly linked to cooperatives |
| IT Administrator | STK-003 | Server access provisioning, full database backup before each migration run, staging environment maintenance |

---

## 10. Risk Register — Migration-Specific

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| MIG-R-001 | GAP-014 unresolved — legacy system identity unknown | High | Critical | Schedule a dedicated discovery session with the Finance Director before Phase 1 planning begins. Block migration planning until output of discovery session is documented. |
| MIG-R-002 | GAP-012 unresolved — Chart of Accounts not available | High | Critical | GAP-012 must be resolved before Phase 1 migration is scheduled. If no existing CoA is available, the Finance Director and Peter design a new CoA from scratch using the ERP's account configuration screens. Allow minimum 5 working days for CoA design and review. |
| MIG-R-003 | Legacy data quality issues — missing fields, inconsistent formats, duplicate records | Medium | High | Build and run data quality validation scripts against legacy exports at least 2 weeks before migration day. Produce a data quality report for the Finance Director. Resolve all critical quality issues before the production migration date is confirmed. |

---

## 11. Open Gaps

The following gaps remain unresolved at the time of writing. Migration execution is blocked on their resolution.

- `[CONTEXT-GAP: GAP-012]` — Chart of Accounts identity: it is unconfirmed whether BIRDC holds a 1,307-account CoA or whether one must be designed from scratch. Owner: Finance Director (STK-002). Trigger: required before Phase 1 migration is scheduled.
- `[CONTEXT-GAP: GAP-014]` — Legacy system identity and migration data volume: the name, version, and data export capability of BIRDC's existing accounting software (if any) are unknown. Owner: Finance Director (STK-002) / Peter Bamuhigire. Trigger: required before migration scripts can be parameterised and data volume estimates finalised.
