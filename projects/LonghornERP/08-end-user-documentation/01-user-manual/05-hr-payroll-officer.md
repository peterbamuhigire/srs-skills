# HR and Payroll Officer Guide

**Role:** HR/Payroll Officer

**Accessible modules:** HR, Leave Management, Attendance, Payroll Run

---

## Adding a New Employee Record

1. In the sidebar, click **HR**, then click **Employees**.
2. Click **New Employee**.
3. Enter the employee's **First Name** and **Last Name**.
4. Enter the **National ID Number**.
5. Enter the **Date of Birth** using the date picker.
6. Select **Gender** from the dropdown.
7. Enter the **Personal Phone Number** and **Personal Email**.
8. Enter the **Start Date** (date of employment).
9. Upload a profile photo by clicking **Upload Photo** and selecting an image file.
10. Click **Save and Continue** to proceed to the employment details step.

---

## Assigning an Employee to a Department and Grade

After saving the basic employee record, the system presents the **Employment Details** tab.

1. Select the **Department** from the dropdown.
2. Select the **Job Title** from the dropdown, or type to search.
3. Select the **Grade** or **Salary Band** from the dropdown. The grade determines the default salary ranges and leave entitlements.
4. Enter the **Basic Salary** amount.
5. Select the **Payment Method**: Bank Transfer or Mobile Money.
6. If bank transfer, enter the **Bank Name**, **Branch**, and **Account Number**.
7. If Mobile Money, enter the **MoMo Number** and select the **Network** (MTN or Airtel).
8. Select the employee's **Branch** from the dropdown.
9. Click **Save Employment Details**.

---

## Recording a Leave Application and Approving It

### Recording a Leave Application

1. In the sidebar, click **HR**, then click **Leave Management**, then click **Leave Applications**.
2. Click **New Leave Application**.
3. Select the **Employee** from the dropdown.
4. Select the **Leave Type** (Annual Leave, Sick Leave, Maternity Leave, etc.).
5. Set the **From Date** and **To Date** using the date pickers.
6. Enter the reason in the **Reason** field.
7. Attach any supporting documents (for example, a medical certificate for sick leave) by clicking **Attach File**.
8. Click **Submit Application**.

### Approving a Leave Application

1. In the sidebar, click **HR**, then click **Leave Management**, then click **Pending Approvals**.
2. Click the leave application you want to review.
3. Verify the leave type, dates, and remaining balance shown on screen.
4. Click **Approve** to grant the leave, or click **Reject** and enter a reason in the dialog.
5. Click **Confirm**. The employee's leave balance updates immediately.

---

## Viewing Employee Leave Balances

1. In the sidebar, click **HR**, then click **Leave Management**, then click **Leave Balances**.
2. Select the **Employee** from the dropdown to view one employee, or leave it blank to view all employees.
3. Select the **Leave Year** from the dropdown.
4. Click **Generate**. The table shows each leave type, the annual entitlement, days taken, and the remaining balance.
5. Click **Export to Excel** to download the report.

---

## Recording Attendance (Manual Entry)

1. In the sidebar, click **HR**, then click **Attendance**.
2. Click **Manual Entry**.
3. Select the **Employee**.
4. Set the **Date**.
5. Enter the **Check-In Time** and **Check-Out Time**.
6. If the employee was absent, select **Absent** from the **Status** dropdown and record a reason.
7. Click **Save Entry**.

To record attendance for multiple employees on the same day, click **Bulk Entry**, select the date, and fill in the attendance grid that lists all active employees.

---

## Running a Monthly Payroll

*Complete all steps in order. Do not skip the review step.*

1. In the sidebar, click **HR**, then click **Payroll**, then click **New Run**.
2. Select the **Payroll Period** (month and year) from the dropdown.
3. Select the **Branch** or branches to include in this run. Select **All Branches** for a company-wide payroll.
4. Click **Generate Preview**. The system calculates gross pay, statutory deductions (PAYE, NSSF, LST), and net pay for every employee in the selected scope.
5. Review the payroll preview table. Verify the **Gross Pay**, **Total Deductions**, and **Net Pay** for each employee. Flag any anomalies before proceeding.
6. To correct an error, click the employee row to open their detail, adjust the value, and click **Update**. Regenerate the preview if you make changes to salary data.
7. When the preview is correct, click **Approve Run**. Enter your password to confirm.
8. Click **Post to GL**. The system creates journal entries in the finance module for the payroll expense and liability accounts.
9. Click **Download Payment File**. Select the format: **Bank CSV** for bank transfers or **MoMo Batch File** for Mobile Money disbursement. Save the file and submit it to your bank or MoMo portal.

---

## Downloading a Payslip PDF

1. In the sidebar, click **HR**, then click **Payroll**, then click **Payslips**.
2. Select the **Employee** from the dropdown.
3. Select the **Payroll Period**.
4. Click **Generate Payslip**.
5. The payslip preview appears on screen.
6. Click **Download PDF** to save the payslip, or click **Email to Employee** to send it directly to the employee's registered email address.

---

## Running a Payroll Validation Pack

1. Open **HR > Payroll > Payroll Runs**.
2. Click the draft payroll run you want to review.
3. Click **Generate Validation Pack**.
4. Review the findings tabs:
   - **Missing Payment Details**
   - **Missing Statutory IDs**
   - **Attendance Exceptions**
   - **Negative Net Pay**
   - **Large Variances**
5. Resolve or waive each finding according to policy.
6. Click **Mark Validation Reviewed** only after all mandatory findings are cleared.

---

## Running a Shadow Payroll

1. Open **HR > Payroll > Shadow Runs**.
2. Click **New Shadow Run**.
3. Select the **Payroll Period** and the **Pay Group**.
4. Choose the comparison basis:
   - **Current Live Data**
   - **Imported Legacy Results**
5. Click **Compute Shadow Run**.
6. Review the variance report. Confirm that the shadow run has **not** posted to the GL and has **not** generated employee payslips or payment files.
7. Export the variance report if Finance or management needs sign-off before the live run is approved.
