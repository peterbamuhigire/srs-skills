# Feature List — Academia Pro

All modules are grouped by build phase. Standard modules ship with every subscription; optional modules are activated on demand.

---

## Phase 1 — Core Web Application (Standard Modules)

### Student Information System (SIS)
Full student lifecycle management: admission, enrollment, transfers, graduated/alumni status. Stores 40+ fields including NIN (National Identification Number), LIN (Learner Identification Number), EMIS number, family contact details, medical summary, and passport photo. Global student identity architecture allows cross-school NIN/LIN lookup without duplicating records.

### Academics Setup
Define school structure: academic years, terms (Uganda 3-term calendar), classes/streams, subjects, timetables, and curricula types (thematic P1–P3, standard P4–P7, O-Level, A-Level).

### Fees Management
Term-based fee billing in Uganda Shillings. Fee structures per class, per term. Manual payment recording by the bursar (cash, bank transfer). Partial payment support (KUPAA micro-payment model — no minimum floor). Auto-generated sequential receipts. Fee balance tracking. Arrears carry-forward. Financial reports (collection summary, defaulters list, term reconciliation).

**Phase 2 addition:** SchoolPay API integration — student payment codes, automated payment sync, webhook reconciliation. See `_context/payment-landscape.md` for full integration spec.

### Attendance
Daily class attendance (present/absent/late/excused). Teacher submits via web or teacher app. Auto-alert to parent on N consecutive absences. Monthly and termly attendance reports.

### Examinations + UNEB Grading Engine
Mark entry for internal exams. Auto-computation of grades for all Uganda curriculum types:
- PLE (4-subject aggregate 4–16, Division I–IV)
- UCE O-Level (9-point D1–F9, aggregate divisions)
- UACE A-Level (A–F principal + subsidiary, points for university entry)
- Thematic Curriculum (P1–P3, competency descriptors)

### Reports (Termly + Annual)
Auto-generated termly report cards per student. Head teacher comments. Class-level performance summaries. School-level performance summaries. Export to PDF. Bulk generation (entire class in one action).

### User Roles + RBAC
Role-based access control. Standard roles: Super Admin (Chwezi), School Owner/Director, Head Teacher, Class Teacher, Accounts Bursar, Receptionist, Librarian, Transport Manager, Hostel Warden, Parent, Student. Custom roles configurable per school. Full permission matrix defined in `_context/gap-analysis.md` (HIGH-002).

### Portal Scaffolds (Phase 1 — basic)
- Super Admin portal (Chwezi staff — tenant management, billing, support)
- School Owner/Director portal (school-level dashboard)
- Student portal (view timetable, results, fee balance)
- Parent portal (view child's results, fees, attendance)

---

## Phase 2 — Extra Modules + SchoolPay Integration

### SchoolPay Integration
Connect the Phase 1 Fees module to SchoolPay's payment rails. Each student receives a SchoolPay payment code. Parents pay via MTN MoMo, Airtel Money, bank, or agent using that code. Academia Pro receives payment notifications via SchoolPay webhook and nightly reconciliation polling. Full integration spec in `_context/payment-landscape.md`. Requires SchoolPay merchant onboarding — approach SchoolPay after Phase 1 go-live.

### Human Resources (HR)
Staff register, payroll, leave management, disciplinary records, performance appraisal.

### Library Management
Book catalogue, borrowing/return records, fines, digital resource links.

### Transport Management
Bus routes, vehicle register, student bus assignments, GPS tracking (optional), fee billing for transport.

### Hostel Management
Dormitory room assignments, boarding fee billing, warden duty roster.

### Communication (Communicate)
Bulk SMS via Africa's Talking, WhatsApp via Meta Business API, in-app notifications, email. Send to parents, students, staff by class/role/group.

### Class Library and E-Learning (Module 21)

Full in-school e-learning suite covering six capabilities:

**Study Materials (§21.1):** Teachers upload PDFs (UNEB past papers, scanned notes — the most important format for Uganda schools), link YouTube or Vimeo videos (no storage cost; first choice), upload MP4 for YouTube-blocked networks, upload audio recordings (MP3/M4A — critical for language subjects), upload PPTX/images/diagrams, type rich-text notes, or post external links (Khan Academy, BBC Bitesize, UACE revision portals). Materials are organised by subject, class, topic, and term. Students filter by resource type and search by title. Teacher can pin up to 3 must-read resources per subject. Students download PDFs and audio for offline use. Teacher sees an access log showing who opened each resource and when — directly useful before exams. Parents see their child's subject library read-only.

**Assignments (§21.2):** Full four-stage workflow — teacher creates → students submit → teacher marks → marks auto-post to gradebook. Creation: title, instructions (rich-text with inline images and file attachments), marks allocation, due date, submission type (typed text / file upload / both / no submission required), optional rubric with per-criterion scoring, and per-assignment late submission policy (Accept / Accept with deduction / Reject). Submission: students type text (auto-saved every 30 seconds), upload up to 5 files per submission (photo from camera, gallery, or device storage, or audio recording), or work offline with auto-submit on reconnect. Marking: teacher reviews in-app (PDF viewer, full-screen photo, in-app audio); enters score per rubric criterion (total auto-calculates); adds written or audio feedback; publishes when ready or per individual student. Gradebook integration: marks auto-post to the correct column (Homework, Classwork, CAT, Project, Practical) on publish — no re-entry. Non-submitters recorded as NSubmit, not zero.

**Online Quizzes (§21.3):** Question types: MCQ, Multiple Select, True/False, Numeric answer (all auto-graded), and Short Answer (teacher-marked). Question bank builds over time per subject; questions are reused across quizzes. Per-student randomisation of question order and answer option order. Configurable timer with auto-submit on expiry; quiz progress saves every 30 seconds locally — timer does not reset on power cuts. Availability window enforced. Marks auto-post to gradebook on completion. Question-level analytics show which questions most students got wrong — informs re-teaching priorities.

**Class Announcements (§21.4):** Teacher posts text notices with optional file attachments; students receive push notifications. Pinned announcements for exam timetables and practical instructions. Head Teacher posts school-wide notices. Structured Q&A: students post questions linked to a specific resource or assignment only — not a general chat room. Teacher answers in-app; all class members see the answer.

**Oversight (§21.5):** Teacher assignment dashboard showing Unpublished / Open / Closed awaiting marking / Marked and published. Overdue-marking alerts after configurable threshold (default: 3 days). Resource usage stats. Head Teacher compliance view: which teachers posted materials this week, set assignments, completed marking — without accessing submission content. School-wide assignment calendar to identify overloaded weeks. E-learning activity report per teacher for staff appraisals.

**Offline Design (§21.6):** PDFs and audio files downloadable for offline reading. Assignment text drafts offline and auto-submits on reconnect. Quiz progress auto-saves locally every 30 seconds. Teacher operates entirely from the Android teacher app — no computer required. Boarding school scenario: Sunday posting, Sunday submissions — all marked on-time within the configured window.

**File Storage (§21.7):** Wasabi S3-compatible cloud storage (recommended for Africa-market cost control — $6/TB/month, no egress fees). Per-school quota: 5 GB Starter / 20 GB Growth / 100 GB Pro. File deduplication — one copy stored if two teachers upload the same file. CDN delivery for reduced latency on slow connections. Virus scanning on upload with quarantine. YouTube-first policy: teachers are encouraged to link YouTube rather than upload MP4 to save storage.

**Academic Integrity (§21.8):** Text submission plagiarism flag at 80% similarity threshold — flags to teacher, does not auto-penalise. Server-side submission timestamps (non-alterable). Question and answer randomisation in quizzes. Submission audit trail with all draft versions preserved.

**BrightSoma Integration (Phase 3):** Academia Pro handles in-school assignment and resource management. BrightSoma handles curriculum-aligned AI tutoring and multi-school content distribution. Integration via API: BrightSoma content can be linked from Academia Pro class libraries without duplication. BrightSoma content is referenced by URL — no copy stored on Academia Pro servers.

### School Calendar
Academic year calendar, events, exam schedule, public holidays. Shared across all roles.

### Certificates
Generate customisable certificates: completion, merit, participation. PDF export + bulk print.

### Front CMS (School Website)
Simple website builder: homepage, news/events feed, gallery, admission inquiry form.

---

## Phase 3 — Admin Portals Complete + Android Scaffold

- Super Admin portal: full tenant management, subscription billing, usage analytics
- Owner/Director portal: full school management dashboard, financial overview, staff management
- Android app scaffolds: Super Admin and Owner apps (basic navigation + auth)

---

## Phase 4 — Extra Modules Perfected + Full System Test

- All Phase 2 modules brought to production quality
- Full automated test suite run to 100% pass before Phase 5 begins

---

## Phase 5 — Student + Parent Portals Complete + Android Start

- Student portal: full access — timetable, results, fee balance, homework, downloads, calendar, health summary
- Parent portal: full access — child results, attendance, fees, communication history, health alerts
- Android apps started: Student app, Parent app (basic navigation + core features)

---

## Phase 6 — Driver App + Owner/Student/Teacher Apps Complete

- School Bus Driver Android app: route view, student roll call, GPS check-in
- Teacher Android app: attendance entry, mark entry, homework posting, communication
- Owner/Director Android app: complete
- Student Android app: complete

---

## Phase 7 — Health Management Module (New Module)

Student health record system. PDPO (Uganda Personal Data Protection Act 2019) compliant.
- Medical history, allergies, vaccinations
- Clinic visit log
- Prescription records (school nurse issues prescriptions; stored and viewable)
- Treatment records
- Sick bay admission and discharge
- Prescription/treatment accessible cross-app: Parent app, Student app, Owner app (medical summary only)
- Access control: health data visible to nurse/doctor role, student, and linked parent only
- Emergency contact escalation

---

## Phase 8 — Go-Live Preparation

- Final security audit
- UNEB grading validation against UNEB sample mark sheets
- EMIS report export validated by MoES officer
- SchoolPay merchant integration certified
- Android app submitted to Google Play Store

---

## Phase 9 — Initial Trials + iOS Start

- Onboard first 10–20 paying schools for live trials
- iOS app development begins: Super Admin, Owner, Teacher, Student, Parent, Bus Driver

---

## Phase 10 — iOS Apps Complete

- All 6 iOS apps complete and submitted to Apple App Store
- KUPAA micro-payment model live pilot with community payment agents

---

## Phase 11 — Full Integration + Scale

- Kenya: NEMIS integration, M-Pesa Daraja API, KCSE grading engine
- Tanzania: NECTA integration, Airtel/Tigo mobile money
- Nigeria/Ghana: WAEC grading engine, Flutterwave/Paystack
- Multi-campus management layer
- USSD short code for fee balance + report card inquiry
- Direct MTN MoMo + Airtel Money (post-BoU licence)
- Diaspora payment corridor (Wise or Flutterwave Global)

---

## Phase 12 — Maintenance + Support

- SLA-backed support tiers
- Automated monitoring and alerting
- Scheduled EMIS reporting automation
- Continuous feature improvement from school feedback
