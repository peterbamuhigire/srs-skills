# 6. Non-Functional Requirements

All non-functional requirements comply with DC-001 through DC-007 and are expressed with measurable thresholds per IEEE 982.1 and the BIRDC ERP Prohibition on Vague Adjectives.

---

## 6.1 Performance

**NFR-PRO-001** — The PR approval workflow transition (from "Submit" click to updated status confirmation on screen) shall complete within 2 seconds at P95 under normal load, defined as up to 50 concurrent web ERP users.

**NFR-PRO-002** — The farmer lookup by name or registration number in the web ERP (across 6,440+ farmer records) shall return results within 1 second at P95.

**NFR-PRO-003** — The Stage 3 farmer contribution breakdown screen shall support data entry for up to 200 individual farmer contributions per batch without pagination reload; each contribution save shall confirm within 1 second.

**NFR-PRO-004** — The batch audit trail report (FR-PRO-059) shall generate a PDF of a complete batch record (Stages 1–5) within 5 seconds at P95.

**NFR-FAR-001** — The Farmer Delivery App farmer search (against locally cached farmer database of up to 3,000 records per officer's assigned cooperatives) shall return results within 0.5 seconds on Android 8.0 hardware.

**NFR-FAR-002** — The Farmer Delivery App shall sync a full day's collection records (up to 500 delivery records and 50 new farmer registrations) to the server within 3 minutes on a 3G connection (minimum 1 Mbps upload).

**NFR-FAR-003** — The bulk mobile money payment submission for up to 500 farmers shall complete API submission within 10 minutes, processing records in batches per the API provider's rate limit specifications. [CONTEXT-GAP: GAP-002 — MTN MoMo API rate limits to be confirmed]

---

## 6.2 Security

**NFR-SEC-001** — All API endpoints for F-009 and F-010 shall enforce the 8-layer authorisation model (Role → Page → API endpoint → UI element → Location → Time → Conditional rules → Object ownership); no procurement or farmer data shall be accessible without a valid session or JWT token.

**NFR-SEC-002** — All farmer personally identifiable information (NIN, phone number, GPS coordinates, photo) shall be encrypted at rest using AES-256 in the server database; field-level encryption keys shall be managed in the application configuration, not in the database.

**NFR-SEC-003** — All mobile money API requests (MTN MoMo, Airtel Money) shall be transmitted over HTTPS/TLS 1.3; API credentials shall be stored in the server `.env` file and shall never appear in application code or logs.

**NFR-SEC-004** — The Farmer Delivery App local Room database shall be encrypted using SQLCipher or equivalent; the encryption key shall not be hardcoded and shall be derived from the officer's authentication credentials.

**NFR-SEC-005** — Every procurement action (PR creation, approval, LPO generation, GRN, GL posting, payment) shall create an immutable audit log entry recording: actor username, actor IP address, action type, affected record ID, timestamp (UTC), and a JSON snapshot of the record before and after the action; these records shall be retained for 7 years per DC-003.

---

## 6.3 Availability

**NFR-AVL-001** — The BIRDC ERP web application shall achieve ≥ 99% uptime during BIRDC's working hours (Monday–Saturday, 07:00–20:00 EAT), measured monthly; planned maintenance windows shall be scheduled outside these hours and communicated at least 24 hours in advance.

**NFR-AVL-002** — The Farmer Delivery App shall function completely offline for a continuous period of up to 7 days without connectivity; all data entered during the offline period shall be preserved in the local Room database and shall not be lost due to app restart or device reboot.

---

## 6.4 Usability

**NFR-USR-001** — The 5-stage cooperative procurement workflow shall be completable by a Procurement Officer (Robert persona) for a single batch of up to 100 farmer contributions within 45 minutes of the batch arriving at the factory gate, including data entry in Stage 3; if this benchmark is not met in user acceptance testing, the UI flow shall be redesigned before go-live (DC-001).

**NFR-USR-002** — A Field Collection Officer (Patrick persona) shall be able to register a new farmer (name, NIN, phone, cooperative, GPS, photo) and record a delivery for that farmer in under 5 minutes using the Farmer Delivery App, per DC-001.

**NFR-USR-003** — All error messages in F-009 and F-010 shall state the specific reason for the error and the corrective action required, in plain English; generic error messages (e.g., "An error occurred") are prohibited.

---

## 6.5 Data Integrity

**NFR-INT-001** — The Stage 3 individual farmer contribution breakdown shall enforce referential integrity: every contribution record must reference a farmer in the farmer registry (tbl_farmers); orphaned contribution records (no matching farmer) are prohibited at the database level via foreign key constraints.

**NFR-INT-002** — The GL auto-posting for Stage 5 (FR-PRO-056) shall be executed as an atomic database transaction; if any part of the GL posting fails, the entire transaction shall be rolled back and the batch status shall remain "Stock Received — Pending GL"; no partial GL postings are permitted.

**NFR-INT-003** — Farmer registration numbers (FMR-NNNNNN) and LPO numbers (LPO-YYYY-NNNN) shall be assigned using database sequences with gap detection per BR-009; any gap in the number series shall generate an automatic alert to the Finance Manager and a log entry in the audit trail.

---

## 6.6 Maintainability and Configurability

**NFR-MNT-001** — All PPDA procurement threshold values, quality grade prices, cooperative levy rates, and transport charge rates shall be stored in configuration tables in the database; the Finance Director or IT Administrator shall be able to update these values through the administration UI without developer involvement, per DC-002; every configuration change shall be logged with the previous value, new value, actor, and timestamp.

**NFR-MNT-002** — The banana variety catalogue, cooperative hierarchy, and quality grade definitions shall be maintainable by the Procurement Manager or Research Coordinator via the web ERP without developer involvement.

**NFR-MNT-003** — The SMS notification templates (FR-FAR-038 through FR-FAR-041, FR-FAR-049) shall be configurable by the IT Administrator via the administration UI; template variables (e.g., `{farmer_name}`, `{batch_number}`, `{amount}`) shall be documented in the template editor.

---

## 6.7 Compliance

**NFR-CMP-001** — All procurement documentation generated by F-009 (PR, RFQ, LPO, GRN, evaluation report, batch audit trail) shall satisfy the documentary requirements of the Uganda PPDA Act and shall be available for PPDA compliance review at any time; the PPDA compliance register (F-016) shall be automatically updated whenever a procurement document is created or status-changed in F-009.

**NFR-CMP-002** — All farmer personal data collected in F-010 shall be processed in compliance with the Uganda Data Protection and Privacy Act 2019; a data processing record documenting the purpose, legal basis, data categories, retention period, and access controls shall be maintained for each category of farmer personal data. [CONTEXT-GAP: GAP-004]
