# Go / No-Go Recommendation — Academia Pro

**Version:** 1.0
**Date:** 2026-03-28
**Decision Authority:** Peter / Chwezi Core Systems

---

## 1. Recommendation

**GO.**

The evidence presented in this business case supports proceeding with Academia Pro development. The recommendation is conditional on completing the Phase 1 gate criteria listed in Section 3 of this document before the first line of production code is written.

---

## 2. Decision Rationale

### 2.1 Factors Supporting GO

| Factor | Evidence |
|---|---|
| Quantified market gap | ~25,000 Uganda schools; majority operating on paper or Excel. No competitor meets all 6 requirements identified in Section 02. |
| Payment integration path is clear | SchoolPay API documented; sandbox contact identified (`[email protected]`); no BoU licence required for Phase 1. Schools face zero payment disruption. |
| Break-even is achievable at low scale | 33 Starter-tier schools covers Phase 8+ infrastructure costs. Year 1 conservative target of 50 schools is above break-even. |
| Competition window is open | SchoolPay ERP is structurally immature (January 2024 launch). ShuleKeeper has documented compliance and technical deficiencies. No competitor has confirmed UNEB grading + EMIS + mobile apps + PDPO compliance simultaneously. |
| Technology is standard and well-understood | PHP/Laravel, React, Kotlin/Jetpack Compose, MySQL, Redis — a solo developer with this stack can build Phase 1 without exotic dependencies. |
| Regulatory requirements are documented and solvable | PDPO 2019, UNEB grading rules, EMIS format, and BoU payment regulations are all identified and mapped to concrete actions. None require multi-year licensing processes before Phase 1 launch. |
| Phase 8 go-live is a defined target, not open-ended | 12 phases, each with gate criteria. Revenue begins at Phase 8 (or earlier at Phase 9 pilot). The Water-Scrum-Fall methodology enforces sign-off before each phase begins. |

### 2.2 Factors Warranting Caution

| Factor | Assessment |
|---|---|
| Solo team capacity (RISK-003, score 9) | The single highest-risk item. Mitigated by phase gating and a defined scope reduction trigger (if Phase 1 is 20%+ behind at Week 12, reduce scope to core SIS + Fees + Attendance + UNEB + Reports). |
| 8 HIGH-priority gaps unresolved | Development must not begin until all 8 HIGH gaps are resolved. Starting with unresolved gaps introduces architectural rework mid-build — the most expensive form of technical debt. |
| SchoolPay sandbox not yet obtained | Phase 1 fee module cannot be fully developed or tested without SchoolPay sandbox credentials. This is a pre-development action item, not a reason to delay the GO decision. |
| PDPO Office not yet registered | Registration is a pre-go-live requirement, not a pre-development requirement. However, the compliance architecture (data model, encryption, retention rules) must be designed into Phase 1. |

No factor in the Caution column is a blocker for a GO decision — each has a defined resolution action. A NO-GO decision would be appropriate only if the SchoolPay API were found to be inaccessible for third-party integration, or if the UNEB grading rules were unavailable for implementation. Neither condition has been confirmed.

---

## 3. Phase 1 Gate Criteria

The following criteria must all be met before Phase 1 development begins. This is the formalised gate requirement from `_context/metrics.md`:

| # | Criterion | Status | Owner |
|---|---|---|---|
| 1 | `HIGH-001` Security architecture document written and reviewed | Not started | Peter |
| 2 | `HIGH-002` Consolidated ERD drawn (Phase 1 entities minimum) | Not started | Peter |
| 3 | `HIGH-003` OpenAPI 3.1 spec written for all Phase 1 endpoints | Not started | Peter |
| 4 | `HIGH-004` Academic year lifecycle management spec completed | Not started | Peter |
| 5 | `HIGH-005` Full RBAC permission matrix produced | Not started | Peter |
| 6 | `HIGH-006` Double-payment prevention rules fully specified | Not started | Peter |
| 7 | `HIGH-007` Data migration specification written | Not started | Peter |
| 8 | `HIGH-008` Uganda PDPO 2019 compliance document written; PDPO registration initiated | Not started | Peter |

All 8 gates are documented in `_context/gap-analysis.md`. Development of Phase 1 is **blocked** until all 8 are marked complete and reviewed.

---

## 4. Immediate Next Steps

Execute the following actions in order. Actions 1–4 are prerequisites for Phase 1 gate resolution. Actions 5–8 run in parallel.

1. **Resolve HIGH-001 through HIGH-008.** Work through each gap in order. Estimated effort: 15–25 hours of specification work. Output: 8 documents written to the paths specified in `_context/gap-analysis.md`.

2. **Contact SchoolPay for sandbox credentials.** Email `[email protected]`. Request: merchant API documentation, sandbox environment access, and the formal merchant onboarding process. This must be completed before Phase 1 fee module development begins. Target: sandbox active within 4 weeks.

3. **Contact UNEB for grading sample data.** Obtain the candidate registration manual and a set of sample mark sheets (PLE, UCE, UACE) for grading engine validation. UNEB grading engine cannot be validated without official sample data. Target: contact initiated within 2 weeks.

4. **Register Chwezi Core Systems with the PDPO Office.** Download the Uganda Data Protection and Privacy Act 2019 from ULRC (ulrc.go.ug). Initiate Data Controller registration with the Personal Data Protection Office. This is a legal obligation — not a pre-development action but a pre-go-live obligation. Starting early reduces Phase 8 risk.

5. **Confirm cloud hosting decision.** Decide between AWS, Azure, and a local Uganda data centre for Phase 8+ production. This decision affects PDPO data residency requirements (Uganda PDPO 2019 has data localisation provisions that should be assessed). Document decision in `_context/tech_stack.md`.

6. **Register software copyright with URSB.** Under the Uganda Copyright Act 2006, register Academia Pro as a software work with the Uganda Registration Services Bureau before Phase 8 go-live. Begin the registration process during Phase 3 to avoid a last-minute blocker.

7. **Draft Data Processing Agreements (DPAs) for pilot schools.** DPAs must be signed before any school data enters the production system. Draft the DPA template during Phase 7. One signed DPA per school is required before Phase 9 trial onboarding.

8. **Engage BoU for PSO licence pre-application guidance.** Phase 3 direct MTN MoMo/Airtel Money processing requires a BoU Payment Systems Operator licence. Contact BoU's Payment Systems department to understand the application timeline and requirements. This is a Phase 3 preparation action — it can run in parallel with Phase 1–2 development.

---

## 5. Decision Summary

| Dimension | Assessment |
|---|---|
| Market opportunity | Confirmed — quantified gap, documented competitive weaknesses |
| Technical feasibility | Confirmed — standard technology stack, documented architecture |
| Financial viability | Confirmed — break-even at 33 schools; conservative Year 3 revenue ~UGX 812M |
| Regulatory pathway | Documented — PDPO, UNEB, EMIS, BoU all identified and solvable |
| Primary risk | Solo team capacity (RISK-003) — mitigated by phase gating |
| Blocker to proceeding | 8 HIGH-priority gaps must be resolved before Phase 1 development begins |
| **Decision** | **GO — conditional on Phase 1 gate criteria completion** |
