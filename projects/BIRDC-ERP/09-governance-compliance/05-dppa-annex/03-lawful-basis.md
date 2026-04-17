# Section 3 — Lawful Basis Mapping (Section 7, DPPA 2019)

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

## 3.1 Farmer Data — Lawful Basis

| Data Field | Tier | Lawful Basis (Section 7) | Specific Legal Ground |
|---|---|---|---|
| Full name | P | Consent + Legal obligation | Consent at farmer registration; legal obligation under cooperative procurement records requirements |
| NIN | P | Consent + Legal obligation | Consent at registration; NIRA identity verification required for PPDA-compliant cooperative procurement |
| Contact phone | P | Consent | Consent at registration — farmer communication and SMS payment confirmation |
| GPS farm coordinates | P | Consent + Performance of contract | Consent at registration; required for farm traceability and cooperative procurement chain of custody |
| Farmer photograph | P | Consent | Consent at registration — identity verification at collection point |
| Mobile money number | **S** | Consent + Legal obligation | Consent at registration; required for bulk payment disbursement per cooperative payment obligation; Income Tax Act payment records |
| Payment amounts | **S** | Legal obligation | Income Tax Act Cap 340 — 7-year payment record retention; PPDA cooperative procurement audit trail |
| Cooperative membership number | P | Performance of contract | Cooperative membership terms |
| Farmer age | P | Consent + Section 8 safeguard | Consent; age verification required by Section 8 DPPA 2019 for data subjects who may be under 18 |

---

## 3.2 Employee Data — Lawful Basis

| Data Field | Tier | Lawful Basis (Section 7) | Specific Legal Ground |
|---|---|---|---|
| Full name | P | Performance of contract | Employment contract |
| NIN | P | Legal obligation | Income Tax Act — employer PAYE obligations; NSSF Act |
| Home address | P | Performance of contract | Employment contract |
| Employee photograph | P | Consent | Explicit consent obtained at onboarding; photograph used for identification only |
| Salary / pay grade / deductions | **S** | Performance of contract + Legal obligation | Employment contract; Income Tax Act (PAYE); NSSF Act; LST |
| Bank account number | **S** | Performance of contract | Employment contract — salary payment |
| Mobile money number | **S** | Performance of contract | Employment contract — casual worker salary payment via mobile money |
| Staff loan balance | **S** | Performance of contract | Loan agreement between employee and BIRDC |
| Leave records | P | Performance of contract | Employment contract; Employment Act Uganda |
| Disciplinary records | P | Performance of contract + Legal obligation | Employment contract; Employment Act Uganda |
| Biometric fingerprint template | P | Legal obligation + Consent | Employment contract attendance obligation; explicit biometric consent obtained separately (ZKTeco device — not stored in application DB) |

---

## 3.3 Agent Data — Lawful Basis

| Data Field | Tier | Lawful Basis (Section 7) | Specific Legal Ground |
|---|---|---|---|
| Full name | P | Performance of contract | Agent distribution agreement |
| NIN | P | Legal obligation | Income Tax Act; WHT (6%) on agent commissions |
| Contact phone | P | Performance of contract | Agent distribution agreement |
| Mobile money number | **S** | Performance of contract | Agent distribution agreement — commission payment |
| Commission amounts | **S** | Performance of contract + Legal obligation | Agent distribution agreement; Income Tax Act (commission income) |
| Cash balance | **S** | Performance of contract | Agent distribution agreement — liability tracking |

---

## 3.4 Uncertain Lawful Basis

The following data fields have an uncertain or contested lawful basis pending legal review:

| Data Field | Uncertainty | Flag |
|---|---|---|
| GPS farm coordinates (polygon detail) | Whether full polygon is necessary or whether a single centroid point satisfies the traceability obligation — affects proportionality under Section 3 DPPA | [CONTEXT-GAP: GAP-004] |
| Farmer photograph retention after NIN validated | Whether photograph must be retained for the full 7-year period or may be deleted after identity verification — affects Section 18 retention proportionality | [CONTEXT-GAP: GAP-004] |
| Agent cash balance (real-time tracking) | Whether continuous monitoring of individual agent financial position requires explicit consent beyond the contract performance basis | [CONTEXT-GAP: GAP-004] |

*Resolution: Commission qualified Uganda DPPA 2019 legal counsel review before Phase 3 go-live. See Section 11.*
