## 10. Traceability Matrix

This matrix maps every functional requirement and non-functional requirement in this SRS to its originating business goal, the platform standard it enforces, and the test case classification required for verification. Unresolved traceability links are flagged as `[TRACE-GAP]` per the project V&V SOP.

### 10.1 Functional Requirements Traceability

| Requirement ID | Requirement Summary | Business Goal | Platform Standard | Test Classification |
|---|---|---|---|---|
| **FR-MAPI-001** | Issue JWT access token and refresh token on valid login | Secure mobile access | RFC 7519, NIST SP 800-63B | Integration |
| **FR-MAPI-002** | JWT contains: `tid`, `uid`, `role`, `modules`, `iat`, `exp` | Tenant-scoped, role-gated access | RFC 7519, OWASP API2 | Unit |
| **FR-MAPI-003** | `tid` sourced from database, never from request body | Prevent tenant impersonation | OWASP API2, NFR-SEC-001 | Security / Penetration |
| **FR-MAPI-004** | Refresh token rotation on each use | Prevent token replay attacks | NIST SP 800-63B, OWASP API2 | Integration |
| **FR-MAPI-005** | Configurable JWT access and refresh token TTL | Operational flexibility | RFC 7519 | Unit |
| **FR-MAPI-006** | HTTP 401 for expired JWT | Enforce token expiry | RFC 6750, OWASP API2 | Integration |
| **FR-MAPI-007** | HTTP 401 for invalid JWT signature or malformed token | Reject tampered tokens | RFC 7519, OWASP API2 | Security |
| **FR-MAPI-008** | HTTP 401 for revoked JWT | Enforce blacklist | OWASP API2 | Integration |
| **FR-MAPI-009** | Invalidate all user tokens within 5 s of account disable | Immediate access revocation | NFR-SEC-003 | Integration |
| **FR-MAPI-010** | Blacklist access and refresh tokens on logout | Clean session termination | OWASP API2 | Integration |
| **FR-MAPI-011** | Blacklist entry TTL = token remaining validity | Prevent indefinite blacklist growth | Operational efficiency | Unit |
| **FR-MAPI-012** | Issue new token pair on valid refresh token | Uninterrupted mobile sessions | RFC 7519 | Integration |
| **FR-MAPI-013** | HTTP 401 for expired or revoked refresh token | Enforce refresh token lifecycle | RFC 7519, OWASP API2 | Integration |
| **FR-MAPI-014** | Device push token registration | Enable push notification delivery | Platform capability | Integration |
| **FR-MAPI-015** | Upsert device token registration (no duplicates) | Data integrity | Platform capability | Unit |
| **FR-MAPI-020** | `tenant_id` sourced exclusively from JWT `tid` claim | Prevent tenant data leakage | NFR-SEC-001, OWASP API3 | Security / Penetration |
| **FR-MAPI-021** | All queries scoped by JWT `tid` | Row-level tenant isolation | NFR-SEC-001 | Security |
| **FR-MAPI-022** | HTTP 404 for cross-tenant resource access | Prevent tenant enumeration | OWASP API3, NFR-SEC-001 | Security / Penetration |
| **FR-MAPI-023** | Audit log entry for cross-tenant access attempts | Security observability | ISO/IEC 27001 | Integration |
| **FR-MAPI-024** | HTTP 403 for disabled-module endpoints | Module-level access control | RBAC model | Integration |
| **FR-MAPI-025** | No module endpoint leakage in discovery responses | Prevent information disclosure | OWASP API3 | Security |
| **FR-MAPI-030** | API versioning via `/api/mobile/v{N}/` URL path | Client backward compatibility | API lifecycle management | Integration |
| **FR-MAPI-031** | ≥ 2 active API versions simultaneously | Zero-disruption upgrades | API lifecycle management | Integration |
| **FR-MAPI-032** | No breaking changes within a version | Client contract stability | API lifecycle management | Contract testing |
| **FR-MAPI-033** | ≥ 90-day deprecation window before version sunset | Client migration runway | API lifecycle management | Operational |
| **FR-MAPI-034** | `GET /api/mobile/versions` version discovery endpoint | Client version negotiation | API lifecycle management | Integration |
| **FR-MAPI-035** | `Deprecation` and `Sunset` headers on deprecated version responses | Programmatic deprecation detection | RFC 8594 | Integration |
| **FR-MAPI-040** | Offline data collection for ≥ 72 hours (Cooperative Procurement) | Field agent productivity | NFR-MAPI-002, NFR-MOBILE-001 | End-to-End |
| **FR-MAPI-041** | Sync all pending records within 60 s of reconnection | Data integrity on reconnect | NFR-MAPI-002, NFR-MOBILE-001 | End-to-End |
| **FR-MAPI-042** | Delta sync via `last_sync_at` timestamp protocol | Bandwidth efficiency | Platform capability | Integration |
| **FR-MAPI-043** | Conflict detection without silent overwrite | Data integrity | Domain: Agriculture | Integration |
| **FR-MAPI-044** | Sync status endpoint | Operational transparency | Platform capability | Integration |
| **FR-MAPI-045** | UUID v4 idempotency key per offline transaction | Prevent duplicate records on retry | Data integrity | Integration |
| **FR-MAPI-046** | `mobile_sync_log` audit trail per synced transaction | Traceability of field data | ISO/IEC 27001 | Integration |
| **FR-MAPI-047** | HTTP 207 partial batch on validation failure | Resilient bulk operations | Platform capability | Integration |
| **FR-MAPI-048** | Maximum batch size of 500 records per sync | Prevent server overload | Operational stability | Unit |
| **FR-MAPI-049** | Offline mode restricted to Cooperative Procurement (v1) | Scope control | Platform capability | Integration |
| **FR-MAPI-050** | Module capabilities endpoint | Offline eligibility discovery | Platform capability | Integration |
| **FR-MAPI-051** | Reference data snapshot endpoint | Offline form population | Domain: Agriculture | Integration |
| **FR-MAPI-052** | `data_version` hash in reference data snapshot | Detect stale reference data | Data integrity | Integration |
| **FR-MAPI-053** | AES-256 encrypted local offline database | Mobile data security | NIST SP 800-63B, OWASP M9 | Security |
| **FR-MAPI-054** | Visual sync status indicator (≤ 2 s update) | User awareness | NFR-USAB-001 | End-to-End / UX |
| **FR-MAPI-055** | Reject sync on expired/revoked JWT during offline period | Enforce authentication lifecycle | RFC 7519, OWASP API2 | Integration |
| **FR-MAPI-060** | Push notifications for 5 event types | Timely operational alerts | Platform capability | End-to-End |
| **FR-MAPI-061** | Standard 6-field notification payload | Consistent notification contract | Platform capability | Unit |
| **FR-MAPI-062** | No sensitive data in push notification payload | Privacy compliance | Uganda DPPA 2019 | Security |
| **FR-MAPI-063** | Device token registration via `POST /api/mobile/v1/devices` | Push notification enablement | Platform capability | Integration |
| **FR-MAPI-064** | Deregister device tokens on account disable or explicit delete | Prevent ghost notifications | Platform capability | Integration |
| **FR-MAPI-065** | APNs/FCM token refresh upsert | Prevent stale token failures | Platform capability | Integration |
| **FR-MAPI-066** | 3-attempt exponential backoff on push delivery failure | Delivery resilience | Platform capability | Integration |
| **FR-MAPI-067** | SMS fallback via Africa's Talking after 3 push failures | Resilience in low-connectivity markets | Domain: Agriculture / East Africa | End-to-End |
| **FR-MAPI-068** | `notification_log` audit trail | Security and delivery observability | ISO/IEC 27001 | Integration |
| **FR-MAPI-069** | Per-event-type notification preferences | User control | NFR-USAB-001 | Integration |
| **FR-MAPI-070** | Quiet hours notification deferral | User experience | NFR-USAB-001 | Integration |
| **FR-MAPI-080** | Token bucket rate limiting per tenant and user | API abuse prevention | OWASP API4 | Load / Integration |
| **FR-MAPI-081** | HTTP 429 with `Retry-After` header on limit exceeded | Client retry guidance | OWASP API4, RFC 6585 | Integration |
| **FR-MAPI-082** | Rate limit rule precedence (most specific wins) | Predictable enforcement | Platform capability | Unit |
| **FR-MAPI-083** | `X-RateLimit-*` headers on all responses | Client observability | OWASP API4 | Integration |
| **FR-MAPI-084** | Default 120 req/60 s platform-wide limit | Baseline abuse protection | OWASP API4 | Integration |
| **FR-MAPI-085** | Rate limit rule updates via Super Admin API, effective ≤ 30 s | Operational control | Platform capability | Integration |
| **FR-MAPI-090** | Data-lite mode (≥ 40% payload reduction via `X-Data-Lite: true`) | Bandwidth cost reduction for African markets | Platform capability | Integration |
| **FR-MAPI-091** | Essential fields retained in data-lite mode | Functional correctness | Platform capability | Integration |
| **FR-MAPI-092** | `X-Data-Lite: applied` confirmation header | Client mode acknowledgement | Platform capability | Unit |
| **FR-MAPI-093** | Data-lite applied at serialisation layer; audit log unaffected | Audit log completeness | NFR-SEC-002, ISO/IEC 27001 | Integration |

### 10.2 Non-Functional Requirements Traceability

| NFR ID | Description | Threshold | Source / Standard | Test Classification |
|---|---|---|---|---|
| **NFR-MAPI-001** | Mobile API P95 response time | ≤ 500 ms at 50 concurrent clients/tenant | NFR-PERF-003, domain.md | Load testing |
| **NFR-MAPI-002** | Offline resilience: intake duration and sync latency | ≥ 72 h offline; sync ≤ 60 s on reconnect | NFR-MOBILE-001, domain.md | End-to-End |
| **NFR-MAPI-003** | Concurrent mobile session capacity per tenant | ≥ 200 sessions; P95 ≤ 500 ms | Platform scalability | Load testing |
| **NFR-MAPI-004** | JWT validation latency | P99 ≤ 10 ms | RFC 7519, performance baseline | Unit / Load |
| **NFR-MAPI-005** | TLS version enforcement | TLS 1.3+ only; TLS < 1.3 rejected | NIST SP 800-63B, ISO/IEC 27001 | Security |
| **NFR-MAPI-006** | Audit log coverage for state-changing requests | 100% coverage; entry within 1 s | NFR-SEC-002, ISO/IEC 27001 | Integration |

### 10.3 Gap Register

No `[TRACE-GAP]`, `[CONTEXT-GAP]`, or `[V&V-FAIL]` flags were raised during generation of this document. All requirements are grounded in `_context/tech-stack.md`, `_context/domain.md`, and the project engineering standards.

*This section must be reviewed and confirmed by the lead developer before this SRS is baselined.*
