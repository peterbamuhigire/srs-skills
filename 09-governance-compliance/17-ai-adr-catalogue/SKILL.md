---
name: 17-ai-adr-catalogue
description: Use when maintaining a catalogue of consequential AI architecture, model, data, evaluation, safety, and provider decisions. Use architecture-decision-records for general ADRs and ai-agent-adr-catalogue for autonomous-agent decisions.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI ADR Catalogue Skill

<!-- dual-compat-start -->

## Use When

- Use when maintaining a catalogue of consequential AI architecture, model, data, evaluation, safety, and provider decisions. Use architecture-decision-records for general ADRs and ai-agent-adr-catalogue for autonomous-agent decisions.

## Do Not Use When

- Do not use for projects without AI features or for one-off research prototypes.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Architecture_Spec.md, AI_Feature_PRD_Spec.md, AI_Model_Card.md, AI_Eval_Harness_Spec.md, AI_Red_Team_Test_Plan.md. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A required source, owner, obligation, or acceptance condition is missing | Stop the affected claim and record the gap | Unsupported governance artefact |
| Evidence satisfies the declared acceptance condition | Record the decision and hand off to the named consumer | Ambiguous approval or release |

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
| AI ADR Catalogue | Accountable reviewer, control owner, auditor, or release authority | Every required ADR slot shall be filled or explicitly waived with an ADR-style waiver. Every decision shall cite its alternatives and the evidence that drove the choice. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI ADR Catalogue evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every required ADR slot shall be filled or explicitly waived with an ADR-style waiver. Every decision shall cite its alternatives and the evidence that drove the choice.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI ADR Catalogue from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a required source, owner, obligation, or acceptance condition is missing, stop the affected claim and record the gap. Record the evidence and result in the validation record; this avoids unsupported governance artefact.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Required ADR slots

Every AI-feature SaaS shall have ADRs for the following decisions. Missing ADRs are blockers for GA.

1. **Model Gateway as Sole Egress** — yes/no, providers in scope, fallback policy.
2. **Primary Model per Feature** — vendor + model + version pin.
3. **Fallback Model per Feature** — vendor + conditions.
4. **RAG vs Fine-tune vs Agent per Feature** — pattern verdict with drivers.
5. **Vector Store Choice** — technology, partitioning model.
6. **Embedding Model Choice** — provider + version + cost profile.
7. **Eval Threshold per Feature** — pass threshold + regression tolerance.
8. **Abstain Policy per Feature** — threshold + payload.
9. **Content Filter Chain** — filters + order + on-trip behaviour.
10. **Prompt Registry Change Protocol** — PR / eval / sign-off / deploy.
11. **Conversation Log Retention** — hot/cold + per-tenant partition.
12. **Training-Data Exclusion Policy** — global rule + per-provider evidence.
13. **Cross-Tenant Retrieval Prohibition** — gateway enforcement mechanism.
14. **Judge-LLM Selection** — model + calibration.
15. **Cost Ceiling and Throttle Policy** — per-feature / per-tenant.
16. **Rollback Trigger Set** — auto vs manual triggers.
17. **Retraining / Re-evaluation Trigger** — model bump policy.

## Workflow

1. Read inputs.
2. For each ADR slot, generate `ADR-AI-NNNN-<slug>.md` using `references/ai-adr-templates.md`.
3. Index in `AI_ADR_Catalogue.md`.
4. Link from the central `09-governance-compliance/05-architecture-decision-records` register.
5. Sign-off per ADR: AI Lead + Architect + (DPO for compliance-touching ADRs).

## Standards

- ADR pattern (Nygard)
- ISO/IEC 42001 Clause 8 (operation)
- IEEE 1016-2009 §5 (Design viewpoints)
