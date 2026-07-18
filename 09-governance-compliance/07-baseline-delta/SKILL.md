---
name: 07-baseline-delta
description: Use when recording the exact approved differences between controlled baselines, including affected artefacts, rationale, evidence, migration, and rollback. Use change-impact-analysis before approval and release-notes for customer-facing changes.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Baseline Delta Skill

<!-- dual-compat-start -->

## Use When

- Use when recording the exact approved differences between controlled baselines, including affected artefacts, rationale, evidence, migration, and rollback. Use change-impact-analysis before approval and release-notes for customer-facing changes.

## Do Not Use When

- Do not use on unstable drafts where identifiers are still being minted rapidly.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Previous and proposed baseline identifiers and hashes; approved change request; impact analysis; affected artefacts; migration and rollback evidence | Configuration manager and change authority | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Execute only non-mutating validation when authorised; editing remediation, publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Required evidence is missing or inaccessible | Mark the check not assessed, state impact, and stop any pass decision | False assurance from an incomplete review |
| Evidence supports the stated criterion | Record the finding and traceable rationale without mutating sources | Unrepeatable review conclusions |

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
| Baseline Delta | Accountable reviewer, control owner, auditor, or release authority | The delta is reproducible at artefact level, traces to approval, identifies downstream actions, and preserves both baseline identifiers. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Baseline Delta evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every baselined ID has a SHA-256 of its defining line; the snapshot file is committed to the project workspace.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Baseline Delta from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if required evidence is missing or inaccessible, mark the check not assessed, state impact, and stop any pass decision. Record the evidence and result in the validation record; this avoids false assurance from an incomplete review.

## References

- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

A **baseline** is a frozen set of identifier IDs plus content hashes. The skill produces snapshots and diffs so Change Impact Analysis entries have a concrete reference point.

## CLI

- `python -m engine baseline snapshot <project> --label vX.Y` writes `projects/<ProjectName>/09-governance-compliance/07-baseline-delta/vX.Y.yaml`.
- `python -m engine baseline diff <project> vX.Y vX.Z` prints added, removed, and modified identifiers between the two labels.

## When to Snapshot

- Phase 02 baseline sign-off.
- Every major release.
- Before a large refactor that will churn many IDs.

## Reconciliation with Change Impact

When `_registry/baselines.yaml` declares `current: vX.Y`, `BaselineDeltaCheck` verifies that the `vX.Y.yaml` snapshot file actually exists in the project workspace. Any difference between snapshots for IDs listed in a CIA entry is the evidence the CIA is complete.

## Snapshot Format

```yaml
label: v1.0
created_on: 2026-04-16
entries:
  - id: FR-0101
    sha256: a1b2c3...
  - id: NFR-0203
    sha256: d4e5f6...
```
