## Human Resources — TC-HR

---

**TC-HR-001** | HR | ZKTeco biometric attendance import: records match device export

*Preconditions:* ZKTeco device export file for 2026-03-01: 50 attendance records (25 employees, in/out pairs).

*Test steps:*
1. Navigate to HR → Attendance → Import Biometric.
2. Upload ZKTeco export file.
3. Confirm import.

*Expected result:* 50 records imported. Each employee's attendance record matches the device export exactly (no rounding on time, no missing records, no duplicates). Import summary shows: 50 records imported, 0 errors. (BR-016.) | **P1**

---

**TC-HR-002** | HR | Biometric attendance override requires Finance Manager approval

*Preconditions:* Employee "Test Employee 01" has biometric record: 2026-03-15 IN 08:05, OUT 17:30. HR Officer attempts to change OUT time to 15:00.

*Test steps:*
1. Navigate to HR → Attendance → Manual Override for Test Employee 01 on 2026-03-15.
2. HR Officer attempts to set OUT time to 15:00.
3. Finance Manager approves override with reason: "Approved medical appointment."

*Expected result:* Override blocked without Finance Manager approval. After Finance Manager approval: attendance record updated to OUT 15:00. Audit trail records: original biometric value (17:30), new value (15:00), Finance Manager identity, timestamp, and reason. (BR-016.) | **P1**

---

**TC-HR-003** | HR | Leave application: HR Self-Service App

*Preconditions:* Employee "Test Employee 02" has 10 annual leave days remaining. HR Self-Service App installed on Android device.

*Test steps:*
1. Log in as Test Employee 02.
2. Apply for annual leave: 5 days, 2026-04-10 to 2026-04-16.
3. Submit application.

*Expected result:* Leave application submitted with status "Pending Approval." HR Manager receives notification. On approval: leave balance reduced to 5 days. Employee receives push notification: "Leave approved: 5 days annual leave, 2026-04-10 to 2026-04-16." | **P2**

---

**TC-HR-004** | HR | Employee payslip viewable via HR Self-Service App

*Preconditions:* Payroll for March 2026 has been run and locked. Employee "Test Employee 03" payslip generated.

*Test steps:*
1. Log in as Test Employee 03 in the HR Self-Service App.
2. Navigate to Payslips → March 2026.
3. Open payslip.

*Expected result:* Payslip displays: employee name, month, gross salary, PAYE deducted, NSSF employee deduction, LST deduction, net pay, and employer NSSF contribution. Values match the locked payroll run. | **P2**

---

**TC-HR-005** | HR | Staff loan with payroll deduction

*Preconditions:* Employee "Test Employee 04" approved loan: UGX 1,000,000. Repayment: UGX 100,000/month for 10 months.

*Test steps:*
1. Record loan in HR → Staff Loans → New Loan for Test Employee 04.
2. Configure deduction: UGX 100,000/month.
3. Run next payroll.

*Expected result:* UGX 100,000 deducted from Test Employee 04's net pay in the payroll run. Loan outstanding balance reduced to UGX 900,000. Deduction visible on payslip. GL posts loan repayment correctly. | **P2**

---

## Payroll — TC-PAY

---

**TC-PAY-001** | Payroll | PAYE oracle: gross UGX 200,000/month — below threshold

*Preconditions:* Employee "Payroll Test 01" gross salary: UGX 200,000/month. Uganda PAYE 2024/25 bands: 0–235,000 = 0%.

*Test steps:*
1. Run payroll for Payroll Test 01.
2. Check PAYE deduction.

*Expected result:* PAYE = UGX 0 (gross is below the UGX 235,000 threshold). Net pay = UGX 200,000 minus other statutory deductions. | **P1**

---

**TC-PAY-002** | Payroll | PAYE oracle: gross UGX 300,000/month

*Preconditions:* Employee "Payroll Test 02" gross salary: UGX 300,000/month.

Uganda 2024/25 PAYE bands:
- Band 1: 0 – UGX 235,000 → 0%
- Band 2: UGX 235,001 – UGX 335,000 → 10%
- Band 3: UGX 335,001 – UGX 410,000 → 20%
- Band 4: UGX 410,001 – UGX 10,000,000 → 30%

*Test steps:*
1. Run payroll for Payroll Test 02.
2. Check PAYE calculation.

*Expected result:* PAYE = (UGX 300,000 − UGX 235,000) × 10% = UGX 65,000 × 10% = **UGX 6,500**. Net pay before NSSF and LST = UGX 300,000 − UGX 6,500 = UGX 293,500. | **P1**

---

**TC-PAY-003** | Payroll | PAYE oracle: gross UGX 400,000/month

*Preconditions:* Employee "Payroll Test 03" gross salary: UGX 400,000/month.

*Test steps:*
1. Run payroll for Payroll Test 03.
2. Check PAYE calculation.

*Expected result:*
- Band 2 tax: (UGX 335,000 − UGX 235,000) × 10% = UGX 100,000 × 10% = UGX 10,000.
- Band 3 tax: (UGX 400,000 − UGX 335,000) × 20% = UGX 65,000 × 20% = UGX 13,000.
- Total PAYE = UGX 10,000 + UGX 13,000 = **UGX 23,000**.
Net pay before NSSF and LST = UGX 400,000 − UGX 23,000 = UGX 377,000. | **P1**

---

**TC-PAY-004** | Payroll | PAYE oracle: gross UGX 700,000/month

*Preconditions:* Employee "Payroll Test 04" gross salary: UGX 700,000/month.

*Test steps:*
1. Run payroll for Payroll Test 04.
2. Check PAYE calculation.

*Expected result:*
- Band 2 tax: (UGX 335,000 − UGX 235,000) × 10% = UGX 100,000 × 10% = UGX 10,000.
- Band 3 tax: (UGX 410,000 − UGX 335,000) × 20% = UGX 75,000 × 20% = UGX 15,000.
- Band 4 tax: (UGX 700,000 − UGX 410,000) × 30% = UGX 290,000 × 30% = UGX 87,000.
- Total PAYE = UGX 10,000 + UGX 15,000 + UGX 87,000 = **UGX 112,000**.
Net pay before NSSF and LST = UGX 700,000 − UGX 112,000 = UGX 588,000. | **P1**

---

**TC-PAY-005** | Payroll | NSSF oracle: gross UGX 500,000

*Preconditions:* Employee "Payroll Test 05" gross salary: UGX 500,000/month. NSSF rates configured: employer 10%, employee 5%.

*Test steps:*
1. Run payroll for Payroll Test 05.
2. Check NSSF calculation.

*Expected result:*
- Employee NSSF contribution: UGX 500,000 × 5% = **UGX 25,000** (deducted from employee net pay).
- Employer NSSF contribution: UGX 500,000 × 10% = **UGX 50,000** (employer cost, not deducted from employee).
- Total NSSF remittance to NSSF Uganda: UGX 75,000.
GL posts: DR Salary Expense UGX 500,000 + DR NSSF Employer Expense UGX 50,000 / CR NSSF Payable UGX 75,000 / CR PAYE Payable [per TC-PAY-xxx] / CR Cash/Bank UGX [net pay]. | **P1**

---

**TC-PAY-006** | Payroll | LST deduction applied at Bushenyi local government rate

*Preconditions:* Employee "Payroll Test 06" based in Bushenyi. LST configured per Bushenyi local government ordinance (e.g., UGX 7,000/month for gross 200,001–500,000 range).

*Test steps:*
1. Run payroll for Payroll Test 06 (gross UGX 400,000).
2. Check LST deduction.

*Expected result:* LST deducted at the Bushenyi-configured rate. Value matches the configured LST band. GL posts LST payable correctly. [CONTEXT-GAP: GAP-005 — Confirm current Bushenyi LST rate schedule with local government before asserting exact oracle value here.] | **P1**

---

**TC-PAY-007** | Payroll | Payroll lock: modification blocked after Finance Manager approval (BR-010)

*Preconditions:* March 2026 payroll run completed and approved (locked) by Finance Manager.

*Test steps:*
1. Attempt to modify an employee salary line in the March 2026 payroll run (any user, including Finance Manager).

*Expected result:* Modification blocked. Error: "Payroll run for March 2026 is locked. No modifications permitted. To correct an error, process an adjustment run in the next payroll period." Payroll run remains unchanged. (BR-010.) | **P1**

---

**TC-PAY-008** | Payroll | Payroll GL auto-posting on approval

*Preconditions:* April 2026 payroll run calculated. Finance Manager approves and locks.

*Test steps:*
1. Finance Manager approves April 2026 payroll.
2. Check GL entries.

*Expected result:* GL auto-posts on approval: DR Salary Expense (gross payroll total) / CR PAYE Payable (total PAYE) / CR NSSF Payable (total employee + employer NSSF) / CR LST Payable / CR Staff Loans Deductions Payable (if any) / CR Bank/Cash (net payroll). No manual journal entry required. | **P1**

---

**TC-PAY-009** | Payroll | NSSF remittance schedule in exact NSSF Uganda format

*Preconditions:* April 2026 payroll locked with 20 employees.

*Test steps:*
1. Navigate to Payroll → Reports → NSSF Remittance Schedule for April 2026.
2. Generate schedule.

*Expected result:* Schedule generated in the format required by NSSF Uganda: member number, employee name, NIN, employer contribution, employee contribution, total contribution per employee. Grand total row present. File downloadable as PDF and Excel. | **P2**

---

**TC-PAY-010** | Payroll | Bulk mobile money salary payment for casual workers

*Preconditions:* 10 test casual workers with mobile money numbers. Net pay calculated for March 2026.

*Test steps:*
1. Navigate to Payroll → Bulk Payment → Mobile Money.
2. Select March 2026, Casual Workers group.
3. Generate bulk payment file.

*Expected result:* Bulk payment file generated for MTN MoMo / Airtel Money API: employee name, mobile number, net pay amount. File downloadable. [CONTEXT-GAP: GAP-002 — MTN MoMo sandbox required for API submission test.] | **P2**

---
