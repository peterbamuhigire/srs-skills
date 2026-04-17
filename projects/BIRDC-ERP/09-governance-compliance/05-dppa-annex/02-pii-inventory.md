# Section 2 — PII Inventory and Classification

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

> **Uganda-Specific Alert — Special Personal Data**
>
> Under Section 9 of the DPPA 2019, *financial information* is Special personal data (S-tier). This includes mobile money numbers, salary amounts, bank account details, agent commission amounts, staff loan balances, and payment histories. This classification differs from the GDPR, which does not designate financial information as a special category. All S-tier fields in the BIRDC ERP require AES-256-GCM encryption at rest, strict role-based access, and access logging on every read or export.

---

## 2.1 Farmer Data Fields

| Field | Module | Tier | Section 9 / Section 2 Basis | Retention Period |
|---|---|---|---|---|
| Full name | F-010 Farmer & Cooperative Mgmt | P | Identification — Section 2 | Cooperative membership + 7 years |
| National Identification Number (NIN) | F-010 | P | Identification number — Section 2(c) | Cooperative membership + 7 years |
| Contact phone number | F-010 | P | Identification — Section 2 | Cooperative membership + 7 years |
| GPS farm coordinates | F-010 | P | Location / identity data — Section 2 | Cooperative membership + 7 years |
| Farmer photograph | F-010 | P | Identity data — Section 2 | Cooperative membership + 7 years (review after NIN validated) |
| Mobile money number (MTN / Airtel) | F-010, F-007 | **S** | Financial information — Section 9(1) | Cooperative membership + 7 years |
| Delivery history (weights, dates, grades) | F-010, F-009 | N | Cannot identify person in isolation | 7 years (audit trail) |
| Payment amounts per farmer | F-010, F-007 | **S** | Financial information — Section 9(1) | 7 years (Income Tax Act) |
| Cooperative membership number | F-010 | P | Identification — Section 2 | Cooperative membership + 7 years |
| Farmer age / date of birth | F-010 | P | Age / identity — Section 2; Section 8 children safeguard | Cooperative membership + 7 years |

---

## 2.2 Employee Data Fields

| Field | Module | Tier | Section 9 / Section 2 Basis | Retention Period |
|---|---|---|---|---|
| Full name | F-013 HR | P | Identification — Section 2 | Employment + 7 years |
| National Identification Number (NIN) | F-013 HR | P | Identification number — Section 2(c) | Employment + 7 years |
| Home address | F-013 HR | P | Identity data / location — Section 2 | Employment + 7 years |
| Employee photograph | F-013 HR | P | Identity data — Section 2 | Employment + 7 years |
| Salary / gross pay / pay grade | F-014 Payroll | **S** | Financial information — Section 9(1) | Employment + 7 years (Income Tax Act) |
| Payroll deductions (PAYE, NSSF, LST) | F-014 Payroll | **S** | Financial information — Section 9(1) | Employment + 7 years |
| Bank account number | F-014 Payroll | **S** | Financial information — Section 9(1) | Employment + 7 years |
| Mobile money number (MTN / Airtel) | F-014 Payroll | **S** | Financial information — Section 9(1) | Employment + 7 years |
| Staff loan balance | F-013 HR | **S** | Financial information — Section 9(1) | Employment + 7 years |
| Leave records | F-013 HR | P | Personal circumstance — Section 2 | Employment + 7 years |
| Disciplinary records | F-013 HR | P | Personal — Section 2 | Employment + 7 years |
| Biometric fingerprint template | F-013 HR | P | Identity data — Section 2 (NOTE: stored on ZKTeco device ONLY — not in application database) | Duration of employment; deleted from device on exit |

---

## 2.3 Agent Data Fields

| Field | Module | Tier | Section 9 / Section 2 Basis | Retention Period |
|---|---|---|---|---|
| Full name | F-004 Agent Distribution | P | Identification — Section 2 | Engagement + 7 years |
| National Identification Number (NIN) | F-004 | P | Identification number — Section 2(c) | Engagement + 7 years |
| Contact phone number | F-004 | P | Identification — Section 2 | Engagement + 7 years |
| Mobile money number (MTN / Airtel) | F-004 | **S** | Financial information — Section 9(1) | Engagement + 7 years |
| Commission amounts | F-004 | **S** | Financial information — Section 9(1) | Engagement + 7 years |
| Cash balance (agent liability) | F-004 | **S** | Financial information — Section 9(1) | Engagement + 7 years |
| Agent stock balance | F-004 | N | Commercial inventory — not personal financial data | 7 years |

---

## 2.4 Special Personal Data Summary (S-Tier Fields)

The following fields are classified as Special personal data under Section 9 DPPA 2019. Every one requires AES-256-GCM encryption at rest.

| Field | Data Subject | Module |
|---|---|---|
| Mobile money number | Farmer | F-010, F-007 |
| Payment amounts | Farmer | F-010, F-007 |
| Mobile money number | Employee | F-014 |
| Salary / pay grade / deductions | Employee | F-014 |
| Bank account number | Employee | F-014 |
| Staff loan balance | Employee | F-013 |
| Mobile money number | Agent | F-004 |
| Commission amounts | Agent | F-004 |
| Cash balance | Agent | F-004 |

---

## 2.5 Non-Personal Data Confirmation

The following fields are N-tier and are not subject to DPPA consent or security requirements beyond standard practice:

- Product batch weight (kg)
- Production order quantities
- Delivery weight per batch (aggregate)
- Invoice totals (commercial — not linked to individual farmer)
- Warehouse stock balances
- Quality inspection results (aggregate)
