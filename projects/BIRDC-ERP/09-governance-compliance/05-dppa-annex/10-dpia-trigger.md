# Section 10 — DPIA Trigger Assessment (Regulation 12, DPPA Regulations 2021)

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

## 10.1 DPIA Trigger Assessment — Farmer Data Processing

**Processing operation:** Collection and processing of National Identification Number, GPS farm coordinates, farmer photograph, and mobile money number for 6,440+ cooperative farmers during farmer registration, delivery recording, and mobile money payment.

**Trigger analysis:**

| Trigger Criterion (Regulation 12) | Present? | Justification |
|---|---|---|
| Large-scale processing of special personal data (financial information) | Yes | Mobile money numbers (S-tier) and payment amounts (S-tier) collected for 6,440+ farmers |
| Large-scale processing of personal data | Yes | NIN, GPS coordinates, photographs collected for 6,440+ farmers |
| Systematic monitoring of a public space | No | Farm GPS coordinates are property records, not public space monitoring |
| Use of new technologies that affect rights and freedoms | Partial | Bulk mobile money payment API introduces financial data processing at scale |

**Determination:** DPIA REQUIRED.

> [DPIA-REQUIRED: Large-scale processing of special personal data (financial information — mobile money numbers and payment records) and personal data (NIN, GPS coordinates, photographs) for 6,440+ cooperative farmers. Regulation 12, Data Protection and Privacy Regulations 2021.]

**Reference DPIA document:** `DPIA_FarmerData_BIRDC_ERP` — located at `projects/BIRDC-ERP/09-governance-compliance/06-dpia-farmer/`.

---

## 10.2 DPIA Trigger Assessment — Employee Payroll Processing

**Processing operation:** Processing of salary amounts, bank account numbers, mobile money numbers, PAYE deductions, NSSF contributions, and staff loan balances for 150+ employees during monthly payroll.

**Trigger analysis:**

| Trigger Criterion (Regulation 12) | Present? | Justification |
|---|---|---|
| Large-scale processing of special personal data (financial information) | Yes | Salary, bank accounts, mobile money, PAYE, NSSF, LST, staff loans — all S-tier — for 150+ employees |
| Processing involves bulk mobile money salary payment | Yes | Casual worker salaries via MTN MoMo / Airtel Money batch API |

**Determination:** DPIA REQUIRED.

> [DPIA-REQUIRED: Large-scale processing of special personal data (financial information — salary, bank accounts, mobile money numbers, PAYE, NSSF, staff loans) for 150+ employees during payroll. Regulation 12, Data Protection and Privacy Regulations 2021.]

**Reference DPIA document:** `DPIA_EmployeePayroll_BIRDC_ERP` — to be generated before Phase 5 (Payroll module) go-live.

---

## 10.3 Legal Review Requirement

The processing operations identified in Sections 10.1 and 10.2 involve sensitive personal and financial data at scale for a government-linked entity with parliamentary accountability. Qualified Uganda legal counsel must review the full DPPA compliance framework — including lawful basis mapping, consent form drafts, retention schedules, and data processor contract terms — before Phase 3 go-live.

[CONTEXT-GAP: GAP-004] — Uganda DPPA 2019 legal review by qualified counsel not yet commissioned. Required before Phase 3 farmer registration go-live and Phase 5 payroll go-live.
