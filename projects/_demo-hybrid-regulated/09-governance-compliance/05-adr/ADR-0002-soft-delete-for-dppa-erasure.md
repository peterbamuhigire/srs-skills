# ADR-0002 Soft-delete with crypto-shredding for DPPA erasure

- Status: accepted
- Date: 2026-04-14

## Context

Uganda DPPA 2019 §30 grants data subjects a right to erasure. A physical
DELETE cascades through foreign keys and breaks audit chains required by
CTRL-UG-004. At the same time, "soft-delete with a flag" leaves plaintext
PII on disk, which violates CTRL-UG-002.

## Decision

Implement crypto-shredding: each patient record is encrypted with a
per-subject data encryption key (DEK). On erasure, destroy the DEK. The
ciphertext remains on disk as an opaque blob that no-one can decrypt. The
audit log chain is preserved.

## Consequences

- Positive: satisfies FR-011 erasure and retains FR-013 audit continuity.
- Positive: aligns with CTRL-UG-002 and CTRL-UG-004.
- Negative: key management complexity; requires HSM-backed DEK store.

## Affects

- FR-011 (erasure), FR-013 (audit log), CTRL-UG-002, CTRL-UG-004.
