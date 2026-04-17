## 2. Audit Capture Requirements

### 2.1 Universal Event Capture

**FR-AUDIT-001:** The system shall create an audit log record when any user creates, updates, deletes, or approves any record in any module.

*Test oracle: Perform a CREATE, UPDATE, DELETE, and APPROVE action against any record in any module. Verify that the `audit_log` table contains 4 corresponding records, one per operation, each with the correct `action` value.*

**FR-AUDIT-002:** The system shall store the following fields in every audit log record: `tenant_id`, `user_id`, `user_name`, `module`, `action`, `affected_table`, `affected_record_id`, `old_values` (JSON), `new_values` (JSON), `ip_address`, `user_agent`, `timestamp` (UTC).

*Test oracle: Insert a record via the application. Query `audit_log` and confirm all 12 fields are populated. Verify `timestamp` is stored in UTC. Verify `old_values` is `NULL` for CREATE actions and `new_values` is `NULL` for DELETE actions.*

**FR-AUDIT-003:** The system shall capture `old_values` as a JSON snapshot of all field values immediately before, and `new_values` as a JSON snapshot of all field values immediately after, every UPDATE operation.

*Test oracle: Update a customer name from "Acme Ltd" to "Acme Uganda Ltd". Retrieve the corresponding audit record. Confirm `old_values` contains `{"name": "Acme Ltd"}` and `new_values` contains `{"name": "Acme Uganda Ltd"}`. Confirm no other fields are included unless they changed.*

**FR-AUDIT-004:** The system shall set `action` to one of the following enumerated values: `CREATE`, `UPDATE`, `DELETE`, `APPROVE`, `REJECT`, `LOGIN`, `LOGOUT`. No other values shall be permitted.

*Test oracle: Attempt to insert an audit record with `action = "MODIFY"` via the application layer. Verify the operation fails with a validation error.*

**FR-AUDIT-005:** The system shall derive `tenant_id` exclusively from the authenticated session context. The system shall not accept `tenant_id` from any client-supplied request parameter.

*Test oracle: Submit a state-changing HTTP request with a crafted `tenant_id` parameter in the request body that differs from the session tenant. Verify the audit record stores the session-derived `tenant_id`, not the client-supplied value.*

### 2.2 Authentication Event Logging

**FR-AUDIT-006:** The system shall create an audit log record for every user login attempt, regardless of outcome, with `action` set to `LOGIN`, and shall include `ip_address`, `user_agent`, and `timestamp` (UTC).

*Test oracle: Perform 1 successful and 1 failed login attempt. Verify 2 records exist in `audit_log` with `action = "LOGIN"`, 1 with a valid `user_id` and 1 with `user_id = NULL` and a `new_values` field containing `{"outcome": "FAILED", "attempted_username": "<value>"}` .*

**FR-AUDIT-007:** The system shall record a failed login attempt's `new_values` field as a JSON object containing `{"outcome": "FAILED", "attempted_username": "<submitted_value>"}`. The system shall not log the submitted password in any field.

*Test oracle: Submit an incorrect password. Retrieve the audit record. Confirm `new_values` contains `outcome` and `attempted_username` only. Confirm no field contains the submitted password string.*

**FR-AUDIT-008:** The system shall create an audit log record with `action = "LOGOUT"` when a user ends a session by an explicit logout action or when the system terminates the session due to inactivity timeout.

*Test oracle: Log in, then log out explicitly. Verify a `LOGOUT` record exists. Log in again, wait for the session timeout period to elapse, then verify a second `LOGOUT` record exists with a `new_values` field containing `{"reason": "TIMEOUT"}`.*

### 2.3 Super Admin Impersonation Logging

**FR-AUDIT-009:** The system shall create an audit log record with `action = "IMPERSONATE_START"` when a super admin initiates an impersonation session, capturing the super admin's `user_id` in `user_id` and the impersonated tenant's `tenant_id` and `user_id` in `new_values`.

*Test oracle: Initiate an impersonation session as super admin. Verify the `audit_log` contains a record with `action = "IMPERSONATE_START"`, `user_id` = super admin ID, and `new_values.impersonated_user_id` = target user ID.*

**FR-AUDIT-010:** The system shall create an audit log record with `action = "IMPERSONATE_END"` when an impersonation session terminates, either by the super admin explicitly ending it or by session expiry.

*Test oracle: End an impersonation session. Verify an `IMPERSONATE_END` record exists with the same `tenant_id` and `new_values.impersonated_user_id` as the corresponding `IMPERSONATE_START` record.*

**FR-AUDIT-011:** The system shall attribute every action performed during an impersonation session to a `new_values` sub-field `{"performed_by_super_admin": "<super_admin_user_id>"}` in addition to storing the impersonated user's identity in `user_id`.

*Test oracle: While impersonating a user, update a record. Retrieve the audit record. Confirm `user_id` equals the impersonated user's ID and `new_values.performed_by_super_admin` equals the super admin's user ID.*

### 2.4 Bulk Operation Logging

**FR-AUDIT-012:** The system shall create one audit log record per affected row when a bulk operation (e.g., bulk approve, bulk delete, bulk status update) is applied to multiple records simultaneously.

*Test oracle: Bulk-approve 50 purchase orders. Verify exactly 50 `APPROVE` audit records are created, one per purchase order, each with the correct `affected_record_id`.*

**FR-AUDIT-013:** The system shall store a `bulk_operation_id` (a UUID generated at the start of the bulk operation) in the `new_values` JSON field of every audit record created by the same bulk operation, enabling grouped retrieval of all records from one bulk action.

*Test oracle: Retrieve audit records from a bulk operation. Verify all records share an identical `new_values.bulk_operation_id` UUID. Verify that a single-record operation does not include `bulk_operation_id` in `new_values`.*

### 2.5 API and Mobile Action Logging

**FR-AUDIT-014:** The system shall create an audit log record for every state-changing operation initiated via the mobile REST API using the same schema as web-initiated operations.

*Test oracle: Create an invoice via the mobile API using a valid JWT. Verify an audit record exists with `module = "Sales"`, `action = "CREATE"`, `affected_table = "invoices"`, and `user_id` matching the JWT `user_id` claim.*

**FR-AUDIT-015:** The system shall store the API client's `user_agent` string (as supplied in the `User-Agent` HTTP header) in the `user_agent` field of every API-initiated audit record.

*Test oracle: Submit a mobile API request with `User-Agent: LonghornMobile/2.1 (Android 14)`. Retrieve the audit record. Confirm `user_agent = "LonghornMobile/2.1 (Android 14)"`.*

### 2.6 Background Job Logging

**FR-AUDIT-016:** The system shall create an audit log record for every state-changing operation performed by a background job (e.g., scheduled depreciation run, automated remittance, payroll calculation batch), with `user_id` set to a reserved system user identifier and `user_name` set to the job's canonical name.

*Test oracle: Execute the scheduled asset depreciation job. Verify audit records exist for each asset updated, with `user_id = "SYSTEM"` and `user_name = "DepreciationJob"`.*

**FR-AUDIT-017:** The system shall store the background job's execution ID in the `new_values` JSON field under the key `job_execution_id` for every audit record generated by that job run.

*Test oracle: Run a payroll batch. Retrieve all audit records from that run. Verify all records share an identical `new_values.job_execution_id` value.*

### 2.7 Configuration and Permission Change Logging

**FR-AUDIT-018:** The system shall create an audit log record when any tenant-level configuration is changed (e.g., localisation profile update, module activation/deactivation, tax rate override), with `affected_table` identifying the configuration entity.

*Test oracle: Change the VAT rate in the tenant's localisation profile. Verify an audit record exists with `action = "UPDATE"`, `affected_table = "tenant_config"`, and `old_values` containing the previous VAT rate.*

**FR-AUDIT-019:** The system shall create an audit log record when any user's role assignment, permission override, or account status changes, capturing the full `old_values` and `new_values` of the affected RBAC record.

*Test oracle: Promote a user from the `cashier` role to the `accountant` role. Verify an audit record exists with `affected_table = "user_roles"`, `old_values.role = "cashier"`, and `new_values.role = "accountant"`.*

**FR-AUDIT-020:** The system shall create an audit log record when a tenant account is created, suspended, or terminated by a super admin, with `affected_table = "tenants"` and `old_values` and `new_values` capturing the status transition.

*Test oracle: Suspend a tenant account. Verify an audit record exists with `action = "UPDATE"`, `affected_table = "tenants"`, `old_values.status = "active"`, and `new_values.status = "suspended"`.*
