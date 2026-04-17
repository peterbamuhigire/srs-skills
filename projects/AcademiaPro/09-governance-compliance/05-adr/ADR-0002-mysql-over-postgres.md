# ADR-0002 MySQL 8 over PostgreSQL 15

- Status: accepted
- Date: 2026-04-17

## Context

Ugandan shared-hosting providers overwhelmingly offer MySQL, not PostgreSQL. Tier-2 schools running on cPanel hosting cannot be migrated to a Postgres-capable VPS within Phase 1 budget. The data model is heavily relational with limited JSON requirements.

## Decision

Adopt MySQL 8.0 (InnoDB) as the primary RDBMS. Use utf8mb4 everywhere. Use InnoDB row-level locking. Use transactions for all multi-row financial operations. Use Percona XtraBackup for physical backups.

## Consequences

- Positive: every Ugandan shared-hosting provider supports MySQL 8; cPanel tooling is mature; the team has 10+ years MySQL operational experience.
- Negative: weaker JSONB than Postgres (acceptable given limited JSON usage); no row-level security, replaced by application-level TenantScope per ADR-0003.
- Mitigated: JSON columns used only for audit-log payloads and AI prompt snapshots, both append-only.

## Affects

- FR-ENR-*, FR-FEE-*, FR-EXM-* (all core CRUD).
- NFR-SEC-002 (tenant isolation relies on app-layer scope not DB RLS).
- `03-design-documentation/04-database-design/01-erd.md` (schema is MySQL 8 dialect).
