# Maduuka Android App: Strategic Gap Analysis & 15-Phase Total Completion Plan

You are a senior Android architect and technical lead for the Maduuka project (Chwezi Core Systems)
— a mobile-first, multi-tenant SaaS POS and business management platform, Uganda-first, expanding
pan-Africa. The Android app is **Phase 1** of Maduuka: it ships simultaneously with the web app
as the primary mobile client.

The team is micro (2–5 people). Methodology is Water-Scrum-Fall: formal requirements sign-off per
phase, iterative delivery within phases.

The Android app is **partially built**. A significant portion of the Kotlin/Compose app exists.
Your job is to:

1. Conduct a brutal, evidence-based gap analysis of the existing Android codebase against the full SRS documentation suite.
2. Generate a 15-phase total completion plan that closes every gap across Phase 1 (core platform), Phase 2 (Restaurant/Bar + Pharmacy add-ons), and Phase 3 (Hotel + Advanced Inventory + EFRIS compliance) — the complete Maduuka Android product.

**The plan you generate is the Android development contract. Every phase must be independently
executable by the Android developer without verbal clarification from the architect.**

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
- `glossary.md` — Defined terms used across all documents

### Strategic Vision (Phase 01)
- `01-strategic-vision/PRD_Maduuka.docx` — Product requirements document
- `01-strategic-vision/VisionStatement_Maduuka.docx` — Product vision with measurable success criteria
- `01-strategic-vision/BusinessCase_Maduuka.docx` — Financial projections, alternatives analysis, investment case

### Requirements Engineering (Phase 02)
- `02-requirements-engineering/SRS_Maduuka_Phase1_Draft.docx` — **PRIMARY ANDROID REFERENCE**: 129 FRs for all 10 Phase 1 modules, IEEE 830 compliant, stimulus-response format
- `02-requirements-engineering/UserStories_Maduuka.docx` — 52 user stories mapped to FR identifiers, MoSCoW priorities
- `02-requirements-engineering/StakeholderAnalysis_Maduuka.docx` — Stakeholder register, Power/Interest grid, RACI matrix
- `02-requirements-engineering/SRS_Maduuka_iOS_Platform.docx` — iOS platform requirements (Phase 2 — architecture awareness only; Android must not diverge from the shared API contract)
- `02-requirements-engineering/SRS_Maduuka_Phase2a_Restaurant.docx` — Restaurant/Bar add-on, 85 FRs (Phase 2a)
- `02-requirements-engineering/SRS_Maduuka_Phase2b_Pharmacy.docx` — Pharmacy add-on, 90 FRs (Phase 2b)
- `02-requirements-engineering/SRS_Maduuka_Phase3a_Hotel.docx` — Hotel/Accommodation, 112 FRs (Phase 3a)
- `02-requirements-engineering/SRS_Maduuka_Phase3b_AdvancedInventory.docx` — Advanced Inventory, 74 FRs (Phase 3b)
- `02-requirements-engineering/SRS_Maduuka_Phase3c_EFRIS.docx` — EFRIS Compliance, 38 FRs (Phase 3c — EFRIS placeholder columns must be present in Room from Phase 2)

### Design Documentation (Phase 03)
- `03-design-documentation/HLD_Maduuka.docx` — System context, component architecture, multi-tenant model, RBAC matrix
- `03-design-documentation/LLD_Maduuka.docx` — **IMPLEMENTATION REFERENCE**: service layer design, method signatures, PAYE/NSSF formulas, audit log schema, offline sync engine design, RBAC permission matrix for all 24 endpoint groups
- `03-design-documentation/APISpec_Maduuka_Phase1.docx` — 64 REST endpoints, request/response schemas, error codes (Android consumes identically to iOS)
- `03-design-documentation/DatabaseDesign_Maduuka.docx` — 30+ tables, entity relationships, EFRIS placeholder columns (Room entities mirror this schema)
- `03-design-documentation/UXSpec_Maduuka.docx` — 39 screens, interaction patterns, Design Covenant validation checklist (governs Android UI)

### Development Artifacts (Phase 04)
- `04-development-artifacts/TechnicalSpec_Maduuka.docx` — **MANDATORY READING**: Android tech stack spec, JWT/EncryptedSharedPreferences auth, error envelope format, pagination format, CI/CD pipeline definition. The Android developer must read this before writing a line of code.
- `04-development-artifacts/CodingGuidelines_Maduuka.docx` — **MANDATORY READING**: Kotlin coding standards, Git workflow, per-PR security checklist. All contributors must read before starting.

### Testing Documentation (Phase 05)
- `05-testing-documentation/TestStrategy_Maduuka.docx` — 8 test levels (unit, integration, system, UAT, performance, security, offline/sync, regression), entry/exit criteria, IEEE 829/1012
- `05-testing-documentation/TestPlan_Maduuka_Phase1.docx` — **TEST GATE REFERENCE**: 110 executable test cases with TC-xxx identifiers. Every phase must reference which TC-xxx cases must pass before it closes.

### Operations (Phase 06)
- `06-deployment-operations/DeploymentGuide_Maduuka.docx` — Server setup, CI/CD pipeline (includes Android/Fastlane), post-deployment verification
- `06-deployment-operations/Runbook_Maduuka.docx` — 6 incident procedures, 4 maintenance procedures

### Agile Artifacts (Phase 07)
- `07-agile-artifacts/SprintPlanning_Maduuka.docx` — 12-sprint Phase 1 plan; Android sprint structure derives from this baseline
- `07-agile-artifacts/DefinitionOfDone_Maduuka.docx` — **DoD: every Android task must satisfy ALL criteria before marking done**
- `07-agile-artifacts/DefinitionOfReady_Maduuka.docx` — DoR: every story must satisfy ALL criteria before sprint pull

### End-User Documentation (Phase 08)
- `08-end-user-documentation/UserManual_Maduuka.docx` — Plain-language manual for Agnes (Cashier) persona; Android flows must match documented workflows
- `08-end-user-documentation/InstallationGuide_Maduuka.docx` — Android + Web setup, first-time business configuration; Android section governs this plan
- `08-end-user-documentation/FAQ_Maduuka.docx` — 30 questions across 6 topic groups

### Governance and Compliance (Phase 09)
- `09-governance-compliance/TraceabilityMatrix_Maduuka.docx` — 129 FRs → Business Goal → TC-xxx test case ID
- `09-governance-compliance/AuditReport_Maduuka.docx` — IEEE 1012 audit, Conditional Pass verdict, 7 open anomalies; Android plan must close relevant anomalies
- `09-governance-compliance/ComplianceDocument_Maduuka.docx` — Uganda Data Protection Act, URA tax compliance; Android EncryptedSharedPreferences and data residency must satisfy these requirements
- `09-governance-compliance/RiskAssessment_Maduuka.docx` — 13 risks: 3 Critical, 6 High

---

## Mandatory Skill Activation — Do This First

Load and apply the following skills in this order before any other action:

1. `superpowers:brainstorming` — structure thinking before gap analysis begins.
2. `superpowers:writing-plans` — govern how phase plan documents are authored.
3. `superpowers:dispatching-parallel-agents` — use parallel agents for independent work streams.
4. `superpowers:test-driven-development` — every code task has a paired test task. No feature
   closes without the corresponding TC-xxx test cases from `TestPlan_Maduuka_Phase1.docx` passing.
5. `jetpack-compose-ui` — Compose component choices, layout, and Material 3 design tokens.

From `C:\Users\Peter\.claude\skills\`, load and apply throughout:

**Android Development:**
- `android-development` — Android-specific development patterns and platform constraints.
- `android-saas-planning` — SaaS architecture patterns on Android: multi-tenant, subscription, offline.
- `mobile-rbac` — Cross-platform RBAC consistency between Android, iOS, and web.
- `mobile-reports` — Report display, filtering, and export on mobile.
- `mobile-report-tables` — Tabular data display optimised for small screens.

**Architecture:**
- `multi-tenant-saas-architecture` — `franchise_id` isolation verified at Room, API, and UI layers per `LLD_Maduuka.docx`.
- `modular-saas-architecture` — feature module boundaries and Gradle dependency management.
- `dual-auth-rbac` — JWT Bearer token authentication with biometric re-auth per `LLD_Maduuka.docx` `AuthService` spec.

**UI/UX:**
- `pos-sales-ui-design` — POS screen design patterns on Android per `UXSpec_Maduuka.docx`.
- `cognitive-ux-framework` — DC-002 (zero mandatory training) validation against `UXSpec_Maduuka.docx` checklist.
- `form-ux-design` — all form designs, keyboard management, input validation.
- `jetpack-compose-ui` — Compose layout, navigation, animations for all 39 screens.
- `interaction-design-patterns` — gesture-driven interactions, Compose transitions.

**Reports & PDF:**
- `mobile-reports` — Report display per `LLD_Maduuka.docx` `ReportService` 14 report types.

**Security:**
- `vibe-security-skill` — security review at every phase; `ComplianceDocument_Maduuka.docx` requirements.

**Testing:**
- `sdlc-testing` — test strategy alignment with `TestStrategy_Maduuka.docx`.
- `api-testing-verification` — API contract verification from Android client against `APISpec_Maduuka_Phase1.docx`.

**Google Play:**
- `android-development` — Play Store distribution configuration, signing, release tracks.

---

## Android Tech Stack (Reference)

| Layer | Technology |
|---|---|
| Language | Kotlin (per `CodingGuidelines_Maduuka.docx` Kotlin standards) |
| UI Framework | Jetpack Compose + Material 3 |
| Architecture | MVVM + Clean Architecture (UI / Domain / Data layers) |
| Local Database | Room (SQLite) — offline-first; schema mirrors `DatabaseDesign_Maduuka.docx` |
| Networking | Retrofit + OkHttp + Kotlin Coroutines / Flow |
| Auth | JWT Bearer: 15-min access + 30-day refresh; stored in EncryptedSharedPreferences |
| Biometric | BiometricPrompt API (fingerprint + face) |
| Encrypted Storage | EncryptedSharedPreferences for tokens; Android Keystore for sensitive data |
| Certificate Pinning | OkHttp `CertificatePinner` with pinned certificate hashes |
| Barcode Scanning | ML Kit Barcode Scanning (or ZXing fallback) |
| Bluetooth Printing | ESC/POS library for 80mm thermal printers (Epson, Xprinter, TP-Link) |
| Background Sync | WorkManager: `PeriodicWorkRequest` (15-min) + expedited `OneTimeWorkRequest` on reconnect |
| Push Notifications | Firebase Cloud Messaging (FCM) |
| PDF Generation | iText / Apache PDFBox (receipts, payslips, reports) |
| Root Detection | RootBeer or Play Integrity API at app launch |
| Maps | Google Maps SDK |
| Charts | MPAndroidChart or Vico |
| SMS/WhatsApp | Africa's Talking API (via backend — no direct Android SDK) |
| Mobile Money | MTN MoMo Business API + Airtel Money API (via backend — no direct Android SDK) |
| CI/CD | GitHub Actions + Fastlane per `DeploymentGuide_Maduuka.docx` |
| Distribution | Firebase App Distribution (beta) → Google Play (production) |

---

## Shared Backend API (Android Consumes Identically to iOS)

- Single REST API — no Android-specific endpoints.
- Base URL: configurable at build time (debug / staging / production build variants per `TechnicalSpec_Maduuka.docx`).
- Auth: JWT Bearer token in `Authorization` header per `LLD_Maduuka.docx` `AuthService` spec.
- All 64 endpoints documented in `APISpec_Maduuka_Phase1.docx`.
- Error format: standardised JSON error response per `TechnicalSpec_Maduuka.docx` error envelope.
- Pagination: cursor-based or offset — match the pagination envelope in `TechnicalSpec_Maduuka.docx` exactly.

---

## Design Covenant (All 6 Are Binding)

Every phase task must be verified against all 6 constraints from `VisionStatement_Maduuka.docx`:

- **DC-001:** Android has feature parity with web and iOS. No feature on web absent from Android.
- **DC-002:** Zero mandatory training. Agnes (Cashier persona) completes a sale in under 3 minutes, first try. Validate against `UXSpec_Maduuka.docx` DC-002 checklist.
- **DC-003:** Offline-first. POS, stock lookup, and dashboard work with airplane mode on.
- **DC-004:** Works on the cheapest Android phone. Target: UGX 250K device (2 GB RAM, Android 8.0 minimum). No Compose recompositions or animations that cause jank (> 16ms frame) on this device.
- **DC-005:** Currency-neutral. No hardcoded "UGX" or "Shs" strings anywhere in the codebase.
- **DC-006:** Compliance built in. EFRIS-ready Room entity columns present from Phase 2. EFRIS UI placeholders visible. See `SRS_Maduuka_Phase3c_EFRIS.docx` for column names.

---

## Critical Business Rules (Enforce on Android)

Read `business_rules.md` for the full set. These rules are non-negotiable:

- **BR-001:** Every Room query and API request scoped to `franchise_id`. Tenant isolation is absolute. See `LLD_Maduuka.docx` multi-tenant section.
- **BR-002:** Credit sale blocked when balance would exceed limit. Manager role override with reason code and audit log entry.
- **BR-004:** Stock movement records are immutable. Corrections require counter-entries.
- **BR-006:** FIFO/FEFO enforced at POS for batch/expiry-tracked products. See `LLD_Maduuka.docx` `StockService::enforceFefo()`.
- **BR-007:** POS session requires opening float before first sale. Closing reconciliation mandatory.
- **BR-008:** Receipt numbers sequential per session. Gap detection in receipt gap report.
- **BR-009:** Offline sales queue locally; replay in chronological order on reconnect. Never block a sale.
- **BR-010:** Multi-payment: sum of components must equal cart total before checkout confirms.
- **BR-011:** Three-way matching: PO vs GRN vs Invoice discrepancies flagged for manager.
- **BR-012:** Approved payroll is immutable. Corrections are counter-entries in the next period. See `LLD_Maduuka.docx` `PayrollService::approvePayroll()`.

---

## LLD Service Reference (Key Implementation Contracts)

The `LLD_Maduuka.docx` defines method signatures for all service classes. The Android app consumes the same contracts via the REST API. Reference these when building the Retrofit layer and Room sync logic:

- `AuthService` — login, refreshToken, logout, validateTOTP
- `RBACMiddleware` — permission matrix for all 24 endpoint groups across 6 roles; governs Android RBAC per-screen and per-action gating
- `POSService` — openSession, processSale, processMoMoPayment [BLOCKED: GAP-001], holdSale, voidSale, closeSession
- `SyncService` — processBatch with idempotency key and conflict resolution; governs WorkManager sync task implementation
- `StockService` — recordMovement, enforceFefo, initiateStockCount, submitCountVariance, approveAdjustment
- `PayrollService` — computePayroll, approvePayroll, generatePayslip; PAYE/NSSF/LST formulas defined here
- `ReportService` — Template Method pattern; 14 Phase 1 report types; governs Android PDF generation scope
- `AuditLogService` — append-only; 21 domain event → action code mappings; Android must trigger these via API on every create/update/delete/void/adjustment

---

## Gap Analysis Methodology

Before writing any phase plan, conduct a structured gap analysis of the existing Android codebase.

### Step 1: Codebase Discovery

Systematically map what exists:

| Target | What to Find | How |
|---|---|---|
| Room entities | Tables, DAOs, foreign keys, franchise_id | Glob `**/data/local/**/*.kt`, `**/*.kt` with `@Entity` |
| Retrofit services | All API interfaces with method and endpoint | Glob `**/data/remote/**/*.kt`, `**/*ApiService.kt` |
| ViewModels | Which modules have ViewModels vs stubs | Glob `**/presentation/**/*ViewModel.kt` |
| Compose screens | Which screens are implemented vs missing | Glob `**/ui/**/*Screen.kt`, `**/*Screen.kt` |
| Repository layer | Repository implementations per module | Glob `**/repository/**/*.kt` |
| WorkManager tasks | Background sync workers defined | Grep `Worker`, `CoroutineWorker` |
| Auth flow | JWT storage, refresh interceptor | Grep `EncryptedSharedPreferences`, `Authenticator` |
| RBAC | Role checks on screens and API calls | Grep `UserRole`, `hasPermission`, `RbacMiddleware` |
| Barcode | ML Kit or ZXing integration | Grep `BarcodeScanner`, `MLKit`, `ZXing` |
| Bluetooth | ESC/POS thermal printer integration | Grep `BluetoothAdapter`, `EscPos` |
| Tests | Existing unit and instrumentation tests | Glob `**/test/**/*.kt`, `**/androidTest/**/*.kt` |
| Currency strings | Hardcoded "UGX" or "Shs" | Grep entire codebase |

### Step 2: Module-by-Module Classification

For each of the 10 Phase 1 modules, classify each component:

| Status | Definition |
|---|---|
| **Complete** | Room entity + DAO + Repository + ViewModel + Compose screen + tests all exist and satisfy the SRS |
| **Partial** | Some layers exist (entity but no screen, or screen but no tests) |
| **Phantom** | In the SRS, zero code footprint |
| **Broken** | Code exists but does not satisfy the SRS requirement |

Cross-reference every finding against the specific FR identifier in `SRS_Maduuka_Phase1_Draft.docx`.

### Step 3: Cross-Cutting Audit

Regardless of module status, check:

- Multi-tenant isolation: `franchise_id` on 100% of Room queries and API calls?
- RBAC: all 64 endpoints and all Compose screens gated per `LLD_Maduuka.docx` permission matrix?
- Error envelope: all API calls map to the standardised error format from `TechnicalSpec_Maduuka.docx`?
- Pagination: all list endpoints and lazy columns implement the pagination envelope?
- Audit log: every create/update/delete/void/adjustment triggers `AuditLogService` via API?
- Currency: zero hardcoded "UGX" or "Shs" strings?
- Offline: Room pending queue exists for sales and sync created offline?
- WorkManager sync: periodic 15-minute sync and reconnect-triggered sync both wired?
- Coding standards: Kotlin lint and detekt passing in CI?

---

## Output Structure

All output goes to `docs/plans/maduuka-android/` (relative to the Maduuka project root).

```
docs/plans/maduuka-android/
├── 00-gap-analysis-summary.md           Gap matrix: all modules, all components, all statuses
├── 01-foundation-environment/           Phase 1  — Foundation audit & environment setup
├── 02-room-multitenant-sync/            Phase 2  — Room schema, multi-tenant layer & sync engine
├── 03-auth-rbac-biometric/              Phase 3  — Auth, JWT, biometric login & RBAC
├── 04-pos-core/                         Phase 4  — POS core (search, barcode, cart, cash payment)
├── 05-pos-payments-receipts/            Phase 5  — POS payments, Bluetooth printing & receipts
├── 06-inventory-stock/                  Phase 6  — Inventory & stock management
├── 07-customers-suppliers/              Phase 7  — Customer & supplier management
├── 08-expenses-finance-hr/              Phase 8  — Expenses, financial accounts & HR/payroll
├── 09-reporting-pdf-dashboard/          Phase 9  — Reporting, PDF export & dashboard
├── 10-integrations-security-hardening/  Phase 10 — Integrations, security hardening & Phase 1 go-live
├── 11-restaurant-bar-android/           Phase 11 — Restaurant/Bar add-on (85 FRs, Phase 2a)
├── 12-pharmacy-android/                 Phase 12 — Pharmacy/Drug Store add-on (90 FRs, Phase 2b)
├── 13-phase2-play-store-update/         Phase 13 — Phase 2 integration & Play Store update
├── 14-hotel-adv-inventory-android/      Phase 14 — Hotel + Advanced Inventory (Phase 3a/3b)
└── 15-efris-total-completion/           Phase 15 — EFRIS Android + total completion & final release
```

Each phase directory contains:
- `PLAN.md` — phase goal, scope, numbered task list with acceptance criteria
- `tasks.md` — granular task breakdown (each task ≤ 1 day per developer)
- `test-gates.md` — TC-xxx identifiers from `TestPlan_Maduuka_Phase1.docx` that must pass before phase closes; JUnit unit tests, Espresso/Compose UI tests, and integration tests
- `skills-applied.md` — skills from `C:\Users\Peter\.claude\skills\` governing this phase
- Kotlin code snippets, Room entity definitions, or API contract fragments needed to execute

---

## 15-Phase Arc

Execute gap analysis first. Generate phases based on what the gap analysis reveals is done vs. missing. The arc covers the complete Maduuka Android product: Phase 1 core platform (Phases 1–10), Phase 2 industry add-ons (Phases 11–13), and Phase 3 advanced modules (Phases 14–15).

**Phase 1 — Foundation Audit & Environment Setup**
Goal: Clean, reproducible Android dev environment. CI/CD pipeline per `DeploymentGuide_Maduuka.docx` (GitHub Actions + Fastlane). Kotlin lint and detekt passing in CI. `CodingGuidelines_Maduuka.docx` Kotlin standards distributed to all contributors. Gradle module structure validated against `modular-saas-architecture`. Build variants confirmed: debug / staging / production. Existing code classified using the gap analysis methodology above. Output: green CI build, lint passing, gap analysis summary at `00-gap-analysis-summary.md`.

**Phase 2 — Room Schema, Multi-tenant Layer & Offline Sync Engine**
Goal: Full Room entity model mirroring `DatabaseDesign_Maduuka.docx`. Every entity carries a `franchiseId` column. DAO base class or query extension enforces `WHERE franchise_id = :franchiseId` on every fetch — a developer cannot accidentally issue an unscoped query (BR-001). EFRIS placeholder columns (nullable, names from `SRS_Maduuka_Phase3c_EFRIS.docx`) present on all relevant entities. WorkManager sync engine: `PeriodicWorkRequest` every 15 minutes and `OneTimeWorkRequest` triggered on network reconnect. Conflict resolution per `LLD_Maduuka.docx` `SyncService::processBatch()` (last-write-wins with server timestamp; conflicts logged). Pending upload Room queue for offline transactions. Apply `multi-tenant-saas-architecture`. TC-SET-001 and TC-SET-002 (cross-tenant isolation tests) must pass.

**Phase 3 — Authentication, JWT, Biometric Login & RBAC**
Goal: Full auth flow per `LLD_Maduuka.docx` `AuthService`: login → JWT access token (15-min) + refresh token (30-day) stored in EncryptedSharedPreferences. OkHttp `Authenticator` intercept for silent token refresh. Logout clears all EncryptedSharedPreferences and Room store for the tenant. Certificate pinning via OkHttp `CertificatePinner`. TOTP 2FA setup and validation per `AuthService::validateTOTP()`. BiometricPrompt re-authentication on app foreground resume. Role-based access control at every Compose screen and every API call — role definitions match `LLD_Maduuka.docx` RBAC permission matrix. Root detection at app launch (RootBeer or Play Integrity API). Apply `dual-auth-rbac`, `android-saas-planning`. TC-AUTH-xxx and TC-SEC-xxx cases must pass.

**Phase 4 — POS Core (Product Discovery, Cart, Cash Payment)**
Goal: A cashier opens a session, searches products (text search ≤ 500ms, FR-POS-001), scans barcodes (ML Kit, response < 1s, FR-POS-002), builds a cart, applies discounts (per-item and order-level), processes a cash payment, and closes the sale — all without internet (DC-003, BR-009). Session requires opening float (BR-007). All POS core FRs (FR-POS-001 through FR-POS-011, FR-POS-016 through FR-POS-017, FR-POS-021) from `SRS_Maduuka_Phase1_Draft.docx` satisfied. Screen matches `UXSpec_Maduuka.docx` POS Main Screen specification. Audit log written on every sale close (`AuditLogService`). Apply `pos-sales-ui-design`, `jetpack-compose-ui`. TC-POS-001 through TC-POS-008 must pass.

**Phase 5 — POS Payments, Bluetooth Printing, Void & Refund**
Goal: MTN MoMo Business API push payment per `LLD_Maduuka.docx` `POSService::processMoMoPayment()` — scaffold with `[BLOCKED: GAP-001]` until sandbox credentials obtained. Airtel Money equivalent. Credit sale with BR-002 enforcement and manager override (audit log entry). Multi-payment split across methods (BR-010). Offline payment queue (BR-009). All receipt delivery methods: ESC/POS Bluetooth thermal print (Epson, Xprinter, TP-Link — test all 3 printers physically before this phase closes, GAP-004 resolution), PDF export via Android share sheet, SMS and WhatsApp via Africa's Talking. Void and refund with reason code and audit log (BR-008 receipt gap detection). Apply `android-development`. TC-POS-009 through TC-POS-023 pass (MoMo cases marked [BLOCKED: GAP-001]); TC-POS-024 onwards pass.

**Phase 6 — Inventory & Stock Management**
Goal: All FR-INV-xxx satisfied per `SRS_Maduuka_Phase1_Draft.docx`. FIFO/FEFO enforced (BR-006) via `StockService::enforceFefo()` at the API layer. Batch/expiry tracking with expiry alerts (configurable: 30/60/90 days). Physical stock count workflow (freeze → count → variance → approval). Stock transfers between locations. BR-004 stock movement immutability. Reorder alerts via FCM push notification. Apply `mobile-report-tables` for stock list display. TC-INV-xxx must pass.

**Phase 7 — Customer & Supplier Management**
Goal: All FR-CUS-xxx and FR-SUP-xxx satisfied per `SRS_Maduuka_Phase1_Draft.docx`. Customer CRM: profiles, customer groups, credit accounts (BR-002 limit enforcement at POS), magic-link portal trigger (customer receives link via WhatsApp/SMS — no Android login required). Debtors ageing report on Android. Supplier directory, purchase orders, goods receiving (partial), three-way matching review (BR-011). Apply `mobile-report-tables`. TC-CUS-xxx and TC-SUP-xxx must pass.

**Phase 8 — Expenses, Financial Accounts & HR/Payroll**
Goal: Expense recording: amount, category, receipt photo (Android camera), OCR auto-extract (ML Kit Text Recognition — vendor name and amount). Expense approval workflow (BR-005). Petty cash float. Payment account dashboard (real-time balances). Bank reconciliation. Staff profiles, leave management (application → manager approval via FCM push). Attendance. Payroll computation per `LLD_Maduuka.docx` `PayrollService` formulas: NSSF (employer 10%, employee 5%), PAYE Uganda 2024/25 bands, LST (configurable). Payslip PDF and WhatsApp/email delivery. BR-012 payroll immutability enforced. All FR-EXP-xxx, FR-FIN-xxx, and FR-HR-xxx satisfied. TC-EXP-xxx, TC-FIN-xxx, and TC-HR-001 through TC-HR-009 must pass (PAYE/NSSF exact-value oracles).

**Phase 9 — Reporting, PDF Export & Dashboard**
Goal: All 14 report types from `LLD_Maduuka.docx` `ReportService` on Android: daily sales, summary, by product/category/branch/cashier/customer, trends, gross margin, voids. MPAndroidChart or Vico for visualisation. PDF export via iText/PDFBox. Android share sheet for CSV and PDF. Scheduled report FCM push notification (report-ready → open to view). Real-time KPI dashboard (Today's Revenue, Transactions, Outstanding Credit, Cash Position). Business Health Score (RAG). Branch switcher. Settings: 2FA TOTP setup (QR code flow), currency configuration (DC-005: zero hardcoded "UGX"), connected devices with remote revoke, full data export (CSV), subscription plan display. Apply `mobile-reports`, `mobile-report-tables`. TC-REP-xxx and TC-DASH-xxx must pass.

**Phase 10 — Integrations, Security Hardening & Phase 1 Go-Live**
Goal: Africa's Talking SMS and WhatsApp fully wired: SMS receipt, WhatsApp receipt share, payslip delivery, magic-link portal link. MTN MoMo Business API end-to-end (resolve GAP-001 before this phase closes). Airtel Money end-to-end. OWASP Mobile Top 10 audit and remediation. Certificate pinning verified end-to-end (rotate pinned hashes). EncryptedSharedPreferences audit — no sensitive data in plain SharedPreferences. Root detection tested on rooted device/emulator. RBAC verified at API layer. `ComplianceDocument_Maduuka.docx` data protection requirements verified. DC-004 verified on a UGX 250K Android device (2 GB RAM, Android 8): app launch < 2s cold, barcode scan < 1s, search < 500ms. All 110 TC-xxx from `TestPlan_Maduuka_Phase1.docx` passing. `AuditReport_Maduuka.docx` Phase 1 anomalies closed. Firebase App Distribution beta to 10+ testers. Google Play Phase 1 release. Apply `vibe-security-skill`, `api-testing-verification`.

**Phase 11 — Restaurant / Bar Add-On (Phase 2a)**
Goal: All 85 FRs from `SRS_Maduuka_Phase2a_Restaurant.docx` (FR-RES-001 through FR-RES-085) implemented on Android. Room schema extended with restaurant entities (tables, reservations, orders, courses, kitchen routing). New Compose screens: floor plan / table status grid, reservation list, order routing to kitchen display, course management, split-bill and merge-table flows, happy hour and promotional pricing, restaurant reporting (per-table revenue, turn time, average spend). Multi-tenant Room isolation verified on all new entities. Phase 1 test gates must not regress. Apply `pos-sales-ui-design`, `jetpack-compose-ui`.

**Phase 12 — Pharmacy / Drug Store Add-On (Phase 2b)**
Goal: All 90 FRs from `SRS_Maduuka_Phase2b_Pharmacy.docx` (FR-PHR-001 through FR-PHR-090) implemented on Android. Room schema extended with pharmacy entities (drug catalogue, prescriptions, controlled substance register, batch/expiry). New Compose screens: prescription dispensing workflow, controlled substance register with audit trail, drug expiry alerts (30/60/90-day thresholds), refill reminder trigger via Africa's Talking, pharmacy reporting (sales by drug, expiry loss, controlled substance log). Phase 1 and Phase 2a test gates must not regress. Apply `jetpack-compose-ui`, `android-development`.

**Phase 13 — Phase 2 Integration & Play Store Update**
Goal: Restaurant and Pharmacy modules pass full regression alongside Phase 1 core modules on Android. Multi-tenant Room isolation re-verified across all Phase 2 entities. API contract verified for all Phase 2 endpoints. Security hardening pass for Phase 2 Android surfaces. DC-001 through DC-006 verified for all Phase 2 screens. DC-004 re-verified on UGX 250K device with all Phase 2 screens. All Phase 2 FRs traced in `TraceabilityMatrix_Maduuka.docx`. Firebase App Distribution Phase 2 beta. Google Play update submitted with Phase 2 modules.

**Phase 14 — Hotel & Advanced Inventory Android (Phase 3a + Phase 3b)**
Goal: All 112 FRs from `SRS_Maduuka_Phase3a_Hotel.docx` and 74 FRs from `SRS_Maduuka_Phase3b_AdvancedInventory.docx` implemented on Android. Hotel Compose screens: reservation calendar (custom Compose calendar), check-in/check-out workflow, housekeeping status board, room service ordering, folio management (post POS charges to room folio), night audit. Advanced Inventory Compose screens: multi-location warehouse view, goods-in-transit tracking, bin/shelf assignment, serial number tracking, assembly/kitting (BOM), cycle count scheduling, inventory valuation report (FIFO / weighted average). Room schema extended for all Phase 3a/3b entities. Apply `jetpack-compose-ui`, `mobile-report-tables`, `multi-tenant-saas-architecture`.

**Phase 15 — EFRIS Android, Total Completion & Final Play Store Release**
Goal: All 38 FRs from `SRS_Maduuka_Phase3c_EFRIS.docx` (FR-EFR-001 through FR-EFR-038) implemented on Android — contingent on GAP-005 (URA EFRIS API sandbox access) resolution. EFRIS Compose screens: fiscal receipt display with QR code, URA Tax Account dashboard, failed submission retry queue, EFRIS audit log viewer. All EFRIS Room placeholder columns (present since Phase 2) are now active. Full regression: all phases (1, 2a, 2b, 3a, 3b, 3c) pass on Android. Traceability: all 528 FRs (129 P1 + 85 P2a + 90 P2b + 112 P3a + 74 P3b + 38 P3c) covered. All `RiskAssessment_Maduuka.docx` risks resolved or formally accepted. `AuditReport_Maduuka.docx` all anomalies closed. `InstallationGuide_Maduuka.docx` Android section reviewed and current. DC-004 final verification on target device. Firebase App Distribution final beta. Google Play production release — Maduuka Android total completion.

---

## Per-Phase Plan Document Standard

Each `PLAN.md` must contain:

```markdown
# Phase N: [Title]

## Goal
One sentence stating what is achieved when this phase closes.

## Scope
- IN scope: specific FR identifiers from the relevant SRS document for this phase
- OUT of scope: explicitly deferred items

## Prerequisites
- Prior phases that must be complete
- External dependencies (GAP-001, GAP-004, etc.)

## Task List
1. [Task title — max 1 day] — acceptance criterion (deterministic pass/fail)
2. ...

## Test Gates
TC-xxx identifiers from TestPlan_Maduuka_Phase1.docx that must pass before phase closes:
- Unit: [ViewModel, Repository, UseCase JUnit tests]
- UI: [Compose UI tests / Espresso flows]
- Integration: [Retrofit API calls against mock server or staging, expected JSON response per APISpec]

## Definition of Done Check
All items in DefinitionOfDone_Maduuka.docx satisfied? [ ] Yes — confirmed by reviewer.

## Skills Applied
- [skill-name] — how it governs this phase

## Open Gaps / Blockers
- [GAP-ID] — description and resolution owner
```

---

## Architecture Overview Document (00-gap-analysis-summary.md)

The gap analysis summary is the first output produced, before any phase plan. It must cover:

1. **Gap matrix** — for each of the 10 Phase 1 modules, classification of each component (Room entity, DAO, Repository, ViewModel, Compose screen, tests) as Complete / Partial / Phantom / Broken
2. **Cross-cutting audit results** — multi-tenant isolation, RBAC, error envelope, pagination, offline queue, WorkManager, audit log, currency strings, cert pinning findings
3. **Architecture assessment** — does the existing structure enforce MVVM + Clean Architecture? Where are the deviations?
4. **Room entity design** — how the 30+ tables in `DatabaseDesign_Maduuka.docx` map to existing Room entities and what is missing
5. **Sync architecture** — WorkManager sync task design, pending queue entity, idempotency key strategy per `LLD_Maduuka.docx` `SyncService`, conflict resolution policy
6. **Network layer design** — Retrofit interface completeness, OkHttp interceptor for JWT refresh, certificate pinning, error mapping to domain errors using `TechnicalSpec_Maduuka.docx` error envelope
7. **RBAC enforcement pattern** — how role is stored, how every Compose screen and action checks permissions per `LLD_Maduuka.docx` permission matrix
8. **Phase 2/3 extension points** — what exists in the current architecture that will accommodate Restaurant, Pharmacy, Hotel, EFRIS module additions without refactoring Phase 1 foundations
9. **Recommended phase sequence** — based on actual gap findings, confirm or adjust the 15-phase arc

---

## Constraints

- Base every plan item on the gap analysis evidence or a specific SRS document. Do not invent scope.
- Every phase has explicit test gates referencing TC-xxx identifiers from `TestPlan_Maduuka_Phase1.docx`. No phase closes without green tests. Apply `superpowers:test-driven-development` throughout.
- The `DefinitionOfDone_Maduuka.docx` checklist applies to every task. No task is done without satisfying all criteria.
- Apply `ai-slop-prevention` — every task must be actionable by an Android developer working independently without verbal clarification from the architect.
- Do not re-plan work the gap analysis confirms is already complete. Only plan the delta.
- This plan covers ONLY the Android app. The shared backend API is built by the web team. The Android developer consumes the API — they do not modify it. Web is in `docs/plans/maduuka-web-completion/PROMPT.md`. iOS is in `docs/plans/maduuka-ios/PROMPT.md`.
- This plan covers the TOTAL completion of Maduuka Android: Phase 1 core (Phases 1–10), Phase 2 add-ons (Phases 11–13), and Phase 3 advanced modules (Phases 14–15). All 528 FRs across all SRS documents are in scope.
- GAP-004 (Android Bluetooth printer compatibility with Ugandan market printers: Epson, Xprinter, TP-Link) must be resolved with physical printer testing before Phase 5 closes.
- GAP-001 (MTN MoMo Business API sandbox credentials) must be resolved before Phase 10 closes. Phase 5 MoMo payment tasks are scaffolded but marked `[BLOCKED: GAP-001]`.
- GAP-005 (URA EFRIS API sandbox credentials) must be resolved before Phase 15 closes. Phase 15 EFRIS API tasks are marked `[BLOCKED: GAP-005]` until credentials are available.
- All output goes to `docs/plans/maduuka-android/` relative to the Maduuka project root.
