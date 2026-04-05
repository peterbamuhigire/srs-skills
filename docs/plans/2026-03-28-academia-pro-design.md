# Academia Pro — Project Design Document

> **Chwezi Core Systems** | Owner: Peter | Date: 2026-03-28

## 1. Product Identity

**Product:** Academia Pro — multi-tenant SaaS school management platform, Uganda-first, pan-Africa expansion.
**Company:** Chwezi Core Systems (chwezicore.com)
**Team:** Solo / micro team (1–3 people)
**Methodology:** Hybrid (Water-Scrum-Fall) — formal requirements and phase gate sign-off before each phase begins; iterative delivery within phases.

## 2. Design Covenant (Binding Constraint)

> Automate every school process as much as possible, yet remain simple enough for a single administrator to operate — provided each user has watched the training videos for their assigned modules. Deep and rich in capability; easy and flexible in daily use. Standard modules ship with every subscription; optional modules are activated on demand.

**Hard requirements from this covenant:**
- Maximum automation by default: fee reminders fire automatically, attendance alerts send without manual trigger, reports generate at term-end unprompted
- Zero-config defaults: every Uganda school operational within 30 minutes of signup
- Role-scoped UX: a teacher never sees an accountant's screen; complexity hidden behind role boundaries
- Training-path architecture: each module ships with embedded video help; learned module-by-module
- Progressive disclosure: advanced settings exist but don't clutter daily workflow
- Single-admin survivability: if the IT person leaves, the head teacher can keep the system running

## 3. Competitive Positioning

### Primary Uganda Competitors

| Competitor | Threat Level | Key Gap to Exploit |
|---|---|---|
| **SchoolPay** | Critical — 15,000+ schools, 50%+ market share, BoU licensed | ERP launched Jan 2024 and immature; no EMIS; no UNEB; no offline; no unified parent portal |
| **ShuleKeeper** | High — Uganda market leader for school management | 60-day data deletion policy; no mobile app; no transport/hostel/library; password reset only via developer WhatsApp |
| **DesisPay** | Medium — direct challenger, free tier | Watch closely; limited depth |
| **Gandapps** | Medium — installable, SchoolPay integration | Not SaaS; no AI; no mobile app |
| **Akademikit** | Low-Medium — WordPress-based, 20 years old | WordPress cannot scale multi-tenant SaaS; no AI; no mobile |

### East Africa Competitors

| Competitor | Country | Threat | Gap |
|---|---|---|---|
| **Cloud School System** | Kenya | High | No offline; no EMIS; Kenya-only despite claims; no local language |
| **JibuERP** | Kenya | Low | Likely rebranded Indian ERP; Kenya-only |
| **ShulePro** | Kenya | Low | Desktop-only; no WhatsApp; no mobile money confirmed |

### 10 Universal Competitive Gaps (Academia Pro moat)

1. EMIS/government portal integration — no competitor connects to any national MoES/EMIS portal
2. Offline-first PWA + cloud sync — ShulePro offline but desktop-only; cloud players have no offline
3. Local language interfaces — no Swahili, Luganda, French, Hausa anywhere
4. Transparent self-serve pricing — all competitors require quote requests
5. Genuine pan-Africa localization — country profiles as data (curriculum, tax, payment, language)
6. KUPAA-style micro-payment model — no competitor supports UGX 1,000 partial payments
7. Community payment agents — unique KUPAA insight; unbuilt anywhere
8. School group/chain management layer — underdeveloped across all
9. Integrated copyright-compliant content licensing (Uganda Copyright Act 2006 obligations)
10. Single-admin survivability with training-path architecture

## 4. Payment Architecture Strategy

### Phase 1–2: Integrate WITH SchoolPay
- Use SchoolPay open API as primary payment backbone
- Schools keep SchoolPay payment rails; Academia Pro is the superior ERP layer
- No Bank of Uganda licence required for Phase 1–2
- Student payment code system operational from day 1

### Phase 3–4: Add Direct MoMo
- MTN MoMo API (parent-initiated, auto-reconcile)
- Airtel Money API
- Pursue BoU Payment Systems Operator licence

### Phase 4+: Expand Payment Ecosystem
- Diaspora/international corridor (Wise API or Flutterwave Global)
- USSD short code for fee balance + report card inquiry
- Visa/Mastercard card-not-present checkout

### Pan-Africa Payment Rails
- Kenya: M-Pesa Daraja API, Equity/KCB bank APIs
- Tanzania: Airtel/Tigo APIs
- Nigeria/Ghana: Flutterwave/Paystack

## 5. SRS Architecture (Approach C)

### Core SRS (1 document, 9 sections)
S1 Platform Vision | S2 Stakeholders & Personas | S3 System Architecture | S4 NFR | S5 Security & Compliance | S6 External Interfaces | S7 Data Architecture | S8 Localization Framework | S9 Subscription & Billing

### Module Cluster Specs (10 documents)
- MC-01: Identity & Access
- MC-02: Core Academic (Student info, UNEB grading, examinations, report cards)
- MC-03: Fees & Payments (SchoolPay, MoMo, micro-payments, agents)
- MC-04: Daily Operations (Attendance, front office, notice board, homework, calendar)
- MC-05: Staff & HR (Payroll, PAYE/NSSF, lesson plans, payroll-by-attendance)
- MC-06: Infrastructure (Library, transport, hostel, inventory, gate passes)
- MC-07: Reporting & Intelligence (EMIS/MoES, Claude AI analytics, DEO portal)
- MC-08: Governance & Protection (Multi-campus, SMC, child protection, auditor)
- MC-09: Extended Learning (Online exams, live classes, LMS, QR attendance, online admission)
- MC-10: Communications & Mobile (WhatsApp, SMS, Android app, certificates, alumni)

### Pan-Africa Expansion Annex (living document)
Country profiles: Kenya, Tanzania, Rwanda, Nigeria, Ghana, Francophone Africa

## 6. Product Surface — All Interfaces

### Web Portals

| Portal | User | Scope |
|---|---|---|
| Super Admin | Chwezi Core Systems (Peter) | Platform-wide: all schools, billing, support |
| Owner/Director | School owner / chain director | Their school(s): consolidated view, approvals |
| School Admin | Head teacher / administrator | Full school daily operations |
| Teacher | Subject & class teachers | Attendance, marks, homework, lesson plans |
| Accountant/Bursar | Finance staff | Fees, expenses, payroll, reports |
| Receptionist | Front desk | Enquiries, visitors, phone log |
| Librarian | Library staff | Catalogue, issue/return, fines |
| Student | Enrolled students | Results, timetable, homework, exams |
| Parent/Guardian | Parents and guardians | Fees, attendance, results, payment |
| DEO | District Education Officer | District aggregate monitoring |

### Android Apps (native Kotlin/Jetpack Compose)

| App | Phase Built | Phase Completed |
|---|---|---|
| Super Admin | Phase 3 | Phase 3 |
| Owner/Director | Phase 3 | Phase 6 |
| Student | Phase 5 | Phase 6 |
| Parent/Guardian | Phase 5 | Phase 6 |
| Teacher | Phase 6 | Phase 6 |
| School Bus Driver | Phase 6 | Phase 6 |

### iOS Apps (Swift/SwiftUI)
Phase 9 (start) → Phase 10 (complete) — mirrors every Android app.

## 7. 12-Phase Build Plan

### Phase 1 — Fully Functional Web App + Portal Scaffolds
**Goal:** First paying school. Full Starter tier. All core workflows operational.

**Web app — fully functional:**
- User roles & RBAC (all 9 built-in roles + super admin + owner)
- Student information (admission, 40+ fields, NIN, sibling linking, CSV import)
- Academics setup (sessions, classes, sections, subjects, timetable builder)
- Examinations & grading (UNEB PLE/UCE/UACE, thematic curriculum P1–P3, report cards, rank lists, admit cards)
- Attendance (student + staff, SMS alerts, term-aware summaries)
- Fees collection (structure, assign, collect, receipts, reminders, carry-forward, SchoolPay API integration)
- Front office (enquiry log, visitor book, phone log, postal)
- Notice board & communicate (notices, email/SMS log)
- Homework (assign, submit, evaluate)
- Download centre (syllabus, past UNEB papers)
- Certificates & ID cards (templates, bulk print, PDF export)
- Calendar & to-do (Uganda public holidays, 3-term template)
- Reports & analytics (enrollment, fees, attendance, exam, staff reports)
- Global student identity foundation (global_students, student_identifiers, school_enrollments schema)

**Portal scaffolds (basic but navigable):**
- Super admin: school list, creation, billing overview, platform stats
- Owner: school(s) list, enrollment + fees overview
- Student: profile, timetable, homework, results
- Parent: child fees balance, attendance, notices, SchoolPay payment

### Phase 2 — Extra Modules Ground Work
Each Growth-tier module functional end-to-end (not polished):
HR, Payroll basic, Library, Transport, Hostel/Boarding, Income & Expenses, Inventory, Lesson Plan, Behaviour Records, Alumni, Chat, Front CMS, Budget Management, Programs & Activities, Gate Passes, Multi-campus basic, Online Admission, EMIS data capture, AI analytics basic (Claude), MTN MoMo + Airtel recording, Micro-payments, Community payment agents.

### Phase 3 — Super Admin & Owner Portals Complete + Android Apps (Scaffold)
Super admin portal complete (tenant management, billing, platform analytics, support tickets, audit log). Owner/Director portal complete (multi-school dashboard, approval workflows, cross-school analytics). DEO portal basics. SMC governance. Child protection module. 2FA module. Super Admin Android app (scaffold). Owner Android app (scaffold).

### Phase 4 — All Extra Modules to Perfection + 100% Test Coverage
All Phase 2 modules polished to production quality. Full test suite: unit, integration, E2E, security, performance, accessibility. 100% passing gate before Phase 5.

### Phase 5 — Student & Parent Portals Complete + Their Android Apps (Basics)
Student portal complete (full academic profile, online exams, e-learning, health records view, AI insights, gate pass requests). Parent portal complete (multi-child, cross-school, full payment, AI summaries). Student Android app (basics). Parent Android app (basics).

### Phase 6 — Bus Driver App + Owner/Student/Teacher Apps Completed
Teacher Android app (new, complete). Owner Android app (completed from Phase 3 scaffold). Student Android app (completed). Parent Android app (completed). School Bus Driver Android app (GPS, pickup/dropoff, emergency alert, offline-capable).

### Phase 7 — Health Management Module
Student health profiles, sick bay log, prescription management, treatment tracking, vaccination records, medical referral log, school health officer portal, health analytics, cross-app access (student, parent, teacher, owner views). Encrypted, PDPO-compliant.

### Phase 8 — Go Live Preparation + Android App Launch
Security audit (OWASP Top 10), penetration testing, load testing (500 concurrent schools), Google Play submission for all 6 apps, BoU licence application initiated, privacy policy + ToS published, support system live, training videos published, monitoring live.

### Phase 9 — Initial Trials + iOS Development Starts
Onboard 5–10 trial Uganda schools (free first term). Collect feedback. iOS development starts for all 6 apps in parallel. Kenya market preparation (KCSE/CBC, M-Pesa, NHIF/NSSF/NITA, KES).

### Phase 10 — iOS Apps Completed
All 6 iOS apps to feature parity. App Store submission. TestFlight beta. iOS-specific UX (Face ID/Touch ID).

### Phase 11 — Full Integration + Scale
Kenya deployment (KCSE/CBC, M-Pesa). Tanzania deployment (NECTA, Airtel/Tigo). All add-on modules live (WhatsApp, online exams, live classes, LMS, QR attendance, USSD shortcode, diaspora payments). Reseller programme. 50+ paying schools.

### Phase 12 — Maintenance & Continuous Improvement
SLA per tier, security patches, annual PAYE/NSSF updates, curriculum updates, client success. Francophone Africa, Rwanda, Nigeria preparation.

## 8. Tech Stack

- **Backend:** PHP 8.2+ Service/Repository pattern, MySQL 8.x InnoDB
- **Frontend (web):** Tabler UI / Bootstrap 5, vanilla JS + Alpine.js
- **Android:** Kotlin, Jetpack Compose, Retrofit, Room (offline), WorkManager
- **iOS:** Swift, SwiftUI, URLSession, Core Data (offline), Background Tasks
- **Auth:** JWT (API) + session (web), bcrypt passwords
- **Payments:** SchoolPay API, MTN MoMo API, Airtel Money API, Flutterwave (pan-Africa)
- **SMS:** Africa's Talking Uganda
- **WhatsApp:** Meta Business API / Twilio fallback
- **AI:** Anthropic Claude API (claude-sonnet-4-6)
- **Email:** SMTP (configurable per tenant)
- **File storage:** Local + S3-compatible cloud storage
- **PDF:** mPDF (PHP)
- **Hosting:** Cloud VPS (DigitalOcean / AWS) + CDN

## 9. Legal & Compliance

- **Uganda Copyright Act 2006:** Register software with URSB. All developer contracts assign IP to Chwezi Core Systems. Student DB qualifies as protected electronic data bank — ToS must define data ownership between platform and subscribing school.
- **Bank of Uganda:** Payment Systems Operator licence required for Phase 3+ direct mobile money processing. Phase 1–2 uses SchoolPay API (no BoU licence needed).
- **NITA-U PDPO:** Personal data protection compliance. Health data encrypted at rest and in transit.
- **EMIS/MoES:** All EMIS-required fields captured at admission. EMIS returns generated with one click.
- **PAYE/NSSF/LST:** Auto-calculated per current URA tax tables, updated annually.
