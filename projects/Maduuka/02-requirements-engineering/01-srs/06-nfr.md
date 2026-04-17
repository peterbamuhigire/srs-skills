# Section 6: Non-Functional Requirements

## 6.1 Performance Requirements

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### NFR-PERF-001: POS Transaction Performance
The system shall complete each step of the POS sale flow -- item addition, payment processing, and receipt generation -- within 3 seconds at the 95th percentile on a device equivalent to a UGX 250,000 entry-level Android phone (minimum 2 GB RAM) on a 3G mobile data connection (minimum 1 Mbps downlink), under peak load equivalent to 150% of average daily transaction volume.

**Verifiability:** Execute a load test simulating 150% of average daily transaction volume. Measure end-to-end sale completion time (first product scan to receipt confirmation); the 95th percentile must be <= 3000 ms. Validate on a device with <= 2 GB RAM on a 3G-simulated network connection.
<!-- [END DOMAIN-DEFAULT] -->

#### NFR-PERF-002: Barcode Scan Response
The system shall add a product to the active cart within 1 second of successful barcode detection by the phone camera or external Bluetooth scanner.

**Verifiability:** Scan 100 barcodes across 10 distinct products; 99 of 100 scans must result in a cart addition event within <= 1000 ms of the scan event timestamp.

#### NFR-PERF-003: Dashboard Load Time
The dashboard screen shall fully render all KPI cards (Today's Revenue, Transaction Count, Outstanding Credit, Cash Position) within 4 seconds at the 95th percentile on a 3G connection (minimum 1 Mbps downlink).

**Verifiability:** Measure time-to-interactive for the dashboard screen across 20 test runs on a 3G-simulated connection; the 95th percentile must be <= 4000 ms.

#### NFR-PERF-004: API Response Time
All REST API endpoints shall return a response within 500 ms at the 95th percentile under normal operating load (defined as average daily request volume for the production environment).

**Verifiability:** Execute a load test at average daily request volume using a tool such as k6 or JMeter; measure response time across all endpoints. The 95th percentile across all measured endpoints must be <= 500 ms.

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### NFR-PERF-005: Inventory Synchronisation
The system shall synchronise inventory stock levels across all active sessions (POS terminal, web dashboard, mobile app) within 5 seconds of a stock-changing event (sale, return, manual adjustment, or goods receipt).

**Verifiability:** Complete a test sale on the POS. Immediately query the inventory quantity on the web dashboard and a second mobile session. Repeat across 100 transactions; in 99 of 100 cases, all sessions must reflect the updated stock level within <= 5 seconds.
<!-- [END DOMAIN-DEFAULT] -->

---

## 6.2 Availability and Reliability Requirements

#### NFR-AVAIL-001: Core POS and API Uptime
The POS module and its backing REST API shall maintain 99.9% uptime (equivalent to <= 8.76 hours downtime per year), measured on a rolling 12-month basis.

**Verifiability:** Monitor uptime continuously using an external uptime monitoring service (e.g., UptimeRobot or equivalent). Calculate availability monthly: Availability = MTTF / (MTTF + MTTR) x 100%. The 12-month rolling value must be >= 99.9%.

#### NFR-AVAIL-002: Offline-First Guarantee
The Android application shall allow a cashier to complete a POS sale, record stock movements, and log expenses when no internet connectivity is available. Offline capability shall activate automatically -- no user configuration or mode switch is required.

**Verifiability:** Disable all network connectivity on the test device (airplane mode). Complete 10 POS sales, 3 stock adjustments, and 2 expense entries. Restore connectivity. All 15 records must appear in the server-side database within 30 seconds of connection restoration.

#### NFR-AVAIL-003: Offline Queue Persistence
If the Android application is closed (process killed) while offline transactions are pending, the system shall retain all pending transactions in the local Room database and resume synchronisation automatically when the app is next opened with internet connectivity.

**Verifiability:** Complete 5 offline sales. Force-close the application. Reopen the application with network connectivity. All 5 sales must appear on the server within 30 seconds of app restart.

---

## 6.3 Security Requirements

#### NFR-SEC-001: Data Encryption in Transit
All data transmitted between the mobile application and the REST API, and between the web browser and the backend, shall be encrypted using TLS 1.3. TLS 1.2 and below shall be rejected by the server.

**Verifiability:** Use a network protocol analyser (e.g., Wireshark) to capture traffic; verify all packets are TLS 1.3. Attempt a TLS 1.2 handshake with the server using OpenSSL; the server must reject the connection.

#### NFR-SEC-002: Password Storage
The system shall never store user passwords in plaintext or using reversible encryption. All passwords shall be hashed using bcrypt with a minimum cost factor of 12.

**Verifiability:** Inspect the users database table; confirm all password column values begin with the bcrypt identifier ($2y$ prefix). Attempt to reverse a stored hash using a known-plaintext attack; the attempt must not succeed within a 1-hour test window.

#### NFR-SEC-003: Mobile Token Storage
JWT access tokens and refresh tokens on Android devices shall be stored exclusively in AES-256-GCM EncryptedSharedPreferences. No token value shall appear in plain SharedPreferences, application files, logcat output, or the system clipboard.

**Verifiability:** Perform static analysis of the Android codebase; no token write shall reference SharedPreferences, File, or Context.openFileOutput APIs. On a rooted test device, inspect all accessible application storage; no token value shall be readable in plaintext.

#### NFR-SEC-004: RBAC at API Layer
The system shall enforce role permissions at every REST API endpoint regardless of request origin. A request from a user without the required permission shall receive HTTP 403 Forbidden with no data payload.

**Verifiability:** For a representative sample of at least 20 API endpoints, send requests authenticated with a user role that does not hold the required permission (e.g., Cashier role attempting GET /api/v1/reports/financial). All such requests must return HTTP 403 with an empty data payload.

#### NFR-SEC-005: Audit Log Immutability
The audit log table shall be append-only. No DELETE or UPDATE statement shall execute successfully against audit log rows from any application user account, including platform administrator accounts.

**Verifiability:** Attempt to delete an audit log entry via the API using a platform admin JWT token. Attempt a direct DELETE SQL statement against the audit log table using the application database user. Both attempts must fail; record count must remain unchanged.

#### NFR-SEC-006: Certificate Pinning
The Android application shall implement certificate pinning via OkHttp CertificatePinner. Any API request that does not match the pinned certificate shall be rejected with a certificate pinning failure error, and the user shall be shown a security warning.

**Verifiability:** Configure a man-in-the-middle proxy (e.g., Charles Proxy) with a custom CA certificate on the test device. Attempt any API call from the Android application; the call must fail with a certificate error, not succeed with a proxied response.

---

## 6.4 Usability Requirements

#### NFR-USE-001: Zero-Configuration Offline Mode
Offline mode shall activate automatically when internet connectivity is lost. No user action, settings toggle, or manual mode switch shall be required to operate the POS offline.

**Verifiability:** Disable network connectivity mid-POS-session without any user interaction. Attempt to add a product to cart and complete a sale; the operation must succeed without any error dialog or mode-change prompt.

#### NFR-USE-002: Per-User Language Selection
The system shall display all UI text in the user's selected language (English or Swahili in Phase 1) without requiring an app restart. Each user shall configure their own language independently of the business's default language.

**Verifiability:** Change a test user's language to Swahili. Navigate through Dashboard, POS, Inventory, and HR screens; verify all visible text strings render in Swahili. Change back to English; verify all strings return to English. No app restart shall be required for either change.

#### NFR-USE-003: Onboarding Completion Time
A new business owner shall be able to complete the 6-step onboarding wizard and process their first POS sale within 20 minutes of account registration, without external assistance.

**Verifiability:** Conduct a usability test with 5 participants matching the Nakato persona (low tech literacy, WhatsApp-proficient). Measure time from account registration to first completed sale; the median time across participants must be <= 20 minutes. 4 of 5 participants must complete without requiring assistance.

---

## 6.5 Scalability Requirements

#### NFR-SCALE-001: Multi-Tenant Load Isolation
The system shall maintain data isolation and response time consistency between tenants under load. Tenant A's high-volume query activity shall not degrade Tenant B's API response time by more than 20%.

**Verifiability:** Run concurrent load tests simulating two tenants each at 10 times average request volume simultaneously. Measure P95 response time per tenant during and outside the load period; the difference between the two tenants' P95 response times must be <= 20%.

#### NFR-SCALE-002: Product Catalogue Scale
The system shall support a product catalogue of up to 10,000 products per tenant (Pro/Enterprise plans) with search response time within the NFR-PERF-001 threshold.

**Verifiability:** Seed a test tenant with 10,000 products. Execute 100 POS product search queries against the full catalogue; the 95th percentile response time must be <= 500 ms.

---

## 6.6 Maintainability Requirements

#### NFR-MAINT-001: Modular Architecture
The Android application shall separate business logic from presentation and data access using MVVM + Clean Architecture with distinct Presentation, Domain, and Data layers. Business logic in the Domain layer shall be testable via JVM unit tests without requiring an Android emulator.

**Verifiability:** Execute the project's JVM unit test suite without an emulator; all Domain layer tests must pass. No Domain layer class shall import Android framework classes (android.*).

#### NFR-MAINT-002: Internationalisation Coverage
All user-visible strings in the Android application shall be defined in strings.xml resource files. No user-visible string shall be hardcoded in Kotlin source files.

**Verifiability:** Run a lint check for hardcoded strings (AndroidLint HardcodedText rule); zero violations shall be reported in view-layer files.
