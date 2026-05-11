# SaaS Trust Center — Public Document Pack Template

## 1. Security Overview (public page)

- Encryption at rest: AES-256, per-tenant KMS keys for Enterprise tier.
- Encryption in transit: TLS 1.2+ everywhere; HSTS; modern cipher suites.
- Authentication: password + MFA; SAML/OIDC SSO on Enterprise tier; passkeys roadmap.
- Authorization: role-based with scoped tokens; tenant claim on every request.
- Tenant isolation: see linked Isolation Evidence summary.
- Vulnerability management: scanning weekly; critical patches within 24 h.
- Secure SDLC: SAST + DAST + SCA in CI; security review at design stage.
- Pentest cadence: external pentest annually + quarterly internal; reports available under NDA.
- Incident response: 24×7 on-call; customer-comms within 15 min for SEV1.
- Data residency: regions available — list them.

## 2. Compliance Attestations

| Attestation | Status | Period | Auditor | Request |
|-------------|--------|--------|---------|---------|
| SOC 2 Type II | held | 2025-04 → 2026-03 | <firm> | https://trust.example.com/request |
| ISO/IEC 27001 | held | 2024 → 2027 | <firm> | as above |
| ISO/IEC 27017 (cloud) | in progress | | | |
| ISO/IEC 27018 (PII) | in progress | | | |
| PCI-DSS | n/a | | | |
| HIPAA | BAA available | | | |
| GDPR | aligned | | | |
| CSA STAR Level 1 (self-assessed) | held | | | |

## 3. Sub-Processor List

| Sub-processor | Purpose | Region | Data classes | Certifications |
|---------------|---------|--------|--------------|----------------|
| AWS | Infrastructure | multi-region | all | SOC 2, ISO 27001 |
| Stripe | Payments | US/EU | billing PII | PCI-DSS L1 |
| Auth0 | Identity (optional) | multi-region | identity PII | SOC 2 |
| <comms provider> | Email | | metadata | |

Notification commitment: 30 days advance notice on new sub-processor with right of objection.

## 4. DPA & Privacy

- Data Processing Addendum: https://trust.example.com/dpa
- Privacy Policy: https://example.com/privacy
- Cookie Policy: https://example.com/cookies
- Data Residency Options: EU, US, UK, APAC (where applicable).
- Breach notification: within 72 hours of confirmation, to the named DPO and customer admins.

## 5. Vulnerability Disclosure Policy

- Channel: security@example.com (PGP key linked).
- Scope: production domains; safe-harbour for good-faith research.
- Response: acknowledgement within 24 h; triage within 5 BD; resolution by severity.
- Recognition: hall of fame; bounty roadmap.

## 6. Status Page

- Public URL: https://status.example.com
- Subscription: email, RSS, webhook, Slack integration.
- Postmortem commitment: published within 5 BD for SEV1, 10 BD for SEV2.

## 7. Customer Data Handling

| Data class | Retention default | Deletion option | Export option | Residency | Encryption |
|------------|-------------------|-----------------|---------------|-----------|------------|
| Account / billing PII | life of contract + 7 y (tax) | yes on offboarding | JSON via DSAR | per region | AES-256 + per-tenant key Enterprise |
| Operational data | per contract | yes on offboarding | JSON / CSV | per region | AES-256 |
| Telemetry | 13 months raw / 7 y aggregate | anonymise on offboarding | aggregate only | per region | AES-256 |
| Logs | 13 months | yes on offboarding | filtered export | per region | AES-256 |

## 8. Questionnaire Pre-Fills

- CAIQ v4: download link.
- SIG Lite: download link.
- SIG Core: under NDA.
