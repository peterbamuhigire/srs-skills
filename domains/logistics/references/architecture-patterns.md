# Logistics: Architecture Patterns

## Real-Time GPS Tracking

- GPS telemetry must be ingested via a dedicated telematics stream (MQTT or WebSocket preferred)
- Location updates must be persisted to a time-series data store optimized for geospatial queries
- Last known position must be queryable with sub-second latency for dispatcher dashboards
- GPS data must include: vehicle ID, driver ID, latitude, longitude, speed, heading, timestamp, odometer

```json
{
  "vehicle_id": "string",
  "driver_id": "string",
  "timestamp": "ISO-8601",
  "latitude": "decimal",
  "longitude": "decimal",
  "speed_kmh": "number",
  "heading_degrees": "number",
  "odometer_km": "number",
  "engine_status": "ON | OFF | IDLE"
}
```

## Event-Driven Shipment Status Updates

- Shipment lifecycle events must be published to an event stream as they occur:
  - `BOOKING_CONFIRMED`, `PICKED_UP`, `IN_TRANSIT`, `AT_HUB`, `OUT_FOR_DELIVERY`, `DELIVERED`, `EXCEPTION`
- Downstream consumers (customer portal, carrier API, WMS) subscribe to relevant events
- Events must be idempotent; duplicate events must not produce duplicate status changes
- Each event must carry: shipment_id, event_type, timestamp, location, actor_id, carrier_id

## ETA Calculation Algorithm

ETA is computed dynamically:

$$ETA = T_{current} + \frac{D_{remaining}}{V_{avg}} + \sum T_{stops}$$

Where:
- $D_{remaining}$ = remaining distance from current GPS position to delivery address
- $V_{avg}$ = rolling average speed over the last 30 minutes, adjusted for traffic data
- $T_{stops}$ = estimated dwell time at remaining planned stops

ETA must be recalculated every 5 minutes or on each GPS update, whichever is sooner.

## Multi-Carrier API Integration

- Carrier integrations must use an adapter pattern; each carrier is implemented as a swappable module
- Common operations: rate quote, booking, label generation, pickup scheduling, tracking query
- EDI X12 204 (motor carrier load tender) and 214 (shipment status) must be supported for truckload carriers
- Carrier API failures must trigger automatic fallback to secondary carrier or manual booking queue

## Warehouse Bin/Slot Management

- Each warehouse location must have a unique slot identifier (zone-aisle-bay-level-position)
- Putaway rules must direct items to optimal slots based on product dimensions, weight, and velocity class
- Slot occupancy must be updated atomically with the pick or putaway scan event
- Cross-docking: inbound receipts that match open outbound orders must bypass slot assignment

## Barcode and RFID Scanning

- All inbound and outbound goods movements must be confirmed by barcode or RFID scan
- Scan events must be timestamped and linked to the user, device, and location
- Scan discrepancies (quantity mismatch, wrong item) must trigger an exception workflow before movement confirmation
