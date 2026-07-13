---
name: 09-sign-off-ledger
description: Use when maintaining an immutable, attributable record of review, approval, rejection, conditions, scope, and date. Use formal-review-gates to define gate criteria and waiver-management for exceptions.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Sign-Off Ledger Skill

<!-- dual-compat-start -->

## Use When

- Use when maintaining an immutable, attributable record of review, approval, rejection, conditions, scope, and date. Use formal-review-gates to define gate criteria and waiver-management for exceptions.

## Do Not Use When

- Do not use for informal stand-up approvals or for internal checkpoint reviews.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Artefact identifier and version; review evidence; open conditions; decision authority and identity; decision date; signature or approval mechanism | Document controller and authorised reviewers or approvers | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Identity, scope, decision, or timestamp is absent | Refuse to record approval | Unauditable consent |
| A condition remains open | Record conditional status, not approved | False finality |

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
| Sign-Off Ledger | Accountable reviewer, control owner, auditor, or release authority | Every entry is attributable, immutable, version-specific, condition-aware, and linked to the reviewed evidence. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Sign-Off Ledger evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every sign-off names a gate, a signer, a role, a date, and at least one artifact file that exists in the workspace.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Sign-Off Ledger from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if identity, scope, decision, or timestamp is absent, refuse to record approval. Record the evidence and result in the validation record; this avoids unauditable consent.

## References

- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

The sign-off ledger is the append-only record of every formal phase-gate approval. `SignOffCheck` reconciles each listed artifact against the filesystem.

## CLI

```bash
python -m engine signoff <project> \
    --gate phase02 \
    --signer "Dr. Jane Doe" \
    --role "Chief Architect" \
    --artifact 02-requirements-engineering/srs.md \
    --artifact _registry/identifiers.yaml \
    --comment "Baseline v1.0 approved."
```

## Events Requiring Sign-Off

- Phase 02 — baseline approval.
- Phase 06 — go-live readiness.
- Phase 09 — audit clearance.

## Ledger Format

```yaml
sign_offs:
  - gate: phase02
    signer: "Dr. Jane Doe"
    role: "Chief Architect"
    signed_on: 2026-04-16
    artifact_set:
      - "02-requirements-engineering/srs.md"
      - "_registry/identifiers.yaml"
    comment: "Baseline v1.0 approved."
```
