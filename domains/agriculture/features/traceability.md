# Feature: Traceability

## Description
End-to-end supply chain traceability from farm to export, enabling batch tracking, chain of custody recording, certification management, and regulatory compliance for EU Deforestation-Free Regulation (EUDR). Supports QR code generation, GPS polygon export, deforestation-free verification against Global Forest Watch baselines, and buyer-facing transparency portals.

## Standard Capabilities
- Batch creation from harvest records with unique batch identifier
- Chain of custody tracking (farm, collection centre, processor, exporter)
- QR code generation per batch linking to traceability profile
- GPS polygon export in GeoJSON format for EUDR due diligence statements
- Farmer profile export for buyer and certification body review
- Input traceability per batch (pesticides, fertilisers applied with dates and rates)
- Certification tracking (Organic, Rainforest Alliance, UTZ, GlobalGAP, FairTrade)
- Deforestation-free verification using Global Forest Watch 31 December 2020 baseline
- EUDR Due Diligence Statement (DDS) generation with required data fields
- Buyer portal with read-only access to batch traceability data
- Batch splitting and merging with full audit trail
- Certificate of origin and phytosanitary certificate reference tracking

## Regulatory Hooks
- EUDR 2023/1115: mandatory geolocation, deforestation-free proof, and due diligence statement for regulated commodities (coffee, cocoa, palm oil, soy, cattle, rubber, wood)
- UCDA (Uganda Coffee Development Authority): coffee export quality and traceability compliance
- UEPB (Uganda Export Promotions Board): export documentation and quality standards
- GlobalGAP: Good Agricultural Practices certification audit trail requirements
- Rainforest Alliance: sustainable agriculture certification chain of custody

## Linked NFRs
- AG-002 (Geospatial Data Accuracy)
- AG-003 (Financial Data Accuracy and Reconciliation)
- AG-009 (Data Privacy and Consent)
