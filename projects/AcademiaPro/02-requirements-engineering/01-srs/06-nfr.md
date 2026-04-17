# Non-Functional Requirements — Academia Pro SRS

---

#### EDU-NFR-001: Student Record Confidentiality
The system shall restrict access to student education records to authorised users whose role grants a legitimate educational interest in the target student. No student record shall be disclosed to a third party without documented parental or student consent or a lawful basis under the Uganda Personal Data Protection and Privacy Act 2019.

**Verifiability:** Authenticate as a role without educational access rights to a target student; issue GET /students/{uid}. The system shall return HTTP 403 and write an audit log entry containing: user_id, tenant_id, timestamp, student_uid, outcome=DENIED. Retrieve the audit log and verify all five fields are present.

---

#### EDU-NFR-002: Web Accessibility
The system shall conform to WCAG 2.1 Level AA for all web portal interfaces (student, parent, teacher, bursar, owner, head teacher). All interactive elements shall be keyboard-operable. All non-text content shall carry a text alternative. All text elements shall meet a minimum colour contrast ratio of 4.5:1.

**Verifiability:** Run Axe CLI against all portal pages in CI; the pipeline shall fail on any WCAG 2.1 AA violation. Conduct a manual keyboard navigation walkthrough of the critical path (login → dashboard → attendance entry → mark entry → fee recording) without using a pointing device.

---

#### EDU-NFR-003: Minor Data Protection
The system shall not disclose personal data of enrolled students (who are presumed minors under 18 per Uganda school context) to any third party without the recorded consent of the student's linked parent or guardian.

**Verifiability:** Attempt to trigger a third-party data share (e.g., EMIS export, CSV download) for a student with no recorded parental consent record. The system shall block the export and log the attempt. Verify the audit log entry.

---

#### EDU-NFR-004: Student Record Retention
The system shall retain student education records and associated audit logs for a minimum of 7 years following the student's last active enrollment date. The system shall not permit permanent deletion of any student record within the 7-year retention window.

**Verifiability:** Attempt to permanently delete the record of a student whose last active enrollment ended fewer than 7 years ago. The system shall reject the deletion with HTTP 422 and a message citing the retention policy. Verify the attempted deletion is logged.

---

#### EDU-NFR-005: Availability During Examinations
The system shall maintain 99.9% monthly uptime ($\leq$ 0.73 hours downtime per month) for the Examinations, Gradebook, and Attendance modules during examination periods as declared in each school's academic calendar configuration.

**Verifiability:** Monitor the three modules via Uptime Robot during the examination window. Calculate $Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$. Result must be $\geq$ 99.9%. Confirm no scheduled maintenance was performed during the window.

---

## Uganda-Specific Non-Functional Requirements

#### UG-NFR-001: UNEB Grading Engine Accuracy
The system's automated grade computation for PLE, UCE (O-Level), and UACE (A-Level) shall produce results 100% identical to manual computation using UNEB's published grading rules, verified against a test dataset of at least 100 sample candidate results provided by UNEB.

**Verifiability:** Load UNEB sample mark sheet data into a test tenant. Execute the grading engine. Compare output with the expected results computed manually from UNEB's published tables. Pass criterion: 0 discrepancies across all test candidates for all three examination types.

#### UG-NFR-002: EMIS Export Compliance
The system's EMIS export shall produce student and teacher data files that validate without error against the current MoES EMIS data dictionary.

**Verifiability:** Generate EMIS export from a test tenant with 500 enrolled students and 30 staff. Validate the output file against the MoES-published EMIS XML schema. Zero validation errors.

#### UG-NFR-003: Uganda 3-Term Calendar Enforcement
For tenants with locale set to Uganda, the system shall accept exactly 3 non-overlapping terms per academic year. Attempts to configure more, fewer, or overlapping terms shall be rejected at the API layer.

**Verifiability:** POST /academic-years with 4 terms for a Uganda-locale tenant → HTTP 422. POST /academic-years with 2 overlapping term date ranges → HTTP 422. POST /academic-years with 3 non-overlapping terms → HTTP 201.

#### UG-NFR-004: Offline Attendance and Mark Entry
The system's teacher-facing interfaces (PWA and Android app) shall support offline entry of daily attendance and exam marks. Offline entries shall be queued locally and synced to the server within 5 minutes of network restoration.

**Verifiability:** On a test device, disable network. Enter 30 attendance records and 15 mark entries. Restore network. Within 5 minutes, verify all 45 records appear in the server database with correct tenant_id, student_uid, class_id, and timestamps.

#### UG-NFR-005: Multi-Tenant Data Isolation
The system shall enforce complete data isolation between tenants at the database query layer. No authenticated user of Tenant A shall be able to read, write, or infer any data belonging to Tenant B by any means (direct API call, URL manipulation, or indirect reference).

**Verifiability:** Create two tenants (Tenant A, Tenant B) with separate student records. Authenticate as a Tenant A user. Attempt to access Tenant B's student records by substituting tenant_id or student_uid values in API requests. All cross-tenant requests shall return HTTP 403. Verify database query logs show every query includes a `tenant_id = ?` predicate.

#### UG-NFR-006: Fee Payment Idempotency
The system shall not create more than one fee payment receipt for the same external payment reference, regardless of how many times the payment notification is received.

**Verifiability:** Send the same SchoolPay webhook payload 3 times in rapid succession. Verify exactly 1 receipt record is created in the database. Verify the second and third requests return `{"status": "duplicate", "original_receipt_id": "..."}` with HTTP 200.

#### UG-NFR-007: API Response Time
The system's REST API shall respond to standard CRUD requests within 500 ms at the 95th percentile under a load of 200 concurrent requests. Report card generation for a single student shall complete within 3,000 ms at the 95th percentile.

**Verifiability:** Execute a k6 load test with 200 virtual users issuing mixed CRUD requests for 5 minutes. P95 response time must be ≤ 500 ms for standard endpoints and ≤ 3,000 ms for report card generation. Results must be captured and stored in the test report.

#### UG-NFR-008: Data Encryption
All personally identifiable student data shall be encrypted at rest using AES-256. All data in transit between clients and the server shall use TLS 1.3. TLS versions below 1.2 shall not be accepted.

**Verifiability:** Inspect database storage volume encryption configuration — AES-256 must be active. Run `nmap --script ssl-enum-ciphers` against the production server; TLS 1.0 and 1.1 must not appear in the accepted cipher list. Connect via a TLS 1.3 client and confirm successful handshake.

---

## AI Module Non-Functional Requirements

> The following NFRs apply only to tenants with an active AI module (`tenant_ai_modules.status = 'active'`). All measurements are taken from the user's perspective at the application layer.

#### AI-NFR-001: AI Insights Panel Load Time

The system shall display a skeleton loader for the AI Insights panel (Zone 3 of the analytics dashboard) within 500 ms of page load. The full AI Insights content shall appear within 8,000 ms of page load at the 95th percentile under normal operating conditions.

**Verifiability:** Load the Owner dashboard for a tenant with all AI Insights features enabled. Start timing at the HTTP response. Measure: (a) skeleton visible within 500 ms; (b) full panel populated within 8,000 ms. Run under k6 with 50 concurrent users. P95 must be ≤ 8,000 ms.

---

#### AI-NFR-002: Token Ledger Write Latency

Writing a row to `ai_usage_log` after each AI API call shall complete within 200 ms at the 95th percentile. This write must complete before the API response is returned to the caller, ensuring the ledger is never out of sync with actual consumption.

**Verifiability:** Instrument the `AIMeteredClient` write step. Issue 1,000 successive AI calls in a load test. P95 ledger write latency must be ≤ 200 ms. Confirm zero calls where the HTTP response preceded the ledger write.

---

#### AI-NFR-003: AI Service Availability

The AI Service (the internal component that wraps the external LLM API) shall maintain 99.5% monthly availability. When the primary provider (Claude API) is unavailable, the system shall fail over to the secondary provider within 30 seconds without requiring manual intervention.

**Verifiability:** Simulate primary provider outage by returning HTTP 503 from the mock Anthropic endpoint. Measure time from first failure to first successful call via the secondary provider. Must be ≤ 30 seconds. Uptime over a 30-day test period (with 2 simulated outages of 1 hour each) must remain ≥ 99.5%.

---

#### AI-NFR-004: Batch Job Completion Window

AI batch jobs (at-risk student scoring, fee default prediction, weekly briefing) shall complete processing for all eligible tenants before 07:00 EAT on the scheduled day. For a platform with 500 active tenants and an average of 300 students per tenant, the batch pipeline shall process all tenants within 60 minutes of the 06:00 EAT job start.

**Verifiability:** Seed 500 test tenants each with 300 students and AI features enabled. Trigger the Monday batch job at 06:00 EAT. Confirm all `nlp_results` rows are written and all in-app notifications are delivered by 07:00 EAT. Monitor job queue depth via Laravel Horizon dashboard.

---

#### AI-NFR-005: PII Scrubbing Completeness

The `PIIScrubber` component shall remove 100% of Uganda-specific personally identifiable information from any string before it is dispatched to an external AI API. Specifically: National Identification Numbers (NIN format CM748383480F83), Ugandan mobile numbers (format +256xxxxxxxxx or 07xxxxxxxx), email addresses, and names matched against the `guardians` and `users` tables for the active tenant.

**Verifiability:** Construct a test string containing: 1 NIN, 1 mobile number, 1 email address, and 3 parent names drawn from the test tenant's `guardians` table. Run `PIIScrubber::scrub()`. Assert: output contains none of the 6 identifiers. Run 1,000 test cases. Zero false negatives permitted.

---

#### AI-NFR-006: AI Output Validation

The system shall validate the JSON structure of every AI API response before writing any data to `nlp_results` or `ai_usage_log`. Malformed JSON, missing required fields, or out-of-range values shall be rejected and logged as `outcome = 'error'` in `ai_audit_log` without writing partial data to any business table.

**Verifiability:** Mock the LLM to return: (a) invalid JSON; (b) JSON missing the `risk_level` field; (c) JSON with `risk_level = 'unknown'` (invalid enum). In all 3 cases: no row written to `nlp_results`; `ai_audit_log.outcome = 'error'`; caller receives a graceful fallback response (not an exception stack trace).

---

#### AI-NFR-007: Budget Enforcement Latency

The budget enforcement check (`BudgetGuard::check()`) shall complete within 50 ms at the 95th percentile so that it does not add perceptible latency to the user's AI request. The guard reads from `ai_usage_monthly` which is a cached pre-aggregated table (TTL = 5 minutes in Redis).

**Verifiability:** Issue 500 successive budget guard checks against a warmed Redis cache. P95 latency must be ≤ 50 ms. Simulate cache miss (Redis cold): P95 must be ≤ 200 ms (database read fallback).

---

#### AI-NFR-008: AI Audit Log Retention

The `ai_audit_log` table shall retain all records for a minimum of 7 years from the date of the AI call, aligned with the Uganda DPPA 2019 audit trail requirements and the general academic record retention policy. No application-layer route shall expose `DELETE` or `UPDATE` operations on this table.

**Verifiability:** Attempt `DELETE /api/v1/ai-audit-log/{id}` via any authenticated role → HTTP 405. Attempt `DELETE FROM ai_audit_log WHERE id = 1` at the database layer → MySQL trigger fires `SIGNAL SQLSTATE '45000'`. Confirm records created 7 years ago are still queryable (test via synthetic aged data in CI).
