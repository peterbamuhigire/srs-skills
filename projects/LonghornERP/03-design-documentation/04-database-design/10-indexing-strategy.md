# Indexing Strategy

## Governing Principle

Indexes in Longhorn ERP are designed around the multi-tenant access pattern. Because every operational query filters by `tenant_id`, this column must be the leftmost column in every compound index on operational tables. Placing `tenant_id` first allows the MySQL InnoDB query planner to use the index's tenant partition as the primary filter, avoiding full-table scans regardless of how large the dataset grows across all tenants.

## Tenant Isolation Index Rule

Every compound index on an operational table (any table with a `tenant_id` column) must begin with `tenant_id`. This rule applies to all table types — transactional, lookup-join, and soft-deleted record sets.

Correct:

```sql
CREATE INDEX idx_invoices_status ON invoices (tenant_id, status, due_date);
```

Incorrect (will be flagged in code review and PHPStan static analysis):

```sql
CREATE INDEX idx_invoices_status ON invoices (status, tenant_id, due_date);
```

## Primary Key Strategy

All tables will use a `BIGINT UNSIGNED AUTO_INCREMENT` surrogate primary key named `id`. Natural keys (e.g., `invoice_number`, `employee_number`) will carry a UNIQUE index in addition to the primary key but will not serve as the primary key. This ensures:

- Foreign key joins use an 8-byte integer, not a variable-length string.
- Natural keys can be regenerated or reformatted without cascading FK updates.
- InnoDB clustered index behaviour is predictable and insertion-ordered.

## Immutable Log Table Indexes (Covering Indexes)

Tables that are INSERT-only and used primarily for range queries — `stock_ledger`, `audit_log`, and `account_ledgers` — will use covering indexes that include all columns needed by their most frequent queries. This allows the query to be satisfied entirely from the index without a table row lookup.

### `stock_ledger` Covering Index

The most frequent query pattern is: retrieve all movements for a given item at a given branch within a date range.

```sql
CREATE INDEX idx_stock_ledger_item_branch_date
    ON stock_ledger (tenant_id, item_id, branch_id, posting_date, movement_type, quantity, unit_cost);
```

### `audit_log` Covering Index

The most frequent query pattern is: retrieve all actions by module within a date range for a given tenant.

```sql
CREATE INDEX idx_audit_log_module_date
    ON audit_log (tenant_id, module, created_at, action, user_id, record_table, record_id);
```

### `account_ledgers` Covering Index

The most frequent query pattern is: retrieve all postings to a given account within a date range.

```sql
CREATE INDEX idx_account_ledgers_account_date
    ON account_ledgers (tenant_id, account_id, posting_date, debit, credit, balance);
```

## Soft-Delete Pattern

Tables that use a status or `is_active` column to logically delete records (rather than physically removing rows) will carry a compound index on `(tenant_id, status)` or `(tenant_id, is_active)`. Active-record list screens will filter on this index, preventing a full-table scan over the full historical dataset.

Examples:

```sql
CREATE INDEX idx_stock_items_active ON stock_items (tenant_id, is_active);
CREATE INDEX idx_employees_status ON employees (tenant_id, status);
CREATE INDEX idx_invoices_status_due ON invoices (tenant_id, status, due_date);
```

## Foreign Key Constraints

InnoDB will enforce all foreign key constraints defined in the schema. Every `FK → <parent_table>.id` relationship noted in the table specifications will be declared as an explicit `FOREIGN KEY` constraint in the migration DDL. Cascading behaviour will be:

- `ON DELETE RESTRICT` — the default; prevents orphaned child records.
- `ON UPDATE CASCADE` — applied only where the parent primary key is a natural key that may legitimately change (e.g., `currencies.code`).
- No `ON DELETE CASCADE` will be used on financial transaction tables, as it would allow silent data loss.

## Unique Constraints

All business uniqueness rules documented in the table specifications will be enforced at the database level with `UNIQUE` indexes, not only at the application layer. Application-layer uniqueness checks are supplementary and do not replace the database constraint.

Examples:

```sql
UNIQUE KEY uq_users_email (tenant_id, email)
UNIQUE KEY uq_invoice_number (tenant_id, invoice_number)
UNIQUE KEY uq_stock_balance (tenant_id, item_id, branch_id)
```

## Indexes to Avoid

The following index patterns are prohibited because they create write overhead without proportionate read benefit:

- Indexing every column individually when a compound index covers the same queries.
- Duplicate indexes that are a prefix-subset of an existing index (e.g., do not create `(tenant_id)` alone if `(tenant_id, status)` already exists).
- Full-text indexes on operational transaction tables; use a dedicated search service for full-text requirements.
- Indexes on JSON columns using generated columns unless a specific high-frequency query justifies the overhead.

## Index Review Cadence

Index performance will be reviewed using the MySQL `sys.schema_unused_indexes` and `EXPLAIN` output at each major milestone:

1. End of Phase 1 UAT, before production go-live.
2. At 10,000 tenant-records per major table.
3. Whenever a query in production exceeds 200 ms at P95 under normal load.

Unused indexes identified at review will be removed in a dedicated migration to reduce write amplification.
