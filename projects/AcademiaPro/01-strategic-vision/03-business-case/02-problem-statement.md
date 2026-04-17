# Problem Statement — Current State of School Administration in Uganda

**Version:** 1.0
**Date:** 2026-03-28

---

## 1. Current State Analysis

### 1.1 Administrative Operations

The majority of Uganda's approximately 25,000 registered schools (primary and secondary combined, MoES estimate) administer students using one or more of the following manual processes:

- **Fee collection:** Paper receipt books (triplicate carbon copy). Bursars hand-write receipts for each payment. End-of-term reconciliation requires matching hundreds of stubs against a ledger book or an unstructured Excel sheet. Schools that use SchoolPay for mobile money collection still reconcile manually — SchoolPay posts transactions but does not manage fee structures, balances per student per term, or arrears carry-forward.
- **Attendance:** Handwritten class registers. Teachers record daily attendance in physical exercise books. Monthly attendance summaries are compiled by hand, consuming 3–5 hours of administrative time per class per term. No automated parent alert system exists.
- **Mark sheets and report cards:** Teachers enter marks on printed mark sheets. Head teachers aggregate results manually — a school with 500 students and 8 subjects generates 4,000 individual marks per examination sitting. Aggregation errors directly affect report card accuracy and, for examination classes, UNEB registration data. Report cards are typed individually (Word or handwritten) or printed from an Excel template that requires manual cell-by-cell entry.
- **UNEB grading:** The UNEB grading algorithm for PLE, UCE, and UACE is non-trivial (documented in BR-UNEB-001 through BR-UNEB-004). Schools compute division aggregates manually using a reference booklet. Computation errors result in wrong division assignments, incorrect university application grades, and school league table distortions. There is no automated validation against UNEB's published rules.
- **EMIS reporting:** MoES requires all registered schools to submit annual headcount and teacher data to the Education Management Information System (EMIS) portal. Schools re-enter data they already hold in paper registers or Excel into the MoES web form. The process takes 2–4 days per school per year and introduces transcription errors.

### 1.2 Quantified Administrative Burden

The estimates below are derived from the project vision document and structured domain research. They are presented as planning assumptions — not audited figures.

| Process | Estimated Time Lost Per Term | Error Vector |
|---|---|---|
| Fee reconciliation (manual) | 15–25 hours (bursar) for a 300-pupil school | Missed payments, unrecorded cash, double-entry |
| Attendance summary compilation | 3–5 hours per class teacher per term | Missed absence alerts to parents |
| Mark aggregation (500 students, 8 subjects) | 20–40 hours (head teacher + teachers) | Division miscalculation, wrong UNEB registration |
| Report card production (500 students) | 30–60 hours | Typographical errors, wrong student data |
| EMIS report submission | 2–4 days per school per year | Transcription errors, format rejections |
| **Total (500-pupil school, 3 terms)** | **~350–420 hours/year** | **Multiple uncontrolled error vectors** |

At the Uganda civil service teacher wage benchmark of approximately UGX 800,000/month, 350+ administrative hours per year per school represents a direct cost of UGX 3,000,000–4,200,000 in productive time diverted from teaching. Multiply across 10,000 schools and the national opportunity cost exceeds UGX 30 billion annually.

### 1.3 Parent and Student Experience Gaps

- Parents receive no real-time visibility into fee balances. They learn of arrears at the school gate when their child is turned away.
- Report cards are distributed physically at term-end. A parent who cannot attend collection day may wait weeks for results.
- Absence notifications rely on the child delivering a handwritten note, which is unreliable.

---

## 2. Existing Software: Evidence of Unmet Need

### 2.1 ShuleKeeper — Demonstrating the Market Gap

ShuleKeeper is an active Uganda-market school management product. Its documented limitations provide direct evidence that the market need is unmet by existing solutions:

- **60-day data deletion policy:** ShuleKeeper deletes school data 60 days after a subscription lapses. A school that stops paying due to cash-flow issues loses its entire historical student, fee, and attendance records — permanently. This is incompatible with Uganda's 7-year education record retention requirement (derived from MoES regulations) and exposes schools to PDPO 2019 liability for destroying records they are legally obligated to retain.
- **No mobile access:** ShuleKeeper has no native mobile application. Class teachers, who predominantly use smartphones, have no mobile-native attendance or mark entry path. Parent access is web-only, which excludes the majority of parents on Android-only devices without full web browsing habits.
- **Developer WhatsApp as primary support channel:** The primary support mechanism is a developer's personal WhatsApp number. This provides no SLA, no ticketing, no audit trail of support interactions, and no escalation path. For a system holding sensitive student and financial data, this is a critical operational risk.
- **No UNEB grading automation:** ShuleKeeper does not automate UNEB division computation. Mark entry is supported, but the grading engine is absent — the school still computes divisions manually.
- **No EMIS integration:** No export of EMIS-format data.

### 2.2 SchoolPay ERP — Market Position but Structural Immaturity

SchoolPay launched an ERP module in January 2024. SchoolPay's strength is its payment rails (BoU licensed, ~11,000 connected schools, MTN MoMo and Airtel Money processing). Its ERP is structurally immature: no UNEB grading, no EMIS export, no mobile apps, and limited school management depth. The January 2024 launch date means the product has fewer than 30 months of production iteration. Academia Pro's opportunity is to be the superior ERP that connects to SchoolPay — rather than competing with SchoolPay's payments business.

### 2.3 Foreign-Built Platforms

Platforms such as Fedena (India), Classter (Greece), and Alma (US) are designed for their domestic markets. None support UNEB grading rules, the Uganda 3-term calendar, MTN MoMo, SchoolPay reconciliation, MoES EMIS format, or pricing in UGX. Localisation retrofits at this level require architectural changes that foreign vendors have no business incentive to make for a market of Uganda's size.

---

## 3. Problem Summary

The core problem is the absence of a Uganda-native school management platform that simultaneously:

1. Automates UNEB-compliant grading with zero manual computation.
2. Integrates with existing payment infrastructure (SchoolPay, MTN MoMo, Airtel Money) rather than requiring schools to change payment habits.
3. Provides mobile-first access for teachers, parents, and students on budget Android devices.
4. Exports EMIS-format data for MoES statutory compliance.
5. Retains records for the legally required 7-year window.
6. Is priced and supported at a level accessible to Uganda's predominantly small and medium private schools.

The combination of these six requirements is unmet by any current product in the market.
