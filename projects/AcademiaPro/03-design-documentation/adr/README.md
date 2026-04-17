# Architecture Decision Records — pointer

This directory is a pointer to the canonical ADR catalog. All Academia Pro ADRs are stored in `09-governance-compliance/05-adr/` and indexed in `_registry/adr-catalog.yaml`.

## Current ADR set (v1.0)

- `ADR-0001` Laravel 11 over Node/NestJS for backend
- `ADR-0002` MySQL 8 over PostgreSQL 15
- `ADR-0003` Multi-tenancy via `tenant_id` + Eloquent `TenantScope`
- `ADR-0004` Global identity architecture for cross-school student portability
- `ADR-0005` Mandatory PII scrubbing before every AI prompt

ADR-0001 and ADR-0002 inform the database design (`04-database-design/01-erd.md`). ADR-0003 informs the HLD (`01-hld/02-security-architecture.md §Tenant Isolation`). ADR-0004 informs the global-identity schema. ADR-0005 informs the AI security section.
