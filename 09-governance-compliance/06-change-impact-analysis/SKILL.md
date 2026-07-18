---
name: 06-change-impact-analysis
description: Use when assessing a proposed change against baselines, requirements, architecture, security, privacy, tests, operations, schedule, and cost before authorisation. Use baseline-delta to record the approved delta and CCB-charter for governance.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Change Impact Analysis Skill

<!-- dual-compat-start -->

## Use When

- Use when assessing a proposed change against baselines, requirements, architecture, security, privacy, tests, operations, schedule, and cost before authorisation. Use baseline-delta to record the approved delta and CCB-charter for governance.

## Do Not Use When

- Do not use for changes to unbaselined drafts or for internal refactors that do not alter a baselined contract.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Change request; current approved baselines; dependency and traceability maps; security/privacy controls; test and deployment evidence; cost and schedule constraints | Change requester and affected technical, product, QA, operations, security, privacy, and finance owners | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
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
| Change Impact Analysis | Accountable reviewer, control owner, auditor, or release authority | Every affected baseline and control has an impact, evidence, owner, test, migration, rollback, and recommendation; missing evidence blocks approval. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Change Impact Analysis evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every CIA entry names at least one affected baseline ID, lists downstream artifacts, and provides a non-empty rollback plan.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Change Impact Analysis from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

A Change Impact Analysis (CIA) is mandatory for any change to a baselined `FR-`, `NFR-`, or selected `CTRL-`. The CIA captures impact, effort, rollback, and the change-control decision.

## Stimulus / Process / Response

1. **Stimulus:** a baseline change request is raised.
2. **Process:**
   1. Identify the affected baseline identifiers.
   2. List every downstream artifact referencing them (designs, tests, runbooks, training).
   3. Assess effort and risk; identify the rollback strategy.
   4. Route to the Change Control Board.
   5. Record the decision and append to `_registry/change-impact.yaml`.
3. **Response:** one CIA file plus one catalog entry, reconciled by `ChangeImpactCheck`.

## Output Contract

- File: `projects/<ProjectName>/09-governance-compliance/06-change-impact/CIA-NNN-<slug>.md`.
- Registry: `projects/<ProjectName>/_registry/change-impact.yaml`.

## Catalog Format

```yaml
entries:
  - id: CIA-001
    raised_on: 2026-04-16
    affected_baseline_ids: ["FR-0101", "NFR-0203"]
    downstream_artifacts:
      - "03-design-documentation/hld.md"
      - "05-testing-documentation/tc.md"
    decision: approved
    decision_body: "Change Control Board"
    decision_date: 2026-04-20
    rollback_plan: "Revert FR-0101 to prior baseline hash; redeploy vX.Y."
```
