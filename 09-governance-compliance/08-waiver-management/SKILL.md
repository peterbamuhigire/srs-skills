---
name: "Waiver Management"
description: "Capture a gate-specific waiver with approver, justification, and an expiry no more than 90 days from approval."
metadata:
  use_when: "Use when a specific kernel finding must be deferred because immediate remediation is not feasible."
  do_not_use_when: "Do not use to bypass systemic failures — waivers are for discrete, time-bounded exceptions."
  required_inputs: "Target gate check ID, scope (path glob or `*`), reason, approver, expiry days (max 90)."
  workflow: "Invoke `python -m engine waive <project> --gate <gate_id> --reason '...' --approver '...' --days N`."
  quality_standards: "Every waiver has an approver, an approved_on date, an expires_on within 90 days, and a unique `WAIVE-NNN` id."
  anti_patterns: "Do not stack overlapping waivers; do not extend a waiver by editing its expiry in place — create a new waiver instead."
  outputs: "Appended entry in `projects/<ProjectName>/_registry/waivers.yaml`."
  references: "`engine/waivers.py`."
---

# Waiver Management Skill

## Overview

A waiver defers a specific finding for a bounded time window. The Phase 09 gate check `phase09.waivers_have_expiry` rejects any waiver whose window exceeds 90 days.

## Stimulus / Process / Response

1. **Stimulus:** a finding the team cannot immediately remediate.
2. **Process:**
   1. Confirm severity with the owning role.
   2. Capture justification in one paragraph.
   3. Identify the approver (role-based).
   4. Set expiry window up to 90 days.
   5. Run the CLI to append the entry.
3. **Response:** a `WAIVE-NNN` entry plus a notification line for the next stand-up.

## CLI

```bash
python -m engine waive <project> \
    --gate phase02.smart_nfr \
    --scope "02-requirements-engineering/*" \
    --reason "NFR thresholds pending customer meeting." \
    --approver "Tech Lead" \
    --days 30
```

## Waiver Format

```yaml
waivers:
  - id: WAIVE-001
    gate: phase02.smart_nfr
    scope: "*"
    reason: "NFR thresholds pending."
    approver: "Tech Lead"
    approved_on: 2026-04-16
    expires_on: 2026-05-16
```
