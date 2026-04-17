---
title: "AcademiaPro — Frequently Asked Questions"
subtitle: "Phase 1 FAQ Reference"
standard: "ISO 26514"
version: "1.0"
date: "2026-04-03"
---

# AcademiaPro — Frequently Asked Questions

## Table of Contents

- [1. General Questions](#1-general-questions)
- [2. Installation and Setup](#2-installation-and-setup)
- [3. Student Information](#3-student-information)
- [4. Academics Setup](#4-academics-setup)
- [5. Fees Management](#5-fees-management)
- [6. Attendance](#6-attendance)
- [7. Examinations and UNEB Grading](#7-examinations-and-uneb-grading)
- [8. Reports](#8-reports)
- [9. User Roles and Permissions](#9-user-roles-and-permissions)
- [10. Account and Access](#10-account-and-access)
- [11. Troubleshooting](#11-troubleshooting)
- [12. Data and Security](#12-data-and-security)

---

## 1. General Questions

**What is AcademiaPro?**

AcademiaPro is a multi-tenant SaaS school management platform built for Ugandan primary and secondary schools. It automates student records, fee collection, attendance, examinations, UNEB grading, and report card generation. The platform is accessible via web portals and Android mobile apps.

**Who is AcademiaPro designed for?**

AcademiaPro serves School Owners/Directors, Head Teachers, Class Teachers, Bursars, Secretaries, Students, and Parents. Each user accesses a role-scoped portal that shows only the features relevant to their responsibilities. See the *User Manual*, Section 2 for a full role description.

**What problem does AcademiaPro solve?**

Schools spend hundreds of hours per term on manual administration — paper receipts, handwritten registers, Excel mark sheets, and individually typed report cards. AcademiaPro eliminates these manual processes while remaining simple enough for a single administrator to operate after watching module training videos.

**What are the system requirements?**

- **Web:** Any modern browser (Chrome, Firefox, Edge, Safari) with an internet connection
- **Android app:** Android 8.0 (API 26) or later, minimum 2 GB RAM
- **iOS app:** Available from Phase 9 onwards (Swift/SwiftUI)
- **Internet:** A stable connection is required for initial data sync; the Android app supports offline attendance and mark entry with automatic background sync

**How do I get started?**

Visit the AcademiaPro registration page, create a school account, and complete the initial setup wizard. The wizard guides you through school profile, academic year, term dates, classes, and your first user accounts. A Uganda school is operational within 30 minutes of signup. See [2. Installation and Setup](#2-installation-and-setup) for details.

**What is the pricing model?**

AcademiaPro uses a subscription model billed per school per term. Pricing tiers are based on student enrolment count. Contact Chwezi Core Systems (chwezicore.com) for current pricing. All fees are in Uganda Shillings (UGX).

**What languages does AcademiaPro support?**

The platform launches in English (East African British English). Support for Luganda and Kiswahili interface translations is planned for later phases.

---

## 2. Installation and Setup

**How do I sign up for AcademiaPro?**

Navigate to the AcademiaPro registration page and complete the sign-up form with your school name, contact details, and administrator credentials. You will receive a confirmation email with a link to activate your account. Once activated, you are directed to the setup wizard. See the *User Manual*, Section 3 for the full onboarding walkthrough.

**How do I configure my school after signing up?**

The first-time setup wizard walks you through 5 steps: school profile (name, motto, logo, EMIS number), academic year and term dates, class and stream structure, fee structures, and initial user accounts. You can revisit any of these settings later from the **Settings** menu.

**How do I set up academic years and terms?**

Navigate to **Settings > Academic Year**. Create a new academic year (e.g., 2026), then define 3 terms with their opening and closing dates. AcademiaPro enforces the Uganda 3-term calendar — monthly billing is not supported. See the *User Manual*, Section 4.1 for step-by-step instructions.

**How do I create classes for the first time?**

Go to **Academics > Classes** and select **Add Class**. Enter the class name (e.g., P4, S1), assign streams if applicable (e.g., East, West), and link the class to its curriculum type (Thematic for P1-P3, Standard for P4-P7, O-Level, or A-Level). The system requires at least one class before students can be admitted.

---

## 3. Student Information

**How do I admit a new student?**

Navigate to **Students > Admit Student**. Enter the student's personal details (name, date of birth, gender, parent/guardian contacts). The system assigns a globally unique student UID automatically. If the student has a NIN or LIN, enter it during admission to link to their national identity record. See the *User Manual*, Section 5.1.

**How do I transfer a student to another school on AcademiaPro?**

Go to **Students > Transfer Out**, select the student, and enter the destination school's AcademiaPro code. The receiving school accepts the transfer via **Students > Transfer In**. The student's global identity and historical records follow them automatically — no duplicate record is created. A student cannot hold active enrolments at two schools simultaneously.

**How do I search for a student?**

Use the global search bar at the top of any page. You can search by student name, admission number, student UID, NIN, or LIN. Results appear in real time as you type. The search is powered by Meilisearch for fast, typo-tolerant results.

**How does NIN/LIN lookup work?**

When admitting a student, enter their NIN (for students aged 16+) or LIN in the identity fields. The system queries the global student identity register to check whether this student already exists in AcademiaPro. If found, their core identity (name, date of birth, gender) is pre-filled and cannot be altered by the enrolling school — only the creating school controls global identity fields.

---

## 4. Academics Setup

**How do I configure the academic year structure?**

Navigate to **Settings > Academic Year**, create the year, and define 3 terms with their start and end dates. Each school sets its own dates within the national guidelines. All fee billing, attendance summaries, and report cards are tied to these term boundaries.

**How do I create classes and streams?**

Go to **Academics > Classes > Add Class**. Enter the class level, assign one or more streams, and link the class to its curriculum type. Supported curriculum types are: Thematic (P1-P3), Standard Primary (P4-P7), O-Level (S1-S4), and A-Level (S5-S6). See the *User Manual*, Section 4.2.

**How does timetable management work?**

Navigate to **Academics > Timetable**. Select a class and term, then assign subjects to time slots across the week. The timetable is visible to teachers on the Teacher portal and to students on the Student portal. Clash detection prevents the same teacher from being assigned to overlapping slots.

**What curriculum types does AcademiaPro support?**

AcademiaPro supports all 4 Uganda curriculum levels: Thematic Curriculum for P1-P3 (competency-based descriptors: Highly Competent, Competent, Not Yet Competent), Standard Primary for P4-P7, O-Level for S1-S4 (9-point grading scale D1-F9), and A-Level for S5-S6 (principal grades A-E, subsidiary grade O).

---

## 5. Fees Management

**How do I define a fee structure?**

Navigate to **Fees > Fee Structures**. Select the academic year, term, and class. Enter the fee amount in UGX and any applicable fee items (tuition, boarding, lunch, transport). Each class level can have a different fee structure per term. See the *User Manual*, Section 6.1.

**How do I record a payment?**

Go to **Fees > Record Payment**. Search for the student, select the term, enter the amount paid and the payment method (cash or bank transfer). AcademiaPro accepts partial payments with no minimum floor (KUPAA micro-payment model). A sequential receipt is generated automatically upon saving.

**How do I print or share a receipt?**

After recording a payment, the receipt appears on screen with a **Print** and **Share** button. You can also retrieve any past receipt from **Fees > Receipts** by searching the student name or receipt number. Receipts are immutable and cannot be deleted after generation.

**How do refunds work?**

The Bursar initiates a refund request from **Fees > Refunds > Request Refund**. The request must be approved by a user with the School Owner/Director role before it is processed. The Bursar role cannot approve their own refund request. See the *User Manual*, Section 6.4.

**How do fee reminders work?**

AcademiaPro sends automatic SMS reminders to parents with outstanding balances at 3 intervals: 7 days before term opens, 1 day before term opens, and 7 days after term opens. Schools can adjust or disable reminders from **Settings > Notifications**, but the 7-day pre-term reminder is enabled by default.

**What fee reports are available?**

Available reports include: collection summary per class per term, defaulters list (students with outstanding balances), term reconciliation report, and payment method breakdown. All reports can be exported to PDF. Navigate to **Fees > Reports** to generate them.

---

## 6. Attendance

**How do I record daily attendance?**

Class Teachers record attendance from **Attendance > Daily Entry** on the web portal or the Teacher Android app. Select the class, date, and mark each student as Present, Absent, Late, or Excused. Attendance can be submitted in under 2 minutes on the mobile app. See the *User Manual*, Section 7.1.

**What happens when a student is absent for multiple consecutive days?**

When a student accumulates 3 consecutive Absent marks, the system automatically sends an SMS alert to the primary parent/guardian on file. No manual intervention is required from the teacher. The alert includes the student's name and the number of consecutive absences.

**Can I correct a past attendance record?**

The Class Teacher can amend attendance for a past date within 48 hours. After 48 hours, only the Head Teacher or a higher role can make corrections. All amendments are logged with the amending user's name, the timestamp, and the reason for the change.

**What attendance reports are available?**

AcademiaPro provides monthly and termly attendance summaries per student, per class, and per school. Reports show attendance rate percentages and highlight students below a configurable attendance threshold. Navigate to **Attendance > Reports** to generate them.

---

## 7. Examinations and UNEB Grading

**How do I enter exam marks?**

Navigate to **Examinations > Mark Entry**, select the class, subject, and exam type. Enter marks for each student. The system rejects any mark that exceeds the configured maximum for that exam — out-of-range values are blocked at submission with a descriptive error message.

**How does UNEB grading work for PLE?**

PLE grading computes an aggregate from 4 compulsory subjects (English, Mathematics, Science, Social Studies and Religious Education). Each subject is graded 1 (Distinction) to 4 (Fail). The aggregate (range 4-36) determines the division: Division I (4-12), Division II (13-23), Division III (24-29), Division IV (30-34), Ungraded (35-36). AcademiaPro computes this automatically.

**How does UNEB grading work for UCE (O-Level)?**

UCE uses a 9-point scale from D1 (highest) to F9 (fail). The system computes subject aggregates and assigns divisions: Division I (aggregate 7-34), Division II (35-46), Division III (47-58), Division IV (59-70), Unclassified (above 70). All computations follow published UNEB rules with zero manual calculation required.

**How does UNEB grading work for UACE (A-Level)?**

UACE grades principal subjects A through E (F = fail) and subsidiary subjects as O (subsidiary pass) or F. Points are: A=6, B=5, C=4, D=3, E=2, O=1, F=0. University entry points are computed from the best 3 principal subjects. The system handles this automatically.

**How does Thematic Curriculum assessment work?**

For P1-P3 classes, AcademiaPro uses competency-based descriptors instead of numeric grades. The 3 descriptors are: Highly Competent (HC), Competent (C), and Not Yet Competent (NYC). Teachers select the appropriate descriptor per learning area per student.

**Is there a mark entry deadline?**

Yes. The Head Teacher or administrator configures an exam submission deadline per exam type. After the deadline, mark entry is locked and no further changes are accepted. For national examination classes (PLE, UCE, UACE), mark entry locks automatically after the school's configured Term 3 exam deadline.

**Can I export UNEB registration data?**

Navigate to **Examinations > UNEB Export**. The system generates a file in the format required by UNEB for candidate registration. Review the data before submission. This feature eliminates manual re-entry of student details into UNEB's registration portal.

---

## 8. Reports

**How do I generate a single student's report card?**

Navigate to **Reports > Report Cards**, select the class and term, then choose the student. Click **Generate**. The report card includes subject marks, grades, aggregates, division (where applicable), class position, teacher comments, and head teacher comments. See the *User Manual*, Section 8.1.

**Can I generate report cards for an entire class at once?**

Yes. Go to **Reports > Report Cards**, select the class and term, then click **Generate All**. The system produces report cards for every student in the class in a single bulk action. Bulk generation runs as a background job — you receive a notification when the batch is ready for download.

**What performance summaries are available?**

AcademiaPro provides class-level performance summaries (grade distribution, mean scores, pass rates) and school-level performance summaries (cross-class comparison, subject analysis, term-over-term trends). Navigate to **Reports > Performance** to access them.

**Can I export reports to PDF?**

Yes. Every report card and performance summary includes a **Download PDF** button. Bulk-generated report cards are packaged as a single PDF file with page breaks between students. PDF exports use the school's configured letterhead and branding.

---

## 9. User Roles and Permissions

**What roles are available in AcademiaPro?**

Standard roles include: Super Admin (Chwezi staff), School Owner/Director, Head Teacher, Class Teacher, Accounts Bursar, Receptionist, Librarian, Transport Manager, Hostel Warden, Parent, and Student. Each role sees only the portal screens and features relevant to their responsibilities.

**Can I create custom roles?**

Yes. Navigate to **Settings > Roles > Create Role**. Define a role name and select the specific permissions to assign. Custom roles allow schools to tailor access control to their organisational structure. A user cannot assign a role with higher privileges than their own.

**How do I assign permissions to a user?**

Go to **Settings > Users**, select the user, and assign one or more roles. Permissions are inherited from the assigned role. A single user can hold different roles at different schools — for example, a teacher at one school and a parent at another. See the *User Manual*, Section 9.2.

---

## 10. Account and Access

**How do I log in?**

Open the AcademiaPro web portal or Android app and enter your registered email address and password. Teachers, Students, and Parents each have their own portal URL or app. Your dashboard displays only the features permitted by your assigned role.

**How do I reset my password?**

Click **Forgot Password** on the login screen. Enter your registered email address and the system sends a password reset link. The link expires after 60 minutes. If you do not receive the email, check your spam folder or contact your school administrator.

**Is multi-factor authentication (MFA) available?**

MFA is mandatory for Super Admin accounts (Chwezi staff) and optional for School Owner/Director accounts. MFA uses a time-based one-time password (TOTP) via an authenticator app. School-level users (teachers, bursars) do not require MFA in Phase 1.

**What dashboards do different roles see?**

Each role has a tailored dashboard. The School Owner sees fee collection totals, attendance rates, and performance trends across the school. The Head Teacher sees academic performance and staff attendance. The Teacher sees their assigned classes and pending tasks. The Parent sees their child's results, attendance, and fee balance. The Student sees their timetable, results, and fee status.

**What happens after a period of inactivity?**

Web sessions expire after 30 minutes of inactivity and the user is redirected to the login screen. Mobile app sessions persist longer but require re-authentication for sensitive actions such as fee recording or mark submission.

---

## 11. Troubleshooting

**The web app will not load. What should I do?**

Verify your internet connection is active. Try clearing your browser cache and cookies, then reload. If the problem persists, try a different browser. If the platform is undergoing scheduled maintenance, a notification banner appears on the login page. Contact support at Chwezi Core Systems if the issue continues.

**I forgot my password and the reset email has not arrived.**

Check your spam or junk folder. Ensure you are entering the email address you registered with. Password reset emails are sent within 2 minutes. If nothing arrives after 5 minutes, contact your school administrator to verify your email is correct in the system, or reach out to Chwezi support.

**I recorded a payment but it does not appear on the student's account.**

Confirm you selected the correct student and term when recording the payment. Check **Fees > Receipts** to verify whether a receipt was generated. If the receipt exists but the balance has not updated, the system may be processing — wait 1 minute and refresh. If the issue persists, contact your school administrator or Chwezi support with the receipt number.

**My marks are not saving when I click submit.**

Ensure no mark exceeds the configured maximum for that exam. The system rejects out-of-range values and displays a red validation message beside the offending field. Also check that the mark entry deadline has not passed — if the deadline has elapsed, the form is locked. Contact the Head Teacher to request a deadline extension if needed.

**The report card shows incorrect grades or missing subjects.**

Verify that all subject marks have been entered and submitted for the student and term in question. Missing marks result in blank fields on the report card. If marks are entered but grades appear wrong, confirm the correct curriculum type (Thematic, Standard, O-Level, A-Level) is assigned to the class under **Academics > Classes**. Regenerate the report card after correcting the data.

**The platform feels slow. How can I improve performance?**

Close unnecessary browser tabs and ensure you are using a supported, up-to-date browser. On Android, ensure the app is updated to the latest version from the Google Play Store. If slowness persists across multiple users at your school, the issue may be network-related — check your school's internet bandwidth. Report persistent performance issues to Chwezi support.

---

## 12. Data and Security

**Where is my school's data stored?**

All data is stored on secure cloud servers with encryption at rest (AES-256) and encryption in transit (TLS 1.3). Student photos, report card PDFs, and documents are stored in AWS S3 with access controlled by authenticated API requests. No data is stored on local devices except temporary offline caches on the Android app, which are encrypted.

**How does AcademiaPro comply with the Uganda Data Protection and Privacy Act (PDPO) 2019?**

All student personal data is classified as sensitive personal data under PDPO. Processing requires a lawful basis — contractual necessity for enrolled students and parental consent for students under 18. The platform provides data export (JSON format) and soft-delete capabilities to support the right of access and right to erasure. Health records (Phase 7) are classified as special category data with restricted access.

**Can I export or delete a student's personal data?**

Yes. School administrators can export a student's complete data record in JSON format from **Students > Data Export**. To request data deletion, navigate to **Students > Data Deletion Request**. Deletion follows a soft-delete pathway — records are marked for removal and permanently purged after a configurable retention period. See the *User Manual*, Section 10.2.

**How are backups handled?**

AcademiaPro performs automated daily backups of all school data. Backups are stored in a geographically separate location from the primary servers. In the event of data loss, Chwezi Core Systems can restore data from the most recent backup. Schools do not need to perform manual backups.

**How is my school's data isolated from other schools?**

AcademiaPro uses row-level tenant isolation. Every database record belonging to your school is tagged with your unique tenant identifier. The system enforces tenant scoping on every database query — no school can access another school's data under any circumstances. Super Admin (Chwezi staff) cross-tenant access is read-only and fully logged.

---

*For questions not covered here, contact Chwezi Core Systems support at chwezicore.com or consult the AcademiaPro User Manual.*


---

## AI Features — Frequently Asked Questions

**Is AI always on for my school?**
No. The AI Module is an optional add-on that costs extra. It is off by default. Your school only has AI features if you have purchased the AI Module subscription and you (as School Owner) have turned on individual features in Settings → AI Module.

**Which AI features are included in my plan?**
- **Starter (UGX 50,000/month):** At-Risk Student Alert, Report Card Comment Generator, Parent Sentiment Analysis.
- **Growth (UGX 200,000/month):** Everything in Starter, plus Weekly Owner Briefing and Fee Default Prediction.
- **Enterprise (UGX 800,000/month):** Everything in Growth, plus AI Executive Dashboard and the Conversational Staff Assistant.

**Does my student data go to OpenAI or Google?**
No. Academia Pro uses Anthropic's Claude AI, which is separate from OpenAI (ChatGPT) and Google. Before your data is sent anywhere, the system removes all student names, ID numbers, and phone numbers. Only anonymous data (like attendance percentages and mark averages) is sent — not individual student records.

**Can the AI get things wrong?**
Yes. The AI analyses patterns in data and makes predictions — it does not know about personal circumstances, family situations, or things that happened outside the system. A student flagged as "at risk" may be fine. A student not on the list may still struggle. The AI is a tool to help teachers and school leaders focus their attention — not a replacement for professional judgement.

**Who can see the AI-generated information?**
- At-risk student lists: School Owner, Head Teacher, Class Teacher (their class only).
- Weekly briefing: School Owner and Head Teacher.
- Fee risk report: School Owner and Bursar.
- Parent sentiment: School Owner and Head Teacher.

Staff who do not need the information cannot see it, following the same role-based access as the rest of the system.

**Can the AI save a report card comment without the teacher seeing it?**
No. Every AI-suggested report card comment must be explicitly accepted by the teacher before it is saved. The teacher can edit or reject any suggestion. The system will never save an AI comment without teacher approval.

**What happens when the AI budget runs out?**
AI features pause for the rest of the month. You will receive a notification when you reach 80% of your budget, giving you time to plan. At 100%, features pause automatically. They restart at the beginning of the next month. You can also contact Chwezi to increase your monthly budget at any time.

**Is the AI compliant with Uganda's data protection law?**
Yes. Academia Pro is built to comply with the Uganda Personal Data Protection and Privacy Act 2019 (DPPA). Student names and government ID numbers are never sent to any AI provider. Only anonymous data is transmitted. An audit trail of all AI activity is maintained for 7 years. The school owner acknowledges the data processing terms when activating the AI module.

**Can I turn off an AI feature I no longer want?**
Yes. Go to Settings → AI Module → Features. You can toggle individual features on or off at any time. Turning off a feature stops new AI calls from being made for that feature. Historical AI insights remain visible until they age out.

**Does the AI learn from my school's data?**
No. Anthropic's standard API terms do not allow customer data to be used for training their models. Your data is processed to generate responses and then discarded by the provider. It is not retained by the AI provider beyond the duration of the API call.
