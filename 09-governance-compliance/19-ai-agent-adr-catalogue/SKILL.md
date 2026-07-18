---
name: 19-ai-agent-adr-catalogue
description: Use when recording agent-specific decisions about autonomy levels, planners, tools, approvals, memory, supervision, reversibility, and audit logs. Use ai-adr-catalogue for non-agent AI decisions and architecture-decision-records for general architecture.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Agent ADR Catalogue Skill

<!-- dual-compat-start -->

## Use When

- Use when recording agent-specific decisions about autonomy levels, planners, tools, approvals, memory, supervision, reversibility, and audit logs. Use ai-adr-catalogue for non-agent AI decisions and architecture-decision-records for general architecture.

## Do Not Use When

- Do not use for projects without agent features.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_Architecture_Spec.md, AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_SLO_Doc.md, AI_Agent_Responsible_AI_Addendum.md. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| AI Agent ADR Catalogue | Accountable reviewer, control owner, auditor, or release authority | Every required agent ADR slot shall be filled or explicitly waived with an ADR-style waiver. Every decision shall cite its alternatives and the evidence that drove the choice. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent ADR Catalogue evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every required agent ADR slot shall be filled or explicitly waived with an ADR-style waiver. Every decision shall cite its alternatives and the evidence that drove the choice.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent ADR Catalogue from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

Every agent-feature SaaS shall have ADRs for the following decisions. Missing ADRs are blockers for any L1+ rollout.

1. **Autonomy Level per Feature** — L0..L4 placement with drivers and rejected alternatives.
2. **Irreversibility-gating Policy** — the rule for when human approval is required for irreversible tool calls; per-feature deviations.
3. **Planner Choice per Feature** — ReAct / Plan-and-execute / Tree-of-thought / Function-calling-loop / custom.
4. **Memory Store Technology and Tiering** — scratchpad, episodic, long-term: storage choice, isolation keys, retention.
5. **Tool-call Audit-log Retention by Event Class** — hot / cold per event class.
6. **Multi-agent Topology per Feature** — single-agent / supervisor-worker / debate / handoff chain.
7. **Supervision Policy** — review-before-act / review-after-act / sample-review.
8. **Kill-switch Propagation SLA** — default 5 s; per-feature exception only with ADR.
9. **Action Catalogue Change-control Protocol** — PR + ADR + red-team smoke + sign-off rules.
10. **Replay Environment Source-of-truth** — where the deterministic replay env lives; update protocol.
11. **Agent-task Quarantine Policy** — when to quarantine; tenant notification SLA.
12. **Agent Cost Envelope per Feature** — max-cost per run + per-tenant per-day budget.
13. **Plan-approval UI Authority** — what is shown at the approval moment; what can be hidden; signing of the approval event.
14. **Long-term Memory Opt-in Mechanism** — per-tenant flag; revocation behaviour.

## Workflow

1. Read inputs.
2. For each ADR slot, generate `ADR-AGT-NNNN-<slug>.md` using `references/ai-agent-adr-templates.md`.
3. Index in `AI_Agent_ADR_Catalogue.md`.
4. Link from the central `09-governance-compliance/05-architecture-decision-records` register and from `09-governance-compliance/17-ai-adr-catalogue`.
5. Sign-off per ADR: AI Lead + Architect + (DPO for compliance-touching ADRs; Security for kill-switch and supervision ADRs).

## Compliance-relevant ADR slots (additions)

In addition to the slots above, the following ADRs are required when the SaaS is in scope of SOC 2, ISO 27001, or HIPAA:

15. **SOC 2 Control-Ownership ADR** — names the role accountable for each agent-specific TSC control row; required before SOC 2 Type II window opens.
16. **HIPAA Admin-Only-PHI-Agent ADR** — confirms the admin-only constraint for clinical PHI agents; lists L0/L1 boundaries; required before any BAA execution.
17. **Audit-Log Integrity ADR** — hash-chain or WORM choice; daily integrity-check job; alerting on chain break.
18. **Auditor Portal Access ADR** — time-bound, named-recipient, logged-access policy; portal-access expiry default.
19. **Cross-Regime Evidence Reuse ADR** — declares the one-evidence-many-regimes posture; cross-link to `27-ai-agent-regulator-overlap-mapping`.

Each compliance ADR is signed by AI Lead + CISO + DPO and added to the agent ADR register before any audit window opens.

## Standards

- ADR pattern (Nygard)
- ISO/IEC 42001 Clause 8
- IEEE 1016-2009 §5
- EU AI Act Art. 14 (for the human-final-decision ADRs)
- AICPA TSP 100 (for SOC 2 control-ownership ADR)
- HIPAA §164.308 (for admin-only ADR)
