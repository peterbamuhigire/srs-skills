# CIA-001 — Add DPIA for the AI Module before Phase-2 go-live

- Status: open
- Opened: 2026-04-17
- Owner: Peter Bamuhigire

## Impact

- FR-AI-001 through FR-AI-007 cannot go live in any tenant without a completed DPIA (Uganda DPPA Regulation 12).
- Linked waiver: W-001 (expires 2026-07-17).

## Plan

1. Invoke the `dpia-generator` skill against the AI module.
2. Review with legal liaison.
3. Sign off by CTO and file in `09-governance-compliance/03-compliance/02-dpia-ai-module.md`.
4. Close waiver W-001.

## Rollback

If the DPIA cannot be completed within the W-001 window, the AI module remains feature-flagged OFF in production; there is no functional regression.
