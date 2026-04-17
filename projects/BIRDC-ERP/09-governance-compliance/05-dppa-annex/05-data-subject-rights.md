# Section 5 — Data Subject Rights (Sections 14–16, DPPA 2019)

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

## 5.1 Right of Access (Section 14)

### FR-DPPA-010 — Farmer Data Access Report

When a farmer (via their cooperative representative) or a farmer's duly authorised agent submits a written data access request, the IT Administrator shall be able to generate a data access report from the system. The report shall list all personal data held for that farmer: name, NIN (masked to last 4 digits), contact phone, GPS coordinates, photograph (thumbnail), mobile money number (masked), delivery history, and payment records.

**Stimulus:** IT Administrator selects a farmer record and triggers "Generate Data Access Report."
**Response:** System compiles and displays all personal data fields held for that farmer. System generates a printable/PDF report. System logs the access request in `tbl_data_subject_requests`.

### FR-DPPA-011 — Employee Self-Service Data Access

When an employee logs into the HR Self-Service App, the system shall display a "My Data" screen showing all personal data held: name, NIN (masked), home address, leave records, payslip history, and loan balance. Employee shall not see other employees' data.

**Stimulus:** Employee selects "My Data" in HR Self-Service App.
**Response:** System displays only that employee's personal data within the same session. No cross-employee data is accessible.

---

## 5.2 Right to Object (Section 15)

### FR-DPPA-012 — Objection Logging

When a data subject (farmer, employee, or agent) submits a written objection to the collection or processing of their personal data, the IT Administrator or DPO shall be able to record the objection in the system. The system shall log: data subject ID, type, objection date, data categories objected to, and grounds stated.

**Stimulus:** DPO selects "Record Objection" for a data subject.
**Response:** System creates a record in `tbl_data_subject_requests` with `request_type = 'objection'`, sets `due_at = submitted_at + 30 days`, and sets status to `'pending'`.

### FR-DPPA-013 — Processing Suspension on Objection

When an objection is recorded for a data subject, the system shall flag that data subject's profile as "objection pending." The system shall prevent new non-essential data collection for that data subject until the DPO resolves the objection. Financial and legal-obligation-basis processing shall continue per Section 7(2) exception. The DPO dashboard shall display the objection as a pending action.

**Stimulus:** Objection flag is set on a data subject.
**Response:** System blocks new consent-basis data entry for that subject. Displays warning to any user attempting data entry: "Data subject objection pending — consult DPO before proceeding." Legal-obligation-basis processes (payment, tax records) continue unaffected.

---

## 5.3 Right to Rectification and Erasure (Section 16)

### FR-DPPA-014 — Rectification Request Workflow

When a data subject submits a rectification request (correct inaccurate, irrelevant, excessive, out-of-date, incomplete, misleading, or unlawfully obtained data), the IT Administrator shall record the request. The system shall set a 30-calendar-day response deadline. The DPO dashboard shall display requests approaching or exceeding the 30-day deadline.

**Stimulus:** IT Administrator records a rectification request.
**Response:** System creates `tbl_data_subject_requests` record with `request_type = 'rectification'` and `due_at = submitted_at + 30 days`.

### FR-DPPA-015 — Erasure with Retention Conflict Check

When an erasure request is received for a data subject, the system shall check whether the data is within the legally mandated 7-year retention window. If within the retention window, the system shall inform the DPO: "Financial records for [Data Subject] cannot be erased until [expiry date] per Income Tax Act Cap 340 and Companies Act 7-year retention obligations." The DPO shall record a written rejection with reasons, which the system shall store and allow the DPO to provide to the data subject.

**Stimulus:** DPO processes an erasure request for a data subject whose financial records are within the 7-year window.
**Response:** System displays retention conflict warning with the earliest eligible erasure date. DPO selects "Record Rejection with Reasons." System stores written rejection and marks request as `'rejected'`.

*Note: The conflict between Section 16 erasure rights and 7-year financial record retention under the Income Tax Act and Companies Act requires resolution by qualified Uganda legal counsel before Phase 3 go-live.* [CONTEXT-GAP: GAP-004]

### FR-DPPA-016 — Erasure Execution for Eligible Records

When a data subject's retention period has expired and an erasure request is submitted (or the automated retention expiry alert fires), the system shall de-identify the data subject's personal data fields: set name to an anonymised token, set NIN to NULL, set GPS coordinates to NULL, set photograph to NULL, set mobile money number to NULL, and set contact phone to NULL. Financial transaction amounts and delivery weights shall remain as N-tier aggregate records with anonymised subject reference.

**Stimulus:** DPO confirms erasure for a data subject whose retention period has expired.
**Response:** System de-identifies all P-tier and S-tier fields. Financial records are retained with anonymised reference. System logs the destruction action in the audit trail with DPO user ID and timestamp.

---

## 5.4 Third-Party Notification After Rectification or Erasure (Section 28(4))

### FR-DPPA-017 — Third-Party Disclosure Log

The system shall maintain a log of all third parties to whom a data subject's personal data has been disclosed (MTN MoMo, Airtel Money, Africa's Talking). When a rectification or erasure is performed, the DPO dashboard shall display a notification task: "Notify third parties of data change for [Data Subject ID]." The DPO shall record the date on which each third party was notified and the method of notification.

---

## 5.5 Data Subject Rights Request Log Schema

All data subject rights requests are stored in `tbl_data_subject_requests`:

| Column | Type | Notes |
|---|---|---|
| `request_id` | BIGINT UNSIGNED PK | Auto-increment |
| `data_subject_id` | INT | FK to farmer / employee / agent table |
| `data_subject_type` | ENUM('farmer','employee','agent') | |
| `request_type` | ENUM('access','rectification','erasure','objection') | Sections 14–16 |
| `submitted_at` | DATETIME | UTC |
| `due_at` | DATETIME | `submitted_at + 30 days` |
| `status` | ENUM('pending','complied','rejected','escalated') | |
| `responded_at` | DATETIME NULL | |
| `response_notes` | TEXT NULL | Written rejection reason if rejected |
| `handled_by` | INT NULL | DPO user ID |
| `third_party_notified_at` | DATETIME NULL | Section 28(4) notification timestamp |

---

## 5.6 DPO Dashboard — Overdue Rights Requests

### FR-DPPA-018 — DPO Overdue Requests Alert

When the DPO logs into the system, the DPO dashboard shall display all data subject rights requests where `due_at < NOW()` and `status = 'pending'`. Each overdue item shall show: data subject ID, type, request type, days overdue, and a direct link to the request record. The dashboard shall display a count of overdue requests with a red indicator if the count is greater than 0.

**Stimulus:** DPO loads the dashboard.
**Response:** System queries `tbl_data_subject_requests` where `due_at < NOW()` and `status = 'pending'` and displays results sorted by `due_at ASC`.
