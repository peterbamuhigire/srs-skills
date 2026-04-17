# Business Rules — Academia Pro

## Uganda Calendar Rules

- BR-CAL-001: The academic year is divided into exactly 3 terms (Term 1, Term 2, Term 3). Monthly billing is not supported. All fee structures, report cards, and attendance summaries are term-based.
- BR-CAL-002: Academic year boundaries are configured per school (schools set their own opening and closing dates within national guidelines). The system does not hardcode calendar dates.
- BR-CAL-003: PLE, UCE (O-Level), and UACE (A-Level) examinations occur in Term 3. The system shall lock mark entry for examination classes after the school's configured exam submission deadline.

## UNEB Grading Rules

- BR-UNEB-001: PLE aggregate is the sum of grades in 4 compulsory subjects (English, Mathematics, Science, Social Studies & Religious Education). Grade scale: 1 (Distinction) to 4 (Fail). Division I: 4–12, Division II: 13–23, Division III: 24–29, Division IV: 30–34, Ungraded: 35–36.
- BR-UNEB-002: UCE O-Level grades are on a 9-point scale: D1 (highest) to F9 (fail). Subject aggregate and division are computed per UNEB rules. Division I: aggregate 7–34, Division II: 35–46, Division III: 47–58, Division IV: 59–70, Unclassified: >70.
- BR-UNEB-003: UACE A-Level: principal passes graded A–E; F = fail. Subsidiary pass graded O. Points: A=6, B=5, C=4, D=3, E=2, O=1, F=0. University entry computed on best 3 principal subject points.
- BR-UNEB-004: Thematic Curriculum (P1–P3): competency-based assessment — no numeric grades. Descriptors: Highly Competent (HC), Competent (C), Not Yet Competent (NYC).
- BR-UNEB-005: The system shall not allow a teacher to submit marks that are outside the configured maximum mark for that exam. Attempted out-of-range submissions are rejected at the API layer with a descriptive validation error.

## Fee Rules

- BR-FEE-001: Fee structures are defined per class per term. One school may have different fee amounts for different class levels.
- BR-FEE-002: Partial payments are accepted with no minimum floor (KUPAA micro-payment model). The outstanding balance is carried forward to the next payment.
- BR-FEE-003: Arrears from a previous term are displayed on the current term invoice and must be cleared before or alongside current term fees. The system does not prevent enrollment due to arrears but flags the outstanding balance prominently.
- BR-FEE-004: A receipt is generated automatically on every payment recorded, whether via SchoolPay integration or manual cash entry by the bursar. Receipts are numbered sequentially per school and cannot be deleted.
- BR-FEE-005: Double-payment prevention — if the same payment code is submitted twice within a 5-minute window with the same amount, the second transaction is rejected with status DUPLICATE and the first receipt is returned. Full specification in `_context/gap-analysis.md` HIGH-006.
- BR-FEE-006: Fee reminders are sent automatically at D-7 before term opening date, D-1 before term opening date, and D+7 after term opening date (for unpaid balances). Schools can configure or disable reminders but cannot remove the D-7 default.
- BR-FEE-007: Refunds must be authorised by the School Owner/Director role. The bursar role may initiate a refund request but cannot approve it.

## Student Identity Rules

- BR-STU-001: Every student admitted to any Academia Pro school is assigned a globally unique `student_uid` (UUID). This UID persists across schools and across time — transferring to another school does not create a new UID.
- BR-STU-002: A student may have a NIN (National Identification Number for age 16+) or LIN (Learner Identification Number assigned by NEMIS/MoES). Both are stored in the `student_identifiers` table with source tagging. Either can be used for cross-school lookup.
- BR-STU-003: A student's global identity record (name, date of birth, gender) is controlled by the creating school. Subsequent schools enrolling the same student via NIN/LIN lookup may not alter the global identity — only the enrolling-school-specific fields (local admission number, class, status).
- BR-STU-004: A student cannot have two active enrollments at two different schools simultaneously. The system enforces single-school active enrollment at the global identity level.

## Attendance Rules

- BR-ATT-001: Attendance is recorded per student per school day. The valid statuses are: Present, Absent, Late, Excused.
- BR-ATT-002: If a student accumulates 3 consecutive Absent marks, an automated SMS alert is sent to the primary parent/guardian on file.
- BR-ATT-003: Attendance records for a past date may be corrected by the Class Teacher within 48 hours. After 48 hours, only the Head Teacher or above may amend an attendance record, and all amendments are logged with the amending user and reason.

## Multi-Tenancy Rules

- BR-MT-001: Every tenant-scoped table carries a `tenant_id` column. The Repository layer appends `WHERE tenant_id = ?` to every query using the authenticated user's `tenant_id` claim. No tenant may access another tenant's data under any circumstances.
- BR-MT-002: Global identity tables (`global_students`, `student_identifiers`) carry no `tenant_id`. Access is controlled at the service layer: any authenticated school may read global identity fields; only the owning school may write them.
- BR-MT-003: Super Admin users (Chwezi staff) may access any tenant's data in read-only mode for support purposes. All Super Admin cross-tenant reads are logged with the Super Admin user_id, target tenant_id, timestamp, and access reason.

## RBAC Rules

- BR-RBAC-001: Role assignment is per school per user. A user may hold different roles at different schools (e.g., a teacher at School A may be a parent at School B).
- BR-RBAC-002: No user may assign a role with higher privilege than their own current role.
- BR-RBAC-003: Full permission matrix to be completed before Phase 1 development begins — see `_context/gap-analysis.md` HIGH-005.

## Data Protection Rules (Uganda PDPO 2019)

- BR-DP-001: All student personal data is classified as sensitive personal data under the Uganda Data Protection and Privacy Act 2019. Processing requires a lawful basis (contractual necessity for enrolled students; parental consent for students under 18).
- BR-DP-002: A school administrator may export or delete a student's personal data on request (right of access / right to erasure). The system provides a GDPR/PDPO-style data export in JSON format and a soft-delete pathway.
- BR-DP-003: Health records (Phase 7) are classified as special category data. Access is restricted to the treating nurse/doctor role and the student's linked parent. No other role — including the School Owner — may access individual health records without an explicit emergency override, which is logged.
- BR-DP-004: All personal data is encrypted at rest (AES-256) and in transit (TLS 1.3). Full compliance specification in `_context/gap-analysis.md` HIGH-008.

## Promotion and Departure Rules

- BR-PROM-001: Class promotion is initiated via the Year-Start Promotion Wizard, which launches automatically when a new academic year is created. Term 1 of the new academic year cannot open until every class has a status of `promoted`, `departed`, or `skipped` in the wizard.
- BR-PROM-002: Each class has a configurable "Promotes To" destination class. Final-year classes (P7, S.4, S.6) have no destination (`promotes_to = null`), which the wizard treats as a departure event.
- BR-PROM-003: The wizard defaults to bulk-promoting all students in a class to the destination class. The Head Teacher may deselect individual students; deselected students are re-enrolled in the same class for the new year (repeating).
- BR-PROM-004: A student who is repeating receives a new `school_enrollments` record in the same class for the new academic year. Their previous year's records remain linked and read-only.
- BR-PROM-005: All marks, attendance, and payment records for a completed academic year are locked (immutable) by an automated scheduled job 30 days after the last term's configured end date. No manual trigger exists for this lock.
- BR-PROM-006: A `promotion_events` audit record is created for each wizard session, capturing: initiating user, academic year, tenant, timestamp, count of promoted/repeating/departed students.
- BR-PROM-007: The Skip option in the wizard is available only for classes with zero prior-year students (newly created classes). Skipping a class with active students requires Head Teacher confirmation and is logged.

## Departure Rules

- BR-DEPART-001: Every student departure — regardless of reason — creates a `school_departures` record with a reason code: `completed`, `transferred_platform`, `transferred_external`, `scholarship`, `expelled`, `withdrawn`, `deceased`, or `other`.
- BR-DEPART-002: A departed student's `global_students` record remains available for enrolment at any other school, with the following exception: students with `reason = deceased` have their global identity locked (`global_students.status = deceased`) and cannot be enrolled at any future school.
- BR-DEPART-003: When a student with a prior `expelled` departure is looked up via NIN/LIN, the system shows only a neutral notice ("This student has a prior enrolment record"). The departure reason is not exposed in the lookup result. The expelled reason is accessible only via the formal Inter-School Record Request workflow with student/parent consent.
- BR-DEPART-004: A departed student's records at the originating school are permanently read-only. No role at the originating school may alter marks, attendance, or fee records after the departure is confirmed.

## Cross-Tenant Student History Rules

- BR-HIST-001: A student may view their own records from all prior schools in the "My Academic History" tab of their current school's portal. This access is scoped exclusively to the student's own `student_uid` via the `withStudentSelfScope()` Service method and is never routed through the standard Repository.
- BR-HIST-002: Every cross-tenant student history read is written to the audit log with: `action = STUDENT_SELF_HISTORY_READ`, `student_uid`, `viewer_user_id`, `source_tenant_id`, `target_tenant_id`, `data_types_accessed`, `timestamp`.
- BR-HIST-003: Fee payment amounts from prior schools are not shown in the history tab. Only a fee clearance status (cleared / not cleared) is displayed. Outstanding balances at prior schools do not follow the student to the new school.
- BR-HIST-004: If a prior school's tenant is suspended or archived, the student's history records from that school remain accessible to the student. Student data survivability is not tied to the school's subscription status.

## Inter-School Record Sharing Rules

- BR-SHARE-001: Schools may only request items from the platform-defined canonical shareable items list: `academic_results`, `report_cards`, `attendance_summary`, `disciplinary_record`, `fee_clearance`, `transfer_letter`, `health_summary` (Phase 7).
- BR-SHARE-002: Every inter-school record request requires explicit, per-item consent from the student (or parent/guardian if the student is under 18) before the source school reviews the request. Inaction by the student within 7 days constitutes automatic denial — there is no silent approval.
- BR-SHARE-003: The `disciplinary_record` item requires a separate explicit consent checkbox with a plain-language warning to the student. It cannot be bundled with other items for a single consent click.
- BR-SHARE-004: The source school (School A) may approve only items that the student has already consented to share. School A cannot override a student denial.
- BR-SHARE-005: Approved records are made available to the requesting school (School B) for a time-limited access window of 7, 14, or 30 days, set by School A at approval time (not to exceed School B's requested duration). After expiry, portal access is revoked; downloaded copies are School B's responsibility.
- BR-SHARE-006: Every step of the record request workflow is immutably logged: request creation, student consent decisions (per item), School A approval decisions (per item), each portal access, each download, and expiry. This log is visible to the student, both schools, and the Super Admin.
- BR-SHARE-007: A student may view the full history of all record requests made about them in their portal at any time.

## In-Platform School Application Rules

- BR-APPLY-001: A student may submit applications only to schools listed in the Academia Pro platform directory. Applications to off-platform schools are out of scope.
- BR-APPLY-002: A student may have a maximum of 5 pending applications at any one time.
- BR-APPLY-003: An application does not share any student records automatically. Records are shared only if the student explicitly attaches them via the mini-record-request flow within the application form.
- BR-APPLY-004: Application records are retained for 2 years after creation, then purged by the scheduled data retention job.

## EMIS Integration Rules

- BR-EMIS-001: Every school on the AcademiaPro platform shall store its MoES EMIS Number. The EMIS Number is a unique institutional identifier assigned by the Ministry of Education and Sports. Schools without an EMIS Number may apply for one via https://emis.go.ug/.
- BR-EMIS-002: Every learner registered in AcademiaPro shall be assigned a Learner Identification Number (LIN) by the EMIS system upon successful EMIS upload. AcademiaPro shall store the LIN alongside the internal `student_uid` and allow search by LIN.
- BR-EMIS-003: The EMIS learner export shall produce 3 separate Excel workbooks matching the MoES EMIS bulk upload templates: (a) Ugandan Learners (identified by NIN), (b) Foreign Non-Refugee Learners (identified by Student Pass), (c) Refugee Learners (identified by Refugee ID). Each template uses distinct ID validation rules.
- BR-EMIS-004: NIN format for Ugandan citizens follows the NIRA standard (e.g., `CM748383480F83` — 14 alphanumeric characters). Student Pass format is `ST` followed by 7 digits (e.g., `ST1234567`). Refugee ID format is `RM1-` followed by 8 digits (e.g., `RM1-23456789`). The system shall validate ID formats before allowing EMIS export.
- BR-EMIS-005: The EMIS staff export shall produce separate Excel workbooks for Ugandan and Foreign staff, further split into Teaching Staff and Non-Teaching Staff. Teaching staff are categorised as Trained or Qualified. Staff on the Government Payroll must include their IPPS (Integrated Personnel and Payroll System) Number.
- BR-EMIS-006: Secondary schools shall store the UNEB Centre Number in institution configuration. This number is required for UNEB candidate registration and EMIS institution particulars.
- BR-EMIS-007: EMIS learner transfers use the LIN or NIN as the lookup key. AcademiaPro's transfer-out process (FR-SIS-004) shall record the LIN to enable the receiving school to complete the EMIS transfer on the MoES portal.
- BR-EMIS-008: EMIS requires a Learner Summary Form per academic year and term — a headcount of learners by class and gender. AcademiaPro shall auto-compute this from enrollment data and export it in the EMIS-required format.
- BR-EMIS-009: The EMIS promotion workflow requires two statuses per learner: Promotion Status (Promote / Repeat) and Reporting Status (Reported / Not Reported). AcademiaPro's Year-Start Promotion Wizard (BR-PROM-001) shall capture both statuses to enable EMIS synchronisation.

## E-Learning Rules

- BR-ELEARN-001: The late submission policy for an assignment is configurable per assignment: Accept late with no penalty / Accept with a percentage deduction per day (configurable rate) / Reject after deadline. The per-assignment policy takes precedence over any school-level default.
- BR-ELEARN-002: Text submissions are auto-saved as drafts every 30 seconds on the client. A submission is not recorded as submitted until the student explicitly submits. A teacher may return a submission for resubmission before the final mark is recorded; the prior version is retained in the audit trail.
- BR-ELEARN-003: When a teacher publishes marks for an assignment, scores shall post automatically to the subject marks register under the correct column (Homework, Classwork, CAT, Project, Practical) as configured in the assignment type. No manual re-entry is required.
- BR-ELEARN-004: Students who did not submit an assignment are recorded in the gradebook as NSubmit (Not Submitted). This status is distinct from a zero mark and is visible to the teacher and parent.
- BR-ELEARN-005: When the system detects that a student's text submission is more than 80% identical to another student's submission for the same assignment in the same class, the system shall flag the submission to the teacher with a plagiarism warning. The system does not auto-penalise; the teacher reviews and decides the appropriate action.
- BR-ELEARN-006: Quiz timer elapsed time is preserved through power cuts and connectivity loss — the client caches progress and elapsed time locally. The timer does not reset if the app re-opens during the same availability window.
- BR-ELEARN-007: For MCQ, True/False, and Numeric question types, grading is automatic upon student submission. Short-answer questions require manual teacher grading. Quiz marks auto-post to the gradebook once all questions in the quiz (including manually graded short-answer questions) have been graded.
- BR-ELEARN-008: Per-school file storage quotas apply: 5 GB (Starter), 20 GB (Growth), 100 GB (Pro). Files are stored in Wasabi S3-compatible object storage. The School Owner/Director may view current storage usage in the school settings panel.
- BR-ELEARN-009: All uploaded files are scanned for malware immediately on upload. A file that fails scanning is quarantined and the uploading teacher is notified. No download link is generated for a quarantined file.
- BR-ELEARN-010: BrightSoma content linked into Academia Pro class libraries via the BrightSoma API (Phase 3) is referenced by URL only — no file copy is stored on Academia Pro servers. If the BrightSoma API link becomes unavailable, the resource card shows a "Content unavailable" notice without removing the library entry.
