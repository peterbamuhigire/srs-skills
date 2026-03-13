# Logistics: Security Baseline

## GPS Data Integrity

- GPS telemetry feeds must be authenticated; unauthenticated telemetry must be rejected
- Telemetry data must be transmitted over TLS 1.2+ to prevent interception or injection
- GPS spoofing detection: cross-reference GPS coordinates with cell tower triangulation and ELD data; anomalies exceeding 2km must trigger an alert
- Historical GPS tracks must be stored as immutable records; no retroactive modification permitted

## Chain of Custody Audit Trail

Every custody transfer event must produce an immutable log entry:

```json
{
  "event_id": "uuid",
  "timestamp": "ISO-8601",
  "shipment_id": "string",
  "event_type": "PICKUP | TRANSFER | DELIVERY | EXCEPTION",
  "actor_id": "string",
  "actor_role": "DRIVER | WAREHOUSE_STAFF | CUSTOMS_BROKER",
  "location": "string",
  "proof_of_delivery": "signature_id | photo_id | null",
  "outcome": "ACCEPTED | REFUSED | EXCEPTION"
}
```

- Audit logs must be write-once and retained for 7 years (U.S. customs record-keeping requirement)
- Chain of custody records must be producible on demand for customs and insurance inquiries

## Tamper-Evident Sealing Records

- Container and trailer seal numbers must be recorded at departure and verified at arrival
- Seal number discrepancies must immediately trigger an exception and notify the compliance officer
- Seal inspection records must include: seal number, condition (intact/broken), inspector ID, timestamp, location

## Driver Identity Verification

- Drivers must authenticate to the ELD and dispatch system using a unique, non-shared credential
- Biometric or PIN-based authentication required for ELD log-in to prevent log falsification
- Driver qualification records (CDL, medical certificate, MVR) must be verified before dispatch assignment
- Driver disqualification (expired CDL, HOS violation) must automatically block dispatch assignment

## Cargo Theft Prevention Monitoring

- High-value shipments must require two-person confirmation at pickup and delivery
- Geofencing alerts must notify dispatch when a vehicle deviates from the planned route by more than 5km
- Unplanned stops exceeding 30 minutes in non-approved locations must trigger a driver welfare and cargo security check
- Cargo insurance documentation must be linked to the shipment record

## Encryption Standards

| Data State | Standard | Minimum Key Length |
|---|---|---|
| At Rest (shipment records, driver data) | AES-256-GCM | 256-bit |
| In Transit (telematics, dispatch) | TLS 1.2+ | — |
| Backups | AES-256 | 256-bit |

## Authentication Requirements

- Dispatch and admin accounts: MFA mandatory
- Driver mobile app: PIN + biometric (device-level authentication)
- Session timeout: 15 minutes for dispatch consoles; driver app sessions tied to shift status
- Account lockout: 5 failed attempts → 15-minute lockout with supervisor alert
