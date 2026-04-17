---
title: "Test Cases — F-007 Reports, F-008 HR/Payroll, F-009 Dashboard, F-010 Settings"
document-id: "MADUUKA-TC-003"
version: "1.0"
date: "2026-04-05"
standard: "IEEE Std 829-2008"
---

# Test Cases: F-007 Reports, F-008 HR and Payroll, F-009 Dashboard, F-010 Settings

**Document ID:** MADUUKA-TC-003
**Version:** 1.0
**Date:** 2026-04-05
**Parent Plan:** MADUUKA-TP-001

---

## Module F-007: Sales Reporting and Analytics

---

### FR-REP-001 — Daily Sales Report

---

**TC-REP-001**

| Field | Content |
|---|---|
| Test Case ID | TC-REP-001 |
| FR Reference | FR-REP-001 |
| Title | Verify daily sales report groups transactions by payment method with correct totals |
| Preconditions | 1. On 2026-04-05: 3 cash sales totalling UGX 90,000, 2 MTN MoMo sales totalling UGX 60,000, and 1 credit sale for UGX 30,000 are completed. 2. Tester is authenticated as Owner, Manager, or Accountant. |
| Test Steps | 1. Navigate to Reports > Daily Sales. 2. Select date = 2026-04-05. 3. View the report. |
| Expected Result | The report shows 3 groups: Cash = UGX 90,000 (3 transactions), MTN MoMo = UGX 60,000 (2 transactions), Credit = UGX 30,000 (1 transaction). Overall total = UGX 180,000. |
| Pass Criteria | Cash total = UGX 90,000; MoMo total = UGX 60,000; Credit total = UGX 30,000; Grand total = UGX 180,000. |
| Priority | High |

---

### FR-REP-008 — Receipt Gap Report

---

**TC-REP-002**

| Field | Content |
|---|---|
| Test Case ID | TC-REP-002 |
| FR Reference | FR-REP-008, BR-008 |
| Title | Verify receipt gap report lists all gaps from closed sessions in the selected period |
| Preconditions | 1. Two POS sessions are closed with the following receipt sequences: Session S1 — receipts 1001, 1002, 1004 (1003 missing); Session S2 — receipts 2001, 2002, 2003, 2004 (no gaps). 2. Both sessions are within the selected date range. |
| Test Steps | 1. Navigate to Reports > Receipt Gap Report. 2. Select the date range covering both sessions. 3. View the report. |
| Expected Result | The report shows 1 gap entry: Session ID = S1, Expected Receipt = 1003, Cashier = the cashier who ran S1, Date = session close date. Session S2 produces 0 gap entries. |
| Pass Criteria | 1 gap entry total; entry references session S1 and receipt 1003; S2 shows 0 gaps. |
| Priority | Critical |

---

### FR-REP-009 — Report Export

---

**TC-REP-003**

| Field | Content |
|---|---|
| Test Case ID | TC-REP-003 |
| FR Reference | FR-REP-009 |
| Title | Verify CSV report export completes within 30 seconds for a 12-month date range |
| Preconditions | 1. The database contains at least 1,000 transaction records spanning 12 months. 2. Tester is authenticated as Owner or Accountant. |
| Test Steps | 1. Navigate to Reports > Sales Summary. 2. Select date range = last 12 months. 3. Tap "Export CSV". 4. Start a timer. 5. Wait for the download link or file to appear. |
| Expected Result | A CSV file is available for download within 30 seconds of the export request. The CSV file contains one row per transaction in the date range. The row count in the CSV matches the transaction count displayed in the report summary. |
| Pass Criteria | CSV available in ≤ 30 seconds; CSV row count = reported transaction count. |
| Priority | High |

---

## Module F-008: HR and Payroll

---

### FR-HR-011 / FR-HR-012 — PAYE Computation (Uganda 2024/25 Tax Bands)

Uganda 2024/25 monthly PAYE tax bands (Uganda Income Tax Act, Cap 340):

- 0% on gross income ≤ UGX 235,000/month
- 10% on the portion between UGX 235,001 and UGX 335,000/month
- 20% on the portion between UGX 335,001 and UGX 410,000/month
- 30% on the portion above UGX 410,000/month

---

**TC-HR-001**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-001 |
| FR Reference | FR-HR-011, FR-HR-012 |
| Title | Verify PAYE is UGX 0 for gross monthly income at or below UGX 235,000 |
| Preconditions | 1. Staff member "Akello Rose" has a salary structure with basic salary = UGX 200,000/month and no other earnings or custom deductions. 2. The 2024/25 Uganda PAYE tax bands are configured in the system. 3. No payroll has been run for the current month. |
| Test Steps | 1. Navigate to HR > Payroll > Run Payroll. 2. Select the current month. 3. Include "Akello Rose" in the payroll run. 4. Preview the payslip for "Akello Rose". |
| Expected Result | Gross Pay = UGX 200,000. PAYE = UGX 0 (gross ≤ UGX 235,000 — nil band). NSSF Employee (5%) = UGX 10,000. Net Pay = UGX 190,000 (200,000 - 0 - 10,000). |
| Pass Criteria | PAYE = UGX 0; NSSF Employee = UGX 10,000; Net Pay = UGX 190,000. |
| Priority | Critical |

---

**TC-HR-002**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-002 |
| FR Reference | FR-HR-011, FR-HR-012 |
| Title | Verify PAYE computation for gross income in the 10% band |
| Preconditions | 1. Staff member "Okello James" has basic salary = UGX 300,000/month. 2. 2024/25 tax bands configured. |
| Test Steps | 1. Run payroll for the current month including "Okello James". 2. Preview the payslip. |
| Expected Result | Gross Pay = UGX 300,000. PAYE computation: first UGX 235,000 at 0% = UGX 0; remainder UGX 65,000 (300,000 - 235,000) at 10% = UGX 6,500. Total PAYE = UGX 6,500. NSSF Employee (5%) = UGX 15,000. Net Pay = UGX 278,500 (300,000 - 6,500 - 15,000). |
| Pass Criteria | PAYE = UGX 6,500; NSSF Employee = UGX 15,000; Net Pay = UGX 278,500. |
| Priority | Critical |

---

**TC-HR-003**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-003 |
| FR Reference | FR-HR-011, FR-HR-012 |
| Title | Verify PAYE computation for gross income spanning the 10% and 20% bands |
| Preconditions | 1. Staff member "Namukasa Esther" has basic salary = UGX 380,000/month. 2. 2024/25 tax bands configured. |
| Test Steps | 1. Run payroll for the current month including "Namukasa Esther". 2. Preview the payslip. |
| Expected Result | Gross Pay = UGX 380,000. PAYE computation: first UGX 235,000 at 0% = UGX 0; next UGX 100,000 (335,000 - 235,000) at 10% = UGX 10,000; next UGX 45,000 (380,000 - 335,000) at 20% = UGX 9,000. Total PAYE = UGX 19,000. NSSF Employee (5%) = UGX 19,000. Net Pay = UGX 342,000 (380,000 - 19,000 - 19,000). |
| Pass Criteria | PAYE = UGX 19,000; NSSF Employee = UGX 19,000; Net Pay = UGX 342,000. |
| Priority | Critical |

---

**TC-HR-004**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-004 |
| FR Reference | FR-HR-011, FR-HR-012 |
| Title | Verify PAYE computation for gross income exceeding the 30% band threshold |
| Preconditions | 1. Staff member "Mugisha Peter" has basic salary = UGX 600,000/month. 2. 2024/25 tax bands configured. |
| Test Steps | 1. Run payroll for the current month including "Mugisha Peter". 2. Preview the payslip. |
| Expected Result | Gross Pay = UGX 600,000. PAYE computation: first UGX 235,000 at 0% = UGX 0; next UGX 100,000 (335,000 - 235,000) at 10% = UGX 10,000; next UGX 75,000 (410,000 - 335,000) at 20% = UGX 15,000; remainder UGX 190,000 (600,000 - 410,000) at 30% = UGX 57,000. Total PAYE = UGX 82,000. NSSF Employee (5%) = UGX 30,000. Net Pay = UGX 488,000 (600,000 - 82,000 - 30,000). |
| Pass Criteria | PAYE = UGX 82,000; NSSF Employee = UGX 30,000; Net Pay = UGX 488,000. |
| Priority | Critical |

---

### FR-HR-016 — NSSF Computation

---

**TC-HR-005**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-005 |
| FR Reference | FR-HR-016 |
| Title | Verify NSSF schedule shows employee contribution at 5% and employer contribution at 10% of gross |
| Preconditions | 1. Staff member "Mugisha Peter" has gross pay = UGX 600,000 (from TC-HR-004). 2. Payroll run has been approved. |
| Test Steps | 1. Navigate to HR > Payroll > NSSF Schedule. 2. Select the payroll period. 3. Find "Mugisha Peter"'s row. |
| Expected Result | The NSSF schedule shows for "Mugisha Peter": Gross Salary = UGX 600,000; Employee NSSF (5%) = UGX 30,000; Employer NSSF (10%) = UGX 60,000; Total Contribution = UGX 90,000. |
| Pass Criteria | Employee NSSF = UGX 30,000; Employer NSSF = UGX 60,000; Total = UGX 90,000. |
| Priority | Critical |

---

### Local Service Tax (LST)

---

**TC-HR-006**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-006 |
| FR Reference | FR-HR-011 |
| Title | Verify LST of UGX 100,000 per year is deducted in January for Kampala staff earning above UGX 1,000,000/month |
| Preconditions | 1. The business is configured in Kampala district. 2. Kampala LST rate is configured: UGX 100,000/year for employees with gross monthly income > UGX 1,000,000. 3. Staff member "Ssemakula David" has gross salary = UGX 1,200,000/month. 4. The payroll run is for January 2026. |
| Test Steps | 1. Run payroll for January 2026 including "Ssemakula David". 2. Preview the payslip. |
| Expected Result | The payslip shows a "Local Service Tax" deduction line = UGX 100,000. This deduction appears only in January (annual LST). |
| Pass Criteria | LST deduction = UGX 100,000 on the January payslip; LST deduction = UGX 0 on a non-January payslip for the same employee. |
| Priority | High |

---

**TC-HR-007**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-007 |
| FR Reference | FR-HR-011 |
| Title | Verify LST is not deducted for Kampala staff earning UGX 1,000,000 or below per month |
| Preconditions | 1. Kampala LST threshold configured at UGX 1,000,000/month. 2. Staff member "Akello Rose" has gross salary = UGX 200,000/month. 3. Payroll run is for January 2026. |
| Test Steps | 1. Run payroll for January 2026. 2. Preview "Akello Rose"'s payslip. |
| Expected Result | No "Local Service Tax" deduction line appears on the payslip. |
| Pass Criteria | LST deduction = UGX 0; no LST line on payslip. |
| Priority | High |

---

### FR-HR-013 — Payroll Immutability After Approval (BR-012)

---

**TC-HR-008**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-008 |
| FR Reference | FR-HR-013, BR-012 |
| Title | Verify approved payroll payslip amounts cannot be modified directly |
| Preconditions | 1. Payroll for March 2026 has been run and approved. 2. "Mugisha Peter"'s approved payslip shows Net Pay = UGX 488,000. 3. Tester is authenticated as Owner or HR Manager. |
| Test Steps | 1. Navigate to HR > Payroll > March 2026 > "Mugisha Peter"'s payslip. 2. Attempt to edit the Net Pay field. 3. Attempt to edit the Basic Salary field. 4. Attempt to save any modification to the payslip. |
| Expected Result | All payslip amount fields are read-only. No edit controls are enabled. A note is displayed: "This payslip is locked. Corrections require a reversal in the next payroll period." No modification can be saved through any UI pathway. |
| Pass Criteria | All amount fields are read-only; save/edit controls are absent or disabled; lock message is displayed. |
| Priority | Critical |

---

**TC-HR-009**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-009 |
| FR Reference | FR-HR-013, BR-012 |
| Title | Verify approved payroll cannot be modified via API |
| Preconditions | 1. Payroll run ID "PR-2026-03" is in "approved" status. 2. A valid JWT for an Owner-role user is available. |
| Test Steps | 1. Send a PUT request to `PUT /api/v1/payroll/PR-2026-03/payslips/{payslip_id}` with a modified net pay value. 2. Observe the HTTP response. |
| Expected Result | The API returns HTTP 403 with error code `PAYROLL_LOCKED`. The payslip record in the database is unchanged. |
| Pass Criteria | HTTP 403 returned; error code = `PAYROLL_LOCKED`; payslip record unchanged in database. |
| Priority | Critical |

---

### FR-HR-014 / FR-HR-015 — Payslip Generation and Delivery

---

**TC-HR-010**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-010 |
| FR Reference | FR-HR-014 |
| Title | Verify PDF payslip contains all required fields |
| Preconditions | 1. Payroll for April 2026 has been approved. 2. "Mugisha Peter"'s payslip for April 2026 shows: Gross = UGX 600,000, PAYE = UGX 82,000, NSSF Employee = UGX 30,000, Net Pay = UGX 488,000. |
| Test Steps | 1. Navigate to HR > Payroll > April 2026 > "Mugisha Peter" > Download Payslip. 2. Open the PDF. 3. Inspect the content. |
| Expected Result | The PDF payslip contains: business name and logo, employee full name "Mugisha Peter", employee ID, pay period (April 2026), earnings breakdown (Basic Salary = UGX 600,000), deductions breakdown (PAYE = UGX 82,000; NSSF Employee = UGX 30,000), Gross Pay = UGX 600,000, Total Deductions = UGX 112,000, Net Pay = UGX 488,000. |
| Pass Criteria | PDF contains all listed fields with correct values; Net Pay = UGX 488,000. |
| Priority | High |

---

### FR-HR-019 — Salary Advance Repayment

---

**TC-HR-011**

| Field | Content |
|---|---|
| Test Case ID | TC-HR-011 |
| FR Reference | FR-HR-019 |
| Title | Verify salary advance creates automatic monthly repayment deduction until balance is zero |
| Preconditions | 1. Staff member "Byamukama Sam" has gross salary = UGX 800,000. 2. A salary advance of UGX 300,000 is recorded, repayable over 3 months (UGX 100,000/month). |
| Test Steps | 1. Run payroll for Month 1 and preview "Byamukama Sam"'s payslip. 2. Approve Month 1 payroll. 3. Run payroll for Month 2 and preview the payslip. 4. Approve Month 2. 5. Run payroll for Month 3 and preview. 6. Approve Month 3. 7. Run payroll for Month 4 and preview. |
| Expected Result | Month 1 payslip: Advance Repayment deduction = UGX 100,000; outstanding advance = UGX 200,000. Month 2 payslip: Advance Repayment deduction = UGX 100,000; outstanding = UGX 100,000. Month 3 payslip: Advance Repayment deduction = UGX 100,000; outstanding = UGX 0. Month 4 payslip: no Advance Repayment deduction line; outstanding = UGX 0. |
| Pass Criteria | 3 consecutive months of UGX 100,000 deductions; Month 4 shows no advance deduction. |
| Priority | High |

---

## Module F-009: Dashboard and Business Health

---

### FR-DASH-001 — KPI Cards

---

**TC-DASH-001**

| Field | Content |
|---|---|
| Test Case ID | TC-DASH-001 |
| FR Reference | FR-DASH-001 |
| Title | Verify dashboard displays correct values for all four KPI cards on open |
| Preconditions | 1. Today's completed sales total = UGX 450,000 (3 transactions). 2. All customer outstanding balances total = UGX 1,200,000. 3. All active payment accounts total = UGX 350,000. 4. Tester is authenticated as Owner or Manager. |
| Test Steps | 1. Open the application and navigate to the Dashboard. 2. Observe the 4 KPI cards. |
| Expected Result | Today's Revenue card shows UGX 450,000. Transaction Count card shows 3. Outstanding Credit card shows UGX 1,200,000. Cash Position card shows UGX 350,000. The last sync timestamp is displayed below or near the cards. |
| Pass Criteria | All 4 KPI values match seeded data exactly; last sync timestamp visible. |
| Priority | High |

---

### FR-DASH-003 — Auto-Refresh (Web)

---

**TC-DASH-002**

| Field | Content |
|---|---|
| Test Case ID | TC-DASH-002 |
| FR Reference | FR-DASH-003 |
| Title | Verify web dashboard KPI values auto-refresh every 2 minutes without a page reload |
| Preconditions | 1. The web dashboard is open with Today's Revenue = UGX 450,000. 2. A new sale of UGX 50,000 is completed (bringing Today's Revenue to UGX 500,000) at time T. 3. Browser network tab is visible. |
| Test Steps | 1. Note the time of the new sale (time T). 2. Do not reload the page. 3. Wait up to 2 minutes (120 seconds) from T. 4. Observe the Today's Revenue KPI card. |
| Expected Result | Within 120 seconds of the new sale, the Today's Revenue card updates to UGX 500,000 without a full page reload. The browser's URL does not change. A background API refresh request is visible in the network tab. |
| Pass Criteria | Revenue card shows UGX 500,000 within 120 seconds; no full page reload; background refresh request observed. |
| Priority | High |

---

### FR-DASH-006 — Branch Switcher

---

**TC-DASH-003**

| Field | Content |
|---|---|
| Test Case ID | TC-DASH-003 |
| FR Reference | FR-DASH-006 |
| Title | Verify branch switcher updates all KPI cards to the selected branch data within 2 seconds |
| Preconditions | 1. The business has 2 branches: Branch A (today's revenue = UGX 300,000) and Branch B (today's revenue = UGX 150,000). 2. The dashboard is showing Branch A data. 3. Tester is authenticated as Owner or Branch Manager with access to both branches. |
| Test Steps | 1. On the dashboard, tap the branch switcher. 2. Select "Branch B". 3. Start a timer. 4. Observe when KPI cards update. |
| Expected Result | Within 2 seconds of selecting "Branch B", the Today's Revenue card updates to UGX 150,000. All other KPI cards reflect Branch B's data. The last sync timestamp updates. |
| Pass Criteria | Today's Revenue = UGX 150,000 within 2 seconds; all KPI cards reflect Branch B data. |
| Priority | High |

---

## Module F-010: Settings and Configuration

---

### FR-SET-005 / FR-SET-006 — Multi-Tenant Data Isolation (BR-001)

---

**TC-SET-001**

| Field | Content |
|---|---|
| Test Case ID | TC-SET-001 |
| FR Reference | FR-SET-005, BR-001 |
| Title | Verify Franchise A cashier cannot read Franchise B sales data |
| Preconditions | 1. Two franchises exist: Franchise A (ID = "FRAN-A") and Franchise B (ID = "FRAN-B"). 2. Franchise B has 5 sales records with known IDs. 3. A Cashier-role JWT for Franchise A is available. |
| Test Steps | 1. Authenticate as a Franchise A Cashier. 2. Send `GET /api/v1/sales` with the Franchise A JWT. 3. Verify that 0 Franchise B sale IDs appear in the response. 4. Attempt to fetch a specific Franchise B sale: `GET /api/v1/sales/{franchise_B_sale_id}`. 5. Observe the response. |
| Expected Result | Step 2 returns only Franchise A sales; Franchise B records are absent. Step 4 returns HTTP 403 or HTTP 404. No Franchise B data is present in any response field. |
| Pass Criteria | `GET /api/v1/sales` response contains 0 Franchise B records; `GET /api/v1/sales/{franchise_B_sale_id}` returns HTTP 403 or HTTP 404. |
| Priority | Critical |

---

**TC-SET-002**

| Field | Content |
|---|---|
| Test Case ID | TC-SET-002 |
| FR Reference | BR-001 |
| Title | Verify SQL injection in franchise_id parameter does not expose cross-tenant data |
| Preconditions | 1. Two franchises exist: Franchise A and Franchise B. 2. A valid JWT for Franchise A is available. |
| Test Steps | 1. Send `GET /api/v1/sales?franchise_id=FRAN-A' OR '1'='1` with the Franchise A JWT. 2. Observe the HTTP response and response body. |
| Expected Result | The API returns HTTP 400 with an error indicating an invalid parameter format. The response body contains no sale records from Franchise B. No database error details are exposed in the response. |
| Pass Criteria | HTTP 400 returned; 0 Franchise B records in response; no SQL error messages in response body. |
| Priority | Critical |

---

### FR-SET-011 — 2FA TOTP Setup and Verification

---

**TC-SET-003**

| Field | Content |
|---|---|
| Test Case ID | TC-SET-003 |
| FR Reference | FR-SET-011 |
| Title | Verify 2FA TOTP setup generates a TOTP secret and QR code for the authenticator app |
| Preconditions | 1. Business owner "Peter Bamuhigire" is authenticated. 2FA is not currently enabled. 2. Google Authenticator or a compatible TOTP app is available on a test device. |
| Test Steps | 1. Navigate to Settings > Security > Enable 2FA. 2. Tap "Set Up Two-Factor Authentication". 3. Observe the screen. |
| Expected Result | A QR code is displayed on screen for scanning by the TOTP app. A text backup code (the TOTP secret) is also displayed for manual entry. The TOTP secret is not re-transmitted after this step. The QR code encodes a valid TOTP URI (`otpauth://totp/...`). |
| Pass Criteria | QR code displayed; TOTP URI format is valid; backup secret displayed; QR code is scannable and registers correctly in Google Authenticator. |
| Priority | High |

---

**TC-SET-004**

| Field | Content |
|---|---|
| Test Case ID | TC-SET-004 |
| FR Reference | FR-SET-011 |
| Title | Verify login from an unrecognised device requires TOTP code entry when 2FA is enabled |
| Preconditions | 1. 2FA is enabled for "Peter Bamuhigire". 2. A valid TOTP secret is registered in Google Authenticator. 3. A new browser session (no existing session cookie or recognised device cookie) is used. |
| Test Steps | 1. Open the web login page in a new browser profile (no cookies). 2. Enter valid email and password for "Peter Bamuhigire". 3. Tap "Sign In". 4. Observe the result. |
| Expected Result | After correct email/password entry, a TOTP code entry screen is displayed: "Enter the 6-digit code from your authenticator app." The user is not logged in until the TOTP code is entered and verified. |
| Pass Criteria | TOTP screen displayed after correct password; login not granted before TOTP entry. |
| Priority | High |

---

**TC-SET-005**

| Field | Content |
|---|---|
| Test Case ID | TC-SET-005 |
| FR Reference | FR-SET-011 |
| Title | Verify a valid TOTP code grants access and an expired TOTP code is rejected |
| Preconditions | 1. 2FA is enabled for "Peter Bamuhigire". 2. The TOTP screen is displayed (continuation of TC-SET-004). 3. Google Authenticator displays the current 6-digit code. |
| Test Steps | 1. Enter the current valid 6-digit TOTP code. 2. Tap "Verify". 3. Observe login result. 4. Log out. 5. Repeat login. 6. On the TOTP screen, enter an obviously expired code (e.g., a code from a screenshot taken 60 seconds ago that is no longer current). 7. Tap "Verify". |
| Expected Result | Step 1–3: Valid code grants access; dashboard is displayed. Step 6–7: Expired code is rejected with message "Invalid or expired code. Try again." Access is not granted. |
| Pass Criteria | Valid current code grants access; expired code rejected with error message; no access granted on invalid code. |
| Priority | High |

---

### FR-SET-012 — Connected Device Revocation

---

**TC-SET-006**

| Field | Content |
|---|---|
| Test Case ID | TC-SET-006 |
| FR Reference | FR-SET-012 |
| Title | Verify revoking a device immediately invalidates its refresh token |
| Preconditions | 1. "Peter Bamuhigire" has 2 active sessions: Device A (web browser) and Device B (Android). 2. Valid refresh tokens exist for both devices. 3. Tester is operating on Device A. |
| Test Steps | 1. Navigate to Settings > Security > Connected Devices. 2. Confirm Device B is listed with a last-active date. 3. Tap "Revoke" next to Device B. 4. On Device B, attempt to use the refresh token to obtain a new access token (`POST /api/v1/auth/refresh` with Device B's refresh token). |
| Expected Result | Device B is removed from the connected devices list. The refresh token request from Device B returns HTTP 401. Device B's access is terminated immediately without requiring Device B to be online at the time of revocation. |
| Pass Criteria | Device B absent from devices list after revocation; `POST /api/v1/auth/refresh` with Device B token returns HTTP 401. |
| Priority | High |

---

*End of MADUUKA-TC-003 v1.0 — Test Cases: F-007 Reports, F-008 HR/Payroll, F-009 Dashboard, F-010 Settings*

**Total test cases in this file: 20**
