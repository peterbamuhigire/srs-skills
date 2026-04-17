## 2. Test Levels

### 2.1 Unit Testing

**Objective:** Verify that individual functions, methods, and stored procedures produce correct outputs for all valid and invalid inputs.

**Technology:** PHPUnit (PHP 8.3 backend services); JUnit with Kotlin test framework (Android apps).

**Coverage requirement:** Minimum 80% line coverage for all financial services: GL posting engine, PAYE/NSSF/LST payroll calculation, commission calculation engine, FIFO remittance allocation stored procedure `sp_apply_remittance_to_invoices`, mass balance verification, and hash chain computation. All other modules: minimum 60% line coverage.

**Responsibility:** Hired developers; Peter Bamuhigire reviews financial service unit test assertions.

**Entry criteria:**
- Feature branch code compiles without errors.
- Developer has written tests for the function under test before committing.

**Exit criteria:**
- Coverage thresholds met per module.
- Zero failing unit tests in the CI pipeline on the feature branch.
- All financial calculation tests use exact-value oracles (no approximate assertions for monetary values).

---

### 2.2 Integration Testing

**Objective:** Verify correct data exchange and contract adherence between internal services and between the system and external APIs.

**Sub-levels:**

1. *Service-to-service integration* — verify that module boundaries honour the service/repository pattern: e.g., SalesService correctly invokes GLPostingService and the resulting journal entry appears in `tbl_gl_entries` with the expected debit/credit split.
2. *Database integration* — verify stored procedures, triggers, and foreign key constraints behave correctly under concurrent writes. Specifically: `sp_apply_remittance_to_invoices` under concurrent remittance posts; hash chain trigger under rapid sequential GL inserts.
3. *API contract testing* — verify the EFRIS REST API integration correctly serialises fiscal documents, handles HTTP 200/400/500 responses, and enqueues retries on failure. Verify MTN MoMo and Airtel Money payment initiation and callback handling. Verify the mobile API JWT token lifecycle: issuance, refresh, expiry, and rejection of tampered tokens.
4. *Biometric device integration* — verify ZKTeco attendance data is imported without duplication, without loss, and is mapped to the correct employee records.

**Responsibility:** Hired developers under Peter Bamuhigire's technical review.

**Entry criteria:**
- All unit tests pass.
- Staging environment is provisioned with integrated services available (EFRIS sandbox, MoMo sandbox).

**Exit criteria:**
- All integration test cases pass against the staging environment.
- No unhandled exception propagates across a service boundary.
- EFRIS sandbox submission returns a valid FDN for a test invoice.

---

### 2.3 System Testing

**Objective:** Verify end-to-end user journeys across module boundaries, simulating real BIRDC operational workflows.

**Key journeys under test:**

1. Factory gate sale → EFRIS submission → GL auto-post → AR update → agent cash balance update.
2. Agent remittance submission → FIFO allocation via `sp_apply_remittance_to_invoices` → AR cleared → commission accrual → GL post.
3. Matooke delivery (Farmer Delivery App offline) → sync → 5-stage procurement workflow → farmer contribution breakdown → stock receipt → GL post.
4. Production order → material requisition → WIP posting → QC inspection → CoA issuance → finished goods transfer → inventory available for sale.
5. Payroll run → PAYE/NSSF/LST calculation → payroll lock → GL auto-post → bank file generation → bulk mobile money payment file.
6. Budget vote expenditure → 80% threshold alert → 95% alert → over-budget override attempt blocked without Director approval.
7. Parliamentary budget report and IFRS P&L generated simultaneously from the same system.

**Responsibility:** Peter Bamuhigire (test execution oversight); hired developers (execution support).

**Entry criteria:**
- Integration tests pass.
- Staging database seeded with representative BIRDC data (test farmer names, agents, chart of accounts matching the 1,307-account configuration).

**Exit criteria:**
- All system test journeys complete without errors.
- All GL auto-postings balance (total debits = total credits for every journey).
- EFRIS FDN returned and stored for every fiscal document in journey 1.

---

### 2.4 User Acceptance Testing (UAT)

**Objective:** Confirm that the delivered system meets BIRDC's operational requirements as judged by domain-expert BIRDC staff.

**UAT owners by module group:**

| Module Group | UAT Owner |
|---|---|
| Financial modules (GL, AR, AP, Budget, Payroll) | Finance Director |
| Sales, Agent Distribution, POS | Sales Manager |
| Quality Control, Manufacturing | QC Manager |
| Procurement, Farmer Management | Procurement/Administration Officer |
| HR, Payroll self-service | HR Manager |
| System Administration | IT Administrator |

**Format:** UAT sessions are script-guided (from the Test Plan) but the UAT owner performs all actions independently. Peter Bamuhigire observes and records outcomes.

**Entry criteria:**
- System tests pass for the phase under UAT.
- UAT environment loaded with a representative dataset approved by BIRDC management.
- UAT owners have received a one-page Quick Reference Card for their module group.

**Exit criteria:**
- UAT owner signs the Phase Gate acceptance form.
- Zero Critical defects open.
- Zero High defects open that affect the UAT owner's primary workflow.
- All Medium defects acknowledged and scheduled for resolution.

---

### 2.5 Performance Testing

**Objective:** Verify the system meets all performance thresholds defined in `_context/metrics.md` under realistic and peak load conditions.

**Scenarios:**

1. *Concurrent user load* — simulate 50 simultaneous authenticated web users performing mixed operations (report generation, invoice posting, stock queries). Measure response times at P95.
2. *Peak production scenario* — simulate the 140 MT/day peak production load: 1,071 agents simultaneously submitting POS transactions, concurrent remittances, and stock queries.
3. *Report generation* — generate Trial Balance, P&L, and Budget vs. Actual for a 12-month period. Target: ≤ 10 seconds.
4. *Trial Balance* — generate on demand. Target: ≤ 5 seconds.
5. *Farmer contribution breakdown* — process a batch of 100+ farmers. Target: ≤ 3 seconds.
6. *Audit trail query* — query any 30-day period for any user. Target: ≤ 5 seconds.
7. *Product search* — barcode scan or text search. Target: ≤ 500 ms at P95.

**Tools:** Apache JMeter or k6 (web); Android Profiler (mobile).

**Entry criteria:** System tests pass; staging server hardware matches production specification.

**Exit criteria:** All thresholds in `_context/metrics.md` met or exceeded under the 50-concurrent-user load scenario. Peak scenario (140 MT/day) completes without errors.

---

### 2.6 Security Testing

**Objective:** Verify the system is free from vulnerabilities in the OWASP Mobile Top 10 and OWASP Web Top 10 categories.

**Scope:**

- *Web application:* OWASP Top 10 (2021) — injection, broken authentication, sensitive data exposure, XML/EFRIS external entities, broken access control, security misconfiguration, XSS, insecure deserialisation, components with known vulnerabilities, logging/monitoring failures.
- *Mobile application:* OWASP Mobile Top 10 (2024) — improper credential usage, inadequate supply chain security, insecure authentication/authorisation, insufficient input/output validation, insecure communication, inadequate privacy controls, insufficient binary protections, security misconfiguration, insecure data storage, insufficient cryptography.
- *Specific controls:* 8-layer RBAC enforcement at the API layer (not just UI); SOD enforcement — verify a user cannot approve their own transaction via direct API call; JWT token replay attack resistance; SQL injection resistance (100% PDO prepared statements); CSRF token validation; account lockout after 5 failed attempts; 2FA enforcement for Director, Finance Director, and IT Administrator roles; bcrypt/Argon2id password hash verification; TLS 1.3 in transit; GL hash chain tamper detection.

**Approach:** Combination of automated SAST scanning (static), DAST scanning (dynamic against staging), and manual penetration testing for critical paths (authentication bypass, privilege escalation, FIFO manipulation, payroll record modification).

**Entry criteria:** System tests pass; security hardening checklist completed by developer.

**Exit criteria:** Zero Critical or High OWASP findings open. All Medium findings remediated or formally accepted with documented rationale. Penetration test report signed off.

---

### 2.7 Offline / Sync Testing

**Objective:** Verify that all Android apps that must operate offline (Sales Agent App, Farmer Delivery App, Warehouse App) do so without data loss, and that sync on reconnect is complete, consistent, and conflict-free.

**Scenarios:**

1. Sales Agent App — 50 POS transactions recorded with network completely off; reconnect; verify all 50 transactions synced to server, GL posted, agent cash balance updated.
2. Farmer Delivery App — register 5 new farmers offline, record 20 deliveries offline; reconnect; verify all farmer records and deliveries appear on server.
3. Warehouse App — complete a physical stock count offline; reconnect; verify count data synced correctly.
4. Conflict scenario — same agent stock item modified offline on the device and online on the server simultaneously; verify conflict logged, server timestamp wins, conflict visible in review queue.
5. Partial sync — simulate sync interrupted mid-way; reconnect; verify sync resumes and completes without duplicate records.

**Entry criteria:** Android apps built with Room (SQLite) offline storage; WorkManager sync jobs configured.

**Exit criteria:** Zero transaction loss across all offline scenarios. Sync completes within 60 seconds for a typical day's transactions (≤ 200 records). All conflicts logged in the review queue.

---

### 2.8 Regression Testing

**Objective:** Verify that new code changes do not break previously passing functionality.

**Trigger:** Regression suite runs automatically on every pull request merge to the `main` branch via GitHub Actions CI/CD pipeline. Full regression suite also runs manually before each Phase Gate sign-off.

**Suite composition:** All unit tests + all integration tests + the critical-path system test cases for modules already in production.

**Entry criteria:** Developer has merged feature branch to `main`.

**Exit criteria:** Zero regressions (no previously passing test now fails). If a regression is detected, the merge is blocked until the root cause is identified and fixed.
