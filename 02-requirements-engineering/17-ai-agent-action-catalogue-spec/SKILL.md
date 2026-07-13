---
name: 17-ai-agent-action-catalogue-spec
description: "Use when defining the schema-bound tools an AI agent may invoke, including side effects, reversibility, approvals, audit fields, quotas, and kill switches; use agent PRD for user outcomes."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# AI Agent Action Catalogue Spec Skill

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- defining the schema-bound tools an AI agent may invoke, including side effects, reversibility, approvals, audit fields, quotas, and kill switches; use agent PRD for user outcomes.
- Use this procedure when the required source artefacts are available and `AI agent action catalogue` is the next lifecycle deliverable.

## Do Not Use When

- Use `ai-agent-feature-prd-spec` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Approved agent tasks, autonomy limits, APIs, roles, and control policy | Product, API, security, and operations owners | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `AI agent action catalogue`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| AI agent action catalogue | Agent runtime, security, evaluation, and operations teams | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `AI agent action catalogue` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A tool mutates state but lacks idempotency, approval, or compensation | Classify it as unavailable until the missing control is specified. | Uncontrolled or unrecoverable agent mutation. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `AI agent action catalogue` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `AI agent action catalogue` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `ai-agent-feature-prd-spec` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
- [Agent Reversibility Classification Rubric](references/agent-reversibility-classification-rubric.md)
- [Ai Agent Action Catalogue Template](references/ai-agent-action-catalogue-template.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview

The action catalogue is the single source of truth for what tools an agent may call. The planner may only emit tool calls whose names appear in the catalogue. The dispatcher refuses any tool call not in the catalogue. The catalogue is the contract that makes agent behaviour analysable, auditable, and operable.

## Core Instructions

### Step 1: Inventory candidate tools

Walk the agent FRs from `ai-agent-feature-prd-spec` and gather every tool the planner could call to satisfy a step. Include reads, writes, external API calls, and internal RPCs.

### Step 2: Apply the reversibility classification rubric

For each tool, classify as one of:

| Class | Definition | Examples |
|-------|-------------|----------|
| `idempotent` | repeated calls have no additional effect | read APIs, lookups, search |
| `compensable` | side-effect can be cleanly reversed by another tool | issue refund (reverse: re-charge), create-draft (reverse: delete-draft), ledger entry (reverse: reverse-entry) |
| `irreversible` | side-effect cannot be reversed without external escalation | send-email-to-customer, charge-card, delete-file, post-to-public-channel, execute-trade |

See `references/agent-reversibility-classification-rubric.md` for the full rubric and edge-case treatment.

### Step 3: Declare schema and side-effect class

Each tool entry:

```yaml
name: email.draft.create
description: Create a draft reply in the inbox owner's drafts folder; does not send.
input_schema:
  type: object
  required: [thread_id, body]
  properties:
    thread_id: { type: string }
    body:     { type: string, maxLength: 8000 }
output_schema:
  type: object
  properties:
    draft_id: { type: string }
side_effect_class: write-internal
reversibility_class: compensable
compensating_tool: email.draft.delete
```

Side-effect classes: `read`, `write-internal`, `write-external` (to a system outside our trust boundary), `billing`, `network-egress`.

### Step 4: Declare per-tier availability

Each tool entry states which pricing tier may include it for which autonomy level:

```yaml
tier_availability:
  free:       [L0]
  pro:        [L0, L1, L2]
  enterprise: [L0, L1, L2, L3]
```

Tools with `side_effect_class != read` shall not be available on Free tier.

### Step 5: Declare audit fields

For every tool call the dispatcher shall log:

- `tenant_id`, `user_id`, `agent_run_id`, `plan_id`, `step_index`.
- `tool_name`, `input_args_redacted`, `output_summary_redacted`, `latency_ms`, `cost_usd`.
- `outcome` (success / refused / error / timeout / kill-switch-aborted).
- `irreversibility_class` snapshot at call time.
- `human_approval_event_id` if applicable.

### Step 6: Declare rate-limit class

Each tool maps to a rate-limit class enforced at the dispatcher:

| Class | Per-tenant | Per-agent-run | Burst |
|-------|------------|----------------|-------|
| `cheap-read` | 60/min | 100 | 20 |
| `expensive-read` | 10/min | 20 | 5 |
| `internal-write` | 30/min | 50 | 10 |
| `external-write` | 5/min | 10 | 2 |
| `billing` | 2/min | 5 | 1 |

### Step 7: Declare kill-switch behaviour

Each tool entry states:

- Whether the global agent kill-switch refuses this tool (yes for all writes; no for cheap reads).
- Whether the per-tenant kill-switch refuses this tool.
- The user-visible message returned on kill-switch refusal.

### Step 8: Write the spec

`Action_Catalogue_Spec.md` sections: 1) Catalogue summary table, 2) Reversibility rubric, 3) Per-tool entries (or pointer to `action-catalogue/<tool>.yaml`), 4) Tier availability matrix, 5) Audit field schema, 6) Rate-limit class table, 7) Kill-switch behaviour, 8) Change-control protocol (PR + ADR + red-team smoke before merge), 9) Traceability to agent FRs.

## Standards

- OWASP LLM Top 10 (agentic addendum)
- Anthropic tool-use guide (schema discipline)
- NIST AI RMF MEASURE-2 (tool misuse)
- ISO/IEC 42001 Clause 8 (operation)

## Compliance metadata fields (additions)

When the SaaS is in scope of SOC 2, ISO 27001, or HIPAA, each tool entry shall carry the following additional metadata fields:

```yaml
phi_touch:               # none | limited | clinical
cardholder_touch:        # none | reads | writes  (for PCI-DSS scoping)
protected_class_decision: # none | applies (for EU AI Act high-risk + EEOC + Colorado + NYC AEDT)
evidence_class:          # access | approval | integrity | monitoring | change | privacy
retention_minimum:       # ISO 8601 duration; floor per HIPAA / DPA where applicable
```

These fields drive:

- HIPAA classification per `22-ai-agent-hipaa-control-pack` (`HIPAA_PHI_Touch_Classification.md`).
- SOC 2 / ISO sampling stratification per `25-ai-agent-evidence-pack-spec`.
- EU AI Act high-risk treatment per `15-ai-act-and-regulatory-compliance-doc`.

A change to any of these fields requires an ADR per the agent ADR catalogue.

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-action-catalogue-template.md`, `references/agent-reversibility-classification-rubric.md`.
