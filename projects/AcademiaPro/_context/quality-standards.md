# Quality Standards — Academia Pro

This document enumerates every regulatory, statutory, and industry standard that Academia Pro must comply with. Every standard cited here is audited by `phase09.obligations` and must be referenced by at least one control in `_registry/controls.yaml`.

## Regulatory Frameworks in Scope

- **Uganda Data Protection and Privacy Act, 2019 (DPPA)** — all schools collect student PII including NIN/LIN, parent contact details, and academic records; financial records (fee ledgers) qualify as special personal data per §9.
- **Uganda Data Protection and Privacy Regulations, 2021** — Regulation 12 (DPIA triggers), Regulation 20 (cross-border transfer controls for AI processing).
- **Uganda Education Act, 2008** and **Education (Pre-Primary, Primary and Post-Primary) Act, 2008** — licensing, curriculum conformance, safeguarding obligations.
- **UNEB Regulations (PLE, UCE, UACE, Thematic)** — candidate registration, mark sheet format, grading conformance.
- **MoES EMIS Reporting Requirements** — annual enrolment return, staff return, performance return.
- **ISO/IEC 27001:2022** — information security management system; all controls in Annex A are candidate controls.
- **IEEE Std 830-1998** — SRS content and structure.
- **IEEE Std 1012-2016** — verification and validation framework.
- **BS ISO/IEC/IEEE 29119-3:2013** — test documentation.
- **PCI DSS v4.0** — applies to any card-present / card-not-present mobile money reconciliation (MTN MoMo, Airtel Money) and card gateway integrations (Flutterwave, Pesapal).
- **WCAG 2.1 Level AA** — accessibility obligation for any schools serving learners with special educational needs.

## Measurable Targets (SMART Obligations)

- **DPPA §7 Lawful Basis** — 100% of PII collection points have a linked consent FR (FR-PRIV-001 through FR-PRIV-008). Measured at every new FR review.
- **DPPA §19 Security of PII** — 0 plaintext special personal data fields in the database; all S-tier fields encrypted with AES-256-GCM. Measured by static analysis of `03-design-documentation/04-database-design/01-erd.md`.
- **DPPA §23 Breach Notification** — PDPO notified within 1 business day of confirmed S-tier leak; SLA 100% over rolling 12 months.
- **DPPA §30 Data Subject Rights** — DSAR closed within 30 calendar days; SLA ≥ 95% over rolling 12 months.
- **Regulation 12 DPIA** — DPIA completed and signed off before any at-scale AI feature go-live that processes student academic or financial data.
- **UNEB Conformance** — 100% of PLE/UCE/UACE/Thematic grade records reconcile to UNEB-published sample mark sheets on a per-release basis.
- **MoES EMIS Export Accuracy** — 100% of required EMIS fields populated for every exported academic year; 0 rejected returns.
- **ISO 27001 A.9 Access Control** — RBAC matrix in `02-requirements-engineering/03-stakeholder-analysis/01-rbac-matrix.md` is re-reviewed quarterly; 100% of production permissions map to a documented role.
- **PCI DSS 3.2** — no cardholder PAN stored by Academia Pro; tokenised vault only. Verified by database schema audit.
- **WCAG 2.1 AA** — all web surfaces pass axe-core with 0 critical violations on merge to `main`.

## Traceability

Each obligation above maps to at least one control in `_registry/controls.yaml` and at least one NFR or CTRL identifier in `_registry/identifiers.yaml`. The `phase09.obligations` gate refuses to pass until every framework listed here has at least one mapped control.
