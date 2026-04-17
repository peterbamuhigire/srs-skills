---
title: "Non-Functional Test Cases — Performance, Offline, Security, Mobile, Cross-Platform"
document-id: "MADUUKA-TC-NFR-001"
version: "1.0"
date: "2026-04-05"
standard: "IEEE Std 829-2008"
---

# Non-Functional Test Cases: Performance, Offline, Security, Mobile, Cross-Platform Parity

**Document ID:** MADUUKA-TC-NFR-001
**Version:** 1.0
**Date:** 2026-04-05
**Parent Plan:** MADUUKA-TP-001

---

## NF-001: Performance Tests

All performance thresholds are sourced from MADUUKA-TS-001 Section 3.6. A result that exceeds any threshold constitutes an S1 defect for POS-critical paths and an S2 defect for all others.

---

**TC-NFR-001**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-001 |
| FR Reference | FR-POS-001 |
| Title | Verify product search returns results within 500 ms at last keystroke under 10,000 SKU catalogue |
| Preconditions | 1. The product catalogue contains exactly 10,000 SKU records. 2. The staging environment is deployed with production-equivalent MySQL configuration. 3. Tester is authenticated as Cashier on either Android or Web. |
| Test Steps | 1. Open the POS search field. 2. Type a 4-character search term that matches at least 5 products. 3. At the moment of the final keystroke, start a timer (or use Android Profiler / browser performance timeline). 4. Stop the timer when the results list first renders. 5. Repeat 5 times and record each result. |
| Expected Result | All 5 measurements show results rendered in ≤ 500 ms from the final keystroke. The results list contains matching products. |
| Pass Criteria | P95 of 5 measurements ≤ 500 ms; no individual measurement exceeds 1,000 ms. |
| Priority | Critical |

---

**TC-NFR-002**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-002 |
| FR Reference | FR-POS-002 |
| Title | Verify barcode scan adds product to cart within 1 second on Android |
| Preconditions | 1. Android device or hardware-capable emulator: API ≥ 26, camera enabled. 2. A physical or printed EAN-13 barcode is available for a product in the catalogue. 3. A POS session is open. |
| Test Steps | 1. Tap the camera icon to open the barcode scanner. 2. Point the camera at the EAN-13 barcode. 3. Note the time of the barcode decode event (Android Profiler `TRACE` marker or log timestamp). 4. Note the time when the cart line item appears in the UI. 5. Repeat 5 times. |
| Expected Result | All 5 measurements show the cart updated within ≤ 1 second of the barcode decode event. |
| Pass Criteria | P95 of 5 measurements ≤ 1,000 ms. |
| Priority | High |

---

**TC-NFR-003**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-003 |
| FR Reference | FR-POS-003 |
| Title | Verify category filter update renders within 300 ms |
| Preconditions | 1. The product catalogue contains products in at least 5 categories. 2. A POS session is open. 3. The product grid view is active. |
| Test Steps | 1. Tap a category filter button. 2. Measure the time from tap to grid re-render completion using Android Profiler (Android) or browser performance timeline (Web). 3. Repeat 5 times across different category selections. |
| Expected Result | All 5 measurements show the grid updated in ≤ 300 ms. |
| Pass Criteria | P95 ≤ 300 ms. |
| Priority | High |

---

**TC-NFR-004**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-004 |
| FR Reference | FR-POS-026, FR-POS-027 |
| Title | Verify API P95 response time is at or below 500 ms under 50 concurrent virtual users |
| Preconditions | 1. k6 or Apache JMeter is installed and configured. 2. The staging API is deployed. 3. Test data: 10,000 products and 50 customers are seeded. |
| Test Steps | 1. Configure the load test script with 50 virtual users. 2. Scenario: each virtual user performs a product search and a cart submission in a loop for 5 minutes. 3. Execute the load test. 4. Collect the P95 response time from the k6/JMeter report. |
| Expected Result | The P95 response time for product search (`GET /api/v1/products?search=`) and cart submission (`POST /api/v1/sales`) endpoints ≤ 500 ms. The P99 response time ≤ 1,000 ms. 0 HTTP 5xx responses during the test. |
| Pass Criteria | P95 ≤ 500 ms; P99 ≤ 1,000 ms; HTTP 5xx error rate = 0%. |
| Priority | Critical |

---

**TC-NFR-005**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-005 |
| FR Reference | FR-POS-026, FR-POS-027 |
| Title | Verify end-to-end POS sale completes in at or below 3 seconds on the target Android device profile |
| Preconditions | 1. Android device: UGX 250,000-class equivalent (2 GB RAM, ARM32, Android 8.0), connected to a 3G network (or network throttled to 3G speeds: 1.5 Mbps down / 768 Kbps up, 100 ms latency). 2. A POS session is open with opening float entered. 3. One product is already in the cart. |
| Test Steps | 1. On the payment screen, tap "Confirm Payment" (cash payment, exact amount). 2. Start the timer at the "Confirm Payment" tap event. 3. Stop the timer when the receipt screen is fully rendered and the receipt number is visible. 4. Record the elapsed time. 5. Repeat 5 times. |
| Expected Result | All 5 measurements record a sale completion time ≤ 3 seconds from "Confirm Payment" tap to receipt screen display. |
| Pass Criteria | P95 of 5 measurements ≤ 3,000 ms. |
| Priority | Critical |

---

**TC-NFR-006**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-006 |
| FR Reference | FR-POS-027 |
| Title | Verify offline sync endpoint processes at least 100 sync payloads per minute per tenant |
| Preconditions | 1. k6 or JMeter configured to send authenticated sync payloads to `POST /api/v1/sales/sync`. 2. Each payload is a valid pending sale with a unique `idempotency_key`. 3. The test tenant's database is clean. |
| Test Steps | 1. Send 100 sync payloads over 60 seconds in a burst (simulating reconnect after offline session). 2. After 60 seconds, count the number of sale records created in the database for this tenant. |
| Expected Result | All 100 sync payloads are accepted and 100 sale records are created within 60 seconds. |
| Pass Criteria | 100 sale records created within 60 seconds; 0 HTTP 5xx errors; 0 duplicate records. |
| Priority | High |

---

**TC-NFR-007**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-007 |
| FR Reference | FR-DASH-001 |
| Title | Verify web dashboard loads all KPI cards within 4 seconds on 3G equivalent connection |
| Preconditions | 1. Web browser with network throttled to 3G equivalent (1.5 Mbps down, 100 ms latency) using browser DevTools. 2. The staging dashboard API is live. 3. Tester is authenticated as Owner. |
| Test Steps | 1. Open the browser performance timeline. 2. Navigate to the dashboard. 3. Measure the time from navigation start to the moment all 4 KPI card values are rendered (not just placeholders). |
| Expected Result | All 4 KPI cards (Today's Revenue, Transaction Count, Outstanding Credit, Cash Position) display their values within ≤ 4 seconds of navigation start. |
| Pass Criteria | All 4 KPI values rendered in ≤ 4,000 ms on the throttled connection. |
| Priority | High |

---

## NF-002: Offline Resilience Tests

The following tests verify the 10 core modules under the constraint of no internet connectivity. Offline-capable features are those served by local Room cache on Android.

**Offline-capable (full functionality without internet):** POS sale processing (F-001), product catalogue browse (F-002 read), customer list and credit balance view (F-003 read), dashboard KPI display using cached data (F-009).

**Requires internet (graceful degradation only):** MTN MoMo / Airtel Money payments (show error, allow switch), receipt delivery via WhatsApp/SMS, dashboard auto-refresh, report generation from server data, HR/payroll, supplier management.

---

**TC-NFR-008**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-008 |
| FR Reference | FR-POS-026, FR-POS-027, BR-009 |
| Title | Verify all 10 offline sales in an airplane-mode sequence are recovered after sync with no losses |
| Preconditions | 1. A POS session is open on Android with a populated product catalogue cached in Room. 2. Android device: API ≥ 26, 2 GB RAM. |
| Test Steps | 1. Enable airplane mode. 2. Process exactly 10 sales (varying products, cash payment). 3. After the 10th sale, note the total sum of all 10 sale amounts. 4. Re-enable network connectivity. 5. Wait up to 30 seconds. 6. Query `GET /api/v1/sales` filtered to the current session. 7. Count the number of records returned and sum the amounts. |
| Expected Result | Exactly 10 sale records appear on the server. The sum of the server-side sale amounts equals the sum calculated in step 3. All 10 records have the correct `franchise_id`. 0 sales are lost. Local Room records show `sync_status = "synced"` for all 10. |
| Pass Criteria | Server record count = 10; server amount sum = offline amount sum; 0 losses; local sync_status = "synced". |
| Priority | Critical |

---

**TC-NFR-009**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-009 |
| FR Reference | FR-POS-026 |
| Title | Verify POS cashier can browse and search the product catalogue while offline |
| Preconditions | 1. A POS session is open on Android. 2. Product catalogue (100+ products) has been loaded while online. 3. Airplane mode is now enabled. |
| Test Steps | 1. Type a product name in the POS search field while in airplane mode. 2. Observe search results. 3. Add the found product to the cart. |
| Expected Result | Search results are displayed from the local Room cache within ≤ 500 ms. Products can be added to the cart. No connectivity error is displayed. |
| Pass Criteria | Search results displayed in ≤ 500 ms from cached data; product added to cart; no error message related to offline state. |
| Priority | Critical |

---

**TC-NFR-010**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-010 |
| FR Reference | FR-POS-026 |
| Title | Verify no partial sale record exists after a connectivity interruption mid-payment |
| Preconditions | 1. A POS session is open on Android. 2. A cart with 1 item (UGX 20,000) is active. 3. A mechanism to interrupt connectivity mid-operation is prepared (automated network kill or manual airplane mode toggle at exact timing). |
| Test Steps | 1. Tap "Confirm Payment" (cash). 2. Immediately enable airplane mode (within 1 second of tap). 3. Wait 10 seconds. 4. Observe the application state. 5. Check the local Room database for any partial sale records. |
| Expected Result | The application shows either: (a) a completed sale receipt (the sale was committed locally before sync was attempted), or (b) the payment screen with an error indicating the sale was not completed — prompting the cashier to retry. In no case does a partial sale record exist in Room with an inconsistent state (e.g., payment deducted but stock not decremented). |
| Pass Criteria | Either a complete sale record exists or no sale record exists; 0 partial/inconsistent records in Room. |
| Priority | Critical |

---

## NF-003: Security Tests

---

**TC-NFR-011**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-011 |
| FR Reference | FR-SET-011 |
| Title | Verify access token expires after exactly 15 minutes and returns HTTP 401 on subsequent requests |
| Preconditions | 1. A valid access token is issued with a 15-minute expiry. 2. The system clock on the test environment is controllable (or the test waits the full 15 minutes). |
| Test Steps | 1. Authenticate and obtain an access token. Note the issue time T. 2. At T + 14 minutes 50 seconds, send `GET /api/v1/products` with the access token. 3. At T + 15 minutes 5 seconds, send `GET /api/v1/products` with the same access token. |
| Expected Result | The request at T + 14:50 returns HTTP 200. The request at T + 15:05 returns HTTP 401 with error code `TOKEN_EXPIRED`. |
| Pass Criteria | T + 14:50 request = HTTP 200; T + 15:05 request = HTTP 401 with `TOKEN_EXPIRED`. |
| Priority | Critical |

---

**TC-NFR-012**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-012 |
| FR Reference | FR-SET-011 |
| Title | Verify refresh token rotation: replaying a used refresh token returns HTTP 401 |
| Preconditions | 1. A valid refresh token RT-001 exists for a test user. |
| Test Steps | 1. Send `POST /api/v1/auth/refresh` with RT-001. 2. Receive new access token AT-002 and new refresh token RT-002. 3. Send `POST /api/v1/auth/refresh` again with the original RT-001 (replaying the consumed token). |
| Expected Result | Step 1 returns HTTP 200 with AT-002 and RT-002. Step 3 returns HTTP 401 with error code `REFRESH_TOKEN_INVALID`. RT-001 is no longer valid. |
| Pass Criteria | First use = HTTP 200; replay = HTTP 401 with `REFRESH_TOKEN_INVALID`. |
| Priority | Critical |

---

**TC-NFR-013**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-013 |
| FR Reference | FR-SET-005, BR-001 |
| Title | Verify Cashier-role user receives HTTP 403 when attempting stock adjustment approval |
| Preconditions | 1. A pending stock adjustment exists with ID "ADJ-001". 2. A valid JWT for a Cashier-role user is available. |
| Test Steps | 1. Send `POST /api/v1/inventory/adjustments/ADJ-001/approve` with the Cashier JWT. |
| Expected Result | The API returns HTTP 403. ADJ-001 remains in "pending_approval" status. |
| Pass Criteria | HTTP 403 returned; adjustment status unchanged. |
| Priority | High |

---

**TC-NFR-014**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-014 |
| FR Reference | FR-SET-005 |
| Title | Verify Cashier-role user receives HTTP 403 when attempting to access payroll endpoints |
| Preconditions | 1. A valid JWT for a Cashier-role user is available. |
| Test Steps | 1. Send `GET /api/v1/payroll` with the Cashier JWT. 2. Send `POST /api/v1/payroll/run` with the Cashier JWT. |
| Expected Result | Both requests return HTTP 403. No payroll data is returned. |
| Pass Criteria | Both requests return HTTP 403. |
| Priority | High |

---

**TC-NFR-015**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-015 |
| FR Reference | FR-SET-005 |
| Title | Verify OWASP ZAP automated scan reports zero confirmed SQL injection findings |
| Preconditions | 1. OWASP ZAP is installed and configured to scan the Maduuka staging web application. 2. A valid authenticated session is provided to ZAP for authenticated scanning. |
| Test Steps | 1. Configure OWASP ZAP with the staging URL and authenticated session cookie or API token. 2. Run an active scan targeting all discovered URLs (forms, API endpoints). 3. Review the ZAP HTML report for "SQL Injection" alerts at confidence level "Confirmed". |
| Expected Result | The ZAP report shows 0 alerts with Alert ID matching SQL Injection at confidence = "Confirmed". No high-risk SQL injection alerts appear in the report. |
| Pass Criteria | 0 confirmed SQL injection findings in the ZAP HTML report. |
| Priority | Critical |

---

**TC-NFR-016**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-016 |
| FR Reference | FR-SET-005 |
| Title | Verify CSRF protection rejects a state-changing POST request without a valid CSRF token |
| Preconditions | 1. The web application is deployed on staging. 2. A valid authenticated session cookie is obtained by logging in. |
| Test Steps | 1. Using a raw HTTP client (e.g., curl), send `POST /sales/create` with the authenticated session cookie but without a CSRF token in the request body or headers. 2. Observe the response. 3. Repeat with an invalid (replayed, previously used) CSRF token. |
| Expected Result | Both requests return HTTP 403. The response body contains no success message and no newly created resource. The database shows no new sale record. |
| Pass Criteria | Both requests = HTTP 403; 0 new records created. |
| Priority | Critical |

---

**TC-NFR-017**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-017 |
| FR Reference | FR-SET-005 |
| Title | Verify bcrypt password hash has cost factor at or above 12 and no plain-text passwords exist |
| Preconditions | 1. Direct read access to the staging MySQL database is available. 2. At least 3 user accounts exist with known passwords. |
| Test Steps | 1. Query `SELECT password FROM users LIMIT 10`. 2. Inspect the hash format of each row. 3. Extract the cost factor from the bcrypt hash prefix (format: `$2y$<cost>$...`). |
| Expected Result | All password values begin with `$2y$` (bcrypt). The cost factor in each hash is ≥ 12. No password column value is a plain-text string, an MD5 hash (32 hex characters), or a SHA-1 hash (40 hex characters). |
| Pass Criteria | All passwords are bcrypt hashes with cost factor ≥ 12; 0 plain-text or weak-hash passwords in the users table. |
| Priority | Critical |

---

**TC-NFR-018**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-018 |
| FR Reference | FR-SET-011 |
| Title | Verify Android app rejects HTTPS connection when a proxy CA certificate is installed (certificate pinning) |
| Preconditions | 1. A physical Android test device is available. 2. Burp Suite (or equivalent) is configured as a proxy with its CA certificate installed on the device. 3. The Maduuka Android app is installed on the device. |
| Test Steps | 1. Configure the device to route traffic through the Burp Suite proxy. 2. Install the Burp Suite CA certificate on the device. 3. Launch the Maduuka app. 4. Attempt any action that requires an API call (e.g., log in). 5. Observe the app's behaviour and the Burp Suite proxy intercept. |
| Expected Result | The app refuses the connection. The Burp Suite proxy receives the connection attempt but the app does not transmit any request data to the proxy. The app displays an appropriate network error or warning, and the login does not proceed. No API credentials or tokens are transmitted through the proxy. |
| Pass Criteria | App refuses proxy connection; 0 API payloads visible in Burp Suite; login fails securely with network error. |
| Priority | Critical |

---

**TC-NFR-019**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-019 |
| FR Reference | FR-SET-011 |
| Title | Verify JWT and sensitive credentials are stored in EncryptedSharedPreferences, not in plain text |
| Preconditions | 1. The Maduuka Android app is installed on a test device. 2. ADB access is available. 3. The user is logged in (a JWT is stored on-device). |
| Test Steps | 1. Use ADB to pull the app's shared preferences directory: `adb shell run-as com.chwezi.maduuka cat /data/data/com.chwezi.maduuka/shared_prefs/`. 2. Inspect all `.xml` files for any plain-text JWT, password, or API key values. |
| Expected Result | No `.xml` file in the shared preferences directory contains a plain-text JWT string (a string matching `^[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+$`). All sensitive values are AES-256-GCM encrypted blobs. |
| Pass Criteria | 0 plain-text JWTs or passwords found in shared preferences XML files. |
| Priority | Critical |

---

## NF-004: Minimum-Spec Mobile Tests

---

**TC-NFR-020**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-020 |
| FR Reference | FR-POS-026 |
| Title | Verify POS sale flow completes on minimum-spec Android device (2 GB RAM, ARM32, Android 8.0) |
| Preconditions | 1. A physical or emulated Android device with: Android 8.0 (API 26), ARM32 architecture, exactly 2 GB RAM. 2. The Maduuka app APK is installed. 3. A POS session is open. |
| Test Steps | 1. Search for a product. 2. Add it to the cart. 3. Process a cash payment (UGX 10,000 for a UGX 8,500 item). 4. Confirm the sale. 5. View the receipt. |
| Expected Result | All 5 steps complete without an application crash (ANR, or Force Close). The receipt displays the correct item, total (UGX 8,500), change (UGX 1,500), receipt number, and timestamp. The end-to-end flow completes in ≤ 5 seconds on this device. |
| Pass Criteria | No ANR or crash; receipt displayed with correct values; total time ≤ 5,000 ms. |
| Priority | Critical |

---

**TC-NFR-021**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-021 |
| FR Reference | FR-POS-026 |
| Title | Verify app does not crash or lose data when device is rotated during an active cart session |
| Preconditions | 1. The Maduuka Android app is open on any Android device. 2. A POS session is open. 3. The active cart contains 2 items: "Bread 400g" × 2 and "Milk 500ml" × 1 with a 10% order-level discount applied. |
| Test Steps | 1. Rotate the device from portrait to landscape. 2. Rotate back to portrait. 3. Observe the cart. |
| Expected Result | After rotation, the cart displays: "Bread 400g" × 2 and "Milk 500ml" × 1 with the 10% order discount intact. No items are lost. No crash or ANR occurs. |
| Pass Criteria | All cart items preserved after rotation; discount preserved; no crash. |
| Priority | High |

---

## NF-005: Cross-Platform Parity Tests

These tests verify that the same business operation produces the same data result on Android and Web.

---

**TC-NFR-022**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-022 |
| FR Reference | FR-POS-014, BR-002 |
| Title | Verify credit limit enforcement produces the same block behaviour on Android and Web |
| Preconditions | 1. Customer "Nalwoga Sarah" has credit limit = UGX 300,000 and outstanding balance = UGX 280,000. 2. A POS session is open on both Android and Web (separate sessions for the same branch). 3. A cart totalling UGX 50,000 is prepared on each platform. |
| Test Steps | 1. On Android: select "Nalwoga Sarah", choose credit payment, tap "Confirm Sale". 2. Note the message and UI state. 3. On Web: repeat the same steps. 4. Compare the behaviour. |
| Expected Result | Both Android and Web display the same block message referencing the same credit limit (UGX 300,000), same outstanding balance (UGX 280,000), and same overage (UGX 30,000). Both platforms show a "Request Manager Override" option. Neither platform completes the sale without the override. |
| Pass Criteria | Block message text is equivalent on both platforms; same credit limit and overage values displayed; sale blocked on both. |
| Priority | Critical |

---

**TC-NFR-023**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-023 |
| FR Reference | FR-HR-011, FR-HR-012 |
| Title | Verify PAYE calculation for the same staff member produces the same result on Android and Web |
| Preconditions | 1. Staff member "Mugisha Peter" has gross salary = UGX 600,000. 2. A payroll preview is accessible from both Android and Web interfaces. 3. 2024/25 PAYE tax bands are configured. |
| Test Steps | 1. On Android: navigate to HR > Payroll > Preview > "Mugisha Peter". Note PAYE amount. 2. On Web: navigate to HR > Payroll > Preview > "Mugisha Peter". Note PAYE amount. 3. Compare both values. |
| Expected Result | Both Android and Web show PAYE = UGX 82,000 for "Mugisha Peter" with gross = UGX 600,000. The NSSF Employee deduction = UGX 30,000 on both platforms. Net Pay = UGX 488,000 on both platforms. |
| Pass Criteria | PAYE = UGX 82,000 on both; NSSF = UGX 30,000 on both; Net Pay = UGX 488,000 on both. |
| Priority | Critical |

---

**TC-NFR-024**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-024 |
| FR Reference | FR-INV-011, BR-006 |
| Title | Verify FEFO batch selection produces the same batch decrement on Android and Web |
| Preconditions | 1. Product "Yoghurt 250ml" has 2 batches: Batch A (expiry 2026-05-01, qty 50), Batch B (expiry 2026-07-15, qty 60). 2. A POS session is open on both Android and Web. |
| Test Steps | 1. On Android: sell "Yoghurt 250ml" × 3 and complete the sale. 2. Note Batch A and Batch B quantities after the sale. 3. Reset the stock to the original state. 4. On Web: repeat the same sale. 5. Note Batch A and Batch B quantities. |
| Expected Result | On both Android and Web: Batch A decrements by 3 (remaining: 47); Batch B remains at 60. Both stock movement records reference Batch A. |
| Pass Criteria | Batch A = 47 on both platforms; Batch B = 60 on both; both movement records reference Batch A. |
| Priority | High |

---

**TC-NFR-025**

| Field | Content |
|---|---|
| Test Case ID | TC-NFR-025 |
| FR Reference | FR-REP-001 |
| Title | Verify daily sales report shows identical totals on Android and Web for the same date |
| Preconditions | 1. On 2026-04-05, 5 sales have been completed from various sessions (mix of Android and Web POS). 2. Total for the day across all payment methods = UGX 380,000. |
| Test Steps | 1. On Android: navigate to Reports > Daily Sales > 2026-04-05. Note the grand total. 2. On Web: navigate to Reports > Daily Sales > 2026-04-05. Note the grand total. 3. Compare. |
| Expected Result | Both Android and Web report grand total = UGX 380,000 for 2026-04-05. Payment method breakdowns are identical on both platforms. |
| Pass Criteria | Grand total identical on both platforms = UGX 380,000; payment method breakdown matches. |
| Priority | High |

---

*End of MADUUKA-TC-NFR-001 v1.0 — Non-Functional Test Cases*

**Total test cases in this file: 25**
