# Integration Layer — Low-Level Design

## Overview

The Integration Layer provides adapter classes that isolate third-party API calls from core business logic. Every adapter implements an interface defined in `App\Contracts\Integration\`. If an external API is unavailable, the adapter throws a typed exception; the calling service is responsible for deciding whether to retry, queue, or surface the error to the user. All adapters are registered in the PHP-DI container and receive their credentials from environment variables, never from the database or request input.

---

## EFRISService

**Namespace:** `App\Modules\Integration\EFRIS`

**Contract:** `App\Contracts\Integration\EFRISInterface`

[CONTEXT-GAP: GAP-001] The Uganda Revenue Authority EFRIS API endpoint, authentication mechanism, request/response payload schema, and error code catalogue have not yet been confirmed. The method signatures below reflect the known business requirements; implementation details are to be finalised once the URA developer portal documentation is obtained.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `submitInvoice(array $invoicePayload): string` | Associative array conforming to the EFRIS invoice submission schema | EFRIS fiscal document number as string | Serialises `$invoicePayload` to JSON. Sends a POST request to the EFRIS submission endpoint using `curl` (via a `GuzzleHttp\Client` instance injected by PHP-DI). On HTTP 200, extracts and returns the fiscal document number. On non-200, throws `EFRISSubmissionException` with the raw response body. |
| `retrieveReceipt(string $fiscalDocNumber): array` | EFRIS fiscal document number | EFRIS receipt data as associative array | Sends a GET request to the EFRIS receipt retrieval endpoint. Returns the decoded JSON response. |

**Environment variables required:** `EFRIS_BASE_URL`, `EFRIS_API_KEY`, `EFRIS_DEVICE_NUMBER`

---

## MoMoService

**Namespace:** `App\Modules\Integration\MoMo`

**Contract:** `App\Contracts\Integration\MoMoInterface`

[CONTEXT-GAP: GAP-011] MTN MoMo and Airtel Money API credentials, sandbox vs. production endpoint configuration, and webhook signature verification have not yet been confirmed. The method signatures reflect the known payment flow requirements.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `initiateBulkDisbursement(array $recipients, string $currency = 'UGX'): string` | Array of `['phone' => string, 'amount' => float, 'reference' => string]` entries, ISO 4217 currency code | Bulk transfer request reference ID | Sends the bulk disbursement request to the MoMo Disbursements API. Returns the provider's reference ID for status polling. |
| `verifyPayment(string $referenceId): array` | Provider payment reference ID | `['status' => string, 'amount' => float, 'currency' => string, 'payer' => string]` | Polls the MoMo Collections API for the transaction status. `status` values: `SUCCESSFUL`, `FAILED`, `PENDING`. |
| `handleCallback(array $payload): void` | Decoded JSON webhook payload from the MoMo provider | `void` | Verifies the HMAC signature of the callback using `MOMO_CALLBACK_SECRET`. Finds the matching transaction record by `external_id`. Updates the transaction status. Triggers downstream actions (e.g., closing a POS transaction or releasing a cooperative payment). |

**Environment variables required:** `MOMO_SUBSCRIPTION_KEY`, `MOMO_API_USER`, `MOMO_API_KEY`, `MOMO_CALLBACK_SECRET`, `MOMO_ENVIRONMENT` (`sandbox` or `production`)

---

## AfricasTalkingService

**Namespace:** `App\Modules\Integration\AfricasTalking`

**Contract:** `App\Contracts\Integration\SMSInterface`

**Dependencies:** PHP-DI–injected `GuzzleHttp\Client`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `sendSMS(string|array $recipients, string $message, ?string $senderId = null): array` | Phone number string or array of phone number strings, message body (maximum 160 characters for single-part SMS), optional sender ID | Array of `['number' => string, 'status' => string, 'messageId' => string]` per recipient | Sends a POST request to the Africa's Talking SMS API. Uses `AT_SENDER_ID` environment variable if `$senderId` is null. Returns the per-recipient delivery status array. |
| `handleUSSD(array $sessionData): string` | Associative array with `['sessionId', 'serviceCode', 'phoneNumber', 'text']` keys from the Africa's Talking USSD callback | USSD response string prefixed with `CON ` (continue) or `END ` (terminate session) | Routes the USSD session to the appropriate USSD controller based on `$sessionData['text']` state. Returns the next menu string. |

**Environment variables required:** `AT_API_KEY`, `AT_USERNAME`, `AT_SENDER_ID`

---

## JWTService (Mobile API)

**Namespace:** `App\Modules\MobileAPI`

**Dependencies:** PHP-DI–injected `Firebase\JWT\JWT` library

`JWTService` issues and validates the JSON Web Tokens consumed by the Android (Kotlin/Compose) and iOS (Swift/SwiftUI) clients. All mobile API endpoints pass through `JWTService::validateToken()` before any business logic executes.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `issueToken(int $userId, int $tenantId, int $branchId): array` | User primary key, tenant primary key, branch primary key | `['access_token' => string, 'refresh_token' => string, 'expires_in' => int]` | Signs an access token (TTL: 3600 seconds) and a refresh token (TTL: 2592000 seconds, 30 days) using the `JWT_SECRET` environment variable and the HS256 algorithm. Stores the refresh token hash in `jwt_refresh_tokens`. |
| `validateToken(string $token): array` | Raw JWT string from the `Authorization: Bearer` header | Decoded payload as associative array | Verifies signature, issuer (`iss`), and expiry (`exp`). Throws `TokenExpiredException` if expired and `TokenInvalidException` if signature fails. |
| `refreshToken(string $refreshToken): array` | Raw refresh token string | New `['access_token' => string, 'expires_in' => int]` | Looks up the refresh token hash in `jwt_refresh_tokens`. Verifies it is not revoked. Issues a new access token. Does not rotate the refresh token unless within 7 days of expiry. |
| `revokeToken(string $refreshToken): void` | Raw refresh token string | `void` | Sets `jwt_refresh_tokens.revoked_at = NOW()` for the matching row. Used on logout. |

**Tables read/written:** `jwt_refresh_tokens`

**Environment variables required:** `JWT_SECRET`, `JWT_ISSUER`

---

## OfflineSyncService (Mobile API)

**Namespace:** `App\Modules\MobileAPI`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

`OfflineSyncService` supports the mobile clients' offline-first capability. Delta responses are computed as the set of rows changed since the client's last synchronisation timestamp, filtered by the tenant and module.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `getDelta(int $tenantId, string $module, string $lastSync): array` | Tenant primary key, module code (e.g., `INVENTORY`), ISO 8601 datetime of the client's last successful sync | Array of changed records since `$lastSync` for the module | Queries each relevant table for the module using `WHERE tenant_id = :tenantId AND updated_at > :lastSync`. Returns a structured payload with the table name, row data, and a new `sync_timestamp`. |
| `pushChanges(int $tenantId, string $module, array $changes): array` | Tenant primary key, module code, array of client-side change records with `['table', 'row', 'client_updated_at']` | Array of `['table', 'row_id', 'result']` with result codes `ACCEPTED`, `CONFLICT`, `REJECTED` | Iterates each change. If the server's `updated_at` for the row is newer than `client_updated_at`, calls `resolveConflict()`. Otherwise applies the client change via the appropriate service method. |
| `resolveConflict(string $table, int $rowId, array $clientRow, array $serverRow): array` | Table name, row primary key, client version of the row, server version of the row | Resolved row as associative array | Applies last-write-wins strategy using `updated_at` timestamp comparison. Returns the winning row and sets `result = 'CONFLICT'` in the push response so the mobile client can notify the user. |
