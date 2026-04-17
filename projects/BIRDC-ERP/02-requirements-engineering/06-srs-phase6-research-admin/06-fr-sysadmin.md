## 3.3 F-017: System Administration / IT

### 3.3.1 User Management

**FR-IT-001**
When the IT Administrator creates a new user account, the system shall store: user ID (auto-assigned, format `USR-NNNN`), full name, email address, username (unique), initial temporary password (system-generated, minimum 12 characters, randomly generated), linked employee record (for staff accounts), and the account creation timestamp and creator identity. The system shall force a password reset on first login; the temporary password shall expire after 72 hours.

**FR-IT-002**
When a new user logs in for the first time with a temporary password, the system shall redirect the user to the password change screen before granting access to any other screen. The new password must satisfy the configured password policy (minimum 12 characters, at least 1 uppercase, 1 lowercase, 1 digit, 1 special character). If the policy is not satisfied, the system shall display specific field-level guidance and reject the submission.

**FR-IT-003**
When the IT Administrator deactivates a user account, the system shall immediately invalidate all active sessions for that user (including JWT refresh tokens), prevent any new logins, and log the deactivation with the IT Administrator's identity, timestamp, and reason. The deactivation shall take effect within 5 seconds of the IT Administrator's action. Historical data created by the deactivated user shall be preserved and attributed to that user's identity.

**FR-IT-004**
When the IT Administrator edits a user account (name, email, department, or role assignment), the system shall log the previous and new values in the immutable audit log with the IT Administrator's identity and timestamp. A role assignment change shall take effect within 60 seconds without requiring the affected user to log out and back in.

**FR-IT-005**
When a user account has not been logged into for more than 90 consecutive days, the system shall automatically flag it as "Inactive — Review Required" and alert the IT Administrator via email. The IT Administrator shall confirm deactivation or reactivation; the account shall not be automatically deactivated without IT Administrator action.

**FR-IT-006**
When the IT Administrator initiates a forced password reset for a user account, the system shall invalidate the current password, generate a new temporary password, email it to the user's registered email address, and force a password change on next login. All active sessions for that user shall be terminated immediately.

### 3.3.2 Role and Permission Matrix

**FR-IT-007**
When the IT Administrator creates a new role, the system shall store the role name, role description, and an 8-layer permission set comprising: (1) allowed pages/modules, (2) allowed API endpoints, (3) allowed UI element visibility (buttons, form fields), (4) location-based access rules (LAN only / VPN / any), (5) time-based access rules (hours of day and days of week), (6) conditional rules (e.g., can view salary details only if own record), (7) object ownership rules (e.g., can edit only own journal entries), and (8) data access scope (own department / all departments / all data). All 8 layers shall be configurable by the IT Administrator without developer involvement (DC-002).

**FR-IT-008**
When a user's request arrives at any API endpoint, the system shall evaluate all 8 permission layers for that user's assigned role and the specific endpoint and action requested. A request shall be authorised only if all applicable layers permit the action. If any layer denies the request, the system shall return HTTP 403 and log the denial with user ID, endpoint, action, layer that denied, and timestamp.

**FR-IT-009**
When the IT Administrator opens the permission matrix editor, the system shall display all roles in a matrix view with modules as columns and roles as rows, showing the permission level for each intersection (None / Read / Create / Edit / Delete / Approve). The IT Administrator shall be able to update individual permissions and save the matrix; changes shall take effect within 60 seconds.

**FR-IT-010**
When the IT Administrator assigns a user to the Finance Director, IT Administrator, or Director role, the system shall require that the user account has two-factor authentication (TOTP) configured before the role assignment is saved. If TOTP is not yet configured, the system shall prompt the IT Administrator to complete TOTP setup for that user before the role can be assigned.

**FR-IT-011**
When a new ERP module or API endpoint is added during system development, the system shall require the developer to register the endpoint in the permission table before the endpoint is accessible. Unregistered endpoints shall return HTTP 404 regardless of the caller's role, preventing accidental access to unreleased functionality.

### 3.3.3 Audit Log Review

**FR-IT-012**
When the IT Administrator or Finance Director opens the audit log review screen and applies filters (user, action type, date range, module, table name, record ID), the system shall return all matching audit records within 3 seconds for a result set of up to 10,000 records, displayed in a DataTable with column-level sorting.

**FR-IT-013**
When the Finance Director or Auditor General requires an audit trail export for a specific date range, the system shall export all matching audit log records to a tamper-evident PDF report — formatted as an ordered table with: record ID, timestamp, actor username, actor IP address, module, action, table name, record ID, field changed, previous value, and new value — within 30 seconds for up to 50,000 records.

**FR-IT-014**
When a financial transaction audit record is written, the system shall include: the GL journal entry reference (if applicable), the module that triggered the transaction, and the hash of the previous audit record for the same actor session, enabling chain-of-custody verification for each user session's activities.

**FR-IT-015**
When any audit log record older than 7 years would be due for deletion, the system shall prevent deletion. Audit log records shall have no delete mechanism accessible to any user role, including IT Administrator. The 7-year retention constraint shall be enforced at the database trigger level, satisfying DC-003 and Uganda Companies Act requirements.

**FR-IT-016**
When the IT Administrator searches the audit log for all actions performed by a specific user on a specific date, the system shall return a chronological log showing every page access, every data change, and every failed action attempted by that user during that day, enabling full forensic reconstruction of user activity.

### 3.3.4 Backup Management

**FR-IT-017**
When the IT Administrator configures the backup schedule, the system shall support the following retention policy: daily backups retained for 7 days, weekly backups retained for 4 weeks, and monthly backups retained for 12 months. The backup schedule configuration UI shall allow the IT Administrator to set the daily backup time, weekly backup day and time, and monthly backup date and time, without developer involvement (DC-002).

**FR-IT-018**
When a scheduled backup runs, the system shall execute a full `mysqldump` of the BIRDC ERP database, compress the dump file, record the backup file name, file size, checksum (SHA-256), and start and end timestamps in the backup log, and store the file in the configured backup destination directory. The backup shall complete without disrupting active user sessions.

**FR-IT-019**
When a backup completes, the system shall perform an integrity check by verifying the SHA-256 checksum of the backup file against the stored checksum. If the checksum verification fails, the system shall alert the IT Administrator via email and log the failure in the backup log with status "Integrity Check Failed".

**FR-IT-020**
When the IT Administrator views the backup management screen, the system shall display: all backup files with their date, type (daily/weekly/monthly), file size, checksum status (Verified / Failed / Not Checked), and the number of days until each backup expires under the retention policy. Files approaching expiry shall be highlighted.

**FR-IT-021**
When a backup file's retention period expires, the system shall automatically delete the file and log the deletion with the file name, original backup date, and deletion timestamp. The IT Administrator shall receive a weekly summary of expired and deleted backup files.

**FR-IT-022**
When the IT Administrator initiates a manual backup outside the schedule (e.g., before a system update), the system shall execute the backup immediately, following the same process as a scheduled backup (FR-IT-018), and log it as a "Manual Backup" in the backup log.

### 3.3.5 Integration Configuration

**FR-IT-023**
When the IT Administrator opens the integration configuration screen, the system shall display a list of all configured external integrations with their current status: EFRIS API, MTN MoMo Business API, Airtel Money API, PHPMailer SMTP, ZKTeco biometric device connection, and Africa's Talking SMS gateway. Each integration shall show: connection status (Connected / Disconnected / Error), last successful connection timestamp, and a "Test Connection" button.

**FR-IT-024**
When the IT Administrator saves API credentials for any external integration (EFRIS API key, MTN MoMo API key, Airtel Money API key, SMTP password, or Africa's Talking API key), the system shall encrypt the credential values using AES-256 before storing them in the database. The credentials shall never appear in plain text in any log file or API response.

**FR-IT-025**
When the IT Administrator clicks "Test Connection" for an external integration, the system shall send a minimal test request to the integration endpoint (e.g., a credentials validation call for EFRIS, an account balance check for MTN MoMo), display the API response code and message, and update the integration status within 15 seconds.

**FR-IT-026**
When an external integration fails during normal operation (e.g., EFRIS submission failure, mobile money disbursement failure), the system shall log the failure with: integration name, request timestamp, request payload (redacted of sensitive values), HTTP status code, error message, and retry count. The IT Administrator shall be alerted by email for failures that exceed 3 retry attempts.

**FR-IT-027**
When the IT Administrator configures the Africa's Talking SMS gateway, the system shall store the sender ID, API key, and account username, and use this gateway for sending payment confirmation SMS messages to farmers and casual workers. The configuration shall be testable via the "Test Connection" mechanism (FR-IT-025).

### 3.3.6 Report Scheduling

**FR-IT-028**
When the IT Administrator or Finance Manager creates a scheduled report configuration, the system shall store: report name, report type (from the available report list across all modules), output format (PDF / Excel), schedule (daily / weekly / monthly — with specific time and day), recipient email list, and the user who configured the schedule.

**FR-IT-029**
When a scheduled report's execution time arrives, the system shall generate the report using the same report engine as the on-demand version, attach it to an email, and send it to all configured recipients via PHPMailer. If the report generation or email delivery fails, the system shall log the failure and retry once after 15 minutes. A persistent failure shall alert the IT Administrator.

**FR-IT-030**
When the IT Administrator views the report schedule list, the system shall display: report name, schedule description, last run timestamp, last run status (Success / Failed), next scheduled run timestamp, and the recipient list. The IT Administrator shall be able to run any scheduled report immediately outside the schedule (on-demand override) without altering the schedule.

### 3.3.7 System Health Dashboard

**FR-IT-031**
When the IT Administrator opens the system health dashboard, the system shall display the following real-time indicators, refreshed at a configurable interval (default: 60 seconds): server CPU utilisation (%), server RAM utilisation (%), disk usage (GB used / GB total / % used), MySQL database size (GB), number of currently active user sessions, number of queries per second (last 60 seconds), and web server error rate (errors per 100 requests in the last hour).

**FR-IT-032**
When the IT Administrator opens the system health dashboard, the system shall display the status of all external integrations (EFRIS, MTN MoMo, Airtel Money, PHPMailer SMTP, ZKTeco biometric, Africa's Talking SMS) as a colour-coded indicator: green (connected and last heartbeat < 5 minutes ago), amber (last heartbeat > 5 minutes), or red (last heartbeat > 30 minutes or last connection attempt failed).

**FR-IT-033**
When the system health dashboard shows the EFRIS submission queue status, the system shall display: number of documents pending submission, number submitted in the last 24 hours, number with submission errors, and the timestamp of the most recent successful submission. The Finance Manager shall also be able to view the EFRIS queue status from the financial accounting module.

**FR-IT-034**
When any system health metric exceeds a configurable alert threshold (e.g., disk usage > 80%, RAM > 90%, error rate > 5 errors per 100 requests), the system shall send an automated email alert to the IT Administrator and log the alert in the system health log with the metric name, threshold value, observed value, and timestamp.

**FR-IT-035**
When the IT Administrator views the error log summary on the system health dashboard, the system shall display the 20 most recent critical and error-level PHP application errors with: timestamp, error code, error message (truncated to 200 characters), file name and line number, and HTTP request URI that triggered the error. A "View Full Log" link shall navigate to the complete error log.

**FR-IT-036**
When the IT Administrator views the last backup status on the system health dashboard, the system shall display: the most recent backup file name, backup type (daily/weekly/monthly), backup timestamp, file size, checksum status, and the number of days since the last successful integrity-verified backup. If the last backup is more than 25 hours old, the status shall display in red.
