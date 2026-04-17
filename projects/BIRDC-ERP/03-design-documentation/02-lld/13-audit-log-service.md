# 13. AuditLogService

**Namespace:** `App\Services\Audit\AuditLogService`
**Dependencies:** `AuditLogRepository`
**Test coverage required:** 100% (security-critical)

## 13.1 Method Signatures

```php
final class AuditLogService
{
    /**
     * Append an immutable audit log entry.
     *
     * This method is called by database triggers (trg_audit_insert, trg_audit_update)
     * and directly by service classes for application-layer events (login, logout,
     * permission denial, EFRIS failure, hash chain violation).
     *
     * @param int|null $userId      Authenticated user ID (null for system-generated events).
     * @param string   $action      Action identifier: 'INSERT' | 'UPDATE' | 'DELETE' |
     *                              'LOGIN' | 'LOGOUT' | 'PERMISSION_DENIED' | 'EFRIS_FAILURE' |
     *                              'HASH_CHAIN_VIOLATION' | 'PAYROLL_LOCK' | 'REMITTANCE_VERIFY'
     * @param string   $tableName   Database table affected (or logical entity for app events).
     * @param int|null $recordId    Primary key of the affected record (null for app events).
     * @param array    $oldValues   Full row snapshot before change (empty array for INSERT).
     * @param array    $newValues   Full row snapshot after change (empty array for DELETE).
     *
     * @return void
     *
     * @throws AuditLogWriteException  If the write to tbl_audit_log fails.
     *                                 This exception must NOT be swallowed — audit log
     *                                 failure is treated as a critical system error.
     *
     * Business rules:
     *   - Append-only: the application DB user (`birdc_app`) has INSERT privilege on
     *     tbl_audit_log but NO UPDATE or DELETE privilege (enforced at the DB level).
     *   - IP address is captured from the current HTTP request context (or '127.0.0.1'
     *     for background jobs / system events).
     *   - `old_values` and `new_values` are stored as JSON.
     *   - Sensitive fields (NIN, mobile money numbers, passwords) are masked before
     *     storage: tbl_audit_log stores "[REDACTED]" for these column values.
     *   - Retention: 7 years minimum (DC-003). Audit log table is partitioned by year
     *     in MySQL for performance on large data sets.
     */
    public function append(
        ?int $userId,
        string $action,
        string $tableName,
        ?int $recordId,
        array $oldValues,
        array $newValues
    ): void;

    /**
     * Query the audit log with filters.
     *
     * @param array $filters {
     *   user_id: int|null,
     *   action: string|null,
     *   table_name: string|null,
     *   record_id: int|null,
     *   date_from: DateString|null,
     *   date_to: DateString|null,
     *   ip_address: string|null,
     *   page: int,              // 1-indexed, default 1
     *   per_page: int,          // default 50, max 200
     * }
     *
     * @return AuditEntry[]  Paginated array of audit log entries, newest first.
     *
     * @throws PermissionException  If the caller does not hold IT_ADMINISTRATOR or
     *                              FINANCE_DIRECTOR or DIRECTOR role.
     *
     * Business rules:
     *   - Read-only query; no write operations.
     *   - Results are paginated to prevent memory exhaustion on large audit logs.
     *   - Sensitive masked fields remain masked in query results.
     */
    public function query(array $filters): array;
}
```

## 13.2 Audit Log Retention and Archival

- Active audit records (≤ 2 years old) remain in `tbl_audit_log` in the live MySQL instance.
- Records older than 2 years are archived monthly to `tbl_audit_log_archive_{year}` (yearly partitioned table on the same server).
- The full 7-year retention window spans both the live table and the archive tables.
- The IT Administrator receives a quarterly retention report via email confirming archive integrity.
- Physical deletion from archive tables is blocked at the DB level for the 7-year window.
