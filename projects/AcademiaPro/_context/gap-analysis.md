# Gap Analysis — Academia Pro (Section 20 from Master Document)

All 8 HIGH-priority gaps must be resolved before Phase 1 development begins. MEDIUM gaps must be resolved before Phase 2. LOW gaps can be resolved during build.

---

## HIGH Priority Gaps (Resolve Before Development Begins)

### HIGH-001: Security Architecture Specification

**Gap:** No document specifies how `tenant_id` is enforced at every application layer (HTTP middleware, service layer, repository layer, raw query exceptions, job queue, event listeners, API responses).

**Resolution Required:**
- Write a security architecture document covering:
  1. JWT middleware: extract `tenant_id` from token; bind to request context
  2. Repository base class: mandatory `where('tenant_id', $tenantId)` appended to every query builder chain
  3. Model-level global scope: Eloquent global scope as secondary defence
  4. Raw query audit: CI check that no `DB::statement()` or `DB::select()` calls exist without `tenant_id` parameter
  5. Queue jobs: `tenant_id` serialised into every job payload; job handler re-binds tenant context on execution
  6. Event listeners: same as queue jobs
  7. API response audit: middleware strips any response key named `tenant_id` from outbound JSON (internal implementation detail)
  8. Super Admin bypass: explicit `withoutTenantScope()` method on Repository base class, audited, restricted to Super Admin role only

**Owner:** Peter (architecture decision) → to be written in `03-design-documentation/01-hld/02-security-architecture.md`
**Status:** [x] ✅ Resolved 2026-04-03 — Full implementation specification written in `03-design-documentation/01-hld/02-security-architecture.md`. Covers all 8 required areas: JWT middleware, Repository base class, Eloquent global scope, CI raw query audit, queue job isolation, event listener isolation, API response sanitisation, Super Admin bypass with audit logging.

---

### HIGH-002: Consolidated Entity Relationship Diagram (ERD)

**Gap:** No ERD exists. The master document describes entities textually across 20 sections with no unified schema view.

**Resolution Required:** Draw a consolidated ERD covering all Phase 1 entities minimum:
- `tenants`, `users`, `roles`, `permissions`, `role_permissions`, `user_roles`
- `global_students`, `student_identifiers`, `school_enrollments`
- `academic_years`, `terms`, `classes`, `streams`, `subjects`, `timetables`
- `fee_structures`, `fee_payments`, `receipts`, `payment_channels`
- `attendance_records`
- `exams`, `exam_results`, `grading_schemes`
- `report_cards`, `report_card_entries`
- `notices`, `homework`, `downloads`, `calendar_events`
- `audit_logs`

**Owner:** Peter → to be written in `03-design-documentation/04-database-design/01-erd.md`
**Status:** [ ] Not started

---

### HIGH-003: OpenAPI Specification

**Gap:** No API contract exists. Without an OpenAPI spec, frontend and mobile teams cannot develop in parallel, and API tests cannot be auto-generated.

**Resolution Required:** Write OpenAPI 3.1 spec for all Phase 1 endpoints:
- Authentication: POST /auth/login, POST /auth/refresh, POST /auth/logout
- Students: CRUD + search + NIN/LIN lookup + transfer
- Fees: fee structures, payment recording, receipt generation, reconciliation trigger
- Attendance: daily entry, bulk entry, monthly summary
- Exams: exam creation, mark entry, grade computation, result publication
- Reports: report card generation (single + bulk), PDF download
- Users/Roles: user management, role assignment

**Owner:** Peter → to be written in `03-design-documentation/03-api-spec/`
**Status:** [x] ✅ Resolved 2026-04-03 — Full OpenAPI 3.1 specification written across 12 files in `03-design-documentation/03-api-spec/`. Covers all 49 Phase 1 FRs: authentication (FR-AUTH-002–004), tenant management (FR-TNT-001–003), students (FR-SIS-001–005), academics (FR-ACA-001–004), fees (FR-FEE-001–007), attendance (FR-ATT-001–004), examinations (FR-EXM-001–008), reports (FR-RPT-001–004), RBAC (FR-RBAC-001–005), EMIS (FR-EMIS-001), audit (FR-AUD-001), and shared schemas (11-schemas.yaml).

---

### HIGH-004: Academic Year Lifecycle Management

**Gap:** No specification for what happens when an academic year ends: class promotion logic, student carry-forward, fee structure reset, historical record locking, repeat-student handling.

**Resolution Required:**
1. Year-end processing workflow: which records are promoted, which are archived, which are cloned for the new year
2. Class promotion rules: automatic (all students in P5 → P6) or manual (head teacher approves individually)
3. Repeat student handling: student stays in same class; previous year's records remain linked
4. Fee structure carry-forward: new term fee structures default to previous year's values; head teacher adjusts before first billing run
5. Historical record locking: all marks, attendance, and payment records for a completed term are locked (immutable) after term close date + 30 days

**Owner:** Peter → to be written in `_context/business_rules.md` (Section: Year-End Rules) and `02-requirements-engineering/01-srs/`
**Status:** [x] ✅ Resolved 2026-03-29 — Design approved and documented in `docs/plans/2026-03-29-academia-pro-student-promotion-portability-design.md`. Business rules BR-PROM-001 through BR-PROM-007 and BR-DEPART-001 through BR-DEPART-004 added to `_context/business_rules.md`. SRS amendment required: add FR-PROM and FR-DEPART groups.

---

### HIGH-005: Full RBAC Permission Matrix

**Gap:** Role names are listed but no permission matrix exists. Without it, the middleware cannot be built and the system cannot be secure.

**Resolution Required:** Produce a permission matrix table with:
- Rows: all actions (e.g., `students:create`, `students:view`, `fees:record-payment`, `fees:approve-refund`, `marks:enter`, `marks:publish`, `reports:generate`, `users:manage`, `settings:configure`)
- Columns: all roles (Super Admin, Owner/Director, Head Teacher, Class Teacher, Accounts Bursar, Receptionist, Librarian, Transport Manager, Hostel Warden, Parent, Student)
- Cell: ✓ (allowed), ✗ (denied), ✓* (allowed with conditions, e.g., own class only)

**Owner:** Peter → to be written in `02-requirements-engineering/03-stakeholder-analysis/01-rbac-matrix.md`
**Status:** [x] ✅ Resolved 2026-03-29 — `02-requirements-engineering/03-stakeholder-analysis/01-rbac-matrix.md`

---

### HIGH-006: Double-Payment Prevention Rules

> **Scope update (2026-03-28):** SchoolPay integration moves to Phase 2. The webhook-specific aspects of this gap apply in Phase 2. The Phase 1 scope is: idempotency on manual cash entries (prevent bursar recording the same payment twice via UI). The full SchoolPay webhook idempotency spec is still required but will be resolved before Phase 2 development begins.
>
> **Status update (2026-03-29):** Phase 1 manual idempotency rule fully specified in SRS `FR-FEE-002` (5-minute window duplicate detection) and `FR-FEE-003` (receipt immutability). Phase 2 webhook idempotency spec remains pending.

**Gap:** BR-FEE-005 states the rule but does not specify the full implementation: idempotency key schema, webhook signature verification, database-level unique constraints, response codes.

**Resolution Required:**
1. Idempotency key: SchoolPay transaction reference stored as `UNIQUE` constraint on `fee_payments.external_reference`
2. Webhook signature: HMAC-SHA256 of payload using SchoolPay merchant secret; verified before any DB write
3. Race condition: database-level `INSERT IGNORE` or `ON DUPLICATE KEY UPDATE status='duplicate'` to handle concurrent webhook replays
4. Response to duplicate: HTTP 200 with `{"status": "duplicate", "original_receipt_id": "..."}` (do not return 4xx — SchoolPay may retry on error responses)
5. Alert: if the same payment reference arrives more than 3 times in 10 minutes, alert Super Admin (possible replay attack)

**Owner:** Peter → to be written in `04-development-artifacts/01-technical-spec/01-payment-idempotency.md`
**Status:** [ ] Not started

---

### HIGH-007: Data Migration Specification

**Gap:** Schools migrating from ShuleKeeper, Excel, or paper have no supported migration path. Without this, pilot school onboarding will be entirely manual.

**Resolution Required:**
1. Supported import formats: Excel (.xlsx), CSV
2. Student import template: define column headers, required vs. optional fields, validation rules, error reporting format
3. Fee history import: define whether historical payments are imported or only opening balances
4. Attendance import: not supported (historical attendance not imported — only from go-live date)
5. Mark / results import: not supported in Phase 1 (historical results not imported)
6. Validation error handling: import halts on first error vs. skip-and-report mode (skip-and-report recommended)
7. Import UI: bursar-facing wizard with step-by-step column mapping and preview before commit

**Owner:** Peter → to be written in `04-development-artifacts/01-technical-spec/02-data-migration.md`
**Status:** [x] ✅ Resolved 2026-04-03 — Full data migration specification written in `04-development-artifacts/01-technical-spec/02-data-migration.md`. Covers: supported formats (xlsx/csv), student import template (13 columns), 2,000-row limit, 4-step import wizard, skip-and-report error handling, NIN/LIN cross-school matching, fee history exclusion policy, audit logging, and implementation notes (job config, batch processing, Excel date handling, atomic global student creation).

---

### HIGH-008: Uganda Data Protection and Privacy Act 2019 Compliance

**Gap:** No compliance document exists. The PDPO 2019 imposes obligations on data controllers processing Ugandan personal data.

**Resolution Required:**
1. Data Controller registration: register Chwezi Core Systems with the Personal Data Protection Office (PDPO) Uganda
2. Privacy Notice: draft and publish Privacy Policy covering: what data is collected, why, how long it is retained, who it is shared with, and data subject rights
3. Data Processing Agreement (DPA): provide each school with a DPA to sign, establishing the school as Data Controller and Chwezi Core Systems as Data Processor
4. Data Subject Rights implementation:
   - Right of Access: export all personal data for a named student in JSON format
   - Right to Erasure: soft-delete pathway with hard-delete after retention period
   - Right to Correction: any role with student:edit permission can correct personal data (logged)
5. Data Retention Policy: see BR-DATA-RETENTION (to be added to business_rules.md) — student records retained for 7 years post-graduation per Uganda education regulations
6. Breach Notification: if personal data breach is detected, notify PDPO Office within 72 hours and affected data subjects without undue delay
7. Health data (Phase 7): special category data under PDPO — additional safeguards required (explicit consent, restricted access, enhanced audit logging)

**Action:** Download Uganda Data Protection and Privacy Act 2019 from ULRC (ulrc.go.ug).

**Owner:** Peter → to be written in `09-governance-compliance/03-compliance/01-pdpo-compliance.md`
**Status:** [x] ✅ Resolved 2026-04-03 — Full PDPO compliance document written in `09-governance-compliance/03-compliance/01-pdpo-compliance.md`. Covers: role mapping (Controller/Processor), 5 external actions required by Peter, lawful basis per data category, 7-year retention policy, all 4 data subject rights (access, correction, erasure, objection), breach notification procedure (24h to school / 72h to PDPO), technical safeguards (TLS 1.3, AES-256, RBAC), DPA summary, privacy notice minimum content, Phase 7 health data special category controls, and compliance checklist.

---

## MEDIUM Priority Gaps (Resolve Before Phase 2 Begins)

1. Timetable conflict detection algorithm specification
2. Library barcode/QR integration spec
3. Transport GPS integration spec (optional module)
4. Hostel room capacity management rules
5. Communication rate limiting (SMS quota management per school per month)
6. Homework submission and grading workflow
7. Download Centre access control matrix (who sees which documents)
8. Certificate template customisation spec
9. Front CMS content moderation rules
10. SchoolPay multi-school merchant account management (for school chains)
11. Offline PWA sync conflict resolution rules (what happens when teacher submits offline attendance that conflicts with a later online entry)
12. ~~EMIS export format validation spec (validate against MoES EMIS data dictionary)~~ — ✅ Resolved 2026-04-03 — EMIS data dictionary created from 5 official MoES documents (EMIS User Manual Primary April 2023, EMIS User Manual Secondary April 2023, Learner EMIS Registration Form 2023, Staff EMIS Registration Form 2024, International Learner EMIS Registration Form). Full field specifications documented in `_context/emis-data-dictionary.md`.

---

## LOW Priority Gaps (Resolve During Build)

1. Report card comment templates and character limits
2. Timetable print format (A4 landscape)
3. Exam seating arrangement generator
4. Bulk SMS template management
5. School logo and branding customisation
6. Parent-teacher meeting scheduling
7. Staff payroll calculation edge cases (overtime, deductions)
8. Library fine calculation edge cases (public holidays, weekends)
9. Transport fee proration for mid-term joiners
10. Hostel checkout procedure and deposit refund rules
11. Front CMS SEO metadata fields

---

## Resource Action List (12 Items from Master Document)

- [ ] Download Uganda Data Protection and Privacy Act 2019 from ULRC (ulrc.go.ug) — HIGH-008
- [x] Contact UNEB for their candidate registration manual and sample mark sheets — HIGH-001 grading validation — ✅ Resolved 2026-04-03 — UNEB registration core fields documented in `_context/emis-data-dictionary.md`; exact file format requires UNEB liaison.
- [x] Get MoES EMIS data dictionary and fee structure approval form — EMIS integration spec — ✅ Resolved 2026-04-03 — EMIS data dictionary created from 5 official MoES documents (EMIS User Manual Primary April 2023, EMIS User Manual Secondary April 2023, Learner EMIS Registration Form 2023, Staff EMIS Registration Form 2024, International Learner EMIS Registration Form). Full field specifications documented in `_context/emis-data-dictionary.md`.
- [ ] Contact SchoolPay for merchant API documentation and sandbox credentials — **Phase 2 only, after Phase 1 go-live** (decision 2026-03-28: approach SchoolPay after the ERP proves its value independently)
- [ ] Apply for MTN MoMo Developer account (momodeveloper.mtn.com) — Phase 3 prep
- [ ] Apply for Airtel Money Uganda Merchant API access — Phase 3 prep
- [ ] Engage BoU for Payment Systems Operator licence pre-application guidance — Phase 3–4 planning
- [ ] Register software copyright with URSB under Uganda Copyright Act 2006 — before Phase 8 go-live
- [ ] Draft Data Processing Agreements for pilot schools — before Phase 8 go-live
- [ ] Internal decision: class promotion — automatic or manual? — HIGH-004
- [ ] Internal decision: which cloud hosting provider for go-live — AWS, Azure, or local Uganda data centre? — affects PDPO data residency
- [ ] Internal decision: USSD short code provider — Africa's Talking or direct UCC application — Phase 11 prep
