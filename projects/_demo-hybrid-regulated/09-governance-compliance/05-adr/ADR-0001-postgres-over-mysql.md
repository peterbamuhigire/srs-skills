# ADR-0001 Postgres over MySQL

- Status: accepted
- Date: 2026-04-12

## Context

Livelink Health requires strong JSON support for clinical notes, row-level
security for multi-tenant isolation, and WAL-based physical replication for
the backup RPO target NFR-008.

## Decision

Adopt PostgreSQL 15 as the primary RDBMS. Use `pgcrypto` for field-level
encryption per CTRL-UG-002. Use streaming replication for DR with RPO
target of 15 minutes.

## Consequences

- Positive: mature RLS, strong JSONB performance, predictable WAL semantics.
- Negative: ops team needs Postgres-specific runbooks; retraining cost.
- Mitigated: runbook and monitoring already written for Postgres.

## Affects

- FR-001, FR-003, FR-013 (all write-path FRs that persist PII).
- NFR-004 (storage), NFR-005 (memory), NFR-008 (RPO).
