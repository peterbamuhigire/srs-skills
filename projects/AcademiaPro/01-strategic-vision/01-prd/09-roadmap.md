# Product Requirements Document — Academia Pro

## Product Roadmap

The roadmap is structured around 12 phases following the confirmed Hybrid (Water-Scrum-Fall) methodology: formal requirements sign-off and phase gate review before each phase; iterative development sprints within each phase. No phase begins development until all `_context/` files for that phase are reviewed and approved by Peter (Chwezi Core Systems).

Phase durations are indicative estimates. Actual start dates depend on phase gate completion and resource availability.

---

### Phase 1 — Core Web Application

*Standard modules: the minimum viable product for a Uganda school*

**Deliverables:**

- Student Information System (SIS): 40+ field student profile, global identity architecture, NIN/LIN cross-school lookup
- Academics Setup: 3-term Uganda calendar, classes, streams, subjects, timetable, curriculum types
- Fees Management + SchoolPay Integration: term-based billing in UGX, webhook reconciliation, nightly polling fallback, KUPAA partial payments, automated SMS reminders, immutable receipts, double-payment prevention
- Attendance: daily per-student status, automated 3-consecutive-absence SMS alert, 48-hour correction window
- Examinations + UNEB Grading Engine: PLE, UCE (O-Level), UACE (A-Level), Thematic P1–P3; mark validation; submission deadline lock
- Reports: bulk termly report card generation, PDF export, class and school-level performance summaries
- RBAC: 11 standard roles, custom role configuration, JWT-enforced permission matrix
- 4 portal scaffolds (web): Super Admin, School Owner/Director, Student, Parent
- MoES EMIS export (XML/CSV)
- Africa's Talking SMS integration

**Phase 1 Gate:**

- All modules pass 100% automated test suite.
- At least 1 pilot school completes a full term on the live system.
- SchoolPay reconciliation passes 7-day live transaction test with 0 unreconciled payments.
- UNEB grading engine validated against manually verified sample mark sheets.

---

### Phase 2 — Optional Add-On Modules + AI Module (Starter Tier)

*Expanding the platform for schools with deeper operational needs*

**Deliverables:**

- Human Resources: staff register, payroll computation, leave management, disciplinary records, performance appraisal
- Library Management: book catalogue, borrowing and return, overdue fines, digital resource links
- Transport Management: bus routes, student bus assignments, transport fee billing
- Hostel Management: dormitory room assignments, boarding fee billing, warden duty roster
- Communication (Communicate): bulk SMS, WhatsApp via Meta Business Cloud API, in-app notifications, email
- Class Library and E-Learning (Module 21): study materials (PDFs, YouTube-linked videos, uploaded MP4 for restricted networks, audio recordings, typed notes, external links) organised by subject, class, topic, and term; full assignment workflow with rubric-based marking, in-app feedback (written and audio), and auto-post to gradebook; online quizzes with auto-grading for MCQ/True/False/Numeric and question bank; class announcements with structured Q&A; Head Teacher e-learning compliance view and assignment calendar; Wasabi file storage with per-school quota, CDN delivery, and virus scanning; offline PDF/audio download and assignment draft sync
- School Calendar: events, exam schedule, public holidays, shared across all roles
- Certificates: customisable PDF certificates (completion, merit, participation)
- Front CMS: school website builder with homepage, news feed, gallery, admission inquiry form
- KUPAA community payment agent role: cash collection, restricted bursar variant
- Pre-term payment discount configuration
- **AI Module — Starter Tier (Phase 2 add-on):** At-risk student weekly alert, report card comment generator, parent feedback sentiment analysis. Sold as a paid subscription (UGX 50,000/month) on top of the core plan. Off by default; School Owner activates individual features. Token metering and budget enforcement built in from day one. See FR-AI-001 through FR-AI-007 for full specification.

---

### Phase 3 — Admin Portals Complete + Android Scaffold + Payment Expansion

*Full-featured admin portals and the first Android applications*

**Deliverables:**

- Super Admin portal: full tenant management, subscription billing, usage analytics, support cross-tenant read (logged), AI module activation and per-tenant token usage monitoring
- BrightSoma API integration: link BrightSoma curriculum content directly from Academia Pro class libraries without file duplication
- Owner/Director portal: full school management dashboard, financial overview, staff management, multi-school switching
- Android app scaffolds (Kotlin/Jetpack Compose): Super Admin app, Owner/Director app — navigation structure and authentication
- Direct MTN MoMo API integration (collection only — pending BoU PSO licence)
- Direct Airtel Money Uganda API integration (collection only — pending BoU licence)

---

### Phase 4 — Extra Modules Perfected + Full System Test + Card Payments

*Production quality across all modules before portal and app expansion begins*

**Deliverables:**

- All Phase 2 optional modules brought to production quality (not just functional — performance, edge cases, error handling)
- Full automated test suite: 100% pass rate across all Phase 1 and Phase 2 modules required before Phase 5 begins
- PHPStan level 8: zero errors in CI
- Flutterwave Visa/Mastercard card payments for school subscription billing and diaspora parent payments
- Diaspora payment corridor via Wise or Flutterwave Global (USD/GBP/EUR → UGX)

**Phase 4 Gate:** 100% test suite pass; PHPStan clean; no regressions against Phase 1 UNEB grading results.

---

### Phase 5 — Student + Parent Portals Complete + Android Start

*Students and parents get full digital access*

**Deliverables:**

- Student portal (web): timetable, results, fee balance, homework, downloads, calendar, health summary (Phase 7 health data visible here)
- Parent portal (web): child results, attendance history, fee balance, payment history, communication history, health alerts
- Android apps started: Student app, Parent app — core features (results, fee balance, attendance, homework)

---

### Phase 6 — Driver App + Teacher + Owner + Student Android Apps Complete

*Full Android mobile suite delivered*

**Deliverables:**

- Teacher Android app: attendance entry (offline-capable), mark entry, homework posting, communication
- Owner/Director Android app: complete (financial dashboard, multi-school switching, staff management, alerts)
- Student Android app: complete (timetable, results, fee balance, homework, downloads)
- Bus Driver Android app: route view, student roll call for boarding/alighting, GPS check-in (GPS tracking optional — depends on hardware)

---

### Phase 7 — Health Management Module

*PDPO-compliant student health records for boarding schools*

**Deliverables:**

- Medical history, allergies, vaccinations per student
- Clinic visit log with presenting complaint and treatment record
- Prescription records: drug, dose, issuing nurse, date
- Sick bay admission and discharge with automated parent SMS notification
- Allergy warning before prescription confirmation
- Access control: nurse/doctor role + linked parent + student only; emergency override logged
- Health data visible in Parent app (Phase 5), Student app (Phase 6), and Owner app (medical summary only — not individual records)
- Full PDPO 2019 special category data compliance

---

### Phase 8 — Go-Live Preparation

*Security hardening, government validation, and app store submission*

**Deliverables:**

- Third-party security penetration test: zero OWASP Top 10 critical or high findings
- UNEB grading engine validation against UNEB-provided sample mark sheets for PLE, UCE, and UACE cohorts
- MoES EMIS export format validation by MoES field officer
- SchoolPay merchant integration certified by SchoolPay operations team
- AWS ECS Fargate migration (auto-scaling for exam-season load profile)
- Android apps submitted to Google Play Store: all 6 apps reviewed and live
- Performance validation: all quality standards from `_context/quality_standards.md` met under load

**Phase 8 Gate:** All validation items above signed off. No unresolved critical or high security findings. Google Play Store approval confirmed.

---

### Phase 9 — Initial Trials + iOS Development Begins

*First paying schools; iOS parity starts*

**Deliverables:**

- Live trial programme: onboard 10–20 paying Uganda schools for structured live trials
- Structured feedback collection: per-module NPS, time-on-task measurements, support ticket analysis
- Onboarding flow validation: measure time-to-operational (target: ≤ 30 minutes from signup)
- iOS development begins: Swift/SwiftUI apps for Super Admin, Owner/Director, Teacher, Student, Parent, Bus Driver — authentication and core navigation

---

### Phase 10 — iOS Apps Complete + KUPAA Live Pilot

*iOS parity achieved; micro-payment model validated in market*

**Deliverables:**

- All 6 iOS apps complete and submitted to Apple App Store
- iOS feature parity with Android for all user roles
- KUPAA micro-payment live pilot: community payment agents active in at least 5 schools; no minimum floor enforced; chronological arrear application validated
- App Store and Google Play Store ratings tracked: target ≥ 4.0 / 5.0 across both platforms

---

### Phase 11 — Full Integration + Pan-Africa Scale

*Platform expands beyond Uganda*

**Deliverables:**

- Kenya: NEMIS API integration, M-Pesa Daraja API (collection + disbursement), KCSE grading engine
- Tanzania: NECTA integration, Airtel Tanzania + Tigo Pesa mobile money
- Nigeria / Ghana: WAEC grading engine, Flutterwave / Paystack payment rails
- Multi-campus management layer: school groups, cross-campus student transfers, consolidated financial reporting
- USSD short code (Africa's Talking, Uganda UCC-licensed): fee balance enquiry, last payment, report card term summary — for feature-phone parents
- Direct MTN MoMo + Airtel Money post-BoU licence (if not yet live in Phase 3)
- **AI Module — Growth Tier upgrade:** Weekly Owner Briefing and Fee Default Prediction features unlocked (UGX 200,000/month). Schools already on Starter Tier can upgrade to Growth without re-onboarding.
- **AI Module — Enterprise Tier:** AI Executive Dashboard (AI Insights panel on Owner dashboard, 4-zone analytics with AI Insights panel) and Conversational Assistant (in-app FAQ and policy chat for staff) (UGX 800,000/month).
- Language localisation: Luganda (Uganda), French, Swahili

**Phase 11 Gate:** Kenya NEMIS integration functional; M-Pesa live transaction test passes; at least 10 Kenya schools active.

---

### Phase 12 — Maintenance + Support (Ongoing)

*Sustainable platform operations*

**Deliverables:**

- SLA-backed support tiers (definition to be completed in `_context/sla.md`)
- Automated monitoring and alerting (Healthchecks.io, AWS CloudWatch, UptimeRobot)
- Scheduled EMIS submission automation: system submits EMIS data on configured schedule without manual trigger
- Continuous feature improvement driven by school feedback and support ticket analysis
- Annual security audit and penetration test renewal
- UNEB and MoES format compliance reviews before each exam and EMIS deadline season

---

### Roadmap Summary Timeline

| Phase | Focus | Key Milestone | AI Module |
|---|---|---|---|
| Phase 1 | Core web modules | Pilot school live | — |
| Phase 2 | Optional add-on modules + E-Learning | Full module catalogue live | Starter Tier available (UGX 50K/mo) |
| Phase 3 | Admin portals + Android scaffold + MoMo | Owner app on Play Store (scaffold) | Super Admin AI usage dashboard |
| Phase 4 | Full test suite + card payments | 100% test pass gate | AI module test suite complete |
| Phase 5 | Student + parent portals + Android start | Parent sees child's data on phone | — |
| Phase 6 | Full Android app suite | 6 Android apps on Play Store | — |
| Phase 7 | Health management | Boarding schools can adopt | — |
| Phase 8 | Security + validation + go-live prep | UNEB and EMIS certified; pentest clean | AI security pentest included |
| Phase 9 | Live trials + iOS start | 10–20 paying schools | Growth Tier available (UGX 200K/mo) |
| Phase 10 | iOS complete + KUPAA pilot | 6 iOS apps on App Store | — |
| Phase 11 | Pan-Africa + USSD | Kenya live; USSD active | Enterprise Tier available (UGX 800K/mo) |
| Phase 12 | Maintenance + SLA support | Ongoing | AI model and prompt updates ongoing |

### 500-School Growth Target Model

To reach 500 Uganda schools within 24 months of Phase 1 launch:

- Months 1–6 (Phase 9 trials): 10–20 schools — validation and feedback
- Months 7–12: 80 additional schools — onboarding programme, SchoolPay channel partnership
- Months 13–24: 400 additional schools — 33 new schools per month average, driven by referral from existing schools and UPSIA channel

This model assumes Phase 1 launches with a production-ready system validated in Phase 8, not a beta product. The quality gate at Phase 8 is what makes the growth trajectory credible.
