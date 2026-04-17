## 3. Immutability Requirements

### 3.1 Database-Level INSERT-Only Enforcement

**FR-AUDIT-030:** The system shall prevent any UPDATE or DELETE operation on the `audit_log` table by any database user, including the application database user and super administrators.

*Test oracle: Connect to the database as the application database user. Execute `UPDATE audit_log SET action = 'DELETE' WHERE id = 1`. Verify the database returns a permission denied error. Execute `DELETE FROM audit_log WHERE id = 1`. Verify the database returns a permission denied error.*

**FR-AUDIT-031:** The system shall implement the `audit_log` table with `GRANT INSERT` privilege only for the application database user. `UPDATE` and `DELETE` privileges on `audit_log` shall not be granted to any application database user or role.

*Test oracle: Query the database privilege catalogue (e.g., `information_schema.role_table_grants` in PostgreSQL) and confirm that the application database user holds `INSERT` on `audit_log` only. Confirm no `UPDATE` or `DELETE` privilege entries exist for `audit_log` for any non-DBA role.*

**FR-AUDIT-032:** The system shall define a database-level trigger on `audit_log` that raises an exception and aborts any UPDATE or DELETE statement regardless of the executing database role, providing a second layer of immutability enforcement beyond privilege restriction.

*Test oracle: Connect as a database superuser. Attempt `UPDATE audit_log SET action = 'CREATE' WHERE id = 1`. Verify the trigger fires and the statement is aborted. Attempt `DELETE FROM audit_log WHERE id = 1`. Verify the trigger fires and the statement is aborted.*

### 3.2 Hash-Based Tamper Detection

**FR-AUDIT-033:** The system shall compute a SHA-256 hash of each audit log record at insert time and store the hash in a dedicated `record_hash` column. The hash input shall be the canonical JSON serialisation of the record's `tenant_id`, `user_id`, `module`, `action`, `affected_table`, `affected_record_id`, `old_values`, `new_values`, `ip_address`, `user_agent`, and `timestamp` fields, concatenated in that fixed order, with no whitespace normalisation.

*Test oracle: Insert a test audit record. Independently compute `SHA-256(canonical_json_of_fields)` using the defined field order. Retrieve `record_hash` from the database. Verify both hashes are identical.*

**FR-AUDIT-034:** The system shall provide a tamper verification report accessible to super admins that re-computes the SHA-256 hash for every record in the `audit_log` table (or a user-specified date range) and identifies any record whose stored `record_hash` does not match the re-computed hash.

*Test oracle: Manually update one record's `action` column using a direct DBA connection (bypassing the trigger for test purposes only). Run the tamper verification report. Confirm the report flags exactly that record as tampered and displays its `id`, `timestamp`, and the hash mismatch.*

**FR-AUDIT-035:** The tamper verification report shall display the following for each flagged record: record `id`, `timestamp`, `tenant_id`, `user_id`, `module`, `action`, stored `record_hash`, re-computed hash, and a `TAMPER_DETECTED` status label.

*Test oracle: Introduce a deliberate hash mismatch. Run the report. Verify all 9 fields are present in the output for the flagged record.*

**FR-AUDIT-036:** The system shall log the execution of every tamper verification report as an audit record with `action = "AUDIT_VERIFY"`, `affected_table = "audit_log"`, and `new_values` containing `{"records_checked": <count>, "tampered_records": <count>, "date_range_start": "<ISO8601>", "date_range_end": "<ISO8601>"}`.

*Test oracle: Run the tamper verification report. Verify a new audit record exists with `action = "AUDIT_VERIFY"` and `new_values.records_checked` equal to the record count in the specified date range.*

### 3.3 Application-Layer Write Control

**FR-AUDIT-037:** The application shall write to `audit_log` exclusively via a dedicated `AuditLogService` class. No other application component shall execute direct SQL INSERT statements against `audit_log`.

*Test oracle: Static analysis and code review shall confirm that no SQL INSERT targeting `audit_log` exists outside the `AuditLogService` class. Any violation is a Critical severity defect.*

**FR-AUDIT-038:** The `AuditLogService` shall not expose any public method for UPDATE or DELETE operations. The public interface shall include `record()` (for inserting a new log entry) and `verify()` (for triggering the tamper verification report) only.

*Test oracle: Review the `AuditLogService` class public method list. Confirm no `update`, `delete`, `purge`, `truncate`, or equivalent method is defined.*

**FR-AUDIT-039:** The system shall use a separate, dedicated database connection pool for audit log writes that is distinct from the main application connection pool, ensuring that audit writes are not blocked by application transaction rollbacks.

*Test oracle: Initiate an application transaction that creates a record and then rolls back. Verify that the corresponding audit record (for the CREATE action) is still present in `audit_log` despite the application transaction rollback.*

**FR-AUDIT-040:** The system shall enqueue the audit log write to a persistent, durable queue (e.g., a database-backed queue or message broker with at-least-once delivery) when the audit log database connection is temporarily unavailable, and shall process the queued record upon connection restoration without data loss.

*Test oracle: Simulate an audit log database connection failure. Perform a state-changing operation. Restore the connection. Verify the audit record is present in `audit_log` with the correct `timestamp` reflecting the time of the original operation.*
