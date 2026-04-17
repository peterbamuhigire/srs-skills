# Technology Stack — Longhorn ERP

## Backend

| Component | Technology | Version |
|---|---|---|
| Language | PHP (strict types, PSR-4) | 8.3+ |
| Architecture Pattern | Service-oriented, Domain-Driven Design | — |
| Dependency Injection | PHP-DI | 7.0 |
| Database Access | PDO with prepared statements only | — |
| PDF Generation | mPDF | 8.2 |
| Spreadsheet Processing | PhpOffice/PhpSpreadsheet | 5.2 |
| Email | PHPMailer (SMTP) | 6.9 |
| JWT Authentication | firebase/php-jwt | 7.0 |
| Validation | respect/validation | 2.3 |
| Expression Language | Symfony/expression-language | 7.3 |
| Environment Config | vlucas/phpdotenv | 5.6 |

## Database

| Component | Technology | Version |
|---|---|---|
| Database Engine | MySQL, InnoDB | 9.1 |
| Character Set | UTF8MB4 | — |
| Multi-tenancy | Row-level isolation via `tenant_id` FK on every operational table | — |
| Complex Logic | Stored procedures (GL posting, numbering, account mapping) | — |
| Reporting | SQL views (materialized and calculated) | — |
| Migrations | Versioned migration files, idempotent, `run_migrations.php` entry point | — |

## Frontend (Web)

| Component | Technology | Version |
|---|---|---|
| CSS Framework | Bootstrap | 5.3.0 |
| JavaScript Library | jQuery | 3.7.0 |
| Tables | DataTables (server-side pagination) | — |
| Dropdowns | Select2 (searchable) | — |
| Date Pickers | Flatpickr | — |
| Icons | Bootstrap Icons (bi-* classes) | — |
| Alerts and Modals | SweetAlert2 | — |
| Charts | Chart.js + ApexCharts | — |
| Vector Maps | jsvectormap | — |
| Rich Text Editor | TinyMCE | — |
| File Upload | Dropzone | — |

## Mobile

| Component | Technology |
|---|---|
| Android | Kotlin + Jetpack Compose |
| iOS | Swift + SwiftUI |
| API Protocol | REST (JSON), JWT Bearer token |
| Offline Support | Last-modified timestamp sync; Cooperative Procurement module supports full offline intake |

## Web Server

| Component | Technology |
|---|---|
| Web Server | Apache with mod_rewrite |
| Development Environment | WAMP (Windows) |
| Production Environment | Apache on Linux |

## Development Tools

| Tool | Purpose | Version |
|---|---|---|
| Composer | PHP package manager | — |
| PHPUnit | Unit and integration testing | 11.2 |
| PHPStan | Static analysis | 1.11 |
| PHP CS Fixer | Code formatting | 3.64 |

## Architecture Panels

| Panel | Path | Purpose |
|---|---|---|
| Tenant Workspace | `/public/` | Day-to-day operations for all tenant staff |
| Super Admin Panel | `/public/superadmin/` | Chwezi platform management, tenant provisioning, billing |
| End-User Portal | `/public/portal/` | Employee payslips, leave, customer statements, agent commissions, farmer statements |

## API Structure

| Type | Path | Auth |
|---|---|---|
| Web UI API | `/public/api/` | Session-based (CSRF token) |
| Mobile API v1 | `/public/api/mobile/v1/` | JWT Bearer token |
| Super Admin API | `/public/superadmin/api/` | Session-based (super admin session) |

## Security Model

- Session-based auth (web): `LONGHORN_ERP_SESSION`, HttpOnly, SameSite=Strict
- JWT with refresh rotation (mobile): Bearer token, claims include `tenant_id`, `user_id`, `role`, enabled modules
- CSRF protection: token-per-session, `X-CSRF-Token` header on all state-changing requests
- Rate limiting: token bucket algorithm, per-tenant and per-user limits
- Tenant isolation: `tenant_id` always sourced from session, never from request parameters
- TLS 1.3 in transit; AES-256 at rest for sensitive fields
- Audit log: immutable INSERT-only, every create/update/delete/approve logged with old values, new values, IP, timestamp
