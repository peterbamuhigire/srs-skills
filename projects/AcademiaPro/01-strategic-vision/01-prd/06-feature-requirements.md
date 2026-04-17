# Product Requirements Document — Academia Pro

## Feature Requirements

Requirements in this section follow IEEE 830 stimulus-response phrasing. Each requirement is uniquely identified and verifiable. Measurable thresholds replace all qualitative descriptors.

---

### FR-SIS: Student Information System

**FR-SIS-001:** When a school administrator submits a new student admission form, the system shall create a globally unique `student_uid` (UUID v4), store the student record with a minimum of 40 profile fields (including NIN, LIN, EMIS number, family contacts, medical summary, and passport photo), and return the new record with HTTP 200 within 500 ms at P95.

**FR-SIS-002:** When a school administrator searches for a student by NIN or LIN, the system shall perform a cross-school lookup in the `global_students` table and return any matching record regardless of the student's current enrolled school, within 500 ms at P95.

**FR-SIS-003:** When a student is enrolled at a second school using a matched NIN or LIN, the system shall copy the student's global identity fields (name, date of birth, gender) into the new enrolment in read-only mode; the enrolling school shall not be able to alter the global identity — only school-specific fields (local admission number, class, status) are writable.

**FR-SIS-004:** When a school attempts to enrol a student who already has an active enrolment at a different school on the same platform, the system shall reject the enrolment request with an error message identifying the conflict, and shall not create the duplicate enrolment record.

**FR-SIS-005:** When a student's status is changed to Transferred Out or Graduated, the system shall retain all historical records for that student in read-only mode, accessible to the originating school indefinitely.

---

### FR-ACA: Academics Setup

**FR-ACA-001:** When a school administrator creates an academic year, the system shall require exactly 3 term records per year with non-overlapping date ranges, and shall reject configurations with fewer or more than 3 terms.

**FR-ACA-002:** When a school selects a curriculum type for a class (Thematic P1–P3, Standard P4–P7, O-Level, A-Level), the system shall automatically apply the corresponding UNEB assessment schema to that class's examination records without requiring further configuration.

**FR-ACA-003:** When a school configures a timetable for a class, the system shall detect and reject period conflicts (same class, same time slot, different subject or teacher) before saving.

---

### FR-FEE: Fees Management

**FR-FEE-001:** When a school administrator defines a fee structure, the system shall accept separate fee amounts per class per term, with no restriction on the number of fee line items (tuition, boarding, transport, lunch, etc.) per structure.

**FR-FEE-002:** When a fee payment is received via the SchoolPay webhook, the system shall: verify the SHA256 signature; check for a duplicate `external_reference` using a UNIQUE constraint; write the payment record to `fee_payments` with channel, amount, receipt number, and SchoolPay transaction ID; return HTTP 200 within 200 ms; and queue receipt generation asynchronously. If the signature fails verification, the system shall return HTTP 200 with `{"status": "rejected", "reason": "invalid_signature"}` and log the event — it shall not return 4xx.

**FR-FEE-003:** When a duplicate SchoolPay webhook arrives (same `external_reference`), the system shall return HTTP 200 with `{"status": "duplicate", "original_receipt_id": "..."}` without creating a second payment record.

**FR-FEE-004:** When a payment is posted (by any channel), the system shall generate a sequentially numbered receipt, immutable and non-deletable, within 3,000 ms.

**FR-FEE-005:** When the nightly reconciliation job runs, the system shall call SchoolPay `SyncSchoolTransactions` for the current date and `SchoolRangeTransactions` for the preceding 3 days, compare results against `fee_payments`, and insert any unmatched transactions flagged as `source=poll_recovery` before 06:00 EAT.

**FR-FEE-006:** When a student's term fee balance is outstanding, the system shall send an automated SMS reminder to the primary parent/guardian contact on D-7 before term opening date, D-1 before term opening date, and D+7 after term opening date. Schools may disable D-1 and D+7 reminders; the D-7 default may not be disabled.

**FR-FEE-007:** When a bursar requests a refund, the system shall create a refund request record with Pending status and notify the School Owner/Director role. The refund shall not be executed until the School Owner/Director explicitly approves it. The bursar role shall not be able to approve a refund.

**FR-FEE-008:** When a payment is applied to a student account, the system shall apply funds in chronological order: oldest arrear balance first, then current term balance.

**FR-FEE-009:** When a school configures a pre-term payment discount (between 1% and 5%), the system shall apply the discount automatically to any full-term payment received before the term opening date and note the discount amount on the receipt.

---

### FR-ATT: Attendance

**FR-ATT-001:** When a class teacher submits attendance for their class, the system shall accept one status per student per school day (Present, Absent, Late, or Excused) and reject duplicate submissions for the same student, same date.

**FR-ATT-002:** When a student accumulates 3 consecutive Absent records, the system shall send an automated SMS alert to the primary parent/guardian within 5 minutes of the third absence being recorded.

**FR-ATT-003:** When a class teacher submits a correction to an attendance record that is within 48 hours of the original submission, the system shall accept the correction and log the amendment with user and timestamp. When the record is more than 48 hours old, the system shall reject the correction unless the requesting user holds the Head Teacher role or above, and shall log the amendment with user, timestamp, and mandatory reason field.

**FR-ATT-004:** When a monthly attendance report is requested for a class, the system shall generate a summary showing each student's total Present, Absent, Late, and Excused counts for the calendar month, exportable as PDF, within 3,000 ms.

---

### FR-EXM: Examinations and UNEB Grading Engine

**FR-EXM-001:** When a class teacher submits a mark, the system shall validate that the mark is ≥ 0 and ≤ the configured maximum mark for that exam. Marks outside this range shall be rejected at the API layer with a descriptive validation error before any database write.

**FR-EXM-002:** When mark entry for a UNEB examination class is submitted after the school's configured submission deadline, the system shall lock the mark entry screen and return an error. Only the Head Teacher role may unlock mark entry after the deadline; the unlock action shall be logged.

**FR-EXM-003:** When PLE marks are finalised for a P7 class, the system shall compute each student's aggregate as the sum of grades in the 4 compulsory subjects (English, Mathematics, Science, Social Studies and Religious Education), assign a Division (I: 4–12; II: 13–23; III: 24–29; IV: 30–34; Ungraded: 35–36), and store the computed aggregate and division. The computation shall match UNEB published rules with 100% accuracy as verified against UNEB sample mark sheets.

**FR-EXM-004:** When UCE O-Level marks are finalised, the system shall compute each subject grade on the 9-point scale (D1–F9), compute the aggregate across best 8 subjects per UNEB rules, and assign a Division (I: 7–34; II: 35–46; III: 47–58; IV: 59–70; Unclassified: >70).

**FR-EXM-005:** When UACE A-Level marks are finalised, the system shall compute principal subject grades (A–E, F), subsidiary grades (O, F), and assign points (A=6, B=5, C=4, D=3, E=2, O=1, F=0). The system shall compute university entry points on the best 3 principal subject grades.

**FR-EXM-006:** When Thematic Curriculum (P1–P3) marks are finalised, the system shall assign competency descriptors (Highly Competent, Competent, Not Yet Competent) per subject per student. No numeric aggregate is computed or displayed for these classes.

**FR-EXM-007:** When UNEB grade computation is triggered for 500 students, the system shall complete all computations within 5 seconds.

**FR-EXM-008:** When a school requests UNEB candidate registration data export, the system shall generate the export in UNEB-specified format (format to be confirmed with UNEB — see gap-analysis resource list) for all eligible candidates, within 30 seconds for a cohort of up to 500 students.

---

### FR-RPT: Report Card Generation

**FR-RPT-001:** When a head teacher triggers bulk report card generation for a class, the system shall generate individual PDF report cards for all students in the class, including computed grades, subject marks, class positions, attendance summary, and head teacher comments, within 120 seconds for a class of 200 students.

**FR-RPT-002:** When a report card is generated, the system shall include the school's logo, name, and address; the student's name, admission number, and class; all subject marks and grades; the UNEB aggregate and division (where applicable); the class position (ranked by aggregate); the term attendance summary; and a head teacher comment field.

**FR-RPT-003:** When a single student's report card is generated on demand, the system shall return the PDF within 3,000 ms.

**FR-RPT-004:** When a school-level performance summary is requested, the system shall generate a report showing class-by-class aggregate statistics (mean, median, top score, pass rate by division) exportable as PDF or CSV within 5,000 ms.

---

### FR-RBAC: Role-Based Access Control

**FR-RBAC-001:** When a user authenticates, the system shall issue a JWT containing the user's `tenant_id` and `role_id` claims. Every subsequent API request shall extract these claims and enforce the permission matrix for the requested resource before any data access.

**FR-RBAC-002:** When a school administrator attempts to assign a role to a user, the system shall reject the assignment if the target role has higher privilege than the requesting administrator's own role.

**FR-RBAC-003:** When a Super Admin accesses a tenant's data in read-only support mode, the system shall log the access with `super_admin_user_id`, `target_tenant_id`, timestamp, and access reason before returning any data.

**FR-RBAC-004:** When a user's session is inactive for 30 consecutive minutes (web) or the refresh token has exceeded 7 days (mobile), the system shall invalidate the session and require re-authentication.

---

### FR-EMIS: Government Integration

**FR-EMIS-001:** When a head teacher requests an EMIS export, the system shall assemble the required student headcount, teacher roster, and class statistics from existing records and produce a file in MoES-specified XML or CSV format without requiring any data re-entry, within 30 seconds for a school of up to 2,000 students.

---

### FR-HEALTH: Health Management (Phase 7)

**FR-HEALTH-001:** When a school nurse records a sick bay admission, the system shall create a visit record linked to the student's global UID, log the presenting complaint, and send an automated SMS notification to the student's primary parent/guardian within 5 minutes.

**FR-HEALTH-002:** When any user other than the assigned nurse/doctor role, the student, or the student's linked parent attempts to access an individual health record, the system shall deny access with HTTP 403. If the School Owner/Director requires emergency access, the system shall require an explicit reason, grant temporary read-only access, and log the user, timestamp, and reason.

**FR-HEALTH-003:** When a prescription is recorded for a student who has a documented allergy to the prescribed substance, the system shall display a prominent warning before allowing the prescription to be saved.

---

### FR-PAY-PANA: Pan-Africa Payment Rails (Phase 11)

**FR-PAY-PANA-001:** When a school's country profile is set to Kenya, the system shall route all payment collection through the configured M-Pesa Daraja API endpoint, display balances in KES, and apply the Kenya curriculum grading rules. No Uganda-specific payment or grading logic shall execute for a Kenya-profile school.

**FR-PAY-PANA-002:** When a country profile is added to the system, the system shall apply all grading, currency, payment gateway, and tax configurations from the `country_profiles` table without requiring a code deployment.

---

### FR-ELEARN: Class Library and E-Learning (Phase 2)

**FR-ELEARN-001:** When a teacher uploads a file to the class library, the system shall scan the file for malware before storing it. If scanning passes, the system shall store the file in Wasabi object storage under the school's quota, generate a CDN-backed download URL, and return HTTP 200 with the resource record within 10,000 ms for files up to 20 MB. If scanning fails, the system shall quarantine the file, notify the teacher via in-app alert, and return HTTP 422 with `{"error": {"code": "FILE_QUARANTINED"}}`.

**FR-ELEARN-002:** When a teacher links a YouTube or Vimeo URL as a study material, the system shall store the URL reference without fetching or caching the video content, verify the URL is syntactically valid (starts with `https://`), and confirm the resource record is created within 500 ms at P95. No storage quota is consumed by linked videos.

**FR-ELEARN-003:** When a teacher creates an assignment and publishes it to a class, the system shall send a push notification (FCM) to all enrolled students in the target class(es) within 5 minutes of publication. For students with push notifications disabled, the system shall send an SMS via Africa's Talking as a fallback if SMS is enabled for the school.

**FR-ELEARN-004:** When a student submits an assignment (typed text or file upload), the system shall record a server-side submission timestamp that is immutable and not alterable by the student. If the submission is received after the assignment due date, the system shall automatically set the submission status to Late. The system shall apply the configured late submission policy for that assignment (no penalty, percentage deduction, or reject) at the point of submission.

**FR-ELEARN-005:** When a teacher publishes marks for an assignment, the system shall automatically write each student's score to the subject marks register under the column corresponding to the assignment type (Homework, Classwork, CAT, Project, Practical), within 3,000 ms. No teacher action beyond clicking Publish is required to transfer marks to the gradebook. Students who did not submit shall be recorded as NSubmit (status code `not_submitted`) — distinct from a zero-mark entry.

**FR-ELEARN-006:** When the system evaluates two text submissions for the same assignment within the same class, and the similarity ratio (Jaccard token similarity or equivalent) between any two students' submissions exceeds 80%, the system shall flag both submissions with a plagiarism warning visible only to the teacher. The system shall not alter the submission, reduce the score, or notify the student automatically.

**FR-ELEARN-007:** When a student opens a quiz within its configured availability window, the system shall present questions in a randomised order unique to that student's session and shuffle the answer options for each MCQ question. The same student revisiting the same quiz attempt shall see the same order as their original session (order is seeded per student per quiz attempt). After the timer expires or the student submits, the quiz availability window shall remain open for other students who have not yet taken it.

**FR-ELEARN-008:** When a student's MCQ, True/False, or Numeric answer is submitted, the system shall compute the grade for those question types immediately and return the result within 1,000 ms. Short-answer questions shall remain in Pending status until the teacher grades them. When the teacher grades the final pending short-answer question in a quiz, the system shall auto-post the total quiz score to the gradebook.

**FR-ELEARN-009:** When a teacher's quiz timer reaches zero on a student's active session, the system shall automatically submit the student's current saved progress as the final submission. If the student has lost connectivity, the locally cached progress shall be submitted as soon as connectivity returns, and the submission shall be accepted as valid if the timer expired during the connectivity loss (not treated as late).

**FR-ELEARN-010:** When a Head Teacher requests the e-learning compliance report for a given week, the system shall return a report showing: for each teacher — number of study materials posted, number of assignments set, number of assignments with all submissions marked, average marking turnaround time in hours — within 5,000 ms.

**FR-ELEARN-011:** When a school's storage usage reaches 90% of its configured quota, the system shall send an in-app alert to the School Owner/Director. When usage reaches 100%, the system shall block new file uploads and notify the teacher attempting to upload with `{"error": {"code": "QUOTA_EXCEEDED"}}`. Existing files remain accessible and downloadable.


---

### FR-AI: AI Module — Intelligent School Management Add-On

> **Positioning:** The AI Module is a paid add-on sold separately from the core subscription. It is off by default. School owners activate it when they are ready to pay for the additional intelligence it provides. Every feature is described in terms that a non-technical school director or head teacher will understand immediately.

> **Pricing (indicative):** Starter — UGX 50,000/month; Growth — UGX 200,000/month; Enterprise — UGX 800,000/month. All plans include a configurable monthly token budget. The system enforces the budget and alerts the school owner at 80% consumption.

---

#### AI Feature 1: Know Which Students Are Falling Behind — Before It Is Too Late

**Who benefits:** Head Teachers and School Owners.

**The problem it solves:** A head teacher at a school of 500 students cannot personally track every student's attendance, marks, and engagement. Students often reach exam season already failing — and it is too late to help them.

**What it does:** Every Monday morning, the system automatically analyses each student's attendance pattern, marks, and activity. It presents the Head Teacher with a ranked list: "These 14 students are at high risk of failing this term. Here is why." The teacher can act immediately — make a phone call, send a note home, arrange extra lessons.

**Why school owners pay for it:** It protects the school's academic reputation and UNEB results. A school that consistently catches struggling students early and intervenes will have better division statistics — which drives enrolment.

**Pricing tier:** Starter and above.

**FR-AI-001** — see SRS Section 4, FR-AI-001 for full technical specification.

---

#### AI Feature 2: Write Report Card Comments in Seconds, Not Hours

**Who benefits:** Class Teachers and Head Teachers.

**The problem it solves:** At the end of every term, each class teacher writes 40 individual report card comments. This takes 2–3 hours and the comments are often generic. Parents can tell when a comment was written for everyone.

**What it does:** After marks are entered, the teacher clicks "Generate AI Comments." The system suggests a personalised 2–3 sentence comment for each student — mentioning their specific marks, attendance, and one thing they should work on. The teacher reviews each one, edits if needed, and approves. Only approved comments are saved.

**Why school owners pay for it:** Teachers save 2 hours per class per term. A school with 15 classes saves 30 teacher-hours every term — time that goes back to teaching. Parents notice the quality difference.

**Pricing tier:** Starter and above.

**FR-AI-002** — see SRS Section 4, FR-AI-002 for full technical specification.

---

#### AI Feature 3: The School Owner's Weekly Briefing in One Paragraph

**Who benefits:** School Owners and Directors.

**The problem it solves:** A school owner running multiple schools, or a busy director, cannot log into a management system every day and navigate dashboards to understand how the school is doing. They rely on verbal reports from staff that are often delayed or filtered.

**What it does:** Every Monday at 7am, the School Owner receives one paragraph in plain English: how attendance was last week, how fee collection is tracking, which class is performing best and which needs attention, and whether there are any student welfare alerts. No login required — it arrives as a notification.

**Why school owners pay for it:** The owner stays in control without being present. Board members can be copied on the briefing. It is the equivalent of a weekly management report, generated in seconds.

**Pricing tier:** Growth and above.

**FR-AI-003** — see SRS Section 4, FR-AI-003 for full technical specification.

---

#### AI Feature 4: Flag Parents Likely to Default on Fees Before the Term Starts

**Who benefits:** Bursars and School Owners.

**The problem it solves:** Schools lose significant revenue to fee defaults and delays. The bursar only finds out a parent is not going to pay when the term is half over and the student is still attending. By then, options are limited.

**What it does:** One week before term opens, the system analyses payment history for every student and flags parents who have a pattern of late payment or arrears. The Bursar gets a list: "These 23 families are likely to delay payment this term, based on the last 3 terms." The bursar can contact them early, agree on payment plans, and reduce mid-term disputes.

**Why school owners pay for it:** A school that recovers even 10% more of its outstanding fees pays for the entire AI module many times over.

**Pricing tier:** Growth and above.

**FR-AI-004** — see SRS Section 4, FR-AI-004 for full technical specification.

---

#### AI Feature 5: Understand What Parents Really Think Without Reading 200 Messages

**Who benefits:** School Owners and Head Teachers.

**The problem it solves:** Schools collect parent feedback but rarely analyse it systematically. Reading 200 survey responses is impractical. The result is that real concerns go unaddressed for a full term.

**What it does:** After each parent feedback round, the system reads every response — in English, Luganda, or Swahili — and produces a one-screen summary: "74% of parents are satisfied. The most common complaint is canteen food quality. The most common praise is the school's exam results. Recommended action: address the canteen." The owner sees themes, not individual messages.

**Why school owners pay for it:** Schools that listen and respond to parent feedback retain students and attract referrals. The AI makes listening systematic rather than occasional.

**Pricing tier:** Starter and above.

**FR-AI-005** — see SRS Section 4, FR-AI-005 for full technical specification.

---

### AI Module Packaging Summary

| Feature | Starter (UGX 50K/mo) | Growth (UGX 200K/mo) | Enterprise (UGX 800K/mo) |
|---|---|---|---|
| At-Risk Student Alert | Yes | Yes | Yes |
| Report Card Comments | Yes | Yes | Yes |
| Parent Sentiment Analysis | Yes | Yes | Yes |
| Weekly Owner Briefing | - | Yes | Yes |
| Fee Default Prediction | - | Yes | Yes |
| AI Executive Dashboard | - | - | Yes |
| Conversational Assistant | - | - | Yes |

**All features are off by default within the purchased plan.** The School Owner enables each feature individually from the AI Module settings screen. This allows schools to start with one or two features and expand as they become comfortable with AI-assisted management.
