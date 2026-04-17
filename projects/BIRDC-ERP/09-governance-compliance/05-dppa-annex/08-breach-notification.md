# Section 8 — Data Breach Notification Procedure (Section 23, Regulation 33, DPPA 2019)

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

> *Critical Uganda-GDPR Difference:* Under Section 23 of the DPPA 2019, breach notification to the PDPO is **IMMEDIATE** — there is no 72-hour window as in the GDPR. Additionally, it is the PDPO — not the data controller — who determines whether data subjects must be notified and by what method. BIRDC must not independently notify data subjects of a breach without PDPO direction.

---

## 8.1 Breach Trigger

### FR-DPPA-023 — Breach Detection Trigger

The system shall treat the following events as potential data breach triggers requiring immediate DPO action:

1. Anomalous S-tier field access: a single user accessing S-tier records for more than 50 data subjects within a 1-hour period.
2. Failed authentication attempts: more than 10 consecutive failed login attempts on any account, followed by a successful login.
3. Bulk export of P-tier or S-tier fields from any module by any user who does not hold the Finance Director or IT Administrator role.
4. Any manual report by a staff member of suspected unauthorised access, data loss, or data disclosure.
5. Detection of a new device or IP address accessing the application outside of BIRDC's defined network range.

**Stimulus:** Any of the above trigger conditions is detected.
**Response:** System creates a breach event record in `tbl_breach_events` and immediately displays a red alert on the DPO dashboard. The alert persists until the DPO acknowledges and classifies it.

---

## 8.2 IMMEDIATE PDPO Notification

### FR-DPPA-024 — Breach Notification Form — IMMEDIATE

When the DPO classifies a breach event as confirmed, the system shall immediately generate a PDPO breach notification form pre-populated with:

1. Nature of breach (from DPO's classification notes).
2. Categories of personal data involved (P-tier and S-tier fields affected, with tier designations).
3. Approximate number of data subjects affected.
4. Likely consequences to affected data subjects.
5. Remedial measures already taken.
6. Remedial measures proposed.
7. DPO name, email, and phone number.
8. Notification timestamp (UTC and EAT — East Africa Time, UTC+3).

**Stimulus:** DPO marks a breach event as "Confirmed" on the DPO dashboard.
**Response:** System generates the PDPO notification form within 3 seconds. Form is accessible for printing and PDF export. System records `notified_pdpo_at` timestamp on the breach event record.

The PDPO notification form shall be accessible from the DPO dashboard in 3 clicks or fewer: (1) DPO Dashboard → (2) Breach Events → (3) Generate PDPO Notification Form.

---

## 8.3 PDPO Contact Details

PDPO notifications shall be submitted to:

**Personal Data Protection Office**
National Information Technology Authority — Uganda (NITA-U)
Communications House, 1 Colville Street
Kampala, Uganda

The system shall store the PDPO contact details in the system administration configuration and pre-populate them on all generated notification forms.

---

## 8.4 PDPO-Directed Data Subject Notification

### FR-DPPA-025 — PDPO Direction Recording

After notifying the PDPO, the DPO shall record the PDPO's direction in the breach event record: whether to notify data subjects, the required notification method (registered mail, email, website placement, or mass media publication), the required content, and the deadline given by PDPO.

*Note: BIRDC shall not notify data subjects independently. Data subject notification occurs only if and as directed by the PDPO.*

### FR-DPPA-026 — Data Subject Notification Tracking

If the PDPO directs data subject notification, the system shall allow the DPO to mark individual data subjects as notified, record the notification method and timestamp, and confirm completion of PDPO-directed notification.

---

## 8.5 Breach Event Log Schema

All breach events are stored in `tbl_breach_events`:

| Column | Type | Notes |
|---|---|---|
| `breach_id` | BIGINT UNSIGNED PK | |
| `detected_at` | DATETIME | UTC timestamp of detection or report |
| `nature_of_breach` | TEXT | Description of unauthorised access/acquisition |
| `data_categories_affected` | JSON | List of field names and tiers (S/P) |
| `estimated_data_subjects` | INT | Approximate number of affected individuals |
| `likely_consequences` | TEXT | Risk assessment to individuals |
| `remedial_taken` | TEXT | Actions already implemented |
| `remedial_proposed` | TEXT | Actions planned |
| `dpo_acknowledged_at` | DATETIME NULL | |
| `classified_as` | ENUM('confirmed','false_positive','under_investigation') NULL | |
| `notified_pdpo_at` | DATETIME NULL | IMMEDIATE — no 72-hour window |
| `pdpo_direction` | TEXT NULL | PDPO's instruction |
| `pdpo_direction_received_at` | DATETIME NULL | |
| `data_subjects_notified_at` | DATETIME NULL | Only if directed by PDPO |
| `notification_method` | VARCHAR(100) NULL | registered mail / email / website / mass media |
| `closed_at` | DATETIME NULL | |
| `handled_by` | INT | DPO user ID |
