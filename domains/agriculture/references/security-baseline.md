# Agriculture: Security Baseline

## Encryption Standards

| Data State | Standard | Minimum Key Length |
|---|---|---|
| In Transit | TLS 1.2+ | — |
| At Rest (sensitive fields) | AES-256 | 256-bit |
| Sensitive Fields | Farm GPS boundaries, financial records, IoT device credentials | AES-256 field-level |
| Android Local DB | SQLCipher | 256-bit |
| iOS Local DB | Core Data encryption via Data Protection API | Hardware-backed |
| Backups | AES-256 | 256-bit |

## Authentication Requirements

- Dual authentication: session-based for web UI, JWT for API/mobile clients
- Biometric app lock option (fingerprint or face recognition) on mobile
- Session timeout: 30 minutes of inactivity
- Password policy: minimum 8 characters with complexity requirements
- Account lockout: 5 failed attempts in 15 minutes triggers 30-minute lockout
- Rate limiting: 100 requests per minute per authenticated user

## Access Control Baseline

### Role Definitions

| Role | Scope | Access Level |
|---|---|---|
| Farm Owner | Own tenant | Full access to all farm data, settings, and financial records |
| Farm Manager | Assigned farm(s) within tenant | Operational data, worker management, limited financial access |
| Worker | Assigned tasks within tenant | Task view, activity logging, simplified interface |
| Director | Enterprise/group level | Cross-farm reporting, strategic dashboards, no operational edits |
| Cooperative Admin | Franchise tenant | Member farm aggregated data (with consent), payment distribution |
| Field Agent | Assigned farms across tenants | Data collection, farm visits, read-only farm data |
| Buyer | Read-only portal | Traceability data for purchased commodities only |

### Access Control Principles

- All permissions scoped to tenant; cross-tenant access architecturally impossible
- Tenant ID validated on every API request, not just at login
- Worker role uses a simplified interface with limited navigation
- Field Agent access is time-bound and revocable per assignment
- Principle of least privilege enforced on all roles

## Farm Data Privacy

- GPS farm boundaries shall never be exposed in marketplace or buyer-facing interfaces
- Financial records scoped to explicit grants; cooperative admin sees aggregated financials only unless farmer grants detailed access
- IoT device tokens encrypted per-tenant; never included in API responses
- Mobile money credentials (API keys, secrets) shall never be stored in client applications
- Farmer phone numbers masked in buyer-facing traceability exports (e.g., `+256XXX***789`)

## Mobile Security

- Local database encrypted using SQLCipher (Android) or Core Data encryption (iOS)
- Biometric lock available as optional app-level gate
- Auto-logout after configured inactivity period (default 30 minutes)
- Offline data wipe capability on remote deactivation by tenant admin
- App data excluded from unencrypted device backups
- Certificate pinning for API communication

## API Security

- JWT token expiry: 24 hours with refresh token rotation
- Refresh token expiry: 30 days; single-use with rotation
- Rate limiting: 100 requests/minute authenticated, 20 requests/minute unauthenticated
- No sensitive data (GPS boundaries, financial amounts, phone numbers) in error responses
- Tenant ID validation on every request via middleware
- Request signing for mobile money API callbacks
- API versioning enforced; deprecated endpoints return 410 after sunset period

## Traceability Data Security

- EUDR exports include minimum required data only: plot GPS polygon, commodity, quantity, harvest date
- No personal financial data included in traceability exports
- Buyer portal is read-only with no access to farmer operational data (expenses, worker records, IoT data)
- Traceability data access logged with buyer ID, timestamp, and export scope

## Vulnerability Management

- OWASP Top 10 compliance required for all web and API endpoints
- Critical vulnerability patches: within 72 hours of disclosure
- High severity patches: within 30 days
- Annual penetration testing by independent assessor
- Dependency scanning on every build (Composer, npm, Gradle, SPM)
- Security headers enforced: CSP, HSTS, X-Content-Type-Options, X-Frame-Options
