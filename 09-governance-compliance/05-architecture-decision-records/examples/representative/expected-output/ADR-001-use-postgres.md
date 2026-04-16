# ADR-001 Use PostgreSQL

- **Status:** Accepted on 2026-04-16.
- **Deciders:** Architecture Review Board.

## Context

The Hospital Admission System needs a relational store with HIPAA-
compliant encryption at rest, row-level security, and a licence cost
below USD 5,000 per year.

## Decision

Adopt PostgreSQL 16 with `pgcrypto` for column-level encryption and
native row-level security policies scoped to ward.

## Consequences

- Positive: zero licence cost; native RLS removes application-layer
  access logic; team already fluent in SQL.
- Negative: on-prem operators must own patch cadence; Windows tooling
  compatibility is thinner than for MSSQL.

## Alternatives rejected

- MySQL: weaker row-level security primitives.
- Microsoft SQL Server: exceeds licence budget.
