## 3. Tenant Isolation for Mobile API Requests

This section specifies tenant isolation enforcement at the Mobile API boundary. Requirements apply the same row-level isolation model as the web session API, sourcing the `tenant_id` exclusively from the validated JWT `tid` claim. These requirements enforce NFR-SEC-001 (Tenant Data Isolation) for the mobile surface.

### 3.1 Tenant Identifier Sourcing

**FR-MAPI-020:** The system shall enforce tenant isolation for all Mobile API requests by reading the `tenant_id` exclusively from the `tid` claim of the validated JWT access token. The system shall never accept a `tenant_id` from request parameters, query strings, request headers (other than the Authorization Bearer), or the request body.

- Test oracle: Submit an authenticated request with a `tenant_id` field injected into the request body set to a different tenant's identifier; assert the response contains only data belonging to the JWT `tid` tenant.

**FR-MAPI-021:** The system shall apply the `tenant_id` from the JWT `tid` claim to every database query executed during Mobile API request processing, ensuring no query returns, modifies, or deletes records belonging to a different tenant.

- Test oracle: Construct a database query trace for any Mobile API endpoint; assert every `WHERE` clause includes `tenant_id = <tid from JWT>`.

### 3.2 Cross-Tenant Access Attempts

**FR-MAPI-022:** The system shall return HTTP 404 Not Found for any Mobile API request that attempts to access a resource identified by a primary key that does not belong to the authenticated tenant, regardless of whether the resource exists in another tenant's data set.

- Test oracle: Authenticate as Tenant A; request a record belonging to Tenant B by its known primary key; assert HTTP 404 (not HTTP 403 or HTTP 401, to avoid confirming the resource exists).

**FR-MAPI-023:** The system shall log cross-tenant access attempts as security anomalies in the audit log, recording the authenticated `user_id`, `tenant_id`, the requested resource identifier, and the request timestamp.

- Test oracle: Trigger a cross-tenant access attempt; assert an audit log entry with `event_type = 'cross_tenant_attempt'` is inserted within 1 second, containing the correct `user_id` and `tenant_id`.

### 3.3 Module Access Gating

**FR-MAPI-024:** The system shall return HTTP 403 Forbidden for any Mobile API request that targets an endpoint belonging to a module whose code is not present in the authenticated JWT `modules` claim array.

- Test oracle: Issue a JWT with `modules: ["ACCOUNTING", "HR"]`; submit a request to an endpoint in the `COOPERATIVE_PROCUREMENT` module; assert HTTP 403 with `{"error": "module_not_enabled"}`.

**FR-MAPI-025:** The system shall not expose module-specific endpoints in API responses (e.g., HATEOAS links, version discovery) for modules not present in the JWT `modules` claim, preventing information leakage about disabled modules.

- Test oracle: Call `GET /api/mobile/versions`; assert the response does not reference endpoints for modules absent from the JWT `modules` claim.
