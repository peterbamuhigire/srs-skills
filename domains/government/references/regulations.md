# Government: Regulations & Standards Reference

## FISMA (Federal Information Security Modernization Act)

| Requirement | Citation | Scope |
|---|---|---|
| Annual Security Assessment | 44 U.S.C. §3554 | Federal agencies must conduct annual reviews of information security programs |
| System Inventory | 44 U.S.C. §3554(a)(1) | Agencies must maintain inventory of all information systems |
| Continuous Monitoring | OMB M-14-03 | Ongoing assessment of security controls, not just annual snapshot |
| Incident Reporting | 44 U.S.C. §3554(b)(7) | Incidents must be reported to US-CERT within prescribed timelines |

- FISMA applies to all federal agencies and contractors operating federal information systems
- Agencies must implement security controls from NIST SP 800-53 at the applicable baseline (Low, Moderate, High)

## NIST SP 800-53 (Security and Privacy Controls)

| Control Family | Examples |
|---|---|
| Access Control (AC) | Least privilege, account management, remote access |
| Audit and Accountability (AU) | Audit log generation, retention, review, and protection |
| Configuration Management (CM) | Baseline configurations, change control, security settings |
| Identification and Authentication (IA) | Unique identifiers, authenticator management, MFA |
| Incident Response (IR) | Incident response plan, testing, reporting |
| System and Communications Protection (SC) | Network segmentation, encryption, transmission confidentiality |

- Federal systems must implement controls at the appropriate impact level per FIPS Publication 199
- High-impact systems require the full SP 800-53 control baseline

## FedRAMP (Federal Risk and Authorization Management Program)

- Cloud service providers (CSPs) serving federal agencies must obtain FedRAMP authorization
- FedRAMP authorizations: Agency ATO or Joint Authorization Board (JAB) Provisional ATO
- CSPs must undergo a 3PAO (Third-Party Assessment Organization) assessment
- Continuous monitoring reports required monthly; vulnerability scans required monthly
- FedRAMP Moderate baseline applies to most federal SaaS/IaaS deployments

## Section 508 (Rehabilitation Act, 29 U.S.C. §794d)

- Federal agencies must ensure ICT developed, procured, or used is accessible to people with disabilities
- Technical standards (36 CFR Part 1194) incorporate WCAG 2.0 Level AA by reference
- Applies to web content, software applications, electronic documents, kiosks, and multimedia
- Procurement: Section 508 conformance must be verified before contract award (Voluntary Product Accessibility Template, VPAT)

## Privacy Act of 1974 (5 U.S.C. §552a)

- Governs collection, maintenance, use, and dissemination of personal information in federal systems
- Requires a System of Records Notice (SORN) for each system that maintains records by personal identifier
- Individuals have rights to access, amend, and receive accounting of disclosures of their records
- Computer Matching Agreements required before sharing records between agencies for matching programs

## Freedom of Information Act (FOIA, 5 U.S.C. §552)

- Federal agencies must make records available to the public upon request, subject to nine exemptions
- Response deadline: 20 business days for routine requests; 10 days for expedited requests
- Systems must support FOIA request intake, tracking, and response workflow
- Exemptions: classified information, internal personnel rules, trade secrets, personal privacy, law enforcement records

## Data Sovereignty Laws

- U.S. federal systems: citizen data must reside on infrastructure within U.S. jurisdiction
- EU member state governments: GDPR and national data sovereignty laws may require data to remain within the country
- Cloud hosting arrangements must include contractual data residency guarantees and right-to-audit clauses
- Transfer of citizen data to foreign jurisdictions requires explicit legal basis and senior official approval
