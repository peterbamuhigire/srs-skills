# Executive Summary — Academia Pro Business Case

**Prepared by:** Chwezi Core Systems (chwezicore.com)
**Owner:** Peter
**Date:** 2026-03-28
**Document Version:** 1.0

---

## Opportunity

Uganda has approximately 25,000 registered primary and secondary schools (MoES 2023 estimate). The majority operate with paper registers, manual fee receipts, and Excel-based mark computation. Existing software options are either foreign-built (no MTN MoMo, no UNEB grading, no Uganda 3-term calendar), prohibitively expensive, or technically deficient — as evidenced by ShuleKeeper's 60-day data deletion policy, absence of mobile access, and developer-level WhatsApp as the primary support channel. SchoolPay, Uganda's dominant payment processor, launched an ERP product in January 2024 that is structurally immature, creating a well-defined window for a superior, Uganda-native platform.

The immediate addressable baseline is SchoolPay's ~11,000 connected schools, which already have payment infrastructure in place. Academia Pro integrates with SchoolPay in Phase 1, removing the payment migration barrier entirely.

---

## Proposed Solution

Academia Pro is a multi-tenant SaaS School Management Platform, architected Uganda-first and designed to scale across East and West Africa. It automates every repeatable school process — fee collection, attendance, examination grading, UNEB-compliant report cards, EMIS statutory reporting, parent communication — while remaining operable by a single administrator after module-specific training. The platform is built on a 12-phase roadmap: Phase 1–8 delivers the full Uganda web platform and Android apps; Phase 9–10 adds iOS; Phase 11 expands to Kenya, Tanzania, Nigeria, and Ghana.

Key differentiators:
- Automated UNEB grading for PLE, UCE, and UACE — zero manual computation
- SchoolPay integration in Phase 1 — schools keep their payment infrastructure
- EMIS export compliance — schools submit statutory reports without re-entering data
- Android-first mobile apps for teachers, parents, students, and bus drivers
- Uganda Data Protection and Privacy Act 2019 (PDPO) compliant architecture
- Zero-config onboarding: a Uganda school is operational within 30 minutes of signup

---

## Expected Return

*All figures are planning estimates. See Section 06 for assumptions and scenario detail.*

A conservative Year 3 scenario of 300 active schools at a blended average revenue per school of UGX 230,000/month yields:

$$AnnualRevenue = 300 \times 230{,}000 \times 12 = UGX\ 828{,}000{,}000\ (\approx USD\ 220{,}000)$$

An optimistic Year 3 scenario of 600 schools at the same blended ARPU yields approximately UGX 1,656,000,000 (~USD 440,000). Pan-Africa expansion (Phase 11) opens a total addressable market of 120,000+ additional schools across Kenya, Tanzania, Nigeria, and Ghana.

Infrastructure and operating costs at 300-school scale are estimated at UGX 12–18 million/month (hosting, SMS, WhatsApp API, Claude AI API), yielding a gross margin above 90% at scale — typical for multi-tenant SaaS on shared infrastructure.

---

## Recommendation

**Proceed.** The market gap is quantified, the competition is structurally weak, the payment integration path is clear (SchoolPay), and the regulatory framework (PDPO, UNEB, EMIS) is documented and solvable. The primary risk is solo-team execution capacity, which is mitigated by the 12-phase phased build plan and the Water-Scrum-Fall gate structure that prevents scope creep.

**Immediate next steps before Phase 1 development begins:**

1. Resolve all 8 HIGH-priority gaps documented in `_context/gap-analysis.md`.
2. Contact SchoolPay at `[email protected]` to obtain sandbox credentials.
3. Contact UNEB to obtain the candidate registration manual and sample mark sheets.
4. Register Chwezi Core Systems with the PDPO Office (Uganda).
5. Confirm Phase 1 gate criteria are met before writing the first line of production code.
