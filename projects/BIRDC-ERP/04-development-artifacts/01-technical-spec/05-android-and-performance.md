# 6. Android Mobile App Technical Stack

## 6.1 Technology Specifications

| Component | Specification | Rationale |
|---|---|---|
| Language | Kotlin (latest stable) | Null safety, coroutines, Jetpack Compose compatibility |
| UI framework | Jetpack Compose | Declarative UI, efficient recomposition, Material Design 3 |
| Local database | Room (SQLite abstraction) | Type-safe DAOs, offline-first storage, migrations |
| HTTP client | Retrofit 2 + OkHttp 4 | REST API calls, request/response interceptors, logging |
| Background sync | WorkManager | Persistent background jobs, constraint-aware (requires network), survives process death |
| Barcode scanning | ML Kit Barcode Scanning | On-device, no internet required, scans Code128, QR, EAN |
| Bluetooth printing | ESC/POS library over `BluetoothSocket` | 80mm thermal receipt printing for 6 Android apps |
| Biometric auth | `BiometricPrompt` API | Fingerprint / face unlock for Sales Agent and Executive Dashboard apps |
| Secure storage | `EncryptedSharedPreferences` | Refresh tokens encrypted with Android Keystore (hardware-backed where available) |
| Crash reporting | Firebase Crashlytics | Real-time crash reports; alert to IT Administrator |
| Push notifications | Firebase Cloud Messaging (FCM) | Executive Dashboard App and budget alert notifications |
| Dependency injection | Hilt (Dagger) | Compile-time DI, tested with standard Android DI patterns |
| Minimum API level | Android 8.0 (API 26) | Covers > 95% of Android devices in Uganda market |

## 6.2 App Architecture

All 6 Android apps follow MVVM architecture with a clean separation of concerns:

```
UI Layer (Compose Screens)
   │  observes
   ▼
ViewModel (StateFlow / SharedFlow)
   │  calls
   ▼
Repository (interface)
   │           │
   ▼           ▼
Remote        Local
DataSource    DataSource
(Retrofit)    (Room DAO)
```

**ViewModel rules:**

- `ViewModel` classes never reference Android context (use `ApplicationContext` via Hilt if needed).
- All UI state is exposed as `StateFlow<UiState>` where `UiState` is a sealed class covering `Loading`, `Success(data)`, and `Error(message)`.
- Long-running operations use `viewModelScope.launch` with structured coroutines.

**Repository rules:**

- The repository decides whether to serve data from local Room or from the remote API based on connectivity status and data freshness.
- For offline-first data (POS products, farmer names, agent stock): Room is the single source of truth. Remote data is synced into Room; the UI always reads from Room.
- For online-only data (financial reports on Executive Dashboard): the repository fetches from API and caches in Room with a timestamp; stale data (> 1 hour) triggers a refresh.

## 6.3 Offline Sync Strategy

WorkManager jobs handle all background synchronisation.

**Upload jobs (device → server):**

| Job | Data | Trigger |
|---|---|---|
| `SyncSalesJob` | New POS transactions created offline | Network available + periodic (every 15 minutes) |
| `SyncRemittanceJob` | Remittance submissions created offline | Network available |
| `SyncFarmerDeliveryJob` | Farmer delivery records created offline | Network available |
| `SyncProductionCompletionJob` | Production completion entries | Network available |
| `SyncQcResultsJob` | QC inspection results | Network available |

All jobs use `Constraints.Builder().setRequiredNetworkType(NetworkType.CONNECTED)` — they only run when connected.

**Conflict resolution:** Last-write-wins with server timestamp. The server's `updated_at` timestamp is authoritative. If a conflict is detected (the record was modified on both device and server since last sync), the conflict is logged to `tbl_sync_conflicts` for manual review by IT Administrator. The server version is used as the resolved value.

**Sync failure handling:** If a sync job fails after 3 attempts (`BackoffPolicy.EXPONENTIAL`), the job is retained in WorkManager's queue and a push notification is sent: "Sync pending — [N] records not yet uploaded. Check connectivity." Records are never deleted from Room until the server confirms receipt.

## 6.4 Bluetooth Scale Integration (Farmer Delivery App)

The Farmer Delivery App integrates with Bluetooth weighing scales at farmer collection points.

1. The scale is paired via the standard Bluetooth printer pairing flow (Section 5.3 of the UX Specification).
2. When a farmer delivery entry is open, a "Capture Weight" button is visible beside the weight input field.
3. Tapping "Capture Weight" opens a `BluetoothSocket` connection to the paired scale and reads the output stream.
4. Scale output is parsed from the device-specific ASCII format. Supported scale protocols: Toledo format and generic UART output (configurable in app settings — DC-002).
5. The captured weight populates the input field. The field is editable — the officer can manually correct the value if the scale output is garbled.
6. If no scale is paired, the weight field is a standard numeric input only.

---

# 7. Performance Requirements

All performance thresholds are sourced from `metrics.md` and apply to the production server under normal operating conditions (50 concurrent web users, or the stated peak scenario).

| Operation | Threshold | Test Condition |
|---|---|---|
| POS transaction: product search to receipt | ≤ 90 seconds (end-to-end, user time) | Prossy DC-001 test; single cashier; 100 products in catalogue |
| Product search (barcode or text) | ≤ 500 ms at P95 | Server-side API response time under 50 concurrent users |
| Standard report generation (up to 12 months) | ≤ 10 seconds | Sales report, P&L, AR aging — 12-month dataset |
| Trial Balance generation | ≤ 5 seconds | Full 1,307-account chart of accounts; any period |
| Farmer contribution breakdown (per batch) | ≤ 3 seconds | Batch of 100 farmers |
| Agent cash balance refresh | Real-time on every transaction post | No polling delay — balance updates on transaction completion |
| Offline POS — data loss on connectivity loss | 0 records lost | All POS transactions persisted to Room before API submission |
| Offline sync (Android apps, on reconnect) | ≤ 60 seconds | A full day of POS transactions for 1 agent (average 30 transactions) |
| Concurrent web users (peak) | 50 simultaneous users without degradation | Apache JMeter load test at 50 concurrent sessions |
| Audit trail query (any 30-day period) | ≤ 5 seconds | `tbl_audit_log` query filtered by user and date range |
| System uptime | ≥ 99% during business hours (06:00–22:00 EAT) | Monitored by uptime script; email alert on downtime |
| Database backup completion | ≤ 4 hours | Full `mysqldump` of the production database |

### Load Test Scenario for Phase 7 Acceptance

The Phase 7 load test simulates peak production day (140 MT/day processing):

- 50 concurrent web sessions: 10 Finance, 8 Sales, 5 Procurement, 5 Inventory, 5 HR, 5 Production/QC, 5 Admin, 7 miscellaneous.
- 200 simultaneous Sales Agent App sync requests (agents submitting end-of-day transactions).
- Concurrent EFRIS submissions for 50 invoices.
- 1 payroll run in background.

All performance thresholds in the table above must be met simultaneously during this load test. Any threshold failure is a Phase 7 go/no-go blocker.
