# CIA-001 Add MFA (TOTP) to provider login

- Status: approved
- Raised on: 2026-04-10
- Decision body: Livelink Steering Committee
- Decision date: 2026-04-12

## Context

A security review of CTRL-UG-004 flagged that provider login relied on
password-only authentication. The steering committee approved adding TOTP
MFA, creating FR-007 and adjusting the session design.

## Affected baseline IDs

- FR-007 (new)
- NFR-002 (availability budget for the MFA service)

## Downstream artifacts

- 03-design-documentation/threat-model.md
- 05-testing-documentation/test-plan/tc.md (TC-007)

## Rollback plan

If MFA causes login failures above 2%, disable the TOTP requirement via
feature flag `auth.require_totp=false` and page the on-call. Session tokens
minted before the flag flip remain valid. Restore within 15 minutes.
