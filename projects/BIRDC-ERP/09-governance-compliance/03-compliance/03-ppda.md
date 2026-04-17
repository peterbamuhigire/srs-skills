# Section 3: PPDA Act Compliance

## 3.1 Scope of PPDA Obligation

BIRDC is a government entity (PIBID, established by presidential directive 2005) and therefore all procurement transactions are subject to the Public Procurement and Disposal of Public Assets Act (PPDA Act, Cap 305) and associated regulations. Every purchase — from office stationery to capital equipment — must be classified, documented, and approved per the PPDA Act requirements.

## 3.2 How the System Enforces PPDA Compliance

### 3.2.1 Procurement Category Classification (BR-005)

FR-PRO-001 mandates that every procurement transaction is classified by PPDA category at the time of purchase request creation. The four categories are:

- *Micro procurement* — below the micro threshold (UGX value to be configured per [CONTEXT-GAP: GAP-007])
- *Small procurement* — between micro and small thresholds
- *Large procurement* — above the small threshold, below restricted
- *Restricted procurement* — sole-source or emergency procurement

The threshold values are stored in a configuration table (Design Covenant DC-002) and can be updated by the IT Administrator or Finance Director via the UI when PPDA publishes revised thresholds, without developer involvement.

### 3.2.2 PPDA Approval Matrix Enforcement (BR-005)

FR-PRO-002 enforces the approval matrix at the API layer. A procurement request cannot advance to the LPO issuance stage unless every required approval in the matrix has been obtained:

| PPDA Category | Required Approvals | System Enforcement |
|---|---|---|
| Micro | Department Head | System checks that Department Head approval flag = true before LPO issuance |
| Small | Finance Manager + Procurement Officer | Both approval flags must be set; sequential enforcement |
| Large | Director + Finance Manager + Solicitor General clearance (where required) | Three approval flags; Director approval is final gate |
| Restricted | Board approval + all PPDA documentation complete | Board approval flag + document completeness check |

FR-PRO-003 adds a payment-level block: the Accounts Payable module will not process payment for a procurement transaction unless the PPDA document checklist is 100% complete. This creates a hard stop at the payment stage that is independent of the procurement approval workflow — a second independent control.

### 3.2.3 PPDA Document Management

FR-ADM-001 manages the full PPDA document set for each procurement category. The required documents per category are:

| Document | Micro | Small | Large | Restricted |
|---|---|---|---|---|
| Purchase Request | Required | Required | Required | Required |
| Quotations (minimum number) | 1 | 3 | 5 | Per PPDA guidance |
| Evaluation Report | Not required | Required | Required | Required |
| Local Purchase Order | Required | Required | Required | Required |
| Goods Receipt Note | Required | Required | Required | Required |
| Vendor Invoice | Required | Required | Required | Required |
| Payment Voucher | Required | Required | Required | Required |
| Solicitor General Clearance | — | — | Where applicable | Where applicable |
| Board Resolution | — | — | — | Required |

FR-ADM-002 maintains the PPDA Procurement Register: a running record of every procurement transaction with its PPDA category, approval status, and document completion status. This register is the primary artefact presented to PPDA inspectors and parliamentary committees.

### 3.2.4 Parliamentary Review Export

FR-ADM-003 generates a PPDA Procurement Register export in a format suitable for parliamentary review. The export includes: transaction date, vendor name, item description, PPDA category, value (UGX), approval chain with timestamps, document completeness status, and vote code (for PIBID budget-funded procurement). This export satisfies the requirement for Parliament's Budget Committee (STK-004) to verify that every shilling of the UGX 200 billion investment is procured in compliance with PPDA rules.

### 3.2.5 Audit Trail for Parliamentary Review

Every procurement action — creation, approval, rejection, payment — is recorded in the system audit trail (FR-SYS-003) with user identity and timestamp. The audit trail is immutable (DC-003) and retained for 7 years. The Office of the Auditor General can query the full procurement audit trail for any period during an annual audit without requiring any manual reconstruction.

## 3.3 PPDA Compliance Summary

The system enforces PPDA compliance at 3 independent control points: (1) purchase request classification and approval routing, (2) LPO issuance blocked without required approvals, and (3) payment blocked without complete documentation. This triple-control architecture exceeds the PPDA minimum requirement of a single approval workflow. The outstanding item is the confirmation of current PPDA threshold values [CONTEXT-GAP: GAP-007].
