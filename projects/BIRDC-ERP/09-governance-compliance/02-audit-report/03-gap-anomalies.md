# Section 3: Open Anomalies — GAP-001 through GAP-014

Each open gap from `_context/gap-analysis.md` is recorded as a Conditional Anomaly. A Conditional Anomaly is an external dependency that prevents full verification of one or more FRs. Unlike an internal consistency anomaly, a Conditional Anomaly does not invalidate the SRS; it defers test execution until the external data is received.

## 3.1 Conditional Anomaly Register

| Anomaly ID | Gap Reference | Description | Affected FRs | Severity | Resolution Action | Target Owner |
|---|---|---|---|---|---|---|
| CA-001 | GAP-001 | URA EFRIS API sandbox credentials not yet provisioned. EFRIS integration cannot be tested in Phase 1 or Phase 7. | FR-SAL-003, FR-SAL-012, FR-EFR-001, FR-EFR-002, FR-EFR-003, FR-EFR-004, FR-POS-008 | High | BIRDC to register with URA EFRIS developer portal and obtain sandbox API key before Phase 1 invoice testing sprint | BIRDC IT / Peter |
| CA-002 | GAP-002 | MTN MoMo Business API sandbox credentials not yet provisioned. Agent remittance and farmer bulk payment tests cannot run. | FR-AGT-009, FR-AP-006, FR-PAY-011 | High | Peter to register MTN MoMo Developer Portal; BIRDC Finance to provide business verification documents | Peter / BIRDC Finance |
| CA-003 | GAP-003 | Airtel Money API sandbox credentials not yet provisioned. Lower priority than MTN MoMo. | FR-PAY-011, FR-AP-006 (Airtel path) | Medium | Register Airtel Money developer portal during Phase 2 development | Peter |
| CA-004 | GAP-004 | Uganda Data Protection and Privacy Act 2019 legal review of farmer PII (GPS, NIN, photo, mobile money number) not completed. System cannot go live with farmer registration until lawful basis is confirmed. | FR-FAR-001, FR-FAR-009, FR-PRO-011 | Critical | BIRDC to engage legal counsel familiar with DPPA 2019. Confirm lawful basis (consent vs. legitimate interest), retention period, and subject rights before go-live | BIRDC Legal |
| CA-005 | GAP-005 | ZKTeco biometric device model numbers and SDK/API version at BIRDC Nyaruzinga not confirmed. Biometric attendance integration design is incomplete. | FR-HR-003, FR-HR-004 | Medium | BIRDC IT to provide ZKTeco model serial numbers from devices already installed | BIRDC IT |
| CA-006 | GAP-006 | BIRDC bank name and bulk credit transfer file format not confirmed. Payroll bank transfer file cannot be finalised. | FR-PAY-010 | Medium | BIRDC Finance to provide specimen of bank's bulk credit transfer file format or their online banking portal's import template | BIRDC Finance |
| CA-007 | GAP-007 | Exact PPDA procurement threshold values (UGX amounts) currently applicable to BIRDC/PIBID as a government entity not confirmed. Procurement approval matrix cannot be configured with correct values. | FR-PRO-001, FR-PRO-002, FR-PRO-003, FR-ADM-001, FR-ADM-002 | High | BIRDC Administration to obtain current PPDA threshold schedule from PPDA Uganda website or procurement office | BIRDC Administration / Peter |
| CA-008 | GAP-008 | Current URA PAYE tax bands for 2025/26 not confirmed. Payroll calculation test values cannot be set. | FR-PAY-002 | High | Peter to confirm from URA Uganda website or finance circular before payroll module development begins | Peter |
| CA-009 | GAP-009 | NSSF remittance schedule exact format required by NSSF Uganda not confirmed. NSSF export test cannot verify format compliance. | FR-PAY-004 | Medium | BIRDC HR to obtain NSSF employer contribution schedule template from NSSF Uganda | BIRDC HR |
| CA-010 | GAP-010 | Export market QC parameter requirements (South Korea, EU/Italy, Saudi Arabia, Qatar, USA) not confirmed. Export CoA template design is incomplete. | FR-QC-005, FR-QC-006 | High | BIRDC QC Manager to obtain import inspection parameter lists from each target market's relevant food safety authority | BIRDC QC Manager |
| CA-011 | GAP-011 | Bluetooth weighing scale model at cooperative collection points not confirmed. Farmer Delivery App hardware integration design is incomplete. | FR-PRO-011 | Medium | BIRDC Procurement to provide scale model/brand currently deployed at cooperative collection points | BIRDC Procurement |
| CA-012 | GAP-012 | BIRDC existing Chart of Accounts status not confirmed — whether the 1,307-account CoA exists or must be designed from scratch. | FR-FIN-001, FR-FIN-002 | High | Finance Director to confirm whether an existing CoA file (in Excel or legacy system export) can be provided | BIRDC Finance Director |
| CA-013 | GAP-013 | BIRDC server hardware specifications (RAM, storage, OS) not confirmed. Deployment guide and performance test baseline cannot be finalised. | FR-SEC-003, FR-SEC-005 | Medium | BIRDC IT to provide server inventory sheet with hardware specifications | BIRDC IT |
| CA-014 | GAP-014 | BIRDC existing accounting software (if any) and data migration requirements not confirmed. Go-live cutover plan and data migration strategy are incomplete. | FR-SEC-007 | High | Finance Director to confirm the current accounting tools in use and authorise a data extraction exercise | BIRDC Finance / Peter |

## 3.2 Internal Anomaly: BR-018 Partial FR Coverage

| Anomaly ID | Type | Description | Affected Rule | Recommended Action |
|---|---|---|---|---|
| IA-001 | Internal — Completeness Gap | BR-018 (Imprest Account Control) is enforced by implicit references in the GL auto-posting FRs but no FR explicitly specifies the blocking condition when an imprest disbursement would drive the balance below zero. | BR-018 | Add FR-FIN-013 and FR-FIN-014 to SRS-P2 before the next SRS review cycle (see RTM Section 4.3 for full FR text). |

This is the only internal anomaly in the SRS suite. All other gaps are external dependencies, not internal consistency failures.
