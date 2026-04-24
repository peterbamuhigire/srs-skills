# Threat Model

STRIDE analysis for the Livelink Health platform.

- Spoofing: mitigated by TOTP MFA for all provider logins (FR-007).
- Detection and notification: breach alerting path satisfies FR-009 through the incident webhook workflow.
- Tampering: mitigated by immutable audit log (FR-013) and WAF.
- Repudiation: mitigated by signed audit entries per CTRL-UG-004.
- Information disclosure: mitigated by AES-256-GCM encryption at rest per CTRL-UG-002 and TLS 1.3 in transit.
- Denial of service: mitigated by rate limiting and NFR-003, NFR-007 capacity planning.
- Elevation of privilege: mitigated by RBAC (FR-014) and CTRL-UG-004 access reviews.

Performance-sensitive paths observe NFR-001 and NFR-002. Storage is sized per NFR-004.
Memory budget follows NFR-005. Error-rate objective NFR-006 and backup RPO NFR-008
are in scope for design.
