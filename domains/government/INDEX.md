# Domain: Government

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | OMB, NIST, GSA, Local and national government bodies |
| **Key Standards** | FISMA (NIST SP 800-53), FedRAMP, Section 508, GDPR / local data sovereignty laws |
| **Risk Level** | High — citizen data, national security implications |
| **Audit Requirement** | Mandatory — FISMA annual assessment, Inspector General audits |
| **Data Classification** | Controlled Unclassified Information (CUI), Personally Identifiable Information (PII), Sensitive But Unclassified (SBU) |

## Default Feature Modules

- Citizen Portal
- Case Management
- Document Management
- Procurement & Contracts

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements
injected into new government projects at scaffold time.

Key injected areas:
- **NFR:** FISMA compliance, Section 508 accessibility, data sovereignty, identity assurance, audit trail retention
- **FR:** FOIA request handling, citizen identity proofing (NIST SP 800-63), PIV/CAC card authentication
- **Interfaces:** Login.gov / national identity provider integration, USASpending API, SAM.gov API, state e-filing systems

## References

- [regulations.md](references/regulations.md) — FISMA, NIST SP 800-53, FedRAMP, Section 508, Privacy Act, FOIA, data sovereignty
- [architecture-patterns.md](references/architecture-patterns.md) — zero-trust, data sovereignty, citizen identity proofing, MFA, air-gapped systems
- [security-baseline.md](references/security-baseline.md) — FIPS 140-2, PIV/CAC, continuous monitoring, supply chain risk, insider threat
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection

## Feature Reference

- [citizen-portal.md](features/citizen-portal.md)
- [case-management.md](features/case-management.md)
- [document-management.md](features/document-management.md)
- [procurement-contracts.md](features/procurement-contracts.md)
