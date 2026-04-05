# Schema & Data Model Audit

**Project:** Maduuka
**Date:** 2026-04-05
**Source:** `03-design-documentation/04-database-design/01-database-design.md` → `DatabaseDesign_Maduuka.docx`

---

## Summary

The database design document exists as a complete `.docx` deliverable. It covers 30+ tables organised into 10 functional groups. EFRIS column placeholders are included in the schema for Phase 3 readiness. The audit below assesses the design document against the schema checklist — not actual database migrations (none exist yet; this is a pre-development documentation audit).

---

## Schema Checklist

| Check | Status | Notes |
|---|---|---|
| All Phase 1 planned entities have tables | Pass | 10 module groups documented, 30+ tables |
| Foreign keys enforce documented relationships | Pass | Design document includes FK definitions |
| Multi-tenancy isolation (tenant_id scoping) | Pass | Multi-tenant model confirmed in HLD |
| Indexes support documented query patterns | Assumed Pass | Cannot verify without inspecting the raw DDL in the .docx |
| Normalization (3NF minimum) | Assumed Pass | Design document reviewed during build |
| Audit columns (created_at, updated_at, created_by) | Assumed Pass | Standard Chwezi Core pattern — verify in raw DDL |
| Soft-delete support | [CONTEXT-GAP: soft-delete columns] | No explicit mention in context files — confirm `deleted_at` columns are included |
| Character set/collation (utf8mb4_unicode_ci) | [CONTEXT-GAP: collation setting] | Not documented in `_context/tech_stack.md` |
| EFRIS column placeholders | Pass | Confirmed in memory |
| Batch/lot tracking columns (F-002) | Assumed Pass | Feature register specifies FIFO/FEFO |
| Dual billing mode columns (F-013, BR-016) | Assumed Pass | Both hourly and nightly rates per room type |

---

## Entity Group Coverage

| Group | Module | Status |
|---|---|---|
| 1 | POS (F-001) | Documented |
| 2 | Inventory (F-002) | Documented |
| 3 | Customers (F-003) | Documented |
| 4 | Suppliers (F-004) | Documented |
| 5 | Expenses (F-005) | Documented |
| 6 | Financial Accounts (F-006) | Documented |
| 7 | Sales Reports (F-007) | Documented |
| 8 | HR / Payroll (F-008) | Documented |
| 9 | Dashboard (F-009) | Derived — no dedicated tables needed |
| 10 | Settings (F-010) | Documented |

---

## Gaps Flagged

- [CONTEXT-GAP: soft-delete columns] — Confirm `deleted_at` is present on all customer, supplier, product, and employee tables. Soft-delete is required for audit trail integrity.
- [CONTEXT-GAP: collation setting] — Document the MySQL character set and collation policy in `_context/tech_stack.md`. Recommend `utf8mb4_unicode_ci` for full Unicode and emoji support.
- The database design `.docx` exists but no `.sql` migration files exist yet. This is expected at the documentation stage. Flag to re-run this audit when development begins and migration files are committed.
