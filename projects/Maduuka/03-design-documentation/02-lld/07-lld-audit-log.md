---
title: "Maduuka Platform — Low-Level Design, Section 7: Audit Log"
author: "Chwezi Core Systems"
date: "2026-04-05"
---

# Audit Log Design

**Document ID:** MADUUKA-LLD-007
**Version:** 1.0
**Status:** Draft
**Owner:** Peter Bamuhigire, Chwezi Core Systems
**Date:** 2026-04-05

---

## 1. Design Principles

The audit log is the authoritative record of every mutation that occurs within the system (BR-003). Three constraints govern its design:

1. **Append-only:** the application database user holds `INSERT` privilege on `audit_log`. No `UPDATE` or `DELETE` privilege is granted at the database level. These privileges are withheld even from the database user that the application's ORM or repository layer connects with.
2. **Completeness:** every service method that creates, updates, voids, transfers, approves, or deletes a record fires an `AuditEntry` before returning. Methods that only read data do not write to the audit log.
3. **Immutability after write:** once a row is inserted into `audit_log`, it is never modified. Corrections to business data require a counter-entry in the source table, not an edit to the audit record.

---

## 2. AuditLogService

```php
class AuditLogService
{
    /**
     * Writes a single audit entry. Called from domain event listeners;
     * never called directly from controllers.
     */
    public function write(AuditEntry $entry): void;

    /**
     * Retrieves a paginated list of audit entries scoped to a tenant.
     * Access restricted to Business Owner and Platform Admin.
     */
    public function query(AuditQuery $query): PaginatedResult;
}
```

### 2.1 AuditEntry Value Object

```php
class AuditEntry
{
    public function __construct(
        public readonly int     $franchiseId,
        public readonly int     $actorId,          // users.id of the authenticated user
        public readonly string  $actorRole,        // role name at time of action
        public readonly string  $action,           // see Section 4 for action codes
        public readonly string  $entityType,       // table name: 'sales', 'stock_movements', etc.
        public readonly ?int    $entityId,         // primary key of the affected row
        public readonly ?array  $oldValue,         // JSON-serialisable before-state; null for CREATE
        public readonly ?array  $newValue,         // JSON-serialisable after-state; null for DELETE
        public readonly string  $ipAddress,        // client IPv4 or IPv6
        public readonly string  $userAgent,        // HTTP User-Agent header value
        public readonly string  $timestamp,        // UTC ISO 8601
    ) {}
}
```

### 2.2 write() Behaviour

1. Validate that `$franchiseId`, `$actorId`, `$action`, and `$entityType` are non-empty.
2. JSON-encode `$oldValue` and `$newValue` (null-safe).
3. Execute a single `INSERT INTO audit_log (...) VALUES (...)` with no transaction wrap (audit writes must not be rolled back with the parent business transaction; they are committed independently).
4. On INSERT failure (e.g., database connection loss), log the failure to the server error log with severity `CRITICAL` and the full `AuditEntry` payload. Do not throw an exception that would surface to the API consumer; the parent business operation has already succeeded.

**Independent commit note:** `AuditLogService::write()` opens its own database connection (or uses a secondary connection pool) distinct from the primary transactional connection. This ensures the audit entry is committed even if the business transaction is rolled back due to a later error — and conversely, that a failed audit write does not roll back a completed sale.

---

## 3. Observer Pattern Integration

Every domain event that represents a mutation fires `AuditLogService::write()` through a registered event listener. The event system decouples audit concerns from service logic.

```
Service method
    ↓  fires domain event (e.g., SaleCreated)
Event Dispatcher
    ↓  notifies registered listeners
AuditLogListener::handle(SaleCreated $event)
    ↓  constructs AuditEntry from event payload
AuditLogService::write(AuditEntry $entry)
    ↓  INSERT into audit_log
```

The listener is registered in the application's event service provider. The mapping of domain events to action codes:

| Domain Event | Action Code |
|---|---|
| `UserLoggedIn` | `LOGIN` |
| `UserLoggedOut` | `LOGOUT` |
| `SaleCreated` | `sale.created` |
| `SaleVoided` | `sale.voided` |
| `SessionOpened` | `session.opened` |
| `SessionClosed` | `session.closed` |
| `StockMovementRecorded` | `stock.movement.{movementType}` |
| `StockCountInitiated` | `stock.count.initiated` |
| `StockCountSubmitted` | `stock.count.submitted` |
| `StockAdjustmentApproved` | `stock.adjustment.approved` |
| `PayrollComputed` | `payroll.computed` |
| `PayrollApproved` | `payroll.approved` |
| `CustomerUpdated` | `customer.updated` |
| `CreditOverrideUsed` | `credit.override.used` |
| `UserCreated` | `user.created` |
| `UserDeactivated` | `user.deactivated` |
| `RoleAssigned` | `role.assigned` |
| `SettingsUpdated` | `settings.updated` |
| `PayslipSent` | `payslip.sent` |
| `ScheduledReportDispatched` | `report.scheduled.dispatched` |

---

## 4. audit_log Table Schema (Reference)

```sql
CREATE TABLE audit_log (
    id            BIGINT UNSIGNED     NOT NULL AUTO_INCREMENT,
    franchise_id  BIGINT UNSIGNED     NOT NULL,
    user_id       BIGINT UNSIGNED     NOT NULL,
    action        VARCHAR(100)        NOT NULL,
    entity_type   VARCHAR(100)        NOT NULL,
    entity_id     BIGINT UNSIGNED     NULL,
    old_values    JSON                NULL,
    new_values    JSON                NULL,
    ip_address    VARCHAR(45)         NOT NULL,
    device_id     VARCHAR(255)        NULL,
    created_at    TIMESTAMP           NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    INDEX idx_audit_franchise_date (franchise_id, created_at),
    INDEX idx_audit_entity (entity_type, entity_id),
    INDEX idx_audit_user (user_id, created_at)
) ENGINE=InnoDB;
```

The `user_agent` string is captured at the HTTP layer and passed into the `AuditEntry`; it is stored in `new_values` as `{ "user_agent": "..." }` rather than as a top-level column, to keep the schema lean. If forensic analysis requires user-agent filtering, the JSON path `new_values->>'$.user_agent'` is queryable in MySQL 8.x.

**Database privilege enforcement:**

```sql
-- Applied to the application database user (e.g., 'maduuka_app'@'localhost')
REVOKE UPDATE, DELETE ON maduuka.audit_log FROM 'maduuka_app'@'localhost';
GRANT INSERT, SELECT ON maduuka.audit_log TO 'maduuka_app'@'localhost';
```

A separate read-only database user (`maduuka_readonly`) holds only `SELECT` on `audit_log` and is used by the reporting layer for audit trail queries. It holds no `INSERT` privilege.

---

## 5. AuditQuery

```php
class AuditQuery
{
    public function __construct(
        public readonly int     $franchiseId,
        public readonly ?int    $actorId    = null,
        public readonly ?string $action     = null,     // partial match: LIKE '%:action%'
        public readonly ?string $entityType = null,
        public readonly ?int    $entityId   = null,
        public readonly ?string $dateFrom   = null,     // ISO 8601
        public readonly ?string $dateTo     = null,
        public readonly int     $page       = 1,
        public readonly int     $perPage    = 50,
    ) {}
}
```

All parameters are optional filters. `franchiseId` is mandatory and is never accepted from the HTTP request; it is injected from `AuthContext`. Queries against `audit_log` use the `idx_audit_franchise_date` index as the primary access path, with additional filter predicates applied on top.

The maximum `perPage` for audit queries is 50 (not 100 as for other collections), because `old_values` and `new_values` JSON columns can be large and returning 100 rows at once risks slow responses under load.
