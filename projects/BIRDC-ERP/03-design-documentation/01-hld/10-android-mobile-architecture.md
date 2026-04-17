# 10. Android Mobile Architecture

## 10.1 App Suite Overview

6 Android applications serve distinct user populations. iOS is deferred. All apps target Android 8.0 (API 26) as the minimum supported version.

| App | Primary Users | Count | Offline Capable |
|---|---|---|---|
| Sales Agent App | Field sales agents | 1,071 | Yes — full POS offline |
| Farmer Delivery App | Field collection officers | ~20 | Yes — farmer registration and delivery recording |
| Warehouse App | Warehouse staff | ~15 | Partial — barcode scan and count offline; sync on reconnect |
| Executive Dashboard App | Director, Finance Director | 2 | No — read-only; requires live data |
| HR Self-Service App | All staff | 150+ | Partial — leave requests queue offline |
| Factory Floor App | Production supervisors, QC staff | ~30 | Partial — order monitoring offline; completion entry sync on reconnect |

## 10.2 Technology Stack

| Component | Technology |
|---|---|
| Language | Kotlin |
| UI framework | Jetpack Compose |
| Local database | Room (SQLite) — one database per app |
| HTTP client | Retrofit 2 + OkHttp 4 |
| Background sync | WorkManager |
| Barcode scanning | ML Kit Barcode Scanning API |
| Bluetooth printing | ESC/POS library (Bluetooth 80mm thermal receipt printer) |
| Biometric authentication | Android BiometricPrompt API |
| Secure storage | EncryptedSharedPreferences (AES-256 for JWT refresh tokens) |

## 10.3 JWT Authentication Flow

1. User launches the app and enters credentials (email + password).
2. App calls `POST /api/auth/login` → receives `access_token` (15-minute TTL) and `refresh_token` (30-day TTL).
3. `refresh_token` is stored in `EncryptedSharedPreferences`.
4. `access_token` is held in memory (not persisted to disk).
5. Every API request attaches `Authorization: Bearer <access_token>`.
6. When a request receives `HTTP 401` (token expired), WorkManager's token refresh interceptor calls `POST /api/auth/refresh` with the `refresh_token` to obtain a new `access_token`.
7. If the refresh token is also expired, the user is redirected to the login screen.

## 10.4 Room Offline Database Design (per app)

Each app maintains its own Room database. There is no shared local database across apps.

**Sales Agent App Room schema (key entities):**
- `AgentInvoice` — invoice records for the agent's territory
- `AgentStockItem` — product catalogue and current agent stock balance (synced)
- `PendingSale` — offline POS sales not yet synced to server
- `PendingRemittance` — remittances submitted offline, awaiting server confirmation

**Farmer Delivery App Room schema (key entities):**
- `Farmer` — farmer profiles cached for offline lookup and new registrations queued
- `PendingDelivery` — individual farmer delivery records captured offline
- `CooperativeBatch` — batch receipt records

**Warehouse App Room schema (key entities):**
- `Product` — product catalogue for barcode lookup
- `PendingGRN` — goods receipt notes captured offline
- `PendingTransfer` — stock transfer confirmations queued

## 10.5 WorkManager Background Sync

WorkManager handles all background data synchronisation. Sync jobs are defined as `CoroutineWorker` implementations with exponential backoff on failure.

| Sync Job | Direction | Trigger | Frequency |
|---|---|---|---|
| `AgentSalesSyncWorker` | Outbound | Connectivity restored; also every 15 minutes on Wi-Fi | Pending sales → server |
| `AgentStockSyncWorker` | Inbound | App foreground; every 30 minutes | Server agent stock → Room |
| `FarmerDeliverySyncWorker` | Outbound | Connectivity restored | Pending deliveries → server |
| `FarmerCatalogueSyncWorker` | Inbound | App start + hourly | Server farmer list → Room |
| `WarehouseSyncWorker` | Bidirectional | Connectivity restored | GRN + transfers outbound; product catalogue inbound |
| `FactoryFloorSyncWorker` | Bidirectional | Connectivity restored | Production order updates bidirectional |

## 10.6 Conflict Resolution Strategy

The conflict resolution policy is **last-write-wins with server timestamp authority**:

1. Every synced record carries a `server_updated_at` timestamp from the server response.
2. When the app submits an offline record, the server compares the `device_created_at` timestamp against the current server state of the same record.
3. If the server record was modified after `device_created_at`, the server's version takes precedence and the conflict is logged in `tbl_sync_conflicts` for review by the IT Administrator.
4. For financial transactions (sales, remittances, deliveries), conflicts are never silently discarded. A conflict alert is sent to the IT Administrator and the relevant supervisor.

**Known limitation:** [CONTEXT-GAP: GAP-002] — the full conflict resolution behaviour for agent remittances submitted while offline simultaneously with a supervisor verification of a prior remittance has not been fully specified. This requires resolution before the Sales Agent App sync logic is finalised.

## 10.7 Bluetooth Thermal Receipt Printing

The Sales Agent App and Farmer Delivery App support Bluetooth-connected 80mm ESC/POS thermal receipt printers.

- Printer pairing is configured once in the app settings and remembered.
- Receipt content is generated on-device from local sale data — printing works offline.
- Receipt format: 80mm width; includes agent name, transaction ID, product, quantity, price, date, and BIRDC branding.
- For the Farmer Delivery App: farmer receipt includes batch ID, weight, quality grade, and net payable estimate.
