# 4 Specific Requirements — Non-Functional

All non-functional requirements specify measurable thresholds per IEEE Std 830-1998 Section 5.3.3. Vague qualifiers are replaced with IEEE-982.1 compatible metrics.

---

## 4.1 Performance

#### NFR-PERF-001: API Response Time (CRUD)

**Phase:** 1

The system shall process CRUD operations (create, read, update, delete) on all API endpoints with a P95 response time $\leq$ 500ms under 1,000 concurrent authenticated users.

**Verifiability:** Execute a load test with 1,000 concurrent users performing mixed CRUD operations for 10 minutes. Measure P95 response time. Pass criterion: P95 $\leq$ 500ms.

---

#### NFR-PERF-002: API Response Time (Reports)

**Phase:** 1

The system shall generate dashboard aggregation queries and report endpoints with a P95 response time $\leq$ 2,000ms under 1,000 concurrent users.

**Verifiability:** Execute a load test with 1,000 concurrent users requesting dashboard and report endpoints. Pass criterion: P95 $\leq$ 2,000ms.

---

#### NFR-PERF-003: Mobile App Cold Start

**Phase:** 1

The Android app shall complete cold start (from tap to interactive home screen) in $\leq$ 3 seconds on a reference device (Tecno Spark, 2GB RAM, Android 11).

**Verifiability:** Perform 10 cold starts on the reference device. Measure time from launcher tap to interactive home screen. Pass criterion: average $\leq$ 3 seconds, no single start exceeding 5 seconds.

---

#### NFR-PERF-004: Screen Transitions

**Phase:** 1

The mobile app shall complete screen transitions (navigation between screens) in $\leq$ 300ms on the reference device.

**Verifiability:** Navigate between 10 different screens on the reference device. Measure transition time for each. Pass criterion: all transitions $\leq$ 300ms.

---

#### NFR-PERF-005: Offline Operation Zero Degradation

**Phase:** 1

The system shall provide zero degradation in core functionality (create, read, update, delete for farms, crops, livestock, finances, tasks) with no internet connectivity. Response times for local operations shall be $\leq$ 200ms.

**Verifiability:** Enable airplane mode. Perform all CRUD operations. Measure response times. Pass criterion: all operations succeed; all response times $\leq$ 200ms.

---

#### NFR-PERF-006: Background Sync Latency

**Phase:** 1

The system shall begin processing queued records within 30 seconds of connectivity detection.

**Verifiability:** Queue 10 records offline. Enable connectivity. Measure time from connectivity detection to first sync request. Pass criterion: $\leq$ 30 seconds.

---

#### NFR-PERF-007: GPS Boundary Accuracy

**Phase:** 2

The GPS polygon capture shall achieve positional accuracy within 5 metres of the actual boundary on a consumer-grade Android device.

**Verifiability:** Walk a known boundary of a surveyed plot. Compare captured polygon coordinates with surveyed coordinates. Pass criterion: maximum deviation $\leq$ 5 metres at any vertex.

---

## 4.2 Availability

#### NFR-AVAIL-001: Web Dashboard Uptime

**Phase:** 1

The web dashboard shall maintain 99.5% uptime per calendar month, allowing a maximum of 3.6 hours unplanned downtime per month.

**Verifiability:** Monitor uptime using an external monitoring service (e.g., UptimeRobot) for 3 consecutive months. Pass criterion: each month $\geq$ 99.5% uptime.

---

#### NFR-AVAIL-002: API Uptime

**Phase:** 1

The REST API shall maintain 99.5% uptime per calendar month.

**Verifiability:** Monitor API health endpoint using external monitoring. Pass criterion: each month $\geq$ 99.5% uptime.

---

#### NFR-AVAIL-003: Planned Maintenance Windows

**Phase:** 1

Planned maintenance shall occur only during the designated window: Sundays 02:00-04:00 East Africa Time (EAT). Users shall receive 48-hour advance notice via in-app notification and email.

**Verifiability:** Schedule a maintenance event. Verify notification is sent 48 hours in advance. Verify maintenance executes within the Sunday 02:00-04:00 EAT window. Pass criterion: no planned maintenance outside the window; notification delivered $\geq$ 48 hours before.

---

#### NFR-AVAIL-004: IoT Gateway Uptime

**Phase:** 3

The IoT Gateway (WebSocket server for Jaguza/sensor data) shall maintain 99.0% uptime per calendar month, with sensor data buffered and retried on temporary failures.

**Verifiability:** Monitor IoT gateway uptime. Simulate a 30-minute outage and verify buffered data is processed on recovery. Pass criterion: monthly uptime $\geq$ 99.0%.

---

#### NFR-AVAIL-005: Camera Proxy Uptime

**Phase:** 3

The camera proxy service (mediamtx/ffmpeg) shall maintain 99.0% uptime per calendar month. On proxy failure, cached snapshots shall be displayed instead of live stream.

**Verifiability:** Monitor camera proxy uptime. Simulate proxy failure — verify cached snapshot displays. Pass criterion: monthly uptime $\geq$ 99.0%.

---

## 4.3 Security

#### NFR-SEC-001: OWASP Top 10 Compliance

**Phase:** 1

The system shall comply with OWASP Top 10 (2021) for all web and API endpoints: A01 (Broken Access Control), A02 (Cryptographic Failures), A03 (Injection), A04 (Insecure Design), A05 (Security Misconfiguration), A06 (Vulnerable Components), A07 (Authentication Failures), A08 (Data Integrity Failures), A09 (Logging Failures), A10 (SSRF).

**Verifiability:** Conduct an OWASP ZAP or Burp Suite scan against all endpoints. Pass criterion: zero high-severity findings for any OWASP Top 10 category.

---

#### NFR-SEC-002: Encryption in Transit

**Phase:** 1

All data transmitted between clients and server shall be encrypted using TLS 1.2 or higher. Connections using TLS 1.1 or lower shall be rejected.

**Verifiability:** Use `ssllabs.com` or `testssl.sh` to scan the API endpoint. Pass criterion: TLS 1.2+ only; no support for TLS 1.1 or lower; rating A or higher.

---

#### NFR-SEC-003: Encryption at Rest

**Phase:** 1

Sensitive data (farm GPS boundaries, financial records, IoT credentials) shall be encrypted at rest on the server. Mobile local databases shall use SQLCipher (Android) or encrypted SwiftData (iOS).

**Verifiability:** Inspect the database encryption configuration. Attempt to read the mobile database file directly without the app — verify data is not readable. Pass criterion: sensitive fields are encrypted; direct file access returns unintelligible data.

---

#### NFR-SEC-004: Session Management

**Phase:** 1

Web sessions shall timeout after 30 minutes of inactivity (configurable per tenant). JWT tokens shall expire after 24 hours with a refresh token mechanism. Refresh tokens shall be single-use and expire after 7 days.

**Verifiability:** Login to web dashboard and remain inactive for 31 minutes — verify session expires. Issue a JWT and wait 25 hours — verify it is rejected. Use a refresh token — verify a new access token is issued and the old refresh token is invalidated.

---

#### NFR-SEC-005: Password Policy

**Phase:** 1

The system shall enforce a minimum password length of 8 characters with complexity requirements (at least 1 uppercase, 1 lowercase, 1 digit).

**Verifiability:** Attempt registration with "pass" — verify rejection. Attempt with "Password1" — verify acceptance. Pass criterion: passwords meeting the policy are accepted; others are rejected with clear error messages.

---

#### NFR-SEC-006: Rate Limiting

**Phase:** 1

The system shall enforce rate limits of 100 requests per minute per authenticated user and 20 requests per minute for unauthenticated endpoints.

**Verifiability:** Send 101 requests in 60 seconds as an authenticated user — verify the 101st returns HTTP 429. Send 21 requests to a public endpoint — verify the 21st returns HTTP 429.

---

#### NFR-SEC-007: Multi-Tenant Data Isolation

**Phase:** 1

The system shall ensure complete data isolation between tenants at the database query level. No API endpoint shall return data belonging to a different tenant, regardless of parameter manipulation.

**Verifiability:** As Tenant A, attempt to access Tenant B's resources by manipulating resource IDs in API requests. Pass criterion: all such attempts return 403 Forbidden or 404 Not Found. Run a penetration test focused on IDOR (Insecure Direct Object Reference).

---

## 4.4 Data Integrity

#### NFR-DATA-001: No Data Loss (Offline Sync)

**Phase:** 1

All records created offline shall eventually sync successfully to the server, or shall be flagged for manual resolution. Zero records shall be silently lost.

**Verifiability:** Create 100 records offline. Sync to server. Verify all 100 records exist on the server. Simulate a sync failure for 5 records — verify they are flagged for manual resolution.

---

#### NFR-DATA-002: Conflict Resolution Logging

**Phase:** 1

Every sync conflict (same record modified on 2 devices) shall be logged with both versions preserved. The farmer shall be able to review conflict history.

**Verifiability:** Create a conflict by modifying the same record on 2 devices. Verify both versions are preserved in the conflict log. Verify the conflict log is accessible to the farmer.

---

#### NFR-DATA-003: Audit Trail

**Phase:** 1

All create, update, and delete operations shall be logged with: user ID, timestamp, action type, entity type, entity ID, and previous values (for updates and deletes).

**Verifiability:** Create, update, and delete a farm record. Query the audit log. Verify entries exist for all 3 operations with user, timestamp, action, and previous values for the update and delete.

---

#### NFR-DATA-004: Financial Transaction Immutability

**Phase:** 1

Income and expense records shall not be deletable after 30 days of creation. Records older than 30 days can only be voided with a reversal entry, preserving the original record.

**Verifiability:** Create an expense record. Wait 31 days (or simulate the timestamp). Attempt to delete — verify deletion is blocked. Void the record — verify the original is preserved and a reversal entry is created.

---

#### NFR-DATA-005: Backup Frequency

**Phase:** 1

The system shall perform automated daily database backups with 30-day retention. Point-in-time recovery shall be possible to any point within the past 7 days.

**Verifiability:** Verify daily backups exist for the past 30 days. Perform a point-in-time recovery to 3 days ago. Verify data matches the state at that point.

---

## 4.5 Usability

#### NFR-USE-001: Core Operation Tap Count

**Phase:** 1

Core farm operations (record activity, log income/expense, mark task complete) shall be achievable in 3 taps or fewer from the home screen on mobile.

**Verifiability:** Measure the tap count for each core operation starting from the home screen. Pass criterion: $\leq$ 3 taps for each operation.

---

#### NFR-USE-002: Touch Target Size

**Phase:** 1

All interactive elements on mobile shall have a minimum touch target size of 48x48dp, compliant with WCAG 2.1 AA.

**Verifiability:** Inspect all interactive elements in the app using Layout Inspector (Android) or Accessibility Inspector (iOS). Pass criterion: all touch targets $\geq$ 48x48dp.

---

#### NFR-USE-003: Font Size

**Phase:** 1

Body text on mobile shall use a minimum font size of 14sp. The app shall respect system font scaling settings.

**Verifiability:** Inspect body text font sizes using Layout Inspector. Set system font scale to 1.5x — verify text scales accordingly. Pass criterion: body text $\geq$ 14sp at default scaling.

---

#### NFR-USE-004: Contrast Ratio

**Phase:** 1

Text elements shall maintain a minimum contrast ratio of 4.5:1 against their background, compliant with WCAG AA.

**Verifiability:** Measure contrast ratios for all text elements using an accessibility colour contrast analyser. Pass criterion: all ratios $\geq$ 4.5:1.

---

#### NFR-USE-005: Language Switching

**Phase:** 1

Language switching shall be instant (no app restart required). All UI text shall update immediately upon language change.

**Verifiability:** Switch language from English to Luganda. Verify all visible text updates without app restart. Measure the switch time. Pass criterion: switch completes in $\leq$ 1 second with no restart.

---

#### NFR-USE-006: Onboarding Time

**Phase:** 1

A new farmer shall be able to register and record their first farm activity within 5 minutes without external help.

**Verifiability:** Conduct a usability test with 5 farmers matching the Nakato Grace persona (P.7 education, low tech comfort). Measure time from opening the app to completing first activity recording. Pass criterion: 4 out of 5 complete within 5 minutes.

---

#### NFR-USE-007: Error Messages

**Phase:** 1

All error messages shall be clear, actionable, and displayed in the user's selected language. Technical error codes shall never be displayed to end users.

**Verifiability:** Trigger 10 different error conditions (validation, network, permission, conflict). Verify each message is in the user's language, describes the problem, and suggests an action. Verify no HTTP status codes or stack traces are displayed.

---

## 4.6 Scalability

#### NFR-SCALE-001: Tenant Capacity

**Phase:** 1

The database shall support 10,000 tenants with an average of 500 records each (5,000,000 total records) without query degradation exceeding 20% compared to a 100-tenant baseline.

**Verifiability:** Load test with 10,000 tenants and 500 records each. Measure P95 query response times. Compare to a 100-tenant baseline. Pass criterion: degradation $\leq$ 20%.

---

#### NFR-SCALE-002: Photo Compression

**Phase:** 1

Photos shall be compressed to a maximum file size of 512KB before upload, regardless of original size.

**Verifiability:** Upload photos of 1MB, 3MB, and 8MB. Verify all are compressed to $\leq$ 512KB before network transmission. Verify visual quality remains acceptable (no visible artefacts at screen resolution).

---

#### NFR-SCALE-003: APK Size

**Phase:** 1

The base Android APK (excluding add-on modules) shall not exceed 30MB.

**Verifiability:** Build a release APK. Measure file size. Pass criterion: $\leq$ 30MB.

---

#### NFR-SCALE-004: Sync Payload Size

**Phase:** 1

Individual sync batches shall not exceed 1MB to accommodate 2G connections.

**Verifiability:** Queue 50 records for sync. Measure the total payload size per sync batch. Pass criterion: each batch $\leq$ 1MB.

---

## 4.7 Accessibility

#### NFR-ACC-001: Screen Reader Compatibility

**Phase:** 1

The web dashboard shall be compatible with screen readers (NVDA, VoiceOver) via proper ARIA labels on all interactive elements.

**Verifiability:** Navigate the web dashboard using NVDA (Windows) and VoiceOver (macOS). Verify all interactive elements are announced correctly. Pass criterion: all buttons, links, form fields, and data tables are screen-reader-accessible.

---

#### NFR-ACC-002: High Contrast Mode

**Phase:** 1

A high contrast mode shall be available on the web dashboard and mobile apps, increasing contrast ratios to $\geq$ 7:1 for all text elements.

**Verifiability:** Enable high contrast mode. Measure contrast ratios for all text elements. Pass criterion: all ratios $\geq$ 7:1.

---

#### NFR-ACC-003: Large Text Mode

**Phase:** 1

The mobile app shall respect system font scaling (up to 2x) without layout breakage. All text shall remain readable and no content shall be clipped.

**Verifiability:** Set system font scale to 2x. Navigate all screens. Verify no text is clipped, overlapping, or breaking out of containers. Pass criterion: all screens render correctly at 2x scaling.

---

#### NFR-ACC-004: No Colour-Only Information

**Phase:** 1

All status indicators shall include text labels or icons alongside colour. Colour shall not be the sole means of conveying information.

**Verifiability:** Enable greyscale mode on the device. Navigate all screens. Verify all status indicators are distinguishable without colour (via text labels or icons). Pass criterion: all statuses are identifiable without colour.

---
