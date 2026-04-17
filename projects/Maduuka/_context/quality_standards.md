# Quality Standards -- Maduuka

## Functional Quality (IEEE 830 Criteria)

- **Correct:** Every requirement mirrors stakeholder intent documented in _context/vision.md.
- **Unambiguous:** Every requirement has exactly one interpretation. No vague adjectives ("fast", "reliable", "intuitive") without a measurable metric.
- **Complete:** Every business rule in _context/business_rules.md has a corresponding FR. Every gap in _context/gap-analysis.md has a flagged note.
- **Verifiable:** Every requirement has a deterministic test case with a pass/fail criterion.

## Performance Thresholds (Per Uganda Market Context)

| Metric | Threshold | Context |
|---|---|---|
| POS sale completion | <= 3 seconds end-to-end on a UGX 250,000 Android phone on 3G | Minimum viable for a busy cashier |
| Barcode scan to cart add | <= 1 second | Per spec section 4.1 |
| Dashboard load time | <= 4 seconds on 3G (P95) | Business owner's morning check |
| API response time | <= 500 ms at P95 under normal load | Standard REST API threshold |
| Offline sale queue sync | All pending transactions synced within 30 seconds of connectivity restoration | Per spec section 6.1 |
| Background sync interval | Every 15 minutes when app is in background | Per spec section 6.1 |
| Receipt print (Bluetooth) | <= 5 seconds from sale completion to first line printing | Cashier experience |

## Availability

| Scope | Target |
|---|---|
| Core API (POS, Inventory) | 99.9% uptime (<= 8.76 hours downtime/year) |
| Dashboard and Reports | 99.5% uptime |
| Offline fallback | 100% -- no POS functionality loss due to connectivity |

## Security Baselines

- All stored passwords: bcrypt (cost factor >= 12)
- All data in transit: TLS 1.3
- Mobile local storage: AES-256
- Audit log retention: minimum 7 years (Uganda tax records requirement)
- RBAC: permissions enforced at API layer, not UI layer only

## Document Quality Gates

- No [V&V-FAIL], [CONTEXT-GAP], or [GLOSSARY-GAP] tags may remain unresolved in a document before it is built to .docx.
- Every non-functional requirement must have a measurable threshold (no [SMART-FAIL] tags).
- Every functional requirement must trace to a business goal (_context/vision.md goals 1-5).
