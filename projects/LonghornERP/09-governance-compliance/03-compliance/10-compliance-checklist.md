# Pre-Launch Compliance Checklist

## 10.1 Purpose

This checklist defines the mandatory compliance gates that shall be completed and signed off before Longhorn ERP is deployed to production and made available to paying tenants. Each item references the section of this document or the relevant gap that governs it. No item may be bypassed without explicit written approval from the Lead Developer.

## 10.2 Mandatory Pre-Launch Items

1. Independent multi-tenancy security review completed and signed off. The review shall cover all controls specified in Section 4 and shall be documented in `09-governance-compliance/02-audit-report/`. Resolves **GAP-004**.

2. Uganda Data Protection and Privacy Act 2019 legal review completed and all provisional requirements in Section 6 updated with confirmed obligations. Resolves **GAP-007**.

3. NITA-U SaaS cloud provider obligations reviewed, Section 9 updated with confirmed obligations, and Tenant Service Agreement updated with required data processing terms. Resolves **GAP-014**.

4. All 10 OWASP Top 10 (2021) items addressed as specified in Section 8. Each item verified by penetration test or static analysis as noted in the corresponding measurable requirement. Test results documented in `09-governance-compliance/02-audit-report/`.

5. Audit log immutability verified by penetration test. The test shall confirm that UPDATE and DELETE operations on the `audit_log` table are rejected at the database privilege level for both the application database user and any simulated administrative user. Test result documented in `09-governance-compliance/02-audit-report/`.

6. TLS 1.3 configured and verified on the production server. Configuration shall be confirmed using an independent TLS scanner (e.g., Qualys SSL Labs). The scan report shall achieve grade A or higher. TLS 1.1 and SSL 3.0 disabled, confirmed by scan output.

7. All sensitive fields listed in Section 6.3 encrypted at rest with AES-256. Encryption verified by inspecting raw database values for at least one record per field category and confirming the stored value is not plaintext.

8. Session security hardening checklist completed. The checklist shall cover: `LONGHORN_ERP_SESSION` cookie attributes (`HttpOnly`, `Secure`, `SameSite=Strict`), CSRF token validation, session invalidation on account deactivation (NFR-SEC-003 ≤ 5 seconds), and session timeout configuration.

9. Rate limiting tested at production-scale load. The test shall confirm that token bucket limits engage correctly for a single `user_id` at the configured threshold and that HTTP 429 is returned with a valid `Retry-After` header. Test conducted using a load testing tool with at least 100 concurrent simulated users per tenant.

10. Security audit report documented and stored in `09-governance-compliance/02-audit-report/`. The report shall include findings from items 1 through 9 above, list any residual risks with a documented acceptance decision, and be signed off by the Lead Developer before production launch.

## 10.3 Ongoing Compliance Items

The following items do not block launch but shall be addressed within the timelines stated.

- Composer dependency security audit (`composer audit`) run on a monthly schedule. High or critical advisories for direct dependencies resolved within 7 days of disclosure.
- Frontend JavaScript library versions reviewed quarterly. High-severity CVEs patched within 14 days.
- Data retention policy review conducted annually or whenever a material change to PDPA or NITA-U guidance is published.
- OWASP Top 10 re-assessment conducted annually and whenever a major new module is added.
- ISO/IEC 27001:2022 certification assessment initiated within 12 months of production launch.
