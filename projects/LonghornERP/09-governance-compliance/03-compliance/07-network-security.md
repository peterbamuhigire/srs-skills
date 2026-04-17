# Transport and Network Security

## 7.1 Transport Layer Security

### 7.1.1 Required Protocol Version

The system shall require Transport Layer Security (TLS) version 1.3 for all connections between clients and the platform. Where TLS 1.3 is not available on the client or intermediate infrastructure, TLS 1.2 is the minimum acceptable version. TLS 1.1 and all earlier versions shall be disabled at the web server configuration level. SSL 3.0 shall be disabled.

### 7.1.2 Cipher Suite Restriction

The server shall be configured to support only cipher suites that provide forward secrecy. RC4, 3DES, and MD5-based cipher suites shall be disabled. The permitted cipher suite list shall be maintained in the Apache SSL configuration and shall be reviewed at each major deployment update.

### 7.1.3 HTTP Strict Transport Security

The system shall include an `HTTP Strict-Transport-Security` (HSTS) header on all responses from HTTPS endpoints. The header value shall be:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

This instructs all compliant browsers to refuse non-HTTPS connections to the domain for 365 days. HSTS preloading is recommended but is subject to confirmation during production domain setup.

## 7.2 Mandatory HTTP Security Headers

Every response from the system — web pages, web API, mobile API, Super Admin Panel — shall include the following security headers:

| Header | Required Value | Purpose |
|---|---|---|
| `X-Content-Type-Options` | `nosniff` | Prevents MIME-type sniffing by browsers |
| `X-Frame-Options` | `DENY` | Prevents clickjacking via iframe embedding |
| `Content-Security-Policy` | See Section 7.2.1 | Restricts sources of executable content |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Limits referrer header leakage |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` | Restricts browser feature access |

### 7.2.1 Content Security Policy Definition

The Content Security Policy (CSP) for the Tenant Workspace and Super Admin Panel shall restrict resource loading as follows:

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'nonce-{request-nonce}';
  style-src 'self' 'unsafe-inline';
  img-src 'self' data:;
  font-src 'self';
  connect-src 'self';
  frame-ancestors 'none';
  form-action 'self';
  base-uri 'self';
  object-src 'none'
```

The `{request-nonce}` value shall be a cryptographically random nonce generated per request and injected into the CSP header and the corresponding `<script>` tags. TinyMCE rich text editor integration may require `'unsafe-inline'` for style; this exception shall be scoped to the minimum required directive and documented in the deployment runbook.

The CSP for the mobile API (`/public/api/mobile/v1/`) shall include `frame-ancestors 'none'` and `default-src 'none'`, as API responses are not rendered in a browser context.

## 7.3 Rate Limiting

### 7.3.1 Algorithm

The system shall implement rate limiting using the token bucket algorithm. Each token bucket is keyed on a combination of `tenant_id` and `user_id` for authenticated requests, and on IP address for unauthenticated requests (e.g., login endpoint).

### 7.3.2 Configuration

Rate limit values shall be stored in the `api_rate_limits` table, not hardcoded. The table shall support configuration at three levels of specificity:

1. Platform default (applies to all tenants and users not covered by a more specific rule).
2. Tenant override (applies to all users of a specific tenant).
3. User override (applies to a specific user within a specific tenant).

The more specific rule takes precedence. Super administrators shall be able to adjust rate limit values through the Super Admin Panel without a code deployment.

### 7.3.3 Response on Limit Exceeded

When a request exceeds the applicable rate limit, the system shall:

- Return HTTP 429 with a `Retry-After` header indicating the number of seconds until the next token is available.
- Log the rate-limit event in the application error log (not in the audit log, to avoid inflating the audit table with high-frequency automated events).
- Not reveal the internal bucket configuration to the client.

## 7.4 Cross-Origin Resource Sharing

### 7.4.1 Mobile API Endpoints

Cross-Origin Resource Sharing (CORS) shall be enabled for mobile API endpoints at `/public/api/mobile/v1/`. The `Access-Control-Allow-Origin` header shall allow all origins (`*`) for these endpoints, as mobile applications do not operate within a browser origin context. Preflight OPTIONS requests shall be handled with the appropriate `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers` responses.

### 7.4.2 Web API Endpoints

CORS shall be disabled for web API endpoints at `/public/api/` and `/public/superadmin/api/`. These endpoints are consumed exclusively by the same-origin web application. The `Access-Control-Allow-Origin` header shall not be set on responses from these paths. Requests carrying an `Origin` header that does not match the server's own domain shall receive HTTP 403.

## 7.5 Internal Network Security

The Super Admin Panel (`/public/superadmin/`) should be restricted at the network level to known operator IP addresses or accessed through a VPN. This is a deployment recommendation, not an application-level control. The deployment runbook shall document the required Apache IP restriction configuration.
