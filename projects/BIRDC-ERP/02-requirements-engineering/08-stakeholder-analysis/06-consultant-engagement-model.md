# Section 6: Consultant Engagement Model

## 6.1 Role and Authority

Peter Bamuhigire, ICT Consultant (techguypeter.com), serves as the sole architect, specification author, and delivery authority for all BIRDC ERP documentation deliverables. He is identified as STK-005 in the stakeholder register and holds the following formally scoped authority:

- **Requirements authority:** Peter is the accountable author of all specification documents (SRS, User Stories, Stakeholder Analysis, Design Documents). He consults department heads for domain knowledge and presents drafts to the Finance Director and BIRDC Director for sign-off. No requirements are finalised without the Director's or Finance Director's explicit sign-off.
- **Architecture authority:** Peter designs the system architecture, module boundaries, data model, and integration specifications. The IT Administrator reviews and approves all infrastructure-facing architecture decisions.
- **Scope change authority:** Peter may recommend scope changes but cannot approve them unilaterally. All scope changes require written approval from the BIRDC Director.
- **Phase-gate authority:** Peter chairs all phase-gate reviews and presents the go/no-go recommendation. The BIRDC Director holds the final go/no-go decision authority.

---

## 6.2 Deliverable Milestones

The table below defines all consultant deliverables, the approving authority, and the acceptance condition for each.

| Milestone | Deliverable | Approving Authority | Acceptance Condition |
|---|---|---|---|
| M-01 | Project Kickoff and Context Documents | BIRDC Director | All 6 `_context/` files reviewed and confirmed accurate by Finance Director and Director |
| M-02 | Phase 1 SRS Document | Finance Director + BIRDC Director | All FR for F-001, F-002, F-003, F-004 reviewed; no unresolved V&V-FAIL tags |
| M-03 | Phase 2 SRS Document | Finance Director + BIRDC Director | Dual-mode accounting specification signed off; hash chain design approved |
| M-04 | Phase 3 SRS Document | Procurement Manager + Finance Director | PPDA workflow and 5-stage cooperative procurement specification approved |
| M-05 | Phase 4 SRS Document | Production Manager + QC Manager | Mass balance specification (BR-008) and CoA template design approved |
| M-06 | Phase 5 SRS Document | Finance Director + HR Manager | Payroll specification (PAYE, NSSF, LST) signed off |
| M-07 | Phase 6 SRS Document | BIRDC Director | R&D and Administration module specifications approved |
| M-08 | User Stories Document (this document's companion) | Finance Director + BIRDC Director | Minimum 65 user stories; all 17 modules covered; acceptance criteria verified as deterministic |
| M-09 | Stakeholder Analysis Document (this document) | BIRDC Director | All 29 stakeholders registered; RACI, communication plan, and concern register complete |
| M-10 | Phase 7 Hardening and Go-Live Plan | IT Administrator + BIRDC Director | Penetration test scope agreed; load test scenario confirmed; training plan approved |
| M-11 | Final Handover Package | BIRDC Director | All deliverables compiled; IT Administrator confirms infrastructure and maintenance documentation complete; consultant formally exited |

---

## 6.3 Sign-Off Authority Matrix

| Document Type | First Reviewer | Approving Authority | Sign-Off Format |
|---|---|---|---|
| SRS Phase Documents (M-02 to M-07) | Finance Director | BIRDC Director | Signed approval email or signed cover page |
| User Stories and Stakeholder Analysis | Finance Director | BIRDC Director | Signed approval email |
| Architecture and Data Model | IT Administrator | BIRDC Director | Signed approval email |
| Payroll Specification | Finance Director + HR Manager | Finance Director (financial authority) | Signed approval email |
| PPDA Workflow and Procurement Specification | Procurement Manager | Finance Director + BIRDC Director | Signed approval email |
| CoA and QC Templates | QC Manager | Finance Director | Signed approval email |
| Go-Live Plan | IT Administrator | BIRDC Director | Signed approval email |
| Final Handover | IT Administrator | BIRDC Director | Formal handover certificate, signed by both parties |

---

## 6.4 Handover Plan

The handover transfers full operational and maintenance responsibility from the consultant to BIRDC's internal team. Handover is not a single event; it is a phased transfer of knowledge and accountability that begins at Phase 4 and completes 30 days after Phase 7 go-live.

### Handover Phases

1. **Phase 4 knowledge transfer (during build):** Peter documents the architecture decision records (ADRs) for every non-obvious design decision. IT Administrator reviews and acknowledges each ADR.

2. **Phase 5 knowledge transfer:** Payroll configuration guide and PAYE/NSSF/LST tax band update procedure delivered to Finance Director. Finance Director confirms she can update tax bands without developer involvement (per DC-002).

3. **Phase 7 pre-go-live handover preparation:** Peter delivers to the IT Administrator:
   - System Administration Guide (user management, role configuration, backup management, integration configuration).
   - Maintenance SOP (database health checks, backup verification, EFRIS retry queue monitoring).
   - Incident escalation procedure (what the IT Administrator does if a critical failure occurs after consultant exit).
   - Training materials for all user groups.

4. **Go-live hypercare (30 days post go-live):** Peter remains available for critical issue resolution via a defined response SLA: Priority 1 (system down) — 4-hour response; Priority 2 (critical function unavailable) — 1 business day; Priority 3 (non-critical issue) — 3 business days.

5. **Formal handover and exit:** At the end of the 30-day hypercare period, Peter presents the Final Handover Package to the IT Administrator and BIRDC Director. Both parties sign the handover certificate. Peter's engagement ends.

### Handover Package Contents

- All SRS and design documents in PDF and source format.
- Fully populated `_context/` project folder.
- System configuration guide.
- User manuals for each role (web ERP and each Android app).
- Training materials (slides and quick reference cards).
- Architecture decision record log.
- Test results and UAT sign-off records.
- Penetration test report and remediation log.
- Load test report.
- PPDA procurement documentation for the ERP system itself.

---

## 6.5 Consultant Independence and Conflict of Interest

Peter Bamuhigire operates as an independent ICT consultant. He has no financial interest in any software vendor, hosting provider, or implementation partner that may be engaged by BIRDC to build the ERP system based on these specifications. The specifications are technology-neutral: they describe what the system must do, not which vendor or technology stack must be used.

Peter will declare any material relationship with a prospective vendor in writing to the BIRDC Director before that vendor is shortlisted for any BIRDC ERP procurement. BIRDC retains the right to exclude Peter from any evaluation process where a conflict of interest, real or perceived, exists.

All intellectual property in the delivered specification documents is transferred to BIRDC / PIBID upon payment of consultant fees. BIRDC may use, reproduce, and modify the documents without restriction after handover.
