# 7. Offline Mobile Intake Requirements

## 7.1 Overview

This section specifies requirements for the mobile application's offline intake capability. Collection centres in rural Uganda, Kenya, and Rwanda frequently have no reliable internet access. The system shall sustain full intake recording for a continuous offline period of up to 72 hours, then synchronise without data loss when connectivity is restored.

## 7.2 Offline Mode Activation and Duration

**FR-COOP-059** — When the mobile application detects that internet connectivity is unavailable (zero HTTP response within 10 seconds of a connectivity probe), the system shall automatically switch to offline mode, display a persistent banner: "Offline mode — data will sync when connected", and continue to accept intake entries using the locally cached commodity, grade, price, and farmer data.

*Acceptance criterion:* With Wi-Fi disabled, the app displays the offline banner within 10 seconds and successfully records 5 intake entries; no data loss occurs.

**FR-COOP-060** — When the device has been in offline mode for 68 hours (4 hours before the 72-hour limit), the system shall display a warning notification: "Offline mode expires in 4 hours. Connect to internet to sync data." When the device reaches 72 hours of continuous offline operation without syncing, the system shall lock new intake entry creation and display: "Offline data limit reached. Sync required before recording more intake."

*Acceptance criterion:* The 68-hour warning is displayed at exactly 68 hours (± 5 minutes); at 72 hours the intake form is disabled and the lock message is displayed.

## 7.3 Local Data Storage

**FR-COOP-061** — When a collection officer records an intake entry in offline mode, the system shall persist the entry to the device's local encrypted database, assign a temporary local reference number (prefixed `TMP-`), and include: farmer ID, commodity, grade, weight, date, GPS timestamp of the device, and the device's offline session ID.

*Acceptance criterion:* 50 intake entries recorded offline are visible in the offline queue with `TMP-` prefixed references; the local database file is AES-256 encrypted; entries are not accessible outside the application sandbox.

## 7.4 Sync and Conflict Resolution

**FR-COOP-062** — When internet connectivity is restored, the mobile application shall automatically initiate a sync within 30 seconds of detecting connectivity, transmit all locally queued intake entries to the server in chronological order, and display a sync progress indicator with the count of entries pending and entries confirmed.

*Acceptance criterion:* On Wi-Fi re-connection, sync begins within 30 seconds; a queue of 40 entries is transmitted and confirmed within 60 seconds on a 3G-equivalent connection (1 Mbps downlink, 512 kbps uplink).

**FR-COOP-063** — When the server receives a synced intake entry and a conflicting entry for the same farmer on the same date and commodity already exists (submitted by another device or user), the system shall:

1. Retain both entries in a conflict queue.
2. Notify the sync initiator: "Conflict detected for Farmer [Name] on [Date] — [N] entries require manual review."
3. Present both entries side-by-side for the supervisor to resolve by selecting the authoritative entry or merging the weights.
4. Archive the rejected entry with status "Conflict — Rejected" and retain it in the audit log.

*Acceptance criterion:* A simulated conflict produces the notification, the side-by-side review screen, and after resolution the winning entry is posted and the losing entry is archived as "Conflict — Rejected".

**FR-COOP-064** — When a sync is interrupted mid-transmission (connectivity drops before all entries are confirmed), the system shall resume the sync from the last unconfirmed entry on the next connectivity event without duplicating any already-confirmed entries.

*Acceptance criterion:* Interrupt a sync after 20 of 40 entries are confirmed; on reconnection, only the remaining 20 are retransmitted; the server receives a total of exactly 40 unique entries.

## 7.5 Offline Data Security

**FR-COOP-065** — When the mobile application is installed on a device, the local offline database shall be encrypted using AES-256 with a key derived from the authenticated user's session token; the database shall be wiped (all offline data deleted) if the user logs out, the session is remotely revoked, or the device is reported as lost by an administrator.

*Acceptance criterion:* Remote device revocation by an administrator triggers database wipe within 60 seconds on a connected device; on a disconnected device, the wipe executes on the next app launch after connectivity is restored. Local database files are unreadable when extracted from the device and opened outside the application.

[CONTEXT-GAP: Target mobile platform(s) — confirm whether offline capability is required for Android only, iOS only, or both, to specify the local database engine (e.g., SQLite via Room for Android, Core Data / SQLite for iOS).]

[CONTEXT-GAP: Minimum device hardware specification for offline collection officers — confirm minimum Android API level and available storage to size the 72-hour offline data footprint.]
