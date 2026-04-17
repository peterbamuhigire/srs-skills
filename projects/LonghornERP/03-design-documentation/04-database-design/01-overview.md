# Database Platform Overview

## Platform and Engine

Longhorn ERP will use MySQL 9.1 as its relational database management system. All tables will use the InnoDB storage engine, which provides ACID-compliant transactions, row-level locking, crash recovery, and foreign key constraint enforcement. The global character set will be UTF8MB4 with UTF8MB4_unicode_ci collation, ensuring correct storage and sorting of Unicode text including emoji and multi-byte African language characters.

## Multi-Tenancy Architecture

Longhorn ERP will implement a shared-database, shared-schema multi-tenancy pattern with row-level isolation. A single database instance will serve all tenants. Every operational table will include a `tenant_id BIGINT UNSIGNED NOT NULL` column as a foreign key referencing `tenants.id`. The application layer will source `tenant_id` exclusively from the authenticated session and will never accept it as a request parameter.

This pattern is chosen over separate-database-per-tenant because it:

- Reduces infrastructure overhead for the initial Uganda market phase.
- Allows a single migration run to upgrade all tenants simultaneously.
- Enables cross-tenant analytics at the super-admin level without schema federation.

The trade-off — that a misconfigured query could expose cross-tenant data — is mitigated by the following controls:

- All data-access queries will be executed through a `QueryBuilder` base class that automatically appends `WHERE tenant_id = :tenant_id` to every query.
- PHPStan static analysis rules will flag any SQL string that contains `FROM <table>` without a corresponding `tenant_id` binding.
- Integration tests will assert that a user authenticated as Tenant A cannot retrieve records belonging to Tenant B.

## Indexing Baseline

`tenant_id` will be the first column in every compound index on operational tables. This ensures that the MySQL query planner uses the tenant partition as the primary filter before applying secondary predicates, preventing full-table scans in a multi-tenant dataset.

## Connection and Configuration

The database connection will be managed via PHP Data Objects (PDO) with prepared statements only. No raw SQL string interpolation will be permitted in application code. Connection credentials will be loaded from environment variables via `vlucas/phpdotenv` and will never be hardcoded.

Character set and collation will be enforced at the connection level with `SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci` on every new connection, in addition to the server-level default.

## Transaction Boundaries

All multi-table write operations — including General Ledger (GL) journal posting, payroll runs, stock movements, and invoice generation — will be wrapped in explicit database transactions. Any exception within the transaction boundary will trigger a full rollback, leaving no partial state in the database.
