# Automotive — Regulations & Compliance Baseline

Automotive service software sits at the intersection of consumer protection, payments, data protection, tax e-invoicing, and environmental compliance. The table below defines the baseline obligations an automotive SaaS platform MUST be able to satisfy as a configurable capability. Specific tenants enable the subset applicable to their jurisdiction.

## Consumer Protection and Right-to-Repair

| Concern | Control | Verifiability |
|---|---|---|
| Repair authorisation | Customer digital approval MUST be captured before billable labour or parts are consumed beyond the inspection scope. Approval record MUST retain actor, timestamp, approved line items, approved amount, and evidence (in-app confirm, signed image, or recorded consent). | Audit log query per job card returns a single authoritative approval artifact before any non-inspection status transition. |
| Price disclosure | Estimate MUST itemise labour, parts, taxes, and shop supplies before approval. Post-approval additions require a supplementary approval. | Invoice total MUST equal sum of approved estimate lines plus supplementary approvals; variance > 0 blocks invoice posting. |
| Parts disclosure | New, remanufactured, used, and aftermarket parts MUST be distinguishable on both estimate and invoice. | Parts line item record carries a `condition` enum {new, reman, used, oem, aftermarket}; UI and PDF renderers MUST display it. |
| Warranty statement | Parts and labour warranty period and conditions MUST be stated on the invoice. | Invoice template includes warranty block sourced from service catalogue entry. |
| Right-to-repair data portability | Customer MUST be able to export full service history in a machine-readable format (PDF + structured JSON). | Self-service export endpoint available from Customer App. |

## Payment Card Industry (PCI-DSS v4.0)

| Concern | Control |
|---|---|
| Card data scope | The platform MUST NOT store PAN, CVV, or track data. All card capture flows MUST use a tokenizing gateway (Stripe, Adyen, local acquirer iframes). |
| Tokenization | Only tokens and last-4 / brand / expiry masks may be persisted. Tokens stored at the tenant or customer scope (never global). |
| 3D Secure | For card-not-present flows (Customer App, web payment links) SCA / 3DS2 MUST be supported. |
| Scope documentation | Each tenant onboarding record MUST declare payment flow(s) in use so PCI scope can be documented per tenant. |

## Data Protection (General + Jurisdictional)

| Concern | Control |
|---|---|
| Vehicle as personal data | Where the jurisdiction treats VIN, plate, or service history as personal data (EU GDPR, Uganda DPPA 2019, California CCPA), the platform MUST support: consent capture, purpose limitation, retention periods, subject access, correction, erasure, and portability. |
| Technician biometrics | Fingerprint / face sign-in, where offered, MUST be device-local (Keychain + Secure Enclave / Android Keystore + StrongBox). Biometric templates MUST NEVER be transmitted to the server. |
| Breach notification | Jurisdiction-specific SLAs (GDPR 72 h, Uganda DPPA immediate to PDPO, CCPA without unreasonable delay) MUST be configurable. |
| DPIA trigger | Fleet tracking, telematics ingestion, and CCTV-linked bay monitoring — if added — require a DPIA per Uganda DPPA Regulation 12 and GDPR Art. 35. |

## Tax & Electronic Invoicing

The platform MUST treat e-invoicing as a pluggable compliance add-on, NOT a core assumption. Supported regimes at MVP:

- **Uganda:** EFRIS (URA) — optional add-on
- **Kenya:** KRA eTIMS — optional add-on
- **Rwanda:** RRA EBM — optional add-on
- **Saudi Arabia:** ZATCA Phase 2 — optional add-on
- **Mexico / LATAM:** CFDI — optional add-on
- **EU:** VAT-compliant invoice format — core

Each regime MUST be implemented behind a common `InvoiceAuthorityAdapter` interface with deterministic retries, idempotency keys, and an auditable submission ledger per invoice.

## Environmental & Waste

Used oil, tyres, batteries, coolant, brake fluid, and refrigerant are regulated waste streams in most jurisdictions. The platform MUST support:

- Tracking outbound waste volumes by category, with a destination (licensed disposer reference).
- Configurable environmental surcharge line items on invoices (where required by jurisdiction).
- Periodic waste reporting export.

## Right to Independent Repair (EU, US State Laws, Industry)

The platform MUST NOT lock customer service history or vehicle data behind a single-tenant wall that prevents the customer from taking that data to another garage. The Customer App export flow above discharges this obligation.

## Standards References

- PCI-DSS v4.0
- ISO 3779 (VIN content), ISO 3780 (WMI)
- SAE J1979 / ISO 15031 (OBD-II diagnostic trouble codes)
- GDPR, Uganda DPPA 2019, CCPA, LGPD, PDPA (SG, TH)
- Local e-invoicing: URA EFRIS, KRA eTIMS, RRA EBM, ZATCA, CFDI, Peppol
- IEEE 830, IEEE 1012, IEEE 1233, IEEE 610.12, ASTM E1340
