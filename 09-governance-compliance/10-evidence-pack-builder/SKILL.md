---
name: 10-evidence-pack-builder
description: Use when assembling indexed, traceable, integrity-checked evidence for a review, audit, release, or acceptance decision. Use traceability-matrix to expose coverage and audit-report to assess the assembled evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Evidence Pack Builder Skill

<!-- dual-compat-start -->

## Use When

- Use when assembling indexed, traceable, integrity-checked evidence for a review, audit, release, or acceptance decision. Use traceability-matrix to expose coverage and audit-report to assess the assembled evidence.

## Do Not Use When

- Do not use for daily internal reviews — use `engine validate` instead.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Review or audit scope and period; control or requirement map; source evidence; provenance and integrity data; redaction rules; recipient access constraints | Control owners, evidence custodians, and review authority | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Provenance, integrity, period, or control mapping is absent | Quarantine the item and record the gap | Misleading or tampered evidence |
| Evidence meets scope, integrity, and traceability checks | Index it for the named consumer | Unreviewable evidence dumps |

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
| Evidence Pack Builder | Accountable reviewer, control owner, auditor, or release authority | Every indexed item is in scope, traceable, integrity-checked, minimally redacted, and mapped to an acceptance decision. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Evidence Pack Builder evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every file is hashed; the manifest includes path, SHA-256, size, and modified timestamp.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Evidence Pack Builder from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if provenance, integrity, period, or control mapping is absent, quarantine the item and record the gap. Record the evidence and result in the validation record; this avoids misleading or tampered evidence.

## References

- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

The evidence pack is a single ZIP that an external auditor can consume without repo access. It contains:

- `_context/` — project vision, quality standards, domain, glossary.
- `_registry/` — identifiers, glossary, controls, ADR catalog, change-impact, baselines, sign-off ledger, waivers.
- `09-governance-compliance/` — traceability, audit reports, risk assessment, compliance documentation, ADRs, CIA entries, baseline snapshots.
- `manifest.csv` — per-file path, SHA-256, size, and last-modified timestamp.

## CLI

```bash
python -m engine pack <project> --out <project>/evidence-pack-YYYY-MM-DD.zip
```

## Phase 09 Reconciliation

`phase09.evidence_pack_buildable` runs the builder against a temp file during every Phase 09 gate evaluation; if the builder cannot produce a non-empty pack, the gate fails.
