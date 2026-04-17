## 5. Non-Functional Requirements

### 5.1 Session Invalidation Latency

**NFR-RBAC-001:** The system shall invalidate all active sessions for a user within 5 seconds of an administrator disabling that user's account or triggering a forced logout action, measured from the moment the administrator action is persisted to the database to the moment the next request from any of the user's sessions receives an unauthenticated response.

*Verification method:* Integration test — disable a user account with 3 concurrent active sessions; assert that all 3 sessions return HTTP 401 within 5 seconds of the disable timestamp.

### 5.2 Permission Evaluation Latency

**NFR-RBAC-002:** The system shall evaluate role permissions for any authenticated page request and return the authorisation decision within 50 ms at P95, measured from the point at which the permission check is invoked to the point at which the allow or deny result is returned, under a load of 100 concurrent authenticated users per tenant.

*Verification method:* Load test — 100 virtual users each making 60 authenticated page requests per minute; assert P95 permission evaluation latency ≤ 50 ms using server-side instrumentation.

### 5.3 Concurrent Authenticated User Capacity

**NFR-RBAC-003:** The system shall support ≥ 500 concurrent authenticated users per tenant without session degradation — defined as no increase in session lookup latency beyond the P95 threshold of 50 ms (see NFR-RBAC-002) and no session loss or corruption events — under steady-state load.

*Verification method:* Load test — ramp to 500 concurrent authenticated users per tenant; assert zero session corruption events and P95 permission evaluation latency ≤ 50 ms throughout the test run.

### 5.4 TOTP Verification Latency

**NFR-RBAC-004:** A TOTP 2FA verification shall complete — from the moment the user submits the 6-digit code to the moment the system returns the authentication result — within 3 seconds at P95, measured at the server side, under a load of 100 concurrent 2FA login requests per tenant.

*Verification method:* Load test — 100 concurrent 2FA login requests per tenant; assert P95 server-side TOTP verification duration ≤ 3 seconds.

### 5.5 Permission Cache Invalidation Latency

**NFR-RBAC-005:** The system shall cache role permissions per user session and shall invalidate the cached permission set within 10 seconds of any role permission change or role reassignment being committed to the database, ensuring that subsequent requests by the affected user reflect the updated permissions.

*Verification method:* Integration test — modify a role's permission for a function; assert that the next authenticated request by a user assigned to that role, made ≥ 10 seconds after the change, returns the updated permission decision; assert that a request made < 10 seconds after may return either the old or new decision without error.
