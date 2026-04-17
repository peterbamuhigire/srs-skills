# Risk Register — Academia Pro

**Version:** 1.0
**Date:** 2026-03-28

*Risk scoring: Probability and Impact are rated H (High), M (Medium), or L (Low). Risk Score = Probability × Impact using a 3×3 ordinal matrix: H×H = 9, H×M = 6, M×M = 4, H×L = 3, M×L = 2, L×L = 1.*

---

## Risk Register

| Risk ID | Description | Probability | Impact | Score | Mitigation Strategy |
|---|---|---|---|---|---|
| **RISK-001** | **SchoolPay builds a competitive ERP.** SchoolPay deploys significant engineering resources to close the feature gap — UNEB grading, mobile apps, EMIS — within 24 months of Academia Pro's launch. Their ~11,000-school network becomes a moat against Academia Pro's primary conversion path. | M | H | 6 | Complete Phase 1–8 before SchoolPay reaches ERP parity (estimated 3–5 years for full feature depth). Secure 200+ schools with 2+ years of embedded data before the threat materialises. Strengthen non-payment moat: EMIS compliance, PDPO architecture, and offline sync are capabilities outside SchoolPay's core competency. Monitor SchoolPay's product announcements quarterly. |
| **RISK-002** | **BoU payment licence not obtained in time for Phase 3.** The Bank of Uganda Payment Systems Operator (PSO) licence process takes longer than anticipated, blocking direct MTN MoMo and Airtel Money integration for Phase 3. | M | M | 4 | Phase 1–2 revenue does not depend on direct mobile money — SchoolPay handles all payments. Phase 3 direct MoMo is additive, not foundational. Begin pre-application engagement with BoU at Phase 1 (action item in gap-analysis.md). Use a licensed aggregator (e.g., Beyonic, Pesawise) as a Phase 3 interim option if PSO licence is delayed. |
| **RISK-003** | **Solo team capacity bottleneck.** The 12-phase build plan is substantial for a 1–3-person team. A critical illness, a personal event, or scope creep on any phase delays go-live and revenue. | H | H | 9 | The 12-phase gate structure (Water-Scrum-Fall) prevents scope creep by locking requirements before each phase. Phase 1–8 scoped to deliver commercial viability first; Phase 11 pan-Africa is after sustainable revenue is established. Track velocity per sprint; if Phase 1 is 20%+ behind by Week 12, reduce Phase 1 scope to core SIS + Fees + Attendance + UNEB grading + Reports only, and defer optional modules to Phase 2. Budget for 1 freelance Laravel developer from Phase 3 onward if revenue permits. |
| **RISK-004** | **MoES changes the EMIS data format after Phase 1 build.** The Ministry updates the EMIS XML/CSV schema, invalidating Academia Pro's export format and breaking statutory compliance for all schools. | M | M | 4 | EMIS format is isolated in a dedicated `EmisExportService` class, not scattered across the codebase. A format change requires updating one service and its tests. Maintain direct contact with the MoES EMIS team; subscribe to MoES communications for format change notices. Phase 12 maintenance plan includes scheduled EMIS format review every academic year. |
| **RISK-005** | **Data breach and PDPO liability.** A security incident exposes student PII — names, NINs, LINs, health records — affecting multiple schools. The PDPO 2019 requires breach notification to the PDPO Office within 72 hours. Reputational damage could trigger school churn. | L | H | 3 | Layered security architecture: AES-256 at rest, TLS 1.3 in transit, OWASP Top 10 zero critical findings (Phase 8 penetration test), role-scoped data access, audit logging on every PII write. PDPO Office registration before Phase 8. Data Processing Agreements with each school. Incident response procedure documented in `09-governance-compliance/`. Phase 7 health data has additional safeguards (special category classification, restricted access roles). If breach occurs: isolate affected tenant immediately, notify PDPO Office within 72 hours, notify affected data subjects without undue delay. |
| **RISK-006** | **School churn — low retention.** Schools subscribe, enter their data, then cancel after Term 1 because the product does not deliver on the onboarding promise (too complex, training not effective, features missing). | M | H | 6 | Design Covenant is a hard constraint on complexity: 30-minute onboarding, role-scoped UX, embedded video help per module. Phase 9 trial schools (10–20) provide retention data before full commercial launch. Retention metric: ≥ 80% of pilot schools renew at 12 months. If a school cancels, exit interview is mandatory — findings fed back into Phase 12 improvement cycle. 90-day data grace period removes the "I'll cancel and come back" risk by not penalising temporary lapses. |
| **RISK-007** | **Pan-Africa localisation complexity — currency, curriculum, and regulation diverge significantly.** The country-profile architecture works for payment and currency, but curriculum engine differences (WAEC vs. UNEB vs. KCSE) require more development than estimated, delaying Phase 11. | M | M | 4 | Pan-Africa (Phase 11) is after Uganda revenue is stable. Each country's curriculum engine is a self-contained service. Phase 11 scope is not commercially necessary for break-even (33 Uganda schools achieves that). If Phase 11 is delayed by 6–12 months, Uganda revenue continues unaffected. Prioritise Kenya first (KCSE grading is structurally similar to UNEB; M-Pesa Daraja API is well-documented). |
| **RISK-008** | **UNEB changes grading rules without adequate notice.** UNEB modifies PLE, UCE, or UACE grading rules mid-development, requiring the grading engine to be rebuilt. | L | H | 3 | The grading engine is data-driven: grading rules are configuration, not hardcoded. A rule change requires updating the rule set and rerunning tests against UNEB sample sheets — not a full rebuild. Maintain direct contact with UNEB; validate engine against each published examination cycle's results. Phase 12 maintenance includes annual UNEB rule review. |
| **RISK-009** | **SchoolPay API changes or removes a critical endpoint.** SchoolPay changes its API contract (endpoint URLs, authentication scheme, or payload format) without adequate notice, breaking Academia Pro's reconciliation system. | L | H | 3 | All SchoolPay API calls are isolated in a `SchoolPayGateway` class — a facade pattern. An API change requires updating one class. Nightly polling fallback (`SyncSchoolTransactions`) is a secondary reconciliation layer that reduces real-time dependency. Bursar manual reconciliation is a tertiary fallback. Formal merchant partnership agreement with SchoolPay should include an advance notice clause for breaking API changes. |
| **RISK-010** | **Android app rejected from Google Play Store.** Google Play Store review rejects one or more of the 6 Android apps for policy compliance reasons (permissions, data safety declaration, or PDPO/privacy policy gaps), delaying Phase 8 go-live. | L | M | 2 | Follow Google Play Store compliance guidelines from Phase 1 planning (data safety section, sensitive permissions declaration, privacy policy URL). Run an internal Play Store compliance check at Phase 7 completion — before the Phase 8 submission. Address rejection criteria immediately; average Play Store review time is 3–7 days for re-submissions. |

---

## Risk Heatmap

```
        IMPACT
         L     M     H
       +-----+-----+-----+
  H    |     |     | R03 |
       +-----+-----+-----+
  M    |     |R02  | R01 |
P      |     |R04  | R06 |
R      |     |R007 |     |
O      +-----+-----+-----+
B  L   | R10 |     | R05 |
       |     |     | R08 |
       |     |     | R09 |
       +-----+-----+-----+
```

**Critical risks (score ≥ 6):**
- **RISK-003** (Solo team capacity, score 9) — highest priority; mitigated by phase gating and scope management
- **RISK-001** (SchoolPay ERP competition, score 6) — mitigated by speed to Phase 8 and moat depth
- **RISK-006** (School churn, score 6) — mitigated by Design Covenant and Phase 9 pilot validation

---

## Action Items from Risk Register

1. Begin BoU PSO licence pre-application engagement at Phase 1 (RISK-002).
2. Contact SchoolPay for formal merchant partnership agreement with API change notice clause (RISK-009).
3. Track Phase 1 build velocity from Week 1; define scope reduction triggers at Week 12 if behind schedule (RISK-003).
4. Register Chwezi Core Systems with the PDPO Office before Phase 8 go-live (RISK-005).
5. Schedule a Google Play Store compliance self-audit at Phase 7 completion (RISK-010).
