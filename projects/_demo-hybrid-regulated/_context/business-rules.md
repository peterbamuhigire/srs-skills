# Business Rules

- BR-001: When a patient submits a DSAR and the system has their NIN on file, the system shall return their record bundle within 30 days.
- BR-002: When a breach of S-tier data is detected, the system shall notify the PDPO via the configured webhook immediately.
- BR-003: When a clinician saves a clinical note, the system shall stamp an immutable audit log entry.
- BR-004: When a patient revokes consent, the system shall mark their record for erasure within 7 days.
- BR-005: When a billing clerk issues an invoice, the system shall submit it to EFRIS within 5 minutes.
- BR-006: When a receptionist enrols a new patient, the system shall capture explicit DPPA consent before storing PII.
- BR-007: When login attempts exceed 5 in a minute, the system shall lock the account for 15 minutes.
- BR-008: When a provider role is revoked, the system shall invalidate their active sessions within 60 seconds.
