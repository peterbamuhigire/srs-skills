# Domain: Logistics

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | DOT FMCSA, IATA, CBP (U.S. Customs and Border Protection), ISO |
| **Key Standards** | DOT FMCSA regulations, ISO 28000, IATA DGR, C-TPAT, Incoterms 2020 |
| **Risk Level** | Medium — supply chain security, hazardous materials compliance |
| **Audit Requirement** | DOT and customs compliance audits |
| **Data Classification** | Shipment Records, Driver Records, Dangerous Goods Manifests, Customs Declarations |

## Default Feature Modules

- Fleet Management
- Shipment Tracking
- Warehouse Management
- Route Optimization

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements
injected into new logistics projects at scaffold time.

Key injected areas:
- **NFR:** Real-time tracking frequency, ETA accuracy, system availability, data retention, dangerous goods validation
- **FR:** Hours-of-service enforcement, dangerous goods pre-booking checks, customs documentation generation
- **Interfaces:** GPS telematics APIs, carrier EDI (X12 204/214), customs broker APIs, ELD (Electronic Logging Device) integration

## References

- [regulations.md](references/regulations.md) — DOT FMCSA, ISO 28000, IATA DGR, C-TPAT, Incoterms 2020
- [architecture-patterns.md](references/architecture-patterns.md) — GPS tracking, event-driven status, ETA calculation, multi-carrier API, warehouse management
- [cltd-network-inventory-transportation.md](references/cltd-network-inventory-transportation.md) — logistics network design, inventory service levels, transportation, carrier/fleet strategy, customs documents, LSP models, and logistics KPIs
- [security-baseline.md](references/security-baseline.md) — GPS integrity, chain of custody, tamper-evidence, driver identity, cargo theft prevention
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection

## Feature Reference

- [fleet-management.md](features/fleet-management.md)
- [shipment-tracking.md](features/shipment-tracking.md)
- [warehouse-management.md](features/warehouse-management.md)
- [route-optimization.md](features/route-optimization.md)
