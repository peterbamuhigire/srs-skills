---
title: "Change Management Procedure — BIRDC ERP"
subtitle: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
status: "Active — Effective from Phase 7 Go-Live"
---

# Change Management Procedure — BIRDC ERP

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC
**Date:** 2026-04-05
**Version:** 1.0
**Status:** Active — Effective from Phase 7 Go-Live

---

## 1. Purpose and Scope

### 1.1 Purpose

This procedure governs all changes to the BIRDC ERP system following initial go-live (Phase 7 complete). It establishes a formal, auditable process that:

- Protects the integrity of financial data and audit trails (DC-003).
- Ensures every change is classified, approved, tested, and documented before deployment to production.
- Provides a written record satisfying Uganda Companies Act 7-year retention requirements and OAG Uganda audit readiness requirements.
- Protects both BIRDC/PIBID and Peter Bamuhigire (Consultant) by ensuring no undocumented changes are made to the production system.

### 1.2 Scope

This procedure applies to all changes to the BIRDC ERP after Phase 7 go-live, including:

- Software changes (PHP application code, SQL stored procedures, JavaScript)
- Database schema changes (table additions, column modifications, index changes)
- Configuration changes (PAYE/NSSF bands, PPDA thresholds, price lists, commission rates, EFRIS API settings)
- Integration changes (EFRIS API, MTN MoMo API, Airtel Money API, ZKTeco biometric integration)
- Security patches and vulnerability remediations
- New feature development and module additions
- Report template changes

This procedure does not apply to routine data entry operations performed by BIRDC staff using the ERP's normal user interface.

---

## 2. Change Classification

All changes are classified into 1 of 4 classes at the impact assessment stage (Section 3, Step 3). The class determines approval authority and maximum permissible turnaround time.

| Class | Description | Examples | Approval Authority | Max Turnaround |
|---|---|---|---|---|
| Emergency | System is down, data integrity is at risk, or a regulatory API breaking change prevents legally required transactions from completing | Security patch for active exploitation; EFRIS API version update that breaks invoice submission; critical bug causing incorrect financial calculations | Peter Bamuhigire alone | 4 hours to production deployment |
| High | A business-critical function is affected or a regulatory rate/threshold change requires a system update | PAYE band update following URA publication; NSSF rate change; PPDA procurement threshold adjustment; bug preventing payroll from running | Peter Bamuhigire + Finance Director (STK-002) | 3 business days |
| Standard | Non-critical enhancement, functional improvement, or bug affecting a non-critical workflow | Report format modification; new export market CoA template; UI workflow improvement; non-critical data fix | Peter Bamuhigire + relevant module owner | 2 weeks |
| Minor | Cosmetic change, documentation update, or low-risk configuration update | Field label text change; email notification template wording; colour or layout adjustment; help text update | Peter Bamuhigire alone | 1 week |

---

## 3. Change Request Process

All approved changes follow the steps below in sequence. No step may be skipped. Steps 3 and 4 may run in parallel where the module owner and Finance Director are different stakeholders.

1. The requestor submits a completed Change Request (CR) form to Peter Bamuhigire by email or via the CR form template in Section 9 (Appendix). Verbal requests are not accepted (see Section 4).

2. Peter Bamuhigire logs the CR in the change register (Section 6) and assigns a unique **CR-ID** in the format `CR-YYYYMMDD-NNN` (e.g., `CR-20260715-001`). The CR-ID is communicated to the requestor by return email within 1 business day.

3. Peter Bamuhigire performs an impact assessment covering:
   - Affected ERP modules and functional requirements
   - Affected database tables and schema changes required
   - Affected test cases that must be re-executed
   - Impact on EFRIS, MTN MoMo, or Airtel Money integrations
   - DPPA implications: does the change affect personal data or special personal data held in the system? If yes, document the lawful basis.
   - GL auto-posting logic: does the change alter any financial calculation or journal entry?

4. The impact assessment is shared with the relevant approval authority:
   - Finance Director (STK-002) for any change affecting the GL, financial statements, payroll, AR, AP, or budget modules.
   - Procurement Manager (STK-007) for PPDA threshold or procurement workflow changes.
   - Relevant department head for module-specific Standard changes.

5. The change is classified (Section 2) and the approval authority issues written approval or rejection. A written rejection must state the reason. Rejection closes the CR without further action; the requestor is notified.

6. If approved, the implementation sequence is:
   1. Develop the change on the development environment.
   2. Deploy to the staging environment and execute all relevant test cases.
   3. Conduct User Acceptance Testing (UAT) with the relevant module owner.
   4. Obtain written UAT sign-off from the module owner.
   5. Deploy to production during a scheduled maintenance window.
   6. Verify the change in production — confirm expected behaviour and confirm no regressions in related modules.

7. The change register is updated with: deployment date, ERP version number after the change (Section 7), and the name of the person who verified the production deployment.

8. All documentation affected by the change is updated to reflect the new behaviour. This includes, as applicable: the Software Requirements Specification, Low-Level Design, API Specification, Database Design Document, and User Manuals.

9. Relevant BIRDC staff are notified of the change. If the change alters a workflow that staff perform daily, Peter Bamuhigire delivers a brief retraining session (in person or by video call) before the production deployment.

---

## 4. No-Verbal-Change-Orders Rule

All change requests must be submitted in writing — by email or using the CR form in Section 9. Verbal instructions from any stakeholder, including the BIRDC Director (STK-001), shall not be acted upon without a written CR logged in the change register.

This rule:

- Protects BIRDC from undocumented changes that cannot be audited by OAG Uganda.
- Protects Peter Bamuhigire as consultant from scope creep and undocumented liability.
- Ensures every production change has a traceable approval chain.

If a stakeholder gives a verbal instruction, Peter Bamuhigire will respond: "Please submit a Change Request form and I will process it under the standard procedure." No exception exists to this rule, including under time pressure.

---

## 5. Emergency Change Protocol

When a change meets the Emergency classification (system down, data integrity at risk, or a regulatory API breaking change preventing legally required transactions), the standard approval sequence in Section 3 is compressed as follows:

1. Peter Bamuhigire may implement and deploy the change immediately to production without waiting for prior written approval.
2. Within 1 hour of production deployment, Peter Bamuhigire must:
   - Log the CR in the change register with class "Emergency" and a description of the issue and the fix applied.
   - Notify the Finance Director (STK-002) by both phone call and email, describing the issue and the action taken.
3. Within 24 hours of production deployment, Peter Bamuhigire must produce full impact documentation (affected modules, tables changed, test cases executed, verification results).
4. Within 3 business days of the emergency deployment, Peter Bamuhigire and the Finance Director conduct a post-change review to confirm:
   - The root cause is identified.
   - The fix is permanent (not a temporary workaround requiring a follow-up Standard change).
   - No financial data was affected; or, if affected, that the correct data has been restored.
5. The post-change review outcome is recorded in the change register.

---

## 6. Change Register Schema

The change register is a living document maintained by Peter Bamuhigire. It is made available to the Finance Director and IT Administrator (STK-003) on request. The register contains 1 row per CR with the following fields:

| Field | Description |
|---|---|
| CR-ID | Unique identifier in format `CR-YYYYMMDD-NNN` |
| Date Submitted | Date the CR form was received |
| Requestor | Name and role of the person requesting the change |
| Description | One-sentence summary of the change |
| Class | Emergency / High / Standard / Minor |
| Affected Modules | Comma-separated list of ERP module codes (e.g., F-005, F-006) |
| Approval Authority | Name and role of approving stakeholder |
| Approved / Rejected Date | Date of written approval or rejection |
| Deployed Date | Date the change was deployed to production (blank if not yet deployed) |
| ERP Version After Change | Semantic version number after deployment (Section 7) |
| Verified By | Name of person who confirmed correct production behaviour |

---

## 7. Version Numbering

The BIRDC ERP uses semantic versioning: **MAJOR.MINOR.PATCH**.

- **MAJOR** — incremented when a new phase deliverable is accepted by the client (e.g., Phase 2 go-live changes version from 1.x.x to 2.0.0).
- **MINOR** — incremented for each Standard or High change deployed to production (e.g., a PAYE band update changes version from 2.1.x to 2.2.0).
- **PATCH** — incremented for each Minor or Emergency change deployed to production (e.g., a label correction changes version from 2.2.0 to 2.2.1).

The current ERP version is recorded in the system administration panel and is displayed in the application footer. The version is updated at deployment time by Peter Bamuhigire.

---

## 8. Post-Go-Live Maintenance Commitment

Peter Bamuhigire commits to 12-month warranty support from the Phase 7 go-live date, covering the following at no additional charge:

- Bug fixes for defects present in the delivered system at go-live.
- PAYE and NSSF rate updates that require only data configuration changes (Finance Director updates via the UI per DC-002; Peter provides guidance if needed).
- EFRIS API version updates required by URA (code change by Peter at no additional charge within the warranty period).
- Security patches for vulnerabilities disclosed in the OWASP Top 10 and CVE feeds applicable to the ERP's technology stack.

The following are **not** included in the warranty and are billable under a separate engagement letter:

- New feature development.
- New module additions.
- Hardware procurement or server upgrades.
- Training sessions beyond those delivered at go-live.
- Data entry services.

All post-warranty work is governed by a new engagement letter agreed in writing before work begins.

---

## 9. Appendix — Change Request Form Template

The following template is used for all change requests. The requestor completes all fields and submits the completed form to Peter Bamuhigire by email.

---

**BIRDC ERP — Change Request Form**

| Field | Value |
|---|---|
| CR-ID | *(assigned by consultant on receipt)* |
| Date | |
| Requestor Name | |
| Requestor Role / Department | |
| Module(s) Affected | *(e.g., Payroll, Accounts Receivable, POS)* |
| Description of Change | *(what needs to change and why)* |
| Business Justification | *(what business problem does this change solve?)* |
| Urgency | *(Emergency / High / Standard / Minor — requestor's assessment)* |
| Is this a regulatory requirement? | Yes / No — if Yes, cite the regulation or URA/NSSF/PPDA publication reference |
| DPPA Implications | Does this change affect personal data or special personal data held in the system? Yes / No — if Yes, describe the data affected and the lawful basis for processing |
| Requestor Signature | |
| Date Signed | |

*Submit completed form to: Peter Bamuhigire — [techguypeter.com](https://techguypeter.com)*

---

*End of Change Management Procedure — BIRDC ERP v1.0*
