---
name: 08-waiver-management
description: Use when documenting, approving, monitoring, expiring, or closing a time-bound exception to a requirement or control. Use risk-assessment to evaluate exposure and sign-off-ledger to record the accountable decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Waiver Management Skill

<!-- dual-compat-start -->

## Use When

- Use when documenting, approving, monitoring, expiring, or closing a time-bound exception to a requirement or control. Use risk-assessment to evaluate exposure and sign-off-ledger to record the accountable decision.

## Do Not Use When

- Do not use to bypass systemic failures — waivers are for discrete, time-bounded exceptions.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Requirement or control identifier; non-compliance evidence; rationale; risk assessment; compensating control; owner; approver; start and expiry dates | Control owner, risk owner, and authorised exception authority | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Owner, compensating control, expiry, or residual risk is missing | Reject or return the waiver for completion | Permanent undocumented exception |
| Expiry arrives without renewal evidence | Close the waiver or escalate the breach | Silent control erosion |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Waiver Management | Accountable reviewer, control owner, auditor, or release authority | Every waiver is bounded, owned, approved, monitored, time-limited, and closed or renewed through fresh evidence before expiry. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Waiver Management evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every waiver has an approver, an approved_on date, an expires_on within 90 days, and a unique `WAIVE-NNN` id.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Waiver Management from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if owner, compensating control, expiry, or residual risk is missing, reject or return the waiver for completion. Record the evidence and result in the validation record; this avoids permanent undocumented exception.

## References

- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

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
