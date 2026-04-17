# Section 6 — Security and Technical Measures (Section 20, DPPA 2019)

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

## 6.1 Encryption at Rest — S-Tier Fields

### NFR-DPPA-001 — AES-256-GCM for Special Personal Data at Rest

The system shall encrypt all S-tier fields at rest using AES-256-GCM. Encryption shall be applied at the application layer before data is written to the database. S-tier fields subject to this requirement:

| Field | Table | Subject |
|---|---|---|
| Mobile money number | `tbl_farmers` | Farmer |
| Payment amounts (per farmer) | `tbl_farmer_payments` | Farmer |
| Mobile money number | `tbl_employees` | Employee |
| Salary / gross pay / pay grade | `tbl_payroll` | Employee |
| Payroll deductions (PAYE, NSSF, LST) | `tbl_payroll` | Employee |
| Bank account number | `tbl_employees` | Employee |
| Staff loan balance | `tbl_staff_loans` | Employee |
| Mobile money number | `tbl_agents` | Agent |
| Commission amounts | `tbl_agent_commissions` | Agent |
| Cash balance | `tbl_agent_cash_balance` | Agent |

*Encryption keys are generated and held by BIRDC IT. Keys are not held by any vendor or cloud provider. Key rotation procedure documented in the System Administration Guide.*

### NFR-DPPA-002 — AES-128+ for Personal Data at Rest

The system shall encrypt all P-tier fields at rest using AES-128-GCM or stronger. P-tier fields subject to this requirement: NIN (farmer, employee, agent), GPS farm coordinates, farmer photograph, employee photograph, home address, contact phone numbers, leave records, disciplinary records.

---

## 6.2 Encryption in Transit

### NFR-DPPA-003 — TLS 1.3 for All Data in Transit

All API communication between the web application and the server, between the Android mobile applications and the server, between the server and external APIs (MTN MoMo, Airtel Money, Africa's Talking, URA EFRIS, NIRA), and all web sessions shall use TLS 1.3 or higher. TLS 1.0 and TLS 1.1 are prohibited. TLS 1.2 is permitted only if TLS 1.3 is not supported by the external API endpoint.

---

## 6.3 Role-Based Access Control for S-Tier Fields

### NFR-DPPA-004 — Named Role Restriction for Special Personal Data

The system shall restrict visibility and export of S-tier fields to the following named roles only:

| S-Tier Field | Authorised Roles |
|---|---|
| Farmer mobile money number | Payroll Officer, Finance Director, IT Administrator |
| Farmer payment amounts | Payroll Officer, Finance Director, Procurement Manager, IT Administrator |
| Employee salary / deductions | HR Manager, Payroll Officer, Finance Director, IT Administrator, Employee Self (own record only) |
| Employee bank account number | Payroll Officer, Finance Director, IT Administrator |
| Employee mobile money number | Payroll Officer, Finance Director, IT Administrator |
| Staff loan balance | HR Manager, Finance Director, IT Administrator, Employee Self (own record only) |
| Agent mobile money number | Finance Director, IT Administrator |
| Agent commission amounts | Finance Director, Sales Manager, IT Administrator, Agent Self (own record only) |
| Agent cash balance | Finance Director, Sales Manager, IT Administrator |

All other roles shall see these fields masked (e.g., `MTN: ****4567`).

### NFR-DPPA-005 — S-Tier Field Access Logging

Every read, display, export, or API transmission of an S-tier field shall be logged in `tbl_audit_log` with: user ID, role, action (`READ` / `EXPORT` / `DECRYPT`), field name, data subject ID, timestamp. This log is immutable and is included in the GL hash chain audit trail.

---

## 6.4 Risk Management Cycle (Section 20)

### NFR-DPPA-006 — Security Risk Review

BIRDC IT shall conduct a formal review of foreseeable security risks to personal data at least annually, or whenever a new integration, module, or data category is added. Risk review findings shall be recorded in the system's administration documentation. Safeguards established in response to identified risks shall be verified for effectiveness within 60 days of implementation.

---

## 6.5 Data Processor Contracts (Section 21)

### NFR-DPPA-007 — Written Data Processor Contracts

BIRDC shall execute written data processor contracts with each of the following processors before any personal data is transmitted to their systems:

| Processor | Data Transmitted | Required Contract Clauses |
|---|---|---|
| MTN Uganda (MTN MoMo API) | Farmer and employee mobile money numbers, payment amounts | Confidentiality, AES-256 in transit, no secondary use, data deletion on contract end |
| Airtel Uganda (Airtel Money API) | Farmer and employee mobile money numbers, payment amounts | Same as MTN |
| Africa's Talking (SMS API) | Farmer and employee phone numbers, SMS content | Confidentiality, no secondary use, data deletion on contract end |

*Note: These contracts cannot be executed until API credentials are obtained.* [CONTEXT-GAP: GAP-002] [CONTEXT-GAP: GAP-003]

The system shall not transmit personal data to any data processor until the corresponding contract record is marked as executed in the system administration configuration.

### NFR-DPPA-008 — Processor Contract Configuration Check

When any scheduled bulk payment run is initiated (farmer payments, payroll), the system shall verify that a data processor contract record is marked as executed for the target payment provider. If no executed contract is on file, the system shall block the payment run and display: "Data processor contract for [Provider] is not executed — payment cannot proceed. Contact the DPO."

---

## 6.6 Encryption Key Management

### NFR-DPPA-009 — BIRDC-Held Encryption Keys

All encryption keys for S-tier and P-tier field encryption shall be generated by BIRDC IT and stored in a key management configuration accessible only to the IT Administrator role. Keys shall not be stored in the application database. Keys shall not be transmitted to any vendor or cloud service. Key backup procedure shall be documented and tested annually.
