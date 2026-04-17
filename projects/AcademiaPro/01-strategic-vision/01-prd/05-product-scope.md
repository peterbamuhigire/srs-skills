# Product Requirements Document — Academia Pro

## Product Scope

### In Scope

The following capabilities are within the defined scope of Academia Pro across all 12 phases. Items marked with their first available phase are not in Phase 1 scope but are committed product scope.

**School Administration**

- Student lifecycle management from application through admission, active enrolment, transfer, graduation, and alumni status (Phase 1)
- Global student identity across all Academia Pro schools using UUID, NIN, and LIN (Phase 1)
- Academic year and term configuration using the Uganda 3-term calendar model, configurable per school (Phase 1)
- Class, stream, subject, timetable, and curriculum type management (Phase 1)
- Staff register, payroll, leave management, and performance appraisal (Phase 2)

**Fees and Payments**

- Term-based fee billing in Uganda Shillings (UGX) per class, per term (Phase 1)
- SchoolPay integration: webhook reconciliation + nightly polling fallback + manual range pull (Phase 1)
- KUPAA micro-payment model: no minimum payment floor, partial payment carry-forward, community payment agents (Phase 2)
- Automated fee reminders via SMS at D-7, D-1, and D+7 relative to term opening date (Phase 1)
- Immutable, sequentially numbered receipts for every payment event (Phase 1)
- Double-payment prevention via unique external reference constraint and 5-minute deduplication window (Phase 1)
- Arrears carry-forward and display on current term invoice (Phase 1)
- Refund workflow: bursar initiates, School Owner/Director approves (Phase 1)
- Direct MTN MoMo and Airtel Money collection (Phase 3, pending BoU licence)
- Visa/Mastercard card payments via Flutterwave (Phase 4)
- Diaspora payment corridor via Wise or Flutterwave Global (Phase 4)
- Pre-term full-payment discount (1–5%, configurable per school) (Phase 2)

**Attendance**

- Daily per-student attendance with statuses: Present, Absent, Late, Excused (Phase 1)
- Automated SMS alert to primary parent/guardian after 3 consecutive Absent marks (Phase 1)
- Attendance entry via web portal and Teacher Android app with offline sync (Phase 1 web / Phase 6 app)
- Attendance correction audit trail: 48-hour self-correction window for class teacher; head teacher override with reason logging after 48 hours (Phase 1)
- Monthly and termly attendance summary reports (Phase 1)

**Examinations and Grading**

- Mark entry for internal examinations per class per subject (Phase 1)
- UNEB grading engine: PLE (4-subject aggregate, Divisions I–IV); UCE O-Level (9-point D1–F9, division aggregates); UACE A-Level (A–F principal, O subsidiary, points for university entry); Thematic Curriculum P1–P3 (Highly Competent / Competent / Not Yet Competent) (Phase 1)
- Mark validation: the system rejects any mark submission outside the configured maximum for that exam at the API layer (Phase 1)
- Mark entry lock for examination classes after the school's configured submission deadline (Phase 1)
- UNEB candidate registration data export in UNEB-specified format (Phase 1)
- Kenya KCSE grading engine (Phase 11)
- Nigeria/Ghana WAEC grading engine (Phase 11)

**Report Generation**

- Automated termly report cards per student, bulk-generated for an entire class in one action (Phase 1)
- Head teacher comments on report cards (Phase 1)
- Class-level and school-level performance summaries (Phase 1)
- PDF export for individual and bulk report cards (Phase 1)
- Annual academic progress reports (Phase 1)

**Government Integration**

- MoES EMIS bulk export in MoES-specified XML/CSV format (Phase 1)
- Kenya NEMIS API integration (Phase 11)
- Tanzania NECTA integration (Phase 11)
- Scheduled automated EMIS submission (Phase 12)

**Communication**

- SMS via Africa's Talking with Uganda local sender ID (Phase 1)
- Bulk SMS, WhatsApp via Meta Business Cloud API, in-app notifications, email (Phase 2)
- USSD short code for feature-phone parents: fee balance, last payment, report card term summary (Phase 11)

**User Access and Security**

- Role-Based Access Control (RBAC) with 11 standard roles and custom role configuration per school (Phase 1)
- Row-level multi-tenant isolation enforced at the Repository layer (Phase 1)
- Multi-factor authentication (TOTP) mandatory for Super Admin and School Owner/Director roles (Phase 1)
- Full audit log for every create/update/delete on student, fee, and health records (Phase 1)
- PDPO-compliant data export (JSON) and soft-delete pathway for right-of-access and right-to-erasure requests (Phase 1)
- AES-256 encryption at rest; TLS 1.3 in transit (Phase 1)

**Mobile Applications**

- Android: 6 native Kotlin/Jetpack Compose apps — Super Admin, Owner/Director, Teacher, Student, Parent, Bus Driver (Phases 3–6)
- iOS: 6 native Swift/SwiftUI apps — same 6 roles (Phases 9–10)
- Offline Room database + WorkManager background sync for Android (Phase 3+)

**E-Learning (Class Library and E-Learning — Module 21)**

- Class Library: teacher-uploaded study materials (PDFs, YouTube-linked videos, uploaded MP4 for restricted networks, audio recordings, PPTX, images, typed rich-text notes, external links) organised by subject, class, topic, and term (Phase 2)
- Student offline access: PDFs and audio files downloadable for offline reading; assignment text drafts offline and submits on reconnect (Phase 2)
- Assignments: full workflow — teacher creates with rubric, marks allocation, due date, and late submission policy → student submits via typed text, file upload (including phone camera photo of handwritten work), or audio recording → teacher marks in-app with written or audio feedback → marks auto-post to gradebook (Phase 2)
- Online quizzes: MCQ, True/False, Numeric (auto-graded), Short Answer (teacher-marked); question bank; per-student question randomisation; timer with auto-save; question-level analytics (Phase 2)
- Class announcements and structured Q&A: announcements with file attachments; student questions linked to a specific resource or assignment — not a general chat room (Phase 2)
- Head Teacher oversight: compliance view, assignment calendar, e-learning activity report per teacher (Phase 2)
- File storage: Wasabi S3-compatible object storage; per-school quota (5 GB / 20 GB / 100 GB); file deduplication; CDN delivery; virus scanning (Phase 2)
- BrightSoma API integration: link BrightSoma curriculum content into Academia Pro class libraries without duplication (Phase 3)

**Optional Add-On Modules**

- Library Management (Phase 2)
- Transport Management with Bus Driver app (Phase 2 + Phase 6)
- Hostel Management (Phase 2)
- Homework and Assignments (Phase 2)
- Download Centre (Phase 2)
- School Calendar (Phase 2)
- Certificates (Phase 2)
- Front CMS / school website (Phase 2)
- Health Management — PDPO special category, restricted access (Phase 7)

**Pan-Africa Expansion**

- Country profile architecture: `country_id`, `currency_code`, `payment_gateways[]`, `tax_rate`, `curriculum_type` as data-driven configuration (Phase 11)
- Kenya: NEMIS, M-Pesa Daraja, KCSE (Phase 11)
- Tanzania: NECTA, Airtel/Tigo mobile money (Phase 11)
- Nigeria/Ghana: WAEC, Flutterwave/Paystack (Phase 11)
- Multi-campus management layer (Phase 11)

**AI-Assisted Analytics**

- Predictive fee defaulter alerts (Phase 11)
- Attendance pattern analysis and anomaly flagging (Phase 11)
- Exam performance trend summaries (Phase 11)
- Natural-language report card commentary generation via Claude API (Phase 11)

### Out of Scope

The following are explicitly outside Academia Pro's scope:

- *External Learning Management System (LMS) standards:* SCORM packages, xAPI/Tin Can packages, IMS Common Cartridge, and third-party LMS curriculum sequencing are outside Academia Pro's scope. Module 21 (Class Library and E-Learning) is Academia Pro's own school-managed classroom layer — distinct from a standards-based LMS — covering teacher-created materials, assignments, quizzes, and announcements for in-school use. BrightSoma handles curriculum-aligned AI tutoring and cross-school content distribution; the two platforms integrate via API (Phase 3) and serve different purposes.
- *Payroll disbursement via mobile money:* Staff payroll calculation is within scope (Phase 2 HR module); actual disbursement to staff bank accounts or mobile wallets is not within scope for any phase. Payroll output is a report/export for the school's own bank.
- *Accounting / double-entry ledger:* Academia Pro manages school fees, receipts, and basic financial reporting. It is not a general-purpose accounting system. Integration with Xero or QuickBooks is a future consideration, not in scope.
- *GPS vehicle tracking:* The Transport module supports route and student assignment management. Real-time GPS tracking is flagged as optional (not committed scope) and requires third-party GPS hardware not provided by Academia Pro.
- *Tertiary / higher education:* The grading engine and academic structure are designed for K–12 and secondary. University or college management is not within scope.
- *Direct cardholder data storage:* All card payment processing is delegated to Flutterwave. No cardholder data is stored on Academia Pro servers.
- *Offline mobile payments:* The system requires connectivity to process or confirm any fee payment. Offline attendance and mark entry are supported; offline payment confirmation is not.

### Scope Boundaries by Phase

| Phase | Scope Boundary |
|---|---|
| Phase 1 | 7 standard web modules; 4 portal scaffolds; SchoolPay integration; UNEB grading; EMIS export; Africa's Talking SMS |
| Phase 2 | All optional add-on modules to initial production quality; Module 21 Class Library and E-Learning (Study Materials, Assignments, Quizzes, Announcements, Oversight, Offline Design, File Storage) |
| Phase 3 | Super Admin + Owner portals complete; Android app scaffolds; MTN MoMo + Airtel Money APIs |
| Phase 4 | All Phase 2 modules to production quality; full automated test suite at 100% pass; Flutterwave card payments |
| Phase 5 | Student + Parent portals complete; Student + Parent Android apps |
| Phase 6 | Teacher + Owner + Student Android apps complete; Bus Driver Android app |
| Phase 7 | Health Management module; PDPO special category compliance |
| Phase 8 | Security audit; UNEB grading validation; EMIS validation; SchoolPay certification; Google Play Store submission |
| Phase 9 | Live trials (10–20 schools); iOS development begins |
| Phase 10 | All 6 iOS apps complete; Apple App Store submission; KUPAA live pilot |
| Phase 11 | Kenya/Tanzania/Nigeria/Ghana; USSD; multi-campus; direct MoMo; diaspora payments; AI analytics |
| Phase 12 | SLA-backed support; automated monitoring; scheduled EMIS automation; continuous improvement |
