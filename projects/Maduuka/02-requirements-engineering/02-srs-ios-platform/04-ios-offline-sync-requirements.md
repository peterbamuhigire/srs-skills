---
title: "SRS — Maduuka iOS Platform"
subtitle: "Section 4: iOS Offline Sync Requirements"
version: "1.0"
date: "2026-04-05"
status: "Draft"
---

# Section 4: iOS Offline Sync Contract

This section specifies the complete offline-first data synchronisation contract for the iOS platform. These requirements extend **BR-009** (Offline Sale Queue), **NFR-AVAIL-002** (Offline-First Guarantee), and **NFR-AVAIL-003** (Offline Queue Persistence) from the Phase 1 SRS to the iOS Core Data implementation.

The Core Data stack is the single source of truth for all data displayed in the iOS app. The server API is the system of record. The sync engine reconciles the two.

---

## 4.1 Pending Queue Structure

**FR-iOS-SYNC-001:** When any create, update, or delete operation occurs on the iOS app while offline (or before the server has confirmed receipt of a prior operation), the system shall record the operation as an entry in a Core Data `PendingSyncQueue` entity with the following attributes:

- `id`: UUID (primary key, idempotency key)
- `sequenceNumber`: Int64 — monotonic, device-local, increments by 1 for each new entry
- `entityType`: String — e.g., `"sale"`, `"stock_adjustment"`, `"expense"`, `"customer"`
- `operation`: String — `"create"`, `"update"`, or `"delete"`
- `payload`: Binary (JSON-encoded entity snapshot at the time of the operation)
- `createdAt`: Date (timestamp of the offline operation)
- `status`: String — `"pending"`, `"uploading"`, `"conflict"`, `"synced"`, `"failed"`
- `retryCount`: Int16 — incremented on each failed upload attempt

The `PendingSyncQueue` entity shall be stored in a separate Core Data persistent store file with `NSFileProtectionCompleteUnlessOpen` to ensure it survives device restarts.

*Verifiability:* Complete 5 operations while in airplane mode. Inspect the Core Data `PendingSyncQueue` entity; 5 entries must exist with `status = "pending"` and monotonically increasing `sequenceNumber` values.

---

## 4.2 Upload on Connectivity Restoration

**FR-iOS-SYNC-002:** When internet connectivity is restored (detected via `NWPathMonitor` path status change to `.satisfied`), the system shall immediately begin uploading all `PendingSyncQueue` entries with `status = "pending"` or `status = "failed"` to the server. Entries shall be uploaded in ascending `sequenceNumber` order (chronological). Each entry shall be sent as a discrete POST request to the server's `/api/v1/sync/batch` endpoint (or equivalent batch endpoint). Each entry's `id` (UUID) shall be included as an `Idempotency-Key` HTTP request header to prevent duplicate server-side processing on retry.

*Verifiability:* Create 10 operations offline. Restore connectivity. Monitor network traffic; the 10 POST requests must be dispatched in `sequenceNumber` order. Resend one request a second time with the same `Idempotency-Key`; the server must return HTTP 200 (acknowledged) without creating a duplicate record.

---

## 4.3 Conflict Resolution

**FR-iOS-SYNC-003:** When the server returns HTTP 409 (Conflict) for a sync queue entry — indicating the server-side record has been modified by another session since the iOS device's last sync — the system shall:

1. Log the conflict as a `SyncConflict` entry in the local Core Data audit table, recording: `localPayload` (the iOS device's version), `serverPayload` (included in the 409 response body), `entityType`, `entityId`, `conflictTimestamp`, and `resolvedBy = "server"`.
2. Update the local Core Data record to match the server's authoritative version.
3. Mark the `PendingSyncQueue` entry as `status = "conflict"`.
4. Display a badge on the Dashboard indicating the count of unresolved conflicts, allowing the user to review discarded local changes.

The server version is authoritative in all conflict scenarios. The iOS app shall never overwrite the server version with a stale local version.

*Verifiability:* Edit a record on both iOS (offline) and the web interface (online). Restore iOS connectivity. The server must return HTTP 409. The iOS app must display a conflict badge. The record on iOS must match the web interface version. The `SyncConflict` table must contain one entry.

---

## 4.4 Sync Status Indicator

**FR-iOS-SYNC-004:** The Dashboard screen shall display a persistent sync status bar below the KPI cards showing:

- *Last successful sync:* Formatted timestamp (e.g., "Last synced 2 minutes ago") — sourced from the most recent `syncedAt` timestamp in the local Core Data metadata store.
- *Pending changes:* Count of `PendingSyncQueue` entries with `status = "pending"` or `status = "failed"` (e.g., "3 changes pending upload").
- *Conflict count:* Count of `SyncConflict` entries with `resolvedBy = "server"` that have not been acknowledged by the user (e.g., "1 conflict — tap to review").

When all queue entries are synced and no conflicts are pending, the status bar shall display "All changes synced" in green.

*Verifiability:* Create 3 pending offline operations. Open the Dashboard. The status bar must show "3 changes pending upload." Restore connectivity and allow sync to complete. The status bar must update to "All changes synced" within 30 seconds of the last upload confirmation.

---

## 4.5 Background Sync Task

**FR-iOS-SYNC-005:** The app shall register a `BGAppRefreshTask` with identifier `com.maduuka.ios.sync` using `BGTaskScheduler.shared.register`. The task shall:

1. Create a `URLSession` background upload task for each pending queue entry.
2. Process responses and update `PendingSyncQueue` entry statuses.
3. Call `BGTask.setTaskCompleted(success: true)` on successful completion.
4. Call `BGTask.setTaskCompleted(success: false)` if the task exceeds 25 seconds (5-second buffer before Apple's 30-second limit) to allow the OS to reschedule. Incomplete entries shall remain in `status = "pending"` for the next sync cycle.
5. Reschedule itself by calling `BGTaskScheduler.shared.submit` with `earliestBeginDate = Date(timeIntervalSinceNow: 900)` (15 minutes) on every completion.

*Verifiability:* Schedule 10 pending operations. Background the app. Wait for the background task to fire (simulate via Xcode BGTaskScheduler simulation tool). Verify all 10 entries are uploaded and their status changes to `"synced"`. Verify `setTaskCompleted(success: true)` is called within 25 seconds.

---

## 4.6 Offline Data Cache Scope

**FR-iOS-SYNC-006:** The following data sets shall be cached in the local Core Data store for offline access. The cache shall be populated on first login and updated on every successful foreground sync:

- *Product catalogue:* All active products including SKU, barcode, category, price tiers, stock levels, UOM, and photos (thumbnail resolution only — original resolution fetched on demand when online).
- *Customer list:* All active customers including name, phone, customer group, credit limit, and outstanding balance.
- *Payment methods:* All configured payment accounts and their types.
- *Business configuration:* Receipt template, tax settings, currency code, language preference, and user role/permissions.
- *Recent sales transactions:* All transactions created in the last 30 calendar days, including line items and payment breakdowns.
- *POS session state:* The currently open POS session, including opening float and all transactions within the session.

Data older than 30 days shall be eligible for purge from the local Core Data store during a background maintenance task to prevent unbounded storage growth.

*Verifiability:* On a freshly logged-in device, enable airplane mode. Navigate to POS (search for a product — must resolve from cache), Customer list (must load), Dashboard (must display KPIs from cache), and a 25-day-old transaction (must be visible). All 4 operations must succeed without any network call.
