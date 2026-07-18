---
name: 05-ai-agent-coding-guidelines-addendum
description: Use when producing or updating AI-agent coding-guidelines addendum for tool schemas, reversibility, blast-radius caps, deterministic state, idempotency, timeouts, and HITL gates. Use coding-guidelines for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Agent Coding Guidelines Addendum Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI-agent coding-guidelines addendum from approved project evidence.
- Resolve decisions about tool schemas, reversibility, blast-radius caps, deterministic state, idempotency, timeouts, and HITL gates.
- Prepare a reviewable handoff for Agent-runtime developers and reviewers.

## Do Not Use When

- The task is primarily owned by coding-guidelines; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, and relevant architecture | Project owner and upstream phase skills | Required | Stop at a gap register; do not invent scope, thresholds, integrations, or owners. |
| Existing artefact, implementation, configuration, and evidence named below | Repository, delivery team, or service owner | Required when updating or assessing | Mark inaccessible items `not assessed`; do not treat them as passed. |
| Target audience, environment, risk tolerance, and authority | Requester and accountable owner | Required | Produce a read-only outline with explicit assumptions; do not mutate project or production state. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI-agent Coding-guidelines Addendum | Agent-runtime developers and reviewers | Every agent tool boundary has schema validation, authority classification, idempotency, timeout, and test obligations. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Assessment and planning default to read-only. Create or edit the named project document only when the request explicitly authorises it. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose controls by tool reversibility and authorised blast radius and produce the full artefact. | Unsafe autonomous mutations or unreplayable runs. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring coding-guidelines concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every agent tool boundary has schema validation, authority classification, idempotency, timeout, and test obligations.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Core Instructions

### Step 1: Codify tool-schema discipline

- Every tool wrapper validates inputs against the catalogue schema at the function boundary; the planner's free-form output is never trusted.
- Outputs from external systems are parsed against the declared output schema and rejected on mismatch.
- Schema validation libraries are pinned and CI-tested.

### Step 2: Codify irreversibility annotations

- Every tool function carries a decorator or attribute that names its `reversibility_class`.
- A static-analysis check fails CI if a tool function exists in the codebase without an irreversibility annotation.
- The dispatcher reads the annotation at runtime; mismatch between code annotation and catalogue YAML fails startup.

### Step 3: Codify blast-radius caps

- Every tool call inside a single agent run has a per-tool cap (e.g. `email.send` capped at 5 per run).
- Caps are enforced at the dispatcher; the planner does not enforce.
- Per-run caps are loaded from the action catalogue at run start.

### Step 4: Codify deterministic state

- Agent run state is `(plan, observations, scratchpad, cumulative_cost)`. State mutations are pure functions of `(previous_state, transition_event)`.
- No tool wrapper is allowed to mutate run state directly; it returns a `ToolResult` that the orchestrator applies to state.
- Replay = re-applying transitions to the initial state in order.

### Step 5: Codify idempotency keys

- Every tool call carries `idempotency_key = sha256(agent_run_id + ':' + step_index)`.
- Tool wrappers pass the key to the underlying API where supported.
- Retries reuse the same key. Different idempotency keys on retry are a bug.

### Step 6: Codify error and timeout policy

- Every tool wrapper has a default timeout from the catalogue YAML.
- Errors are classified `retryable | non-retryable | safety`.
- `retryable` errors back off (1s, 4s, 16s) with the same idempotency key.
- `non-retryable` errors fail the step; orchestrator decides whether to abstain or re-plan.
- `safety` errors (content-filter trip, kill-switch hit, schema fail) terminate the run; no retry.

### Step 7: Codify the test contract

- Every tool wrapper has unit tests against (a) happy path, (b) schema-fail input, (c) timeout, (d) non-retryable error, (e) safety error.
- Every planner change ships with an agent-eval rig run on the affected feature's golden-task set.
- Coverage on agent-runtime code: 90% line coverage; 100% on the dispatcher hot path.

### Step 8: Write the addendum

`Coding_Guidelines_Agent_Addendum.md` sections: 1) Tool-Schema Discipline, 2) Irreversibility Annotations, 3) Blast-Radius Caps, 4) Deterministic State, 5) Idempotency Keys, 6) Error & Timeout Policy, 7) Test Contract, 8) Static-Analysis & CI Hooks, 9) Style Examples.

## Standards

- OWASP LLM Top 10 (agentic addendum)
- Anthropic agent-engineering patterns
- Google production-LLM playbooks
- IEEE 1016-2009 §5 (Design viewpoints)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-coding-guidelines-addendum-template.md`.
