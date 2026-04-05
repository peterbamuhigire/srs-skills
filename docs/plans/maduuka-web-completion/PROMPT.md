# Maduuka Web App: Strategic Gap Analysis & 22-Phase Total Completion Plan

You are a senior systems architect and technical lead for the Maduuka project (Chwezi Core Systems)
— a mobile-first, multi-tenant SaaS POS and business management platform, Uganda-first, expanding
pan-Africa. The team is a micro team (2–5 people). Methodology is Water-Scrum-Fall: formal
requirements sign-off per phase, iterative delivery within phases.

The web application is **partially built**. A significant portion of the PHP/Bootstrap/Tabler web
app exists. Your job is to:

1. Conduct a brutal, evidence-based gap analysis of the existing codebase against the full SRS documentation suite.
2. Generate a 22-phase total completion plan that closes every gap across Phase 1 (core platform), Phase 2 (Restaurant/Bar + Pharmacy add-ons), and Phase 3 (Hotel + Advanced Inventory + EFRIS compliance) — the complete Maduuka product.

**The plan you generate is the development contract. Every phase must be independently executable
by the development team without verbal clarification from the architect.**

---

## Complete SRS Documentation Suite (33 Documents)

All requirements are fully documented. Read ALL relevant documents before generating the plan.
All documents are in `<srs-skills-root>/projects/Maduuka/`.

### Context Files (`_context/`)
- `vision.md` — Product vision, Design Covenant (6 binding constraints), 5 strategic goals
- `features.md` — F-001 through F-015: complete feature register for all phases
- `business_rules.md` — BR-001 through BR-016: immutable business rules
- `tech_stack.md` — Full technology stack for Web, Android, iOS, and shared backend API
- `stakeholders.md` — All 16 stakeholder profiles and primary needs
- `personas.md` — Agnes (Cashier), Robert (Owner), Grace (Accountant), David (Stock), Amara (HR)
- `gap-analysis.md` — GAP-001 through GAP-010: known external dependency gaps
- `metrics.md` — Phase gate criteria and KPIs
- `business_rules.md` — BR-001 through BR-016: all immutable business rules
- `glossary.md` — Defined terms used across all documents

### Strategic Vision (Phase 01)
- `01-strategic-vision/PRD_Maduuka.docx` — Product requirements document
- `01-strategic-vision/VisionStatement_Maduuka.docx` — Product vision with measurable success criteria
- `01-strategic-vision/BusinessCase_Maduuka.docx` — Financial projections, alternatives analysis, investment case

### Requirements Engineering (Phase 02)
- `02-requirements-engineering/SRS_Maduuka_Phase1_Draft.docx` — **PRIMARY REFERENCE**: 129 FRs for all 10 Phase 1 modules, IEEE 830 compliant, stimulus-response format
- `02-requirements-engineering/UserStories_Maduuka.docx` — 52 user stories mapped to FR identifiers, MoSCoW priorities
- `02-requirements-engineering/StakeholderAnalysis_Maduuka.docx` — Stakeholder register, Power/Interest grid, RACI matrix
- `02-requirements-engineering/SRS_Maduuka_iOS_Platform.docx` — iOS platform requirements (Phase 2 planning reference)
- `02-requirements-engineering/SRS_Maduuka_Phase2a_Restaurant.docx` — Restaurant/Bar add-on, 85 FRs (Phase 2 — not in this plan's scope)
- `02-requirements-engineering/SRS_Maduuka_Phase2b_Pharmacy.docx` — Pharmacy add-on, 90 FRs (Phase 2 — not in this plan's scope)
- `02-requirements-engineering/SRS_Maduuka_Phase3a_Hotel.docx` — Hotel/Accommodation, 112 FRs (Phase 3 — not in scope)
- `02-requirements-engineering/SRS_Maduuka_Phase3b_AdvancedInventory.docx` — Advanced Inventory, 74 FRs (Phase 3 — not in scope)
- `02-requirements-engineering/SRS_Maduuka_Phase3c_EFRIS.docx` — EFRIS Compliance, 38 FRs (Phase 3 — not in scope)

### Design Documentation (Phase 03)
- `03-design-documentation/HLD_Maduuka.docx` — System context, component architecture, multi-tenant model, RBAC matrix
- `03-design-documentation/LLD_Maduuka.docx` — **IMPLEMENTATION REFERENCE**: service layer design, method signatures, PAYE/NSSF formulas, audit log schema, sync engine design, RBAC permission matrix for all 24 endpoint groups
- `03-design-documentation/APISpec_Maduuka_Phase1.docx` — 64 REST endpoints, request/response schemas, error codes
- `03-design-documentation/DatabaseDesign_Maduuka.docx` — 30+ tables, entity relationships, EFRIS placeholder columns
- `03-design-documentation/UXSpec_Maduuka.docx` — 39 screens, interaction patterns, Design Covenant validation checklist

### Development Artifacts (Phase 04)
- `04-development-artifacts/TechnicalSpec_Maduuka.docx` — **MANDATORY READING**: PHP 8.3+ stack, JWT/session auth, MySQL schema standards, error envelope format, pagination format, CI/CD pipeline definition
- `04-development-artifacts/CodingGuidelines_Maduuka.docx` — **MANDATORY READING**: PHP/Kotlin/Swift standards, Git workflow, per-PR security checklist — all contributors must read before writing a line of code

### Testing Documentation (Phase 05)
- `05-testing-documentation/TestStrategy_Maduuka.docx` — 8 test levels, entry/exit criteria, IEEE 829/1012
- `05-testing-documentation/TestPlan_Maduuka_Phase1.docx` — **TEST GATE REFERENCE**: 110 executable test cases. Every phase must reference which test cases must pass before it closes.

### Operations (Phase 06)
- `06-deployment-operations/DeploymentGuide_Maduuka.docx` — Server setup, CI/CD pipeline, post-deployment verification
- `06-deployment-operations/Runbook_Maduuka.docx` — 6 incident procedures, 4 maintenance procedures

### Agile Artifacts (Phase 07)
- `07-agile-artifacts/SprintPlanning_Maduuka.docx` — 12-sprint Phase 1 plan, velocity baseline
- `07-agile-artifacts/DefinitionOfDone_Maduuka.docx` — **DoD: every task must satisfy ALL criteria before marking done**
- `07-agile-artifacts/DefinitionOfReady_Maduuka.docx` — DoR: every story must satisfy ALL criteria before sprint pull

### End-User Documentation (Phase 08)
- `08-end-user-documentation/UserManual_Maduuka.docx` — Plain-language manual for Agnes (Cashier) persona
- `08-end-user-documentation/InstallationGuide_Maduuka.docx` — Android + Web setup, first-time business configuration
- `08-end-user-documentation/FAQ_Maduuka.docx` — 30 questions across 6 topic groups

### Governance and Compliance (Phase 09)
- `09-governance-compliance/TraceabilityMatrix_Maduuka.docx` — 129 FRs → Business Goal → Test Case ID (TC-xxx)
- `09-governance-compliance/AuditReport_Maduuka.docx` — IEEE 1012 audit, Conditional Pass verdict, 7 open anomalies
- `09-governance-compliance/ComplianceDocument_Maduuka.docx` — Uganda Data Protection Act, URA tax compliance
- `09-governance-compliance/RiskAssessment_Maduuka.docx` — 13 risks: 3 Critical, 6 High

---

## Mandatory Skill Activation — Do This First

Load and apply the following skills in this order before any other action:

1. `superpowers:brainstorming` — structure thinking before gap analysis begins.
2. `superpowers:writing-plans` — govern how phase plan documents are authored.
3. `superpowers:dispatching-parallel-agents` — use parallel agents for independent work streams.
4. `superpowers:test-driven-development` — every code task has a paired test task. No feature
   closes without the corresponding test cases from `TestPlan_Maduuka_Phase1.docx` passing.
5. `frontend-design:frontend-design` — apply to all UX gap analysis and frontend task breakdowns.
   Every screen must satisfy `UXSpec_Maduuka.docx`.
6. `pos-sales-ui-design` — apply to all POS screen implementations.

From `C:\Users\Peter\.claude\skills\`, load and apply throughout:

**Database & Backend:**
- `mysql-best-practices` — database gap analysis, migrations, index strategy per `TechnicalSpec_Maduuka.docx`
- `php-modern-standards` — PHP 8.3+ gap analysis per `CodingGuidelines_Maduuka.docx`
- `php-security` — security review of every backend component
- `api-error-handling` — enforce the standardised error envelope from `TechnicalSpec_Maduuka.docx`
- `api-pagination` — enforce the pagination envelope from `TechnicalSpec_Maduuka.docx` on all list endpoints
- `api-testing-verification` — API test gates per `TestPlan_Maduuka_Phase1.docx`

**Architecture:**
- `multi-tenant-saas-architecture` — validate `franchise_id` isolation at ORM/service layer per `LLD_Maduuka.docx`
- `modular-saas-architecture` — phase structure and module boundaries
- `dual-auth-rbac` — JWT Bearer (API) + Session/CSRF (Web) + RBAC per `LLD_Maduuka.docx` permission matrix
- `saas-business-metrics` — subscription management and billing logic
- `saas-seeder` — realistic test data per module for each test gate

**UI & Frontend:**
- `webapp-gui-design` — Tabler UI per `UXSpec_Maduuka.docx` screen specifications
- `responsive-design` — mobile-first responsive for DC-004 (low-end Android browser)
- `frontend-performance` — PWA Service Worker, lazy loading, low-bandwidth optimisation
- `cognitive-ux-framework` — DC-002 (zero mandatory training) validation per UX validation checklist
- `form-ux-design` — all forms across 10 modules

**Reports & PDF:**
- `report-print-pdf` — server-side PDF generation per `TechnicalSpec_Maduuka.docx`

**Security:**
- `vibe-security-skill` — security review at every phase
- `web-app-security-audit` — OWASP Top 10 gate before Phase 14 closes
- `php-security` — PHP-specific hardening

**Testing:**
- `sdlc-testing` — test execution aligned to `TestStrategy_Maduuka.docx`
- `api-testing-verification` — API contract verification against `APISpec_Maduuka_Phase1.docx`

**Business:**
- `software-pricing-strategy` — subscription plan display and upgrade/downgrade flow

---

## Phase 1 Web Tech Stack

| Layer | Technology |
|---|---|
| Language | PHP 8.3+ (`declare(strict_types=1)` on every file) |
| Frontend | Bootstrap 5 + Tabler UI |
| JavaScript | Vanilla JS + Alpine.js (minimal) |
| Charts | ApexCharts |
| Maps | Leaflet.js |
| Auth (web) | Session + CSRF token on every state-changing form |
| Auth (API) | JWT Bearer: 15-min access + 30-day refresh |
| PWA | Service Worker + Web App Manifest |
| Barcode | USB/Bluetooth HID keyboard events; browser camera API |
| Receipts | Browser print dialog + USB thermal printer |
| PDF | Server-side HTML-to-PDF |
| Database | MySQL 8.x, utf8mb4_unicode_ci |
| File Storage | Wasabi S3-compatible |
| SMS/WhatsApp | Africa's Talking API |
| Mobile Money | MTN MoMo Business API + Airtel Money API |
| Queue | Redis + queue worker (scheduled reports, email) |
| CI/CD | GitHub Actions (lint → test → build → deploy) |

---

## Design Covenant (6 Binding Constraints — All Non-Negotiable)

Verify every gap finding and every phase task against all 6:

- **DC-001:** Web and Android are feature-equal. No feature on Android absent from web.
- **DC-002:** Zero mandatory training. Agnes (Cashier) completes a sale in under 3 minutes, first try.
- **DC-003:** Offline-first. POS and stock lookup must function with no internet (PWA + Service Worker).
- **DC-004:** Works on cheapest hardware. Web must perform on a UGX 250K Android phone's browser.
- **DC-005:** Currency-neutral. No hardcoded "UGX" or "Shs" anywhere in the codebase.
- **DC-006:** Compliance built in. EFRIS column placeholders present and populated from Phase 1.

---

## Critical Business Rules (Enforce Without Exception)

Read `business_rules.md` for the full set. Critical rules for gap analysis:

- **BR-001:** Every DB query scoped to `franchise_id`. Cross-tenant reads are architecturally impossible.
- **BR-002:** Credit sale blocked when balance exceeds limit. Manager override with reason code, audit log entry.
- **BR-004:** Stock movement records are immutable. Corrections require counter-entries.
- **BR-006:** FIFO/FEFO enforced for batch/expiry-tracked products at POS. See `LLD_Maduuka.docx` `StockService::enforceFefo()`.
- **BR-007:** POS session requires opening float before first sale. Closing reconciliation mandatory.
- **BR-008:** Receipt numbers sequential per session. Gaps flagged in gap report.
- **BR-009:** Offline sales queue locally, replay chronologically on reconnect. Never block a sale.
- **BR-010:** Multi-payment: sum of components must equal cart total before completion.
- **BR-011:** Three-way matching: PO vs GRN vs Invoice. Discrepancies flagged for manager.
- **BR-012:** Approved payroll is immutable. Corrections are counter-entries in next period. See `LLD_Maduuka.docx` `PayrollService::approvePayroll()`.

---

## LLD Service Reference (Key Implementation Contracts)

The `LLD_Maduuka.docx` defines method signatures for all service classes. Use these as the implementation contract — do not deviate without documenting the reason:

- `AuthService` — login, refreshToken, logout, validateTOTP
- `RBACMiddleware` — permission matrix for all 24 endpoint groups across 6 roles
- `POSService` — openSession, processSale, processMoMoPayment [BLOCKED: GAP-001], holdSale, voidSale, closeSession
- `SyncService` — processBatch with idempotency key and conflict resolution
- `StockService` — recordMovement, enforceFefo, initiateStockCount, submitCountVariance, approveAdjustment
- `PayrollService` — computePayroll, approvePayroll, generatePayslip; PAYE/NSSF/LST formulas defined
- `ReportService` — Template Method pattern; 14 Phase 1 report types defined
- `AuditLogService` — append-only; 21 domain event → action code mappings; DB privilege enforcement

---

## Gap Analysis Methodology

Before writing any phase plan, conduct a structured gap analysis of the existing web codebase.

### Step 1: Codebase Discovery

Systematically map what exists:

| Target | What to Find | How |
|---|---|---|
| Database migrations | Tables, columns, foreign keys, indexes | Glob `**/*.sql`, `**/migrations/**` |
| API routes | All endpoints with HTTP method and middleware | Grep route files |
| Controllers | Which modules have controllers vs stubs | Glob `**/Controllers/**/*.php` |
| Models | Models per module, `franchise_id` scoping | Glob `**/Models/**/*.php` |
| Views/Templates | Which screens are rendered HTML | Glob `**/views/**`, `**/templates/**` |
| Service classes | Business logic layer | Glob `**/Services/**/*.php` |
| JavaScript | Alpine.js components, form handlers | Grep `x-data`, `Alpine.` |
| Auth middleware | RBAC enforcement per route | Read middleware files |
| Tests | Any existing unit/integration tests | Glob `**/tests/**`, `**/Tests/**` |
| PWA | Service Worker, manifest | Glob `**/service-worker.js`, `**/manifest.json` |
| Audit log | Audit event recording | Grep `AuditLog`, `audit_log` |
| Currency strings | Hardcoded "UGX" or "Shs" | Grep entire codebase |

### Step 2: Module-by-Module Classification

For each of the 10 Phase 1 modules, classify each component:

| Status | Definition |
|---|---|
| **Complete** | Schema + endpoints + controller + service + view + tests all exist and satisfy the SRS |
| **Partial** | Some layers exist (schema but no view, or view but no tests) |
| **Phantom** | In the SRS, zero code footprint |
| **Broken** | Code exists but does not satisfy the SRS requirement |

Cross-reference every finding against the specific FR identifier in `SRS_Maduuka_Phase1_Draft.docx`.

### Step 3: Cross-Cutting Audit

Regardless of module status, check:

- Multi-tenant isolation: `franchise_id` on 100% of DB queries?
- RBAC: all 64 endpoints protected per `LLD_Maduuka.docx` permission matrix?
- Error envelope: all endpoints return the standardised error format from `TechnicalSpec_Maduuka.docx`?
- Pagination: all list endpoints implement the pagination envelope?
- CSRF: every state-changing web form validates CSRF token?
- Audit log: every create/update/delete/void/adjustment writes to audit log?
- Currency: zero hardcoded "UGX" or "Shs" strings?
- PWA: Service Worker exists and caches POS-critical assets?
- Coding standards: PHPStan level 8 passes? PSR-12 enforced?

---

## Output Structure

All output goes to `docs/plans/maduuka-web-completion/` (relative to the Maduuka project root).

```
docs/plans/maduuka-web-completion/
├── 00-gap-analysis-summary.md        Gap matrix: all modules, all components, all statuses
├── 01-foundation-environment/        Phase 1  — Foundation & CI/CD
├── 02-multitenant-schema/            Phase 2  — Multi-tenant data layer
├── 03-auth-rbac/                     Phase 3  — Authentication, RBAC & session management
├── 04-pos-core/                      Phase 4  — POS core (product search, cart, cash payment)
├── 05-pos-payments/                  Phase 5  — POS payments (MoMo, Airtel, credit, offline queue)
├── 06-pos-receipts-void/             Phase 6  — POS receipts, void & refund
├── 07-inventory/                     Phase 7  — Inventory & stock management
├── 08-customers-suppliers/           Phase 8  — Customer & supplier management
├── 09-expenses-financial/            Phase 9  — Expenses, financial accounts & cash flow
├── 10-reporting/                     Phase 10 — Sales reporting & analytics
├── 11-hr-payroll/                    Phase 11 — HR & payroll
├── 12-dashboard-settings/            Phase 12 — Dashboard, settings & configuration
├── 13-integrations/                  Phase 13 — Third-party integrations (MoMo, Africa's Talking)
├── 14-security-compliance/           Phase 14 — Security hardening & compliance
├── 15-performance-pwa-golive-p1/     Phase 15 — Performance, PWA & Phase 1 go-live
├── 16-restaurant-bar/                Phase 16 — Restaurant/Bar add-on (85 FRs, Phase 2a)
├── 17-pharmacy-drugstore/            Phase 17 — Pharmacy/Drug Store add-on (90 FRs, Phase 2b)
├── 18-phase2-integration-golive/     Phase 18 — Phase 2 integration, regression & go-live
├── 19-hotel-accommodation/           Phase 19 — Hotel/Accommodation module (112 FRs, Phase 3a)
├── 20-advanced-inventory/            Phase 20 — Advanced Inventory module (74 FRs, Phase 3b)
├── 21-efris-compliance/              Phase 21 — EFRIS Compliance module (38 FRs, Phase 3c)
└── 22-phase3-total-completion/       Phase 22 — Phase 3 integration, regression & total go-live
```

Each phase directory contains:
- `PLAN.md` — phase goal, scope, numbered task list with acceptance criteria
- `tasks.md` — granular task breakdown (each task ≤ 1 day per developer)
- `test-gates.md` — specific TC-xxx identifiers from `TestPlan_Maduuka_Phase1.docx` that must pass before phase closes
- `skills-applied.md` — skills from `C:\Users\Peter\.claude\skills\` governing this phase

---

## 22-Phase Arc

Execute gap analysis first. Generate phases based on what the gap analysis reveals is done vs. missing. The arc covers the complete Maduuka product: Phase 1 core platform (Phases 1–15), Phase 2 industry add-ons (Phases 16–18), and Phase 3 advanced modules (Phases 19–22).

**Phase 1 — Foundation Audit & Environment Setup**
Goal: Clean, reproducible dev environment. CI/CD pipeline per `DeploymentGuide_Maduuka.docx`. PHPStan level 8 and PHP_CodeSniffer (PSR-12) passing in CI. MySQL migrations tool configured. Verify `CodingGuidelines_Maduuka.docx` is distributed to all contributors.

**Phase 2 — Multi-tenant Data Layer**
Goal: `franchise_id` applied to 100% of database queries. Audit every model and raw query. Add missing composite indexes per `TechnicalSpec_Maduuka.docx`. Validate against BR-001. Apply `mysql-best-practices`. Cross-tenant leak test: TC-SET-001 and TC-SET-002 from `TestPlan_Maduuka_Phase1.docx` must pass.

**Phase 3 — Authentication, RBAC & Session Management**
Goal: Web session + CSRF and JWT Bearer auth implemented per `TechnicalSpec_Maduuka.docx`. All 64 API endpoints protected per `LLD_Maduuka.docx` RBAC permission matrix. Role definitions match `APISpec_Maduuka_Phase1.docx`. JWT payload matches `LLD_Maduuka.docx` `JWTService` spec. Apply `dual-auth-rbac`.

**Phase 4 — POS Core (Product Discovery, Cart, Cash Payment)**
Goal: FR-POS-001 through FR-POS-017 and FR-POS-021 to FR-POS-027 satisfy `SRS_Maduuka_Phase1_Draft.docx`. Screen matches `UXSpec_Maduuka.docx` POS Main Screen specification. TC-POS-001 through TC-POS-008 pass. Apply `pos-sales-ui-design`.

**Phase 5 — POS Payments (MoMo, Airtel, Credit, Offline Queue)**
Goal: MTN MoMo Business API push payment per `LLD_Maduuka.docx` `POSService::processMoMoPayment()` — stub with `[BLOCKED: GAP-001]` until credentials obtained. Airtel Money equivalent. BR-002 credit limit enforcement. BR-009 offline sale queue. FR-POS-012 through FR-POS-015 complete. TC-POS-009 through TC-POS-023 pass (MoMo cases marked [BLOCKED: GAP-001]).

**Phase 6 — POS Receipts, Void & Refund**
Goal: Browser print, USB thermal, PDF download, SMS via Africa's Talking, WhatsApp via Africa's Talking — all per FR-POS-017 through FR-POS-020. Void and refund with reason code and audit log. BR-008 receipt gap detection. TC-POS-024 onwards pass. Apply `report-print-pdf`.

**Phase 7 — Inventory & Stock Management**
Goal: All FR-INV-xxx satisfied per `SRS_Maduuka_Phase1_Draft.docx`. FIFO/FEFO per `LLD_Maduuka.docx` `StockService::enforceFefo()`. BR-004 stock movement immutability. Physical stock count workflow. Reorder alerts. TC-INV-xxx pass.

**Phase 8 — Customer & Supplier Management**
Goal: All FR-CUS-xxx and FR-SUP-xxx satisfied. BR-002 credit limit enforcement at POS. Magic-link customer portal via WhatsApp/SMS. BR-011 three-way matching. TC-CUS-xxx and TC-SUP-xxx pass.

**Phase 9 — Expenses, Financial Accounts & Cash Flow**
Goal: All FR-EXP-xxx and FR-FIN-xxx satisfied. BR-005 approval threshold. Expense photo attachment and OCR (server-side). Bank statement CSV import (web). Bank reconciliation. TC-EXP-xxx and TC-FIN-xxx pass.

**Phase 10 — Sales Reporting & Analytics**
Goal: All 14 report types from `LLD_Maduuka.docx` `ReportService` implemented. ApexCharts. CSV and PDF export per `report-print-pdf`. Scheduled reports via queue worker. Custom report builder (web). TC-REP-xxx pass.

**Phase 11 — HR & Payroll**
Goal: All FR-HR-xxx satisfied. PAYE, NSSF, LST computed per `LLD_Maduuka.docx` formulas. `PayrollService::approvePayroll()` enforces BR-012 immutability. Payslip PDF via WhatsApp/email. Bank payment files for 6 Uganda banks. TC-HR-001 through TC-HR-009 pass (PAYE/NSSF exact-value oracles).

**Phase 12 — Dashboard, Settings & Configuration**
Goal: Real-time KPI dashboard, Business Health Score (RAG), branch switcher. Settings: 2FA TOTP, subscription management, connected devices with revoke, full data export, currency config (DC-005 audit). TC-DASH-xxx and TC-SET-xxx pass.

**Phase 13 — Third-Party Integrations**
Goal: Africa's Talking SMS and WhatsApp fully wired to receipt delivery, payslip delivery, magic-link portal, refill reminders. MTN MoMo Business API end-to-end (resolve GAP-001 before this phase closes). Airtel Money end-to-end. Apply `api-testing-verification` against `APISpec_Maduuka_Phase1.docx`.

**Phase 14 — Security Hardening & Compliance**
Goal: OWASP Top 10 audit and remediation per `web-app-security-audit`. CSRF on every form. SQL injection prevention. `ComplianceDocument_Maduuka.docx` GAP-002 resolved (Data Protection Act legal review completed). RBAC verified at API layer. Audit log completeness verified against `LLD_Maduuka.docx` 21 event mappings. TC-NFR-011 through TC-NFR-019 pass.

**Phase 15 — Performance, PWA, QA Sprint & Phase 1 Go-Live**
Goal: PWA Service Worker offline cache for POS-critical assets. Load testing: P95 ≤ 500ms search, ≤ 1s barcode, ≤ 300ms filter update. DC-004: verified on low-end Android browser. DC-005: zero hardcoded "UGX" strings. Full test suite: all 110 TC-xxx from `TestPlan_Maduuka_Phase1.docx` passing. Post-deployment verification per `DeploymentGuide_Maduuka.docx`. Staging sign-off. Phase 1 production go-live — all 10 core modules live and operational.

**Phase 16 — Restaurant / Bar Add-On (Phase 2a)**
Goal: All 85 FRs from `SRS_Maduuka_Phase2a_Restaurant.docx` (FR-RES-001 through FR-RES-085) implemented and verified. Scope includes: table management, floor plan editor, reservation system, order routing to kitchen/bar, kitchen display screen (KDS), course management, split bill and merge table, happy hour and promotional pricing, online ordering integration hooks, restaurant-specific reporting (covers per table, turn time, average spend). Database schema amendments in a separate migration; multi-tenant isolation verified on all new tables. Apply `pos-sales-ui-design`, `mysql-best-practices`.

**Phase 17 — Pharmacy / Drug Store Add-On (Phase 2b)**
Goal: All 90 FRs from `SRS_Maduuka_Phase2b_Pharmacy.docx` (FR-PHR-001 through FR-PHR-090) implemented and verified. Scope includes: drug catalogue with dosage forms and generic/brand mapping, prescription management and dispensing workflow, controlled substance register with audit trail, drug expiry management and near-expiry alerts (30/60/90 days), supplier drug orders and GRN with batch and expiry capture, refill reminders via Africa's Talking SMS/WhatsApp, pharmacy-specific reporting (sales by drug, expiry loss, controlled substance log), NDA Uganda regulatory compliance placeholders. Apply `healthcare-ui-design`, `mysql-best-practices`.

**Phase 18 — Phase 2 Integration, Regression & Go-Live**
Goal: Restaurant and Pharmacy add-ons pass regression testing alongside Phase 1 core modules. API spec amendments for Phase 2 endpoints documented and versioned. Multi-tenant isolation re-verified across all 30+ tables + Phase 2 additions. All Phase 2 SRS requirements traced in `TraceabilityMatrix_Maduuka.docx`. Security hardening pass (OWASP Top 10) for Phase 2 surfaces. Subscription plan updated to reflect Phase 2 module pricing per `BusinessCase_Maduuka.docx`. Phase 2 staging sign-off. Production go-live for Restaurant and Pharmacy modules.

**Phase 19 — Hotel / Accommodation Module (Phase 3a)**
Goal: All 112 FRs from `SRS_Maduuka_Phase3a_Hotel.docx` (FR-HTL-001 through FR-HTL-112) implemented and verified. Scope includes: property and room type setup, reservation calendar and booking engine, check-in / check-out workflow, housekeeping status board, room service order routing, folio management (post charges from POS, restaurant, and phone to room folio), night audit automation, channel manager integration hooks (OTA placeholder), hotel-specific reporting (occupancy rate, ADR, RevPAR, folio summary). Apply `mysql-best-practices`, `webapp-gui-design`.

**Phase 20 — Advanced Inventory Module (Phase 3b)**
Goal: All 74 FRs from `SRS_Maduuka_Phase3b_AdvancedInventory.docx` (FR-AINV-001 through FR-AINV-074) implemented and verified. Scope includes: multi-location warehouse management, goods-in-transit tracking, bin/shelf location assignment, serial number tracking, assembly / kitting (BOM), landed cost allocation, cycle count scheduling, inventory valuation methods (FIFO standard + weighted average), demand forecasting and auto-reorder suggestions, advanced inventory reporting (slow-moving, dead stock, days-on-hand, valuation). Apply `mysql-best-practices`, `multi-tenant-saas-architecture`.

**Phase 21 — EFRIS Compliance Module (Phase 3c)**
Goal: All 38 FRs from `SRS_Maduuka_Phase3c_EFRIS.docx` (FR-EFR-001 through FR-EFR-038) implemented and verified — contingent on GAP-005 (URA EFRIS API sandbox access) being resolved before this phase closes. Scope includes: URA EFRIS API integration for real-time fiscal receipt submission, E-receipt generation with QR code, fiscal device management, EFRIS-compliant invoice numbering, URA Tax Account dashboard, failed submission retry queue, EFRIS audit log with tamper-evident records, zero-rated and exempt VAT handling per URA rules. All EFRIS placeholder columns (populated in Phase 2 schema) are now active. Apply `php-security`, `api-testing-verification`.

**Phase 22 — Phase 3 Integration, Regression & Total Go-Live**
Goal: Hotel, Advanced Inventory, and EFRIS modules pass full regression alongside all Phase 1 and Phase 2 modules. Traceability matrix covers 100% of all FRs across all phases (129 Phase 1 + 85 Phase 2a + 90 Phase 2b + 112 Phase 3a + 74 Phase 3b + 38 Phase 3c = 528 total FRs). Final OWASP Top 10 security audit. DC-001 through DC-006 verified end-to-end across all modules. All `RiskAssessment_Maduuka.docx` risks resolved or formally accepted. `AuditReport_Maduuka.docx` all anomalies closed. Full data export and account deletion tested across all modules. `InstallationGuide_Maduuka.docx` updated for all Phase 2/3 modules. Production go-live — Maduuka total completion.

---

## Per-Phase Plan Document Standard

```markdown
# Phase N: [Title]

## Goal
One sentence: what is true when this phase closes.

## Scope
- IN scope: specific FR identifiers from the relevant SRS document for this phase
- OUT of scope: explicitly deferred items

## Prerequisites
- Prior phases that must be complete
- External dependencies (GAP-xxx)

## Task List
1. [Task — max 1 day] — acceptance criterion (deterministic pass/fail oracle)
2. ...

## Test Gates
TC identifiers from TestPlan_Maduuka_Phase1.docx that must pass before phase closes:
- Unit: [service methods]
- Integration: [API endpoints + scenarios]
- Acceptance: [user journey TC-xxx]

## Definition of Done Check
All items in DefinitionOfDone_Maduuka.docx satisfied? [ ] Yes — confirmed by reviewer.

## Skills Applied
- [skill-name] — how it governs this phase

## Open Gaps / Blockers
- [GAP-ID] — description, resolution owner
```

---

## Constraints

- Base every plan item on the gap analysis evidence or a specific SRS document. Do not invent scope.
- Every phase has explicit test gates referencing TC-xxx identifiers from `TestPlan_Maduuka_Phase1.docx`. No phase closes without green tests.
- Apply `superpowers:test-driven-development` throughout.
- Apply `ai-slop-prevention` — every task must be actionable by a developer working independently without verbal clarification.
- The `DefinitionOfDone_Maduuka.docx` checklist applies to every task. No task is done without satisfying all criteria.
- Do not re-plan work the gap analysis confirms is already complete. Only plan the delta.
- This plan covers ONLY the web app and shared backend API. Android is a separate plan. iOS is in `docs/plans/maduuka-ios/PROMPT.md`.
- This plan covers the TOTAL completion of Maduuka: Phase 1 core (Phases 1–15), Phase 2 add-ons (Phases 16–18), and Phase 3 advanced modules (Phases 19–22). All 528 FRs across all SRS documents are in scope.
- GAP-005 (URA EFRIS API sandbox credentials) must be resolved before Phase 21 closes. Phase 21 EFRIS API tasks are scaffolded but marked `[BLOCKED: GAP-005]` until credentials are available.
- All output goes to `docs/plans/maduuka-web-completion/` relative to the Maduuka project root.
