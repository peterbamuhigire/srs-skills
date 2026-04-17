# Technology Stack — BIRDC ERP

**Deployment model:** Single-tenant, on-premise at BIRDC Nyaruzinga, Bushenyi, Uganda.
No SaaS, no cloud hosting, no subscription fees after build.

---

## Web Application Stack

| Component | Specification |
|---|---|
| Backend language | PHP 8.3+ with `declare(strict_types=1)` on every file, PSR-4 autoloading, PSR-12 coding standard |
| Architecture pattern | Service / Repository pattern with PHP-DI dependency injection container |
| Database | MySQL 9.1 InnoDB, utf8mb4 character set, comprehensive indexing |
| Database features | Stored procedures for complex business logic (commission triggers, FIFO remittance allocation via `sp_apply_remittance_to_invoices`, production variance); database triggers for automated business rules |
| Frontend framework | Bootstrap 5 + Tabler admin UI template |
| JavaScript | jQuery, Alpine.js (minimal) |
| Charts | ApexCharts |
| Data tables | DataTables (handles 6,440+ farmer names, 1,071 agents) |
| Dropdowns | Select2 (searchable dropdowns for large data sets) |
| Date pickers | Flatpickr |
| User feedback | SweetAlert2 |
| PDF generation | mPDF (invoices, CoA, payslips, procurement POs, farmer payment statements) |
| Excel / CSV | PhpSpreadsheet (farmer bulk import, product bulk import, payroll bank transfer lists) |
| Email | PHPMailer with SMTP TLS (report delivery, password resets, agent/farmer notifications) |
| Testing | PHPUnit, minimum 80% coverage for financial services (GL posting, payroll, commission, remittance) |
| Biometric integration | ZKTeco fingerprint device integration — attendance records imported directly into HR module |

## Three Application Panels

| Panel | URL Path | Users |
|---|---|---|
| Main ERP Workspace | `/public/` | All BIRDC/PIBID staff (Finance, Sales, Procurement, Inventory, Manufacturing, QC, HR, Management) |
| Sales Agent Portal | `/public/sales-agents/` | 1,071 field sales agents — simplified sub-application with agent POS, reports, remittance, commission, stock enquiry |
| System Administration | `/public/admin/` | IT administrators and super-users — user management, role config, audit log, backup, integration config |

## Security Architecture

| Concern | Implementation |
|---|---|
| Authentication (web) | Session-based: HttpOnly cookies, SameSite, session regeneration on login |
| Authentication (mobile API) | JWT Bearer (HS256): 15-minute access tokens, 30-day refresh tokens |
| Authorisation | 8-layer: Role → Page → API endpoint → UI element → Location-based → Time-based → Conditional rules → Object ownership |
| Segregation of duties | Enforced at API layer, not just UI |
| Password hashing | bcrypt / Argon2id |
| SQL injection | 100% PDO prepared statements; no string concatenation in queries |
| XSS prevention | `htmlspecialchars()` on all output |
| CSRF | CSRF tokens on all state-changing forms |
| Audit trail | Immutable audit tables: actor, IP address, timestamp, old values, new values; 7-year retention |
| Data encryption | TLS 1.3 in transit; sensitive fields encrypted at rest |
| Account lockout | After 5 failed login attempts, configurable lockout duration |
| 2FA | TOTP (Google Authenticator compatible) for Director, Finance Director, IT Administrator roles |
| Database security | Dedicated application DB user with minimum permissions; root access disabled from application; credentials in `.env`, never in code |

## Mobile API

| Concern | Specification |
|---|---|
| Protocol | REST API over HTTPS |
| Authentication | JWT Bearer tokens (same as above) |
| Authorisation | Same RBAC rules as web — role and permission enforced at every API endpoint |
| Offline support | Android apps use Room (SQLite) for local storage; WorkManager for background sync |
| Sync | Conflict resolution: last-write-wins with server timestamp; conflicts logged for review |

## Android Mobile Apps (6 Apps — iOS Deferred)

| App | Users | Key Capability |
|---|---|---|
| Sales Agent App | 1,071 field sales agents | Offline POS, agent stock view, cash remittance submission, commission statements, Bluetooth 80mm thermal printing |
| Farmer Delivery App | Field collection officers | Register new farmers offline, GPS farm profiling, record individual deliveries (Bluetooth scale integration), print farmer receipts |
| Warehouse App | Warehouse staff | Barcode scan for stock receipts, transfer confirmation, physical stock count |
| Executive Dashboard App | Director, Finance Director | Trial balance summary, P&L snapshot, cash position, budget variance alerts (push notifications) |
| HR Self-Service App | All staff (150+) | Apply for leave, view payslips, check leave balance, view attendance record |
| Factory Floor App | Production supervisors, QC | Monitor active production orders, record worker attendance, enter completion quantities, submit QC inspection results |

**Android tech stack:** Kotlin, Jetpack Compose, Room (SQLite offline), Retrofit + OkHttp,
WorkManager (background sync), ML Kit (barcode scanning), Bluetooth ESC/POS (thermal printing),
BiometricPrompt, EncryptedSharedPreferences.
**Minimum Android version:** Android 8.0 (API 26).

## Infrastructure

| Component | Specification |
|---|---|
| Server | On-premise at BIRDC Nyaruzinga, Bushenyi — BIRDC-owned hardware |
| Web server | Apache / Nginx with HTTPS (Let's Encrypt or self-signed for LAN-only) |
| Database server | MySQL 9.1 on dedicated or same server |
| Backups | Automated daily database backups; weekly offsite backup (USB drive + remote encrypted copy) |
| CI/CD | GitHub Actions — lint → test → build → deploy to staging; manual approval for production |
| Monitoring | Basic uptime monitoring; error logging to file with email alerts for critical errors |

## EFRIS Integration (URA)

| Concern | Specification |
|---|---|
| API type | URA EFRIS system-to-system REST API |
| Trigger | Every commercial invoice and POS receipt submitted in real time on posting |
| Response | Fiscal Document Number (FDN) and QR code stored against the transaction |
| Failure handling | Failed submissions queued for retry; Finance Manager alerted if retry fails after 3 attempts |
| Documents affected | Sales invoices, credit notes, POS receipts, pro forma invoices |

## Mobile Money Integration

| Provider | Use case |
|---|---|
| MTN MoMo Business API | Agent remittance collection (push payment prompt), farmer bulk payment, casual worker salary, customer payment collection |
| Airtel Money API | Same use cases as MTN MoMo — dual-provider redundancy |
