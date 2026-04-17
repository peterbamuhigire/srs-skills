# Section 9: Assumptions and Open Items

The following assumptions underpin this Product Requirements Document. Each assumption corresponds to a known information gap (from the project Gap Analysis). If any assumption is invalidated, the affected module specifications must be revised before development of that module begins.

The gap owner is responsible for resolution. The consultant (Peter Bamuhigire) will update the relevant specification section when each gap is closed.

## 9.1 Open Item Register

| GAP ID | Assumption (if unresolved) | Severity | Owner | Resolution Trigger |
|---|---|---|---|---|
| GAP-001 | EFRIS API sandbox credentials will be provided by BIRDC IT before Phase 1 invoice testing commences. Until provided, EFRIS integration is designed against the URA EFRIS public API specification only. | High | BIRDC IT / Peter | Required before Phase 1 invoice testing |
| GAP-002 | MTN MoMo Business API sandbox credentials will be provided by BIRDC Finance before agent remittance and farmer payment testing. | High | Peter / BIRDC Finance | Required before agent remittance testing |
| GAP-003 | Airtel Money API sandbox credentials will be provided before Airtel payment testing. MTN MoMo is higher priority and will be integrated first. | Medium | Peter / BIRDC Finance | Required before Airtel payment testing |
| GAP-004 | BIRDC will obtain a legal review of farmer data collection (GPS coordinates, NIN, photo, mobile money number) under the Uganda Data Protection and Privacy Act 2019 before go-live. The Farmer Registration module is specified on the assumption that this review confirms compliance. | Critical | BIRDC Legal / Peter | Required before go-live with farmer registration |
| GAP-005 | The ZKTeco biometric devices deployed at BIRDC use a standard ZKTeco SDK API compatible with direct MySQL import. The exact device model numbers will be confirmed by BIRDC IT before HR biometric integration is finalised. | Medium | BIRDC IT | Required before HR biometric integration design |
| GAP-006 | BIRDC's bank accepts a standard Uganda ACH/EFT bulk credit transfer file format. The exact format will be confirmed with BIRDC Finance before the payroll bank transfer file specification is finalised. | Medium | BIRDC Finance | Required before payroll bank transfer specification |
| GAP-007 | The PPDA procurement threshold values (UGX amounts for micro, small, large, and restricted categories) applicable to PIBID/BIRDC as a government entity will be confirmed with BIRDC Administration. The procurement approval matrix (BR-005) is designed around these thresholds and will be updated when confirmed. | High | BIRDC Administration / Peter | Required before procurement approval matrix is configured |
| GAP-008 | Uganda PAYE tax bands are assumed to be the 2024/25 URA-published rates. If URA has published updated bands, BIRDC's Finance Director will provide the updated schedule before payroll module specification is finalised. | High | Peter | Confirm before payroll calculation specification |
| GAP-009 | The NSSF contribution schedule format required by NSSF Uganda for employer remittance will be provided by BIRDC HR. The payroll module NSSF export is designed around the standard NSSF Uganda employer format and will be updated when the exact template is confirmed. | Medium | BIRDC HR | Required before payroll NSSF export specification |
| GAP-010 | Export CoA parameter requirements (specific test parameters and limits for South Korea, EU/Italy, Saudi Arabia, Qatar, and USA import inspection) will be provided by the BIRDC QC Manager. Export CoA templates are specified as configurable; the default parameter sets will be finalised when market requirements are confirmed. | High | BIRDC QC Manager | Required before export CoA template design |
| GAP-011 | The Bluetooth weighing scale at cooperative collection points uses a standard Bluetooth serial/BLE protocol compatible with Android Bluetooth API. The exact model will be confirmed by BIRDC Procurement before the Farmer Delivery App hardware specification is finalised. | Medium | BIRDC Procurement | Required before Farmer Delivery App hardware specification |
| GAP-012 | BIRDC holds an existing Chart of Accounts. If the 1,307-account chart referenced in the feature specification does not exist, the Finance Director will lead a chart-of-accounts design workshop with the consultant before the GL module database design is finalised. | High | BIRDC Finance Director | Required before GL module database design |
| GAP-013 | BIRDC's server hardware at Nyaruzinga meets minimum specifications for the system. BIRDC IT will provide server specifications (RAM, storage, OS version) before the deployment guide is written. | Medium | BIRDC IT | Required before deployment guide |
| GAP-014 | If BIRDC uses an existing accounting system, data migration will be scoped as a separate engagement. The current specification assumes a greenfield go-live. If historical data migration is required, it must be agreed and funded as an additional sprint. | High | BIRDC Finance / Peter | Required before go-live strategy is confirmed |

## 9.2 Assumption Management

When a gap is resolved:

1. The gap owner notifies Peter Bamuhigire with the confirmed information.
2. The consultant updates the relevant `_context/` file and affected specification section.
3. The updated section is marked with the gap closure date and the gap status is updated to "Resolved" in the gap analysis register.
4. No development work on a module affected by an unresolved Critical or High severity gap shall commence until that gap is resolved.

