# ADR-0005 Mandatory PII scrubbing before every AI prompt

- Status: accepted
- Date: 2026-04-17

## Context

The AI Module (FR-AI-001 through FR-AI-007) invokes a third-party LLM provider hosted outside Uganda. DPPA §20 and Regulation 20 restrict cross-border transfer of personal data; Uganda NIN/LIN and parent phone numbers are S-tier. Sending raw student data to an international LLM would be a regulatory breach.

## Decision

Before any prompt is constructed, the payload passes through `PIIScrubber::scrub()`. The scrubber:

1. Replaces Ugandan NIN patterns (`CF\d{12}[A-Z]{2}`) with `[NIN_REDACTED]`.
2. Replaces Ugandan mobile patterns with `[PHONE_REDACTED]`.
3. Replaces first-name + last-name combinations from the active tenant's roster with per-request pseudonyms (`STUDENT_A`, `GUARDIAN_B`).
4. Rounds financial amounts to the nearest UGX 1,000 and tags the currency to prevent fingerprinting.

The scrubber writes to `ai_audit_log` with `pii_scrubbed=1`. Any call that bypasses the scrubber (detectable via `pii_scrubbed=0` on the row) raises a Sev-1 alert to the on-call and the PDPO liaison.

## Consequences

- Positive: DPPA §20 and Regulation 20 compliance; AI features remain available under cross-border transfer constraints.
- Negative: aggressive redaction can degrade AI answer quality. Mitigation: pseudonym pairing is stable within a single conversation turn so the model can reason about "STUDENT_A scored 80".
- Must-have: `PIIScrubber` is a shared-security component; any code path that talks to the LLM routes through it. Enforced by an architecture fitness test in CI.

## Affects

- FR-AI-001 through FR-AI-007.
- CTRL-UG-005.
- `03-design-documentation/01-hld/02-security-architecture.md §AI PII Scrubbing`.
