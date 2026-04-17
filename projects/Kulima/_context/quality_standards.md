# Quality Standards

## Performance
- API response time: P95 < 500ms under 1,000 concurrent users for CRUD operations
- API response time: P95 < 2,000ms for report generation and dashboard aggregation queries
- Mobile app cold start: < 3 seconds on a Tecno Spark (2GB RAM, Android 11)
- Mobile app screen transitions: < 300ms
- Offline operation: zero degradation in core functionality (record, read, edit, delete) with no internet
- Background sync: queued records sync within 30 seconds of connectivity detection
- GPS boundary capture: polygon accuracy within 5 metres of actual boundary

## Availability
- Web dashboard uptime: 99.5% monthly (allows ~3.6 hours downtime/month)
- API uptime: 99.5% monthly
- Planned maintenance windows: Sundays 02:00-04:00 EAT with 48-hour advance notice
- IoT Gateway uptime: 99.0% (allows for sensor data buffering and retry)
- Camera proxy uptime: 99.0% (live streams are best-effort; cached snapshots shown on failure)

## Security
- OWASP Top 10 compliance for all web and API endpoints
- All data encrypted in transit (TLS 1.2+)
- Sensitive data encrypted at rest (farm GPS boundaries, financial records, IoT credentials)
- Mobile local database encrypted (SQLCipher / Core Data encryption)
- Session timeout: 30 minutes of inactivity (configurable per tenant)
- Password policy: minimum 8 characters, complexity enforced
- JWT token expiry: 24 hours with refresh token mechanism
- Rate limiting: 100 requests/minute per authenticated user; 20 requests/minute for unauthenticated endpoints

## Data Integrity
- No data loss: all offline records must eventually sync successfully or be flagged for manual resolution
- Conflict resolution: every conflict logged with both versions preserved for farmer review
- Audit trail: all create, update, and delete operations logged with user, timestamp, and previous value
- Financial transaction immutability: income and expense records cannot be deleted after 30 days — only voided with a reversal entry
- Backup frequency: daily automated database backup with 30-day retention
- Point-in-time recovery: capable of restoring to any point within the past 7 days

## Usability
- Core farm operations (record activity, log income/expense, mark task complete) achievable in 3 taps or fewer
- Touch targets: minimum 48x48dp on mobile (WCAG 2.1 AA)
- Font size: minimum 14sp on mobile for body text
- Contrast ratio: minimum 4.5:1 for text (WCAG AA)
- Language switching: instant, no app restart required
- Onboarding: new farmer can register and record their first activity within 5 minutes without external help
- Error messages: clear, actionable, in the user's selected language — never display technical error codes to farmers

## Scalability
- Database: supports 10,000 tenants with average 500 records each without query degradation
- File storage: photo compression to max 512KB before upload
- Mobile app APK size: base APK < 30MB (excluding add-on modules)
- Sync payload: individual sync batch < 1MB to accommodate 2G connections

## Accessibility
- Screen reader compatibility for web dashboard (ARIA labels)
- High contrast mode available
- Large text mode on mobile (system font scaling respected)
- No colour-only information — all status indicators include text labels or icons alongside colour
