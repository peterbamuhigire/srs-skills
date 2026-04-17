## Research & Development — TC-RES

---

**TC-RES-001** | R&D | Banana variety performance record entry and retrieval

*Preconditions:* R&D module accessible to Research Officer.

*Test steps:*
1. Navigate to R&D → Banana Varieties → New Record.
2. Enter: cultivar name "Kayinja," processing yield 32%, quality score 8.5/10, regional suitability "Western Uganda."
3. Save.
4. Search for "Kayinja" in the variety database.

*Expected result:* Record saved and retrieved with all entered values intact. Search response within 500 ms. | **P3**

---

**TC-RES-002** | R&D | Field trial: yield analysis recorded per plot

*Preconditions:* Field trial FT-TEST-001 created with 3 plots: Plot A (cv. Kayinja), Plot B (cv. Mbwazirume), Plot C (cv. Nfuuka).

*Test steps:*
1. Record harvest data for each plot: weights, quality scores, harvest dates.
2. Run yield analysis for FT-TEST-001.

*Expected result:* Yield analysis displays: cultivar, input area, kg harvested, yield per hectare, quality score per plot. Highest-yield cultivar highlighted. Data exportable as Excel. | **P3**

---

**TC-RES-003** | R&D | R&D expenditure linked to GL

*Preconditions:* R&D cost centre configured in chart of accounts.

*Test steps:*
1. Record R&D expenditure: UGX 500,000 for field trial equipment.
2. Confirm GL posting.

*Expected result:* GL auto-posts: DR R&D Expense UGX 500,000 / CR AP (or Cash) UGX 500,000. Expenditure visible in R&D module and in GL R&D cost centre report. | **P3**

---

## Administration & PPDA Compliance / System Administration — TC-ADM

---

**TC-ADM-001** | Administration | PPDA procurement register: all document types tracked

*Preconditions:* 3 test procurement transactions of different PPDA categories (micro, small, large) with all required documents uploaded.

*Test steps:*
1. Navigate to Administration → PPDA Procurement Register.
2. View all 3 transactions.

*Expected result:* Each transaction shows: procurement category, PPDA document checklist with status (complete / missing) for each required document (request, quotation, evaluation report, LPO, GRN, invoice, payment). All documents for all 3 test transactions show "Complete." | **P2**

---

**TC-ADM-002** | Administration | Asset register: depreciation calculation

*Preconditions:* Asset "Factory Generator" acquisition cost UGX 50,000,000, acquisition date 2020-01-01, useful life 10 years, straight-line depreciation.

*Test steps:*
1. Navigate to Administration → Asset Register → Factory Generator.
2. View depreciation schedule as at 2026-04-05.

*Expected result:* Annual depreciation: UGX 5,000,000. Accumulated depreciation (6.25 years): UGX 31,250,000. Net book value as at 2026-04-05: UGX 18,750,000. | **P3**

---

**TC-ADM-003** | System Admin | User role assignment and immediate enforcement

*Preconditions:* User "Test User 01" currently has "Sales Officer" role. IT Administrator changes role to "Finance Officer."

*Test steps:*
1. Log into `/public/admin/` as IT Administrator.
2. Edit Test User 01 → change role to "Finance Officer." Save.
3. Test User 01 attempts to access the Sales module.

*Expected result:* Role change effective immediately (no re-login required). Test User 01 can now access Finance module pages. Test User 01 receives HTTP 403 on Sales module pages not accessible to Finance Officer role. | **P1**

---

**TC-ADM-004** | System Admin | Audit log query: any 30-day period, any user, ≤ 5 seconds

*Preconditions:* Audit log contains ≥ 10,000 records across the test dataset.

*Test steps:*
1. Navigate to `/public/admin/` → Audit Log.
2. Filter: user = "Sales Officer A," date range = 2026-03-01 to 2026-03-31.
3. Start timer. Click Search.

*Expected result:* Results returned within 5 seconds. All records show: actor, action, table affected, old values, new values, IP address, timestamp. | **P2**

---

**TC-ADM-005** | System Admin | 8-layer RBAC: time-based access restriction

*Preconditions:* Role "Field Agent" configured with time-based access: Monday–Friday, 07:00–20:00 EAT only.

*Test steps:*
1. Test Field Agent user attempts login at 23:00 EAT on a weekday.

*Expected result:* Login rejected. Error: "Access is restricted outside permitted hours (07:00–20:00, Monday–Friday)." Attempt logged in audit trail. | **P2**

---

**TC-ADM-006** | System Admin | Automated database backup completes within 4 hours

*Preconditions:* Backup schedule configured for daily at 23:00. Database size: representative of production (staged with full test dataset).

*Test steps:*
1. Trigger a manual backup via Admin → Backup Management.
2. Monitor backup progress.

*Expected result:* Backup completes successfully. Backup file created and verified. Completion time ≤ 4 hours. Backup log records: start time, end time, file size, and status = "Success." | **P2**

---

**TC-ADM-007** | System Admin | 2FA enforcement for Director role

*Preconditions:* Director account with 2FA (TOTP) configured.

*Test steps:*
1. Director logs in with correct username and password.
2. System prompts for TOTP code.
3. Enter correct TOTP code.

*Expected result:* Director access granted only after TOTP code verified. Attempt with incorrect TOTP code rejected. Account lockout triggered after 5 failed TOTP attempts. | **P1**

---

**TC-ADM-008** | System Admin | Integration configuration: EFRIS API credentials update

*Preconditions:* IT Administrator logged into `/public/admin/`.

*Test steps:*
1. Navigate to Admin → Integration Configuration → EFRIS.
2. Update EFRIS API key and endpoint URL.
3. Click Test Connection.

*Expected result:* System sends test ping to EFRIS sandbox. If valid: "EFRIS connection successful." Credentials saved encrypted (not visible in plain text in the UI after save). Old credentials overwritten. | **P2**

---
