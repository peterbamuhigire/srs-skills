# Database Migration Strategy

## Overview

All schema changes in Longhorn ERP will be managed through a versioned migration system. No manual Data Definition Language (DDL) statements will be executed directly against a production database. Every structural change — including table creation, column additions, index changes, and stored procedure updates — will be delivered as a migration file and executed through the migration runner.

## File Naming Convention

Migration files will be placed in the `database/migrations/` directory and named using the following format:

```
YYYY_MM_DD_HHMMSS_description.sql
```

Examples:

```
2026_04_05_093000_create_tenants_table.sql
2026_04_05_093100_create_users_table.sql
2026_04_10_140000_add_wht_applicable_to_suppliers.sql
```

The timestamp prefix guarantees deterministic execution order. The description uses lowercase words separated by underscores, clearly stating the change being made.

## Entry Point

The migration entry point is `run_migrations.php`, a Command Line Interface (CLI) script executed as follows:

```
php run_migrations.php
```

The script will:

1. Connect to the database using credentials from the `.env` file.
2. Read the `migrations` tracking table to determine which files have already been applied.
3. Identify unapplied migration files in `database/migrations/` by comparing filenames.
4. Execute each unapplied file in ascending timestamp order, wrapping each in a transaction.
5. On success, insert a record into the `migrations` table with the filename and execution timestamp.
6. On failure, roll back the transaction, log the error, and halt execution. Subsequent migrations will not run until the failed one is resolved.

## Idempotency Requirement

Every migration file must be idempotent: safe to re-run without causing errors or duplicate state. This is achieved by using conditional DDL guards:

- `CREATE TABLE IF NOT EXISTS` for table creation.
- `ALTER TABLE ... ADD COLUMN IF NOT EXISTS` for column additions (MySQL 8.0+).
- `DROP INDEX IF EXISTS` before `CREATE INDEX` to avoid duplicate index errors.
- `CREATE OR REPLACE PROCEDURE` for stored procedure definitions.
- `CREATE OR REPLACE VIEW` for view definitions.

Idempotency ensures that a migration re-run caused by a deployment script retry does not leave the schema in an inconsistent state.

## Immutability Rule

Once a migration file has been applied to any environment — development, staging, or production — it must not be modified. Changes to an already-applied migration must be delivered as a new migration file with a later timestamp. This rule preserves a verifiable, auditable history of every schema change and prevents schema drift between environments.

## Migration Tracking Table

The `migrations` table is created by `run_migrations.php` on first run if it does not exist:

```sql
CREATE TABLE IF NOT EXISTS migrations (
    id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    filename    VARCHAR(255) NOT NULL UNIQUE,
    applied_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## Deployment Integration

In the Continuous Integration (CI) pipeline, `php run_migrations.php` will be executed as the first step after the application code is deployed. Deployment will be halted if the migration runner exits with a non-zero status.

On production, migrations will be executed during a maintenance window or as a zero-downtime rolling deployment depending on the scope of the change. DDL operations that lock tables (such as adding a non-nullable column without a default) will be avoided; all such changes will use a two-step migration: first add the column as nullable, backfill data, then add the NOT NULL constraint.

## Rollback Policy

MySQL does not support transactional DDL rollback for all statement types (e.g., `CREATE TABLE` is auto-committed). Therefore, rollback migrations will be maintained as separate `_rollback` files where feasible:

```
2026_04_10_140000_add_wht_applicable_to_suppliers.sql
2026_04_10_140000_add_wht_applicable_to_suppliers_rollback.sql
```

Rollback files will be executed manually by the Database Administrator (DBA) following an explicit decision to revert a deployment. They will not be executed automatically.

## Prohibited Practices

- Executing DDL statements directly against a production database outside of the migration runner.
- Modifying an existing migration file after it has been applied.
- Embedding business data changes (DML) inside a migration unless those data changes are required to make the schema change functional (e.g., populating a new non-nullable column).
- Dropping columns or tables in the same migration that removes references to them — allow at least one deployment cycle before issuing the DROP to avoid breaking in-flight application instances.
