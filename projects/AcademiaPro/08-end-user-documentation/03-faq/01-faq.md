---
title: "AcademiaPro — Frequently Asked Questions"
subtitle: "Phase 1 FAQ Reference"
standard: "ISO 26514"
version: "1.0"
date: "2026-04-03"
---

# AcademiaPro — Frequently Asked Questions

## General

### 1. Is AcademiaPro free for my school?

No. AcademiaPro is a SaaS subscription. Pricing is tiered by enrolment count; the Tier-2 school tier starts at USD 3 per month for schools under 300 learners. See the pricing page at `https://chwezicore.com/academiapro/pricing`.

### 2. Which Uganda curricula does AcademiaPro support?

PLE (Primary Leaving Examination, P7), UCE (Uganda Certificate of Education, S4), UACE (Uganda Advanced Certificate of Education, S6), and the Thematic Curriculum (P1–P3). The grading engine auto-applies UNEB grading rules per the active curriculum.

### 3. Can the school administrator work offline?

Yes — the Android app (Phases 1–8) and iOS app (Phases 9–10) support offline enrolment capture, attendance capture, and grade entry. Data syncs on next network availability. Conflicts are resolved per the last-write-wins policy with full audit.

## Data and Privacy

### 4. Who owns the data the school puts into AcademiaPro?

The school owns the data. AcademiaPro is a processor under Uganda DPPA 2019. A signed Data Processing Agreement covers every tenant. Export of all school data as CSV or PDF is available at any time.

### 5. How is my learners' NIN and LIN protected?

Every S-tier PII field is encrypted at rest with AES-256-GCM. Access to the NIN/LIN lookup is rate-limited, MFA-gated, and audited. Implements `CTRL-UG-002` of the controls catalogue.

### 6. Where is the data stored?

Primary storage in AWS `eu-west-1` (Ireland). DR replicas in `us-east-1`. You can opt your tenant in or out of cross-region replication from the school settings page; default is opt-out (`eu-west-1` only) to keep data as close to East Africa as possible.

## Payments

### 7. Can parents pay via MTN Mobile Money and Airtel Money?

Yes. Both MTN MoMo and Airtel Money are first-class payment channels. Reconciliation is automatic. SchoolPay integration is also supported.

### 8. What happens if a parent pays twice by mistake?

The system detects duplicate payment attempts within 10 minutes of the same amount from the same MSISDN against the same fee line and prompts before confirming. Already-confirmed duplicates are flagged for refund; see `FR-FEE-005` and `BR-FEE-005`.

## Exams and Reporting

### 9. Does the system generate UNEB-compatible mark sheets?

Yes. The UNEB export wizard produces the exact CSV format required by UNEB for candidate registration. See the UNEB Export section of the user manual.

### 10. Does the system produce the annual MoES EMIS return?

Yes. The EMIS dashboard builds the annual enrolment and staff return for direct upload to the MoES EMIS portal. Field-by-field reconciliation is shown before submission.

### 11. How do report cards get to parents?

Three channels: in-app parent portal, SMS summary with PDF link, and printable PDF delivered via the school. Channel preference is per-parent, captured at enrolment.

## Support

### 12. How do I reach support?

Email `support@chwezicore.com` or use the in-app chat (weekdays 08:00–20:00 EAT). Sev-1 issues trigger the on-call rotation; see `runbook.md`.
