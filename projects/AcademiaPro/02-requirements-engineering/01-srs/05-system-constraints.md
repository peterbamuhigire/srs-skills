## Section 5: System Constraints

> Constraints are binding restrictions that narrow the solution space. They are not requirements — they do not describe desired behaviours. They describe boundaries within which every design and implementation decision must remain. Non-compliance with any constraint listed here constitutes a defect.

---

### 5.1 Legal and Regulatory Constraints

#### LC-001: Uganda Data Protection and Privacy Act 2019 (PDPO 2019)

Chwezi Core Systems is the Data Processor. Each subscribing school is the Data Controller. The following obligations are binding:

1. **Data Controller registration:** Chwezi Core Systems must register with the Personal Data Protection Office (PDPO) Uganda before Phase 1 goes live.
2. **Privacy Notice:** A Privacy Policy covering data collection, purpose, retention, sharing, and data subject rights must be published at `/privacy` before first school signs up.
3. **Data Processing Agreement (DPA):** Each school must sign a DPA establishing the school as Data Controller and Chwezi Core Systems as Data Processor before tenant activation.
4. **Data Subject Rights (implemented in Phase 1):**
   - Right of Access: `GET /api/v1/students/{uid}/data-export` returns all personal data for that student in JSON format, downloadable by the School Owner or the student themselves.
   - Right to Correction: any role with `students:edit` permission may correct personal data (all corrections logged in FR-AUD-001).
   - Right to Erasure: soft-delete pathway with hard-delete scheduled after the 7-year retention period. Hard-delete before 7 years is blocked (FR-SIS-005).
5. **Breach Notification:** If a personal data breach is detected, the PDPO Office must be notified within 72 hours and affected data subjects notified without undue delay. Incident response procedure must be documented before Phase 1 launch.

*See `_context/gap-analysis.md` HIGH-008 for complete compliance checklist.*

#### LC-002: Uganda Copyright Act 2006

All software produced under this project is the intellectual property of Chwezi Core Systems. All contributing developers must sign an IP assignment agreement before commencing work. Copyright registration with the Uganda Registration Services Bureau (URSB) must be completed before Phase 8 go-live.

#### LC-003: Bank of Uganda (BoU) Payment Systems Regulations

Phase 1 does not process payments directly. The bursar records payment facts manually; no payment API is called. SchoolPay (a BoU-licensed Payment Service Provider) is the payment rail for Phase 2. Direct mobile money processing (MTN MoMo, Airtel Money) is deferred until a BoU Payment Systems Operator (PSO) licence is obtained (Phase 3–4).

#### LC-004: UNEB Data Governance

Student exam registration data submitted to UNEB must conform exactly to UNEB's specified format. No student examination result may be altered by the system after UNEB export confirmation. Exported data must not be shared with any third party other than UNEB.

#### LC-005: MoES EMIS Reporting

EMIS export data must conform to the MoES EMIS data dictionary. Schools remain responsible for the accuracy of their data; the system is the transport mechanism, not the data validator. Chwezi Core Systems does not submit to MoES on behalf of schools; the export is downloaded by the Head Teacher for manual submission (automated submission is Phase 11).

---

### 5.2 Technology Constraints

#### TC-001: PHP 8.2 Minimum

All server-side code must be compatible with PHP 8.2 or later. PHP 7.x patterns (array functions returning references, deprecated function calls, `create_function`) are prohibited.

#### TC-002: Laravel 11 Framework

The application must be built on Laravel 11. No alternative PHP framework is permitted. Laravel's routing, validation, queuing (Horizon), authentication (Sanctum), and file storage (S3 via Flysystem) subsystems must be used as the framework intends.

#### TC-003: MySQL 8.x InnoDB Only

All tables must use the InnoDB storage engine. MyISAM is prohibited. MySQL 8.x-specific features (window functions, CTE, generated columns, JSON columns) may be used where appropriate. All table creation must specify `ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci`.

#### TC-004: No Direct `DB::statement` Without Tenant Scope

Any call to `DB::statement()`, `DB::select()`, `DB::insert()`, `DB::update()`, or `DB::delete()` on a tenant-scoped table without a `tenant_id` parameter binding is a security defect. CI pipeline (GitHub Actions + PHPStan custom rule) must flag this pattern.

#### TC-005: React 18 / TypeScript Frontend

All web portal frontend code must be written in TypeScript (strict mode). JavaScript (`.js`) files are prohibited in the `resources/` directory. React class components are prohibited; all components must use functional components with hooks.

#### TC-006: Vite Build System

The frontend build system is Vite. Webpack is prohibited. All asset imports must use Vite's module system.

#### TC-007: OpenAPI 3.1 Specification Prerequisite

Frontend and mobile development must not begin on any endpoint until that endpoint is specified in the OpenAPI 3.1 document at `03-design-documentation/03-api-spec/`. This is a process constraint, not a runtime constraint.

#### TC-008: GitHub Actions CI/CD

All code changes must pass the GitHub Actions CI pipeline before merging to `main`. The pipeline must include: PHPStan level 8, PHP CS Fixer, ESLint, Prettier, Pest unit tests, Pest feature tests (with a test database), and Playwright E2E tests (on the staging environment).

#### TC-009: Argon2ID Password Hashing Exclusively

`password_hash()` with `PASSWORD_BCRYPT` is prohibited. All password storage must use `PASSWORD_ARGON2ID` with `memory_cost ≥ 65536`, `time_cost = 4`, `threads = 3`, a 32-byte random salt, and the `PASSWORD_PEPPER` environment variable.

#### TC-010: Redis for Session Storage in Production

In production, PHP sessions must use the Redis session driver (not file-based sessions). File-based sessions are permitted in development only.

---

### 5.3 Performance Constraints

These constraints define the minimum acceptable performance thresholds. They are duplicated in Section 6 (NFR) in measurable form for V&V purposes; they are stated here as design constraints to enforce architectural decisions.

| Constraint | Threshold |
|---|---|
| Standard CRUD API endpoints | ≤ 500 ms P95 under 200 concurrent users |
| Student search (Meilisearch) | ≤ 500 ms P95 |
| Report card (single, PDF queued) | ≤ 3,000 ms P95 |
| Bulk report card (200 students) | ≤ 120 seconds (parallel Horizon workers) |
| UNEB grade computation (500 students) | ≤ 5 seconds |
| Fee collection report (PDF/CSV) | ≤ 5,000 ms |
| EMIS export (2,000 students) | ≤ 30 seconds |
| Availability during exam periods | ≥ 99.9% monthly uptime |

These thresholds must be validated with a k6 load test before Phase 1 go-live. Test results must be stored in `09-governance-compliance/` as part of the go-live evidence package.

---

### 5.4 Design Constraints

#### DC-001: Three-Tier Panel Separation

The school admin workspace, super admin panel, and end-user portal must be architecturally separated. They share the same Laravel backend and database, but their routes, controllers, middleware stacks, and frontend bundles are distinct. Shared UI components are permitted via a shared component library; shared business logic is permitted via shared Services; shared data access is permitted via shared Repositories.

#### DC-002: Tenant Isolation by Default

Tenant isolation is the default state. The Repository base class applies `WHERE tenant_id = ?` automatically. Opting out of isolation (via `withoutTenantScope()`) is only permitted in the Super Admin panel and must always be paired with an audit log write. Any `withoutTenantScope()` call outside the Super Admin namespace is a security defect.

#### DC-003: Job Queue for All Long-Running Operations

Operations exceeding 3 seconds must be executed asynchronously via Laravel Horizon. Synchronous HTTP responses for long operations are prohibited. The API must return HTTP 202 with a `job_id` for any queued operation, and provide a polling endpoint for status updates.

#### DC-004: No Hardcoded Tenant Data

No tenant-specific data (school names, fee amounts, calendar dates, user IDs) may be hardcoded in application code. All tenant configuration is stored in the database and loaded at runtime.

#### DC-005: Zero-Config Uganda Default

A school that completes onboarding without changing country settings must be fully operational with correct Uganda defaults: 3-term calendar, UGX currency, UNEB grading schemas, Africa's Talking SMS, EAT timezone. The system achieves this without requiring the school to explicitly configure each default.

#### DC-006: Database Migrations Must Be Non-Destructive and Idempotent

All production database migrations must be non-destructive (no `DROP COLUMN`, `DROP TABLE`, or data truncation without a preceding deprecation migration). Migrations must be idempotent — running them twice must not cause errors. Migrations follow the `mysql-best-practices` skill migration checklist.

#### DC-007: Session Prefix Isolation

All session variable names must use the `academia_pro_` prefix (e.g., `academia_pro_user_id`, `academia_pro_tenant_id`). Direct access to `$_SESSION` is prohibited; use the `setSession()` / `getSession()` / `hasSession()` / `destroySession()` helper functions. This prevents session variable collisions if the platform is hosted on a shared server or alongside other applications during development.
