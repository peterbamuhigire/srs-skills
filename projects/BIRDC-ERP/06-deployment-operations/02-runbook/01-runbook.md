---
title: "BIRDC ERP — Operations Runbook"
subtitle: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
---

# BIRDC ERP Operations Runbook

**Document:** Operations Runbook
**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com)
**Client:** PIBID / BIRDC, Nyaruzinga hill, Bushenyi District, Western Uganda
**Date:** 2026-04-05
**Version:** 1.0
**Deployment Model:** Single-tenant, on-premise at BIRDC Nyaruzinga, Bushenyi, Uganda

---

## How to Use This Runbook

Each procedure in this runbook is written for the BIRDC IT Administrator or Finance Director. Procedures are self-contained: complete all steps in sequence, in order, without skipping. Steps marked **ESCALATE** require immediate notification of Peter Bamuhigire or the Finance Director before continuing.

**Escalation contacts:**

| Contact | Role | Channel |
|---|---|---|
| Peter Bamuhigire | ICT Consultant | WhatsApp / Email: peter@techguypeter.com |
| Finance Director | BIRDC Finance Director | Internal phone / WhatsApp |
| URA EFRIS Support | Uganda Revenue Authority | EFRIS helpdesk: efris@ura.go.ug |
| OAG Uganda | Office of the Auditor General | Formal written notification only |

---

## Part A — Incident Procedures

Incident procedures address conditions that interrupt normal system operation. Each procedure states the symptoms, diagnosis steps, resolution steps, and escalation path.

---

## INC-001: EFRIS Submission Failure

<!-- [CONTEXT-GAP: GAP-001] URA EFRIS API sandbox credentials have not been obtained. This procedure is based on EFRIS system-to-system REST API behaviour. Steps referencing EFRIS error codes must be verified against the URA EFRIS Technical Integration Guide once GAP-001 is resolved. -->

### Symptoms

- An invoice or POS receipt shows status **EFRIS: Pending** or **EFRIS: Failed** in the transaction list.
- The Finance Manager receives an automated email alert: "EFRIS submission failed after 3 retries."
- The transaction does not show a Fiscal Document Number (FDN) or QR code.

### Diagnosis

1. Navigate to **Admin > Integrations > EFRIS > Submission Queue**.
2. Locate the failed submission — note the error message and HTTP response code.
3. Common error codes and their meanings:

| HTTP Code | EFRIS Error | Likely Cause |
|---|---|---|
| 401 | Authentication failure | EFRIS certificate expired or credentials changed |
| 400 | Invalid payload | Invoice data fails URA validation (e.g., missing TIN, invalid item code) |
| 503 | Service unavailable | URA EFRIS system is down or under maintenance |
| 408 | Request timeout | Network connectivity to URA EFRIS endpoint lost |

4. Check internet connectivity from the server:

```bash
curl -I https://efris.ura.go.ug
```

Expected: `HTTP/2 200`. If the command fails or returns an error, the problem is network connectivity.

5. Check the application error log:

```bash
sudo tail -n 100 /var/log/apache2/birdc-erp-error.log
```

### Resolution Steps

**Case A — Network connectivity failure (HTTP 408 or `curl` fails):**

1. Verify the server's internet connection:

```bash
ping -c 4 8.8.8.8
```

2. If the server has no internet: contact BIRDC IT to restore the internet connection.
3. Once connectivity is restored, navigate to **Admin > Integrations > EFRIS > Submission Queue**.
4. Select all failed submissions and click **Retry All**.
5. Monitor the queue for 5 minutes — all items must move to **Submitted** status.

**Case B — Authentication failure (HTTP 401):**

1. **ESCALATE** to Peter Bamuhigire immediately.
2. Do not post any further invoices until the EFRIS credentials are verified.
3. Peter Bamuhigire will: verify the certificate expiry date, renew the certificate if expired (see Maintenance Procedure MNT-005), and update the `.env` file with new credentials.

**Case C — URA EFRIS system down (HTTP 503):**

1. Navigate to the URA EFRIS status page or call URA EFRIS support: efris@ura.go.ug.
2. Continue posting invoices — the system queues failed submissions automatically.
3. Once URA confirms the system is restored, retry all queued submissions from **Admin > Integrations > EFRIS > Submission Queue**.

**Case D — Invalid payload (HTTP 400):**

1. **ESCALATE** to Peter Bamuhigire.
2. Do not retry the submission until the payload error is investigated — retrying invalid data will not succeed and will clutter the queue.

### Escalation to URA

If EFRIS is unavailable for more than 4 hours during business hours:

1. Send a formal email to URA EFRIS support at efris@ura.go.ug stating: BIRDC TIN, description of the error, and time of first failure.
2. Request a URA incident reference number and record it in the BIRDC IT incident log.
3. Notify the Finance Director that EFRIS is unavailable — invoices can still be posted but will not have FDNs until EFRIS is restored.

---

## INC-002: Android App Sync Failure

### Symptoms

- A field agent or field officer reports: transactions entered offline on the Android app have not appeared in the ERP system after reconnecting to Wi-Fi or mobile data.
- The Android app shows a sync error notification or a sync status indicator that has not updated.

### Diagnosis

1. Ask the user to open the app and navigate to **Settings > Sync Status**.
2. Note the last successful sync timestamp and the error message (if displayed).
3. Common sync failure causes:

| Cause | Indicator |
|---|---|
| No internet on the device | Sync status shows "No connection" |
| JWT access token expired | Sync error: "Authentication failed" or HTTP 401 |
| Server unreachable from the internet | Sync error: "Server error" or HTTP 503 |
| Local database conflict | Sync error: "Conflict detected" |

4. From the ERP admin panel, navigate to **Admin > Mobile Sync Log** and search for the device's user account — review the last sync attempt and any error detail.

### Resolution Steps

**Case A — No internet on device:**

1. Ask the user to connect to a Wi-Fi network or confirm mobile data is enabled.
2. In the app, navigate to **Settings > Sync** and tap **Sync Now**.
3. Verify the sync completes within 60 seconds and the sync status updates to the current timestamp.

**Case B — Authentication failure (JWT expired or revoked):**

1. Ask the user to log out of the app completely.
2. Log back in with their credentials.
3. The login process issues a new JWT access token and refresh token.
4. Tap **Sync Now** after login.

**Case C — Server unreachable:**

1. Verify the BIRDC ERP server is running:

```bash
sudo systemctl status apache2
sudo systemctl status php8.3-fpm
sudo systemctl status mysql
```

2. All 3 services must show `active (running)`. If any is stopped, start it:

```bash
sudo systemctl start <service-name>
```

3. Once the server is confirmed running, ask the user to retry the sync.

### Force Sync Procedure

If the standard sync does not resolve the issue:

1. In the app, navigate to **Settings > Advanced > Force Full Sync**.
2. This discards the local sync delta and re-downloads the server state.
3. Warn the user: any data entered offline that has not been marked as synced will be included in the force sync — it will not be lost.

### Data Recovery

If the user suspects offline transactions are missing after sync:

1. Navigate to **Admin > Mobile Sync Log > [username] > Offline Transactions**.
2. The system records every offline transaction with its local timestamp and sync status.
3. If a transaction shows **Synced** status, it is in the database — search the relevant module (Sales, Farmer Delivery) by date and user.
4. If a transaction shows **Sync Failed** status, **ESCALATE** to Peter Bamuhigire for manual data recovery from the device's Room (SQLite) database.

---

## INC-003: Database Connection Failure

### Symptoms

- The web application displays an error page containing: "Database connection failed", "SQLSTATE", or "Can't connect to MySQL server."
- All users are unable to log in or load any page beyond the login screen.
- Android app sync fails with a server error.

### Diagnosis

1. Verify MySQL is running:

```bash
sudo systemctl status mysql
```

If the status shows `failed` or `inactive`, proceed to Resolution Steps Case A.

2. If MySQL is running, verify the application can connect:

```bash
mysql -u birdc_app -p -h 127.0.0.1 birdc_erp -e "SELECT 1;"
```

If this fails with an access denied error, the database user credentials may have changed — proceed to Case B.

3. Check MySQL error log for crash details:

```bash
sudo tail -n 50 /var/log/mysql/error.log
```

4. Check disk space — a full disk will prevent MySQL from writing:

```bash
df -h
```

If the volume hosting MySQL data is at 100% capacity, proceed to Case C.

### Resolution Steps

**Case A — MySQL service stopped:**

1. Restart MySQL:

```bash
sudo systemctl restart mysql
sudo systemctl status mysql
```

2. If MySQL restarts successfully, test the web application within 30 seconds.
3. If MySQL fails to restart, review `/var/log/mysql/error.log` for a specific crash reason.
4. **ESCALATE** to Peter Bamuhigire if MySQL cannot be restarted within 5 minutes.

**Case B — Database user authentication failure:**

1. Log in to MySQL as root:

```bash
sudo mysql -u root -p
```

2. Reset the application user's password:

```sql
ALTER USER 'birdc_app'@'localhost' IDENTIFIED BY '<new-strong-password>';
FLUSH PRIVILEGES;
EXIT;
```

3. Update the `.env` file with the new password and restart PHP-FPM:

```bash
sudo systemctl restart php8.3-fpm
```

**Case C — Disk full:**

1. **ESCALATE** to Peter Bamuhigire immediately.
2. Do not attempt to delete files without guidance — deleting the wrong files can corrupt the MySQL data directory.
3. As a temporary measure, identify the largest log files:

```bash
sudo du -sh /var/log/* | sort -rh | head -20
```

4. Peter Bamuhigire will direct which log files can safely be cleared or rotated.

---

## INC-004: MTN MoMo / Airtel Money Bulk Payment Failure

### Symptoms

- A farmer payment batch or casual worker salary batch shows status **Payment Failed** or **Partially Paid**.
- The Finance Director receives an automated alert: "Bulk payment batch [Batch ID] failed."
- Individual payment lines show error codes from the MTN MoMo or Airtel Money API.

### Diagnosis

1. Navigate to **Finance > Payments > Bulk Payment Batches** and open the failed batch.
2. Review the status column for each payment line — note which lines failed and their error codes.
3. Common MTN MoMo API error codes:

| Error Code | Meaning |
|---|---|
| `PAYER_NOT_FOUND` | The mobile number is not registered on MTN MoMo |
| `NOT_ENOUGH_FUNDS` | The BIRDC MoMo business account has insufficient balance |
| `INTERNAL_PROCESSING_ERROR` | MTN MoMo system error — retry |
| `APPROVAL_REJECTED` | The BIRDC authorised approver rejected the batch in the MoMo portal |

4. Check the BIRDC MTN MoMo business account balance in the MTN Business Portal.

### Resolution Steps

**Case A — Insufficient funds in MoMo account:**

1. Notify the Finance Director immediately.
2. Do not retry the batch until the MoMo account is topped up.
3. Finance Director authorises a top-up via the bank or BIRDC cashier.
4. Once the balance is confirmed, retry the failed payment lines from **Finance > Payments > Bulk Payment Batches > [Batch ID] > Retry Failed**.

**Case B — Invalid mobile numbers (`PAYER_NOT_FOUND`):**

1. Export the failed payment lines to Excel.
2. Contact the relevant field officer or farmer coordinator to obtain the correct mobile numbers.
3. Update the farmer or employee records in the system.
4. Create a new payment batch for the corrected numbers — do not retry the original batch line with the incorrect number.

**Case C — Manual payment fallback (when API is fully unavailable):**

If the MTN MoMo API is unavailable and farmers are waiting for payment:

1. **ESCALATE** to Finance Director and Peter Bamuhigire.
2. Generate the payment list from **Finance > Payments > Bulk Payment Batches > [Batch ID] > Export to Excel**.
3. Finance Director authorises manual bank transfer or cash payment for urgent cases.
4. Record each manual payment in the system under **Finance > Payments > Manual Payment** — this preserves the audit trail.
5. When the API is restored, mark the manually paid lines as **Paid — Manual Override** in the batch, with a note referencing the manual payment record.

---

## INC-005: Payroll Calculation Discrepancy Discovered Post-Approval

### Symptoms

- After a payroll has been approved, a calculation error is discovered (wrong PAYE rate, incorrect allowance, missing deduction).
- A staff member reports their payslip shows an incorrect net pay amount.

### Design Constraint

Business Rule **BR-010** enforces payroll immutability: an approved payroll run cannot be edited or deleted. This is required for audit compliance under the Uganda Income Tax Act 7-year retention requirement (Design Covenant DC-003). The payroll journal entry is locked and cannot be reversed by a user.

### Resolution Steps

1. **Do not attempt to edit or delete the approved payroll run.** Any such attempt will be blocked by the system and logged in the audit trail.
2. Navigate to **HR > Payroll > Payroll Runs** and open the affected run.
3. Click **View Discrepancy Report** — enter a description of the error discovered.
4. Notify the Finance Director by phone or WhatsApp immediately.
5. The Finance Director navigates to **HR > Payroll > Correction Runs** and creates a new correction run:
   - Select the original payroll period.
   - Select only the affected employees.
   - Enter the correction amounts as positive (underpayment) or negative (overpayment) adjustments.
   - Provide a mandatory correction reason that will appear in the audit trail.
6. The correction run goes through the standard payroll approval workflow before it is locked.
7. The correction run's journal entry posts separately to the GL — both the original and the correction are visible in the audit trail.

### Audit Trail Requirements

The system automatically records:

- The user who discovered and logged the discrepancy.
- The Finance Director who authorised the correction run.
- The original payroll run ID and the correction run ID (linked).
- The old and new values for each affected payroll line.

No additional manual audit documentation is required — the system captures all fields automatically.

### Finance Director Notification

Send the Finance Director a written WhatsApp message (for record) stating:

- Payroll period affected.
- Number of employees affected.
- Nature of the error.
- Estimated total correction amount.
- Proposed correction run date.

The Finance Director must acknowledge in writing before the correction run is created.

---

## INC-006: Biometric Device Offline

### Symptoms

- The attendance import job in **HR > Attendance > Import** returns: "Device [device-name] unreachable."
- Employees cannot register their fingerprint attendance at the affected terminal.
- The BIRDC IT Administrator receives an automated alert: "Biometric device [device-name] offline."

### Manual Attendance Fallback Procedure

When a biometric device is offline, revert to manual attendance recording immediately:

1. The HR Supervisor retrieves the paper attendance register for the affected location.
2. All employees at that location sign in and out on the paper register for each shift until the device is restored.
3. The HR Supervisor initials the register at the end of each shift.

Do not allow employees to sign in retroactively after the shift ends — each entry must be made in real time.

### Device Restoration

1. Check the device's power supply — confirm the device is powered on and the display is active.
2. Check the network cable or Wi-Fi connection.
3. From the ERP server, test connectivity:

```bash
ping <zkteco-device-ip>
```

4. If the ping fails, check the BIRDC network switch for the port the device is connected to.
5. If the device is powered and networked but still unreachable, restart the device using the power button.
6. After restart, test connectivity again and verify the connection in **Admin > Integrations > Biometric Devices > [device-name] > Test Connection**.

**ESCALATE** to Peter Bamuhigire if the device cannot be restored within 2 hours.

### Reconciliation When Device Reconnects

1. Once the device is back online, navigate to **HR > Attendance > Import > Manual Reconciliation**.
2. Enter the date range during which the device was offline.
3. Upload the scanned paper attendance register as a PDF (for audit purposes).
4. Manually enter each attendance record from the paper register into the manual entry form.
5. The HR Supervisor and Finance Director both digitally sign the reconciliation record in the system before the period is closed.

---

## INC-007: Duplicate Invoice Number Detected

### Symptoms

- The system displays an alert: "Invoice number [INV-XXXX] already exists."
- A user reports that two invoices appear to share the same number.
- An automated gap/duplicate check (Business Rule **BR-009**) sends an alert to the Finance Director.

### Diagnosis

The system enforces unique invoice numbering via a database unique index. A true duplicate at the database level should be impossible. If the alert fires, the most likely causes are:

1. A manual journal entry or data import bypassed the invoice numbering sequence.
2. A legacy data migration introduced duplicate numbers in the opening balance import.
3. An edge case in the invoice number generator (race condition under high concurrency) — this must be treated as a system defect.

### Investigation Steps

1. Navigate to **Finance > Invoices > Audit > Duplicate Check**.
2. The system generates a duplicate invoice number report — download it.
3. Identify which invoice number is duplicated and the two (or more) records using it.
4. Determine the posting date and user for each record.

### Finance Director Notification

Send the Finance Director a written WhatsApp message immediately stating:

- The duplicate invoice number detected.
- The transaction amounts and dates of both records.
- Whether either invoice has been submitted to EFRIS (check the EFRIS Submission Queue).

The Finance Director must not approve any further invoices or payments referencing the duplicate number until the investigation concludes.

### Audit Log Review

1. Navigate to **Admin > Audit Log** and filter by:
   - Resource type: Invoice
   - Invoice number: [duplicate number]
2. Review every action taken on both records: who created them, when, from which IP address.
3. Export the audit log to PDF and preserve it as an investigation artefact.

### Resolution

1. Determine which invoice record is correct based on supporting documents (delivery notes, purchase orders, contracts).
2. The incorrect invoice must be voided — not deleted — by the Finance Director. A voided invoice remains visible in the audit trail with a **VOID** status and the reason for voiding.
3. **ESCALATE** to Peter Bamuhigire if the duplication cannot be explained by user action — this may indicate a system defect requiring a code fix.

---

## INC-008: GL Hash Chain Integrity Check Failure

### Symptoms

- The system's automated nightly integrity check sends an alert: "GL hash chain integrity check FAILED for [date range]."
- A user running a manual integrity check from **Finance > Audit > Hash Chain Integrity** receives a **CHAIN BROKEN** result.

### Severity

This is a **Critical** incident. A hash chain failure indicates that one or more posted journal entries have been modified outside the application after posting. This is:

- A potential indicator of financial tampering.
- An audit anomaly that must be reported to the Office of the Auditor General (OAG Uganda) if tampering is confirmed.

### Immediate Actions

1. **ESCALATE immediately** to Peter Bamuhigire and the Finance Director by phone — do not send by WhatsApp alone for this incident.
2. Do not post any new journal entries until the investigation is complete. The Finance Director issues a freeze order verbally — this is documented in the incident log.
3. Do not restart MySQL or modify any files. Preserve the current state of the database.
4. Take a full database dump immediately (before any further action):

```bash
mysqldump -u birdc_app -p --single-transaction --routines --triggers \
  birdc_erp | gzip > /backups/incident_$(date +%Y%m%d_%H%M%S).sql.gz
```

### Evidence Preservation

1. Navigate to **Finance > Audit > Hash Chain Integrity > Export Failure Report**.
2. The report identifies: the first transaction in the broken chain, the expected hash, and the actual hash found.
3. Export the full audit log for the affected date range to PDF.
4. Peter Bamuhigire will compare the affected journal entry records against the previous day's database backup to identify which fields were changed.

### Investigation Procedure

Peter Bamuhigire will:

1. Restore the previous day's backup to an isolated test database (not the production database).
2. Compare the affected journal entry records field by field between the test (pre-incident) database and the production database.
3. Identify the specific field(s) that changed and correlate with the MySQL binary log (if enabled) to determine whether the change came from the application or was a direct database modification.

### OAG Notification

If the investigation confirms that a journal entry was modified outside the application:

1. The Finance Director prepares a formal written incident report addressed to the OAG Uganda.
2. The report includes: the transaction ID, the original values, the modified values, the date the modification was detected, the names of all users with database access, and the steps taken to preserve evidence.
3. The report must be submitted within 5 business days of the confirmed tampering finding.
4. Simultaneously, the Finance Director notifies the BIRDC Board of Directors.

---

## Part B — Maintenance Procedures

Maintenance procedures are scheduled, planned activities that keep the system operating correctly. Unlike incident procedures, maintenance procedures are performed at defined intervals by authorised personnel.

---

## MNT-001: Monthly Payroll Close

**Performed by:** HR Manager (payroll preparation) + Finance Director (approval)
**Schedule:** Last working week of each month (recommend Tuesday–Wednesday to allow Thursday for corrections before Friday bank transfer)
**Pre-condition:** All employee attendance records for the month are confirmed and imported from ZKTeco devices.

### Payroll Run Checklist

1. Navigate to **HR > Payroll > New Payroll Run**.
2. Select the payroll period (month and year).
3. Verify the employee count shown matches the active employee headcount — if there is a discrepancy, resolve it before proceeding.
4. Click **Calculate** — the system calculates gross pay, PAYE, NSSF, LST, and all deductions for every employee.
5. Review the **Payroll Summary** — check that:
   - Total gross pay is within 5% of the previous month's total (flag larger variances for review).
   - PAYE total is consistent with the employee count and salary distribution.
   - No employee shows a negative net pay (this indicates a deduction configuration error).
6. Spot-check at least 3 employees' payslip calculations manually against their contract salary and deduction records.
7. If corrections are needed, adjust employee records or deduction configurations — do not proceed to approval until the calculation is correct.

### Approval

8. Navigate to **HR > Payroll > [Current Run] > Submit for Approval**.
9. The Finance Director receives an email notification.
10. The Finance Director logs in, reviews the payroll summary, and clicks **Approve** — this locks the payroll run under BR-010 immutability.

### GL Posting

11. After approval, navigate to **HR > Payroll > [Approved Run] > Post to GL**.
12. Verify the GL posting creates the correct debit entries (Salaries Expense accounts) and credit entries (PAYE Payable, NSSF Payable, Net Salaries Payable).
13. Confirm the journal entry appears in the General Ledger with the correct posting date.

### Bank File Generation

14. Navigate to **HR > Payroll > [Approved Run] > Export Bank Transfer File**.
15. The system generates the bank credit transfer file in the format required by BIRDC's bank. [CONTEXT-GAP: GAP-006]
16. The Finance Director downloads the file and submits it to the bank via the bank's internet banking portal.
17. Retain a copy of the bank submission confirmation in **HR > Payroll > [Approved Run] > Bank Submission Documents**.

### NSSF Schedule Export

18. Navigate to **HR > Payroll > [Approved Run] > Export NSSF Schedule**.
19. The system generates the NSSF contribution schedule in the format required by NSSF Uganda. [CONTEXT-GAP: GAP-009]
20. Submit the schedule and payment to NSSF Uganda by the statutory deadline (15th of the following month).
21. Upload the NSSF submission confirmation receipt to **HR > Payroll > [Approved Run] > NSSF Submission Documents**.

### Payslip Delivery

22. Navigate to **HR > Payroll > [Approved Run] > Distribute Payslips**.
23. The system sends payslips to each employee via:
   - Email (for staff with registered email addresses), and
   - HR Self-Service App (visible in the app's Payslips section).
24. For staff without email or smartphone access, print payslips from **HR > Payroll > [Approved Run] > Print Payslips** and distribute physically.

---

## MNT-002: PAYE Tax Band Update

**Triggered by:** URA publishing new PAYE tax bands (typically following the annual Uganda budget, June each year)
**Performed by:** Finance Director
**Pre-condition:** URA has published the new tax bands in the Official Gazette or via formal URA communication. Do not update rates based on media reports alone.

1. Obtain the official URA PAYE tax band schedule from the Uganda Gazette or the URA website.
2. Log in to the ERP as Finance Director.
3. Navigate to **HR > Payroll Configuration > PAYE Tax Bands**.
4. Click **Add New Band Set** — enter the effective date as the first day of the new tax year (typically 1 July).
   - Do not edit the existing band set — create a new version. The system uses the effective date to determine which band set applies to each payroll run.
5. Enter each income bracket and its applicable tax rate from the official URA schedule.
6. Click **Save Draft** — do not activate yet.

### Test Payroll Run

7. Navigate to **HR > Payroll > New Payroll Run > Test Mode**.
8. Select 3–5 representative employees covering different income brackets (low, middle, high earner).
9. Run a test payroll for the new period using the new band set.
10. Manually verify the PAYE calculation for each test employee against the URA tax band schedule:

   $PAYE = \sum_{i} (min(Income, BandMax_i) - BandMin_i) \times Rate_i$

11. If the calculated PAYE matches the manual calculation for all test employees, proceed to activation.
12. If any discrepancy is found, review the band entry for that income bracket and correct it. Repeat the test run.

### Production Implementation

13. Navigate to **HR > Payroll Configuration > PAYE Tax Bands > [New Band Set] > Activate**.
14. Confirm the activation — the new bands are now live for all payroll runs with a period start date on or after the effective date.
15. The old band set remains in the system (read-only) for historical payroll recalculation.

### Audit Trail

The system automatically records:

- The Finance Director user who created and activated the new band set.
- The timestamp of activation.
- The previous band set values and the new band set values.

No additional manual documentation is required.

---

## MNT-003: Database Backup Verification

**Schedule:** First Monday of every month
**Performed by:** IT Administrator
**Purpose:** Confirm that the daily automated backup is restorable and complete. A backup that cannot be restored is not a backup.

1. Identify the most recent backup file:

```bash
ls -lh /backups/birdc-erp/ | tail -5
```

2. Verify the backup file is not corrupted:

```bash
gzip -t /backups/birdc-erp/birdc_erp_<date>.sql.gz && echo "File integrity OK"
```

3. Create a test database (do not use the production database):

```bash
sudo mysql -u root -p -e "CREATE DATABASE birdc_erp_restore_test CHARACTER SET utf8mb4;"
```

4. Restore the backup to the test database:

```bash
zcat /backups/birdc-erp/birdc_erp_<date>.sql.gz | \
  sudo mysql -u root -p birdc_erp_restore_test
```

5. Verify the restore by running a spot-check query:

```bash
sudo mysql -u root -p birdc_erp_restore_test -e "
  SELECT
    (SELECT COUNT(*) FROM journal_entries) AS journal_entry_count,
    (SELECT COUNT(*) FROM users) AS user_count,
    (SELECT COUNT(*) FROM agents) AS agent_count;
"
```

Compare the counts against the production database — they should match (within a few rows for transactions posted since the backup was taken).

6. Drop the test database:

```bash
sudo mysql -u root -p -e "DROP DATABASE birdc_erp_restore_test;"
```

7. Record the result in the BIRDC IT backup log: date of test, backup file tested, restore result (Pass/Fail), record counts.
8. If the restore failed, **ESCALATE** to Peter Bamuhigire immediately — investigate and fix the backup configuration before the next scheduled backup runs.

### Sign-Off

The IT Administrator and Finance Director both sign (physically or digitally) the backup verification log entry. The log is retained for 7 years as part of the audit trail.

---

## MNT-004: ZKTeco Device Maintenance

**Schedule:** Monthly (first Friday of each month)
**Performed by:** IT Administrator

### Attendance Data Import Schedule

Daily attendance import runs automatically via a scheduled task. Verify the import is running:

1. Navigate to **HR > Attendance > Import Log**.
2. Confirm a successful import entry exists for every working day in the current month.
3. If any day shows a missed import, run a manual import for that date:
   - Navigate to **HR > Attendance > Import > Manual > [device] > [date range]**.

### Device Calibration

1. Visit each ZKTeco device physically.
2. Verify the device clock is set to the correct EAT time — compare against the server time:

```bash
date
```

If the device clock has drifted by more than 2 minutes, adjust it in the device's network time settings (NTP server address: point to the BIRDC ERP server or an internet NTP server).

3. Clean the fingerprint sensor with a dry microfibre cloth — do not use cleaning fluids.
4. Test the fingerprint reader with 5 known enrolled employees: each should authenticate within 3 seconds.
5. If any employee's fingerprint fails to authenticate after 3 attempts, re-enrol their fingerprint via **HR > Employees > [employee] > Biometric Enrolment**.

### Battery / Power Check

1. Verify each device is connected to a UPS or surge protector — not directly to a wall outlet.
2. Check the device manufacturer's battery backup (if the device has an internal battery) — replace if battery runtime is less than 30 minutes.
3. Confirm the backup power supply covers the device location in the event of a BIRDC power outage.

### Monthly Report

After completing the device maintenance round, record in the BIRDC IT maintenance log:

- Devices inspected.
- Any devices with clock drift corrected.
- Any fingerprint re-enrolments performed.
- Power backup status for each device.

---

## MNT-005: EFRIS API Credential Rotation

**Triggered by:** EFRIS RSA certificate expiry (URA issues certificates with a defined validity period — check the expiry date in **Admin > Integrations > EFRIS > Certificate Info**)
**Performed by:** IT Administrator with guidance from Peter Bamuhigire
**Pre-condition:** New EFRIS certificate obtained from URA.

### Certificate Renewal

1. Contact URA EFRIS support (efris@ura.go.ug) to initiate the certificate renewal process.
2. URA will provide a new certificate (public key) and instructions for generating a new private key.
3. Generate a new RSA key pair (4096-bit) on the BIRDC ERP server:

```bash
openssl genrsa -out storage/keys/efris_private_new.pem 4096
openssl rsa -in storage/keys/efris_private_new.pem -pubout \
  -out storage/keys/efris_public_new.pem
```

4. Submit the new public key (`efris_public_new.pem`) to URA as part of the certificate renewal request.
5. URA will validate the key and return a signed certificate with a new validity period.

### Test in Sandbox

6. Update the `.env` file to point to the sandbox environment and the new key files:

```
EFRIS_API_URL=https://efrisws-sandbox.ura.go.ug/...
EFRIS_PRIVATE_KEY_PATH=storage/keys/efris_private_new.pem
EFRIS_PUBLIC_KEY_PATH=storage/keys/efris_public_new.pem
```

7. Restart PHP-FPM to load the new environment values:

```bash
sudo systemctl restart php8.3-fpm
```

8. Post a test invoice from the Sales module.
9. Verify the EFRIS submission succeeds in sandbox and returns a valid FDN.

### Production Cut-Over (Zero-Downtime Procedure)

The cut-over must not interrupt active invoicing. Schedule it during a low-activity period (Sunday morning, 06:00–08:00 EAT).

10. At the scheduled cut-over time, update the `.env` file for production:

```
EFRIS_API_URL=https://efris.ura.go.ug/efrisws/ws/taInvoice
EFRIS_PRIVATE_KEY_PATH=storage/keys/efris_private_new.pem
EFRIS_PUBLIC_KEY_PATH=storage/keys/efris_public_new.pem
```

11. Restart PHP-FPM:

```bash
sudo systemctl restart php8.3-fpm
```

12. PHP-FPM restart takes less than 5 seconds — in-flight web requests will complete before the restart. There is no application downtime.
13. Immediately post a test production invoice and verify the FDN is returned.
14. If the test fails, revert `.env` to the old key file paths and restart PHP-FPM:

```bash
# Revert — old keys
EFRIS_PRIVATE_KEY_PATH=storage/keys/efris_private.pem
EFRIS_PUBLIC_KEY_PATH=storage/keys/efris_public.pem
sudo systemctl restart php8.3-fpm
```

15. **ESCALATE** to Peter Bamuhigire if the revert is needed — do not retry the production cut-over without investigation.

16. After successful cut-over, rename the old key files:

```bash
mv storage/keys/efris_private.pem storage/keys/efris_private_expired_$(date +%Y%m%d).pem
mv storage/keys/efris_public.pem storage/keys/efris_public_expired_$(date +%Y%m%d).pem
```

Do not delete old keys — retain them for the 7-year audit trail period.

17. Update **Admin > Integrations > EFRIS > Certificate Info** with the new expiry date.
18. Set a calendar reminder 60 days before the new certificate's expiry date for the next renewal.
