# Mobile Architecture

## 10.1 Overview

Longhorn ERP shall deliver a native mobile experience for both Android and iOS platforms. The mobile applications are companion clients to the web platform: they consume the same tenant data through the JWT-secured Mobile API v1 and enforce the same multi-tenancy, RBAC, and localisation rules.

## 10.2 Platform Technologies

| Platform | Language | UI Framework |
|---|---|---|
| Android | Kotlin | Jetpack Compose |
| iOS | Swift | SwiftUI |

Both applications are built as native clients — no cross-platform bridge framework is used. Native development is chosen to maximise integration with device capabilities (biometric authentication, offline storage, push notifications, background sync).

## 10.3 API Integration

Both Android and iOS clients consume the Mobile API v1 at `/public/api/mobile/v1/`. All API communication uses:

- **Protocol:** REST over HTTPS (TLS 1.3).
- **Data format:** JSON.
- **Authentication:** JWT Bearer token (see Section 6.3 for token structure and refresh rotation).
- **Tenant isolation:** The `tid` JWT claim carries the `tenant_id`. The mobile client never sends `tenant_id` as a request body parameter — the server always derives it from the validated token.

## 10.4 Offline Sync Architecture

Network conditions in Uganda and East Africa range from fibre broadband (≥ 10 Mbps) to intermittent 2G/EDGE (< 200 kbps). The mobile architecture shall maintain core functionality at ≤ 200 kbps connection throughput.

### Sync Protocol

The system uses a last-modified timestamp synchronisation protocol:

1. The mobile client stores a `last_sync_timestamp` per entity type (e.g., customers, items, invoices).
2. On sync, the client sends a request to the relevant sync endpoint with the `last_modified` query parameter set to the stored timestamp.
3. The server returns only records modified after that timestamp (delta sync).
4. The client applies the delta to its local store and updates `last_sync_timestamp`.

### Cooperative Procurement Offline Mode

The Cooperative Procurement module (`COOPERATIVE`) shall support full offline intake for up to 72 hours. Field agents operating at farmer collection points without connectivity shall be able to:

- Record commodity intake transactions (commodity type, weight, grading, farmer identity).
- View the farmer's running balance and previous intake records (last synced).
- Issue printed or on-screen acknowledgement receipts.

On reconnection, the system shall sync all pending offline transactions to the server within 60 seconds (NFR-MOBILE-001). Conflict resolution follows a last-write-wins policy with server-side timestamp authority; conflicts are flagged in the audit log for supervisor review.

## 10.5 Push Notifications

The mobile applications shall receive push notifications for the following events:

| Event Type | Trigger |
|---|---|
| Approval required | A document (purchase order, leave request, payment) is routed to the user for approval. |
| Payment confirmation | A mobile money payment initiated from the app is confirmed by the gateway. |
| Stock alert | A stock item falls below its reorder level (where the user has inventory management access). |
| Payslip published | HR publishes payslips for the current period (employee self-service). |

Push notification delivery uses the platform notification service. The mobile app registers a device token on login; the server routes notifications to the device token associated with the authenticated user.

## 10.6 Data-Lite Mode

For users on 3G or low-bandwidth connections, the mobile app shall support a data-lite mode that:

- Compresses API responses (gzip/deflate, HTTP `Accept-Encoding`).
- Defers loading of non-critical images and charts until explicitly requested.
- Reduces pagination batch sizes to 20 records per request (compared to the standard 50).
- Disables auto-refresh polling; updates require a manual pull-to-refresh action.

Data-lite mode is activated manually by the user or automatically when the device reports a metered connection.

## 10.7 Biometric Authentication

The mobile app shall support biometric login (fingerprint and face recognition) on devices that provide the platform biometric API (Android BiometricPrompt; iOS LocalAuthentication). Biometric authentication unlocks a securely stored refresh token; the server is not involved in the biometric verification itself. The biometric-gated token must still pass server-side JWT validation on every API request.

## 10.8 Mobile-Specific NFR Summary

| NFR ID | Requirement |
|---|---|
| NFR-MOBILE-001 | The Cooperative Procurement module shall support offline intake for up to 72 hours and sync within 60 seconds of reconnection. |
| NFR-PERF-003 | The Mobile API shall return any REST response in ≤ 500 ms at P95 under 50 concurrent mobile clients per tenant. |
| NFR-SEC-001 | The `tenant_id` shall always be derived from the validated JWT `tid` claim — never from a request body parameter. |
