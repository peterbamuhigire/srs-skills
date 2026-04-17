# User Stories — Academia Pro Phase 1

> User stories follow the format: **As a [role], I want to [action], so that [value].**
> Each story includes Acceptance Criteria in Gherkin Given/When/Then form.
> Stories are grouped by functional area and labelled with the corresponding FR group.

---

## US-AUTH: Authentication

### US-AUTH-001 — Web Login

**As a** school staff member,
**I want to** log in with my username and password,
**so that** I can access the features my role permits.

**Acceptance Criteria:**

```gherkin
Given I am on the login page
When I enter a valid username and password and click Login
Then I am redirected to my role's dashboard
And my session is active with the correct tenant scope

Given I enter an incorrect password
When I click Login
Then I see "Invalid username or password" — without indicating which field is wrong
And my failed attempt count increases by 1

Given I have failed login 5 times
When I attempt a 6th login
Then I see "Account locked. Contact your administrator."
And I am not redirected to the dashboard

Given my session has been idle for 30 minutes
When I click any page element
Then I am redirected to the login page with the message "Your session expired"
```

---

### US-AUTH-002 — Super Admin MFA

**As a** Chwezi Super Admin,
**I want to** be required to complete a second authentication factor after my password,
**so that** platform administration is protected even if my password is compromised.

**Acceptance Criteria:**

```gherkin
Given I am a Super Admin and I enter correct credentials
When I click Login on the Super Admin panel
Then I am shown an MFA code input screen, not the dashboard

Given I enter a correct TOTP code
When I click Verify
Then I am admitted to the Super Admin dashboard

Given I enter an incorrect TOTP code
When I click Verify
Then I see "Invalid code" and am returned to the MFA screen
And the session is not created
```

---

## US-TNT: Tenant Management

### US-TNT-001 — School Onboarding

**As a** Super Admin,
**I want to** create a new school tenant and send the owner a welcome email,
**so that** schools can sign up and start using the platform without manual setup.

**Acceptance Criteria:**

```gherkin
Given I am on the New School form in the Super Admin panel
When I enter school name, owner name, owner email, country, and plan, then click Create
Then the school is created with status "Pending"
And the owner receives a welcome email with a login link and temporary password

Given I view the school in the tenant list
When I click Activate
Then the school status changes to "Active"
And the owner can now log in

Given a user from a suspended school attempts to log in
When they submit their credentials
Then they see "Your school account has been suspended. Contact support."
```

---

## US-SIS: Student Information System

### US-SIS-001 — New Student Admission

**As a** Receptionist,
**I want to** admit a new student by filling in their details,
**so that** they have a school record and can be assigned to a class.

**Acceptance Criteria:**

```gherkin
Given I am on the New Student form
When I fill in all required fields and click Save
Then the student is created with a unique student_uid
And they appear in the class list for the selected class

Given I enter a NIN that already exists in the system
When I click Save
Then I see a message: "A student with this NIN is already registered. Would you like to enrol this existing student?"
And I can choose to link the existing identity rather than create a duplicate

Given I try to save without entering First Name, Last Name, Date of Birth, Gender, or Class
When I click Save
Then I see validation errors next to each missing required field
And no student record is created
```

---

### US-SIS-002 — Student Transfer Out

**As a** Head Teacher,
**I want to** record that a student has transferred to another school,
**so that** the student's record is marked inactive and another school can enrol them.

**Acceptance Criteria:**

```gherkin
Given a student has an active enrolment at my school
When I set their status to "Transferred Out" and provide a transfer date
Then the student no longer appears in the active class list
And all their historical records remain accessible in read-only mode
And if another school searches by NIN, they find the student available for enrolment
```

---

### US-SIS-003 — Student Search

**As a** Class Teacher,
**I want to** search for a student by name or admission number,
**so that** I can quickly find a specific student's record.

**Acceptance Criteria:**

```gherkin
Given the school has 300 students
When I type "nakato" in the search box
Then I see a list of students whose name contains "nakato" within 1 second
And all results are from my school only

When I type a NIN value in the search box
Then I see the matching student if they are enrolled in my school
```

---

## US-ACA: Academics Setup

### US-ACA-001 — Academic Year Setup

**As a** Head Teacher,
**I want to** configure the academic year with 3 terms and their dates,
**so that** all attendance, fee, and exam records can be correctly associated with a term.

**Acceptance Criteria:**

```gherkin
Given I am on the Academic Year setup form
When I enter year label "2026/2027" with 3 non-overlapping term date ranges and click Save
Then the academic year is created with 3 terms

When I try to save with 4 terms
Then I see "Uganda calendar requires exactly 3 terms per academic year"

When I try to save with Term 1 ending after Term 2 starts
Then I see "Term dates must not overlap"
```

---

### US-ACA-002 — Class Creation

**As a** Head Teacher,
**I want to** create class groups with their curriculum type,
**so that** the correct UNEB grading rules apply automatically.

**Acceptance Criteria:**

```gherkin
Given I create a class named "S.4 West" with curriculum type "O-Level"
When I navigate to mark entry for that class
Then the mark entry form shows grade selectors aligned with the UCE 9-point scale

Given I create a class named "Primary 2" with curriculum type "Thematic"
When I view the report card template for that class
Then no numeric aggregate or division is shown — only competency descriptors
```

---

## US-FEE: Fees Management

### US-FEE-001 — Fee Structure Setup

**As an** Accounts Bursar,
**I want to** define the fee structure for each class per term,
**so that** the system can calculate how much each student owes.

**Acceptance Criteria:**

```gherkin
Given I am on the Fee Structures page
When I select "Primary 5", "Term 1 2026", and add line items: Tuition 450,000, Lunch 80,000, Activity 30,000 — then click Save
Then the fee structure is saved and shows on the student's fee balance as UGX 560,000

When I try to save a line item with amount 0
Then I can save it (zero-amount line items are valid placeholders)
```

---

### US-FEE-002 — Manual Payment Recording

**As an** Accounts Bursar,
**I want to** record a student's cash payment and generate a receipt,
**so that** the school's fee ledger is accurate and the parent has proof of payment.

**Acceptance Criteria:**

```gherkin
Given I select a student and enter amount UGX 300,000 paid by cash on today's date
When I click Record Payment
Then a receipt is generated with a sequential number (e.g., REC-2026-0042)
And the student's outstanding balance decreases by UGX 300,000
And an SMS notification is queued to the parent

Given I try to record the identical payment (same student, same amount, same channel) within 5 minutes
When I click Record Payment
Then I see "This payment appears to be a duplicate. Original receipt: REC-2026-0042"
And no second payment record is created

Given I try to delete a receipt
When I click Delete on any receipt
Then the Delete button is not present (receipts are immutable)
```

---

### US-FEE-003 — Refund Request

**As an** Accounts Bursar,
**I want to** submit a refund request for an overpayment,
**so that** the School Owner can review and approve it before the refund is processed.

**Acceptance Criteria:**

```gherkin
Given I submit a refund request for UGX 50,000 with reason "Overpayment Term 1"
When I click Submit Request
Then the request appears in the refund queue with status "Pending Approval"
And the School Owner receives an in-app notification

Given I am logged in as Bursar and try to approve my own refund request
When I click Approve
Then I see "Permission denied. Only the School Owner can approve refunds."

Given the School Owner approves the refund
Then the student's balance is reduced by UGX 50,000
And a credit note receipt is generated
```

---

### US-FEE-004 — Automated Fee Reminders

**As a** Head Teacher,
**I want** the system to automatically send SMS reminders to parents with outstanding fees before term begins,
**so that** we collect fees without manually contacting each parent.

**Acceptance Criteria:**

```gherkin
Given a student has an outstanding balance of UGX 200,000 and term starts in 7 days
When the daily reminder job runs
Then the parent receives an SMS: "Dear [Parent], [Student]'s school fees of UGX 200,000 are due on [date]..."

Given I disable the D-1 reminder in school settings
When D-1 arrives
Then no SMS is sent for the D-1 trigger

Given I try to disable the D-7 reminder in school settings
When I click Save
Then I see "The D-7 reminder cannot be disabled" and the setting is not saved
```

---

## US-ATT: Attendance

### US-ATT-001 — Daily Attendance Entry

**As a** Class Teacher,
**I want to** mark attendance for my class from the web portal,
**so that** the school has an accurate daily record without paper registers.

**Acceptance Criteria:**

```gherkin
Given I am on the Attendance page for my class and today's date
When I mark each student Present, Absent, Late, or Excused and click Submit
Then 45 attendance records are created
And the page shows "Attendance submitted for 45 students"

Given I try to submit attendance for a class that isn't assigned to me
When I navigate to that class's attendance page
Then I see "You do not have permission to access this class"

Given I already submitted attendance for today
When I try to submit again for the same class and date
Then I see "Attendance already recorded for today. Use the Edit function to amend."
```

---

### US-ATT-002 — Absence Alert

**As a** Parent,
**I want to** receive an SMS when my child is absent for 3 consecutive days,
**so that** I can investigate and take action promptly.

**Acceptance Criteria:**

```gherkin
Given my child was marked Absent on Monday, Tuesday, and Wednesday
When the Wednesday attendance is saved
Then I receive an SMS: "Dear [Parent], [Child] has been absent from [School] for 3 consecutive days. Please contact the school."

Given my child was Absent Monday, Present Tuesday, Absent Wednesday and Thursday
When Thursday's absence is saved
Then no alert is sent (the streak was broken by Tuesday's presence)
```

---

### US-ATT-003 — Attendance Amendment

**As a** Class Teacher,
**I want to** correct an attendance record I entered incorrectly within 48 hours,
**so that** the student's record reflects what actually happened.

**Acceptance Criteria:**

```gherkin
Given I submitted attendance 6 hours ago and marked a student Absent by mistake
When I edit that record and change it to Present
Then the record is updated and the amendment is logged with my name and timestamp

Given I try to amend an attendance record from 3 days ago
When I click Edit
Then I see "Records older than 48 hours can only be amended by the Head Teacher"
And the field is disabled for me
```

---

## US-EXM: Examinations

### US-EXM-001 — Exam Setup

**As a** Head Teacher,
**I want to** create an exam with a subject list, maximum marks, and a submission deadline,
**so that** teachers know exactly what marks to enter and when.

**Acceptance Criteria:**

```gherkin
Given I create "End of Term 1 Exams" for P7 with subjects English (max 100), Maths (max 100), Science (max 100), Social Studies (max 100) and a deadline of 15 November 2026
When I save
Then the exam appears in the exam list with the correct subjects and deadline

Given a teacher tries to submit marks after 15 November 2026 without an unlock
When they click Submit Marks
Then they see "Mark entry deadline has passed. Contact the Head Teacher to unlock."
```

---

### US-EXM-002 — Mark Entry

**As a** Class Teacher,
**I want to** enter exam marks for my students from the web portal,
**so that** the system can compute grades and generate report cards automatically.

**Acceptance Criteria:**

```gherkin
Given I am on the mark entry form for P7 English (max mark 100)
When I enter a mark of 85 for a student and click Save
Then the mark is saved and displayed with a provisional grade

When I enter a mark of 105 (exceeding the maximum)
Then I see "Mark cannot exceed 100 for this subject" and the entry is rejected

When I enter a mark for a student not enrolled in this class
Then I see "Student not found in this class" and the entry is rejected
```

---

### US-EXM-003 — UNEB Grade Computation

**As a** Head Teacher,
**I want to** trigger automatic UNEB grade computation after all marks are entered,
**so that** students' aggregates and divisions are calculated instantly without manual effort.

**Acceptance Criteria:**

```gherkin
Given all marks are entered for P7 Term 3 exams
When I click "Compute PLE Grades"
Then each student's aggregate and Division (I–IV or Ungraded) is computed
And the results match the expected values from the UNEB grading tables
And computation for the entire class (up to 200 students) completes within 5 seconds

Given a P4 class with curriculum type "Standard" (not PLE)
When I compute grades
Then no aggregate or division is shown — only subject marks and averages
```

---

## US-RPT: Report Cards

### US-RPT-001 — Bulk Report Card Generation

**As a** Head Teacher,
**I want to** generate report cards for an entire class in one action,
**so that** I don't have to generate them individually for each of the 45 students.

**Acceptance Criteria:**

```gherkin
Given all marks and grades are computed for P7 Term 3
When I click "Generate All Report Cards" for the class
Then a job is queued and I see "Generating 45 report cards..."
And within 120 seconds, I receive a notification: "45 report cards generated. Download all as ZIP."
And clicking the ZIP link downloads a file containing 45 individual PDFs

Given one student has missing marks for Science
When generation completes
Then I see "44 generated, 1 failed: [Student Name] — missing marks for Science"
And I can re-generate that student's card after entering the missing mark
```

---

### US-RPT-002 — Parent Views Report Card

**As a** Parent,
**I want to** view my child's report card on the portal as soon as it's released,
**so that** I don't have to travel to the school to collect a paper copy.

**Acceptance Criteria:**

```gherkin
Given the Head Teacher has released Term 3 report cards
When I log into the parent portal and navigate to my child's report
Then I see the report card with all subjects, grades, aggregate, division, and attendance summary
And I can download it as a PDF

Given report cards have not yet been released
When I navigate to the report card section
Then I see "Term 3 report cards are not yet available. Check back after [release date]."

Given I have two children at the same school
When I view report cards
Then I see a switcher to toggle between child A and child B
```

---

## US-RBAC: User and Role Management

### US-RBAC-001 — Teacher Invitation

**As a** Head Teacher,
**I want to** invite a new Class Teacher by entering their email and assigning their role,
**so that** they can log in and start using the system without me creating their password.

**Acceptance Criteria:**

```gherkin
Given I enter a teacher's email and select "Class Teacher" role and click Send Invite
When the teacher receives the email and clicks the registration link
Then they are taken to a form to set their name and password
And after completing, they can log in as a Class Teacher with appropriate permissions

Given I try to invite someone and assign them the "School Owner" role
When I click Send Invite
Then I see "You cannot assign a role with higher privilege than your own"

Given the invitation link has not been used for 48 hours
When the teacher clicks the link
Then they see "This invitation has expired. Contact the Head Teacher for a new invitation."
```

---

## US-EMIS: Government Export

### US-EMIS-001 — EMIS Data Export

**As a** Head Teacher,
**I want to** export student and teacher data in the MoES EMIS format with one click,
**so that** I can submit our statutory EMIS report without manually compiling data.

**Acceptance Criteria:**

```gherkin
Given the school has 500 active students and 30 staff in the system
When I click "Generate EMIS Export" and select the current academic year
Then the system compiles the required data and downloads a file in MoES format
And the generation completes within 30 seconds

Given some student records are missing EMIS numbers
When the export is generated
Then those students are flagged in the export summary: "[N] students missing EMIS number"
And the export file is still generated for students with complete data
```

---

## US-AUD: Audit Trail

### US-AUD-001 — Owner Views Audit Log

**As a** School Owner,
**I want to** view a log of all significant actions taken in my school's account,
**so that** I can investigate discrepancies and maintain accountability.

**Acceptance Criteria:**

```gherkin
Given a bursar recorded a payment and later a Head Teacher amended an attendance record
When I open the Audit Log
Then I see entries for both actions with timestamp, user, and action type

Given I search the audit log for "fee payment" in the last 30 days
When I click Filter
Then I see only fee payment events from the last 30 days

Given a Super Admin accessed my school's data in support mode
When I view the audit log
Then I see an entry: "Platform Support Access — [Admin Name] — [timestamp]"
```

---

## US-ELEARN: Class Library and E-Learning (Phase 2)

> User stories for Module 21 — Class Library and E-Learning. Roles: Class Teacher (creates materials and assignments), Student (submits and views results), Parent (views results and materials), Head Teacher (oversight).

---

### US-ELEARN-001 — Teacher Uploads a Study Material

**As a** Class Teacher,
**I want to** upload a PDF or link a YouTube video to my subject's class library,
**so that** my students can access revision materials at any time from their phone or the school computer.

**Acceptance Criteria:**

```gherkin
Given I am on the Class Library tab for S4 Biology
When I click Upload Material, select a 5 MB PDF, tag it to Topic "Cell Division", and click Save
Then the PDF appears in the S4 Biology library under "Cell Division"
And students enrolled in S4 Biology can see and download it
And I can see a storage usage indicator showing the file was added to my school's quota

Given I paste a YouTube URL and click Save
Then the resource appears in the library as an embedded link
And no storage quota is consumed by this resource

Given a student opens the PDF from the class library
When I check the Access Log for that material
Then I see the student's name and the date and time they opened it
```

---

### US-ELEARN-002 — Student Downloads a Resource for Offline Use

**As a** Student,
**I want to** download a PDF from my class library while I am on the school's WiFi,
**so that** I can read it at home without needing internet access.

**Acceptance Criteria:**

```gherkin
Given I am logged in and viewing my S4 Biology class library on the app
When I tap the Download button on a PDF resource
Then the file is saved to my device and appears in My Downloads
And when I turn off WiFi and open the app, the PDF opens from local storage

Given I am offline and open the app
When I navigate to My Downloads
Then I can open all previously downloaded PDFs without any error message
```

---

### US-ELEARN-003 — Teacher Creates an Assignment with a Rubric

**As a** Class Teacher,
**I want to** create an assignment with a rubric and a due date,
**so that** students know exactly what they are being assessed on and I can mark consistently.

**Acceptance Criteria:**

```gherkin
Given I am on the New Assignment form for S4 Biology
When I enter title "Cell Division Essay", set due date 3 days from today, set marks total to 20, add rubric criteria "Content (10 marks)" and "Presentation (10 marks)", and click Publish
Then the assignment appears in the student's Assignments tab with the rubric visible
And students see the deadline highlighted in their assignment inbox

Given a student opens the assignment
When they tap View Rubric before submitting
Then they see "Content — 10 marks" and "Presentation — 10 marks"

Given I open the assignment for marking
When I enter scores per rubric criterion for a student
Then the total auto-calculates and I cannot save a total that does not match the criterion sum
```

---

### US-ELEARN-004 — Student Submits Assignment via Phone Camera

**As a** Student,
**I want to** photograph my handwritten work and submit it as my assignment,
**so that** I do not need to retype everything digitally.

**Acceptance Criteria:**

```gherkin
Given I open my Biology Cell Division Essay assignment on the app
When I tap Upload File and select Take a Photo
Then the device camera opens in-app
And I can take a photo of my handwritten work and attach it to my submission

Given I attach 3 photos of 3 pages of handwritten work and tap Submit
Then my submission is recorded with a timestamp confirmation
And I see a green tick on the assignment card showing "Submitted"

Given I lose internet connection after writing my response but before submitting
When I regain connectivity
Then the app automatically submits my draft
And I receive a confirmation that my submission was received
```

---

### US-ELEARN-005 — Teacher Marks and Returns Feedback

**As a** Class Teacher,
**I want to** mark a student's submission in the app and publish written feedback,
**so that** the student understands where they lost marks without me printing and returning papers.

**Acceptance Criteria:**

```gherkin
Given I open the Biology Cell Division Essay marking view
When I tap a student's name
Then I see their submitted text or uploaded photos in-app without downloading separately

When I enter scores per rubric criterion and type feedback "Good analysis of mitosis, but missed meiosis comparison"
And click Publish
Then the student receives a push notification: "Your Cell Division Essay has been marked: 14/20. Tap to view feedback."
And the mark auto-posts to the Biology marks register under the CAT column without any additional action from me

Given I view the class statistics after all marking is done
Then I see class average, highest, lowest, and a score distribution chart
```

---

### US-ELEARN-006 — Marks Auto-Post to Gradebook

**As a** Class Teacher,
**I want** marks to automatically appear in the marks register when I publish an assignment,
**so that** I do not have to enter the same scores twice.

**Acceptance Criteria:**

```gherkin
Given I publish marks for the Biology Cell Division Essay (assignment type: CAT)
When I navigate to the Biology marks register for S4
Then I see each student's essay score already populated in the CAT column
And students who did not submit show "NSubmit" in the column, not a zero

Given the school uses weighted averages (CAT 40%, Exam 60%)
When I view a student's term average
Then the CAT score from the assignment is included in the 40% CAT weight automatically
```

---

### US-ELEARN-007 — Teacher Creates a Revision Quiz

**As a** Class Teacher,
**I want to** create a timed multiple-choice quiz for my class,
**so that** I can check understanding before the end-of-term exam and save marking time.

**Acceptance Criteria:**

```gherkin
Given I create a quiz "Cell Biology Revision" with 10 MCQ questions, 15-minute timer, unlimited attempts, and shuffle enabled
When I publish it to S4 Biology
Then students see the quiz in their Assignments tab during the availability window

Given two students start the quiz at the same time
When each student views their question list
Then the question order is different for each student

Given a student completes the quiz and submits
Then they immediately see their score (e.g., 7/10)
And I see their score in the quiz results list without any marking action from me

Given I view the question analytics after all students complete
Then I see which questions most students answered incorrectly
```

---

### US-ELEARN-008 — Student Submits Quiz with Power Cut

**As a** Student,
**I want** my quiz progress to be saved automatically so I do not lose my work if the power cuts out,
**so that** I am not penalised for an unreliable power supply.

**Acceptance Criteria:**

```gherkin
Given I am 8 minutes into a 15-minute quiz when the power cuts
When power is restored and I reopen the app
Then I resume the quiz with 8 minutes elapsed — the timer does not reset
And all my previously answered questions are still saved

Given the 15-minute timer expires while I am offline
When I reconnect
Then the app automatically submits my cached answers
And my submission is accepted as on-time (not late)
```

---

### US-ELEARN-009 — Parent Views Child's Assignment Result

**As a** Parent,
**I want to** see my child's assignment results and teacher feedback in my app,
**so that** I can support their revision without visiting the school.

**Acceptance Criteria:**

```gherkin
Given my child's Biology essay has been marked and published by their teacher
When I open the parent app and navigate to Assignments
Then I see "Cell Division Essay — 14/20" with the teacher's written feedback

When I try to view the content of my child's submission
Then I can see the score and feedback but not the full submission text or photos (submission privacy)

Given my child received a mark below the class average
When I tap the result
Then I see my child's score and the teacher's feedback — not other students' scores
```

---

### US-ELEARN-010 — Head Teacher Reviews E-Learning Compliance

**As a** Head Teacher,
**I want to** see which teachers have posted materials and set assignments this week,
**so that** I can follow up with those who have not before the end of the school week.

**Acceptance Criteria:**

```gherkin
Given it is Thursday and 3 of 8 teachers have not posted any materials this week
When I open the E-Learning Compliance report for the current week
Then I see a table showing each teacher's name, materials posted, assignments set, and assignments fully marked

Given one teacher has 5 submissions waiting more than 3 days without marking
When I view the compliance report
Then that teacher's row is highlighted with an overdue marking alert

Given I open the Assignment Calendar
When I view the upcoming two weeks
Then I see all assignment deadlines across all classes laid out by date
And I can identify any date where more than 3 assignments are due simultaneously
```
