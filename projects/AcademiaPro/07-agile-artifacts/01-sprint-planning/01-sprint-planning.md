# Sprint Planning — AcademiaPro Phase 1

## Document Control

| Field | Value |
|---|---|
| Project | AcademiaPro |
| Phase | Phase 1 — Core Web Application |
| Methodology | Hybrid (Water-Scrum-Fall) |
| Sprint Duration | 2 weeks (10 working days) |
| Team Size | 1 (solo developer — Peter, Chwezi Core Systems) |
| Total FRs in Scope | 49 (FR-AUTH through FR-AUD) |
| Planned Sprints | Sprint Zero + Sprints 1 through 8 + Post-Sprint 8 UAT |
| Estimated Duration | 18 weeks (Sprint Zero: 1 week; Sprints 1–8: 16 weeks; UAT: 1+ weeks) |

---

## Sprint Cadence and Ceremonies

| Ceremony | Frequency | Duration | Participants |
|---|---|---|---|
| Sprint Planning | Day 1 of each sprint | 1 hour | Peter (dev) |
| Daily Stand-up Log | Daily | 10-minute written log in `docs/standups/` | Peter |
| Sprint Review / Demo | Last day of each sprint | 30 minutes recorded screen demo | Peter |
| Sprint Retrospective | Last day of each sprint | 15-minute written retro in `docs/retros/` | Peter |
| Phase Gate Review | After Sprint 8 + UAT | Formal sign-off against Phase 1 gate criteria | Peter |

> Solo developer adaptation: ceremonies are written logs and screen recordings rather than meetings. The discipline of documenting each ceremony is preserved to maintain audit traceability per the Water-Scrum-Fall methodology.

---

## Velocity Assumptions

| Parameter | Value | Rationale |
|---|---|---|
| Story points per sprint | 20–25 SP | Solo developer, 2-week sprints, estimated from complexity not hours |
| Sprint Zero capacity | 10–12 SP | 1-week sprint; infrastructure tasks carry high uncertainty |
| Buffer allocation | Sprint 8 is 100% buffer | No new features; integration testing, performance testing, bug fixes |
| Total story points (Phase 1) | ~180 SP estimated | 49 FRs across 8 feature sprints |

---

## Sprint Zero — Foundation (1 Week)

**Goal:** Establish the development environment, database schema, CI/CD pipeline, and UI framework so that Sprint 1 begins with zero infrastructure blockers.

**Duration:** 1 week (5 working days).

| Task ID | Task | Story Points | Acceptance Criteria |
|---|---|---|---|
| S0-001 | Initialise Laravel 11 project with PHP 8.2+ | 2 | `php artisan serve` returns HTTP 200; PSR-12 enforced via PHP CS Fixer |
| S0-002 | Configure MySQL 8.x database with strict mode, utf8mb4, InnoDB | 1 | `SHOW VARIABLES LIKE 'sql_mode'` returns strict mode; `SHOW CREATE DATABASE` shows utf8mb4 |
| S0-003 | Run baseline migrations: `tenants`, `tbl_users`, `tbl_audit_log` | 2 | `php artisan migrate` succeeds; tables exist with `tenant_id` columns where applicable |
| S0-004 | Configure Redis 7 for cache and queue drivers | 1 | `php artisan queue:work` processes a test job; `Cache::put()` / `Cache::get()` round-trips |
| S0-005 | Set up GitHub Actions CI pipeline: lint, PHPStan level 8, PHPUnit | 3 | Push to `main` triggers pipeline; pipeline passes with zero errors |
| S0-006 | Install React 18 / TypeScript / Vite frontend scaffold | 2 | `npm run dev` serves the Vite dev server; TypeScript compilation succeeds |
| S0-007 | Install shadcn/ui + Tailwind CSS; configure Tabler dashboard layout | 2 | Login page renders with shadcn/ui components; Tailwind classes apply correctly |
| S0-008 | Seed Super Admin user and default Uganda tenant for development | 1 | `php artisan db:seed` creates 1 Super Admin user and 1 tenant with `status = active` |

**Total:** ~14 SP (1 week).

**Sprint Zero Exit Criteria:**

- **SP-001** Laravel project boots and serves HTTP 200
- **SP-002** MySQL strict mode confirmed
- **SP-003** CI pipeline green on push to `main`
- **SP-004** Frontend dev server renders the Tabler dashboard shell
- **SP-005** Super Admin can log in to a blank dashboard (no module functionality yet)

---

## Sprint 1 — Authentication and Tenant Management (2 Weeks)

**Goal:** Deliver secure authentication (web + API) and Super Admin tenant lifecycle management so that all subsequent sprints operate within a multi-tenant, role-scoped context.

**FR Scope:** FR-AUTH-001 through FR-AUTH-006 (6 FRs) + FR-TNT-001 through FR-TNT-003 (3 FRs) = 9 FRs.

| FR ID | Description | Story Points | Dependencies |
|---|---|---|---|
| FR-AUTH-001 | Web session login (Argon2ID, CSRF, account lock after 5 failures) | 5 | S0-003 (users table) |
| FR-AUTH-002 | API / mobile JWT login (access + refresh tokens, device tracking) | 5 | FR-AUTH-001 |
| FR-AUTH-003 | JWT token refresh with rotation and revocation | 3 | FR-AUTH-002 |
| FR-AUTH-004 | Session logout (web + API) | 2 | FR-AUTH-001, FR-AUTH-002 |
| FR-AUTH-005 | Idle session timeout (30 minutes) | 2 | FR-AUTH-001 |
| FR-AUTH-006 | Super Admin MFA (TOTP) | 3 | FR-AUTH-001 |
| FR-TNT-001 | Tenant provisioning (create school, owner account, welcome email) | 3 | FR-AUTH-001 |
| FR-TNT-002 | Tenant activation (pending to active) | 2 | FR-TNT-001 |
| FR-TNT-003 | Tenant suspension | 2 | FR-TNT-001 |

**Total:** ~27 SP.

**Key Deliverables:**

- **SP-006** Login page (web) with lockout behaviour
- **SP-007** JWT endpoint for mobile/API clients
- **SP-008** Token refresh and revocation
- **SP-009** MFA challenge for Super Admin panel
- **SP-010** Tenant CRUD in Super Admin panel
- **SP-011** Welcome email on tenant creation
- **SP-012** Tenant status transitions: pending, active, suspended

**Sprint 1 Exit Criteria:**

- **SP-013** All 6 FR-AUTH acceptance criteria pass (Playwright + PHPUnit)
- **SP-014** All 3 FR-TNT acceptance criteria pass
- **SP-015** JWT tokens decode with correct `tenant_id` claim
- **SP-016** Account lockout triggers after 5 failed attempts
- **SP-017** Super Admin MFA blocks dashboard access until TOTP verified
- **SP-018** CI pipeline green

---

## Sprint 2 — Student Information System (2 Weeks)

**Goal:** Deliver the full student lifecycle — admission, enrollment, cross-school lookup, transfer, and retention lock — establishing the global student identity architecture.

**FR Scope:** FR-SIS-001 through FR-SIS-005 (5 FRs).

| FR ID | Description | Story Points | Dependencies |
|---|---|---|---|
| FR-SIS-001 | Student admission (40+ fields, NIN/LIN, passport photo upload) | 8 | Sprint 1 (auth, tenant context) |
| FR-SIS-002 | Cross-school enrollment via NIN/LIN lookup | 5 | FR-SIS-001, BR-STU-001 through BR-STU-004 |
| FR-SIS-003 | Student search (Meilisearch integration) | 3 | FR-SIS-001 |
| FR-SIS-004 | Transfer out (departure record, reason code, read-only lock) | 3 | FR-SIS-001, BR-DEPART-001 through BR-DEPART-004 |
| FR-SIS-005 | Retention lock (prevent deletion of enrolled student) | 2 | FR-SIS-001 |

**Total:** ~21 SP.

**Key Deliverables:**

- **SP-019** Student admission form (40+ fields with validation)
- **SP-020** `global_students` and `school_enrollments` table separation
- **SP-021** NIN/LIN cross-school lookup (no duplicate UIDs)
- **SP-022** Meilisearch-powered student search
- **SP-023** Transfer-out workflow with departure reason codes
- **SP-024** Student record immutability after departure

**Sprint 2 Exit Criteria:**

- **SP-025** Student admission creates both `global_students` and `school_enrollments` records
- **SP-026** NIN/LIN lookup returns existing global student without duplication (BR-STU-001)
- **SP-027** Single-school active enrollment enforced (BR-STU-004)
- **SP-028** Departed student records are read-only (BR-DEPART-004)
- **SP-029** Meilisearch index returns results within 200 ms (P99)
- **SP-030** CI pipeline green

---

## Sprint 3 — Academics Setup (2 Weeks)

**Goal:** Define the school structure — academic years, terms, classes/streams, subjects, curricula, and timetables — so that downstream modules (Fees, Attendance, Examinations) can reference a configured academic context.

**FR Scope:** FR-ACA-001 through FR-ACA-004 (4 FRs).

| FR ID | Description | Story Points | Dependencies |
|---|---|---|---|
| FR-ACA-001 | Academic year lifecycle (create, open, close, promotion wizard) | 5 | Sprint 1 (tenant), BR-PROM-001 through BR-PROM-007 |
| FR-ACA-002 | Class and stream management (promotes-to config) | 3 | FR-ACA-001 |
| FR-ACA-003 | Curriculum type configuration (Thematic P1–P3, standard P4–P7, O-Level, A-Level) | 3 | FR-ACA-002 |
| FR-ACA-004 | Timetable builder (per class per term) | 5 | FR-ACA-002, FR-ACA-003 |

**Total:** ~16 SP.

**Key Deliverables:**

- **SP-031** Academic year CRUD with term dates (3-term Uganda calendar)
- **SP-032** Year-Start Promotion Wizard (BR-PROM-001 through BR-PROM-007)
- **SP-033** Class/stream CRUD with "Promotes To" configuration
- **SP-034** Curriculum type selector per class level
- **SP-035** Timetable grid builder (days x periods)

**Sprint 3 Exit Criteria:**

- **SP-036** Academic year creates 3 terms automatically (BR-CAL-001)
- **SP-037** Promotion wizard blocks Term 1 opening until all classes processed (BR-PROM-001)
- **SP-038** Final-year classes (P7, S.4, S.6) have `promotes_to = null` (BR-PROM-002)
- **SP-039** Curriculum type determines available grading scales
- **SP-040** Timetable renders correctly for a class with 8 periods per day
- **SP-041** CI pipeline green

---

## Sprint 4 — Fee Management and SchoolPay Integration (2 Weeks)

**Goal:** Deliver term-based fee billing, manual payment recording, receipt generation, fee reminders, refund workflow, and the SchoolPay webhook integration for automated payment sync.

**FR Scope:** FR-FEE-001 through FR-FEE-007 (7 FRs).

| FR ID | Description | Story Points | Dependencies |
|---|---|---|---|
| FR-FEE-001 | Fee structure definition (per class, per term, UGX) | 3 | Sprint 3 (academic year, classes) |
| FR-FEE-002 | Manual payment recording (cash/bank, partial payments, KUPAA model) | 5 | FR-FEE-001, BR-FEE-002, BR-FEE-005 |
| FR-FEE-003 | Auto-generated sequential receipts | 3 | FR-FEE-002, BR-FEE-004 |
| FR-FEE-004 | Fee reminders (D-7, D-1, D+7 auto-send via SMS) | 3 | FR-FEE-001, BR-FEE-006 |
| FR-FEE-005 | Refund workflow (bursar initiate, owner approve) | 3 | FR-FEE-002, BR-FEE-007 |
| FR-FEE-006 | Fee balance tracking and arrears carry-forward | 2 | FR-FEE-001, BR-FEE-003 |
| FR-FEE-007 | Financial reports (collection summary, defaulters, term reconciliation) | 3 | FR-FEE-002 |

**Total:** ~22 SP.

**SchoolPay Integration Tasks** (bundled with FR-FEE scope):

| Task ID | Task | Story Points |
|---|---|---|
| SP-001 | SchoolPay API client service (student payment codes) | 3 |
| SP-002 | Webhook receiver for payment notifications | 3 |
| SP-003 | Nightly reconciliation polling job | 2 |
| SP-004 | Double-payment prevention (5-minute window, BR-FEE-005) | 2 |

**SchoolPay Total:** ~10 SP.

**Combined Sprint 4 Total:** ~32 SP. This sprint is overloaded by ~7–12 SP. Mitigation: SchoolPay integration tasks SP-003 and SP-004 may spill into Sprint 5 if velocity is below 25 SP. The manual fee workflow (FR-FEE-001 through FR-FEE-007) is the priority; SchoolPay auto-sync is secondary.

**Sprint 4 Exit Criteria:**

- **SP-042** Fee structure created for a class/term in UGX
- **SP-043** Partial payment accepted with zero minimum floor (BR-FEE-002)
- **SP-044** Receipt auto-generated with sequential number (BR-FEE-004)
- **SP-045** Duplicate payment within 5-minute window rejected (BR-FEE-005)
- **SP-046** Refund requires owner approval (BR-FEE-007)
- **SP-047** Fee reminders fire at D-7, D-1, D+7 (configurable, BR-FEE-006)
- **SP-048** SchoolPay webhook processes a test payment notification
- **SP-049** Financial reports generate correctly for a test dataset
- **SP-050** CI pipeline green

---

## Sprint 5 — Attendance and Examinations Core (2 Weeks)

**Goal:** Deliver daily attendance entry with parent alerts, and lay the examination foundation — exam configuration, mark entry, and the mark-unlock workflow.

**FR Scope:** FR-ATT-001 through FR-ATT-004 (4 FRs) + FR-EXM-001, FR-EXM-002, FR-EXM-003 (3 FRs) = 7 FRs.

| FR ID | Description | Story Points | Dependencies |
|---|---|---|---|
| FR-ATT-001 | Daily attendance entry (Present/Absent/Late/Excused) | 3 | Sprint 2 (students), Sprint 3 (classes) |
| FR-ATT-002 | Absence alert (auto-SMS after N consecutive absences) | 3 | FR-ATT-001, BR-ATT-002 |
| FR-ATT-003 | Attendance amendment (48-hour teacher window, Head Teacher override) | 3 | FR-ATT-001, BR-ATT-003 |
| FR-ATT-004 | Monthly attendance report | 2 | FR-ATT-001 |
| FR-EXM-001 | Exam configuration (exam type, subjects, max marks) | 3 | Sprint 3 (curriculum type) |
| FR-EXM-002 | Mark entry (per student per subject, out-of-range rejection) | 5 | FR-EXM-001, BR-UNEB-005 |
| FR-EXM-003 | Mark unlock workflow (teacher request, Head Teacher approval) | 3 | FR-EXM-002 |

**Total:** ~22 SP.

**Key Deliverables:**

- **SP-051** Attendance entry grid (class view, one-click per student)
- **SP-052** Auto-SMS to parent after 3 consecutive absences (Africa's Talking)
- **SP-053** Attendance amendment audit trail
- **SP-054** Monthly attendance summary report
- **SP-055** Exam configuration CRUD
- **SP-056** Mark entry sheet with real-time validation (reject marks > max)
- **SP-057** Mark-unlock request/approval workflow

**Sprint 5 Exit Criteria:**

- **SP-058** Attendance recorded for a class of 50 students within 2 minutes
- **SP-059** 3 consecutive absences trigger SMS to parent/guardian (BR-ATT-002)
- **SP-060** Amendment after 48 hours requires Head Teacher role (BR-ATT-003)
- **SP-061** Marks exceeding configured maximum are rejected at API layer (BR-UNEB-005)
- **SP-062** Mark-unlock requires Head Teacher approval
- **SP-063** CI pipeline green

---

## Sprint 6 — Examinations Grading and Report Cards (2 Weeks)

**Goal:** Deliver the UNEB grading engine for all 4 curriculum types and auto-generated report cards, completing the academic cycle from mark entry to printed report.

**FR Scope:** FR-EXM-004 through FR-EXM-008 (5 FRs) + FR-RPT-001 through FR-RPT-004 (4 FRs) = 9 FRs.

| FR ID | Description | Story Points | Dependencies |
|---|---|---|---|
| FR-EXM-004 | PLE grading engine (4-subject aggregate, divisions) | 3 | FR-EXM-002, BR-UNEB-001 |
| FR-EXM-005 | UCE O-Level grading engine (D1–F9, aggregate divisions) | 3 | FR-EXM-002, BR-UNEB-002 |
| FR-EXM-006 | UACE A-Level grading engine (principal/subsidiary points) | 3 | FR-EXM-002, BR-UNEB-003 |
| FR-EXM-007 | Thematic Curriculum grading (P1–P3, HC/C/NYC descriptors) | 2 | FR-EXM-002, BR-UNEB-004 |
| FR-EXM-008 | UNEB exam registration data export | 2 | FR-EXM-004 through FR-EXM-006 |
| FR-RPT-001 | Single student report card (auto-generated, PDF export) | 5 | FR-EXM-004 through FR-EXM-007 |
| FR-RPT-002 | Bulk report card generation (entire class) | 3 | FR-RPT-001 |
| FR-RPT-003 | School-level performance summary | 2 | FR-EXM-004 through FR-EXM-007 |
| FR-RPT-004 | Head Teacher comments on report cards | 1 | FR-RPT-001 |

**Total:** ~24 SP.

**Key Deliverables:**

- **SP-064** UNEB grading engine: PLE, UCE, UACE, Thematic (4 algorithms)
- **SP-065** Grade computation unit tests with 100% coverage against UNEB rules
- **SP-066** UNEB export file generation
- **SP-067** Single student report card (PDF) with grades, comments, school logo
- **SP-068** Bulk report card generation (200 students within 120 seconds per quality target)
- **SP-069** School performance summary dashboard
- **SP-070** Head Teacher comment entry per student

**Sprint 6 Exit Criteria:**

- **SP-071** PLE aggregate computation matches BR-UNEB-001 division boundaries exactly
- **SP-072** UCE aggregate computation matches BR-UNEB-002 division boundaries exactly
- **SP-073** UACE points computation matches BR-UNEB-003 rules exactly
- **SP-074** Thematic grading returns HC/C/NYC descriptors only (BR-UNEB-004)
- **SP-075** 100% unit test coverage on all 4 grading algorithms
- **SP-076** Single report card generates within 3,000 ms (quality target)
- **SP-077** Bulk generation of 200 report cards completes within 120 seconds
- **SP-078** UNEB export file validates against expected format
- **SP-079** CI pipeline green

---

## Sprint 7 — RBAC, EMIS Export, and Audit Trail (2 Weeks)

**Goal:** Deliver the full RBAC permission system, the MoES/EMIS government data export, and the immutable audit trail — closing all remaining Phase 1 functional requirements.

**FR Scope:** FR-RBAC-001 through FR-RBAC-005 (5 FRs) + FR-EMIS-001 (1 FR) + FR-AUD-001 (1 FR) = 7 FRs.

| FR ID | Description | Story Points | Dependencies |
|---|---|---|---|
| FR-RBAC-001 | Permission resolution engine (role + custom overrides) | 5 | Sprint 1 (users, tenant) |
| FR-RBAC-002 | Role assignment per school per user | 3 | FR-RBAC-001, BR-RBAC-001 |
| FR-RBAC-003 | User invitation workflow (email invite, role pre-assignment) | 3 | FR-RBAC-002 |
| FR-RBAC-004 | Session expiry enforcement by role | 2 | FR-AUTH-005, FR-RBAC-001 |
| FR-RBAC-005 | Super Admin cross-tenant audit logging | 2 | FR-RBAC-001, BR-MT-003 |
| FR-EMIS-001 | EMIS government export (MoES-specified format) | 3 | Sprint 2 (students), Sprint 3 (academics) |
| FR-AUD-001 | Immutable audit trail (create/update/delete on all sensitive entities) | 5 | All prior sprints |

**Total:** ~23 SP.

**Key Deliverables:**

- **SP-080** Permission resolution: 60+ permissions x 8 standard roles (per RBAC matrix)
- **SP-081** Custom role creation per school
- **SP-082** User invitation email with role pre-assignment
- **SP-083** Role-scoped session timeout rules
- **SP-084** Super Admin cross-tenant read logging (BR-MT-003)
- **SP-085** EMIS bulk export in MoES-specified format (XML/CSV)
- **SP-086** Immutable audit log: user_id, tenant_id, timestamp, before/after values on all student, fee, and health records

**Sprint 7 Exit Criteria:**

- **SP-087** Permission resolution returns correct allow/deny for all 60+ permissions per role
- **SP-088** No user can assign a role with higher privilege than their own (BR-RBAC-002)
- **SP-089** Invited user receives email and can register with pre-assigned role
- **SP-090** Super Admin cross-tenant reads are logged with access reason (BR-MT-003)
- **SP-091** EMIS export generates valid file for a school with 500 students
- **SP-092** Audit log captures before/after values for all create/update/delete operations
- **SP-093** Audit log records are append-only (no update/delete permitted on `tbl_audit_log`)
- **SP-094** CI pipeline green

---

## Sprint 8 — Integration Testing, Performance Testing, and Hardening (2 Weeks)

**Goal:** No new features. Conduct end-to-end integration testing across all 49 FRs, performance testing against quality targets, security hardening, and bug fixes.

**FR Scope:** 0 new FRs. All 49 existing FRs under regression testing.

| Task ID | Task | Story Points | Acceptance Criteria |
|---|---|---|---|
| S8-001 | End-to-end integration test suite (Playwright): admission through report card | 5 | All critical user flows pass |
| S8-002 | Performance testing (k6): API P95 ≤ 500 ms under 200 concurrent requests | 3 | k6 report shows P95 ≤ 500 ms for all CRUD endpoints |
| S8-003 | Bulk report card load test: 200 students within 120 seconds | 2 | Timed test passes |
| S8-004 | UNEB grading accuracy test: 500 students within 5 seconds | 2 | PHPUnit timed test passes |
| S8-005 | Security audit: OWASP Top 10 scan, tenant isolation verification | 3 | Zero critical or high findings |
| S8-006 | Multi-tenant isolation test: tenant A cannot access tenant B data | 3 | Cross-tenant query returns 0 records for all endpoints |
| S8-007 | Bug fix backlog (accumulated from Sprints 1–7) | 5 | All P1/P2 bugs resolved |
| S8-008 | CI/CD pipeline for staging environment deployment | 2 | Push to `staging` branch deploys to staging server |

**Total:** ~25 SP.

**Sprint 8 Exit Criteria:**

- **SP-095** All 49 FRs have passing automated tests (PHPUnit + Playwright)
- **SP-096** Backend test coverage ≥ 80% line coverage
- **SP-097** UNEB grading engine test coverage = 100%
- **SP-098** Fee calculation logic test coverage = 100%
- **SP-099** API P95 response time ≤ 500 ms (k6 report)
- **SP-100** Bulk report card generation ≤ 120 seconds for 200 students
- **SP-101** Zero critical or high OWASP findings
- **SP-102** Zero P1/P2 open bugs
- **SP-103** Staging environment deployed and accessible
- **SP-104** CI pipeline green

---

## Post-Sprint 8 — User Acceptance Testing (1+ Weeks)

**Goal:** Conduct UAT with 3 pilot schools to validate real-world usability before Phase 1 sign-off.

| Task ID | Task | Duration | Acceptance Criteria |
|---|---|---|---|
| UAT-001 | Pilot school onboarding (3 schools: 1 primary, 1 secondary, 1 mixed) | 2 days | All 3 schools have active tenants with real data seeded |
| UAT-002 | Guided UAT sessions: admission, fee payment, attendance, mark entry, report card | 3 days | Each school completes the full workflow without system errors |
| UAT-003 | Bug triage and hot-fix cycle | 2 days | All UAT-discovered P1 bugs fixed and re-tested |
| UAT-004 | UNEB grading validation with real mark sheets | 1 day | Grades match manual computation for all 4 curriculum types |
| UAT-005 | Phase 1 gate sign-off | 1 day | Peter signs off Phase 1 gate criteria (see `_context/metrics.md`) |

**UAT Exit Criteria:**

- **SP-105** At least 1 pilot school is live on production (Phase 1 gate requirement)
- **SP-106** All P1/P2 bugs from UAT resolved
- **SP-107** UNEB grading accuracy confirmed against sample mark sheets
- **SP-108** SchoolPay test transaction confirmed (if SchoolPay merchant onboarding is complete)
- **SP-109** Phase 1 gate criteria in `_context/metrics.md` all met

---

## Sprint Allocation Summary

| Sprint | Duration | FR Groups | FR Count | Estimated SP |
|---|---|---|---|---|
| Sprint Zero | 1 week | Infrastructure | 0 | 14 |
| Sprint 1 | 2 weeks | FR-AUTH, FR-TNT | 9 | 27 |
| Sprint 2 | 2 weeks | FR-SIS | 5 | 21 |
| Sprint 3 | 2 weeks | FR-ACA | 4 | 16 |
| Sprint 4 | 2 weeks | FR-FEE + SchoolPay | 7 | 32 |
| Sprint 5 | 2 weeks | FR-ATT, FR-EXM (core) | 7 | 22 |
| Sprint 6 | 2 weeks | FR-EXM (grading), FR-RPT | 9 | 24 |
| Sprint 7 | 2 weeks | FR-RBAC, FR-EMIS, FR-AUD | 7 | 23 |
| Sprint 8 | 2 weeks | Hardening (no new FRs) | 0 | 25 |
| UAT | 1+ weeks | Validation | 0 | — |
| **Total** | **18 weeks** | | **49** (unique) | **~204** |

---

## Risk Register (Sprint-Level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Sprint 4 overloaded (FR-FEE + SchoolPay) | High | Medium | SchoolPay reconciliation tasks spill to Sprint 5; manual fees are priority |
| SchoolPay merchant onboarding delayed | Medium | High | Manual fee workflow is fully functional without SchoolPay; integration is additive |
| UNEB grading rules ambiguous without official UNEB manual | Medium | High | Peter contacts UNEB for grading manual before Sprint 6 (see external actions in README) |
| EMIS export format unavailable from MoES | Medium | Medium | Generate best-effort export based on available MoES documentation; validate post-launch |
| Solo developer illness/unavailability | Low | High | Sprint 8 buffer absorbs 1-sprint delay; all work is in version control |
| Performance targets missed on budget hardware | Medium | Medium | Optimise queries in Sprint 8; defer to AWS EC2 scaling in Phase 8 if needed |

---

## Cross-References

| Reference | Location |
|---|---|
| Functional Requirements (49 FRs) | `02-requirements-engineering/01-srs/04-functional-requirements.md` |
| User Stories (20 stories) | `02-requirements-engineering/02-user-stories/01-user-stories.md` |
| RBAC Permission Matrix | `02-requirements-engineering/03-stakeholder-analysis/01-rbac-matrix.md` |
| Business Rules | `_context/business_rules.md` |
| Quality Standards (performance targets) | `_context/quality_standards.md` |
| Technology Stack | `_context/tech_stack.md` |
| Phase Gate Criteria | `_context/metrics.md` |
| Definition of Done | `07-agile-artifacts/02-dod/01-definition-of-done.md` |
| Definition of Ready | `07-agile-artifacts/03-dor/01-definition-of-ready.md` |
