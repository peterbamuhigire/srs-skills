# Product Requirements Document — Academia Pro

## Product Overview

### What Academia Pro Is

Academia Pro is a cloud-hosted, multi-tenant SaaS platform that manages the complete operational lifecycle of a K–12 school. It is not a learning management system (LMS), a content delivery platform, or an e-learning tool. It manages administration: who attends, what they owe, how they perform in examinations, and what statutory data the government requires.

The product serves three layers of user simultaneously:

1. *School staff* — administrators, head teachers, class teachers, bursars, librarians, hostel wardens, transport managers, and school nurses each receive a role-scoped view of exactly the functions they need.
2. *Students and parents* — read-only access to results, fee balances, attendance records, timetables, assignments, and health summaries via web portals and mobile applications.
3. *Chwezi Core Systems (operator)* — a Super Admin portal for tenant provisioning, subscription billing, usage analytics, and support access.

### Design Covenant

The binding constraint governing every design decision is: automate every school process as much as possible, yet remain simple enough for a single administrator to operate — provided each user has watched the training videos for their assigned modules.

This covenant produces the following mandatory design properties:

- *Maximum automation by default* — fee reminders fire automatically, attendance alerts send without manual trigger, report cards queue for bulk generation at term end, and EMIS exports are assembled from data already in the system. No workflow requires a manual trigger where automation is possible.
- *Zero-config defaults* — a Uganda school is fully operational within 30 minutes of signup. Default fee structures, grading rules, and calendar templates are pre-loaded for the Uganda context.
- *Role-scoped user experience* — a class teacher never sees an accountant's screen. Complexity is hidden behind role boundaries, not buried in preference menus.
- *Training-path architecture* — every module ships with embedded video help accessible from the interface. Users learn module by module; no single user needs to understand the entire system.
- *Progressive disclosure* — advanced configuration exists but does not appear in daily workflows unless the user navigates to it deliberately.
- *Single-admin survivability* — if the school's dedicated IT person leaves, the head teacher can continue operating the system using the same training videos.

### Core Architecture Properties

**Multi-tenancy:** Every school is an isolated tenant. Row-level isolation is enforced at the Repository layer by appending `WHERE tenant_id = ?` to every query using the authenticated user's `tenant_id` claim. No tenant may access another tenant's data under any circumstances.

**Global student identity:** Every student admitted to any Academia Pro school receives a globally unique `student_uid` (UUID) that persists across schools and across time. A student transferring from School A to School B retains the same UID. National Identification Numbers (NIN) and Learner Identification Numbers (LIN) are stored in a shared identity table with no `tenant_id`, accessible (read) by any authenticated school, writable only by the creating school.

**Progressive Web App (PWA):** The web frontend is built as a PWA with offline support via Workbox service workers. Attendance entry and mark entry function without an internet connection and synchronise on reconnect. This is essential for Uganda schools with intermittent connectivity.

**Mobile applications:** 6 native Android applications (Phases 1–8) and 6 native iOS applications (Phases 9–10) provide role-appropriate mobile access: Super Admin, School Owner/Director, Teacher, Student, Parent, and Bus Driver. Android is prioritised because the dominant smartphone category in Uganda is Android budget devices (Tecno, Samsung Galaxy A-series, Itel).

**Payment architecture:** Academia Pro is an ERP layer, not a payment processor. In Phases 1 and 2, all payments flow through SchoolPay's licensed infrastructure. Direct MTN MoMo and Airtel Money APIs (Phase 3) require a Bank of Uganda Payment Systems Operator licence. Card payments via Flutterwave (Phase 4) are PCI-DSS scoped entirely on Flutterwave's servers.

**AI-assisted analytics:** The Anthropic Claude API (claude-sonnet-4-6) powers predictive fee defaulter alerts, attendance pattern analysis, exam performance trend summaries, and natural-language commentary generation for report cards in later phases.

### Platform Modules at a Glance

The full module set spans Phase 1 through Phase 11. Standard modules ship with every subscription; optional (add-on) modules are activated per school on demand.

**Standard modules (Phase 1):**

- Student Information System (SIS)
- Academics Setup (year, terms, classes, subjects, curricula)
- Fees Management + SchoolPay Integration
- Attendance
- Examinations + UNEB Grading Engine
- Reports (termly and annual)
- Role-Based Access Control (RBAC)
- 4 portal scaffolds (Super Admin, Owner/Director, Student, Parent)

**Optional add-on modules (Phase 2+):**

- Human Resources and Payroll
- Library Management
- Transport Management
- Hostel Management
- Communication (SMS, WhatsApp, push, email)
- Homework and Assignments
- Download Centre
- School Calendar
- Certificates
- Front CMS (school website)
- Health Management (Phase 7 — PDPO special category)

**Integrations (Phases 1–11):**

- SchoolPay (Phase 1), MTN MoMo / Airtel Money (Phase 3), Flutterwave card (Phase 4)
- MoES EMIS export (Phase 1), UNEB exam registration export (Phase 1)
- Africa's Talking SMS, Meta WhatsApp Business API, Firebase Cloud Messaging
- Kenya NEMIS, M-Pesa Daraja, KCSE grading (Phase 11)
- Tanzania NECTA, Nigeria/Ghana WAEC, Flutterwave/Paystack (Phase 11)
- USSD short code via Africa's Talking (Phase 11)

### Technology Platform

The system is built on PHP 8.2+ / Laravel 11 (backend), React 18 / TypeScript / shadcn/ui (web frontend), Kotlin / Jetpack Compose (Android), and Swift / SwiftUI (iOS). The database is MySQL 8.x InnoDB with strict mode. Redis handles caching and job queuing via Laravel Horizon. Production infrastructure migrates from VPS to AWS ECS Fargate at Phase 8 to support auto-scaling for the exam-season load profile.

The full technology specification is documented in `_context/tech_stack.md`.
