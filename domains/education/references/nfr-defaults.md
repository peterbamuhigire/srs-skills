# Education: Default Non-Functional Requirements

These requirements are auto-injected into new education project scaffolds.
All blocks are tagged `[DOMAIN-DEFAULT: education]` for consultant review.

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-001: Student Record Confidentiality
The system shall restrict access to education records to authorized users with
a demonstrated legitimate educational interest, in compliance with FERPA
(20 U.S.C. §1232g) and 34 CFR Part 99. No education record shall be disclosed
to a third party without documented student or parental consent or a recognized
FERPA exception.

**Verifiability:** Authenticate as a user without a legitimate educational interest
in a target student; attempt to retrieve the student's education record. The system
shall return an authorization error and log the denied access attempt. Verify that
the audit log entry is created with user_id, timestamp, student_id, and outcome=DENIED.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-002: Accessibility Compliance
The system shall conform to WCAG 2.1 Level AA and Section 508 standards for all
student-facing and staff-facing interfaces. All interactive content shall be
operable via keyboard alone, and all non-text content shall have a text alternative.

**Verifiability:** Execute an automated accessibility scan (e.g., Axe, WAVE) against
all public-facing pages; the scan must report zero WCAG 2.1 AA violations. Conduct
a manual keyboard-navigation test; all interactive elements must be reachable and
operable without a pointing device. Verify color contrast ratios meet the minimum
4.5:1 ratio for normal text.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-003: Parental Consent for Under-13
The system shall not collect, use, or disclose personal information from any user
identified as under 13 years of age until verifiable parental consent (VPC) has
been obtained and recorded, in compliance with COPPA (15 U.S.C. §6501) and
16 CFR Part 312.

**Verifiability:** Create a test account with a date of birth indicating an age
below 13. Attempt to proceed through account setup without completing the parental
consent workflow. The system shall block access to all data-collection features
and redirect to the VPC workflow. Verify that no personal information is persisted
prior to consent confirmation.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-004: Data Retention for Student Records
The system shall retain student education records and associated audit logs for
a minimum of 5 years following the student's graduation, withdrawal, or transfer,
and shall not permit permanent deletion of records within the mandatory retention
window.

**Verifiability:** Attempt to permanently delete an education record for a student
who graduated fewer than 5 years ago. The system shall reject the deletion, return
an appropriate error message citing the retention policy, and log the attempted
deletion with the requesting user's identity.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: education] Source: domains/education/references/nfr-defaults.md -->
#### EDU-NFR-005: System Availability During Exam Periods
The system shall maintain 99.9% uptime availability ($\leq 8.76$ hours downtime
per year) for all assessment and gradebook modules during designated examination
periods, as defined in the institutional academic calendar.

**Verifiability:** Monitor uptime for the gradebook and assessment modules during
the examination period as declared in the institutional calendar. Calculate availability
as $Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$. The result must be
$\geq 99.9\%$ for the designated examination window. Scheduled maintenance must
not be permitted during examination periods without explicit academic calendar exception.
<!-- [END DOMAIN-DEFAULT] -->

---
