# Domain Profile: Education (Uganda-First / Pan-Africa)

> Auto-populated from domains/education/INDEX.md at scaffold time — 2026-03-27.
> Domain deduced from project description (school management, students, UNEB exams, Uganda 3-term calendar).
> **Uganda/Africa adaptation:** The US-centric standards below (FERPA, COPPA, Section 508) are noted for reference only. The primary regulatory framework for Academia Pro is Uganda law. Equivalent Uganda provisions are listed in the adaptation notes below each standard.

---

## Domain Profile (from domains/education/INDEX.md)

| Property | Value | Uganda Adaptation |
|---|---|---|
| **Regulatory Bodies** | U.S. Department of Education, FTC, State boards | Uganda MoES, UNEB, NIRA, PDPO Office, BoU (payments), UCC (USSD) |
| **Key Standards** | FERPA, COPPA, WCAG 2.1 AA, Section 508 | Uganda PDPO 2019, Uganda Copyright Act 2006, EMIS data standards |
| **Risk Level** | Medium — student PII, minor data protection | Medium-High — student PII includes NIN/LIN (biometric); health data (Phase 7) is special category |
| **Audit Requirement** | Required for FERPA compliance | Required for PDPO compliance; annual internal audit |
| **Data Classification** | Education Records (FERPA), PII, Child Online Data (COPPA) | Personal Data (PDPO), Special Category Data (health — Phase 7), EMIS Data (government) |

---

## Auto-Injected NFR Defaults (from domains/education/references/nfr-defaults.md)

The following requirements were injected at scaffold time. Review each block — keep, edit, or remove as applicable. Uganda-specific notes are appended to each.

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-001: Student Record Confidentiality
The system shall restrict access to education records to authorised users with a demonstrated legitimate educational interest. No education record shall be disclosed to a third party without documented student or parental consent or a recognised legal exception.

**Uganda adaptation:** The relevant law is the Uganda Personal Data Protection and Privacy Act 2019 (PDPO), not FERPA. The lawful basis for processing enrolled student data is contractual necessity. See `_context/gap-analysis.md` HIGH-008 for full compliance spec.

**Verifiability:** Authenticate as a user without a legitimate educational interest in a target student; attempt to retrieve the student's education record via the API. The system shall return HTTP 403 and log the denied access attempt. Verify the audit log entry contains user_id, tenant_id, timestamp, student_uid, and outcome=DENIED.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-002: Accessibility Compliance
The system shall conform to WCAG 2.1 Level AA for all student-facing and staff-facing interfaces. All interactive content shall be operable via keyboard alone, and all non-text content shall have a text alternative.

**Uganda adaptation:** Section 508 is a US federal requirement and does not apply directly. WCAG 2.1 AA is retained as the accessibility standard. Priority: mobile viewport accessibility for low-end Android devices (360 × 800 px, 2GB RAM) is equally important — see quality_standards.md.

**Verifiability:** Execute an automated Axe scan against all portal pages; zero WCAG 2.1 AA violations. Conduct a manual keyboard-navigation test on all interactive elements. Verify color contrast ≥ 4.5:1 for normal text.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-003: Parental Consent for Under-18
The system shall not disclose a student's personal data to any third party without the consent of the student's parent or guardian, where the student is under 18 years of age.

**Uganda adaptation:** COPPA (US, under-13) replaced with Uganda PDPO 2019 provisions for minors under 18. All students in Uganda school system are assumed minors unless individually verified otherwise. The system records the consenting parent/guardian at enrollment time.

**Verifiability:** Confirm that the student enrollment form requires linkage of at least one parent/guardian contact before completion. Attempt to export a student's record to a third party without recorded consent — the system shall reject the export and log the attempt.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-004: Student Record Retention
The system shall retain student education records and associated audit logs for a minimum of 7 years following the student's graduation, withdrawal, or transfer, and shall not permit permanent deletion of records within the mandatory retention window.

**Uganda adaptation:** Uganda education regulations specify minimum 7-year record retention (adapted from the default 5-year FERPA provision). This is a binding business rule — see business_rules.md BR-DP-002.

**Verifiability:** Attempt to permanently delete an education record for a student who graduated fewer than 7 years ago. The system shall reject the deletion, return an error message citing the retention policy, and log the attempt with the requesting user's identity.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-005: System Availability During Exam Periods
The system shall maintain 99.9% uptime ($\leq 0.73$ hours downtime/month) for all assessment and gradebook modules during designated examination periods, as defined in each school's academic calendar configuration.

**Uganda adaptation:** Examination periods in Uganda are Term 3 (October–November for national exams) and end-of-term exam weeks. The system determines examination period status from the school's configured academic calendar, not from hardcoded dates. Scheduled maintenance is prohibited during examination periods.

**Verifiability:** Monitor uptime for the Gradebook and Examinations modules during the examination window declared in the school's calendar. Calculate $Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$. Result must be $\geq 99.9\%$.
<!-- [END DOMAIN-DEFAULT] -->

---

## Uganda-Specific Domain Requirements (No US Equivalent)

#### UG-NFR-001: UNEB Grading Engine Accuracy
The system's automated grade computation for PLE, UCE (O-Level), and UACE (A-Level) shall produce results that are 100% identical to manual computation using UNEB's published grading rules for a test dataset of at least 100 sample candidate results provided by UNEB.

**Why:** Incorrect UNEB grades result in wrong university applications and wrong school league table positions. There is zero tolerance for computational error.

**Verifiability:** Execute the grading engine against UNEB sample mark sheet data (to be obtained from UNEB — see gap-analysis.md resource list). Compare output with manually computed expected results. Pass criterion: 0 discrepancies across all 100+ test candidates.

#### UG-NFR-002: EMIS Export Compliance
The system's EMIS export function shall produce student headcount and teacher data files that validate without error against the MoES EMIS data dictionary (version current at time of Phase 1 completion).

**Verifiability:** Generate EMIS export from a test tenant with 500 enrolled students and 30 staff. Upload to MoES EMIS staging portal (or validate against MoES-published XML schema). Zero validation errors.

#### UG-NFR-003: Uganda 3-Term Calendar Enforcement
The system shall not permit configuration of more or fewer than 3 terms per academic year for Uganda-locale tenants. Date ranges for each term must be non-overlapping and must collectively span at least 9 months of the academic year.

**Verifiability:** Attempt to configure 4 terms for a Uganda-locale tenant — the system shall reject the configuration with a descriptive validation error. Attempt to configure 2 overlapping term date ranges — the system shall reject the overlap.

#### UG-NFR-004: Offline Attendance and Mark Entry
The system's teacher-facing PWA and Android app shall support entry of daily attendance and exam marks while offline (no internet connection). Offline entries shall be queued and synced to the server within 5 minutes of the device regaining connectivity, with conflict resolution per the offline sync spec (see gap-analysis.md MEDIUM-011).

**Verifiability:** Disable network on a test device; enter 30 attendance records and 15 mark entries offline. Restore network. Verify all 45 records appear in the server database within 5 minutes with correct `tenant_id`, `student_uid`, and timestamps.
