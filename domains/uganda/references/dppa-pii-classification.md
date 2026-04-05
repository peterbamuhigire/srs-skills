# DPPA 2019 — PII Classification Matrix

Use this reference when classifying data fields in any Uganda system. Paste the relevant
rows into the SRS Section 3 data inventory.

---

## Classification Tiers

| Tier | Definition | Encryption | Access Control | Retention |
|---|---|---|---|---|
| **S** — Special Personal Data | Data that relates to: financial information, health status, medical records, religious/philosophical beliefs, political opinions, sexual life (Section 9, DPPA 2019) | AES-256-GCM at rest + TLS 1.3 in transit | Strict — named roles only, logged every access | As long as necessary; de-identify or destroy at expiry |
| **P** — Personal Data | Any data from which a person can be identified: name, NIN, contact details, GPS coordinates, photograph, occupation, age, nationality (Section 2, DPPA 2019) | AES-128+ at rest + TLS 1.3 in transit | Role-based; logged on access and export | As long as necessary; de-identify or destroy at expiry |
| **N** — Non-Personal Data | Data that cannot identify a natural person: anonymised aggregates, product SKUs, batch weights, transaction counts | Standard | Standard | Standard |

---

## Common Uganda ERP Data Fields

| Field | Tier | Rationale | Handling Notes |
|---|---|---|---|
| National Identification Number (NIN) | P | Identification number assigned to person (Section 2(c)) | Encrypt; validate via NIRA if available; mask in display |
| Mobile money number (MTN MoMo, Airtel) | **S** | Financial information (Section 9(1)) | AES-256-GCM; restricted role access; mask in display |
| Salary amount / gross pay | **S** | Financial information (Section 9(1)) | AES-256-GCM; visible only to HR/Finance/employee self |
| Bank account number | **S** | Financial information (Section 9(1)) | AES-256-GCM; restricted to payroll processing roles |
| GPS farm coordinates | P | Location data identifying person's property | Encrypt; access restricted to Procurement/Finance |
| Farmer photograph | P | Identity data | Encrypt at rest; access restricted |
| Employee photograph | P | Identity data | Encrypt at rest |
| Biometric fingerprint template | P | Identity data (ZKTeco) | Never stored in system DB — queried from device only |
| Health status / medical leave record | **S** | Health status (Section 9(1)) | AES-256-GCM; HR Director access only |
| Date of birth | P | Age / identity data | Encrypt |
| Home address | P | Identity data / location | Encrypt |
| Email address | P | Identification | Standard encryption |
| Phone number (personal) | P | Identification | Standard encryption |
| Religious affiliation (if collected) | **S** | Religious beliefs (Section 9(1)) | Do not collect unless operationally necessary |
| Trade union membership | **S** | Political opinion-adjacent (precautionary) | Do not collect unless required |
| Product batch weight | N | Cannot identify person | Standard |
| Invoice total amount (commercial) | N | Business transaction, not personal financial data | Standard |
| Agent commission amount | **S** | Financial information relating to an individual | AES-256-GCM; restricted to Finance/HR |
| Staff loan balance | **S** | Financial information (Section 9(1)) | AES-256-GCM; HR + employee self only |
| LST amount per employee | **S** | Financial information (Section 9(1)) | AES-256-GCM |

---

## Consent Register Schema

Every collection of personal or special personal data must have a corresponding consent record:

| Column | Type | Notes |
|---|---|---|
| `consent_id` | BIGINT UNSIGNED PK | |
| `data_subject_id` | INT | FK to farmer/employee table |
| `data_subject_type` | ENUM('farmer','employee','agent') | |
| `purpose` | VARCHAR(255) | Specific purpose stated at collection |
| `legal_basis` | ENUM('consent','legal_obligation','public_duty','contract','medical','security') | Section 7 basis |
| `data_categories` | JSON | List of data fields collected |
| `consent_given_at` | DATETIME | UTC timestamp |
| `consent_given_by` | INT | User ID of collector |
| `consent_withdrawn_at` | DATETIME NULL | If withdrawn |
| `withdrawal_method` | VARCHAR(100) NULL | How withdrawal was received |

---

## Data Subject Rights Request Schema

| Column | Type | Notes |
|---|---|---|
| `request_id` | BIGINT UNSIGNED PK | |
| `data_subject_id` | INT | |
| `request_type` | ENUM('access','rectification','erasure','objection') | Section 14–16 |
| `submitted_at` | DATETIME | UTC |
| `due_at` | DATETIME | submitted_at + 30 days |
| `status` | ENUM('pending','complied','rejected','escalated') | |
| `responded_at` | DATETIME NULL | |
| `response_notes` | TEXT NULL | Written rejection reason if status = rejected |
| `handled_by` | INT NULL | DPO user ID |

---

## Data Breach Notification Template (Section 23 + Regulation 33)

When generating a breach notification for PDPO, the system shall populate:

1. **Nature of breach** — describe the type of unauthorised access/acquisition
2. **Data involved** — categories of personal data affected (with tier: S/P/N)
3. **Approximate number of data subjects affected**
4. **Likely consequences** — risk level to affected individuals
5. **Remedial measures taken** — actions already implemented to contain the breach
6. **Remedial measures proposed** — actions planned
7. **DPO contact details** — name, email, phone
8. **Notification timestamp** — must be immediate (no 72-hour window)

PDPO contact: Personal Data Protection Office, National Information Technology Authority – Uganda (NITA-U), Kampala.
