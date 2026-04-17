# Product Requirements Document — Academia Pro

## Executive Summary

Academia Pro is a multi-tenant Software as a Service (SaaS) school management platform built for Uganda and architected for pan-African expansion. It automates every repeatable school administration process — fee collection and reconciliation, attendance tracking, examination grading, report card generation, and statutory government reporting — while remaining operable by a single administrator after completing module-specific training videos.

### The Problem

Schools across Uganda spend hundreds of hours per term on manual administration. Fee collection relies on paper receipts reconciled against daily SMS notifications from mobile money providers. Attendance registers are handwritten, rarely aggregated, and never reach parents in real time. Mark sheets are computed in Excel by class teachers, re-checked by hand by the head teacher, and typed individually into Word report card templates. Uganda National Examinations Board (UNEB) grade computation — PLE aggregates, O-Level divisions, A-Level points — is performed manually, introducing calculation errors that affect student progression. Ministry of Education and Sports (MoES) EMIS reports are assembled from teacher-supplied spreadsheets days before statutory deadlines.

No existing product addresses the full depth of this problem for the Uganda context. Foreign-built systems lack MTN Mobile Money (MoMo), Airtel Money, UNEB grading rules, the 3-term Uganda academic calendar, and SchoolPay integration. Locally available tools are either too shallow in capability or require a dedicated IT team to operate.

### The Solution

Academia Pro delivers an enterprise-grade school management platform that is:

- *Uganda-first by design* — 3-term calendar, UNEB grading engine for PLE/UCE/UACE, Uganda Shillings (UGX), SchoolPay integration, MoES EMIS export, and Africa's Talking SMS with Uganda sender IDs are first-class features, not afterthoughts.
- *Automation-first* — fee reminders fire automatically, attendance alerts send without manual trigger, term-end report cards queue for bulk generation, and EMIS exports are assembled from data already in the system.
- *Single-admin survivable* — role-scoped UX ensures complexity is hidden behind role boundaries; any user who has watched the training video for their assigned module can operate it without IT support.
- *Pan-Africa by architecture* — country profiles (curriculum type, currency, payment gateways, tax rate) are data-driven configuration records, not hardcoded logic. Kenya, Tanzania, and Nigeria expansion requires no code changes to the core platform.

### Scale of Opportunity

SchoolPay, Uganda's dominant school payments processor, serves approximately 11,000 schools. Academia Pro enters this market as the superior ERP layer that already speaks SchoolPay's language — schools migrate without changing their payment infrastructure or parent behaviour. The commercial target is 500 Uganda schools within 24 months of Phase 1 launch, expanding to at least 3 additional African countries within 36 months.

### Build Approach

The platform is delivered across 12 phases, beginning with 7 standard web modules in Phase 1 and adding optional modules, Android and iOS applications, government integrations, and pan-Africa payment rails through Phase 11. Phase 12 is ongoing maintenance and support. Each phase is gated by a formal requirements review and 100% automated test pass before the next phase begins, following the confirmed Hybrid (Water-Scrum-Fall) methodology.

### Commercial Model

Academia Pro operates on a subscription model billed per school per term or per year. The KUPAA micro-payment model — no minimum payment floor, community payment agents, partial payment carry-forward — removes the last barrier to adoption for cost-sensitive schools in rural and semi-urban Uganda.

### Ownership and Compliance

Academia Pro is developed and operated by Chwezi Core Systems (chwezicore.com), Kampala. The software is registered with the Uganda Registration Services Bureau (URSB) under the Uganda Copyright Act 2006. All processing of student personal data complies with the Uganda Data Protection and Privacy Act 2019 (PDPO). Payment processing in Phases 1 and 2 operates under SchoolPay's Bank of Uganda licence; direct mobile money processing in Phase 3 and beyond requires a separate BoU Payment Systems Operator licence, currently in pre-application planning.
