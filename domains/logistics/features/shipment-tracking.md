# Feature: Shipment Tracking

## Description
End-to-end visibility of shipment lifecycle — from booking through delivery —
with real-time GPS tracking, event-driven status updates, ETA calculation,
and proof-of-delivery capture.

## Standard Capabilities
- Shipment booking and waybill/BOL generation
- Barcode and QR label generation (GS1-128, ZPL, PDF)
- Real-time GPS position tracking with < 5-minute update frequency
- Shipment status event recording (pickup, in-transit, hub scan, out for delivery, delivered, exception)
- Automated customer notifications (email/SMS) on key status events
- ETA calculation with dynamic recalculation based on GPS and traffic data
- Proof of delivery capture (signature, photo, geofenced auto-confirm)
- Exception management workflow (damage, delay, address issue, refused delivery)
- Multi-carrier tracking aggregation (carrier-agnostic tracking interface)
- Shipment history and audit trail export for customs and insurance

## Regulatory Hooks
- CBP (19 CFR Part 163): shipment records including origin, destination, commodity, and value must be retained 7 years
- IATA DGR: DG shipments must have the dangerous goods declaration linked to the waybill
- DOT FMCSA: driver logs linked to shipment must be retained per HOS retention rules
- C-TPAT: chain of custody documentation required for C-TPAT certified importers

## Linked NFRs
- LOG-NFR-001 (Real-Time Tracking — ≤ 5-minute GPS update frequency)
- LOG-NFR-002 (ETA Accuracy — ≤ 15 minutes for last-mile)
- LOG-NFR-003 (System Availability — tracking must be available 99.9%)
- LOG-NFR-004 (Data Retention — 7 years for shipment records)
