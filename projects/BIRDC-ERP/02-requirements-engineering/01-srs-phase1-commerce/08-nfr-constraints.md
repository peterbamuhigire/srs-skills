# 4. Non-Functional Requirements

## 4.1 Performance Requirements

| ID | Requirement | Metric |
|---|---|---|
| **NFR-PERF-001** | Product search response time at POS (online) | Response time ≤ 500 ms at P95 under normal operating load (defined as up to 50 concurrent POS sessions) |
| **NFR-PERF-002** | Invoice confirmation (including EFRIS submission trigger and GL posting queue) | End-to-end confirmation completes in ≤ 3 seconds at P95 |
| **NFR-PERF-003** | Agent cash balance calculation display | Balance rendered in ≤ 2 seconds for any agent with up to 5,000 transactions |
| **NFR-PERF-004** | Stock movement ledger query (12-month range) | Results returned in ≤ 2 seconds for queries spanning 12 months |
| **NFR-PERF-005** | POS offline sync on reconnect | All queued transactions synced to server within 60 seconds of connectivity restoration, for a queue of up to 200 transactions |
| **NFR-PERF-006** | Daily sales summary notification dispatch | Delivered to Director and Sales Manager inbox by 18:05 EAT at latest |
| **NFR-PERF-007** | Expiry alert batch job | Daily batch job completes within 10 minutes; no near-expiry batch is missed |

## 4.2 Security Requirements

| ID | Requirement |
|---|---|
| **NFR-SEC-001** | All web sessions use HttpOnly, SameSite cookies; sessions are regenerated on login |
| **NFR-SEC-002** | All mobile API calls use JWT Bearer tokens (HS256); access tokens expire in 15 minutes; refresh tokens in 30 days |
| **NFR-SEC-003** | Authorisation is enforced at the API endpoint layer for every request; UI-only enforcement is insufficient |
| **NFR-SEC-004** | All database queries use 100% PDO prepared statements; no string concatenation in query construction |
| **NFR-SEC-005** | All user output is escaped via `htmlspecialchars()`; no raw user input is rendered in HTML |
| **NFR-SEC-006** | CSRF tokens are required on all state-changing forms |
| **NFR-SEC-007** | Passwords are hashed with bcrypt or Argon2id |
| **NFR-SEC-008** | After 5 consecutive failed login attempts, the account is locked for a configurable duration |
| **NFR-SEC-009** | Director, Finance Director, and IT Administrator roles require TOTP 2FA (Google Authenticator compatible) |
| **NFR-SEC-010** | All data in transit uses TLS 1.3; sensitive fields (NIN, mobile money numbers) are encrypted at rest |
| **NFR-SEC-011** | The database application user has minimum permissions; root access is disabled from the application |
| **NFR-SEC-012** | Segregation of duties (BR-003) is enforced at the API layer; a crafted API request cannot bypass the segregation check |

## 4.3 Reliability and Availability

| ID | Requirement |
|---|---|
| **NFR-REL-001** | The system shall be available ≥ 99% of scheduled operating hours (06:00-22:00 EAT, Monday-Saturday) |
| **NFR-REL-002** | No POS transaction data shall be lost during offline operation; the offline queue is durable and survives device restart |
| **NFR-REL-003** | Automated daily database backups shall complete successfully; an email alert shall be sent to the IT Administrator if a backup fails |
| **NFR-REL-004** | The EFRIS submission retry queue shall survive a server restart; queued submissions shall be retried after restart |

## 4.4 Maintainability

| ID | Requirement |
|---|---|
| **NFR-MNT-001** | PHPUnit test coverage shall be ≥ 80% for all financial services (GL posting, commission calculation, FIFO remittance allocation) |
| **NFR-MNT-002** | All business rule parameters (commission thresholds, float limits, expiry alert days, suspension thresholds) shall be configurable via the System Administration panel without code changes (DC-002) |
| **NFR-MNT-003** | The codebase shall follow PSR-4 autoloading and PSR-12 coding standards; CI linting shall fail on violations |
| **NFR-MNT-004** | All database schema changes shall be managed via versioned migration scripts |

## 4.5 Usability

| ID | Requirement |
|---|---|
| **NFR-UX-001** | A cashier with no prior training (Prossy persona) shall complete a cash POS sale from product search to printed receipt in ≤ 90 seconds on first attempt (DC-001 test criterion) |
| **NFR-UX-002** | Every daily-use screen shall be reachable in ≤ 3 navigation steps from the home page |
| **NFR-UX-003** | All data tables shall support column-level sorting and text search via DataTables |
| **NFR-UX-004** | All forms shall display inline field-level validation errors immediately on blur, without requiring a full page submit |
| **NFR-UX-005** | The system shall display a confirmation dialog (SweetAlert2) before every irreversible action (void, adjustment, termination) |

## 4.6 Audit and Compliance

| ID | Requirement |
|---|---|
| **NFR-AUD-001** | Every financial transaction (invoice posting, stock adjustment, remittance, commission) shall generate an immutable audit record containing: actor identity, IP address, timestamp, table name, primary key, old values (JSON), and new values (JSON) |
| **NFR-AUD-002** | Audit records shall be retained for a minimum of 7 years in compliance with the Uganda Companies Act 2012 and Income Tax Act Cap 340 |
| **NFR-AUD-003** | The GL hash chain (BR-013) shall pass integrity verification on demand; the Finance Director or IT Administrator may trigger a hash chain check from the System Administration panel |
| **NFR-AUD-004** | All EFRIS submissions and responses shall be logged verbatim (FR-SAL-033) and retained for 7 years |
| **NFR-AUD-005** | Sequential number gap detection (BR-009) shall run as a scheduled daily check and alert the Finance Manager immediately upon gap detection |

# 5. Design Constraints and Standards Compliance

## 5.1 Technology Constraints

The following technology decisions are fixed and apply to all Phase 1 modules:

| Constraint | Specification |
|---|---|
| **DC-T-001** | Backend language: PHP 8.3+ with `declare(strict_types=1)` on every file |
| **DC-T-002** | Database: MySQL 9.1 InnoDB, utf8mb4 character set |
| **DC-T-003** | PDF generation: mPDF for all invoice, receipt, and statement PDFs |
| **DC-T-004** | Excel export: PhpSpreadsheet for all spreadsheet exports and imports |
| **DC-T-005** | Mobile: Android 8.0 (API 26) minimum; Kotlin, Jetpack Compose, Room, WorkManager |
| **DC-T-006** | Barcode scanning (mobile): Android ML Kit |
| **DC-T-007** | Thermal printing (mobile): Bluetooth ESC/POS |
| **DC-T-008** | EFRIS: URA EFRIS system-to-system REST API |
| **DC-T-009** | Mobile money: MTN MoMo Business API (primary), Airtel Money API (secondary) |

## 5.2 Regulatory Compliance Constraints

| Constraint | Regulation |
|---|---|
| **DC-R-001** | All commercial invoices and POS receipts must be submitted to URA EFRIS; FDN and QR code must appear on all printed documents |
| **DC-R-002** | All financial records must be retained for 7 years (Uganda Companies Act 2012, Income Tax Act Cap 340) |
| **DC-R-003** | Farmer data (NIN, GPS, photo, mobile money number) collection must comply with Uganda Data Protection and Privacy Act 2019 `[CONTEXT-GAP: GAP-004]` |
| **DC-R-004** | The system is not subject to cloud data residency rules (DC-006: on-premise); all data remains within BIRDC's servers in Uganda |

## 5.3 Architectural Constraints

| Constraint | Description |
|---|---|
| **DC-A-001** | `tbl_stock_balance` and `tbl_agent_stock_balance` are permanently separate; no application feature may merge them without explicit labelling (BR-001) |
| **DC-A-002** | The FIFO remittance allocation logic is implemented exclusively as the stored procedure `sp_apply_remittance_to_invoices`; no application-layer equivalent is permitted |
| **DC-A-003** | Segregation of duties is enforced at the API layer; no UI-only enforcement is acceptable |
| **DC-A-004** | All GL postings from Phase 1 modules write to the GL staging table; the Phase 2 GL module activates entries on deployment |
| **DC-A-005** | Hash chain integrity for GL entries (BR-013) is implemented in the database layer, not the application layer |
