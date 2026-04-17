# 8. Design Constraints, Open Gaps, and Traceability

## 8.1 Design Constraints Summary

All Phase 3 requirements are subject to the 7 binding Design Covenants. The table below records how each DC applies to Phase 3.

| DC | Covenant | Phase 3 Application |
|---|---|---|
| DC-001 | Zero mandatory training | Patrick (collection officer) completes farmer registration + delivery in < 5 minutes first attempt (NFR-USR-002). Robert (procurement manager) completes 5-stage batch in < 45 minutes (NFR-USR-001). |
| DC-002 | Configuration over code | PPDA thresholds, grade prices, cooperative levies, transport charges, SMS templates, and mobile money credentials all configurable in admin UI per NFR-MNT-001 through NFR-MNT-003. |
| DC-003 | Audit readiness | Every stage transition in the 5-stage workflow creates an immutable audit trail entry. Batch audit trail report (FR-PRO-059) provides full PPDA documentation. 7-year retention enforced. |
| DC-004 | Dual-mode accounting | GL postings in Stage 5 use the dual-mode GL engine from Phase 2 (F-005); PIBID and BIRDC accounts updated simultaneously. |
| DC-005 | Offline-first | Farmer Delivery App operates fully offline (Section 5). All FR-MOB-xxx requirements explicitly tested for offline operation. |
| DC-006 | Data sovereignty | Farmer NIN, GPS, photo, and phone number stored on BIRDC on-premise server only. Mobile money API credentials never leave the server. |
| DC-007 | Replicable by design | Cooperative hierarchy, PPDA thresholds, quality grade structure, and mobile money provider configuration isolated in config tables. Redeploy for any government agro-processor by changing configuration. |

## 8.2 Business Rule Compliance Matrix

| BR | Rule | Phase 3 Enforcement |
|---|---|---|
| BR-003 | Segregation of duties | PR creator ≠ PR approver; GRN creator ≠ invoice approver; batch contribution recorder ≠ GL poster; enforced at API layer (FR-PRO-001 to FR-PRO-028) |
| BR-005 | PPDA approval matrix | Enforced in FR-PRO-003 through FR-PRO-007; threshold table configurable per NFR-MNT-001 |
| BR-009 | Sequential numbering | PR, RFQ, LPO, GRN, BPO, batch numbers all sequential; gap detection alerts Finance Manager (NFR-INT-003) |
| BR-011 | Individual farmer contribution tracking | 100% weight allocation enforced before Stage 4 advance (FR-PRO-050, FR-PRO-051) |
| BR-012 | Three-way matching | Enforced in FR-PRO-026; variances flagged for Finance Manager; no payment without match confirmation |
| BR-013 | GL hash chain integrity | Stage 5 GL posting uses the hash-chain GL engine from Phase 2 (F-005) |

## 8.3 Open Gaps Registry — Phase 3 Specific

All gaps flagged in this document are registered in `_context/gap-analysis.md`. The Phase 3 relevant gaps are:

| GAP ID | Description | Severity | Impact on Phase 3 | Resolution Owner |
|---|---|---|---|---|
| GAP-002 | MTN MoMo Business API sandbox credentials | High | Farmer bulk payment integration cannot be tested (FR-PRO-063, FR-FAR-033) | Peter / BIRDC Finance |
| GAP-003 | Airtel Money API sandbox credentials | Medium | Airtel farmer payment flow cannot be tested (FR-FAR-034) | Peter / BIRDC Finance |
| GAP-004 | Uganda Data Protection and Privacy Act 2019 legal review for farmer data | Critical | FR-FAR-005, FR-FAR-045, FR-FAR-046, NFR-CMP-002 cannot be finalised without legal advice | BIRDC Legal / Peter |
| GAP-007 | Exact PPDA procurement threshold values (UGX) | High | FR-PRO-003 approval matrix cannot be configured (threshold table will be populated with placeholder values in dev) | BIRDC Administration / Peter |
| GAP-011 | Bluetooth weighing scale model at collection points | Medium | FR-MOB-011 Bluetooth scale SDK integration cannot be coded until model is confirmed | BIRDC Procurement |

## 8.4 Requirement Traceability Matrix — Phase 3

| Requirement ID | Description (Summary) | Business Goal | Business Rule | DC |
|---|---|---|---|---|
| FR-PRO-001 | PR creation and sequential numbering | Operational unity, PPDA compliance | BR-009 | DC-003 |
| FR-PRO-003 | PPDA category classification | PPDA compliance | BR-005 | DC-002, DC-003 |
| FR-PRO-026 | Three-way matching enforcement | Financial integrity | BR-012 | DC-003 |
| FR-PRO-040 | Cooperative Bulk PO creation | Operational unity, farmer management | — | DC-002 |
| FR-PRO-047 | Individual farmer lookup in Stage 3 | Farmer accountability | BR-011 | DC-003 |
| FR-PRO-050 | 100% weight allocation gate | Individual farmer contribution tracking | BR-011 | DC-003 |
| FR-PRO-056 | Stage 5 GL auto-posting | Financial integrity | BR-013 | DC-003, DC-004 |
| FR-PRO-060 | Farmer payment aggregation | Farmer accountability, financial integrity | — | DC-003 |
| FR-FAR-001 | Farmer registration — all fields | 6,440+ farmer network management | — | DC-005, DC-006 |
| FR-FAR-005 | Farmer data encryption at rest | Data sovereignty, DPPA 2019 | — | DC-006 |
| FR-FAR-025 | Input loan issuance | Agent/farmer accountability | — | DC-002, DC-003 |
| FR-FAR-035 | Payment confirmation and GL update | Financial integrity | — | DC-003 |
| FR-MOB-005 | Offline operation — all collection functions | Offline-first | — | DC-005 |
| FR-MOB-019 | Conflict resolution rules | Data integrity, offline-first | — | DC-005 |

## 8.5 Human Review Gate

*Per the PRIME Methodology (Kodukula & Vinueza, 2024) and the Skill Execution Workflow, the consultant must review this document before proceeding to design or build. The following items require explicit acknowledgement:*

**Context Gaps requiring resolution before go-live:**

- [CONTEXT-GAP: GAP-002] — MTN MoMo API credentials; farmer payment integration testing blocked.
- [CONTEXT-GAP: GAP-003] — Airtel Money API credentials; Airtel payment flow testing blocked.
- [CONTEXT-GAP: GAP-004] — Uganda DPPA 2019 legal review; farmer data handling (NIN, GPS, photos) must be legally cleared before system goes live with live farmer data.
- [CONTEXT-GAP: GAP-007] — PPDA threshold values; procurement approval matrix will use placeholder values in development; must be confirmed and configured before procurement module testing.
- [CONTEXT-GAP: GAP-011] — Bluetooth scale model; FR-MOB-011 scale SDK integration cannot be specified until model is confirmed.

**Glossary gaps identified during generation:**

- [GLOSSARY-GAP: NIRA] — National Identification and Registration Authority; add to `_context/glossary.md`.
- [GLOSSARY-GAP: BPO] — Bulk Purchase Order; add to `_context/glossary.md`.
- [GLOSSARY-GAP: BTH] — Batch number prefix used in Stage 2; add to `_context/glossary.md`.
- [GLOSSARY-GAP: DPPA] — Data Protection and Privacy Act; add to `_context/glossary.md`.
- [GLOSSARY-GAP: Grade A / Grade B / Grade C] — Matooke quality grades; formal definitions (minimum weight thresholds, visual quality criteria) to be provided by QC Manager and added to `_context/glossary.md`.

**Verification items for consultant review:**

1. Confirm that the cooperative hierarchy (4 levels: farmer → cooperative → zone → BIRDC) matches BIRDC's actual field structure.
2. Confirm the SMS gateway provider to be used (INT-005) — this determines the SMS API integration specification.
3. Confirm whether the farmer portal (FR-FAR-042) is deferred to a specific named future phase or indefinitely deferred.
4. Confirm the deduction priority order in FR-PRO-061 with the Finance Director (loan repayment → cooperative levy → transport charges).
5. Confirm whether WHT (FR-PRO-029) applies to cooperative farmer payments or only to standard vendor service payments.
