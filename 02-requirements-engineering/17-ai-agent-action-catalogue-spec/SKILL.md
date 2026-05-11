---
name: "ai-agent-action-catalogue-spec"
description: "Generate the Action Catalogue Spec: the enumerated, schema-bound set of tools an agent may call. Every tool declares input/output schema, side-effect class, reversibility class, per-tier availability, audit fields, rate-limit class, and kill-switch behaviour. This is the contract between the planner, the dispatcher, and the operator."
metadata:
  use_when: "Use as soon as one or more agent features are admitted to the AI Agent Feature PRD Spec. The action catalogue is the single source of truth for what tools the agent may call."
  do_not_use_when: "Do not use for non-agent AI features that have no tool surface; the AI architecture spec already covers retrieval and direct LLM calls."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, AI_Architecture_Spec.md, Multi_Tenancy_Architecture_Spec.md, API specifications for the back-end systems the agent will call, agent reversibility classification rubric."
  workflow: "Inventory candidate tools, apply the reversibility classification rubric, attach schema and side-effect class, attach per-tier availability, attach audit fields, attach rate-limit class, attach kill-switch behaviour, write the Action_Catalogue_Spec.md."
  quality_standards: "Every tool shall declare schema, side-effect class, reversibility class, per-tier availability, audit fields, rate-limit class, and kill-switch behaviour. Any tool with reversibility=irreversible shall have a human-approval gate referenced at the FR layer."
  anti_patterns: "Do not admit free-form 'execute shell' tools. Do not omit the reversibility class. Do not let any tool ship at Free tier with side-effect class != read. Do not omit the kill-switch behaviour."
  outputs: "Action_Catalogue_Spec.md and per-tool YAML entries in `action-catalogue/`."
  references: "Use references/ai-agent-action-catalogue-template.md and references/agent-reversibility-classification-rubric.md."
---

# AI Agent Action Catalogue Spec Skill

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
