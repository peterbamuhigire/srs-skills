---
title: "Maduuka Platform — Low-Level Design, Section 1: Overview"
author: "Chwezi Core Systems"
date: "2026-04-05"
---

# Low-Level Design Overview

**Document ID:** MADUUKA-LLD-001
**Version:** 1.0
**Status:** Draft
**Owner:** Peter Bamuhigire, Chwezi Core Systems
**Date:** 2026-04-05

---

## 1. Purpose and Scope

This Low-Level Design (LLD) document specifies the internal structure of the Maduuka platform at the class, method, and data-flow level for Phase 1: the Web backend and the shared REST API. It bridges the High-Level Design (HLD), which defines component boundaries and responsibilities, and the implementation, where developers write production code.

The scope of this document covers:

- The PHP 8.3+ backend service layer and its method signatures
- The REST API request-handling pipeline, including authentication, authorisation, and validation
- Internal data flow for all Phase 1 modules: POS/Sales, Inventory, HR/Payroll, Reporting, and Audit
- Cross-cutting concerns: multi-tenancy enforcement, audit logging, error handling, and pagination

The Android Kotlin client, iOS Phase 2 client, and all Phase 3 add-on modules are outside the scope of this document.

---

## 2. Architecture Layers

The backend is structured as a four-layer stack. Each layer has a strict dependency direction: upper layers may call lower layers; lower layers never call upward.

```
┌─────────────────────────────────────────────────────┐
│  Presentation Layer                                 │
│  PHP Controllers / API Route Handlers               │
│  Responsibility: parse HTTP request, validate input,│
│  delegate to Service Layer, format HTTP response    │
├─────────────────────────────────────────────────────┤
│  Application (Service) Layer                        │
│  Business-logic classes: POSService, StockService,  │
│  PayrollService, ReportService, AuditLogService     │
│  Responsibility: orchestrate domain operations,     │
│  enforce business rules, coordinate repositories   │
├─────────────────────────────────────────────────────┤
│  Domain Layer                                       │
│  Value objects, domain entities, business-rule      │
│  validators (e.g., CreditLimitChecker, FEFOSelector)│
│  Responsibility: pure logic with no I/O or DB calls │
├─────────────────────────────────────────────────────┤
│  Infrastructure Layer                               │
│  Repository classes (MySQL via PDO/Eloquent),       │
│  external API clients (MTN MoMo, Africa's Talking,  │
│  Wasabi S3), file system, SMTP adapter              │
│  Responsibility: all I/O and external integration   │
└─────────────────────────────────────────────────────┘
```

---

## 3. Design Patterns

### 3.1 Repository Pattern

Every database entity group has a corresponding repository class that encapsulates all SQL for that group. Service-layer classes call repository methods; they never construct raw SQL queries directly. This decouples business logic from the database engine and simplifies unit testing via repository mocking.

Example repository contract:

```php
interface SaleRepositoryInterface
{
    public function findById(int $saleId, int $franchiseId): ?Sale;
    public function create(SaleData $data): Sale;
    public function updateStatus(int $saleId, string $status, int $franchiseId): void;
    public function findBySession(int $sessionId, int $franchiseId): Collection;
}
```

Every repository method that fetches or mutates tenant-scoped data accepts `int $franchiseId` as a mandatory parameter and includes `WHERE franchise_id = :franchiseId` in every query it executes (BR-001).

### 3.2 Service Layer

Business logic resides exclusively in service classes. Controllers receive an HTTP request, extract validated parameters, and hand control to the relevant service. Controllers contain no conditional business logic.

### 3.3 RBAC Middleware

A `RBACMiddleware` class executes on every protected endpoint before the controller runs. It:

1. Extracts and validates the JWT (or web session).
2. Resolves the authenticated user's role from the `user_roles` table.
3. Checks whether the role holds the required permission for the endpoint being accessed.
4. Passes the request to the controller if authorised; returns HTTP `403` immediately if not.

The middleware injects a `AuthContext` value object — containing `userId`, `franchiseId`, `role`, and `branchId` — into the request context. Every downstream service reads tenant identity exclusively from `AuthContext`, never from request parameters.

### 3.4 Observer Pattern — Audit Logging

`AuditLogService::write()` is invoked via an event/observer mechanism. When a service method mutates data, it fires a domain event (e.g., `SaleCreated`, `StockAdjusted`). A registered listener catches the event and calls `AuditLogService::write()` with the before/after state. This decouples audit concerns from business logic and ensures no mutation path can bypass the audit trail (BR-003).

### 3.5 Strategy Pattern — Payment Methods

`POSService::processSale()` delegates payment processing to a payment-method strategy selected at runtime. The `PaymentStrategyInterface` defines a single `process(PaymentRequest $request): PaymentResult` method. Concrete implementations:

- `CashPaymentStrategy` — records cash against the session's cash account
- `MTNMoMoStrategy` — calls the MTN MoMo Business API
- `AirtelMoneyStrategy` — calls the Airtel Money API
- `CreditPaymentStrategy` — increments the customer's `outstanding_balance` after credit-limit validation

Adding a new payment method in a future phase requires only a new strategy class; `POSService` is unchanged.

### 3.6 Template Method Pattern — Report Generation

`ReportService::generate()` defines the report-generation skeleton: build query, execute, format result, optionally export. Each concrete report type overrides `buildQuery()` and `formatResult()`. The base class handles pagination, caching headers, and export dispatch. This eliminates duplicated plumbing code across the 10+ report types in Phase 1.

---

## 4. Cross-Cutting Concerns

### 4.1 Multi-Tenancy Enforcement

Every service method receives an `AuthContext` object (injected by the RBAC middleware). The `franchiseId` from `AuthContext` is passed as a parameter to every repository call. No service method accepts a `franchise_id` from the HTTP request payload; the client cannot override tenant identity.

The `BaseRepository` abstract class enforces this by implementing a `scopeToTenant(QueryBuilder $query, int $franchiseId): QueryBuilder` method that appends `WHERE franchise_id = ?` to every query. Child repositories that override query-building methods are required to call `scopeToTenant()` before executing the query.

### 4.2 Audit Logging

Every service method that creates, updates, voids, or deletes a record fires a domain event. `AuditLogService::write()` captures: `franchise_id`, `actor_id`, `actor_role`, `action`, `entity_type`, `entity_id`, `old_value`, `new_value`, `ip_address`, `user_agent`, and `timestamp`. The `audit_log` table is append-only; the application database user holds no `UPDATE` or `DELETE` privilege on it.

### 4.3 Error Handling

All exceptions propagate to a global exception handler that maps them to standardised HTTP responses:

| Exception Class | HTTP Status | Error Code |
|---|---|---|
| `ValidationException` | 422 | `VALIDATION_ERROR` |
| `AuthorisationException` | 403 | `FORBIDDEN` |
| `ResourceNotFoundException` | 404 | `NOT_FOUND` |
| `BusinessRuleViolationException` | 409 | `RULE_VIOLATION` |
| `ExternalServiceException` | 502 | `UPSTREAM_ERROR` |
| `Throwable` (uncaught) | 500 | `INTERNAL_ERROR` |

All `500` responses log the full stack trace to the server error log and suppress the trace from the API response body (information leakage prevention).

### 4.4 Pagination

All collection endpoints return paginated responses. The default page size is 25 records; the maximum is 100. The response envelope for paginated collections:

```json
{
  "data": [ ... ],
  "meta": {
    "current_page": 1,
    "per_page": 25,
    "total": 340,
    "last_page": 14
  },
  "links": {
    "first": "https://api.maduuka.app/v1/...",
    "prev": null,
    "next": "https://api.maduuka.app/v1/...",
    "last": "https://api.maduuka.app/v1/..."
  }
}
```

The `page` and `per_page` query parameters are accepted on all collection endpoints. Repository methods accept `int $page` and `int $perPage` and apply `LIMIT` and `OFFSET` at the database level.
