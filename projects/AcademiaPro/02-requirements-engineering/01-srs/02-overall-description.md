## Section 2: Overall Description

### 2.1 Product Perspective

Academia Pro is a new, independently developed multi-tenant SaaS platform. It does not replace or integrate with any existing Chwezi Core Systems product. It replaces the following legacy tools currently in use by target schools: paper fee registers, Excel-based mark sheets, Word-based report card templates, handwritten attendance registers, and informal SMS communication.

#### 2.1.1 System Context Diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                     Academia Pro Platform                          │
│                                                                    │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                   Shared Infrastructure                      │  │
│  │  Laravel 11 API  |  MySQL 8.x  |  Redis 7  |  Wasabi S3     │  │
│  └──────────────────────────────────────────────────────────────┘  │
│         │                   │                    │                 │
│  ┌──────▼──────┐   ┌────────▼───────┐  ┌────────▼──────────┐     │
│  │  /public/   │   │  /adminpanel/  │  │  /memberpanel/    │     │
│  │  School     │   │  Super Admin   │  │  Student/Parent   │     │
│  │  Workspace  │   │  Panel         │  │  Portal           │     │
│  │  (Tenant    │   │  (Chwezi       │  │  (End Users)      │     │
│  │  Admin)     │   │  Staff)        │  │                   │     │
│  └─────────────┘   └────────────────┘  └───────────────────┘     │
└────────────────────────────────────────────────────────────────────┘
         │                                       │
         ▼                                       ▼
┌─────────────────┐                   ┌──────────────────┐
│  External APIs  │                   │  External Actors │
│  - SchoolPay    │                   │  - Teachers      │
│  - Africa's     │                   │  - Bursars       │
│    Talking SMS  │                   │  - Head Teachers │
│  - Claude API   │                   │  - Parents       │
│  - Wasabi S3    │                   │  - Students      │
│  - CDN          │                   │  - MoES/EMIS     │
│  - FCM Push     │                   │  - BrightSoma    │
│  - BrightSoma   │                   │                  │
│    API (Ph 3)   │                   │                  │
└─────────────────┘                   └──────────────────┘
```

#### 2.1.2 Three-Tier Panel Architecture

Academia Pro implements the three-tier panel architecture defined in the `multi-tenant-saas-architecture` skill:

- **School Admin Workspace (`/`):** The primary daily operational interface. All school staff roles (Owner/Director, Head Teacher, Class Teacher, Accounts Bursar, Receptionist) access the platform through this workspace. Every request is scoped to a single `tenant_id`. Staff cannot access any other tenant's data.
- **Super Admin Panel (`/adminpanel/`):** Restricted to Chwezi Core Systems staff. Provides tenant provisioning, billing management, cross-tenant support access (logged), and platform analytics. Super admins may access any tenant's data in read-only support mode; every such access is written to the audit log before data is returned.
- **End User Portal (`/memberpanel/`):** Self-service access for Students and Parents/Guardians. Read-mostly. Scoped to the user's enrolled school (`tenant_id`). A parent with children at multiple schools holds separate sessions per school.

#### 2.1.3 Multi-Tenant Data Model

All tenant-scoped tables carry a `tenant_id` column (non-nullable, foreign key to `tenants`). The Laravel Repository base class appends `WHERE tenant_id = ?` to every query builder chain before execution. Raw SQL usage is prohibited in application code (CI enforces this). Global identity tables (`global_students`, `student_identifiers`) carry no `tenant_id` and are access-controlled at the Service layer.

### 2.2 Product Functions — Phase 1 Summary

Phase 1 delivers the following functional groups. Detailed requirements are in Section 4.

| Group | Code | Primary Users | Phase |
|---|---|---|---|
| Authentication and Session Management | FR-AUTH | All roles | 1 |
| Student Information System | FR-SIS | Head Teacher, Receptionist, Class Teacher | 1 |
| Academics Setup | FR-ACA | Head Teacher, School Owner | 1 |
| Fees Management (manual entry) | FR-FEE | Accounts Bursar, School Owner | 1 |
| Attendance | FR-ATT | Class Teacher, Head Teacher | 1 |
| Examinations and UNEB Grading | FR-EXM | Class Teacher, Head Teacher | 1 |
| Report Card Generation | FR-RPT | Head Teacher, Class Teacher | 1 |
| Role-Based Access Control | FR-RBAC | School Owner, Head Teacher (user management) | 1 |
| EMIS / Government Export | FR-EMIS | Head Teacher | 1 |
| Audit Trail | FR-AUD | Super Admin (Chwezi) | 1 |
| Tenant Lifecycle Management | FR-TNT | Super Admin (Chwezi) | 1 |
| Class Library and E-Learning | FR-ELEARN | Class Teacher, Head Teacher, Student, Parent | 2 |

### 2.3 User Classes and Characteristics

User classes are ordered from highest to lowest privilege within the school-tenant scope.

#### 2.3.1 Super Admin (Chwezi Staff)

Platform operators. No school-specific scope. Access to all tenant data in logged read-only support mode; write access only through tenant administration functions. Must authenticate with Multi-Factor Authentication (MFA). Tech comfort: high. Expected volume: 2–5 users.

#### 2.3.2 School Owner / Director

The subscriber account holder for a school. Full read/write access within their tenant. Approves refunds. Views financial and academic dashboards. Primary decision-maker for school-level settings. Tech comfort: medium to high (see persona: Patrick Byamukama). Typically accesses via web portal and, from Phase 3, a mobile app. Expected volume: 1–3 per tenant.

#### 2.3.3 Head Teacher

Daily operational lead. Manages class setup, examinations schedule, report card sign-off, staff oversight, EMIS submission. Unlocks mark entry after deadline. Initiates bulk report card generation. Tech comfort: low to medium (see persona: John Ssemakula). Primary interface: web portal. Expected volume: 1–2 per tenant.

#### 2.3.4 Accounts Bursar

Manages all fee transactions. Enters cash and bank-transfer payments. Generates receipts. Produces fee collection reports and defaulter lists. Cannot approve refunds. Tech comfort: medium (see persona: Agnes Nakabugo). Primary interface: web portal. Expected volume: 1–3 per tenant.

#### 2.3.5 Class Teacher

Enters daily attendance and exam marks for assigned classes. Posts homework (Phase 2). Views class lists and timetables. Primary concern: speed and mobile access. Tech comfort: medium to high (see persona: David Okello). Phase 1 interface: web portal (mobile app deferred to Phase 6). Expected volume: 5–60 per tenant.

#### 2.3.6 Receptionist

Admits new students, updates student records, manages visitor log (out of Phase 1 scope). Limited financial visibility (no payment entry). Tech comfort: medium. Expected volume: 1–2 per tenant.

#### 2.3.7 Parent / Guardian

Views child's results, fee balance, and attendance. Receives automated SMS alerts. Does not enter data. Tech comfort: low (see persona: Grace Atuhaire). Phase 1: web portal only; mobile app from Phase 5. Expected volume: 100–2,000 per tenant. Key constraint: must function on low-end smartphones and intermittent 3G connections.

#### 2.3.8 Student

Views own timetable, results, fee balance (Phase 1 web portal). Tech comfort: variable. Expected volume: 100–2,000 per tenant.

### 2.4 Operating Environment

#### 2.4.1 Server Environment

| Parameter | Specification |
|---|---|
| Operating System | Ubuntu 22.04 LTS |
| PHP | 8.2 or later |
| Framework | Laravel 11 |
| Database | MySQL 8.x InnoDB, strict mode, `utf8mb4_unicode_ci` |
| Cache / Queue | Redis 7 (Laravel Horizon) |
| Search | Laravel Scout + Meilisearch |
| Object Storage | Wasabi (S3-compatible; recommended for e-learning file storage — $6/TB/month, no egress fees). AWS S3 remains available for generated PDFs and report storage. |
| CDN | AWS CloudFront |
| SSL/TLS | Let's Encrypt (TLS 1.3; TLS ≤ 1.1 rejected) |
| DNS | Cloudflare |

#### 2.4.2 Development Environment

| Parameter | Specification |
|---|---|
| OS | Windows 11 / WSL2 |
| Local Server | WAMP64 (MySQL 8.4.7) |
| Version Control | Git / GitHub |
| CI/CD | GitHub Actions |
| Code Quality | PHP CS Fixer, PHPStan level 8, ESLint, Prettier |
| Testing | Pest (backend), Vitest (frontend), Playwright (E2E) |

#### 2.4.3 Client Environment — Web Portal

- **Minimum supported browsers:** Chrome 110+, Firefox 110+, Safari 16+, Edge 110+
- **Minimum screen width:** 360 px (mobile web); optimised for 1,024 px+ (desktop)
- **JavaScript:** Required (React 18 SPA)
- **Network:** Must function on 3G (≥ 1 Mbps); offline PWA for attendance and mark entry on service worker
- **Frontend framework:** React 18 / TypeScript / Vite; UI: shadcn/ui + Tailwind CSS; state: Zustand

#### 2.4.4 Client Environment — Android (Phase 6 — noted here for architectural constraint)

- **Minimum Android version:** Android 8.0 (API level 26)
- **Language / UI:** Kotlin / Jetpack Compose
- **Architecture:** MVVM + Repository pattern
- **Offline:** Room database + WorkManager background sync
- **Offline capability for Phase 1 features:** PWA (web) handles offline attendance and mark entry until the Android app launches in Phase 6

### 2.5 Design and Implementation Constraints

The following constraints are binding. They are not negotiable and must be satisfied by every architectural and implementation decision.

#### C-001: Mandatory Tenant Isolation

Every database query against a tenant-scoped table **must** include `WHERE tenant_id = ?` using the value extracted from the authenticated JWT (`tenant_id` claim) or server-side session. Client-supplied `tenant_id` values in request bodies or URL parameters shall never be trusted. The Repository base class enforces this constraint. CI pipelines shall reject any `DB::statement()` or `DB::select()` call that does not include a `$tenantId` parameter binding.

*Aligned with:* `multi-tenant-saas-architecture` skill — Franchise Isolation Model.

#### C-002: Dual Authentication Architecture

Web portals (school workspace, super admin panel, end-user portal) shall use server-side PHP session authentication with the `academia_pro_` session prefix. Mobile apps (Phase 6+) and API clients shall use JWT authentication. The session prefix `academia_pro_` isolates session variables from any other application on the same host. JWT access tokens expire in 15 minutes; refresh tokens expire in 30 days with rotation on every refresh.

*Aligned with:* `dual-auth-rbac` skill — Session prefix system and JWT architecture.

*Note: `FR-RBAC-004` in the PRD stated 7 days for mobile refresh token. This SRS supersedes the PRD and adopts the 30-day standard from the `dual-auth-rbac` skill, which provides better mobile user experience while maintaining security through token rotation.*

#### C-003: Password Storage Standard

All user passwords shall be hashed with Argon2ID (memory_cost ≥ 65,536 KB, time_cost = 4, threads = 3) with a 32-byte random salt and a 64-character application pepper stored in the `PASSWORD_PEPPER` environment variable. bcrypt is prohibited. MD5 and SHA-1 are prohibited.

*Aligned with:* `dual-auth-rbac` skill — Password Security section.

#### C-004: Service/Repository Pattern

Business logic must not reside in Laravel Eloquent model classes or in controllers. All database access must go through Repository interfaces. Service classes orchestrate business logic and call Repository methods. Controllers are thin HTTP adapters only.

*Aligned with:* `_context/tech_stack.md` — Backend Architecture.

#### C-005: No Eloquent ORM in Business Logic

Eloquent may be used for migrations and seeders. Eloquent query builder methods are permitted inside Repository implementations. Eloquent model usage in Service classes or Controllers is prohibited.

#### C-006: Strict SQL Mode and Charset

MySQL must run in strict mode (`STRICT_TRANS_TABLES`). All tables use `ENGINE=InnoDB`, `CHARACTER SET utf8mb4`, `COLLATE utf8mb4_unicode_ci`. Composite indexes on `(tenant_id, <lookup_field>)` are mandatory on all tenant-scoped tables.

*Aligned with:* `mysql-best-practices` skill.

#### C-007: OpenAPI Specification Required Before Development

All API endpoints must be specified in an OpenAPI 3.1 document before frontend/mobile development begins. This resolves gap `HIGH-003` in `_context/gap-analysis.md`. The OpenAPI spec lives in `03-design-documentation/03-api-spec/`.

#### C-008: HTTPS Only in Production

The server shall redirect all HTTP requests to HTTPS. HSTS header (`max-age=31536000; includeSubDomains`) shall be set on all responses. TLS versions 1.0 and 1.1 are rejected at the web server configuration level.

#### C-009: Uganda-First Defaults

New tenant accounts with no explicit country configuration shall default to Uganda locale: 3-term calendar, Uganda Shilling (UGX), UNEB grading, EAT timezone (UTC+3), Africa's Talking SMS gateway.

### 2.6 Assumptions and Dependencies

#### 2.6.1 Assumptions

| ID | Assumption |
|---|---|
| A-001 | Each school will complete a one-time onboarding wizard (configure academic year, import student list, set fee structures) before first use. The system does not support retroactive data entry for periods before go-live. |
| A-002 | School administrators will watch module training videos before first use, per the Design Covenant in `_context/vision.md`. The UX is designed for trained users, not first-time discovery. |
| A-003 | Uganda schools operate on a 3-term calendar. No monthly billing model is supported in Phase 1. |
| A-004 | All monetary values in Phase 1 are in Uganda Shillings (UGX). Multi-currency is introduced in Phase 11. |
| A-005 | UNEB publishes its grading rules and sample mark sheets in a format accessible to the product team. `[CONTEXT-GAP: UNEB grading confirmation]` — contact UNEB per gap-analysis resource list before FR-EXM verification. |
| A-006 | MoES EMIS data dictionary is available and reviewed by the product team before FR-EMIS implementation. `[CONTEXT-GAP: MoES EMIS format]` — obtain from MoES per gap-analysis resource list. |
| A-007 | Phase 1 does not include SchoolPay API integration. Fees are recorded manually by the bursar. SchoolPay integration is Phase 2. |
| A-008 | The `dual-auth-rbac` skill's 30-day refresh token standard supersedes the 7-day value stated in `01-prd/06-feature-requirements.md FR-RBAC-004`. |

#### 2.6.2 Dependencies

| ID | Dependency | Risk if Unavailable |
|---|---|---|
| D-001 | Africa's Talking SMS gateway — Uganda sender ID approved | Automated SMS alerts (attendance, fee reminders) non-functional |
| D-002 | AWS S3 bucket configured and IAM credentials set | PDF report storage non-functional; PDF generation fails |
| D-003 | UNEB grading rules confirmed with UNEB | FR-EXM-003 through FR-EXM-006 cannot be verified |
| D-004 | MoES EMIS data dictionary obtained | FR-EMIS-001 cannot be implemented or verified |
| D-005 | Firebase Cloud Messaging (FCM) project configured | Push notification delivery for PWA attendance/mark entry non-functional |
| D-006 | Let's Encrypt certificate provisioned for production domain | HTTPS enforcement (C-008) non-functional in production |
| D-007 | `PASSWORD_PEPPER` environment variable set (64+ chars) in production `.env` | All password authentication broken |
