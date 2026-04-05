# BIRDC ERP — Design Document

**Date:** 2026-04-05
**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com)
**Client:** PIBID / BIRDC, Bushenyi, Western Uganda
**Project:** BIRDC ERP — Purpose-built single-tenant enterprise resource planning system

---

## Project Overview

A purpose-built, single-tenant, on-premise ERP for the Banana Industrial Research and
Development Centre (BIRDC) and its parent body, the Presidential Initiative on Banana
Industrial Development (PIBID). BIRDC operates Uganda's only industrial-scale matooke
processing facility at Nyaruzinga hill, Bushenyi, producing the Tooke brand.

The system must serve three simultaneous roles: government initiative (parliamentary
accountability), commercial enterprise (IFRS reporting, export markets), and R&D centre
(agronomy and food science).

---

## Key Decisions

| Decision | Choice | Reason |
|---|---|---|
| Deployment | Single-tenant, on-premise | Data sovereignty (government initiative), no recurring SaaS cost, offline capability |
| Stack | PHP 8.3+ / MySQL 9.1 / Bootstrap 5 / Tabler | Most available developer skill in Uganda for long-term maintainability |
| Methodology | Hybrid: formal documentation gates + fixed-price deliverable milestones | Government consultancy contract; Parliament and management require formal sign-offs |
| Team | Peter Bamuhigire (architect) + 1–3 hired developers | Micro team; Peter leads architecture and quality |
| Mobile | Android only; iOS deferred | Reduce scope and cost; Android dominant in Uganda SMB market |
| Domain | Agriculture + Manufacturing + Uganda Government Compliance | Banana value chain, food processing, PPDA/EFRIS/ICPAU |

---

## Seven Delivery Phases

### Phase 1 — Commerce Foundation
**Modules:** Sales & Distribution, Point of Sale (POS), Inventory & Warehouse Management,
Agent Distribution Management
**Android apps:** Sales Agent App, Warehouse App
**Key complexity:** Dual-track inventory (warehouse ≠ agent stock), FIFO remittance allocation,
agent cash accountability, EFRIS fiscal receipt submission

### Phase 2 — Financial Core
**Modules:** Financial Accounting & General Ledger, Accounts Receivable (agent remittance
system), Accounts Payable (farmer payment system), Budget Management (parliamentary +
commercial dual-mode)
**Android apps:** Executive Dashboard App
**Key complexity:** Dual-mode accounting (PIBID parliamentary votes + BIRDC IFRS commercial),
cryptographic hash chain integrity on GL ledger, 7-year audit trail retention

### Phase 3 — Supply Chain & Farmers
**Modules:** Procurement & Purchasing (standard PPDA + 5-stage cooperative farmer workflow),
Farmer & Cooperative Management
**Android apps:** Farmer Delivery App
**Key complexity:** 5-stage cooperative procurement, 6,440+ farmer individual contribution
tracking, GPS farm profiling, bulk MTN MoMo / Airtel Money farmer payment

### Phase 4 — Production & Quality
**Modules:** Manufacturing & Production (circular economy BOM), Quality Control & Laboratory
**Android apps:** Factory Floor App
**Key complexity:** Circular economy recipes (peels → biogas, waste water → bio-slurry),
mass balance verification, QC gate blocking inventory release, Certificate of Analysis for export

### Phase 5 — People
**Modules:** Human Resources, Payroll (PAYE / NSSF / LST / mobile money salary)
**Android apps:** HR Self-Service App
**Key complexity:** Government pay scales (PIBID) + commercial pay scales (BIRDC), biometric
ZKTeco integration, payroll immutability after approval, bulk mobile money casual worker payment

### Phase 6 — Research, Administration & Compliance
**Modules:** Research & Development, Administration & PPDA Compliance, System Administration / IT
**Android apps:** None
**Key complexity:** PPDA procurement document management, banana variety R&D tracking,
government replication configuration framework

### Phase 7 — Integration, Hardening & Go-Live
**Scope:** EFRIS full wiring across all modules, performance load testing, full security audit
(OWASP), acceptance testing sign-off, production deployment, staff training delivery
**Key complexity:** System-to-system EFRIS API (URA), end-to-end regression across all 17 modules

---

## Document Suite (~32 documents)

### Phase 01 — Strategic Vision
- PRD_BIRDC_ERP.docx
- VisionStatement_BIRDC_ERP.docx
- BusinessCase_BIRDC_ERP.docx

### Phase 02 — Requirements Engineering
- SRS_BIRDC_ERP_Phase1_Commerce.docx (Sales, POS, Inventory, Agent Distribution)
- SRS_BIRDC_ERP_Phase2_Finance.docx (GL, AR, AP, Budget)
- SRS_BIRDC_ERP_Phase3_SupplyChain.docx (Procurement, Farmers)
- SRS_BIRDC_ERP_Phase4_Production.docx (Manufacturing, QC)
- SRS_BIRDC_ERP_Phase5_People.docx (HR, Payroll)
- SRS_BIRDC_ERP_Phase6_ResearchAdmin.docx (Research, Admin, IT)
- UserStories_BIRDC_ERP.docx
- StakeholderAnalysis_BIRDC_ERP.docx

### Phase 03 — Design Documentation
- HLD_BIRDC_ERP.docx
- LLD_BIRDC_ERP.docx
- APISpec_BIRDC_ERP.docx
- DatabaseDesign_BIRDC_ERP.docx
- UXSpec_BIRDC_ERP.docx

### Phase 04 — Development Artifacts
- TechnicalSpec_BIRDC_ERP.docx
- CodingGuidelines_BIRDC_ERP.docx

### Phase 05 — Testing Documentation
- TestStrategy_BIRDC_ERP.docx
- TestPlan_BIRDC_ERP.docx

### Phase 06 — Deployment & Operations
- DeploymentGuide_BIRDC_ERP.docx
- Runbook_BIRDC_ERP.docx

### Phase 07 — Delivery Artifacts
- MilestoneDeliveryPlan_BIRDC_ERP.docx
- DefinitionOfDone_BIRDC_ERP.docx
- DefinitionOfReady_BIRDC_ERP.docx

### Phase 08 — End-User Documentation
- UserManual_BIRDC_ERP.docx
- InstallationGuide_BIRDC_ERP.docx
- FAQ_BIRDC_ERP.docx

### Phase 09 — Governance & Compliance
- TraceabilityMatrix_BIRDC_ERP.docx
- AuditReport_BIRDC_ERP.docx
- ComplianceDocument_BIRDC_ERP.docx
- RiskAssessment_BIRDC_ERP.docx

---

## Core Design Principles (Design Covenant)

- **DC-001:** Zero mandatory training for routine operations — every daily-use screen is self-discoverable with built-in helptext.
- **DC-002:** Configuration over code — all business rules (PAYE bands, NSSF rates, recipe ingredients, commission rates, PPDA thresholds) configurable via UI by Finance Director or IT Administrator.
- **DC-003:** Audit readiness by design — every financial transaction creates an immutable, hash-chained audit trail automatically. 7-year retention.
- **DC-004:** Dual-mode accounting — PIBID parliamentary budget votes and BIRDC commercial IFRS accounts in one system, always simultaneously reportable.
- **DC-005:** Offline-first where it matters — POS, Farmer Delivery App, and Warehouse App function fully offline.
- **DC-006:** Data sovereignty — all data on BIRDC's own servers in Bushenyi, Uganda.
- **DC-007:** Replicable by design — all BIRDC-specific configuration isolated in tables, not code; redeployable for Uganda Coffee Development Board or similar government agro-processors.

---

## Critical Business Rules

- **BR-001:** Dual-track inventory — warehouse stock and agent field stock are permanently separate ledgers. Reports never cross-contaminate.
- **BR-002:** FIFO remittance allocation — agent remittances allocated to oldest outstanding invoices first via stored procedure `sp_apply_remittance_to_invoices`.
- **BR-003:** Segregation of duties — transaction creator ≠ approver for all financial transactions, enforced at API layer.
- **BR-004:** QC gate — production output cannot enter saleable inventory until QC issues an approved Certificate of Analysis.
- **BR-005:** PPDA approval matrix — PO approval levels match Uganda PPDA Act procurement category thresholds (micro / small / large / restricted).
- **BR-006:** Agent stock float limit — stock transfer to agent blocked if it would exceed the agent's float limit.
- **BR-007:** FEFO enforcement — First Expiry First Out for all products with expiry dates; no manual batch selection at POS.
- **BR-008:** Circular economy mass balance — 100% of input matooke must be accounted for across primary products + by-products + scrap. Mass balance variance ≠ 0 triggers a production alert.
- **BR-009:** Sequential numbering — invoice, receipt, and journal entry numbers are sequential and gap-free; gaps trigger immediate alerts.
- **BR-010:** Payroll immutability — approved payroll is locked; corrections processed as adjustment runs in the next period.
- **BR-011:** Farmer individual tracking — every cooperative batch receipt broken down to individual farmer contributions with separate GL entries and payment records.
- **BR-012:** Three-way matching — PO → GRN → Vendor Invoice; price and quantity discrepancies flagged before payment authorisation.
- **BR-013:** GL hash chain — the general ledger implements a cryptographic hash chain; any tampering with a historical entry is mathematically detectable.
- **BR-014:** Budget alert — system alerts when departmental spending approaches the parliamentary vote threshold.
- **BR-015:** Commission on verified sales only — agent commission calculated on remittance-verified sales, not on cash collection.
