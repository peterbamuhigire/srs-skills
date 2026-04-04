# Domain: Agriculture

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | MAAIF (Uganda), EU Commission (EUDR), UCDA, NAADS/OWC, National Data Protection Authority |
| **Key Standards** | Uganda Data Protection Act 2019, EUDR 2023/1115, GlobalGAP, RainForest Alliance/UTZ, ISO 22000, Codex Alimentarius, Employment Act 2006, NSSF Act |
| **Risk Level** | Medium — commercially sensitive farm data (GPS boundaries, financials), export compliance (EUDR), labour law |
| **Audit Requirement** | Moderate — financial transaction audit trail, traceability chain of custody, EUDR DDS records |
| **Data Classification** | Commercially Sensitive (farm boundaries, financials), Personal (farmer identity, NIN, mobile money), Export Compliance (traceability, GeoJSON polygons, deforestation checks) |

## Default Feature Modules

- Farm and Plot Management
- Crop Management
- Livestock Management
- Financial Records
- Inventory and Input Management
- Task and Worker Management
- Weather and Advisory
- Supply Chain Traceability
- Marketplace and Market Linkage
- IoT Device Integration
- GPS Animal Tracking
- Live Camera Surveillance
- AI Farm Advisor
- Cooperative Management

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements
injected into new agriculture projects at scaffold time.

Key injected areas:
- **NFR:** Offline-first capability, GPS boundary data encryption, financial audit trail, multi-lingual support, low-bandwidth optimisation
- **FR:** Farm boundary mapping, crop lifecycle tracking, livestock individual ID, mobile money payment, EUDR DDS generation
- **Interfaces:** Mobile money APIs (MTN MoMo, Airtel Money), weather APIs (Open-Meteo), IoT device APIs (Jaguza), map SDKs (Google Maps), satellite imagery (Sentinel-2), AI (Claude API)

## References

- [regulations.md](references/regulations.md) — Uganda DPA, EUDR, GlobalGAP, employment law, export compliance
- [architecture-patterns.md](references/architecture-patterns.md) — Offline-first, GIS storage, IoT ingestion, stream proxy, dual-mode accounting
- [security-baseline.md](references/security-baseline.md) — Farm data encryption, mobile security, API security, device credential management
- [nfr-defaults.md](references/nfr-defaults.md) — Default non-functional requirements for injection

## Feature Reference

- [farm-plot-management.md](features/farm-plot-management.md)
- [crop-management.md](features/crop-management.md)
- [livestock-management.md](features/livestock-management.md)
- [financial-records.md](features/financial-records.md)
- [inventory-management.md](features/inventory-management.md)
- [task-worker-management.md](features/task-worker-management.md)
- [weather-advisory.md](features/weather-advisory.md)
- [traceability.md](features/traceability.md)
- [marketplace.md](features/marketplace.md)
- [iot-integration.md](features/iot-integration.md)
- [gps-tracking.md](features/gps-tracking.md)
- [camera-surveillance.md](features/camera-surveillance.md)
- [ai-advisor.md](features/ai-advisor.md)
- [cooperative-management.md](features/cooperative-management.md)
