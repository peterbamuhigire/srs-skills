# Domain Profile: Retail (Primary) + Healthcare (Phase 2) + Hospitality (Phase 2/3)

> Auto-populated from domains/retail/INDEX.md at scaffold time.
> Maduuka is multi-domain: Retail is primary (core modules, general merchants).
> Healthcare domain applies to the Phase 2 Pharmacy module.
> Hospitality domain applies to Phase 2 Restaurant/Bar and Phase 3 Hotel modules.
> No hospitality domain exists in srs-skills yet -- hospitality requirements must be authored manually in Phase 2/3 SRS sessions.
> Review and remove sections not applicable to Uganda/Africa market context.

## Retail Domain Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | URA (Uganda Revenue Authority), Uganda Data Protection Office |
| **Key Standards** | Uganda Data Protection and Privacy Act 2019, EFRIS (URA mandate from July 2025), PCI-DSS v4.0 (card payments where applicable) |
| **Risk Level** | Medium -- payment data, consumer PII, multi-tenant isolation |
| **Audit Requirement** | EFRIS: real-time URA submission (Phase 3). Data protection: annual internal review |
| **Data Classification** | Transaction records, consumer PII, employee PII, financial records |

## Default Feature Modules (Retail)

- Product Catalogue and Inventory
- Point of Sale
- Customer Management
- Supplier Management

## Healthcare Domain Profile (Phase 2 -- Pharmacy Module)

| Property | Value |
|---|---|
| **Regulatory Bodies** | National Drug Authority (NDA) Uganda |
| **Key Standards** | NDA Uganda approved drug list, Pharmacy and Drugs Act Uganda, Narcotic Drugs and Psychotropic Substances Act |
| **Risk Level** | High -- prescription data, controlled substances, patient safety |
| **Audit Requirement** | NDA inspection compliance, controlled drugs register retention |
| **Data Classification** | Patient PHI, prescription records, controlled substance logs |

## Hospitality Domain Profile (Phase 2/3 -- Restaurant/Hotel)

| Property | Value |
|---|---|
| **Regulatory Bodies** | Uganda Tourism Board, local health authority |
| **Key Standards** | Uganda Tourism Act, local food safety regulations |
| **Risk Level** | Medium -- guest PII, financial records |
| **Data Classification** | Guest PII (including ID documents for hotel), reservation records, billing records |

## NFR Injection Notes

Retail domain NFR defaults are injected into 02-requirements-engineering/01-srs/06-nfr.md.
Healthcare NFR defaults will be injected into Phase 2 SRS sections.
Hospitality NFR defaults must be authored manually (no hospitality domain in srs-skills yet).
