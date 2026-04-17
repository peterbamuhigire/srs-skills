# Product Requirements Document — Academia Pro

## Market Analysis

### Uganda Education Sector — Baseline

Uganda has approximately 21,000 registered primary schools and 4,500 registered secondary schools, with an estimated total of over 25,000 formal learning institutions when tertiary and vocational institutions are included (MoES Annual School Census, 2023 estimates). Enrolment in Universal Primary Education (UPE) exceeds 9 million pupils. The education sector is a large, underserved market for digital administration tools.

Fee collection volume is substantial. A secondary school with 600 students charging an average of UGX 600,000 per term generates UGX 360,000,000 (~USD 95,000) per term in fee inflows. A national platform processing fees across 500 schools approaches UGX 180 billion per year — a transaction volume that justifies the investment in payment infrastructure and compliance.

### Payment Infrastructure Maturity

SchoolPay is Uganda's dominant school fee processor, operating under a Bank of Uganda Payment Systems Operator licence and serving approximately 11,000 schools. This is the single most important market fact for Academia Pro's go-to-market strategy: SchoolPay schools have already digitalised their payment collection. They have payment codes, reconciliation habits, and parent awareness of mobile money fee payment. What they lack is a capable ERP layer above the payment processor.

SchoolPay launched its own ERP product in January 2024. The product is functionally immature at this stage — limited reporting, no UNEB grading engine, no offline PWA, no EMIS integration. Academia Pro enters this market as the superior ERP layer that already speaks SchoolPay's language. Schools using SchoolPay do not need to change their payment infrastructure; parents do not change their payment habits. Migration friction is lower than any competing scenario.

Mobile money penetration in Uganda exceeds 65% of adults (Bank of Uganda, 2024). MTN MobileMoney and Airtel Money dominate. This penetration extends to parents paying school fees — the majority of Uganda school fees now transit through mobile money channels, either directly to school accounts or via SchoolPay agent codes.

### Competitive Landscape

**Existing Uganda / East Africa products:**

- *SchoolPay ERP (January 2024):* Payment-native, weak on school management depth. No UNEB grading engine, no offline support, no mobile apps for teachers. Functional immaturity is a time-limited opportunity — SchoolPay will invest in their product.
- *Eduweb / Skuli / similar local tools:* Web-based, shallow feature sets. Typically fee management plus basic report cards. No EMIS integration. No mobile apps. No offline support.
- *Classter / SchoolMint / Blackbaud (international):* Enterprise-grade but built for Western markets. No MTN MoMo, no UNEB grading, no SchoolPay, no 3-term calendar. Priced in USD, inaccessible for Uganda private school budgets.
- *Excel + paper:* The default "system" for the majority of Uganda schools. This is the primary competitor by volume — not a software product but a workflow. Academia Pro must be meaningfully faster and less error-prone than Excel for every daily task to displace it.

**Key differentiators that no current competitor can match simultaneously:**

- UNEB grading engine with 100% computational accuracy across PLE, UCE, and UACE
- SchoolPay-native integration (schools migrate without changing payment infrastructure)
- Offline PWA for teacher attendance and mark entry in low-connectivity schools
- Global student identity (NIN/LIN cross-school lookup, EMIS-ready)
- MoES EMIS export without re-entering data
- KUPAA micro-payment model with community payment agents
- 12-platform mobile app suite (Android + iOS, 6 roles each)
- PDPO-compliant health records (Phase 7) as a boarding school differentiator
- USSD short code for feature-phone parents (Phase 11)

### Pan-Africa Expansion Opportunity

**Kenya:** 34,000+ registered schools. NEMIS (National Education Management Information System) is mandatory for all public schools. The KCSE grading engine for A-Level equivalent is well-documented. M-Pesa Daraja API is the dominant payment rail. Kenya is the highest-readiness expansion market after Uganda — NEMIS integration and M-Pesa support unlock the government school segment.

**Tanzania:** NECTA (National Examinations Council of Tanzania) governs CSEE (O-Level equivalent) and ACSEE (A-Level equivalent) examinations. Airtel Money Tanzania and Tigo Pesa dominate mobile money. Private school market is growing with urbanisation.

**Nigeria:** The largest education market in Africa by raw enrolment (50+ million primary pupils). WAEC governs West African Senior School Certificate (WASSCE) grading. Flutterwave and Paystack provide mature payment rails. The complexity of 36 state-level curricula requires a data-driven country profile model — which Academia Pro's architecture supports.

**Ghana:** Shares WAEC with Nigeria. Smaller market but higher income levels and stronger institutional willingness to pay for technology.

Pan-Africa expansion is enabled by the country profile architecture: `country_id`, `currency_code`, `payment_gateways[]`, `tax_rate`, and `curriculum_type` are configuration records. No new core code is required to add a country — only a new country profile, curriculum configuration, and payment gateway integration.

### Market Entry Strategy

Phase 1 targets the SchoolPay-integrated private school segment in Kampala and major urban centres (Jinja, Mbarara, Gulu, Mbale). These schools have the following profile:

- 200–1,500 students
- At least 1 semi-technical staff member (bursar or IT teacher)
- Already using SchoolPay for fee collection
- Pain points include: manual reconciliation, per-student report card typing, EMIS deadline panic

Phase 9 live trials target 10–20 paying schools for validation before the 500-school growth campaign begins. The trial pricing model and onboarding support process are to be defined in `_context/pricing.md` (currently a gap).

The 500-school target within 24 months of Phase 1 launch translates to approximately 21 new schools per month in Year 2, assuming a slow ramp in Year 1. SchoolPay's existing merchant relationships and the Uganda Private Schools and Educational Institutions Association (UPSIA) are potential channel partners.

### Regulatory Environment

- **Uganda Data Protection and Privacy Act 2019 (PDPO):** Student data is sensitive personal data. Lawful basis for processing is contractual necessity (enrolled students) and parental consent (students under 18). Full compliance is a gating requirement, not a Phase 11 item.
- **Bank of Uganda (BoU) Payment Systems Regulations:** Direct mobile money collection requires a Payment Systems Operator licence. Phase 1 and 2 operate under SchoolPay's licence. BoU pre-application engagement is scheduled for Phase 3 planning.
- **MoES EMIS Requirements:** Schools are legally required to submit EMIS data annually. Academia Pro's EMIS export makes compliance automatic, removing a pain point that currently requires 3–5 days of manual data assembly per school.
- **UNEB Examination Regulations:** Candidate registration data must be submitted in UNEB-specified format. The UNEB grading engine must match published grade boundary rules exactly — any deviation is a compliance defect, not a product limitation.
- **URSB Software Registration:** Academia Pro is registered under the Uganda Copyright Act 2006. All developers engaged on the platform sign IP assignment agreements.
