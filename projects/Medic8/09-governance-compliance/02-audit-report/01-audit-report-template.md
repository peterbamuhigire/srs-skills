# Audit Report Template -- Medic8

**Document ID:** Medic8-AUD-[SEQUENCE]
**Version:** [VERSION]
**Standards:** IEEE 1012-2016 (V&V), ISO/IEC 15504 (Process Assessment), Uganda PDPA 2019

---

## 1. Audit Header

| Field | Value |
|---|---|
| **Project** | Medic8 -- Multi-Tenant Healthcare Management System |
| **Phase** | [Phase number and name, e.g., "Phase 1 -- Core Clinical Platform"] |
| **Audit Type** | [Requirements / Design / Code / Security / Clinical Safety / Compliance / Data Protection] |
| **Audit ID** | AUD-[PHASE]-[TYPE]-[SEQUENCE], e.g., AUD-P1-REQ-001 |
| **Auditor** | [Name, role, and organisation] |
| **Audit Date** | [YYYY-MM-DD] |
| **Audit Period** | [Start date] to [End date] |
| **Report Date** | [YYYY-MM-DD] |
| **Distribution** | [List of recipients] |
| **Classification** | Confidential -- contains references to patient health information architecture |
| **Integrity Level** | [IL-1 / IL-2 / IL-3 / IL-4 per IEEE 1012-2016 Table 1] |

---

## 2. Scope

### 2.1 Artifacts Audited

List all documents and artifacts reviewed during this audit:

| # | Artifact | Version | Location |
|---|---|---|---|
| 1 | [e.g., Software Requirements Specification] | [e.g., 1.0] | [e.g., `02-requirements-engineering/01-srs/`] |
| 2 | [e.g., High-Level Design Document] | [e.g., 1.0] | [e.g., `03-design-documentation/01-hld/`] |
| 3 | [e.g., Entity-Relationship Diagram] | [e.g., 1.0] | [e.g., `03-design-documentation/04-database-design/`] |
| 4 | [Continue for all audited artifacts] | | |

### 2.2 Standards Applied

| Standard | Scope of Application |
|---|---|
| IEEE 830-1998 | SRS structure and requirement quality (correctness, unambiguity, completeness, verifiability) |
| IEEE 1012-2016 | Verification and validation processes, integrity levels, anomaly identification |
| IEEE 29148-2018 | Requirements engineering life cycle processes |
| Uganda PDPA 2019 | Data protection compliance for patient health information |
| HIV/AIDS Prevention and Control Act 2014 | Mandatory confidentiality of HIV test results (Section 18) |
| Uganda MoH HMIS Standards | HMIS 105, HMIS 108, HMIS 033b reporting compliance |
| HL7 FHIR R4 | Interoperability standard compliance |
| ISO 31000 | Risk management framework |
| ISO/IEC 15504 | Process assessment model for audit artifact traceability |

### 2.3 Out of Scope

List any artifacts, modules, or standards explicitly excluded from this audit and the reason for exclusion:

- [e.g., "Phase 2-4 requirements -- not yet elaborated"]
- [e.g., "Third-party library source code -- covered by dependency audit"]

---

## 3. Findings

### 3.1 Findings Summary

| Severity | Count |
|---|---|
| Critical | [count] |
| Major | [count] |
| Minor | [count] |
| Observation | [count] |
| **Total** | **[count]** |

### 3.2 Findings Detail

| Finding ID | Severity | Category | Description | Affected Artifact | Recommendation | Status |
|---|---|---|---|---|---|---|
| F-[AUD-ID]-001 | Critical / Major / Minor / Observation | Correctness / Consistency / Completeness / Verifiability / Traceability / Compliance | [Clear description of the finding. State what was expected per the applicable standard and what was observed.] | [Document name, section, and requirement ID] | [Specific, actionable recommendation with a measurable completion criterion] | Open / In Progress / Resolved / Deferred |
| F-[AUD-ID]-002 | | | | | | |
| F-[AUD-ID]-003 | | | | | | |

**Severity definitions:**

- **Critical:** Requirement or design defect that, if unresolved, would result in patient harm, data breach, regulatory violation, or system failure. Blocks release.
- **Major:** Defect that materially reduces system quality, creates a traceability gap, or violates a binding standard. Must be resolved before the phase gate.
- **Minor:** Defect that does not materially affect system correctness or safety but should be corrected to maintain document quality.
- **Observation:** Suggestion for improvement that does not constitute a defect. No mandatory action required.

**Category definitions:**

- **Correctness:** Artifact does not match stakeholder intent documented in `_context/vision.md`
- **Consistency:** Terminology, identifiers, or logical structure conflict between sections or documents
- **Completeness:** Missing requirement, missing test case, missing design mapping, or missing context file data
- **Verifiability:** Requirement or test case does not provide a deterministic pass/fail criterion
- **Traceability:** Requirement cannot be traced forward to design/test or backward to business goal
- **Compliance:** Artifact violates a regulatory requirement (PDPA, HIV Act, HMIS, FHIR)

---

## 4. V&V Assessment

### 4.1 Correctness

Does the artifact accurately reflect stakeholder intent as documented in `_context/vision.md`?

| Assessment Area | Result | Evidence |
|---|---|---|
| Business goals alignment | [Pass / Fail / Partial] | [Reference specific vision.md goals and how they map to the audited artifact] |
| Stakeholder role coverage | [Pass / Fail / Partial] | [Confirm all 18 roles from stakeholders.md are addressed where applicable] |
| Domain constraint adherence | [Pass / Fail / Partial] | [Confirm domain.md regulatory requirements are reflected] |
| Clinical workflow accuracy | [Pass / Fail / Partial] | [Confirm business rules from business_rules.md are correctly implemented] |

**Correctness verdict:** [Pass / Conditional Pass / Fail]

### 4.2 Consistency

Is terminology uniform across sections and documents?

| Assessment Area | Result | Evidence |
|---|---|---|
| Identifier consistency (FR/NFR IDs) | [Pass / Fail / Partial] | [Verify no duplicate or skipped IDs] |
| Terminology uniformity | [Pass / Fail / Partial] | [Verify glossary terms used consistently] |
| Cross-document alignment | [Pass / Fail / Partial] | [Verify SRS Section 3.1 aligns with Section 3.2, HLD aligns with LLD] |
| Business rule cross-references | [Pass / Fail / Partial] | [Verify BR-xxx references are valid and bidirectional] |

**Consistency verdict:** [Pass / Conditional Pass / Fail]

### 4.3 Completeness

Does every context file gap have a corresponding requirement? Does every requirement have all required elements?

| Assessment Area | Result | Evidence |
|---|---|---|
| Gap analysis coverage | [Pass / Fail / Partial] | [Cross-reference gap-analysis.md HIGH-001 through HIGH-007 against requirements] |
| Requirement element completeness | [Pass / Fail / Partial] | [Verify each FR has: ID, stimulus, response, inputs, outputs, business rule ref, verifiability] |
| NFR metric completeness | [Pass / Fail / Partial] | [Verify each NFR has a measurable threshold, not vague adjectives] |
| Edge case coverage | [Pass / Fail / Partial] | [Verify context file edge cases have corresponding FRs] |

**Completeness verdict:** [Pass / Conditional Pass / Fail]

### 4.4 Verifiability

Does every requirement have a deterministic test case with a clear pass/fail criterion?

| Assessment Area | Result | Evidence |
|---|---|---|
| FR test oracle quality | [Pass / Fail / Partial] | [Sample 10 FRs; verify each has deterministic expected result] |
| NFR measurement criterion | [Pass / Fail / Partial] | [Verify each NFR has a numeric threshold or observable outcome] |
| Test case traceability | [Pass / Fail / Partial] | [Verify RTM links every requirement to at least 1 test case] |
| Boundary condition coverage | [Pass / Fail / Partial] | [Verify edge cases have explicit test cases] |

**Verifiability verdict:** [Pass / Conditional Pass / Fail]

---

## 5. Anomaly Identification

Per IEEE 1012-2016 Section 9.3, all anomalies discovered during the audit are recorded below.

| Anomaly ID | Type | Description | Resolution | Owner | Due Date |
|---|---|---|---|---|---|
| A-[AUD-ID]-001 | [CONTEXT-GAP / GLOSSARY-GAP / V&V-FAIL / TRACE-GAP / SMART-FAIL / VERIFIABILITY-FAIL] | [Description of the anomaly, including what was expected and what was found] | [Required corrective action] | [Person responsible] | [YYYY-MM-DD] |
| A-[AUD-ID]-002 | | | | | |
| A-[AUD-ID]-003 | | | | | |

**Anomaly type definitions:**

- `[CONTEXT-GAP]` -- required context is absent from `_context/` files
- `[GLOSSARY-GAP]` -- term used in output is not defined in `_context/glossary.md`
- `[V&V-FAIL]` -- requirement fails verification/validation
- `[TRACE-GAP]` -- requirement has no traceability to a business goal or test case
- `[SMART-FAIL]` -- non-functional requirement lacks a specific, measurable metric
- `[VERIFIABILITY-FAIL]` -- expected result is not a deterministic test oracle

---

## 6. Recommendations

### 6.1 Phase Gate Decision

| Decision | Criteria |
|---|---|
| **Go** | Zero Critical findings AND zero Major findings AND all anomalies have assigned owners and due dates |
| **Conditional Go** | Zero Critical findings AND all Major findings have approved remediation plans with due dates before the next phase gate |
| **No-Go** | One or more Critical findings remain unresolved OR Major findings exceed the remediation capacity before the next phase gate |

**Recommendation:** [Go / Conditional Go / No-Go]

**Rationale:** [2-3 sentences explaining the recommendation based on the findings]

### 6.2 Required Actions Before Next Phase Gate

| # | Action | Owner | Due Date | Dependency |
|---|---|---|---|---|
| 1 | [e.g., Resolve HIGH-001: Licence drug interaction database] | [Name] | [Date] | [e.g., Blocks FR-OPD-008 implementation] |
| 2 | [e.g., Resolve HIGH-002: Complete PDPA compliance documentation] | [Name] | [Date] | [e.g., Blocks data protection audit] |
| 3 | [Continue for all required actions] | | | |

### 6.3 Observations for Continuous Improvement

- [e.g., "Consider automating RTM maintenance to reduce manual traceability effort"]
- [e.g., "Document drug interaction database licensing decision before Phase 1 development sprint 1"]

---

## 7. Sign-Off

| Role | Name | Decision | Signature | Date |
|---|---|---|---|---|
| Project Owner | [Name] | [Go / Conditional Go / No-Go] | | [YYYY-MM-DD] |
| Clinical Safety Officer | [Name] | [Go / Conditional Go / No-Go] | | [YYYY-MM-DD] |
| Data Protection Officer | [Name] | [Go / Conditional Go / No-Go] | | [YYYY-MM-DD] |
| Lead Architect | [Name] | [Go / Conditional Go / No-Go] | | [YYYY-MM-DD] |
| Quality Assurance Lead | [Name] | [Go / Conditional Go / No-Go] | | [YYYY-MM-DD] |

---

## Appendix A: Audit Checklist

The following checklist was used during this audit. Items marked [x] were verified; items marked [ ] were not applicable or deferred.

### A.1 Requirements Audit Checklist

- [ ] Every FR has a unique identifier
- [ ] Every FR follows stimulus-response format
- [ ] Every FR includes input specifications
- [ ] Every FR includes error conditions
- [ ] Every FR cross-references applicable business rules
- [ ] Every FR has a verifiability section with deterministic test oracle
- [ ] Every NFR has a measurable metric (no vague adjectives)
- [ ] All PDPA-relevant requirements reference specific PDPA sections
- [ ] All HIV-related requirements enforce Section 18 confidentiality
- [ ] All HMIS requirements reference specific HMIS form numbers

### A.2 Design Audit Checklist

- [ ] HLD covers all FR groups (AUTH, TNT, REG, OPD, LAB, PHR, BIL, APT, RBAC)
- [ ] LLD specifies service classes for every FR group
- [ ] ERD defines tables for all data entities referenced in FRs
- [ ] API spec defines endpoints for all FRs requiring HTTP interfaces
- [ ] Tenant isolation (BR-DATA-004) is enforced at HLD, LLD, and ERD levels
- [ ] Offline architecture (HLD Section 6) addresses NFR-HC-013

### A.3 Clinical Safety Audit Checklist

- [ ] Drug interaction checking covers all 4 tiers (BR-CLIN-004)
- [ ] Paediatric dosing safeguards are specified (BR-CLIN-006)
- [ ] Critical value escalation cascade is defined (BR-CLIN-003)
- [ ] Five Rights CPOE enforcement is specified (BR-CLIN-008)
- [ ] NEWS2 early warning score is calculated (BR-CLIN-007)
- [ ] Medication reconciliation is enforced at transitions (BR-CLIN-005)
- [ ] Tall Man Lettering is applied to LASA drugs (BR-RX-003)
- [ ] Narcotic register maintains running balance (BR-RX-001)

### A.4 Compliance Audit Checklist

- [ ] PDPA Section 5 (principles of data processing) addressed
- [ ] PDPA Section 10 (consent requirements) addressed
- [ ] PDPA Section 16 (rights of data subjects) addressed
- [ ] PDPA Section 22 (security of personal data) addressed
- [ ] PDPA Section 24 (record of processing) addressed
- [ ] PDPA Section 31 (breach notification) addressed
- [ ] PDPA Section 34 (cross-border transfer) addressed
- [ ] HIV/AIDS Act Section 18 (mandatory confidentiality) addressed
- [ ] HMIS 105, 108, 033b reporting compliance verified
- [ ] DHIS2 integration capability confirmed

---

## Appendix B: Document Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | [Name] | Initial audit report |
| | | | |
