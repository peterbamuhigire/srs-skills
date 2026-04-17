# AcademiaPro

**Status:** Phase 2 — Requirements Engineering ✅ Complete | Phase 3 — Design Documentation 🔲 Next
**Owner:** Peter — Chwezi Core Systems (chwezicore.com)
**Domain:** education (Uganda-first; pan-Africa expansion)
**Methodology:** Hybrid (Water-Scrum-Fall) — formal requirements gate per phase; iterative delivery within phases
**Started:** 2026-03-27
**Requirements Baseline Completed:** 2026-03-29

---

## Quick Links

- `DOCUMENTATION-STATUS.md` — Full document inventory, generation status, and progress summary

## Context Files

- `_context/vision.md` — Project vision, 12-phase build plan, design covenant
- `_context/stakeholders.md` — Stakeholder register
- `_context/glossary.md` — Project terminology
- `_context/domain.md` — Education domain baseline (adapted for Uganda/Africa)
- `_context/features.md` — Module feature list (35+ modules across 12 phases)
- `_context/tech_stack.md` — Technology decisions
- `_context/business_rules.md` — Uganda-specific business rules
- `_context/quality_standards.md` — Quality and performance targets
- `_context/personas.md` — User personas
- `_context/payment-landscape.md` — Payment architecture: SchoolPay, MoMo, pan-Africa rails
- `_context/gap-analysis.md` — Section 20 gap analysis: 8 HIGH / 12 MEDIUM / 11 LOW priority items
- `_context/quality-log.md` — QA issue log
- `_context/metrics.md` — Phase gate criteria and KPI targets

---

## Design Covenant

> Automate every school process as much as possible, yet remain simple enough for a single administrator to operate — provided each user has watched the training videos for their assigned modules. Deep and rich in capability; easy and flexible in daily use.

---

## Phase Progress

| Phase | Folder | Status | Deliverables |
|---|---|---|---|
| 01 — Strategic Vision | `01-strategic-vision/` | ✅ Complete | PRD, Vision Statement, Business Case |
| 02 — Requirements Engineering | `02-requirements-engineering/` | ✅ Complete | SRS, User Stories, RBAC Matrix |
| 03 — Design Documentation | `03-design-documentation/` | 🔲 Next | HLD, ERD, OpenAPI Spec, DB Design, UX Spec |
| 04 — Development Artifacts | `04-development-artifacts/` | 🔲 Pending | Technical specs, ADRs |
| 05 — Testing Documentation | `05-testing-documentation/` | 🔲 Pending | Test plan, test cases |
| 06 — Deployment & Operations | `06-deployment-operations/` | 🔲 Pending | CI/CD plan, runbook |
| 07 — Agile Artifacts | `07-agile-artifacts/` | 🔲 Pending | Sprint plans, backlog |
| 08 — End User Documentation | `08-end-user-documentation/` | 🔲 Pending | User manuals, training guides |
| 09 — Governance & Compliance | `09-governance-compliance/` | 🔲 Pending | PDPO compliance doc, DPA template |

---

## Phase 2 — Requirements Engineering: Deliverables

All Phase 2 `.docx` files are in `02-requirements-engineering/`.

| Document | File | Content |
|---|---|---|
| Software Requirements Specification | `AcademiaPro_SRS.docx` | 6 sections: Introduction, Overall Description, External Interfaces, Functional Requirements (49 FRs), System Constraints, NFRs |
| User Stories | `AcademiaPro_UserStories.docx` | 20 user stories with Gherkin acceptance criteria across all Phase 1 modules |
| RBAC & Stakeholder Analysis | `AcademiaPro_RBAC_Stakeholder.docx` | Full permission matrix: 60+ permissions × 8 roles; resolves HIGH-005 |

### SRS Coverage Summary

| FR Group | Count | Modules |
|---|---|---|
| FR-AUTH | 6 | Web login, JWT login, token refresh, logout, idle timeout, MFA |
| FR-TNT | 3 | Tenant provisioning, activation, suspension |
| FR-SIS | 5 | Student admission, cross-school enrollment, search, transfer out, retention lock |
| FR-ACA | 4 | Academic year, class/stream, curriculum type, timetable |
| FR-FEE | 7 | Fee structures, manual payment, receipts, reminders, refund workflow, balance, reports |
| FR-ATT | 4 | Attendance entry, absence alert, amendment, monthly report |
| FR-EXM | 8 | Exam config, mark entry, unlock, PLE/UCE/UACE/Thematic grading, UNEB export |
| FR-RPT | 4 | Single/bulk report cards, school performance, comments |
| FR-RBAC | 5 | Permission resolution, role assignment, invitations, session expiry, super admin audit |
| FR-EMIS | 1 | EMIS government export |
| FR-AUD | 1 | Immutable audit trail |
| **Total** | **49** | |

---

## 12-Phase Build Plan Summary

| Phase | Scope |
|---|---|
| 1 | Core web app — Student info, Fees (manual), Attendance, Examinations, Academics, Reports, User roles; portal scaffolds |
| 2 | Extra modules — HR, Library, Transport, Hostel, Communicate, Homework, Downloads, Calendar, Certificates, Front CMS; SchoolPay integration |
| 3 | Super Admin + Owner portals complete; Android apps scaffolded |
| 4 | Extra modules perfected; full system test to 100% pass |
| 5 | Student + Parent portals complete; Android apps started |
| 6 | Bus Driver app; Owner/Student/Teacher Android apps complete |
| 7 | Health Management module (prescriptions, treatments, cross-app access) |
| 8 | Go-live preparation; Android app launch |
| 9 | Onboard initial trials; iOS apps begin |
| 10 | iOS apps complete |
| 11 | Full integration; pan-Africa expansion |
| 12 | Maintenance and support |

---

## Phase 1 Development Gate: Gap Status

**Gate opens when all 8 HIGH-priority gaps are resolved.** Current status:

| Gap | Description | Status |
|---|---|---|
| HIGH-001 | Security architecture specification | ✅ Resolved — `03-design-documentation/01-hld/02-security-architecture.md` |
| HIGH-002 | Consolidated ERD | ✅ Resolved — `03-design-documentation/04-database-design/01-erd.md` |
| HIGH-003 | OpenAPI 3.1 specification | ✅ Resolved — `03-design-documentation/03-api-spec/` (12 files, 49 FRs) |
| HIGH-004 | Academic year lifecycle (year-end rules) | ✅ Resolved — design doc `docs/plans/2026-03-29-academia-pro-student-promotion-portability-design.md`; SRS amendment pending |
| HIGH-005 | Full RBAC permission matrix | ✅ Resolved — `02-requirements-engineering/03-stakeholder-analysis/01-rbac-matrix.md` |
| HIGH-006 | Double-payment prevention rules | ✅ Specified in SRS FR-FEE-002/003 and `_context/business_rules.md` |
| HIGH-007 | Data migration specification | ✅ Resolved — `04-development-artifacts/01-technical-spec/02-data-migration.md` |
| HIGH-008 | Uganda PDPO 2019 compliance document | ✅ Resolved — `09-governance-compliance/03-compliance/01-pdpo-compliance.md` |

**Resolved: 8 of 8.** ✅ All HIGH-priority gaps resolved. Phase 1 development gate is open.

---

## Immediate Next Steps (Phase 3 — Design Documentation)

Work through the following in priority order. All must be complete before development begins.

### 1. Security Architecture Document (HIGH-001) — Highest Priority
**File:** `03-design-documentation/01-hld/02-security-architecture.md`

Must specify:
- JWT middleware: extract `tenant_id` from token, bind to request context
- Repository base class: mandatory `WHERE tenant_id = ?` enforcement
- Eloquent global scope: secondary defence layer
- Raw query audit: CI rule rejecting `DB::statement()` / `DB::select()` without `$tenantId`
- Queue jobs: `tenant_id` serialised into every job payload
- Event listeners: same as queue jobs
- API response sanitisation: middleware strips `tenant_id` from outbound JSON
- Super Admin bypass: `withoutTenantScope()` method — audited, restricted to Super Admin only

### 2. Entity Relationship Diagram (HIGH-002)
**File:** `03-design-documentation/04-database-design/01-erd.md`

A `.docx` exists at `03-design-documentation/AcademiaPro_ERD.docx`. The source `.md` file needs to be written so the diagram can be regenerated and version-controlled. Minimum Phase 1 entities are listed in `_context/gap-analysis.md` HIGH-002.

### 3. OpenAPI 3.1 Specification (HIGH-003)
**File:** `03-design-documentation/03-api-spec/`

All 49 Phase 1 FR endpoints must be specified before frontend or mobile development begins. Reference the FR identifiers from the SRS (FR-AUTH, FR-SIS, FR-FEE, etc.) as the source of truth for request/response shapes.

### 4. Academic Year Lifecycle Rules (HIGH-004)
**File:** `_context/business_rules.md` (new section) + SRS amendment

Decisions required from Peter:
- Class promotion: automatic (all P5 → P6) or manual (Head Teacher approves individually)?
- Repeat student handling: same class, previous year records linked
- Historical record locking: marks/attendance/fees locked after term close + 30 days
- Fee structure carry-forward defaults

### 5. Data Migration Specification (HIGH-007)
**File:** `04-development-artifacts/01-technical-spec/02-data-migration.md`

Import wizard for schools migrating from Excel/paper. Specify: student import template columns, validation rules, error handling (skip-and-report mode), fee history handling, what is not imported (attendance history, historical marks).

### 6. PDPO 2019 Compliance Document (HIGH-008)
**File:** `09-governance-compliance/03-compliance/01-pdpo-compliance.md`

Legal obligations documented in `_context/gap-analysis.md` HIGH-008. Requires DPA template and Privacy Policy draft before first school signs up.

---

## External Actions Required (From Peter)

These cannot be completed by the AI and require Peter's direct action:

| Action | Purpose | Urgency |
|---|---|---|
| Contact UNEB for grading manual and sample mark sheets | Verify FR-EXM-003 through FR-EXM-006 | Before Phase 1 dev begins |
| Obtain MoES EMIS data dictionary | Complete FR-EMIS-001 specification | Before Phase 1 dev begins |
| Register Chwezi Core Systems with Uganda PDPO Office | LC-001 legal compliance | Before first school signs up |
| Draft Privacy Policy and publish at `/privacy` | LC-001 legal compliance | Before first school signs up |
| Decide: class promotion — automatic or manual? | HIGH-004 blocking | Before Phase 1 dev begins |
| Decide: hosting provider — AWS, Azure, or local Uganda DC? | PDPO data residency | Before Phase 8 |
| Apply for Africa's Talking Uganda sender ID | SMS alerts (FR-ATT-002, FR-FEE-004) | Before Phase 1 go-live |
| Set up AWS S3 buckets (prod/staging/dev) | PDF report storage (Section 3.3.4) | Before Phase 1 dev begins |
