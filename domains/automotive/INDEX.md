# Domain: Automotive

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | Local motor vehicle authorities, PCI SSC, data protection authorities (GDPR / regional DPAs / Uganda DPPA), tax authorities (e-invoicing — EFRIS, ZATCA, KRA TIMS, SAT CFDI, GST) |
| **Key Standards** | PCI-DSS v4.0, OBD-II (SAE J1979 / ISO 15031), VIN (ISO 3779 / ISO 3780), GDPR, local consumer protection laws, right-to-repair provisions |
| **Risk Level** | Medium — cardholder data, consumer PII, vehicle ownership records, fleet operational data, workshop safety, parts provenance |
| **Audit Requirement** | PCI-DSS annual assessment when handling card data in scope; local tax e-invoicing certifications where mandated |
| **Data Classification** | Cardholder Data (CHD), Consumer PII, Vehicle Identification Data (VIN, plate, ownership), Service History, Technician Productivity Data, Parts Inventory Valuation |

## Default Feature Modules

- Workshop Operations (job cards, bay board, status workflow, QC)
- Vehicle Inspection (digital multi-point, photos, DTC, approvals)
- Parts & Inventory (multi-location stock, barcode, supplier, valuation)
- Customer Portal / Customer App (booking, live status, digital approval, payment, service history)
- Service Catalogue & Labour Pricing (labour rates, service templates, menu pricing)
- Estimates, Approvals & Invoicing (e-invoice, tax, warranty lines)
- Technician Productivity & Payroll (clock-on/clock-off per job, billable vs non-billable)
- Fleet & Corporate Accounts (bulk vehicle, statement billing, SLA)

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements injected into new automotive projects at scaffold time.

Key injected areas:

- **NFR:** Offline-first workshop operations, mobile capture performance (<=30 s round-trip for status / inspection photo), camera and barcode reliability on low-end Android, multi-tenant data isolation at the service layer, VIN and plate uniqueness, cardholder data scope minimization, e-invoicing compliance latency.
- **FR:** VIN decode and normalisation, odometer monotonicity, multi-point digital inspection with photo evidence, parts stock-on-hand reconciliation, warranty period tracking, customer digital approval capture (signature or in-app confirm), job-level labour cost roll-up, technician productivity metrics, corporate invoice accounts with purchase orders.
- **Interfaces:** OBD-II Bluetooth reader (ELM327-class), payment gateways (Stripe, mobile money rails, local card acquirers), SMS / WhatsApp gateway, e-invoicing authorities (EFRIS / ZATCA / KRA TIMS / SAT), parts supplier catalogues, insurance claim formats, vehicle registration / licence reminder data sources where available.

## References

- [regulations.md](references/regulations.md) — consumer protection, right-to-repair, PCI-DSS in automotive context, e-invoicing per jurisdiction, data protection for vehicle + owner data, waste and environmental rules (used oil, tyres, batteries).
- [architecture-patterns.md](references/architecture-patterns.md) — multi-branch tenant model, offline-first mobile sync, job card state machine, parts reservation vs issue, payment tokenization, OBD integration envelope, white-label Customer App, real-time vs batch GL posting.
- [security-baseline.md](references/security-baseline.md) — tenant isolation, role-scoped mobile navigation, photo evidence integrity, super-admin impersonation audit, PCI scope minimization via tokenization, barcode spoofing controls.
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection.

## Feature Reference

- [workshop-operations.md](features/workshop-operations.md)
- [vehicle-inspection.md](features/vehicle-inspection.md)
- [parts-inventory.md](features/parts-inventory.md)
- [customer-portal.md](features/customer-portal.md)
