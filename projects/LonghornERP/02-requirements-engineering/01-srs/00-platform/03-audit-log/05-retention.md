## 5. Retention Requirements

### 5.1 Retention Period Configuration

**FR-AUDIT-070:** The system shall enforce a minimum audit log retention period of 7 years from the timestamp of each record. A tenant administrator shall be able to increase the retention period beyond 7 years. The retention period shall not be configurable below 7 years.

*Test oracle: Attempt to set the retention period to 4 years via the tenant configuration interface. Verify the system rejects the value and displays an error message stating the minimum retention period is 7 years. Set the retention period to 10 years. Verify the setting is accepted and persisted.*

**FR-AUDIT-071:** The system shall display the currently configured retention period to the tenant administrator in the audit log settings interface, expressed in years and as a calculated expiry date based on the current date.

*Test oracle: Set the retention period to 7 years. Open the audit log settings interface. Verify the display shows "7 years" and a calculated expiry date equal to the current date plus 7 years.*

### 5.2 Automatic Archival

**FR-AUDIT-072:** The system shall automatically archive audit log records whose `timestamp` exceeds the configured retention threshold to an `audit_log_archive` table on a scheduled basis not less frequent than once every 24 hours.

*Test oracle: Set the retention period to a test minimum (7 years). Introduce records with `timestamp` values older than the threshold. Run the archival job manually. Verify the records appear in `audit_log_archive` and are no longer present in `audit_log`.*

**FR-AUDIT-073:** The `audit_log_archive` table shall enforce the same immutability constraints as the `audit_log` table: INSERT-only privilege for the application database user, a database-level trigger preventing UPDATE and DELETE operations, and SHA-256 `record_hash` verification.

*Test oracle: Attempt `UPDATE audit_log_archive SET action = 'CREATE' WHERE id = 1` as the application database user. Verify permission denied. Attempt the same as a database superuser. Verify the database trigger aborts the statement.*

**FR-AUDIT-074:** The system shall include archived records from `audit_log_archive` in audit log search results when the user's specified date range overlaps with the archive period, returning a unified result set that spans both `audit_log` and `audit_log_archive` transparently.

*Test oracle: Configure a date range filter that includes both current and archived records. Submit the search. Verify results include records from both `audit_log` and `audit_log_archive`, rendered identically. Verify the source table is not exposed to the user in the results.*

### 5.3 Record Deletion Beyond Retention Period

**FR-AUDIT-075:** The system shall allow a super admin to permanently delete audit log records that have exceeded the configured retention period, subject to an explicit, two-step confirmation workflow that requires the super admin to type the phrase `CONFIRM DELETE AUDIT LOG` before the deletion is executed.

*Test oracle: Log in as super admin. Navigate to the audit log retention management interface. Select a batch of records whose retention period has expired. Initiate the deletion workflow. Verify the system presents a confirmation dialog. Submit the request without typing the confirmation phrase. Verify the deletion is blocked. Type `CONFIRM DELETE AUDIT LOG` exactly and submit. Verify the records are deleted from both `audit_log` and `audit_log_archive`.*

**FR-AUDIT-076:** The system shall create an audit record for every permanent audit log deletion event, with `action = "AUDIT_PURGE"`, `affected_table = "audit_log_archive"`, `user_id` = the super admin's user ID, and `new_values` containing `{"records_deleted": <count>, "oldest_record_timestamp": "<ISO8601>", "newest_record_timestamp": "<ISO8601>", "confirmed_by": "<super_admin_user_name>"}`.

*Test oracle: Execute a retention deletion. Verify a new audit record exists in `audit_log` with `action = "AUDIT_PURGE"` and all 4 `new_values` sub-fields populated with accurate values.*

**FR-AUDIT-077:** The system shall prohibit the deletion of any audit log record (from either `audit_log` or `audit_log_archive`) that has not yet exceeded the configured retention period, regardless of the requesting user's role.

*Test oracle: Log in as super admin. Attempt to initiate a deletion batch that includes a record whose retention period has not elapsed. Verify the system rejects the batch and identifies which records are ineligible by their `id` and `timestamp`.*
