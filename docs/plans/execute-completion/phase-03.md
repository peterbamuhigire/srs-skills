# Phase 3: Architecture, Design & Data Modeling

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Complete the architecture layer by adding event-driven architecture and GraphQL
patterns — the two remaining gaps in system design coverage. Everything else in this domain
is already expert-grade.

**Architecture:** Two new skills extend an already strong foundation of 20+ architecture,
database, and API design skills. The additions close the event-driven and GraphQL gaps
that modern SaaS platforms require.

**Skills library path:** `C:\Users\Peter\.claude\skills\`

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Design any system architecture from monolith to distributed microservices
- Model relational data for transactional systems using MySQL (expert) or PostgreSQL
- Design vector database schemas for AI-powered features (pgvector, Pinecone, Qdrant)
- Build event-driven systems using domain events, event sourcing, and CQRS
- Design GraphQL APIs with federation for multi-team SaaS platforms
- Choose the right persistence pattern: SQL, NoSQL, vector, or polyglot
- Produce architecture decision records (ADRs) for every major design choice
- Design for SaaS-specific patterns: multi-tenancy, soft delete, audit trails

---

## Current Strengths — Skills Already Built

### System Architecture
- `system-architecture-design` — Monolith, modular monolith, microservices selection framework
- `modular-saas-architecture` — Modular SaaS: feature modules, plug-in design, tenant isolation
- `multi-tenant-saas-architecture` — Multi-tenancy strategies: shared schema, separate schema, separate DB
- `distributed-systems-patterns` — CAP theorem, consistency, partitioning, two-phase commit
- `realtime-systems` — WebSocket, SSE, CRDT, real-time sync patterns
- `saas-erp-system-design` — ERP module design for multi-vertical SaaS

### Database Layer — MySQL (Expert)
- `mysql-data-modeling` — ERD design, normalisation (1NF–3NF/BCNF), schema patterns for SaaS
- `mysql-advanced-sql` — CTEs, window functions, stored procedures, triggers, full-text search
- `mysql-best-practices` — Index design, query optimisation, connection pooling, locking
- `mysql-query-performance` — EXPLAIN analysis, slow query log, covering indexes, partitioning
- `mysql-administration` — Replication, backup/restore, InnoDB tuning, security hardening

### Database Layer — PostgreSQL + Vector (Expert)
- `postgresql-fundamentals` — PostgreSQL syntax, types, constraints, transactions vs MySQL
- `postgresql-advanced-sql` — JSONB, window functions, full-text search (tsvector/tsquery)
- `postgresql-performance` — EXPLAIN ANALYZE, partial indexes, parallel query, VACUUM
- `postgresql-administration` — PgBouncer, WAL, replication, streaming standby
- `postgresql-server-programming` — PL/pgSQL, triggers, row-level security
- `postgresql-ai-platform` — pgvector: embedding storage, HNSW indexes, RAG retrieval pipeline

### API & Communication Design
- `api-design-first` — OpenAPI 3.1, schema-first design, versioning, hypermedia
- `api-error-handling` — RFC 7807 Problem Details, error taxonomy, retry patterns
- `api-pagination` — Cursor, offset, keyset pagination patterns for large datasets
- `api-testing-verification` — Contract testing, API test strategy, Postman/Newman
- `graphql-security` — GraphQL injection prevention, query depth limiting, batching attacks

### Microservices Architecture
- `microservices-fundamentals` — Service decomposition, bounded contexts, DDD
- `microservices-architecture-models` — CQRS, saga, API gateway, BFF patterns
- `microservices-communication` — gRPC, message brokers, async patterns, choreography vs orchestration
- `microservices-resilience` — Circuit breaker, bulkhead, timeout, retry, fallback
- `microservices-ai-integration` — AI service mesh, model router, LLM integration in microservices

### Supplementary
- `database-design-engineering` — Database design principles, normalisation, physical design
- `gis-mapping` — PostGIS, Leaflet.js, spatial queries for location-aware SaaS
- `data-visualization` — Chart patterns, dashboard data modeling, aggregation strategies

---

## Build Tasks

### Task 1: Create `event-driven-architecture` skill

**File to create:** `C:\Users\Peter\.claude\skills\event-driven-architecture\SKILL.md`

**Read first:** *Building Event-Driven Microservices* (Bellemare) + *Designing Data-Intensive
Applications* Ch. 11 (Kleppmann)

**Content outline for SKILL.md (target: 380–450 lines):**

1. **What Is Event-Driven Architecture** — events vs commands vs queries, why EDA
2. **Domain Events** — naming conventions (past tense), event schema design, versioning
3. **Event Sourcing** — event store, append-only log, event replay, snapshot patterns
4. **CQRS** — command model vs read model, projection design, eventual consistency trade-offs
5. **Message Brokers** — RabbitMQ vs SQS vs Kafka: when to use which, connection patterns
6. **Saga Pattern** — choreography saga vs orchestration saga, compensation transactions
7. **Outbox Pattern** — guarantee event delivery without two-phase commit
8. **Event Schema Registry** — Avro/Protobuf vs JSON schema, schema evolution rules
9. **Idempotency** — exactly-once semantics, deduplication keys, consumer groups
10. **Dead Letter Queues** — poison message handling, DLQ monitoring and reprocessing
11. **EDA for SaaS** — multi-tenant event routing, tenant isolation in shared brokers
12. **Testing Event-Driven Systems** — in-process event bus for tests, integration test patterns
13. **Anti-patterns** — event spaghetti, missing domain boundaries, over-eventification

**Step 1:** Read the source materials listed above.
**Step 2:** Create `SKILL.md` following the content outline.
**Step 3:** Verify: every section has at least one concrete code example or schema snippet.
**Step 4:** Run `wc -l SKILL.md` and confirm line count is between 300 and 500.
**Step 5:** Commit: `feat(skills): add event-driven-architecture skill`

---

### Task 2: Create `graphql-patterns` skill

**File to create:** `C:\Users\Peter\.claude\skills\graphql-patterns\SKILL.md`

**Read first:** *Learning GraphQL* (Porcello & Banks) + Apollo Server documentation

**Content outline for SKILL.md (target: 350–420 lines):**

1. **GraphQL vs REST** — when GraphQL wins, when REST is better, hybrid strategies
2. **Schema-First Design** — SDL types, queries, mutations, subscriptions, interfaces, unions
3. **Apollo Server Setup** — Node.js server, schema stitching, context object
4. **Resolvers** — resolver chain, context passing, resolver composition patterns
5. **N+1 Problem** — DataLoader pattern, batch loading, request deduplication
6. **Authentication & Authorisation** — JWT in context, field-level permissions, directives
7. **Pagination** — Relay cursor connection spec, offset pagination in GraphQL
8. **Error Handling** — error extensions, error codes, partial success responses
9. **GraphQL Federation** — Apollo Federation 2, subgraph schemas, gateway routing
10. **Subscriptions** — WebSocket transport, subscription filters, connection lifecycle
11. **File Uploads** — multipart request spec, storage integration
12. **Persisted Queries** — automatic persisted queries (APQ), query whitelisting
13. **Testing** — Apollo Testing utilities, mocking schema, integration test patterns
14. **Code Generation** — GraphQL Code Generator for TypeScript types

**Step 1:** Read the source materials listed above.
**Step 2:** Create `SKILL.md` following the content outline.
**Step 3:** Verify: every section has schema snippet or TypeScript code example.
**Step 4:** Run `wc -l SKILL.md` and confirm line count is between 300 and 500.
**Step 5:** Commit: `feat(skills): add graphql-patterns skill`

---

## Phase Completion Checklist

- [ ] `event-driven-architecture` SKILL.md created — 300–500 lines
- [ ] `graphql-patterns` SKILL.md created — 300–500 lines
- [ ] Both skills reference the books and materials used to build them
- [ ] No skill file exceeds 500 lines (doc-standards.md hard limit)
- [ ] Cross-references added: `microservices-communication` references `event-driven-architecture`
- [ ] Cross-references added: `api-design-first` references `graphql-patterns`
- [ ] Git commit made: `feat(skills): complete phase-3 — architecture & data modeling`

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *Designing Data-Intensive Applications* | Martin Kleppmann | O'Reilly | ~$60 | The most important backend architecture book written. Covers replication, partitioning, transactions, stream processing. Essential for every phase. |
| 2 | *Building Event-Driven Microservices* | Adam Bellemare | O'Reilly | ~$55 | The definitive book for `event-driven-architecture` skill. Event sourcing, CQRS, saga patterns, message broker selection. |
| 3 | *Building Microservices* (2nd ed.) | Sam Newman | O'Reilly | ~$60 | Deepens existing microservices skills — service decomposition, DDD, communication patterns. |
| 4 | *Clean Architecture* | Robert C. Martin | Prentice Hall | ~$35 | Architectural principles — dependency rule, boundaries, use case design. Foundational for all skills. |
| 5 | *Learning GraphQL* | Eve Porcello & Alex Banks | O'Reilly | ~$50 | The `graphql-patterns` skill source book — schema design, Apollo Server, federation. |

### Free Resources

- Apollo Federation documentation — `apollographql.com/docs/federation` — GraphQL federation spec
- Apollo Server documentation — `apollographql.com/docs/apollo-server` — Node.js GraphQL server
- GraphQL specification — `spec.graphql.org` — the authoritative language spec
- DataLoader documentation — `github.com/graphql/dataloader` — N+1 problem solution
- RabbitMQ tutorials — `rabbitmq.com/tutorials` — message broker fundamentals
- Martin Fowler's bliki — `martinfowler.com` — CQRS, event sourcing, saga patterns explained

---

*Next phase: [Phase 4 — Web Application Stack](phase-04.md)*
