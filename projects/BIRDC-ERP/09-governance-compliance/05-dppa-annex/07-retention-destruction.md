# Section 7 — Retention and Destruction Schedule (Section 18, DPPA 2019)

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

## 7.1 Retention Schedule

| Data Category | Data Subjects | Retention Period | Legal Basis for Retention |
|---|---|---|---|
| Farmer personal data (name, NIN, GPS, photo, phone, mobile money number) | Cooperative farmers | Duration of cooperative membership + 7 years from last payment | Income Tax Act Cap 340 — 7-year financial record retention |
| Farmer payment records (amounts, dates) | Cooperative farmers | 7 years from payment date | Income Tax Act Cap 340; PPDA cooperative procurement audit trail |
| Farmer delivery records (weights, grades, dates) | Cooperative farmers | 7 years | PPDA cooperative procurement audit trail |
| Employee personal data (name, NIN, address, photo, phone) | All employees | Duration of employment + 7 years | Income Tax Act Cap 340; NSSF Act |
| Employee payroll records (salary, deductions, PAYE, NSSF) | All employees | Duration of employment + 7 years | Income Tax Act Cap 340 — PAYE records; NSSF Act |
| Employee bank account and mobile money numbers | All employees | Duration of employment + 7 years | Income Tax Act — payment records |
| Employee leave and disciplinary records | All employees | Duration of employment + 7 years | Employment Act obligations |
| Staff loan records | All employees | Duration of employment + 7 years | Financial obligation records |
| Biometric fingerprint template (ZKTeco device) | All employees | Duration of employment | Not stored in application DB — deleted from ZKTeco device on exit |
| Agent personal data (name, NIN, phone, mobile money) | Field agents | Duration of engagement + 7 years | Income Tax Act — WHT on commissions |
| Agent commission and cash balance records | Field agents | Duration of engagement + 7 years | Income Tax Act — commission income records |
| Consent records | Farmers, employees, agents | 7 years after data subject relationship ends | DPPA 2019 accountability principle — Section 3 |
| Data subject rights request records | All | 7 years | DPPA 2019 accountability — audit evidence |
| Breach notification records | N/A | 10 years | PDPO audit trail; criminal liability period |

---

## 7.2 Automated Expiry Alerts

### FR-DPPA-019 — DPO Retention Expiry Alert

The system shall calculate the retention expiry date for each data subject's personal data record. When a data subject's retention expiry is within 90 calendar days, the system shall generate an alert on the DPO dashboard listing: data subject name (or ID if anonymised), data subject type (farmer / employee / agent), data categories affected, expiry date, and recommended action (de-identify or review retention extension justification).

**Stimulus:** System daily background job identifies data subjects with retention expiry within 90 days.
**Response:** System creates pending DPO alert items. DPO dashboard displays count of upcoming expirations with earliest expiry date.

---

## 7.3 Destruction Method

### FR-DPPA-020 — De-identification on Retention Expiry

When a data subject's retention period expires and no legal extension applies, the system shall de-identify all P-tier and S-tier fields for that data subject using the following method:

| Field | De-identification Action |
|---|---|
| Full name | Set to `[ANONYMISED-{farmer/employee/agent_id}]` |
| NIN | Set to NULL |
| GPS farm coordinates | Set to NULL |
| Photograph | Delete file reference; set field to NULL |
| Contact phone | Set to NULL |
| Mobile money number | Set to NULL |
| Bank account number | Set to NULL |
| Home address | Set to NULL |
| Email address | Set to NULL |

Financial transaction amounts (payment totals, salary totals) shall be retained as N-tier aggregate records with the anonymised subject reference. These records cannot be destroyed during the 7-year window. After the 7-year window, they may be destroyed or retained in permanently anonymised form for statistical purposes (Section 17 DPPA 2019).

### FR-DPPA-021 — Destruction Audit Log

When de-identification is executed, the system shall create an immutable audit log record: data subject ID (anonymised form), data categories de-identified, de-identification timestamp, DPO user ID who authorised the action, and confirmation that no intelligible reconstruction is possible.

---

## 7.4 Biometric Data Destruction

### FR-DPPA-022 — Biometric Template Deletion on Employee Exit

When an employee's exit clearance is completed in the HR module, the system shall display a mandatory checklist item: "Delete biometric fingerprint template from ZKTeco device for [Employee Name]." The IT Administrator shall confirm this action is complete before the exit clearance is marked as finalised. The system shall record: employee ID, device ID, deletion confirmation timestamp, IT Administrator user ID.

*The biometric fingerprint template is stored on the ZKTeco device only and is not held in the application database. This requirement ensures the device record is deleted on exit.*

---

## 7.5 Financial Records — Destruction Restriction

Financial records (payment amounts, salary amounts, commission amounts, tax deduction records) that are within the 7-year retention window under the Uganda Income Tax Act Cap 340 and the Uganda Companies Act **cannot be de-identified or destroyed**. The system shall block any erasure request that targets these records during the retention window and display the retention restriction notice (see **FR-DPPA-015**).
