# Government: Default Non-Functional Requirements

These requirements are auto-injected into new government project scaffolds.
All blocks are tagged `[DOMAIN-DEFAULT: government]` for consultant review.

---

<!-- [DOMAIN-DEFAULT: government] Source: domains/government/references/nfr-defaults.md -->
#### GOV-NFR-001: FISMA Compliance — NIST SP 800-53 Controls Baseline
The system shall implement the applicable NIST SP 800-53 security control
baseline (Low, Moderate, or High) as determined by the FIPS 199 system
categorization. All controls must be documented in the System Security Plan
(SSP) and assessed by an independent assessor prior to system Authority to
Operate (ATO) issuance, in compliance with FISMA (44 U.S.C. §3554).

**Verifiability:** Prior to production deployment, an independent assessor
(3PAO or agency IA team) shall evaluate all required controls against the
applicable baseline. The assessment report must show a "Satisfied" finding
for all required controls with no open POA&M items rated Critical or High
without an accepted risk. ATO issuance by the Authorizing Official constitutes
formal acceptance of the compliance evidence.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: government] Source: domains/government/references/nfr-defaults.md -->
#### GOV-NFR-002: Accessibility — Section 508 / WCAG 2.1 AA
The system shall conform to Section 508 of the Rehabilitation Act
(29 U.S.C. §794d) and WCAG 2.1 Level AA for all citizen-facing and
staff-facing interfaces. No citizen shall be denied access to a government
service due to a disability-related accessibility barrier.

**Verifiability:** Execute automated accessibility scanning (e.g., Axe, WAVE)
against all public-facing pages; the scan must report zero WCAG 2.1 AA
violations. Conduct manual testing with assistive technologies (JAWS, NVDA,
VoiceOver) covering the primary citizen service workflows (application
submission, status inquiry, document upload). All tested workflows must be
completable without a mouse. Provide a completed VPAT (Voluntary Product
Accessibility Template) prior to procurement acceptance.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: government] Source: domains/government/references/nfr-defaults.md -->
#### GOV-NFR-003: Data Sovereignty — Citizen Data Must Not Leave National Jurisdiction
The system shall store, process, and replicate all citizen personally
identifiable information (PII) and government records exclusively on
infrastructure physically located within the national jurisdiction. No
citizen data shall be transmitted to, processed in, or stored within a
foreign jurisdiction without explicit legal authority and senior official
approval.

**Verifiability:** Inspect all data storage and processing configurations
(cloud region settings, database replication targets, backup destinations,
CDN edge node configurations) to confirm all data resides within the
approved national jurisdiction. Deploy a network monitoring agent and
verify that no outbound data transfers to foreign IP address ranges occur
during a 72-hour observation window. Review cloud service provider contracts
for data residency commitments and audit rights.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: government] Source: domains/government/references/nfr-defaults.md -->
#### GOV-NFR-004: Identity Assurance Level — NIST SP 800-63 IAL2 Minimum
The system shall require identity proofing at Identity Assurance Level 2
(IAL2) or higher, as defined in NIST SP 800-63A, for any citizen accessing
services involving personal records, benefits determination, or financial
transactions. Self-asserted identity (IAL1) is not sufficient for these
service categories.

**Verifiability:** Attempt to access a benefit determination or financial
transaction service using an account that has completed only IAL1 self-assertion
(no identity proofing evidence presented). The system shall deny access and
redirect to the identity proofing workflow. Verify that the identity proofing
process collects and validates at least one piece of SUPERIOR or STRONG
identity evidence as defined in NIST SP 800-63A Table 2.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: government] Source: domains/government/references/nfr-defaults.md -->
#### GOV-NFR-005: Audit Trail Retention
The system shall retain all audit logs recording access to and modification
of citizen records, case files, and financial transactions for a minimum of
3 years from the date of the logged event, and a minimum of 7 years for
audit records related to financial disbursements or contracts, in compliance
with OMB Circular A-130 and the National Archives General Records Schedule.
Audit logs shall be stored in a write-once, tamper-evident log management
system separate from the primary application infrastructure.

**Verifiability:** Attempt to delete or modify an audit log entry from the
log management system; the system shall reject the modification and return
an appropriate error. Query the log management system for audit records
from 3 years prior; all records must be retrievable and intact. Verify via
system configuration that the log management platform is isolated from
application administrator access.
<!-- [END DOMAIN-DEFAULT] -->

---
