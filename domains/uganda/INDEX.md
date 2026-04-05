# Domain: Uganda Government & Public Sector

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | URA (Uganda Revenue Authority), PDPO (Personal Data Protection Office / NITA-U), PPDA (Public Procurement and Disposal of Public Assets Authority), OAG (Office of the Auditor General), NSSF Uganda, NIRA (National Identification and Registration Authority), ICPAU, UNBS |
| **Key Standards** | DPPA 2019 + Regulations 2021, PPDA Act (Cap 305), Uganda Income Tax Act (Cap 340), NSSF Act, Uganda Companies Act, IFRS for SMEs (ICPAU), ISO 22000 (food-sector entities), Codex Alimentarius (export), IEEE 830-1998 |
| **Risk Level** | High — citizen PII, parliamentary accountability, OAG audit exposure |
| **Audit Requirement** | Mandatory — OAG annual audit, 7-year record retention (Income Tax Act), PDPO registration and compliance |
| **Data Classification** | Personal data (NIN, name, contact), Special personal data (financial info, health, religious/political beliefs, sexual life, medical records), Sensitive government data (parliamentary budget votes, procurement records) |

## Uganda-Specific Rules

### DPPA 2019 — Critical Differences from GDPR

| Provision | Uganda Rule | GDPR Equivalent |
|---|---|---|
| Financial information | **Special personal data** — requires heightened protection | Not special category |
| Breach notification | **Immediately** notify PDPO (no 72-hour window) | Within 72 hours |
| Breach — notify data subject | PDPO decides and directs (not controller's choice) | Controller decides |
| Right to portability | Not established | Article 20 right |
| Deceased persons | Data still protected | Not covered |
| Data collector | Distinct legal role (separate from controller/processor) | Not defined |
| Penalties — individuals | Up to 245 currency points (UGX 4.9M ≈ USD 1,300) | N/A |
| Penalties — corporations | Up to 2% annual gross turnover | Up to 4% global turnover |
| Imprisonment | Up to 10 years (Part VII offences) | No criminal sanctions |
| Children's consent | Parent/guardian OR statutory need OR research | Parent/guardian or 16+ |
| PDPO registration | Mandatory for all data controllers | Not required |
| Data subject response | 30 days (data controller must comply or reject in writing) | 1 month |
| Extraterritorial scope | Applies to any entity processing Ugandan citizens' data | EU residents |

### Special Personal Data (Section 9, DPPA 2019)

Processing of the following requires explicit lawful basis or express consent:
- Religious or philosophical beliefs
- Political opinions
- Sexual life
- **Financial information** ← Uganda-unique; applies to mobile money numbers, salary data, bank accounts, payment histories
- Health status
- Medical records

### Lawful Processing Bases (Section 7, DPPA 2019)

- Prior consent of data subject
- Authorised or required by law
- Proper performance of a public duty by a public body
- National security
- Prevention/detection/prosecution of an offence
- Performance of a contract
- Medical purposes
- Compliance with a legal obligation

### Mandatory DPIA Triggers (Regulation 12)

A DPIA is required when processing poses a high risk, including:
- Large-scale processing of special personal data
- Systematic monitoring of individuals
- Any processing using new technologies that may affect rights and freedoms

### PDPO Registration (Regulation 15-16)

Every data controller and data processor must register with the PDPO (Form 2, Schedule 1 of Regulations). Unregistered processing is an offence.

## Default Feature Modules

- PDPO Registration Management
- Consent Capture and Management
- Data Subject Rights Portal (access, rectification, erasure — 30-day response)
- Data Breach Notification Workflow (immediate → PDPO)
- DPIA Documentation Module
- DPO Designation and Contact Record
- Data Retention and Destruction Schedule

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT: uganda]` requirements
injected into new Uganda government/public sector projects at scaffold time.

Key injected areas:
- **NFR:** DPPA 2019 compliance, PPDA procurement documentation, 7-year audit trail retention (OAG), EFRIS real-time fiscal receipting
- **FR:** Consent capture at registration, data subject rights endpoint, breach notification workflow, DPO designation record, PDPO registration
- **Interfaces:** URA EFRIS API, MTN MoMo / Airtel Money, ZKTeco biometric, NIRA NIN validation, NSSF reporting, bank bulk credit transfer

## References

- [regulations.md](references/regulations.md) — Full Uganda regulatory framework: DPPA, PPDA, Income Tax Act, NSSF Act, OAG requirements
- [nfr-defaults.md](references/nfr-defaults.md) — Default NFRs for Uganda government projects
- [dppa-pii-classification.md](references/dppa-pii-classification.md) — PII classification matrix and encryption requirements

## Feature Reference

- `features/` — (populate as Uganda-specific feature modules are documented)

## Keyword Signals (for domain auto-detection)

`Uganda`, `BIRDC`, `PIBID`, `URA`, `EFRIS`, `PPDA`, `OAG`, `NSSF Uganda`, `NIRA`, `NIN`, `matooke`, `cooperative farmers`, `Kampala`, `Bushenyi`, `MTN MoMo`, `Airtel Money`, `parliamentary budget vote`, `ICPAU`, `DPPA`
