# Section 9 — DPO and PDPO Registration Requirements (Section 6, Regulations 15–16, 47)

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

## 9.1 DPO Designation Record

### FR-DPPA-027 — DPO Designation Storage

The system shall store the DPO designation record in the system administration configuration. The designation record shall include:

| Field | Requirement |
|---|---|
| DPO full name | Mandatory |
| DPO role / title | Mandatory |
| DPO email address | Mandatory |
| DPO phone number | Mandatory |
| Date of designation | Mandatory |
| Appointing authority | Record of BIRDC Director designation |

Per Section 6 DPPA 2019 and Regulation 47, the head of every institution must designate a DPO. The DPO designation record is the system's evidence of compliance with this requirement.

### FR-DPPA-028 — DPO Configuration Warning

When any user accesses the system administration panel and no DPO designation record is stored, the system shall display: "No Data Protection Officer is designated. Designate a DPO and enter their details in System Administration before processing any farmer or employee personal data. This is required under Section 6, DPPA 2019."

---

## 9.2 PDPO Registration

### FR-DPPA-029 — PDPO Registration Number Storage

The system shall store the PDPO registration number and registration date in the system administration configuration. The PDPO registration number is issued upon registration in the PDPO Data Protection Register (Section 29 DPPA 2019; Regulations 15–16 — PDPO Form 2).

### FR-DPPA-030 — PDPO Registration Warning

When the system is accessed and no PDPO registration number is configured, the system shall display a persistent banner on the administration dashboard: "PDPO registration number not configured — register with the Personal Data Protection Office at NITA-U, Kampala before processing farmer personal data. Registration is required under Section 29, DPPA 2019."

This warning shall also appear on the Farmer Delivery App when a Collections Officer attempts to register a new farmer.

---

## 9.3 DPO Dashboard

### FR-DPPA-031 — DPO Dashboard Consolidated View

The DPO role shall have access to a dedicated DPO Compliance Dashboard displaying the following widgets simultaneously:

1. **Overdue Rights Requests:** Count of data subject rights requests (access, rectification, erasure, objection) where `due_at < NOW()` and `status = 'pending'`. Red badge if count > 0.
2. **Pending Consent Records:** Count of farmer, employee, and agent records where consent record is missing or withdrawn.
3. **Active Breach Events:** Count of breach events where `classified_as IN ('confirmed', 'under_investigation')` and `closed_at IS NULL`. Red badge if count > 0.
4. **Retention Expiry Alerts:** Count of data subject records with retention expiry within 90 days.
5. **Processor Contract Status:** Status of data processor contracts (MTN MoMo, Airtel, Africa's Talking) — Executed / Pending / Not Configured.
6. **PDPO Registration Status:** Registered / Not Registered.
7. **DPO Designation Status:** Designated / Not Designated.

**Stimulus:** DPO user logs in and navigates to the DPO Compliance Dashboard.
**Response:** System queries all relevant tables and displays current counts and statuses. Dashboard refreshes automatically every 5 minutes.
