# Appendix A: Open Items, Context Gaps, and V&V Flags

## A.1 Context Gaps

The following items are unresolved at the time of this document's drafting. No requirement that depends on these gaps may pass acceptance testing until the gap is resolved.

| Gap ID | Description | Severity | Blocking Requirement(s) | Owner |
|---|---|---|---|---|
| **GAP-001** | URA EFRIS API sandbox credentials for development and testing | High | FR-SAL-011, FR-SAL-012, FR-SAL-015, FR-SAL-033, FR-POS-014, FR-POS-015, FR-POS-017, FR-SAL-030, FR-SAL-035 | BIRDC IT / Peter |
| **GAP-002** | MTN MoMo Business API sandbox credentials | High | FR-POS-009, FR-AGT-028 | Peter / BIRDC Finance |
| **GAP-003** | Airtel Money API sandbox credentials | Medium | FR-POS-010 | Peter / BIRDC Finance |
| **GAP-004** | Uganda Data Protection and Privacy Act 2019 legal review for agent NIN, photo, GPS, and mobile money data | Critical | FR-AGT-001 (agent NIN/photo) | BIRDC Legal / Peter |
| **GAP-012** | Confirm whether BIRDC holds an existing Chart of Accounts (1,307 accounts) or this requires design from scratch | High | FR-SAL-013, FR-AGT-010, FR-AGT-034, FR-INV-020, FR-INV-028 | BIRDC Finance Director |
| **GAP-013** | Cold store temperature sensor capability at BIRDC Nyaruzinga (automated or manual) | Medium | FR-INV-029 | BIRDC IT |
| **GAP-014** | Packaging material item codes and existing legacy data migration requirements | High | FR-INV-030, phase go-live planning | BIRDC Finance / Procurement |

## A.2 V&V Flags and Verification Notes

The following requirements require additional detail or stakeholder confirmation before they can be marked "verified" per the IEEE 1012 framework.

| Flag | Location | Description |
|---|---|---|
| `[CONTEXT-GAP: GAP-001]` | FR-SAL-011, FR-SAL-030, FR-SAL-035, FR-POS-014, FR-POS-017 | EFRIS sandbox not yet available; EFRIS submission logic cannot be integration-tested until credentials are provided |
| `[CONTEXT-GAP: GAP-002]` | FR-POS-009, FR-AGT-028 | MTN MoMo API integration cannot be tested until sandbox credentials are confirmed |
| `[CONTEXT-GAP: GAP-003]` | FR-POS-010 | Airtel Money integration cannot be tested |
| `[CONTEXT-GAP: GAP-004]` | FR-AGT-001 | Agent personal data collection (NIN, photo) requires legal sign-off before implementation |
| `[CONTEXT-GAP: GAP-012]` | FR-INV-028, FR-AGT-034 | GL account mapping for product categories and agent AR sub-accounts depends on Chart of Accounts availability |
| `[VERIFIABILITY-FAIL: FR-POS-017]` | FR-POS-017 | SMS/WhatsApp gateway provider not confirmed; receipt delivery mechanism cannot be fully specified until provider is named |
| `[CONTEXT-GAP: GAP-013]` | FR-INV-029 | Cold store temperature logging mechanism depends on hardware confirmation |

## A.3 Glossary Gaps

All domain terms used in this document are defined in `_context/glossary.md`. The following terms are used in this document and are confirmed present in the glossary:

BIRDC, PIBID, Tooke, Agent, Agent Cash Balance, Agent Stock Balance, CoA, Cooperative, Circular Economy, DC, Dual-Mode Accounting, Dual-Track Inventory, EFRIS, FEFO, FDN, Float Limit, GL, GRN, Hash Chain, ICPAU, Imprest, JE, LPO, LST, Mass Balance, Matooke, NCR, NIN, NSSF, OAG, PAYE, POS, PPDA, PRD, QC, Remittance, RFQ, SPC, TIN, URA, Vote, WHT, WIP, ZKTeco.

No `[GLOSSARY-GAP]` flags at this time.

## A.4 Human Review Gate — Required Stakeholder Acknowledgements

Per the PRIME Methodology (Inspect step), the following items require explicit stakeholder acknowledgement before this document is baselined for development:

1. **Finance Director (STK-002)** shall confirm the GL account structure for FR-SAL-013, FR-SAL-018, FR-INV-020, FR-AGT-010, and FR-AGT-014 (dependent on GAP-012 resolution).
2. **Sales and Marketing Manager (STK-006)** shall confirm the daily sales summary content (FR-SAL-025) and the automatic agent suspension threshold (FR-AGT-016).
3. **BIRDC Director (STK-001)** shall confirm the push notification recipients and escalation thresholds.
4. **IT Administrator (STK-003)** shall confirm server hardware availability (**GAP-013**) and EFRIS API access.
5. **BIRDC Legal** shall confirm data protection compliance posture (**GAP-004**) before FR-AGT-001 is implemented.

---

*End of Appendix A*

---

*End of Document*

*SRS Version 1.0 DRAFT — BIRDC ERP Phase 1: Commerce Foundation*

*Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC*

*2026-04-05*
