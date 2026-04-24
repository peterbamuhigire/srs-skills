---
domain: automotive
---

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
- Service Catalogue & Labour Pricing
- Estimates, Approvals & Invoicing
- Technician Productivity & Payroll
- Fleet & Corporate Accounts

## References

Full domain knowledge base lives under `domains/automotive/` at the repository root:

- `domains/automotive/INDEX.md`
- `domains/automotive/references/regulations.md`
- `domains/automotive/references/architecture-patterns.md`
- `domains/automotive/references/security-baseline.md`
- `domains/automotive/references/nfr-defaults.md`
- `domains/automotive/features/workshop-operations.md`
- `domains/automotive/features/vehicle-inspection.md`
- `domains/automotive/features/parts-inventory.md`
- `domains/automotive/features/customer-portal.md`
