## 8. Context Gaps and Outstanding Actions

The following gaps were identified during strategy authoring. Resolution is required before the affected test activities can begin.

| Gap ID | Description | Affected Test Activity | Required Action | Owner |
|---|---|---|---|---|
| GAP-001 | URA EFRIS sandbox credentials and endpoint URL not confirmed. | Integration testing (Phase 1), System testing (Phase 1 and Phase 7). | Obtain sandbox access credentials from URA Developer Portal. Confirm sandbox base URL and API version. | Peter Bamuhigire / BIRDC Finance Director |
| GAP-002 | MTN MoMo sandbox API key and collection URL not confirmed. | Integration testing (Phase 1 — agent remittance push, Phase 3 — farmer bulk payment, Phase 5 — salary payment). | Obtain from MTN Uganda Developer Portal (momodeveloper.mtn.com). Register BIRDC as a business API user. | Peter Bamuhigire / BIRDC Director |
| GAP-003 | Airtel Money sandbox credentials not confirmed. | Integration testing (same scope as GAP-002 — dual-provider redundancy). | Obtain from Airtel Africa developer programme. | Peter Bamuhigire / BIRDC Director |
| GAP-004 | ZKTeco device model and SDK version not confirmed. | Integration testing (Phase 5 — biometric attendance import). | Confirm ZKTeco model number and SDK from the BIRDC IT Administrator. Obtain SDK documentation before HR module development. | BIRDC IT Administrator |
| GAP-005 | Uganda PAYE tax bands for 2025/26 financial year not yet confirmed (URA may publish revised bands). | Unit testing (TC-PAY-xxx). | Confirm URA 2025/26 PAYE bands when published. Update oracles in Test Plan if bands change from 2024/25. | Peter Bamuhigire |
| GAP-006 | Staging server hardware specification and availability date not confirmed. | All test levels from integration onwards. | BIRDC IT Administrator to confirm staging hardware and expected ready date. | BIRDC IT Administrator |
