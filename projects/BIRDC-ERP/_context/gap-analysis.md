# Gap Analysis & Open Items — BIRDC ERP

Known external dependencies, unresolved decisions, and information gaps that must be
resolved before or during development. Flag any unresolved gap as `[CONTEXT-GAP: GAP-xxx]`
in generated documents.

---

| GAP ID | Description | Severity | Owner | Resolution Trigger |
|---|---|---|---|---|
| GAP-001 | URA EFRIS API sandbox credentials for development and testing | High | BIRDC IT / Peter | Required before Phase 1 invoice testing can complete |
| GAP-002 | MTN MoMo Business API sandbox credentials | High | Peter / BIRDC Finance | Required before agent remittance and farmer payment testing |
| GAP-003 | Airtel Money API sandbox credentials | Medium | Peter / BIRDC Finance | Required before Airtel payment testing (MTN MoMo is higher priority) |
| GAP-004 | Uganda Data Protection and Privacy Act 2019 — legal review of farmer data (GPS coordinates, NIN, photo, mobile money number) collection and storage | Critical | BIRDC Legal / Peter | Required before system goes live with farmer registration |
| GAP-005 | ZKTeco biometric device model numbers deployed at BIRDC and their API/SDK version — needed for HR integration specification | Medium | BIRDC IT | Required before HR biometric integration design is finalised |
| GAP-006 | BIRDC bank name and bulk credit transfer file format required by their bank | Medium | BIRDC Finance | Required before payroll bank transfer file specification |
| GAP-007 | Exact PPDA procurement threshold values (UGX amounts) currently applicable to BIRDC/PIBID as a government entity | High | BIRDC Administration / Peter | Required before procurement approval matrix can be configured |
| GAP-008 | Current URA PAYE tax bands (confirm 2024/25 rates apply or if updated) | High | Peter | Confirm before payroll calculation specification is finalised |
| GAP-009 | NSSF contribution schedule exact format required by NSSF Uganda for employer remittance | Medium | BIRDC HR | Required before payroll module NSSF export is specified |
| GAP-010 | Export market QC parameter requirements — exact parameters and limits for South Korea, EU (Italy), Saudi Arabia, Qatar, USA import inspection | High | BIRDC QC Manager | Required before export CoA template design |
| GAP-011 | Bluetooth weighing scale model used at cooperative collection points — for Farmer Delivery App integration | Medium | BIRDC Procurement | Required before Farmer Delivery App hardware specification |
| GAP-012 | Confirm whether BIRDC holds an existing Chart of Accounts (1,307 accounts referenced in spec) or if this needs to be designed from scratch | High | BIRDC Finance Director | Required before database design and GL module |
| GAP-013 | Server hardware specifications currently available at BIRDC Nyaruzinga — RAM, storage, OS version — for deployment guide | Medium | BIRDC IT | Required before deployment guide can be written |
| GAP-014 | BIRDC's existing accounting software (if any) — data migration requirements from legacy system | High | BIRDC Finance / Peter | Required before data migration plan and go-live strategy |
