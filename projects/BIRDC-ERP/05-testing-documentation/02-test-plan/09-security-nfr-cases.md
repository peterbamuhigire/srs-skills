## Security — TC-SEC

---

**TC-SEC-001** | Security | SQL injection: parameterised query blocks injection attempt

*Preconditions:* System running on staging. Test tool: OWASP ZAP or manual test string.

*Test steps:*
1. Attempt SQL injection via the product search field: enter `' OR '1'='1`.
2. Attempt SQL injection via the invoice number filter.
3. Attempt SQL injection via the agent name search.

*Expected result:* All fields reject injection. No SQL error returned. No data exposed. 100% PDO prepared statements — no string concatenation in queries. Response is a normal "no results" or validation error, not a database error. | **P1**

---

**TC-SEC-002** | Security | XSS prevention: script tags stripped on output

*Preconditions:* Test user with access to a free-text field (e.g., product description or journal entry notes).

*Test steps:*
1. Enter `<script>alert('XSS')</script>` in a product description field.
2. Save.
3. View the product description on screen.

*Expected result:* Script tag not executed. Output displayed as plain text (HTML-encoded: `&lt;script&gt;alert('XSS')&lt;/script&gt;`). `htmlspecialchars()` applied on all output. | **P1**

---

**TC-SEC-003** | Security | CSRF token validation: state-changing request without token rejected

*Preconditions:* Staging environment running.

*Test steps:*
1. Intercept a POST request for invoice confirmation using Burp Suite.
2. Remove the CSRF token from the request.
3. Resubmit the request.

*Expected result:* Server returns HTTP 403. Invoice not confirmed. Error logged. CSRF token validation applied on all state-changing forms. | **P1**

---

**TC-SEC-004** | Security | Account lockout after 5 failed login attempts

*Preconditions:* Test account "lockout.test@birdc.go.ug" with a known password.

*Test steps:*
1. Attempt login with incorrect password 5 times.
2. Attempt login with correct password on the 6th attempt.

*Expected result:* Account locked after 5th failed attempt. 6th attempt (correct password) returns: "Account locked. Contact IT Administrator." Lockout duration applies per configured setting. Audit trail records all 5 failed attempts and the lockout event. | **P1**

---

**TC-SEC-005** | Security | JWT token: expired access token rejected, refresh token valid

*Preconditions:* Mobile app authenticated with a JWT access token. Token validity: 15 minutes.

*Test steps:*
1. Wait for access token to expire (15 minutes).
2. Attempt an API call with the expired access token.
3. Use the refresh token (30-day validity) to obtain a new access token.
4. Retry the API call with the new access token.

*Expected result:* Step 2: API returns HTTP 401 Unauthorized. Step 3: New access token issued. Step 4: API call succeeds. | **P1**

---

**TC-SEC-006** | Security | SOD enforcement at API layer: self-approval of journal entry

*Preconditions:* "Finance Officer A" creates a journal entry JE-TEST-100.

*Test steps:*
1. Finance Officer A attempts to approve JE-TEST-100 via a direct API request (bypassing the UI approval button which is hidden for the entry creator).

*Expected result:* API returns HTTP 403 Forbidden. JE-TEST-100 remains in "Draft" status. Audit trail records the failed approval attempt with Finance Officer A's identity. (BR-003 enforced at API layer.) | **P1**

---

**TC-SEC-007** | Security | Password hashing: stored hash is bcrypt or Argon2id

*Preconditions:* DBA access to staging database `users` table.

*Test steps:*
1. Create a test user account with password "TestPass@2026."
2. Query the `users` table for the stored password hash.

*Expected result:* Stored value is a bcrypt ($2y$) or Argon2id hash. The plain-text password is not stored. The hash cannot be reversed to reveal the password. | **P1**

---

**TC-SEC-008** | Security | TLS 1.3 enforced in transit — no plain HTTP accepted

*Preconditions:* Staging server with HTTPS configured.

*Test steps:*
1. Attempt to access the ERP via `http://` (plain HTTP).
2. Verify TLS version negotiated on HTTPS connection.

*Expected result:* HTTP request redirected to HTTPS (HTTP 301). TLS version negotiated: TLS 1.3. TLS 1.0 and TLS 1.1 rejected. | **P1**

---

**TC-SEC-009** | Security | Privilege escalation: Sales Officer cannot access Finance module pages

*Preconditions:* User "Sales Officer B" has role "Sales Officer." Finance module pages are restricted to "Finance Officer" and above.

*Test steps:*
1. Log in as Sales Officer B.
2. Directly navigate to `/public/finance/gl/journal-entries` (URL guessing).
3. Attempt API call to GL posting endpoint with Sales Officer B's session token.

*Expected result:* Both the URL navigation and the direct API call return HTTP 403 Forbidden. No GL data exposed. Attempt logged in audit trail. | **P1**

---

**TC-SEC-010** | Security | Android app: sensitive data not stored in plain text (OWASP Mobile M9)

*Preconditions:* Sales Agent App installed on Android test device. Agent logged in.

*Test steps:*
1. Inspect app data storage on the device (adb shell or device file explorer).
2. Check `EncryptedSharedPreferences` and Room database for plain-text credentials or sensitive financial data.

*Expected result:* No plain-text JWT tokens, passwords, or financial transaction data in the app's local storage. All sensitive data stored using `EncryptedSharedPreferences`. Room database encrypted at rest. | **P1**

---

## Non-Functional Requirements — TC-NFR

---

**TC-NFR-001** | NFR | Product search response ≤ 500 ms at P95 under 50 concurrent users

*Preconditions:* Staging environment with 100+ products. 50 concurrent virtual users simulated via JMeter.

*Test steps:*
1. Configure JMeter: 50 concurrent users, ramp-up 30 seconds, hold 2 minutes.
2. Each user sends a product text search request.
3. Collect P95 response time.

*Expected result:* P95 response time ≤ 500 ms across all 50 users. Zero errors. | **P1**

---

**TC-NFR-002** | NFR | 50 concurrent users: no degradation on mixed operations

*Preconditions:* Staging environment. JMeter configured for 50 concurrent users performing mixed operations: 30% invoice queries, 20% stock queries, 20% report generation, 15% GL entry, 15% POS transactions.

*Test steps:*
1. Run 5-minute mixed load test with 50 concurrent users.
2. Measure: response times, error rates, CPU and memory on staging server.

*Expected result:* No request times out. No HTTP 500 errors. All response times within thresholds defined in `_context/metrics.md`. Server CPU < 85%. Server memory < 90%. | **P1**

---

**TC-NFR-003** | NFR | Report generation ≤ 10 seconds for 12-month report

*Preconditions:* 12 months of test transactions in staging.

*Test steps:*
1. Generate Sales by Territory report for 12-month period.
2. Generate P&L report for 12-month period.
3. Generate AR Aging report for 12-month period.

*Expected result:* Each report generated within 10 seconds. | **P2**

---

**TC-NFR-004** | NFR | System uptime ≥ 99% during business hours (06:00–22:00 EAT)

*Preconditions:* Uptime monitoring configured on staging server. Monitor checks every 1 minute.

*Test steps:*
1. Monitor system for 7 consecutive business days.
2. Calculate uptime percentage for 06:00–22:00 EAT windows.

*Expected result:* Uptime ≥ 99% during business hours. Any downtime event < 1% of total monitored business hours. Downtime events logged with cause and duration. | **P2**

---

**TC-NFR-005** | NFR | Audit trail query for 30-day period ≤ 5 seconds

*Preconditions:* Audit log with ≥ 10,000 records.

*Test steps:*
1. Query audit log: any user, 30-day date range.
2. Measure query time.

*Expected result:* Results returned within 5 seconds. All mandatory fields present in results: actor, action, table, old values, new values, IP address, timestamp. | **P2**

---

**TC-NFR-006** | NFR | DC-001 compliance: new accounts assistant can post journal entry without training

*Preconditions:* Staging environment. Test participant "New Accounts Assistant" — a person unfamiliar with the system, given no training.

*Test steps:*
1. New Accounts Assistant logs into the Main ERP Workspace.
2. Navigates to the GL module.
3. Attempts to post a balanced journal entry (DR Cash UGX 50,000 / CR Revenue UGX 50,000) without referring to a manual.

*Expected result:* New Accounts Assistant completes the task correctly without manual reference. UI labels, tooltips, and workflow guide the user through the process. Task completed in ≤ 5 minutes. (DC-001 — zero mandatory training for routine operations.) | **P2**

---

**TC-NFR-007** | NFR | DC-002 compliance: Finance Director updates PAYE tax bands without developer

*Preconditions:* Finance Director account with payroll configuration access. Current PAYE bands loaded.

*Test steps:*
1. Finance Director logs into the system.
2. Navigates to Payroll → Configuration → PAYE Tax Bands.
3. Updates Band 2 threshold from UGX 235,000 to a hypothetical new threshold.
4. Saves configuration.
5. Runs a test payroll calculation to confirm the new band applies.

*Expected result:* Finance Director completes the configuration change independently. No developer access or code change required. Test payroll calculation uses the new band correctly. (DC-002 — configuration over code.) | **P1**

---

**TC-NFR-008** | NFR | Peak production load: 140 MT/day simulation — no errors

*Preconditions:* Staging environment. JMeter load profile simulating 140 MT/day peak scenario: 1,071 agents active, concurrent POS transactions, stock queries, remittance submissions.

*Test steps:*
1. Run peak load simulation for 30 minutes.
2. Monitor: error rate, response times, server resources.

*Expected result:* Zero HTTP 500 errors. Zero timeouts. Response times within thresholds. Server resources stable (CPU < 85%, memory < 90%). This test satisfies Phase 7 load testing requirement. | **P1**

---

**TC-NFR-009** | NFR | Offline sync completes within 60 seconds for typical day's transactions

*Preconditions:* Sales Agent App with 200 offline transactions (typical day's volume for an active agent).

*Test steps:*
1. Record 200 transactions offline on the Sales Agent App.
2. Restore connectivity.
3. Start timer from reconnect event.
4. Wait for sync complete notification.

*Expected result:* All 200 transactions synced to server within 60 seconds. Zero transactions lost. No duplicates. | **P1**

---

**TC-NFR-010** | NFR | Data sovereignty: no data transmitted to external servers except EFRIS, MoMo, Airtel

*Preconditions:* Network traffic monitoring tool (e.g., Wireshark) configured on staging server network interface.

*Test steps:*
1. Monitor all outbound network traffic from the ERP server for 24 hours during normal operation.
2. Identify all external IP addresses contacted.

*Expected result:* Outbound connections only to: URA EFRIS endpoint, MTN MoMo API endpoint, Airtel Money API endpoint, SMTP server (for email notifications), and GitHub (for CI/CD). No BIRDC data transmitted to any other external server. (DC-006 — data sovereignty.) | **P1**

---
