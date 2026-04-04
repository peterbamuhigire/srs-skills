# Feature: Farm and Plot Management

## Description
Core farm registration and spatial management for agricultural operations. Supports plot subdivision across 25+ land-use types (cropland, pasture, greenhouse, poultry house, fish pond, apiary, woodlot, nursery, etc.), GPS boundary mapping stored as GeoJSON polygons, soil profile data, irrigation infrastructure records, and seasonal awareness for planning cycles.

## Standard Capabilities
- Farm registration with Uganda administrative hierarchy (district, sub-county, parish, village)
- Plot subdivision with typed land-use classification (25+ types)
- GPS boundary mapping with GeoJSON polygon capture and storage
- Soil data recording (type, pH, organic matter, nutrient profiles)
- Irrigation infrastructure mapping (drip, sprinkler, furrow, rainfed)
- Land tenure type tracking (customary, freehold, leasehold, mailo)
- Season-aware plot calendar (Season A, Season B, dry season)
- Plot area calculation from GPS coordinates (hectares/acres)
- Photo attachment per plot with geotagged metadata
- Multi-farm support per farmer account
- EUDR compliance polygon export for supply chain due diligence

## Regulatory Hooks
- Uganda Data Protection and Privacy Act 2019: GPS location data requires explicit farmer consent before collection and processing
- EU Deforestation-Free Regulation (EUDR 2023/1115): polygon export in GeoJSON format for geolocation-based due diligence statements
- Uganda Land Act 1998: land tenure classification must align with statutory tenure categories

## Linked NFRs
- AG-001 (Data Integrity and Audit Trail)
- AG-002 (Geospatial Data Accuracy)
- AG-009 (Data Privacy and Consent)
