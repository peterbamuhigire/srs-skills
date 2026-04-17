## 2. Task-Level Definition of Done

A task (feature, fix, or change) is DONE only when ALL of the following criteria are true. Each criterion must be verifiable — not assumed.

### 2.1 Code Review

- Code has been reviewed by Peter Bamuhigire (or a designated reviewer explicitly named by Peter Bamuhigire for that task) and approved in writing (pull request approval or equivalent).
- No open review comments remain unresolved at the time of approval.

### 2.2 Static Analysis — PHPStan

- PHPStan analysis at level 8 passes with zero errors on all files modified or added by this task.
- The PHPStan baseline (if used) has not been extended to suppress new errors introduced by this task.

### 2.3 Coding Standards — PHP_CodeSniffer

- PHP_CodeSniffer with the PSR-12 ruleset passes with zero errors and zero warnings on all files modified or added by this task.

### 2.4 Automated Tests — PHPUnit

- PHPUnit tests are written for every new service method introduced by this task.
- Overall test coverage for financial service classes (GL posting, payroll calculation, remittance allocation, invoice lifecycle) is maintained at ≥ 80%.
- All existing tests pass with no regressions.

### 2.5 RBAC Enforcement

- Every new API endpoint introduced by this task has a Role-Based Access Control permission check implemented at the API layer (controller or middleware), not only in the user interface.
- The permission check is verified by an automated test that confirms a request without the required role receives an HTTP 403 response.

### 2.6 Audit Log

- Every new state-changing operation introduced by this task calls `AuditLogService` and records an audit log entry.
- The audit log entry includes: user ID, action type, affected table and record ID, before-state, after-state, and timestamp.
- The audit log entry is verified by an automated test.

### 2.7 Configuration Over Code (DC-002)

- No business rule introduced or modified by this task is hardcoded in PHP source code.
- All configurable values — tax rates, commission rates, PPDA thresholds, price list values, recipe quantities, payroll element rates — are stored in configuration tables and changeable via the administration UI without developer involvement.
- No hardcoded currency symbols or monetary amounts appear in any PHP file, template, or migration introduced by this task.

### 2.8 SQL Injection Prevention

- Every new database query introduced by this task uses PDO prepared statements with bound parameters.
- No string concatenation is used to build SQL queries in any file modified or added by this task.

### 2.9 CSRF Protection

- Every new state-changing web form introduced by this task includes and validates a CSRF token.
- CSRF validation is verified by an automated test that confirms a request without a valid CSRF token is rejected.

### 2.10 GL Auto-Posting Verification

- If the task involves any financial transaction that creates or modifies a General Ledger entry, an automated test verifies that the resulting GL entry is double-entry balanced (total debits equal total credits).
- The test explicitly names the debit account and credit account and asserts the correct amounts.

### 2.11 Segregation of Duties (BR-003)

- If the task touches any workflow covered by Business Rule BR-003 (the creator of a transaction must not be the approver or verifier of the same transaction), an automated test confirms that the system rejects an approval or verification action performed by the same user who created the record.

### 2.12 Business Rule Tests (BR-001 to BR-018)

- If the task introduces or modifies behaviour governed by any of Business Rules BR-001 through BR-018, at least one automated test is written that directly verifies compliance with that business rule.
- The test is named with the business rule identifier (e.g., `test_br_008_mass_balance_verification`).

### 2.13 Documentation

- All new public methods and classes are documented with PHPDoc block comments: description, parameter types, return type, and exceptions thrown.
- If the task introduces new API endpoints, the API specification document is updated with the endpoint path, HTTP method, request parameters, response schema, and required RBAC permission.

### 2.14 Staging Deployment and Smoke Test

- The completed feature is deployed to the staging environment on BIRDC's infrastructure.
- A smoke test is performed on staging: the feature is exercised through its primary happy-path workflow end-to-end.
- The smoke test result is documented (pass/fail with notes).

### 2.15 Peer Confirmation

- At least one other developer (or Peter Bamuhigire, if working solo) confirms that the feature works as specified by exercising it on the staging environment — not merely confirming that the code compiles or tests pass.
