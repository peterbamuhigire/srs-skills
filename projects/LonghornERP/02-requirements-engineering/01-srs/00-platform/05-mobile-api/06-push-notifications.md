## 6. Push Notifications

This section specifies the push notification dispatch model. Push notifications are server-initiated messages delivered to registered mobile devices to alert users of actionable events without requiring the app to be open. iOS delivery uses Apple Push Notification service (APNs); Android delivery uses Firebase Cloud Messaging (FCM). SMS fallback is provided via Africa's Talking for tenants where mobile data connectivity is unreliable.

### 6.1 Notification Events

**FR-MAPI-060:** The system shall send a push notification to the relevant mobile device(s) when any of the following events occurs:

- Approval required — a Purchase Order (PO), leave request, or journal entry has been submitted and is awaiting the authenticated user's approval.
- Approval decision — a PO, leave request, or journal entry submitted by the authenticated user has been approved or rejected by an approver.
- Payment received — a customer payment has been recorded against a sales invoice owned by the authenticated user's assigned account.
- Low stock alert — a stock item's quantity on hand has fallen below the reorder point configured for the tenant, triggering an alert to users with the `INVENTORY_MANAGER` role.
- Payslip available — a payslip has been generated for the authenticated employee for the current payroll period.

- Test oracle (approval required): Submit a PO for approval; assert the approver's registered device receives a push notification with `event_type: "approval_required"` within 30 seconds.

**FR-MAPI-061:** The system shall include the following fields in every push notification payload: `event_type` (string, one of the values in FR-MAPI-060), `entity_type` (e.g., `purchase_order`, `leave_request`), `entity_id` (string), `tenant_id` (string), `message` (human-readable summary ≤ 120 characters), and `timestamp` (ISO-8601).

- Test oracle: Capture the FCM/APNs payload for any notification event; assert all 6 fields are present with correct types and non-null values.

**FR-MAPI-062:** The system shall not include sensitive financial amounts, personal employee data, or full account details in push notification payloads, as notifications may be displayed on lock screens. The `message` field shall contain a summary reference (e.g., "PO #PO-2026-00123 awaiting your approval") without exposing full data.

- Test oracle: Review the `message` field of a payslip notification; assert it contains only the pay period reference and not the net pay amount or bank account details.

### 6.2 Device Token Management

**FR-MAPI-063:** The system shall accept device push notification token registration via `POST /api/mobile/v1/devices` with the following required fields: `device_token` (string), `platform` (`android` or `ios`), and `app_version` (string). The endpoint shall be authenticated with a valid JWT.

- Test oracle: Submit a valid device registration request; assert HTTP 201 and a `device_id` in the response; assert the record is stored in `mobile_devices` under the authenticated tenant and user.

**FR-MAPI-064:** The system shall deregister all push notification device tokens for a user when that user's account is disabled or when the user explicitly calls `DELETE /api/mobile/v1/devices/{device_id}`.

- Test oracle: Register a device; disable the user account; assert the `mobile_devices` record is marked inactive; assert no further push notifications are dispatched to that token.

**FR-MAPI-065:** The system shall handle APNs and FCM token refresh events by updating the stored `device_token` when a mobile client re-registers with a new token for the same device identifier, preventing notification delivery failures caused by stale tokens.

- Test oracle: Re-register a device with a new `device_token` for the same `device_id`; assert the `mobile_devices` table contains 1 record for that device with the updated token.

### 6.3 Delivery Assurance and SMS Fallback

**FR-MAPI-066:** The system shall retry push notification delivery up to 3 attempts with exponential backoff (attempt 1: immediate; attempt 2: 30 seconds; attempt 3: 90 seconds) when the push notification provider (APNs or FCM) returns a delivery failure code.

- Test oracle: Simulate an APNs/FCM failure response; assert 3 delivery attempts are logged with timestamps matching the backoff schedule; assert no further attempts occur after the 3rd failure.

**FR-MAPI-067:** The system shall send an SMS fallback message via Africa's Talking when push notification delivery fails after 3 attempts, provided the user's profile includes a verified mobile phone number and the tenant's Africa's Talking credentials are configured.

- Test oracle: Disable a user's registered device token; trigger a notification event; assert 3 push attempts fail; assert an SMS is dispatched via Africa's Talking to the user's registered phone number within 5 minutes of the 3rd push failure.

**FR-MAPI-068:** The system shall log every push notification dispatch attempt (success or failure) in the `notification_log` table, recording: `user_id`, `tenant_id`, `event_type`, `platform`, `device_token` (last 8 characters only, to avoid storing full tokens in logs), `delivery_status`, `attempt_number`, and `attempted_at` timestamp.

- Test oracle: Trigger a notification; assert a corresponding row exists in `notification_log` with all required fields populated; assert `device_token` is truncated to 8 characters.

### 6.4 Notification Preferences

**FR-MAPI-069:** The system shall allow a mobile user to configure per-event-type push notification preferences via `PUT /api/mobile/v1/notifications/preferences`. A user may disable any notification event type individually. The system shall honour these preferences before dispatching a notification.

- Test oracle: Disable `low_stock_alert` notifications for a user; trigger a low stock alert event; assert no push notification is dispatched to that user's device.

**FR-MAPI-070:** The system shall apply a daily quiet hours window per user preference (configurable start and end time in the user's local timezone) during which push notifications are queued and dispatched when the quiet hours window ends, rather than delivered immediately.

- Test oracle: Set quiet hours 22:00–07:00 for a user; trigger a notification event at 23:00; assert the notification is not dispatched until 07:00; assert it arrives within 60 seconds of the quiet hours window ending.
