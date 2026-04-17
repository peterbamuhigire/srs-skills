# Domain Profile: Agriculture

> No standard agriculture domain exists in `domains/INDEX.md` yet. This domain will be created as part of the Kulima project. The following profile captures the agriculture-specific requirements context.

## Domain Overview

Agriculture farm management systems operate in environments characterised by:
- **Offline-first requirement:** Rural farms frequently have no internet connectivity
- **Mixed enterprise management:** Most African farms combine crops and livestock on the same land
- **Seasonal cyclicality:** Two growing seasons in Uganda (March-June, August-November)
- **Mobile-money-first economy:** MTN MoMo and Airtel Money are the primary payment methods
- **Low-spec device constraints:** Target users operate Android phones with 2GB RAM and 32GB storage
- **Multi-lingual user base:** Users span multiple languages within a single country
- **GPS/GIS dependency:** Farm boundary mapping, animal tracking, and satellite imagery are core features
- **IoT integration:** Livestock sensors, soil sensors, weather stations, and camera systems feed real-time data
- **Supply chain traceability:** Export markets (EU, US) require verifiable farm-to-buyer traceability chains
- **Regulatory context:** Uganda Data Protection Act 2019, EUDR, MAAIF compliance, UCDA registration

## Key Standards and Regulations

| Standard / Regulation | Relevance |
|---|---|
| Uganda Data Protection and Privacy Act 2019 | Consent for GPS collection, data retention, third-party sharing |
| EU Deforestation Regulation (EUDR) 2023/1115 | GPS polygon, deforestation baseline, DDS generation for coffee/cocoa/timber exports |
| GlobalGAP | Good Agricultural Practices certification for export horticulture |
| RainForest Alliance / UTZ | Sustainability certification for coffee, tea, cocoa |
| UCDA Regulations | Uganda coffee sector registration and traceability |
| NAADS / OWC Programme Rules | Government agricultural input subsidy programme compliance |
| NSSF Act | Social security contributions for permanent farm workers |
| Employment Act 2006 | Labour law compliance for farm workers (minimum wage, working hours, leave) |
| ISO 22000 | Food safety management (relevant for processing and export) |
| Codex Alimentarius | International food standards (pesticide residue limits, quality grading) |

## Risk Level: Medium

Farm management data includes commercially sensitive information (GPS boundaries, financial records, production data) but is not as heavily regulated as healthcare (HIPAA) or finance (PCI-DSS). The primary compliance concerns are data privacy (DPA 2019), export traceability (EUDR), and labour law (Employment Act).

## Architecture Patterns

- **Offline-first with background sync:** All core operations must function without internet
- **Multi-tenant with franchise model:** Individual farmers as tenants, cooperatives as franchise tenants with member sub-accounts
- **Event-driven IoT ingestion:** Sensor data arrives asynchronously via webhooks and polling; must not block the main application
- **GIS-capable database:** MySQL JSON columns with spatial indexing for GeoJSON farm/plot boundaries
- **Stream proxy architecture:** Camera streams proxied (RTSP → HLS) rather than stored, minimising storage costs and privacy risks
- **Dual-mode financial records:** Simple bookkeeping for smallholders, double-entry accounting for commercial farms — same underlying data model
