---
title: "BIRDC ERP — Database Design Specification"
subtitle: "Design Documentation — Document 04-DATABASE-DESIGN"
author: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0 — Draft"
---

# BIRDC ERP — Database Design Specification

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC
**Date:** 2026-04-05
**Version:** 1.0 — Draft
**Classification:** Confidential — BIRDC Internal

---

## Document Purpose

This specification defines the relational database schema for the BIRDC ERP system — a single-tenant MySQL 9.1 InnoDB database hosted on BIRDC's on-premise server at Nyaruzinga, Bushenyi. The schema covers all 17 operational modules across 7 delivery phases.

For each table this document provides:

- Table name and purpose
- Key columns with data type and constraints
- Foreign key relationships
- Index definitions
- `CREATE TABLE` SQL for key tables

## Database Standards

All tables are created with the following baseline settings:

- Storage engine: `InnoDB`
- Character set: `utf8mb4`
- Collation: `utf8mb4_unicode_ci`
- All primary keys: `INT UNSIGNED AUTO_INCREMENT` named `<table_short>_id`
- Soft deletes: `deleted_at DATETIME NULL` where records must be retained for audit
- Audit columns on all tables: `created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP`, `updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP`, `created_by INT UNSIGNED NULL`
- All `DECIMAL` columns for money: `DECIMAL(18,4)` — sufficient precision for UGX, USD, EUR, KES
- 7-year data retention enforced by policy; hard deletes prohibited on financial tables

## Critical Architecture Decisions

### BR-001: Dual-Track Inventory Separation

Warehouse stock and agent field stock are maintained in entirely separate tables:

- `tbl_stock_balance` — warehouse inventory only
- `tbl_agent_stock_balance` — agent field inventory only

No JOIN, UNION, or stored procedure may combine rows from these two tables without an explicit label. Any consolidated report that includes both must label each source. This architectural separation is enforced in schema design, application code, and API layer.

### BR-013: GL Hash Chain Integrity

`tbl_journals` contains a `hash_prev` column (`CHAR(64)`) that stores the SHA-256 hash of the previous journal entry in the same account's series. Any modification to a historical journal entry breaks the chain — detectable by the Finance Director's integrity verification function. This column is set by the application on journal insertion and is never updated. The `hash_self` column stores the SHA-256 hash of this entry's own content.

### DC-004: Dual-Mode Accounting

`tbl_accounts` includes a `parliamentary_segment` column to classify accounts under PIBID parliamentary budget votes. Both IFRS commercial accounts and parliamentary vote accounts coexist in the same chart of accounts table, distinguished by the `accounting_mode` column (`commercial`, `parliamentary`, `both`).

---
