## 5. Offline Data Collection and Synchronisation

This section specifies the offline data collection capability and the delta synchronisation protocol used by mobile clients operating in low-connectivity environments. The primary use case is commodity intake recording by field agents using the Cooperative Procurement module, where network connectivity is intermittent or absent for extended periods.

### 5.1 Offline Data Collection

**FR-MAPI-040:** The system shall support offline data collection for the Cooperative Procurement module for up to 72 hours without connectivity, enabling field agents to record commodity intake transactions locally on the mobile device without a server connection (NFR-MAPI-002).

- Test oracle: Disable network access on a test device; record 50 commodity intake transactions over a 72-hour period; restore network access; assert all 50 transactions sync successfully to the server.

**FR-MAPI-041:** The system shall synchronise all pending offline transactions to the server within 60 seconds of connectivity restoration, without requiring any manual action from the mobile user.

- Test oracle: Record 10 offline transactions; restore network access; assert all 10 transactions appear in the server database within 60 seconds, measured from the moment the device regains network access.

### 5.2 Delta Synchronisation Protocol

**FR-MAPI-042:** The system shall use a last-modified timestamp protocol for delta synchronisation: when a mobile client calls `POST /api/mobile/v1/sync`, the request body shall include a `last_sync_at` ISO-8601 timestamp; the server shall return only records belonging to the authenticated tenant and user that have a `modified_at` value greater than `last_sync_at`.

- Test oracle: Perform an initial full sync (omit `last_sync_at`); modify 3 records on the server; perform a delta sync with the previous sync timestamp; assert the response contains exactly 3 records.

**FR-MAPI-043:** The system shall detect and flag data conflicts when the same record has been modified both on the mobile device (offline) and on the server since the last successful sync. Conflicting records shall be marked with `"conflict": true` in the sync response and shall not be silently overwritten. The conflict shall be presented to the user for manual resolution.

- Test oracle: Modify record R on the server; modify the same record R offline; trigger a sync; assert the sync response contains record R with `"conflict": true`; assert the server's copy of R is unchanged after the sync.

**FR-MAPI-044:** The system shall provide a sync status endpoint at `GET /api/mobile/v1/sync/status` that returns the following fields for the authenticated user: `pending_upload_count` (integer count of transactions queued for upload), `last_sync_at` (ISO-8601 timestamp of the last successful sync), and `conflict_count` (integer count of unresolved conflicts).

- Test oracle: Queue 5 offline transactions; call the sync status endpoint; assert `pending_upload_count` = 5 and `last_sync_at` matches the previous successful sync timestamp.

### 5.3 Sync Integrity

**FR-MAPI-045:** The system shall assign a client-generated Universally Unique Identifier (UUID v4) to each offline transaction at the time of local creation. The server shall use this UUID as an idempotency key to prevent duplicate records when a sync request is retried due to a network interruption.

- Test oracle: Submit the same sync payload (containing the same transaction UUID) twice; assert the server contains exactly 1 record for that UUID; assert HTTP 200 on both submissions (not HTTP 409).

**FR-MAPI-046:** The system shall record the `device_id`, `synced_at` timestamp, and `sync_attempt_count` for every transaction successfully written to the server during synchronisation, stored in the `mobile_sync_log` table under the authenticated tenant and user.

- Test oracle: Sync 5 transactions from a registered device; assert the `mobile_sync_log` table contains 5 rows with correct `device_id`, non-null `synced_at`, and `sync_attempt_count` ≥ 1.

**FR-MAPI-047:** The system shall return HTTP 422 Unprocessable Entity with a field-level error body when a synced transaction fails server-side validation (e.g., referenced supplier does not exist for the tenant). The invalid transaction shall be excluded from the committed sync batch; all other valid transactions in the same batch shall be committed.

- Test oracle: Submit a sync batch of 5 transactions in which 1 references a non-existent supplier; assert HTTP 207 Multi-Status; assert 4 records are committed; assert the invalid record is returned with a field-level error.

**FR-MAPI-048:** The system shall enforce a maximum offline transaction batch size of 500 records per sync request. Requests exceeding this limit shall return HTTP 413 Payload Too Large with `{"error": "batch_size_exceeded", "max": 500}`.

- Test oracle: Submit a sync request with 501 transaction records; assert HTTP 413 with the specified error body; assert no records from the batch are committed.

### 5.4 Offline-Capable Modules

**FR-MAPI-049:** The system shall restrict offline data collection to the Cooperative Procurement module in Mobile API version 1. Other modules require active connectivity and shall return HTTP 503 Service Unavailable with `{"error": "offline_not_supported"}` if the client attempts an offline-mode sync for those modules.

- Test oracle: Submit an offline sync payload tagged with module code `ACCOUNTING`; assert HTTP 503 with the specified error body.

**FR-MAPI-050:** The system shall provide a module capability endpoint at `GET /api/mobile/v1/modules/capabilities` that returns a JSON object listing each module code and a boolean `offline_supported` field, enabling mobile clients to determine offline eligibility without hardcoding.

- Test oracle: Call the capabilities endpoint; assert `COOPERATIVE_PROCUREMENT` has `"offline_supported": true`; assert all other module codes have `"offline_supported": false`.

**FR-MAPI-051:** The system shall allow a tenant administrator to download a reference data snapshot (active suppliers, commodity types, unit-of-measure codes) via `GET /api/mobile/v1/sync/reference-data` for pre-loading on the mobile device before field deployment, to support form population during offline sessions.

- Test oracle: Call the reference data endpoint with a valid JWT; assert the response contains `suppliers`, `commodity_types`, and `uom_codes` arrays, each filtered to the authenticated tenant.

**FR-MAPI-052:** The system shall include a `data_version` hash in the reference data snapshot response. When the mobile client detects that the server-side `data_version` has changed (via the sync status endpoint), it shall re-download the full reference data snapshot.

- Test oracle: Add a new supplier for the tenant; call the sync status endpoint; assert `reference_data_version` has changed relative to the previously recorded hash.

**FR-MAPI-053:** The system shall store pending offline transactions in an encrypted local database on the mobile device, using AES-256 encryption keyed to the device's secure enclave (iOS Keychain / Android Keystore). This requirement is a mobile client implementation constraint documented here for traceability.

- Test oracle: Extract the local database file from the device storage; assert the file is not readable as plaintext without the device key.

**FR-MAPI-054:** The system shall present a visual sync status indicator in the mobile app showing one of 3 states — *Synced*, *Pending Sync*, or *Sync Failed* — updated within 2 seconds of any change in sync state. This requirement is a mobile client implementation constraint documented here for traceability.

- Test oracle: Queue an offline transaction; assert the indicator transitions to *Pending Sync* within 2 seconds; complete a sync; assert the indicator transitions to *Synced* within 2 seconds.

**FR-MAPI-055:** The system shall reject sync requests from a mobile client whose JWT has expired or been revoked during the offline period, returning HTTP 401. The mobile client shall prompt the user to re-authenticate before the next sync attempt.

- Test oracle: Record offline transactions; allow the JWT to expire; trigger a sync; assert HTTP 401; assert the mobile app displays a re-authentication prompt rather than silently discarding pending transactions.
