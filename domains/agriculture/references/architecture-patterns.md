# Agriculture: Architecture Patterns

## Offline-First Architecture

Farm operations occur in areas with intermittent or no connectivity. The system must operate fully offline and sync when a connection becomes available.

### Queue-Based Sync

- All write operations are queued locally in a persistent operation log
- Each operation is timestamped with device clock and tagged with a sync status (PENDING, SYNCING, SYNCED, FAILED)
- Sync priority order: financial transactions > livestock health events > crop activities > photos/attachments > analytics data
- Retry with exponential backoff: 5s, 15s, 45s, 120s, then queue for next connectivity window

### Local Databases

- **Android:** Room with SQLCipher encryption for sensitive data (financial records, GPS boundaries)
- **iOS:** SwiftData with Core Data encryption for local persistence
- Database schema mirrors server-side schema to minimise transformation overhead

### Conflict Resolution

- **Default Strategy:** Last-write-wins based on device-local timestamp
- **Conflict Log:** When the same record is modified on two devices while offline, the losing version is stored in a `conflict_log` table with both versions, timestamps, and device IDs
- **Farmer Review:** Conflicts are surfaced to the farmer on next app open with a side-by-side comparison and manual merge option

### Attachment Compression

- Photos compressed client-side to ≤ 512 KB before queuing for upload
- Compression preserves sufficient quality for pest/disease identification
- Thumbnails (≤ 50 KB) synced first; full images synced on Wi-Fi or when bandwidth exceeds 512 kbps

## GIS Data Storage

### GeoJSON in MySQL JSON Columns

```sql
ALTER TABLE farm_plots ADD COLUMN boundary JSON NOT NULL;
ALTER TABLE farm_plots ADD COLUMN centroid POINT NOT NULL SRID 4326;
CREATE SPATIAL INDEX idx_centroid ON farm_plots(centroid);
```

- Farm boundaries stored as GeoJSON `Polygon` or `MultiPolygon` features in a MySQL `JSON` column
- Centroid extracted and stored in a `POINT` column with SRID 4326 (WGS 84) for spatial indexing
- Spatial queries use the indexed `POINT` column; boundary polygon used for precise area calculations and EUDR exports

### Farm Boundary Polygons

- Minimum 4 vertices for a valid polygon (3 unique points + closing point)
- Coordinate validation: latitude -90 to 90, longitude -180 to 180
- Self-intersection detection on client before submission

### Plot Subdivision

- A farm contains one or more plots; each plot has its own boundary polygon
- Plots must not overlap within a farm (validated server-side using `ST_Intersects`)
- Plot area calculated using `ST_Area` with geographic coordinate correction

## IoT Data Ingestion

### WebSocket Gateway

- Real-time sensor data (soil moisture, temperature, humidity, rainfall) ingested via WebSocket connections
- Gateway authenticates devices using per-device IoT tokens (JWT with device_id claim)
- Message format: JSON with `device_id`, `sensor_type`, `value`, `unit`, `timestamp`

### Polling and Webhook Patterns

- **Polling:** For devices behind cellular gateways that cannot maintain WebSocket connections; poll interval configurable per device (default 5 minutes)
- **Webhook:** Third-party weather station APIs push data to a tenant-scoped webhook endpoint

### Time-Series Storage

```sql
CREATE TABLE sensor_readings (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_id VARCHAR(36) NOT NULL,
    tenant_id INT NOT NULL,
    sensor_type ENUM('soil_moisture', 'temperature', 'humidity', 'rainfall', 'ph') NOT NULL,
    value DECIMAL(10,4) NOT NULL,
    unit VARCHAR(10) NOT NULL,
    recorded_at DATETIME(3) NOT NULL,
    INDEX idx_device_time (device_id, recorded_at),
    INDEX idx_tenant_sensor (tenant_id, sensor_type, recorded_at)
);
```

- Partition by month for efficient range queries and archival
- Aggregate to hourly and daily summaries for dashboard display

### Alert Threshold Engine

- Per-sensor-type configurable thresholds (e.g., soil moisture < 20% triggers irrigation alert)
- Alerts delivered via in-app notification and optional SMS
- Alert cooldown period to prevent notification flooding (default 1 hour)

### Device Management Lifecycle

- States: REGISTERED → ACTIVE → INACTIVE → DECOMMISSIONED
- Device tokens rotated every 90 days; stale tokens rejected
- Heartbeat monitoring: device marked INACTIVE after 3 missed heartbeat intervals

## Camera Stream Proxy

### RTSP-to-HLS Conversion

- Live camera feeds converted from RTSP to HLS using mediamtx or ffmpeg
- No video storage on server (privacy-first architecture); stream is ephemeral
- HLS segment duration: 2 seconds for near-real-time viewing

### Bandwidth-Adaptive Streaming

- Multiple HLS quality variants: 240p (150 kbps), 480p (500 kbps), 720p (1.5 Mbps)
- Client selects variant based on detected bandwidth
- Fallback to JPEG snapshot mode (1 frame/5 seconds) on connections below 128 kbps

### Camera Brand Integration

- Generic ONVIF protocol support for IP cameras
- Brand-specific adapters for common agricultural cameras (Reolink, Hikvision, Dahua)
- Camera credentials stored encrypted per-tenant; never exposed in API responses

## Dual-Mode Financial Records

### Shared Data Model

```
transactions
├── id (PK)
├── tenant_id (FK)
├── date
├── description
├── amount
├── type (INCOME | EXPENSE | TRANSFER)
├── category_id (FK)
├── payment_method (CASH | MOBILE_MONEY | BANK)
├── reference_number
└── created_by (FK)

journal_entries (generated from transactions)
├── id (PK)
├── transaction_id (FK)
├── account_id (FK → chart_of_accounts)
├── debit DECIMAL(15,2)
├── credit DECIMAL(15,2)
└── posted_at
```

### Simple Bookkeeping Mode

- Farmer sees: Money In, Money Out, Balance
- System auto-generates journal entries against a simplified 2-level chart of accounts
- Reports: Income Statement, Cash Flow summary

### Double-Entry Accounting Mode

- Full chart of accounts (assets, liabilities, equity, revenue, expenses)
- Manual journal entry capability for accountants
- Reports: Trial Balance, Balance Sheet, Income Statement, Cash Flow Statement
- Enterprise profitability tracking per crop, per plot, per season

## Multi-Tenant with Franchise Model

### Tenant Types

- **Individual Farmer:** Single tenant with one or more farms
- **Cooperative (Franchise Tenant):** Cooperative admin manages the cooperative account; member farmers are sub-accounts within the franchise
- **Buyer/Exporter:** Read-only access to traceability data for purchased commodities

### Aggregated Reporting

- Cooperative admins see aggregated production, financial, and compliance data across all member farms
- Individual farmer data is visible to cooperative admin only with farmer consent flag enabled
- Export-level traceability reports aggregate from plot → farm → cooperative → exporter

### Payment Distribution

- Cooperative receives bulk payment from buyer
- System calculates per-farmer share based on delivered quantity and quality grade
- Payment distribution records linked to source transaction for audit trail

## Multi-Lingual Architecture

### Translation Table Pattern

```sql
CREATE TABLE translations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    locale VARCHAR(5) NOT NULL,       -- e.g., 'en', 'lg', 'sw', 'fr'
    translation_key VARCHAR(255) NOT NULL,
    translation_value TEXT NOT NULL,
    UNIQUE KEY uk_locale_key (locale, translation_key)
);
```

### Per-User Language Selection

- Language preference stored per user; switchable without app restart
- Fallback chain: user locale → tenant default locale → English
- All user-facing text referenced by translation key, never hardcoded

### JSON-Based Local Name Maps

- Library data (crop varieties, livestock breeds, pest species, diseases) stored with a `local_names` JSON column
- Example: `{"en": "Fall Armyworm", "lg": "Ekiwuka ky'emmwaanyi", "sw": "Viwavi vya jeshi"}`
- Client displays name matching user's selected locale; falls back to English

## Mobile Money Integration

### Supported Providers

- **MTN Mobile Money (MoMo):** Collections API for receiving payments; Disbursements API for paying farmers
- **Airtel Money:** Similar collections and disbursements pattern

### Retry Queue

- Failed mobile money transactions queued for retry with exponential backoff
- Maximum 3 retries over 15 minutes; after that, transaction marked FAILED and farmer notified
- Idempotency key on every request to prevent duplicate charges

### Transaction Reference Tracking

- Each mobile money transaction assigned an internal reference and mapped to the provider's external reference
- Status polling: check transaction status every 30 seconds until SUCCESSFUL or FAILED (max 5 minutes)
- Callback/webhook endpoint for provider-initiated status updates
- Full transaction history stored with: amount, phone number (masked), provider reference, status, timestamps
