# Product Requirements Document — Academia Pro

## Target Users

Academia Pro serves distinct user groups across three layers: school operators, students and guardians, and the platform operator (Chwezi Core Systems). Each group has different access levels, different technology comfort profiles, and different definitions of value. The design covenant requires that every user's daily workflow be simpler and faster than the manual process it replaces.

### User Group Hierarchy

| User Group | Access Scope | Phase Available |
|---|---|---|
| Chwezi Super Admin | All tenants (read-only support); platform configuration | Phase 1 |
| School Owner / Director | All data within their school(s); multi-school view | Phase 1 |
| Head Teacher | Academic data; staff coordination; communication | Phase 1 |
| Class Teacher | Their class: attendance, marks, homework | Phase 1 |
| Accounts Bursar | Fee management; receipts; financial reports | Phase 1 |
| Receptionist | Student admission; inquiry management | Phase 1 |
| Librarian | Book catalogue; borrowing records | Phase 2 |
| Transport Manager | Routes; student assignments; transport fees | Phase 2 |
| Hostel Warden | Room assignments; boarding fees; duty roster | Phase 2 |
| School Nurse | Health records; prescriptions; sick bay | Phase 7 |
| Parent / Guardian | Their child's data: results, fees, attendance, health | Phase 1 (web) / Phase 5 (app) |
| Student | Their own data: timetable, results, fee balance | Phase 1 (web) / Phase 5 (app) |
| Community Payment Agent | Cash collection only; restricted bursar variant | Phase 2 |

### Primary Operator Personas

**Agnes Nakabugo — Accounts Bursar**

Agnes is 38, holds a diploma in Business Administration, and has worked at a boarding school in Kampala for 10 years. Her daily workflow involves Excel, paper receipts, and manual reconciliation of SchoolPay SMS notifications. Her primary pain points are: partial payment tracking lost in spreadsheets, double-entry errors for which she is held accountable, and manual WhatsApp messages to parents for balances.

Academia Pro replaces her entire workflow: fee structures are configured once per term; SchoolPay payments reconcile automatically via webhook and nightly polling; receipts are generated and numbered without manual action; SMS balance reminders fire on schedule without her typing a single number. The system produces the financial reports her owner needs in one click.

*Design requirement:* The fee recording and receipt workflow must be completable in ≤ 3 clicks from the point a payment notification arrives. Reconciliation must require zero manual data entry for SchoolPay-sourced transactions.

**John Ssemakula — Head Teacher / Deputy Head**

John is 52, a Bachelor of Education graduate with 25 years of teaching and 8 years as head teacher at a government-aided secondary school in Mukono. He collects paper mark sheets from 12 class teachers every exam season, re-checks calculations by hand, types results into Excel, and generates report cards one class at a time in Word. EMIS deadlines cause annual panic. He has low-medium technology comfort — uses email and WhatsApp but prefers large text and simple navigation.

Academia Pro eliminates every manual step in his exam cycle: marks are entered directly by class teachers; UNEB grades are computed automatically; report cards are generated for an entire class in one action; EMIS data is already in the system.

*Design requirement:* All exam-season workflows must be accessible from a single dashboard section labelled **Examinations**. EMIS export must require no data preparation — the system assembles the export from existing student and class records.

**David Okello — Class Teacher (Primary)**

David is 27, a Bachelor of Education graduate teaching P6 at a private school in Gulu. He owns a Samsung Galaxy A14 (Android 13). His pain points are: one shared computer in the school office requiring a physical trip to log attendance; paper attendance registers that no one reads; marks lost when the head teacher's hard drive failed.

Academia Pro gives David a mobile-first workflow: attendance entry from his phone in under 2 minutes before the first lesson; mark entry online without paper; homework posting visible to parents immediately.

*Design requirement:* The Teacher Android app attendance flow must require ≤ 5 taps to submit a full class register. The app must function in offline mode and sync when connectivity is restored.

**Grace Atuhaire — Parent / Guardian**

Grace is 34, a market trader in Mbarara with primary school education and 2 children at a nearby school. She owns a Tecno Android smartphone (Android 10, 2GB RAM). She travels 40 minutes to school for report cards and fee balance checks. She pays fees via MTN MoMo to a SchoolPay agent code but is uncertain whether the school receives the payment.

Academia Pro gives Grace instant visibility: fee payment confirmation via push notification and SMS; report card access from her phone; attendance alerts when her child is absent. She never needs to travel to school for information.

*Design requirement:* The Parent Android app must render all screens correctly on 360 × 800 px resolution with a minimum tap target of 44 × 44 dp. Critical information (fee balance, last payment confirmation, attendance status) must appear on the home screen without navigation. SMS fallback is mandatory for parents without smartphones.

**Patrick Byamukama — School Owner / Director**

Patrick is 45, holds an MBA, and owns 2 private schools in Masaka and Mbarara. He uses an iPhone 14 Pro and MacBook. He has no real-time visibility into his schools without calling head teachers; he receives different-format spreadsheets monthly; he suspects fee leakage but cannot audit it.

Academia Pro gives Patrick a real-time financial dashboard across both schools: fee collection rate, outstanding balances, staff attendance, and comparative performance metrics — all accessible from his phone. Every financial transaction has an immutable audit trail.

*Design requirement:* The Owner/Director portal must display a school-level financial summary (total fees billed, total collected, outstanding, collection rate %) refreshed within 5 minutes of any payment event. Multi-school owners must be able to switch between schools within ≤ 2 taps.

**Immaculate Nakato — School Nurse (Phase 7)**

Immaculate is 30, an Enrolled Nurse at a boarding secondary school. She keeps a paper-based sick bay register. Her pain points are: paper records inaccessible to the school office; parents not notified when a child is admitted; no allergy history check before issuing medication.

Academia Pro's Health Management module gives Immaculate a digital sick bay: visit log, prescription records, allergy and vaccination history, and automated parent notification on sick bay admission.

*Design requirement:* Health records must be accessible only to the nurse/doctor role, the student, and the student's linked parent. Access by any other role — including the School Owner — requires an explicit emergency override logged with user, reason, and timestamp. This is a hard constraint under PDPO 2019 special category data rules.

### Secondary Users

**Government — MoES / EMIS:** Passive stakeholder. Receives bulk EMIS-format exports. Academia Pro must produce output that passes MoES validation without manual reformatting. Communication is by export only.

**UNEB:** Passive stakeholder. Receives candidate registration data in UNEB-specified format. The UNEB grading engine must compute divisions and aggregates that match UNEB's published grade boundary tables exactly.

**SchoolPay:** Integration partner, not a user. Interactions are API-to-API. The business relationship is collaborative — SchoolPay benefits from a better ERP that drives more volume through their payment rails.

### Technology Access Profile

The product must serve users across a wide technology access gap:

| Access Profile | Users | Implication |
|---|---|---|
| Desktop web, broadband | School Owner, Head Teacher, Bursar | Full-featured web portal with dense information display |
| Mobile web / PWA, intermittent 3G | Class Teacher, Receptionist | Offline-capable PWA; lightweight pages ≤ 2,000 ms on simulated 3G |
| Android budget phone (2GB RAM, Android 10+) | Parent, Student, Class Teacher | Native Android app ≤ 44 MB APK; 360 × 800 px viewport; low memory footprint |
| Feature phone (no smartphone) | Rural parents | SMS alerts via Africa's Talking; USSD short code (Phase 11) |
| iPhone / high-end Android | School Owner | iOS app (Phase 10); full-feature parity with Android |
