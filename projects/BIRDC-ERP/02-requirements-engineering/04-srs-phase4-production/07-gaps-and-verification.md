# 6. Context Gaps, Verification Annotations, and Human Review Gate

## 6.1 Open Context Gaps

The following gaps were identified during requirements generation. No assumption has been made to fill these gaps; the corresponding requirements are marked with [CONTEXT-GAP] tags and flagged below. No downstream Phase 4 development activity that depends on these gaps may begin until the gap is resolved.

| Gap ID | Requirement(s) Affected | Description | Owner | Severity |
|---|---|---|---|---|
| GAP-010 | FR-QC-022, FR-QC-023, FR-QC-024, FR-QC-025, FR-QC-026, FR-QC-027, FR-QC-066 | Exact QC parameter requirements and document formats for all 5 export markets (South Korea MFDS, EU/Italy Codex Alimentarius, Saudi Arabia SFDA, Qatar MOPH, USA FDA) are not yet provided by the BIRDC QC Manager. Export CoA templates cannot be designed without these specifications. | BIRDC QC Manager (STK-010) | High |

**Resolution required:** The BIRDC QC Manager must supply the full parameter list (name, unit, USL, LSL), acceptable result format, document layout requirements, and any market-specific declarations for each of the 5 destination markets before export CoA template development commences.

---

## 6.2 Glossary Gaps

The following terms are used in this document but are not yet defined in `_context/glossary.md`. These must be added before the final document version is issued.

| Term | Used In | Definition Needed |
|---|---|---|
| Cp | FR-QC-032 | Process capability index — ratio of specification width to 6-sigma process spread |
| Cpk | FR-QC-032, FR-QC-033 | Process capability index adjusted for process centering |
| UCL | FR-QC-030 | Upper Control Limit — statistical boundary on SPC control chart |
| LCL | FR-QC-030 | Lower Control Limit — statistical boundary on SPC control chart |
| USL | FR-QC-002, FR-QC-030 | Upper Specification Limit — maximum acceptable value for a quality parameter |
| LSL | FR-QC-002, FR-QC-030 | Lower Specification Limit — minimum acceptable value for a quality parameter |
| MFDS | FR-QC-022 | Ministry of Food and Drug Safety — South Korea's food import regulatory authority |
| SFDA | FR-QC-024 | Saudi Food and Drug Authority |
| MOPH | FR-QC-025 | Qatar Ministry of Public Health |
| Cpk Threshold | FR-QC-033 | The minimum acceptable $C_{pk}$ value (default 1.33) below which a process is flagged as a capability concern |
| Room (SQLite) | NFR-P-002 | Android Jetpack Room persistence library providing an abstraction layer over SQLite for local offline data storage |

---

## 6.3 Requirement Traceability Matrix — Phase 4

Every functional requirement maps to a business goal in the vision document. The following table documents traceability for all Phase 4 requirements.

| Requirement Range | Business Goal (from vision.md) | Design Covenant(s) | Business Rule(s) |
|---|---|---|---|
| FR-MFG-001 to FR-MFG-007 | Goal 1 (Operational unity), Goal 4 (Circular economy visibility) | DC-002, DC-003, DC-007 | — |
| FR-MFG-008 to FR-MFG-012 | Goal 4 (Circular economy visibility) | DC-002, DC-003, DC-007 | BR-008 |
| FR-MFG-013 to FR-MFG-020 | Goal 1 (Operational unity), Goal 4 | DC-002, DC-003, DC-005 | BR-003, BR-004, BR-008 |
| FR-MFG-021 to FR-MFG-024 | Goal 1, Goal 4 | DC-003, DC-005 | BR-007, BR-008 |
| FR-MFG-025 to FR-MFG-030 | Goal 1 (Operational unity) | DC-001, DC-002, DC-003 | BR-003 |
| FR-MFG-031 to FR-MFG-033 | Goal 1, Goal 4 | DC-003 | — |
| FR-MFG-034 to FR-MFG-037 | Goal 4 | DC-003, DC-005 | BR-004, BR-008 |
| FR-MFG-038 to FR-MFG-041 | Goal 4 (Mass balance — complete circular economy) | DC-002, DC-003 | BR-008 |
| FR-MFG-042 to FR-MFG-045 | Goal 1 | DC-002, DC-003 | — |
| FR-MFG-046 to FR-MFG-050 | Goal 2 (Financial integrity), Goal 1 | DC-002, DC-003 | — |
| FR-MFG-051 to FR-MFG-055 | Goal 2 (Financial integrity) | DC-003, DC-004 | — |
| FR-MFG-056 to FR-MFG-066 | Goal 1, Goal 3 (Agent accountability) | DC-001, DC-005 | DC-005 |
| FR-QC-001 to FR-QC-004 | Goal 1 | DC-002, DC-003 | — |
| FR-QC-005 to FR-QC-012 | Goal 1, Goal 3 (Farmer payment via quality grade) | DC-002, DC-003 | — |
| FR-QC-013 to FR-QC-016 | Goal 1 | DC-003 | BR-004 |
| FR-QC-017 to FR-QC-028 | Goal 1, Goal 3 (Export compliance) | DC-002, DC-003 | BR-004, BR-017 |
| FR-QC-029 to FR-QC-034 | Goal 1 | DC-002 | — |
| FR-QC-035 to FR-QC-041 | Goal 1, Goal 2 | DC-002, DC-003 | — |
| FR-QC-042 to FR-QC-047 | Goal 1 | DC-002, DC-003 | — |
| FR-QC-048 to FR-QC-052 | Goal 1 | DC-002, DC-003 | — |
| FR-QC-053 to FR-QC-055 | Goal 1, Goal 2 | DC-003 | BR-004, BR-017 |
| FR-QC-056 to FR-QC-068 | Goal 1, Goal 2 | DC-003 | — |

---

## 6.4 Requirement Count Summary

| Module | Requirement ID Range | Count |
|---|---|---|
| F-011 Manufacturing & Production | FR-MFG-001 to FR-MFG-066 | 66 |
| F-012 Quality Control & Laboratory | FR-QC-001 to FR-QC-068 | 68 |
| Non-Functional Requirements | NFR-P-001 to NFR-PR-001 | 11 |
| **Total** | | **145** |

---

## 6.5 Human Review Gate

*Per the PRIME Methodology (Kodukula & Vinueza, 2024) and IEEE 1012 V&V SOP:* this document is a draft requiring human verification before it is treated as a finalised requirements baseline. The consultant presents the following checklist to the BIRDC stakeholders for review:

1. Review all FR-MFG requirements against the Factory / Production Manager's (STK-009) operational understanding of the production process.
2. Review all FR-QC requirements against the QC Manager's (STK-010) laboratory workflows and inspection practices.
3. Resolve GAP-010 by providing the QC Manager's export market parameter specifications for all 5 destination markets.
4. Add all terms listed in Section 6.2 to `_context/glossary.md`.
5. Confirm the configured overhead absorption rate with the Finance Director (STK-002) before production costing requirements (FR-MFG-046 to FR-MFG-050) are developed.
6. Confirm the ±2% mass balance tolerance with the Production Manager before FR-MFG-038 through FR-MFG-041 are baselined.
7. Confirm the 6 processing stations listed in FR-MFG-031 against the actual Nyaruzinga factory layout.

*No downstream Phase 4 development activity may commence until STK-009 and STK-010 acknowledge this Human Review Gate in writing.*

---

## 6.6 IEEE 830 Completeness Self-Check

| IEEE 830 Criterion | Status |
|---|---|
| All FRs follow stimulus-response pattern | Pass |
| All FRs have a deterministic test oracle | Pass |
| All unresolved gaps flagged with [CONTEXT-GAP] | Pass — 1 gap (GAP-010) flagged across 7 requirements |
| No vague adjectives without measurable thresholds | Pass |
| All acronyms defined on first use | Pass (see Section 1.3) |
| All mathematical expressions use LaTeX | Pass |
| No requirement uses "fast", "reliable", "robust" without a metric | Pass |
| All NFRs specify measurable thresholds | Pass |
| Document has full traceability to business goals | Pass (Section 6.3) |
| Segregation of duties enforced at API layer (BR-003) | Pass — NFR-S-003 specifies API enforcement |
