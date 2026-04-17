## 7. Rate Limiting

This section specifies the token bucket rate limiting model applied to all Mobile API requests. Rate limiting protects the platform from abuse, prevents runaway mobile clients from degrading service for other tenants, and enforces fair use across the multi-tenant deployment.

### 7.1 Rate Limit Enforcement

**FR-MAPI-080:** The system shall enforce rate limits on all Mobile API requests using the token bucket algorithm. Per-tenant and per-user rate limit configurations shall be stored in the `api_rate_limits` table with the following columns: `tenant_id`, `user_id` (nullable — null applies a tenant-wide limit), `endpoint_pattern` (nullable — null applies to all endpoints), `limit` (integer, tokens per window), and `window_seconds` (integer).

- Test oracle: Configure a limit of 60 requests per 60 seconds for a test user; submit 61 requests within 60 seconds; assert the 61st request returns HTTP 429; assert the first 60 return HTTP 200 (or the appropriate success code).

**FR-MAPI-081:** The system shall return HTTP 429 Too Many Requests when a mobile client exceeds its configured rate limit. The response body shall contain `{"error": "rate_limit_exceeded", "retry_after": <seconds>}`. The response shall include a `Retry-After` header whose value equals the number of seconds until the client's token bucket is replenished.

- Test oracle: Exhaust the rate limit for a test user; assert HTTP 429 with `Retry-After` header present; wait for the indicated duration; assert the next request succeeds.

**FR-MAPI-082:** The system shall apply the most specific matching rate limit rule for a given request in the following precedence order (highest to lowest): per-user per-endpoint, per-user all-endpoints, per-tenant per-endpoint, per-tenant all-endpoints, global default.

- Test oracle: Configure a per-user per-endpoint limit of 10/min and a per-tenant all-endpoints limit of 1000/min for the same user; exhaust the per-user per-endpoint limit; assert HTTP 429 despite the tenant-wide limit not being exhausted.

**FR-MAPI-083:** The system shall include the following rate limit status headers on every Mobile API response, regardless of whether the limit has been exceeded:

- `X-RateLimit-Limit` — the total token capacity for the current window.
- `X-RateLimit-Remaining` — the number of tokens remaining in the current window.
- `X-RateLimit-Reset` — the Unix timestamp at which the current window resets and the bucket is refilled.

- Test oracle: Submit any authenticated Mobile API request; assert all 3 headers are present in the response with integer values; assert `X-RateLimit-Remaining` decrements by 1 on each subsequent request within the same window.

### 7.2 Rate Limit Configuration

**FR-MAPI-084:** The system shall apply a platform-wide default rate limit of 120 requests per 60 seconds per user when no matching rule exists in the `api_rate_limits` table for the authenticated user or tenant. This default may be overridden by a super administrator for any tenant.

- Test oracle: Authenticate as a user with no entry in `api_rate_limits`; assert `X-RateLimit-Limit` = 120 and `X-RateLimit-Reset` advances by 60 seconds per window.

**FR-MAPI-085:** The system shall allow a super administrator to modify rate limit rules in the `api_rate_limits` table via the Super Admin API at `POST /superadmin/api/rate-limits`. Changes shall take effect within 30 seconds of submission without requiring a server restart.

- Test oracle: Submit a new rate limit rule via the Super Admin API; wait 30 seconds; submit a mobile API request under the affected tenant; assert the new limit is reflected in the `X-RateLimit-Limit` header.
