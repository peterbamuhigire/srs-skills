# Section 11 — Human Review Gate

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

---

## 11.1 CONTEXT-GAP Flags Detected

The following gaps were identified during generation of this compliance annex. Each must be resolved before the corresponding module enters production.

| Flag | Description | Resolution Trigger |
|---|---|---|
| [CONTEXT-GAP: GAP-004] | Uganda DPPA 2019 legal review by qualified counsel not yet commissioned. Required for: lawful basis mapping confirmation, consent form draft review (English + Runyankore/Rukiga), retention schedule vs. erasure rights conflict resolution, and data processor contract terms review. | Commission legal review before Phase 3 go-live |
| [CONTEXT-GAP: GAP-004] | DPO not yet designated by BIRDC. Section 6 DPPA 2019 requires every institution head to designate a DPO. Without a designated DPO, the breach notification, rights requests, and consent functions cannot be operationally activated. | BIRDC Director to designate DPO before Phase 3 |
| [CONTEXT-GAP: GAP-002] | MTN MoMo API credentials not yet obtained. Data processor contract with MTN Uganda cannot be executed without API credentials. Farmer payment and payroll modules cannot transmit S-tier data without an executed processor contract. | Obtain MTN MoMo Business API credentials |
| [CONTEXT-GAP: GAP-003] | Airtel Money API credentials not yet obtained. Same constraint as GAP-002 for Airtel. | Obtain Airtel Money API credentials |

---

## 11.2 DPIA-REQUIRED Flags Detected

| Flag | Processing Operation | Reference Document |
|---|---|---|
| [DPIA-REQUIRED: Large-scale processing of S-tier financial data and P-tier data for 6,440+ farmers — Regulation 12] | Farmer registration, GPS mapping, NIN collection, mobile money payment | DPIA_FarmerData_BIRDC_ERP (Section 10.1) |
| [DPIA-REQUIRED: Large-scale processing of S-tier financial data for 150+ employees — Regulation 12] | Monthly payroll — salary, bank accounts, mobile money, PAYE, NSSF | DPIA_EmployeePayroll_BIRDC_ERP (Section 10.2) |

---

## 11.3 DPPA-FAIL Tags Detected

**No DPPA-FAIL tags were detected in this annex.** All S-tier fields have AES-256-GCM encryption specified (Section 6). Breach notification is labelled IMMEDIATE (Section 8). Data subject rights response SLA is 30 calendar days (Section 5). PDPO — not the data controller — decides whether to notify data subjects (Section 8.4). Consent mechanisms are specified for all consent-basis fields (Section 4).

---

## 11.4 Recommended Actions Before Phase 3 Go-Live

The following 4 actions must be completed before the Farmer Registration and Cooperative Management module (Phase 3) enters production:

1. **Commission legal review (GAP-004).** Engage qualified Uganda DPPA 2019 legal counsel to review this annex, the DPIA for farmer data processing, the consent form drafts, and the data processor contract templates. Document the review outcome and incorporate any amendments.

2. **Draft and test consent form in English and Runyankore/Rukiga.** The farmer registration consent form (FR-DPPA-009) must be drafted in both languages, reviewed by a native Runyankore/Rukiga speaker, and tested with Patrick (Collections Officer persona) before go-live.

3. **Register with PDPO at NITA-U.** BIRDC must complete registration with the Personal Data Protection Office (PDPO Form 2 per Regulations 15–16). The PDPO registration number must be entered in the system administration configuration before farmer registration begins.

4. **Designate DPO and enter in system.** BIRDC Director must formally designate a Data Protection Officer per Section 6 DPPA 2019 and Regulation 47. The DPO designation record must be entered in the system administration configuration. The DPO must be trained on the DPO dashboard, breach notification workflow, and 30-day response obligations before go-live.

---

## 11.5 Consultant Acknowledgement

This annex was prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com), from BIRDC ERP context files as of 2026-04-05. It is a draft compliance specification, not legal advice. The findings and requirements herein require review by qualified Uganda legal counsel before being relied upon for regulatory compliance.

*Do not proceed to Phase 3 or Phase 5 implementation without completing the 4 actions in Section 11.4.*
