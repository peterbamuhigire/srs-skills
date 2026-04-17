# Proposed Solution — Academia Pro

**Version:** 1.0
**Date:** 2026-03-28

---

## 1. Platform Overview

Academia Pro is a multi-tenant SaaS school management platform. The architecture is Uganda-first, with country configuration profiles enabling expansion to Kenya, Tanzania, Nigeria, and Ghana in Phase 11 without code branching. A single shared codebase serves all tenants; tenant isolation is enforced at the data layer via `tenant_id` on every tenant-scoped table.

The system is designed around a single binding constraint (*Design Covenant*): automate every repeatable school process to the maximum degree, while remaining operable by a single administrator after module-specific training. This constraint drives every feature and UX decision.

**Technology summary:**
- Backend: PHP 8.2 / Laravel 11, MySQL 8.x, Redis 7, REST API (OpenAPI 3.1)
- Frontend: React 18 / TypeScript, shadcn/ui + Tailwind CSS, progressive web app (offline support)
- Mobile: Kotlin / Jetpack Compose (Android, Phase 1–8); Swift / SwiftUI (iOS, Phase 9–10)
- Infrastructure: VPS (early phases) → AWS ECS Fargate + S3 + CloudFront (Phase 8+)
- Communications: Africa's Talking (SMS), Meta Business Cloud API (WhatsApp), Firebase (push)

---

## 2. The 12-Phase Build Plan

### Phase 1 — Core Web Application (Standard Modules)

Delivers the full Uganda primary operational platform: all modules included in every subscription tier.

| Module | Scope |
|---|---|
| Student Information System (SIS) | Full lifecycle: admission, enrollment, transfers, alumni. 40+ fields including NIN, LIN, EMIS number, family contacts, medical summary. |
| Academics Setup | Academic years, 3-term calendar, classes/streams, subjects, timetables, curricula types (Thematic P1–P3, Standard P4–P7, O-Level, A-Level). |
| Fees Management + SchoolPay Integration | Term-based billing per class. SchoolPay webhook + polling reconciliation. Partial payments (KUPAA model). Auto-receipts. Arrears carry-forward. |
| Attendance | Daily class attendance (Present / Absent / Late / Excused). Auto-SMS alert on 3 consecutive absences. Monthly and termly reports. |
| Examinations + UNEB Grading Engine | Mark entry. Auto-computation: PLE (Div I–IV), UCE (D1–F9 aggregates), UACE (A–F principal + points), Thematic (HC/C/NYC). |
| Reports | Termly report cards per student. Head teacher comments. Class and school performance summaries. Bulk PDF generation (full class in one action). |
| RBAC | 11 standard roles; custom role configuration per school. Full permission matrix (HIGH-005). |
| Portal Scaffolds | Super Admin, School Owner, Student, Parent portals (basic Phase 1 versions). |

### Phase 2 — Optional Add-On Modules

Modules activated on demand (included in Growth and Pro tiers):

- Human Resources (HR): staff register, payroll, leave, disciplinary, appraisal
- Library Management: catalogue, borrowing/return, fines
- Transport Management: routes, student assignments, transport fee billing
- Hostel Management: room assignments, boarding fees, warden roster
- Communication (Communicate): bulk SMS, WhatsApp, in-app, email — by class/role/group
- Homework / Assignments, Download Centre, School Calendar, Certificates, Front CMS (school website)

### Phase 3–4 — Portals Complete + Full Test Suite

- Super Admin portal: tenant management, subscription billing, usage analytics
- Owner/Director portal: financial overview, staff management, school performance
- Android scaffold: Super Admin, Owner apps
- Phase 4 gate: 100% automated test suite passes before Phase 5

### Phase 5–6 — Student, Parent, Teacher, Driver Android Apps

- Student portal + app: timetable, results, fee balance, homework, downloads
- Parent portal + app: child results, attendance, fees, communication history
- Teacher Android app: attendance entry, mark entry, homework posting
- Bus Driver Android app: route view, student roll call, GPS check-in

### Phase 7 — Health Management Module

PDPO 2019 compliant student health records: medical history, clinic visits, prescriptions, sick bay. Access restricted to nurse/doctor role + parent. Emergency escalation. Special-category data classification.

### Phase 8 — Go-Live Preparation

- Final security audit (OWASP Top 10 zero critical/high findings)
- UNEB grading validation against UNEB-provided sample mark sheets
- EMIS export validated by MoES field officer
- SchoolPay merchant integration certified
- Android apps submitted to Google Play Store

### Phase 9–10 — Initial Trials + iOS Apps

- First 10–20 paying schools onboarded for live trials
- Full iOS suite (6 apps): Super Admin, Owner, Teacher, Student, Parent, Bus Driver
- KUPAA community payment agent pilot

### Phase 11 — Pan-Africa Expansion

- Kenya: NEMIS integration, M-Pesa Daraja API, KCSE/KCPE grading engine
- Tanzania: NECTA integration, Airtel/Tigo payment rails
- Nigeria/Ghana: WAEC engine, Flutterwave/Paystack
- Multi-campus management, USSD short code (Africa's Talking), direct MTN MoMo/Airtel Money (post-BoU licence), diaspora payment corridors

### Phase 12 — Maintenance + Support

SLA-backed support tiers, automated monitoring, scheduled EMIS reporting, continuous improvement.

---

## 3. Subscription Model

### 3.1 Tier Structure

| Tier | Pupil Range | Modules Included |
|---|---|---|
| **Starter** | 50–200 pupils | All Phase 1 standard modules |
| **Growth** | 201–500 pupils | All Phase 1 modules + all Phase 2 optional modules |
| **Pro** | 501+ pupils | All modules + priority support + custom branding + advanced analytics |

*Pricing detail in Section 06 (Financial Model).*

### 3.2 Billing

- Annual subscription billed monthly in UGX.
- Payment via SchoolPay (school pays via MTN MoMo, Airtel Money, bank) or Flutterwave (card, diaspora).
- No free tier. A 30-day trial period is offered at onboarding.
- Subscription lapses trigger a 90-day data grace period (data is retained, not deleted) — a direct competitive differentiator against ShuleKeeper's 60-day permanent deletion policy. After 90 days of non-payment, data is archived (not deleted) and the school is contacted by Chwezi support.

---

## 4. SchoolPay Integration Strategy

Academia Pro positions as the ERP layer on top of SchoolPay's payment rails — not a competitor.

- **Phase 1:** SchoolPay student payment codes are imported at onboarding. Payments made via any SchoolPay channel (MTN MoMo, Airtel Money, bank, agent) are automatically reconciled to the student's fee account within minutes via webhook, with a mandatory nightly polling fallback (SchoolPay webhooks have no retry mechanism).
- **Phase 3+:** Direct MTN MoMo and Airtel Money APIs added for schools that want ERP-native payment processing without SchoolPay. Requires BoU Payment Systems Operator licence.
- **Phase 4+:** Visa/Mastercard via Flutterwave for school subscription payments and diaspora parents.

The go-to-market message for SchoolPay-connected schools: *"Your parents already use SchoolPay. Academia Pro connects to it automatically. You gain a full school management system; your payment infrastructure stays exactly as it is."*

---

## 5. Compliance Architecture

| Obligation | Platform Response |
|---|---|
| Uganda PDPO 2019 | AES-256 at rest, TLS 1.3 in transit, 7-year record retention, data subject rights API, PDPO Office registration, Data Processing Agreements with each school |
| UNEB grading accuracy | 100% match against UNEB sample mark sheets (Phase 8 gate) |
| MoES EMIS | Bulk XML/CSV export validated against MoES data dictionary |
| UNEB exam registration | Candidate data export in UNEB-specified format |
| Uganda Copyright Act 2006 | Software registered with URSB before Phase 8 go-live |
| BoU payment licence | Phase 3–4 direct mobile money requires BoU PSO licence application |

---

## 6. Onboarding Design

A Uganda school must be operationally live — fee structures configured, student roll imported, SchoolPay codes mapped — within 30 minutes of signup. This is a hard product requirement (Design Covenant), not a marketing aspiration. The onboarding wizard drives the administrator through:

1. School profile (name, logo, MoES registration number, EMIS number)
2. Academic year and 3-term calendar configuration
3. Class and stream setup
4. Fee structure per class per term
5. Student import (Excel template or manual entry)
6. SchoolPay code mapping (bulk import via CSV)
7. User accounts for head teacher, bursars, and class teachers

Each step includes embedded video help (2–5 minutes per module). A school that completes all 7 steps has a fully operational system before the first fee collection cycle.
