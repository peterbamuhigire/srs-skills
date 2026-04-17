# AcademiaPro User Manual

**Version:** 1.0
**Date:** 2026-04-03
**Audience:** All AcademiaPro users (School Owners, Head Teachers, Teachers, Bursars, Secretaries, Students, Parents)

---

## 1 Getting Started

### 1.1 Accessing AcademiaPro

AcademiaPro is a web application. You do not need to install any software on your computer.

1. Open a web browser (Chrome, Firefox, Edge, or Safari).
2. Type `https://app.academiapro.com` in the address bar and press Enter.
3. The login page appears.

If your school has provided you with the AcademiaPro mobile app, download it from the Google Play Store (Android) or the Apple App Store (iOS). See Section 10 for download instructions.

### 1.2 Logging In

1. On the login page, enter the **Email** or **Phone Number** your school registered for you.
2. Enter your **Password**.
3. Press the **Login** button.
4. If your account is linked to more than one school (for example, you are a teacher at one school and a parent at another), select the school you want to access from the list that appears.

If you have forgotten your password, press the **Forgot Password** link on the login page. Enter your email address. A password reset link is sent to your email. Open the email and follow the instructions.

### 1.3 Navigating the Dashboard

After logging in, you see your dashboard. The dashboard shows only the features your role is allowed to access. A Class Teacher sees different menu items from a Bursar.

The main navigation menu is on the left side of the screen. On phones, tap the menu icon (three horizontal lines) at the top left to open the menu.

Common elements on every dashboard:

- **Top bar:** Your name, school name, current term, and a notification bell
- **Side menu:** Links to every module you have access to
- **Quick actions:** Shortcuts to your most-used tasks (for example, "Take Attendance" for teachers, "Record Payment" for bursars)
- **Notifications:** A red badge on the bell icon shows unread notifications. Press the bell to see alerts such as absent students, payment confirmations, or system messages.

### 1.4 Updating Your Profile

1. Press your name or profile picture at the top right of the screen.
2. Select **My Profile** from the dropdown menu.
3. You can update your phone number, email address, and profile photo.
4. Press **Save Changes** when finished.

To change your password:

1. On the **My Profile** page, press the **Change Password** tab.
2. Enter your current password.
3. Enter your new password and confirm it.
4. Press **Update Password**.

---

## 2 School Owner Guide

As the School Owner or Director, you have full visibility over your school. You can manage staff, configure modules, view financial summaries, and monitor academic performance.

### 2.1 School Setup

When your school first joins AcademiaPro, the onboarding wizard walks you through the initial configuration. If you need to change any of these settings later:

1. Go to **Settings > School Profile**.
2. Update the school name, address, motto, badge/logo, contact details, and EMIS school code.
3. Press **Save**.

### 2.2 Managing Staff Accounts

1. Go to **Staff > Staff List**.
2. Press **Add Staff Member**.
3. Enter the staff member's full name, email, phone number, and national ID.
4. Select the role to assign: Head Teacher, Class Teacher, Subject Teacher, Bursar, Secretary, Accountant, Librarian, or any custom role you have created.
5. Press **Save**. The system sends a welcome email with login credentials.

To deactivate a staff account (for example, when a staff member leaves):

1. Go to **Staff > Staff List**.
2. Find the staff member and press **Edit**.
3. Change the status to **Inactive**.
4. Press **Save**. The person can no longer log in.

### 2.3 Configuring Modules

AcademiaPro ships with standard modules enabled for every school. Optional modules (Library, Transport, Hostel, Communication) can be activated as your subscription allows.

1. Go to **Settings > Modules**.
2. Toggle each module on or off using the switch.
3. Press **Save**.

Disabling a module hides it from all staff menus. Data already entered in that module is not deleted.

### 2.4 Viewing Reports and Dashboards

Your dashboard shows a financial overview with total fees collected, outstanding balances, and recent payments. Below that you see academic summaries and attendance rates.

To view detailed financial reports:

1. Go to **Reports > Financial Reports**.
2. Select the report type: Collection Summary, Defaulters List, or Term Reconciliation.
3. Choose the term and class (or select "All Classes").
4. Press **Generate Report**.
5. Press **Export to Excel** or **Export to PDF** to download the report.

To view academic performance reports:

1. Go to **Reports > Academic Reports**.
2. Select School Performance Summary or Class Comparison.
3. Choose the academic year and term.
4. Press **Generate Report**.

### 2.5 Approving Fee Refunds

When a bursar submits a refund request, you receive a notification.

1. Go to **Fees > Refund Requests**.
2. Review the details: student name, amount, reason.
3. Press **Approve** or **Reject**.
4. If approved, the refund is processed and the student's balance is updated.

Only the School Owner or Director role can approve refunds.

---

## 3 Head Teacher Guide

As Head Teacher, you manage the academic structure of the school: academic years, classes, subjects, examinations, and report cards. You also oversee attendance and submit statutory reports.

### 3.1 Setting Up an Academic Year

At the beginning of each year:

1. Go to **Academics > Academic Years**.
2. Press **Create New Academic Year**.
3. Enter the year (for example, "2026").
4. Set the opening and closing dates for Term 1, Term 2, and Term 3.
5. Press **Save**.

When you create a new academic year, the Year-Start Promotion Wizard launches automatically. See Section 3.9 for details.

### 3.2 Managing Classes and Streams

1. Go to **Academics > Classes**.
2. Press **Add Class** to create a new class (for example, "P.6" or "S.3").
3. If the class has streams, press **Add Stream** and enter the stream name (for example, "East", "West", "Red").
4. Set the "Promotes To" destination class. For final-year classes (P.7, S.4, S.6), leave this blank.
5. Assign a Class Teacher to each class or stream.
6. Press **Save**.

### 3.3 Managing Subjects

1. Go to **Academics > Subjects**.
2. Press **Add Subject**.
3. Enter the subject name and code (for example, "Mathematics", "MATH").
4. Select the curriculum type: Thematic (P.1-P.3), Standard Primary (P.4-P.7), O-Level, or A-Level.
5. Set the maximum mark for internal exams (for example, 100).
6. Assign the Subject Teacher.
7. Press **Save**.

### 3.4 Curriculum Type Configuration

AcademiaPro supports all Uganda curriculum types:

- **Thematic Curriculum (P.1-P.3):** Competency-based. No numeric grades. Descriptors are Highly Competent (HC), Competent (C), and Not Yet Competent (NYC).
- **Standard Primary (P.4-P.7):** Numeric marks converted to PLE-style grades (1 = Distinction to 4 = Fail). The PLE aggregate is computed from 4 compulsory subjects.
- **O-Level (S.1-S.4):** 9-point scale (D1 to F9). Aggregate and division computed per UNEB rules.
- **A-Level (S.5-S.6):** Principal passes graded A to E; F = Fail. Subsidiary pass graded O. Points are computed for university entry.

You do not need to configure grading scales manually. The system applies the correct UNEB grading rules based on the curriculum type you select for each class.

### 3.5 Exam Configuration

1. Go to **Examinations > Exam List**.
2. Press **Create Exam**.
3. Enter the exam name (for example, "End of Term 1 Examinations 2026").
4. Select the term.
5. Select the classes that sit this exam.
6. Set the exam period start and end dates.
7. Set the mark entry deadline. After this deadline, Subject Teachers can no longer enter or change marks. Only the Head Teacher can unlock mark entry after the deadline has passed.
8. Press **Save**.

### 3.6 UNEB Setup

For candidate classes sitting national examinations (P.7, S.4, S.6):

1. Go to **Examinations > UNEB Configuration**.
2. Confirm that the correct subjects are mapped to the UNEB compulsory and elective categories for each class.
3. Verify the grading scale matches the current UNEB published rules. AcademiaPro ships with the current UNEB scales pre-configured. If UNEB changes its grading rules, Chwezi Core Systems will update the system.
4. Review the candidate list. The system pulls all active students in the candidate class.
5. Press **Export Candidate List** to generate a file in UNEB registration format if needed.

### 3.7 Report Cards

To generate termly report cards:

1. Ensure all Subject Teachers have completed mark entry and the mark entry deadline has passed.
2. Go to **Reports > Report Cards**.
3. Select the class and term.
4. The system computes grades automatically using the UNEB grading engine.
5. Add your Head Teacher's comment for each student, or use the **Bulk Comment** feature to apply a general comment to all students.
6. Press **Generate Report Cards**.
7. The system generates a PDF report card for each student.
8. Press **Download All** to get a single PDF file containing all report cards for the class, ready for printing.

Individual report cards can also be viewed and downloaded from the student's profile.

### 3.8 EMIS Export

The Ministry of Education and Sports (MoES) requires schools to submit statistical returns through the Education Management Information System (EMIS).

1. Go to **Reports > EMIS Export**.
2. Select the reporting period.
3. The system compiles student headcount, gender breakdown, teacher count, and other EMIS-required data from your existing records.
4. Press **Generate EMIS Report**.
5. Review the data summary before exporting.
6. Press **Export** to download the file in the format required by MoES (CSV or XML).
7. Submit the exported file to your EMIS coordinator.

### 3.9 Year-Start Promotion Wizard

When you create a new academic year, the Promotion Wizard runs automatically. Term 1 of the new year cannot open until every class has been processed.

1. The wizard displays each class with all enrolled students.
2. By default, all students are set to **Promote** to the next class (the "Promotes To" destination you configured).
3. To hold a student back (repeat the class), deselect that student. They will be re-enrolled in the same class for the new year.
4. For final-year classes (P.7, S.4, S.6), students are automatically set to **Depart** because there is no destination class.
5. For each departing student, select the departure reason: Completed, Transferred, Withdrawn, or Other.
6. Press **Confirm Promotions** for each class.
7. After all classes are processed, the new academic year opens.

### 3.10 Attendance Oversight

1. Go to **Attendance > Overview**.
2. You see attendance rates per class for the current week.
3. Press any class to see individual student attendance.
4. Students with 3 or more consecutive absences are flagged in red. The system has already sent an SMS alert to their parents automatically.
5. To amend an attendance record older than 48 hours (after the Class Teacher's editing window has closed), press the record and enter the correction with a reason.

---

## 4 Class Teacher Guide

As a Class Teacher, you are responsible for daily attendance, entering marks for your class, adding report card comments, and managing student profiles within your assigned class.

### 4.1 Taking Attendance

1. Go to **Attendance > Take Attendance**.
2. Select your class (if not already selected by default).
3. The current date is selected automatically. You can change the date to record attendance for a previous day (within the past 48 hours only).
4. The student list appears. Each student defaults to **Present**.
5. Tap the status next to each student's name to change it: Present, Absent, Late, or Excused.
6. Press **Submit Attendance**.
7. If any student reaches 3 consecutive absent days, the system automatically sends an SMS to the parent.

On the mobile app, swipe left on a student's name to mark them Absent quickly.

### 4.2 Entering Marks

1. Go to **Examinations > Enter Marks**.
2. Select the exam and subject.
3. The student list for your class appears with a marks input field next to each name.
4. Type the mark for each student. The system rejects marks that exceed the configured maximum mark for that exam (for example, typing 120 when the maximum is 100 will show a red error).
5. Press **Save** after entering marks for all students.
6. You may return and edit marks until the mark entry deadline set by the Head Teacher. After the deadline, marks are locked.

### 4.3 Adding Report Card Comments

1. Go to **Reports > Report Cards > My Class**.
2. Select the term.
3. Each student has a **Class Teacher's Comment** field.
4. Type your comment for each student. Keep comments professional and constructive.
5. Press **Save Comments**.

The Head Teacher adds their own comment separately.

### 4.4 Viewing Student Profiles

1. Go to **Students > My Class**.
2. Press any student's name to view their full profile.
3. The profile shows: personal details, parent/guardian contact, attendance summary, exam results, fee balance, and medical summary (if recorded).
4. You can update limited fields such as the student's emergency contact number. For major changes (name, date of birth), contact the Secretary or Head Teacher.

---

## 5 Subject Teacher Guide

As a Subject Teacher, you enter marks for the subjects assigned to you across one or more classes.

### 5.1 Entering Marks for Your Subjects

1. Go to **Examinations > Enter Marks**.
2. Select the exam.
3. You see only the subjects assigned to you. Select a subject.
4. Select the class.
5. The student list appears with a marks input field next to each name.
6. Enter each student's mark. The system rejects marks above the configured maximum.
7. Press **Save**.
8. Repeat for each class and subject assigned to you.

You may return and edit marks until the mark entry deadline passes.

### 5.2 Viewing Grades

After the Head Teacher publishes results:

1. Go to **Examinations > Results**.
2. Select the exam and your subject.
3. The system displays each student's mark, computed grade, and class ranking for that subject.
4. You can download this list as an Excel file by pressing **Export**.

---

## 6 Bursar Guide

As the Bursar (Accounts), you manage fee structures, record payments, generate receipts, track balances, and produce financial reports.

### 6.1 Setting Up Fee Structures

Fee structures are defined per class per term.

1. Go to **Fees > Fee Structures**.
2. Press **Add Fee Structure**.
3. Select the class (for example, "P.5" or "S.2").
4. Select the term (Term 1, Term 2, or Term 3).
5. Enter the fee items and amounts in Uganda Shillings (UGX). Common items include: tuition, boarding, lunch, uniform, development fund.
6. Enter the total fee for the term.
7. Press **Save**.
8. Repeat for each class and term.

Arrears from previous terms are carried forward automatically. You do not need to add them manually.

### 6.2 Recording a Payment (Manual)

When a parent or student pays fees at the school office:

1. Go to **Fees > Record Payment**.
2. Search for the student by name, admission number, or student payment code.
3. The current fee balance is displayed.
4. Select the payment method: Cash, Bank Transfer, or Cheque.
5. Enter the amount paid. There is no minimum payment amount; partial payments of any size are accepted (KUPAA micro-payment model).
6. Press **Record Payment**.
7. A receipt is generated automatically with a sequential receipt number. The receipt cannot be deleted.
8. Press **Print Receipt** to print, or **Send Receipt** to send a copy to the parent's phone via SMS.

### 6.3 SchoolPay and Mobile Money Payments

When SchoolPay integration is active (Phase 2), payments made by parents via MTN MoMo, Airtel Money, bank, or agent through SchoolPay are recorded automatically.

1. The system receives payment notifications from SchoolPay in real time.
2. Go to **Fees > Payment History** to see all payments, including those received via SchoolPay.
3. Each SchoolPay payment shows the source channel (MTN MoMo, Airtel Money, Bank, Agent), the SchoolPay receipt number, and the timestamp.
4. If a payment appears in SchoolPay but not in AcademiaPro (rare, caused by temporary network issues), the system's nightly reconciliation job corrects the gap automatically. You may also trigger a manual reconciliation from **Fees > Reconciliation**.

### 6.4 Receipts

Every payment, whether recorded manually or received via SchoolPay, generates a receipt.

1. Go to **Fees > Receipts**.
2. Search by student name, receipt number, or date range.
3. Press **View** to see the receipt details.
4. Press **Print** to print a paper copy.
5. Press **Resend** to send the receipt to the parent's registered phone number or email.

Receipts are numbered sequentially per school and cannot be modified or deleted.

### 6.5 Fee Reports

1. Go to **Reports > Financial Reports**.
2. Available reports:
   - **Collection Summary:** Total fees collected per class, per term, broken down by payment method.
   - **Defaulters List:** Students with outstanding balances, sorted by amount owed. Filterable by class.
   - **Term Reconciliation:** Compares total fees expected against total fees collected, with a breakdown of each payment.
   - **Daily Collection Report:** All payments recorded today, useful for end-of-day cash reconciliation.
3. Select the report, choose the term and class filters, and press **Generate**.
4. Press **Export to Excel** or **Export to PDF** to download.

### 6.6 Fee Reminders

The system sends automated fee reminders to parents:

- 7 days before the term opening date
- 1 day before the term opening date
- 7 days after the term opening date (for unpaid balances)

You can configure additional reminder dates or disable reminders (except the 7-day pre-term reminder, which cannot be removed) from **Settings > Fee Reminders**.

### 6.7 Requesting a Refund

If a parent requests a fee refund:

1. Go to **Fees > Refund Requests**.
2. Press **New Refund Request**.
3. Search for the student.
4. Enter the refund amount and reason.
5. Press **Submit Request**.
6. The request goes to the School Owner/Director for approval. You cannot approve refunds yourself.
7. You receive a notification when the request is approved or rejected.

---

## 7 Secretary Guide

As the Secretary (Receptionist), you handle student admissions, enrolments, transfers, and certificate generation.

### 7.1 Admitting a New Student

1. Go to **Students > New Admission**.
2. Enter the student's personal details: full name, date of birth, gender, nationality, religion.
3. Enter identification numbers if available: NIN (for students aged 16 and above), LIN (Learner Identification Number).
4. Upload a passport-sized photograph.
5. Enter parent/guardian details: name, phone number, email, relationship.
6. Enter the class and stream to enrol the student in.
7. Press **Save**.
8. The system assigns a unique Student ID (UUID) that stays with the student permanently, even if they transfer to another school.

**Cross-school lookup:** Before admitting a student, the system checks if the student already exists on the platform using NIN or LIN. If a match is found, the student's global identity (name, date of birth, gender) is pulled automatically. You do not re-enter it.

### 7.2 Enrolling a Student for a New Term

If a student is already admitted but needs to be enrolled for a new term or academic year:

1. Go to **Students > Student List**.
2. Find the student and press **Enrol**.
3. Select the academic year and term.
4. Confirm the class and stream.
5. Press **Save**.

### 7.3 Transferring a Student

**Transfer to another AcademiaPro school (in-platform):**

1. Go to **Students > Student List**.
2. Find the student and press **Transfer**.
3. Select **In-Platform Transfer**.
4. Search for the destination school.
5. Confirm the transfer. The student's record becomes read-only at your school, and the destination school can enrol the student using their existing global identity.

**Transfer to a non-AcademiaPro school (external):**

1. Follow the same steps but select **External Transfer**.
2. Enter the destination school name (for reference only).
3. The student's record is marked as departed with reason "Transferred (External)".

In both cases, a departure record is created. The student's historical data (marks, attendance, fees) at your school is permanently locked and read-only.

### 7.4 Generating Certificates

1. Go to **Certificates > Generate**.
2. Select the certificate type: Completion, Merit, or Participation.
3. Select the students to receive the certificate.
4. Customise the certificate text if needed.
5. Press **Generate**.
6. Certificates are produced as PDF files. Press **Download** or **Print**.
7. For bulk printing, select multiple students and press **Generate All**.

---

## 8 Student Guide

As a student, you can view your academic information through the Student Portal.

### 8.1 Accessing the Student Portal

1. Log in to AcademiaPro using the credentials your school gave you.
2. Your dashboard shows an overview of your current term: timetable, recent marks, attendance, and fee balance.

### 8.2 Viewing Your Marks and Grades

1. Go to **My Results**.
2. Select the academic year and term.
3. Your marks, grades, and class position for each subject are displayed.
4. Press **View Report Card** to see the full termly report card as a PDF.

### 8.3 Viewing Your Attendance

1. Go to **My Attendance**.
2. A calendar view shows your attendance for the current term.
3. Green days are Present, red days are Absent, yellow days are Late, and blue days are Excused.
4. Monthly and termly attendance percentages are shown at the bottom.

### 8.4 Checking Your Fee Balance

1. Go to **My Fees**.
2. Your current term fee balance is displayed, along with a history of all payments made.
3. If your school uses SchoolPay, your Student Payment Code is shown. Give this code to your parent/guardian for making payments.

### 8.5 Viewing Your Timetable

1. Go to **My Timetable**.
2. The weekly timetable for your class is displayed.
3. Subjects, teachers, and room numbers are shown for each period.

### 8.6 Viewing Your Academic History

If you have attended more than one AcademiaPro school, you can view your records from all previous schools.

1. Go to **My Academic History**.
2. Select the previous school.
3. View your marks, attendance summaries, and report cards from that school.

Fee payment amounts from previous schools are not shown. Only a clearance status (Cleared or Not Cleared) is displayed.

---

## 9 Parent Guide

As a parent or guardian, you can monitor your child's academic progress, attendance, and fee balance through the Parent Portal or the mobile app.

### 9.1 Accessing the Parent Portal

1. Log in to AcademiaPro using the credentials your school gave you.
2. If you have more than one child at the school (or at different AcademiaPro schools), select which child to view from the dropdown at the top of the screen.

### 9.2 Viewing Your Child's Marks

1. Go to **My Child > Results**.
2. Select the term.
3. Your child's marks, grades, and class position are displayed.
4. Press **View Report Card** to see the full termly report card.
5. Press **Download** to save the report card as a PDF on your phone or computer.

### 9.3 Viewing Your Child's Attendance

1. Go to **My Child > Attendance**.
2. A calendar view shows your child's attendance.
3. If your child has been absent for 3 consecutive days, you will have received an SMS alert automatically.
4. Monthly and termly attendance percentages are displayed.

### 9.4 Checking Your Child's Fee Balance

1. Go to **My Child > Fees**.
2. The current outstanding balance is displayed.
3. A full payment history shows every payment made, the date, the amount, and the receipt number.
4. Arrears from previous terms are listed separately.

### 9.5 Paying Fees via Mobile Money (SchoolPay)

When SchoolPay integration is active:

1. Your child's **Student Payment Code** is displayed on the Fees page.
2. On your phone, open your MTN MoMo or Airtel Money menu.
3. Select **Payments** or **Pay Bill**.
4. Search for "SchoolPay" or enter the SchoolPay merchant code.
5. Enter your child's Student Payment Code when prompted.
6. Enter the amount you wish to pay. You can pay any amount, even a small one. There is no minimum.
7. Confirm the payment with your mobile money PIN.
8. You receive a confirmation SMS from your mobile money provider.
9. Within minutes, the payment appears on the AcademiaPro Fees page with the receipt number.

If the payment does not appear within 1 hour, contact the school bursar. The system performs a nightly reconciliation that catches any delayed payments.

### 9.6 Receiving Notifications

You receive notifications through:

- **SMS:** Attendance alerts (3 consecutive absences), fee reminders (7 days before term, 1 day before term, 7 days into term if unpaid), and critical school announcements.
- **In-app notifications:** Press the bell icon to view all notifications.
- **Email:** If you registered an email address, you also receive notifications there.

### 9.7 Communication with Teachers

If the school has enabled the Communication module:

1. Go to **My Child > Messages**.
2. You can view messages sent by the school, the Head Teacher, or your child's Class Teacher.
3. Some messages allow a reply. Press **Reply** to respond.

---

## 10 Troubleshooting

### 10.1 I Cannot Log In

- Confirm that you are using the correct email or phone number.
- Check that your password is correct. Passwords are case-sensitive.
- If you have forgotten your password, press **Forgot Password** on the login page.
- If your account is locked (after 5 failed login attempts), wait 15 minutes and try again, or contact the school administration.
- If your account has been deactivated by the school, contact the Head Teacher or School Owner.

### 10.2 The Page Is Loading Slowly

- Check your internet connection. AcademiaPro requires an active internet connection.
- Close other browser tabs that may be using bandwidth.
- Try refreshing the page (press F5 on a computer, or pull down to refresh on a phone).
- If the problem persists, try using a different browser (Chrome is recommended).

### 10.3 I Cannot See a Module in My Menu

- You only see modules that your role has access to. A Class Teacher does not see the Fees module, for example.
- If you believe you should have access to a module, contact the Head Teacher or School Owner to check your assigned role and permissions.

### 10.4 Marks Entry Is Locked

- Mark entry is locked after the deadline set by the Head Teacher. Contact the Head Teacher to unlock mark entry if you need to make a correction.
- Marks are also permanently locked 30 days after the term's configured end date. After that point, corrections require the Head Teacher's intervention and all changes are logged.

### 10.5 A Payment Does Not Appear

- If you paid via SchoolPay (mobile money), the payment should appear within a few minutes. If it does not appear within 1 hour, contact the school bursar.
- The system runs a nightly reconciliation with SchoolPay. Missing payments are recovered automatically by the next morning.
- If you paid cash at the school office, confirm that the bursar recorded the payment. Ask for your receipt number.

### 10.6 I Entered the Wrong Attendance

- If the mistake is within the past 48 hours, you (the Class Teacher) can correct the attendance record directly.
- If more than 48 hours have passed, ask the Head Teacher to correct the record. The Head Teacher must enter a reason for the amendment, and the change is logged.

### 10.7 My Report Card Has Incorrect Grades

- Report card grades are computed automatically by the system using UNEB grading rules. If a grade appears wrong, the most likely cause is an incorrect mark entered by the Subject Teacher.
- Contact the Head Teacher, who can check the original mark entry and request a correction from the Subject Teacher before regenerating the report card.

### 10.8 I Cannot Access the Mobile App

- Ensure your phone meets the minimum requirements: Android 8.0 or later, or iOS 14.0 or later.
- Ensure you have downloaded the official AcademiaPro app from the Google Play Store or Apple App Store. Do not download from other sources.
- Ensure your phone has at least 100 MB of free storage.
- If the app does not open, uninstall and reinstall it.

### 10.9 I Need Help Not Covered Here

- Contact your school's Head Teacher or administration office.
- For technical issues, the school administration can contact Chwezi Core Systems support via the in-app support chat or at `support@academiapro.com`.


---

## Chapter: AI Features

> The AI features in Academia Pro are only available if your school has purchased the AI Module add-on. If you do not see these features, contact your Chwezi account manager to activate the AI Module for your school.

### For School Owners and Directors

#### Your Weekly School Briefing

Every Monday morning at 7am, you will receive a notification in Academia Pro with a short summary of how your school performed last week. The summary is written in plain English and covers:
- Overall school attendance for the week.
- How fee collection is tracking against your target.
- Which class is performing best and which needs attention.
- Any student welfare alerts flagged by the system.

You do not need to log in or navigate any reports. The briefing comes to you.

**What to do:** Read the briefing. If the briefing flags a concern (e.g., "attendance dropped to 78% this week"), click the link in the notification to see the full attendance report.

#### Understanding AI Confidence Levels

Some AI outputs show a confidence level — High, Medium, or Low.
- **High:** The AI has strong data to support its conclusion. You can act on this with reasonable confidence.
- **Medium:** The AI's conclusion is reasonable but you should verify with the underlying data before taking a significant decision.
- **Low:** The AI has limited data or the pattern is unclear. Review carefully. Do not rely on this alone.

#### AI Budget

Your school has a monthly AI budget. When your school uses 80% of its AI budget in a month, you will receive an alert. When the budget is fully used, AI features pause until the following month.

To check your current AI usage: go to **Settings → AI Module → Usage and Budget**.

---

### For Head Teachers

#### Reviewing the At-Risk Student List

Every Monday, the system analyses each student's attendance, marks, and activity. Students who are at risk of failing appear in a ranked list on your dashboard under **AI Insights**.

**How to use it:**
1. Review the list each Monday morning.
2. For each High Risk student, look at the reason (e.g., "Attendance 54% and marks below 45%").
3. Contact the class teacher or the student's parents as appropriate.
4. The system does not take any automatic action — all decisions are yours.

**What it does not do:** The AI does not know about personal circumstances, family situations, or anything outside the data in the system. Use your own judgement alongside the AI list.

---

### For Class Teachers

#### AI Report Card Comments

After you have entered all marks for the term and the Head Teacher has verified them, you can ask the AI to suggest a comment for each student's report card.

**How to use it:**
1. Go to **Report Cards → Your Class → Generate AI Comments**.
2. The system generates a suggested comment for each student (usually within 30 seconds for a full class).
3. Review each comment. You will see: Accept, Edit, or Reject.
   - **Accept:** The comment is saved as written.
   - **Edit:** Change any part of the comment before saving.
   - **Reject:** The comment is not used. Write your own instead.
4. Click **Save Approved Comments** when you are done.

**Important:** Only comments you Accept or Edit are saved. The AI cannot save a comment without your approval. You remain responsible for everything in the report card.

**What makes a good AI comment?** The AI uses the student's actual marks, attendance percentage, and class. The more accurate the data in the system, the better the AI comment will be.

#### Rating AI Suggestions

After using any AI feature, you can rate the output with a thumbs-up (the AI was helpful) or thumbs-down (the AI got it wrong). Your ratings help us improve the system over time.

---

### For Bursars

#### Fee Risk Report

One week before each term opens, the system analyses payment history and identifies parents who may need early contact about fees. You will find this under **Fees → Fee Risk Report**.

The list shows: student name, parent contact, and a risk level (High or Medium). High Risk means the family has a pattern of late or partial payment. Medium Risk means they sometimes delay.

**How to use it:**
1. Review the High Risk list 7 days before term opens.
2. Contact parents early — before the term begins — to confirm payment plans.
3. You can export the list as CSV for use in a phone call tracking sheet.

**Note:** This list is a prediction, not a certainty. Some parents on the list may pay on time. Some parents not on the list may miss payment. Use it as a starting point for proactive communication, not a definitive judgment.
