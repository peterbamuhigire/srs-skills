# Maduuka iOS App: 25-Phase Total Completion Plan

You are a senior iOS architect and technical lead for the Maduuka project (Chwezi Core Systems)
— a mobile-first, multi-tenant SaaS POS and business management platform, Uganda-first, expanding
pan-Africa. The iOS app achieves feature parity with the web and Android apps across ALL product
phases: Phase 1 (core platform, 10 modules), Phase 2 (Restaurant/Bar + Pharmacy add-ons), and
Phase 3 (Hotel + Advanced Inventory + EFRIS compliance).

The team is micro (2–5 people). Methodology is Water-Scrum-Fall: formal requirements sign-off per
phase, iterative delivery within phases.

**The iOS app is a new build — it is not a port of the Android app.** It must be architecturally
idiomatic Swift/SwiftUI and achieve complete feature parity with the web and Android apps. Every
feature available on web must be available on iOS, and vice versa (Design Covenant DC-001).

**The plan you generate is the iOS development contract. Every phase must be independently
executable by the iOS developer without verbal clarification from the architect.**

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
- `02-requirements-engineering/SRS_Maduuka_Phase1_Draft.docx` — 129 FRs for all 10 Phase 1 modules, IEEE 830 compliant, stimulus-response format (Android + Web primary reference)
- `02-requirements-engineering/SRS_Maduuka_iOS_Platform.docx` — **PRIMARY iOS REFERENCE**: 63 iOS-specific requirements covering 13 NFRs, 33 module FRs, 6 sync FRs, 11 security FRs. Every iOS task must trace to a requirement in this document.
- `02-requirements-engineering/UserStories_Maduuka.docx` — 52 user stories mapped to FR identifiers, MoSCoW priorities
- `02-requirements-engineering/StakeholderAnalysis_Maduuka.docx` — Stakeholder register, Power/Interest grid, RACI matrix
- `02-requirements-engineering/SRS_Maduuka_Phase2a_Restaurant.docx` — Restaurant/Bar add-on, 85 FRs (Phase 2 — plan the architecture foundation only)
- `02-requirements-engineering/SRS_Maduuka_Phase2b_Pharmacy.docx` — Pharmacy add-on, 90 FRs (Phase 2 — plan the architecture foundation only)
- `02-requirements-engineering/SRS_Maduuka_Phase3a_Hotel.docx` — Hotel/Accommodation, 112 FRs (Phase 3 — architecture awareness only)
- `02-requirements-engineering/SRS_Maduuka_Phase3b_AdvancedInventory.docx` — Advanced Inventory, 74 FRs (Phase 3 — architecture awareness only)
- `02-requirements-engineering/SRS_Maduuka_Phase3c_EFRIS.docx` — EFRIS Compliance, 38 FRs (Phase 3 — EFRIS placeholder attributes must be present in Core Data from Phase 2)

### Design Documentation (Phase 03)
- `03-design-documentation/HLD_Maduuka.docx` — System context, component architecture, multi-tenant model, RBAC matrix
- `03-design-documentation/LLD_Maduuka.docx` — **IMPLEMENTATION REFERENCE**: service layer design, method signatures, PAYE/NSSF formulas, audit log schema, offline sync engine design, RBAC permission matrix for all 24 endpoint groups. iOS consumes the same service contracts as Android and web.
- `03-design-documentation/APISpec_Maduuka_Phase1.docx` — 64 REST endpoints, request/response schemas, error codes (iOS consumes identically to Android)
- `03-design-documentation/DatabaseDesign_Maduuka.docx` — 30+ tables, entity relationships, EFRIS placeholder columns (Core Data mirrors this schema)
- `03-design-documentation/UXSpec_Maduuka.docx` — 39 screens, interaction patterns, Design Covenant validation checklist (governs iOS UI)

### Development Artifacts (Phase 04)
- `04-development-artifacts/TechnicalSpec_Maduuka.docx` — **MANDATORY READING**: iOS tech stack spec, JWT/Keychain auth, error envelope format, pagination format, CI/CD pipeline definition. The iOS developer must read this before writing a line of code.
- `04-development-artifacts/CodingGuidelines_Maduuka.docx` — **MANDATORY READING**: Swift coding standards section, Git workflow, per-PR security checklist. All contributors must read before starting.

### Testing Documentation (Phase 05)
- `05-testing-documentation/TestStrategy_Maduuka.docx` — 8 test levels (unit, integration, system, UAT, performance, security, offline/sync, regression), entry/exit criteria, IEEE 829/1012
- `05-testing-documentation/TestPlan_Maduuka_Phase1.docx` — **TEST GATE REFERENCE**: 110 executable test cases with TC-xxx identifiers. Every phase must reference which TC-xxx cases must pass before it closes. iOS must achieve parity on all 110 test cases.

### Operations (Phase 06)
- `06-deployment-operations/DeploymentGuide_Maduuka.docx` — Server setup, CI/CD pipeline (includes iOS/Fastlane), post-deployment verification
- `06-deployment-operations/Runbook_Maduuka.docx` — 6 incident procedures, 4 maintenance procedures

### Agile Artifacts (Phase 07)
- `07-agile-artifacts/SprintPlanning_Maduuka.docx` — 12-sprint Phase 1 plan (Android+Web); iOS Phase 2 sprint structure derives from this baseline
- `07-agile-artifacts/DefinitionOfDone_Maduuka.docx` — **DoD: every iOS task must satisfy ALL criteria before marking done**
- `07-agile-artifacts/DefinitionOfReady_Maduuka.docx` — DoR: every story must satisfy ALL criteria before sprint pull

### End-User Documentation (Phase 08)
- `08-end-user-documentation/UserManual_Maduuka.docx` — Plain-language manual for Agnes (Cashier) persona; iOS flows must match documented workflows
- `08-end-user-documentation/InstallationGuide_Maduuka.docx` — Android + Web setup; iOS section to be added in Phase 20
- `08-end-user-documentation/FAQ_Maduuka.docx` — 30 questions across 6 topic groups

### Governance and Compliance (Phase 09)
- `09-governance-compliance/TraceabilityMatrix_Maduuka.docx` — 129 FRs → Business Goal → TC-xxx test case ID; iOS requirements in `SRS_Maduuka_iOS_Platform.docx` must be cross-referenced
- `09-governance-compliance/AuditReport_Maduuka.docx` — IEEE 1012 audit, Conditional Pass verdict, 7 open anomalies; iOS plan must close relevant anomalies
- `09-governance-compliance/ComplianceDocument_Maduuka.docx` — Uganda Data Protection Act, URA tax compliance; iOS Keychain storage and data residency must satisfy these requirements
- `09-governance-compliance/RiskAssessment_Maduuka.docx` — 13 risks: 3 Critical, 6 High; GAP-004 (iOS Bluetooth printer) is a High risk directly affecting this plan

---

## Mandatory Skill Activation — Do This First

Load and apply the following skills in this order before any other action:

1. `superpowers:brainstorming` — structure thinking before architecture decisions.
2. `superpowers:writing-plans` — govern how phase plan documents are authored.
3. `superpowers:dispatching-parallel-agents` — use parallel agents for independent module plans.
4. `superpowers:test-driven-development` — every feature task has a paired test task. No feature
   closes without the corresponding TC-xxx test cases from `TestPlan_Maduuka_Phase1.docx` passing.
5. `swiftui-design` — SwiftUI component choices, layout, animations, and accessibility.
6. `swiftui-pro-patterns` — architecture patterns, property wrappers, Combine integration.

From `C:\Users\Peter\.claude\skills\`, load and apply throughout:

**iOS Development:**
- `ios-development` — iOS-specific development patterns and Apple platform constraints.
- `ios-project-setup` — Xcode project structure, targets, schemes, build configurations per `TechnicalSpec_Maduuka.docx`.
- `ios-tdd` — Test-driven development with XCTest; TC-xxx test case parity from `TestPlan_Maduuka_Phase1.docx`.
- `ios-rbac` — Role-based access control on iOS: every screen and action gated by user role per `LLD_Maduuka.docx` permission matrix.
- `ios-data-persistence` — Core Data schema design, migrations, iCloud sync considerations; schema mirrors `DatabaseDesign_Maduuka.docx`.
- `ios-biometric-login` — Face ID / Touch ID implementation with LocalAuthentication framework.
- `ios-bluetooth-printing` — Core Bluetooth / Raw Print for 80mm thermal printers (Epson, Xprinter, TP-Link). GAP-004: test all 3 printers in Uganda market before Phase 9 closes.
- `ios-pdf-export` — PDF generation for receipts, invoices, payslips, and reports.
- `mobile-rbac` — Cross-platform RBAC consistency between iOS, Android, and web.
- `mobile-reports` — Report display, filtering, and export on mobile.
- `mobile-report-tables` — Tabular data display optimised for small screens.

**Architecture:**
- `multi-tenant-saas-architecture` — `franchise_id` isolation verified at Core Data, API, and UI layers per `LLD_Maduuka.docx`.
- `modular-saas-architecture` — feature module boundaries and dependency management.
- `dual-auth-rbac` — JWT Bearer token authentication with biometric re-auth per `LLD_Maduuka.docx` `AuthService` spec.

**UI/UX:**
- `pos-sales-ui-design` — POS screen design patterns on iOS per `UXSpec_Maduuka.docx`.
- `cognitive-ux-framework` — DC-002 (zero mandatory training) validation against `UXSpec_Maduuka.docx` checklist.
- `form-ux-design` — all form designs, keyboard management, input validation.
- `healthcare-ui-design` — Pharmacy module screens (Phase 2 — plan the architecture foundation only in Phase 1).
- `interaction-design-patterns` — gesture-driven interactions, SwiftUI transitions.
- `motion-design` — purposeful micro-animations on a low-end device budget.

**Security:**
- `vibe-security-skill` — security review at every phase; `ComplianceDocument_Maduuka.docx` requirements.
- `ios-biometric-login` — biometric re-authentication on app resume.

**App Store:**
- `ios-project-setup` — App Store distribution configuration, signing, entitlements per `DeploymentGuide_Maduuka.docx`.
- `app-store-review` — App Store Review Guidelines compliance gate before Phase 20.

**Testing:**
- `sdlc-testing` — test strategy alignment with `TestStrategy_Maduuka.docx`.
- `ios-tdd` — XCTest unit and UI test suites; TC-xxx parity from `TestPlan_Maduuka_Phase1.docx`.
- `api-testing-verification` — API contract verification from iOS client against `APISpec_Maduuka_Phase1.docx`.

---

## iOS Tech Stack (Reference)

| Layer | Technology |
|---|---|
| Language | Swift 5.9+ (`CodingGuidelines_Maduuka.docx` Swift standards apply) |
| UI Framework | SwiftUI (iOS 16+ minimum deployment target) |
| Architecture | MVVM + Clean Architecture (Presentation / Domain / Data) |
| Local Database | Core Data (SQLite) — offline-first; schema mirrors `DatabaseDesign_Maduuka.docx` |
| Networking | URLSession + async/await; Alamofire if justified |
| Auth | JWT Bearer: 15-min access token + 30-day refresh; stored in Keychain (AES-256) |
| Biometric | LocalAuthentication — Face ID / Touch ID |
| Encrypted Storage | Keychain Services for tokens; CryptoKit for sensitive local data |
| Certificate Pinning | URLSession delegate with pinned certificate hashes |
| Barcode Scanning | AVFoundation + Vision framework (EAN-13, EAN-8, Code-128, QR) |
| Bluetooth Printing | Core Bluetooth / Raw Print protocol (80mm thermal: Epson, Xprinter, TP-Link) |
| Background Sync | BackgroundTasks framework (BGAppRefreshTask, BGProcessingTask) — every 15 min |
| Push Notifications | APNs via Firebase Cloud Messaging |
| PDF Generation | PDFKit + Core Graphics (receipts, payslips, reports) |
| Root/Jailbreak Detection | At app launch — DTTJailbreakDetection or equivalent |
| Maps | MapKit (customer location map) |
| Charts | Swift Charts (iOS 16+) |
| SMS/WhatsApp | Africa's Talking API (via backend — no direct iOS SDK) |
| Mobile Money | MTN MoMo Business API + Airtel Money API (via backend — no direct iOS SDK) |
| CI/CD | Xcode Cloud or GitHub Actions with Fastlane per `DeploymentGuide_Maduuka.docx` |
| Distribution | TestFlight (beta) → App Store (production) |

---

## Shared Backend API (iOS Consumes Identically to Android)

- Single REST API — no iOS-specific endpoints.
- Base URL: configurable at build time (dev / staging / production schemes per `TechnicalSpec_Maduuka.docx`).
- Auth: JWT Bearer token in `Authorization` header per `LLD_Maduuka.docx` `AuthService` spec.
- All 64 endpoints documented in `APISpec_Maduuka_Phase1.docx`.
- Error format: standardised JSON error response per `TechnicalSpec_Maduuka.docx` error envelope.
- Pagination: cursor-based or offset — match the pagination envelope in `TechnicalSpec_Maduuka.docx` exactly.

---

## Design Covenant (All 6 Are Binding)

Every phase task must be verified against all 6 constraints from `VisionStatement_Maduuka.docx`:

- **DC-001:** iOS has feature parity with web and Android. No feature on web/Android absent from iOS.
- **DC-002:** Zero mandatory training. Agnes (Cashier persona) completes a sale in under 3 minutes, first try. Validate against `UXSpec_Maduuka.docx` DC-002 checklist.
- **DC-003:** Offline-first. POS, stock lookup, and dashboard work with airplane mode on.
- **DC-004:** Works on the cheapest iPhone. Target: iPhone X equivalent (A11, 3 GB RAM, iOS 16). No animations that drop below 60fps on this device.
- **DC-005:** Currency-neutral. No hardcoded "UGX" strings. Currency symbol from tenant configuration.
- **DC-006:** Compliance built in. EFRIS-ready Core Data attributes present from Phase 2. EFRIS UI placeholders visible. See `SRS_Maduuka_Phase3c_EFRIS.docx` for attribute names.

---

## Critical Business Rules (Enforce on iOS)

Read `business_rules.md` for the full set. These rules are non-negotiable:

- **BR-001:** Every Core Data fetch and API request scoped to `franchise_id`. Tenant isolation is absolute. See `LLD_Maduuka.docx` multi-tenant section.
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

The `LLD_Maduuka.docx` defines method signatures for all service classes. The iOS app consumes the same contracts via the REST API. Reference these when building the network layer and Core Data sync logic:

- `AuthService` — login, refreshToken, logout, validateTOTP
- `RBACMiddleware` — permission matrix for all 24 endpoint groups across 6 roles; governs iOS `ios-rbac` implementation
- `POSService` — openSession, processSale, processMoMoPayment [BLOCKED: GAP-001], holdSale, voidSale, closeSession
- `SyncService` — processBatch with idempotency key and conflict resolution; governs BGAppRefreshTask implementation
- `StockService` — recordMovement, enforceFefo, initiateStockCount, submitCountVariance, approveAdjustment
- `PayrollService` — computePayroll, approvePayroll, generatePayslip; PAYE/NSSF/LST formulas defined here
- `ReportService` — Template Method pattern; 14 Phase 1 report types; governs iOS PDF generation scope
- `AuditLogService` — append-only; 21 domain event → action code mappings; iOS must trigger these via API on every create/update/delete/void/adjustment

---

## Output Structure

All output goes to `docs/plans/maduuka-ios/` (relative to the Maduuka project root).

```
docs/plans/maduuka-ios/
├── 00-ios-architecture-overview.md      Architecture decisions, Core Data design, sync strategy
├── 01-project-setup/                    Phase 1  — Xcode project setup & architecture
├── 02-core-data-multitenant/            Phase 2  — Core Data schema & multi-tenant foundation
├── 03-authentication-jwt/               Phase 3  — Authentication & JWT token management
├── 04-biometric-rbac/                   Phase 4  — Biometric login, RBAC & jailbreak detection
├── 05-offline-sync-engine/              Phase 5  — Offline sync engine
├── 06-dashboard-navigation/             Phase 6  — Dashboard & navigation
├── 07-pos-core/                         Phase 7  — POS core
├── 08-pos-payments/                     Phase 8  — POS payments
├── 09-pos-receipts-bluetooth/           Phase 9  — Receipts, Bluetooth printing, void & refund
├── 10-inventory-stock/                  Phase 10 — Inventory & stock management
├── 11-customers-suppliers/              Phase 11 — Customer & supplier management
├── 12-expenses-financial/               Phase 12 — Expenses, financial accounts & cash flow
├── 13-reporting-pdf/                    Phase 13 — Sales reporting & PDF export
├── 14-hr-payroll/                       Phase 14 — HR & payroll
├── 15-settings-configuration/           Phase 15 — Settings & configuration
├── 16-integrations-africa/              Phase 16 — Africa's Talking & mobile money integration
├── 17-ui-polish-icons-branding/         Phase 17 — UI polish, icons & branding
├── 18-security-hardening/               Phase 18 — Security hardening
├── 19-performance-device-testing/       Phase 19 — Performance & low-end device testing
├── 20-testflight-appstore-phase1/       Phase 20 — TestFlight beta & Phase 1 App Store release
├── 21-restaurant-bar-ios/               Phase 21 — Restaurant/Bar add-on iOS (85 FRs, Phase 2a)
├── 22-pharmacy-ios/                     Phase 22 — Pharmacy/Drug Store iOS (90 FRs, Phase 2b)
├── 23-phase2-appstore-update/           Phase 23 — Phase 2 integration & App Store update
├── 24-hotel-adv-inventory-ios/          Phase 24 — Hotel + Advanced Inventory iOS (Phase 3a/3b)
└── 25-efris-total-completion/           Phase 25 — EFRIS iOS + total completion & final release
```

Each phase directory contains:
- `PLAN.md` — phase goal, scope, numbered task list with acceptance criteria
- `tasks.md` — granular task breakdown (each task ≤ 1 day of work for one iOS developer)
- `test-gates.md` — TC-xxx identifiers from `TestPlan_Maduuka_Phase1.docx` that must pass before phase closes; XCTest unit tests, UI tests, and integration tests
- `skills-applied.md` — skills from `C:\Users\Peter\.claude\skills\` governing this phase
- Swift code snippets, Core Data entity definitions, or API contract fragments needed to execute

---

## 25-Phase Arc

Generate phases in this arc. Every phase builds on the one before it. The arc covers the complete Maduuka iOS product: Phase 1 core parity (Phases 1–20), Phase 2 add-ons (Phases 21–23), and Phase 3 advanced modules (Phases 24–25).

**Phase 1 — iOS Project Setup & Architecture**
Goal: A clean, production-ready Xcode project with correct signing, targets, schemes (debug /
staging / production), CI/CD pipeline per `DeploymentGuide_Maduuka.docx`, and folder structure
enforcing MVVM + Clean Architecture. Apply `ios-project-setup` and `CodingGuidelines_Maduuka.docx`
Swift standards. No feature code — only the skeleton that all subsequent phases build on.
Output: Green CI build. SwiftLint passing. README with setup instructions.

**Phase 2 — Core Data Schema & Multi-tenant Foundation**
Goal: Full Core Data entity model mirroring the `DatabaseDesign_Maduuka.docx` schema.
Every entity carries a `franchiseId` attribute. NSFetchRequest helper wrappers enforce
`franchiseId == currentTenant` on every fetch — a developer cannot accidentally issue an
unscoped query. EFRIS placeholder attributes (nullable, names from `SRS_Maduuka_Phase3c_EFRIS.docx`)
present on all relevant entities. Apply `ios-data-persistence`, `multi-tenant-saas-architecture`.
TC-SET-001 and TC-SET-002 (cross-tenant isolation tests) must pass.

**Phase 3 — Authentication & JWT Token Management**
Goal: Full auth flow per `LLD_Maduuka.docx` `AuthService`: login → JWT access token (15-min) +
refresh token (30-day) stored in Keychain. Auto-refresh on token expiry. Logout clears all Keychain
entries and Core Data store. Certificate pinning via URLSession delegate. TOTP 2FA setup and
validation (`AuthService::validateTOTP()`). Apply `dual-auth-rbac`, `ios-development`.
TC-AUTH-xxx cases must pass.

**Phase 4 — Biometric Login, RBAC & Jailbreak Detection**
Goal: Face ID / Touch ID re-authentication on app foreground resume per `ios-biometric-login`.
Role-based access control at every SwiftUI view and every API call. Role definitions match the
RBAC matrix in `LLD_Maduuka.docx` (24 endpoint groups, 6 roles). Jailbreak detection at app
launch — warn user, log audit event, optionally block (configurable per tenant). Apply
`ios-rbac`, `mobile-rbac`. TC-SEC-xxx security cases must pass.

**Phase 5 — Offline Sync Engine**
Goal: The Core Data ↔ server sync engine is the backbone of DC-003 (offline-first). This phase
builds it before any feature module. Implement: background sync every 15 minutes
(BGAppRefreshTask per `TechnicalSpec_Maduuka.docx`), online sync on reconnect, pending upload
queue for transactions created offline, conflict resolution strategy per `LLD_Maduuka.docx`
`SyncService::processBatch()` (last-write-wins with server timestamp, log conflicts), sync status
indicator (last sync time, pending count). Apply `ios-data-persistence`, `multi-tenant-saas-architecture`.
TC-SYNC-xxx offline/sync test cases must pass.

**Phase 6 — Dashboard & Navigation**
Goal: App entry point per `UXSpec_Maduuka.docx` Dashboard screen specification. Bottom tab bar
(5 tabs: Dashboard, POS, Inventory, Reports, More). Real-time KPI cards (Today's Revenue,
Transactions, Outstanding Credit, Cash Position). Business Health Score (RAG: green/amber/red
based on gross margin %, expense ratio, stock turnover, collection rate). Branch switcher. POS
session status indicator. Apply `swiftui-design`, `pos-sales-ui-design`.
TC-DASH-xxx cases must pass.

**Phase 7 — POS Core (Product Discovery, Cart, Cash Payment)**
Goal: A cashier opens a session, searches products (text search + AVFoundation barcode scan,
FR-POS-002 response < 1s), builds a cart, applies discounts (per-item and order-level), processes
a cash payment, and prints or shares a receipt — all without internet (DC-003). Satisfies all
iOS-equivalent FRs from `SRS_Maduuka_iOS_Platform.docx` for POS core plus FR-POS-001 through
FR-POS-011, FR-POS-016 through FR-POS-017, FR-POS-021 from `SRS_Maduuka_Phase1_Draft.docx`.
Screen matches `UXSpec_Maduuka.docx` POS Main Screen specification. Apply `pos-sales-ui-design`.
TC-POS-001 through TC-POS-008 must pass.

**Phase 8 — POS Payments (MoMo, Airtel, Credit, Multi-Payment)**
Goal: MTN MoMo Business API push payment flow per `LLD_Maduuka.docx` `POSService::processMoMoPayment()`
(pending indicator → success/failure → retry). Airtel Money equivalent. Credit sale with BR-002
enforcement and manager override (audit log entry via `AuditLogService`). Multi-payment split
across methods (BR-010). Offline payment queue (BR-009). Flag MTN MoMo cases as
`[BLOCKED: GAP-001]` until sandbox credentials are available. Satisfies iOS payment FRs from
`SRS_Maduuka_iOS_Platform.docx`. TC-POS-009 through TC-POS-023 must pass (MoMo cases marked
[BLOCKED: GAP-001]).

**Phase 9 — POS Receipts, Bluetooth Thermal Printing, Void & Refund**
Goal: All receipt delivery methods: Core Bluetooth 80mm thermal print (Epson, Xprinter, TP-Link —
GAP-004 resolved: test all 3 printers physically before this phase closes), PDF export via iOS
share sheet per `ios-pdf-export`, SMS and WhatsApp via Africa's Talking. Void and refund with
reason code and audit log (`AuditLogService` action codes from `LLD_Maduuka.docx`). Receipt gap
detection (BR-008). Apply `ios-bluetooth-printing`, `ios-pdf-export`.
TC-POS-024 onwards must pass.

**Phase 10 — Inventory & Stock Management**
Goal: Full product catalogue (F-002) on iOS per iOS inventory FRs in `SRS_Maduuka_iOS_Platform.docx`.
FIFO/FEFO enforced (BR-006) via `StockService::enforceFefo()` at the API layer. Batch/expiry
tracking with expiry alerts (configurable: 30/60/90 days). Physical stock count workflow
(freeze → count → variance → approval). Stock transfers between locations. BR-004 immutability
enforced (no direct edits — counter-entries only). Reorder alerts. Apply `mobile-report-tables`
for stock list display. TC-INV-xxx must pass.

**Phase 11 — Customer & Supplier Management**
Goal: Customer CRM per iOS CRM FRs in `SRS_Maduuka_iOS_Platform.docx`: profiles, customer
groups, credit accounts (BR-002), magic-link portal trigger (customer receives link via
WhatsApp/SMS — no iOS login). Debtors ageing report. Supplier directory, purchase orders,
goods receiving (partial), three-way matching review (BR-011). All FR-CUS-xxx and FR-SUP-xxx
from `SRS_Maduuka_Phase1_Draft.docx` satisfied at iOS parity. TC-CUS-xxx and TC-SUP-xxx must pass.

**Phase 12 — Expenses, Financial Accounts & Cash Flow**
Goal: Expense recording per iOS finance FRs in `SRS_Maduuka_iOS_Platform.docx`: amount,
category, receipt photo (iOS camera), OCR auto-extract (Vision framework — vendor name and
amount). Expense approval workflow (BR-005). Petty cash float. Payment account dashboard
(real-time balances). Bank reconciliation. All FR-EXP-xxx and FR-FIN-xxx from
`SRS_Maduuka_Phase1_Draft.docx` satisfied. TC-EXP-xxx and TC-FIN-xxx must pass.

**Phase 13 — Sales Reporting & PDF Export**
Goal: All 14 report types from `LLD_Maduuka.docx` `ReportService` on iOS: daily sales, summary,
by product/category/branch/cashier/customer, trends, gross margin, voids. Swift Charts for
visualisation. PDF export via PDFKit. iOS share sheet for CSV and PDF. Scheduled report push
notification (report-ready → open to view). Apply `ios-pdf-export`, `mobile-reports`,
`mobile-report-tables`. TC-REP-xxx must pass.

**Phase 14 — HR & Payroll**
Goal: Staff profiles, leave management (application → manager approval via push notification),
attendance. Payroll computation per `LLD_Maduuka.docx` `PayrollService` formulas: NSSF (employer
10%, employee 5%), PAYE Uganda 2024/25 bands (0% ≤ UGX 235K, 10% 235K–335K, 20% 335K–410K,
30% > 410K monthly), LST (configurable). Payslip PDF generation and delivery via WhatsApp/email.
Payroll immutability after approval (BR-012). All FR-HR-xxx from `SRS_Maduuka_Phase1_Draft.docx`
satisfied. TC-HR-001 through TC-HR-009 must pass (PAYE/NSSF exact-value test oracles).

**Phase 15 — Settings & Configuration**
Goal: Business profile (name, logo, address, TIN). Receipt customisation with live iOS preview.
Tax settings (VAT 18%, zero-rated, exempt; inclusive/exclusive toggle). Currency configuration
(any world currency — DC-005 audit: zero hardcoded "UGX" strings in the entire iOS codebase).
2FA TOTP setup (QR code + authenticator app flow per `LLD_Maduuka.docx` `AuthService::validateTOTP()`).
Connected devices list with remote revoke. Full data export (CSV). Account deletion with data
export. Subscription plan display and upgrade CTA. Verify `ComplianceDocument_Maduuka.docx`
data residency requirements are met. TC-SET-xxx must pass.

**Phase 16 — Africa's Talking Integration & Magic-Link Portal**
Goal: Africa's Talking SMS and WhatsApp fully wired from iOS-triggered events: SMS receipt
(FR-POS-020), WhatsApp receipt share (FR-POS-019), payslip delivery, magic-link customer portal
link. MTN MoMo Business API end-to-end integration — resolve GAP-001 before this phase closes.
Airtel Money end-to-end. Apply `api-testing-verification` against `APISpec_Maduuka_Phase1.docx`.
TC-INT-xxx integration test cases must pass.

**Phase 17 — UI Polish, Custom Icons & App Branding**
Goal: Consistent Chwezi Core Systems / Maduuka branding throughout the app per `UXSpec_Maduuka.docx`
Design Covenant validation checklist. Custom app icon (all required sizes and dark mode variants).
SF Symbols + custom icon set for navigation and features. Dark mode support. Dynamic Type
(accessibility text scaling). All 39 screens pass `UXSpec_Maduuka.docx` DC-002 checklist.
Apply `swiftui-design`, `motion-design`, `interaction-design-patterns`.

**Phase 18 — Security Hardening**
Goal: Certificate pinning verified end-to-end (rotate pinned hashes). Keychain storage audit —
no sensitive data in UserDefaults. Jailbreak detection tested on jailbroken device/simulator.
RBAC enforcement verified at API layer (iOS cannot bypass by crafting raw requests). All 11
iOS security FRs from `SRS_Maduuka_iOS_Platform.docx` satisfied. AES-256 Keychain encryption
for tokens and sensitive settings. `ComplianceDocument_Maduuka.docx` data protection requirements
verified. Apply `vibe-security-skill`, `ios-development`. TC-NFR-011 through TC-NFR-019 must pass.

**Phase 19 — Performance Optimisation & Low-End Device Testing**
Goal: Verified performance on iPhone X (A11 bionic, iOS 16) — DC-004 target device. Instruments
profile: no memory leaks, no retain cycles, no main-thread blocks > 16ms. Core Data fetch
optimisation: faulting, batch fetch, background context. App launch time < 2s cold start.
Barcode scan response < 1s (FR-POS-002). Search results < 500ms (FR-POS-001). All 6 iOS sync
FRs from `SRS_Maduuka_iOS_Platform.docx` verified under simulated poor network. PWA web fallback
for iOS users before native app ships — confirm decommission plan.
TC-NFR performance cases must pass.

**Phase 20 — TestFlight Beta, App Store Submission & Phase 1 Go-Live**
Goal: App Store Review Guidelines compliance (Privacy Nutrition Label, App Privacy policy,
no 3rd-party code violations). Fastlane match for code signing per `DeploymentGuide_Maduuka.docx`.
TestFlight build distributed to 10+ beta testers (business owners, cashiers matching personas
in `StakeholderAnalysis_Maduuka.docx`). Crash-free sessions > 99% in TestFlight. All 110
TC-xxx test cases from `TestPlan_Maduuka_Phase1.docx` passing on iOS. `InstallationGuide_Maduuka.docx`
iOS section authored and delivered. Phase 1 App Store release — 10 core modules live. Apply `app-store-review`.

**Phase 21 — Restaurant / Bar iOS (Phase 2a)**
Goal: All 85 FRs from `SRS_Maduuka_Phase2a_Restaurant.docx` (FR-RES-001 through FR-RES-085)
implemented on iOS with feature parity to the web app. Core Data schema extended with restaurant
entities (tables, reservations, orders, courses, kitchen routing). New SwiftUI screens: floor plan
view, table status grid, order routing to kitchen display, course management, split-bill and
merge-table flows, happy hour and promotional pricing, restaurant reporting (per-table revenue,
turn time, average spend). Apply `pos-sales-ui-design`, `swiftui-design`, `ios-data-persistence`.
Restaurant module regression must not break Phase 1 test gates.

**Phase 22 — Pharmacy / Drug Store iOS (Phase 2b)**
Goal: All 90 FRs from `SRS_Maduuka_Phase2b_Pharmacy.docx` (FR-PHR-001 through FR-PHR-090)
implemented on iOS with feature parity to the web app. Core Data schema extended with pharmacy
entities (drug catalogue, prescriptions, controlled substance register, batch/expiry). New SwiftUI
screens: prescription dispensing workflow, controlled substance register with audit trail, drug
expiry alerts (30/60/90-day thresholds), refill reminder trigger via Africa's Talking,
pharmacy-specific reporting (sales by drug, expiry loss, controlled substance log). Apply
`healthcare-ui-design`, `ios-data-persistence`, `ios-pdf-export`. Pharmacy module regression must
not break Phase 1 and Phase 2a test gates.

**Phase 23 — Phase 2 iOS Integration & App Store Update**
Goal: Restaurant and Pharmacy modules pass full regression alongside Phase 1 modules on iOS.
Multi-tenant Core Data isolation re-verified across all Phase 2 entities. API contract verified
for all new Phase 2 endpoints against `APISpec_Maduuka_Phase1.docx` amendments. Security
hardening pass for Phase 2 iOS surfaces. DC-001 through DC-006 verified for all Phase 2 screens.
All Phase 2 FRs traced in `TraceabilityMatrix_Maduuka.docx`. TestFlight Phase 2 beta distributed.
App Store update submitted with Phase 2 modules. Apply `app-store-review`, `vibe-security-skill`.

**Phase 24 — Hotel & Advanced Inventory iOS (Phase 3a + Phase 3b)**
Goal: All 112 FRs from `SRS_Maduuka_Phase3a_Hotel.docx` and 74 FRs from
`SRS_Maduuka_Phase3b_AdvancedInventory.docx` implemented on iOS. Hotel screens: reservation
calendar (SwiftUI calendar view), check-in/check-out workflow, housekeeping status board, room
service ordering, folio management (post POS charges to room), night audit. Advanced Inventory
screens: multi-location warehouse view, goods-in-transit tracking, bin/shelf assignment, serial
number tracking, assembly/kitting (BOM), cycle count scheduling, inventory valuation report
(FIFO / weighted average). Core Data schema extended for all Phase 3a/3b entities. Apply
`ios-data-persistence`, `mobile-report-tables`, `multi-tenant-saas-architecture`.

**Phase 25 — EFRIS iOS, Total Completion & Final App Store Release**
Goal: All 38 FRs from `SRS_Maduuka_Phase3c_EFRIS.docx` (FR-EFR-001 through FR-EFR-038)
implemented on iOS — contingent on GAP-005 resolution. EFRIS screens: fiscal receipt display
with QR code, URA Tax Account dashboard, failed submission retry queue, EFRIS audit log viewer.
All EFRIS Core Data placeholder attributes (present since Phase 2) are now active. Full
regression: all phases (1, 2a, 2b, 3a, 3b, 3c) pass on iOS. Traceability: all 528 FRs
(129 P1 + 85 P2a + 90 P2b + 112 P3a + 74 P3b + 38 P3c) covered. All `RiskAssessment_Maduuka.docx`
risks resolved or formally accepted. `AuditReport_Maduuka.docx` all anomalies closed. Final
TestFlight beta. Final App Store release — Maduuka iOS total completion. Apply `app-store-review`.

---

## Per-Phase Plan Document Standard

Each `PLAN.md` must contain:

```markdown
# Phase N: [Title]

## Goal
One sentence stating what is achieved when this phase closes.

## Scope
- IN scope: specific iOS SRS requirement IDs from SRS_Maduuka_iOS_Platform.docx,
  FR identifiers from SRS_Maduuka_Phase1_Draft.docx, Swift APIs
- OUT of scope: what is deferred

## Prerequisites
- Prior phases that must be complete
- External dependencies (GAP-001, GAP-004, etc.)

## Task List
1. [Task title — max 1 day] — acceptance criterion (deterministic pass/fail)
2. ...

## Test Gates
TC-xxx identifiers from TestPlan_Maduuka_Phase1.docx that must pass before phase closes:
- Unit: [specific Swift types and functions to test]
- UI: [XCUITest flows]
- Integration: [API endpoints exercised from iOS, expected JSON response per APISpec]

## Definition of Done Check
All items in DefinitionOfDone_Maduuka.docx satisfied? [ ] Yes — confirmed by reviewer.

## Skills Applied
- [skill-name] — how it governs this phase

## Open Gaps / Blockers
- [GAP-ID] — description and resolution owner
```

---

## Architecture Overview Document (00-ios-architecture-overview.md)

Generate this before any phase plan. It must cover:

1. **Project structure** — folder layout enforcing MVVM + Clean Architecture per `CodingGuidelines_Maduuka.docx`
2. **Core Data entity design** — how the 30+ tables in `DatabaseDesign_Maduuka.docx` map to Core Data entities, including EFRIS placeholder attributes
3. **Sync architecture** — Core Data ↔ REST API sync flow per `LLD_Maduuka.docx` `SyncService::processBatch()` design (text-based diagram)
4. **Network layer design** — URLSession wrapper, request building, JWT refresh interceptor per `LLD_Maduuka.docx` `AuthService`, certificate pinning, error mapping to domain errors using `TechnicalSpec_Maduuka.docx` error envelope
5. **RBAC enforcement pattern** — how role is stored (Keychain), how every SwiftUI view checks permissions per `LLD_Maduuka.docx` permission matrix, how API calls carry the role claim
6. **Offline queue design** — Core Data pending queue entity, sync replay logic, idempotency key strategy per `LLD_Maduuka.docx` `SyncService`, conflict resolution policy
7. **Module dependency graph** — which features depend on which (sync engine, auth, RBAC are shared; feature modules are independent per `modular-saas-architecture`)
8. **Phase 2/3 extension points** — how the architecture accommodates Restaurant (`SRS_Maduuka_Phase2a_Restaurant.docx`), Pharmacy (`SRS_Maduuka_Phase2b_Pharmacy.docx`), and EFRIS (`SRS_Maduuka_Phase3c_EFRIS.docx`) modules without refactoring Phase 1 foundations
9. **Testing strategy** — XCTest unit, XCUITest UI, mock URLSession for API tests; TC-xxx parity target from `TestPlan_Maduuka_Phase1.docx`

---

## Constraints

- Base every plan item on requirements in `SRS_Maduuka_iOS_Platform.docx` or `SRS_Maduuka_Phase1_Draft.docx`. Do not invent scope.
- Every phase has explicit test gates referencing TC-xxx identifiers from `TestPlan_Maduuka_Phase1.docx`. No phase closes without green tests. Apply `superpowers:test-driven-development` and `ios-tdd` throughout.
- The `DefinitionOfDone_Maduuka.docx` checklist applies to every task. No task is done without satisfying all criteria.
- Apply `ai-slop-prevention` — every task must be actionable by an iOS developer working independently without verbal clarification from the architect.
- Flag missing information with `[CONTEXT-GAP: <topic>]` rather than assuming.
- This plan covers ONLY the iOS app. The shared backend API is built by the web team. The iOS developer consumes the API — they do not modify it.
- Android is handled by a separate developer and a separate plan. iOS must not depend on Android-specific implementation details.
- This plan covers the TOTAL completion of Maduuka iOS: Phase 1 core parity (Phases 1–20), Phase 2 add-ons (Phases 21–23), and Phase 3 advanced modules (Phases 24–25). All 528 FRs across all SRS documents are in scope.
- All output goes to `docs/plans/maduuka-ios/` relative to the Maduuka project root.
- GAP-004 (iOS Bluetooth printer compatibility with Ugandan market printers: Epson, Xprinter, TP-Link) must be resolved with physical printer testing before Phase 9 closes.
- GAP-001 (MTN MoMo Business API sandbox credentials) must be resolved before Phase 16 closes. Phase 8 payment tasks are scaffolded but marked `[BLOCKED: GAP-001]`.
- GAP-005 (URA EFRIS API sandbox credentials) must be resolved before Phase 25 closes. Phase 25 EFRIS API tasks are marked `[BLOCKED: GAP-005]` until credentials are available.
