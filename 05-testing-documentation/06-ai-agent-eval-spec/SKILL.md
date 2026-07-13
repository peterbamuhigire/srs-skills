---
name: 06-ai-agent-eval-spec
description: Use when evaluating a multi-step AI agent for task success, tool selection, budgets, intervention, recovery, and side-effect evidence; use ai-eval-harness-spec for single-call or non-agentic AI feature evaluation.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Agent Eval Spec Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI evaluation specification from approved project evidence.
- Resolve decisions about representative datasets, evaluators, thresholds, calibration, regression gates, and evidence.
- Prepare a reviewable handoff for AI engineering and release teams.

## Do Not Use When

- The task is primarily owned by test-plan; route there and use this skill only for its named output.
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
| AI Evaluation Specification | AI engineering and release teams | Each evaluated behaviour has a representative dataset, deterministic scoring rule, threshold rationale, and retained run evidence. |
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
| Evidence is complete and authority is explicit | Choose evaluators and thresholds from the stated product risk and produce the full artefact. | A benchmark score without a release oracle. |
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
- Mixing the neighbouring test-plan concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when each evaluated behaviour has a representative dataset, deterministic scoring rule, threshold rationale, and retained run evidence.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

The agent-specific complement to `ai-eval-harness-spec`. Agents are evaluated on outcomes and trajectories, not single-shot generations. Eval requires (a) golden-task sets that capture the goal state, (b) replay environments that make every tool call deterministic, and (c) agent-specific metrics.

## Core Instructions

### Step 1: Inventory golden-task sets per feature

For each agent FR declare a `GOLDEN-AGT-<FEATURE>-NNN` set. Each task carries:

```yaml
id: AGT-TRG-001
feature: inbox-triage
initial_state: <world state before the run>
user_goal: <natural-language goal>
gold_trajectory: <ordered list of (tool, args, observation) tuples that a competent operator would execute>
goal_state: <world state the agent should reach>
acceptance_rubric: <how a judge decides whether goal_state was reached>
tags: [tier:pro, locale:en-US, sensitivity:low]
```

### Step 2: Define the replay environment

For each feature, declare a deterministic synthetic environment that responds to tool calls with canned outputs:

- Storage: `replay-env/<feature>/<task_id>.yaml`.
- Responder: maps `(tool_name, input_args_canonical)` to a fixed output.
- Variance: zero (the environment is byte-deterministic given the same agent trajectory).
- Failure injection: parameterised — the environment can be configured to return errors, timeouts, or malicious outputs for adversarial replays.

### Step 3: Declare the six core agent metrics with thresholds

| Metric | Definition | Default threshold |
|--------|------------|---------------------|
| Task success rate | judge marks `goal_state` reached | >= 0.90 |
| Step efficiency | mean(actual_steps / gold_steps) on successful runs | <= 1.5 |
| Tool-choice quality | % of tool calls that match the gold tool at the gold step | >= 0.92 |
| Hallucinated-argument rate | % of tool calls with at least one fabricated argument | <= 0.01 |
| Irreversible-action-incident rate | irreversible actions that the judge marks as incorrect | 0 (zero-tolerance) |
| Intervention rate | % of runs where mid-run human intervention was required | feature-specific; declared in PRD |

### Step 4: Define the judge-LLM rubric per metric

- Task success: pairwise compare `goal_state` claimed by agent vs the YAML `goal_state`; rubric 3 binary criteria.
- Tool-choice quality: exact-match for `tool_name`; semantic-match for `args` via judge-LLM.
- Hallucinated argument: judge inspects each arg; flags any arg not derivable from the observation history.

Calibration set per feature scored monthly by humans; recalibrate if drift > 5 pp.

### Step 5: Define the CI gate

CI gate runs on every PR touching `planner/`, `tools/`, `prompts/agent/`, or `action-catalogue/`:

1. Task success on the affected feature's golden set not down > 2 pp.
2. Tool-choice quality not down > 1 pp.
3. Hallucinated-argument rate not up > 0.005 pp.
4. Irreversible-action-incident rate = 0.

### Step 6: Define scheduled regression

| Cadence | Suite | Action on drop |
|---------|-------|------------------|
| Nightly | Golden + adversarial smoke per feature | SEV3 to AI lead if any metric down > 3 pp |
| Weekly | Full agent red-team replay | SEV2 if any new HIGH finding |
| Monthly | Calibration recheck | recalibrate judge if drift > 5 pp |
| Quarterly | Full sweep | update agent model card; review with security |

### Step 7: Operational ownership

The agent eval rig is owned by the AI lead with a named back-up. Replay-env updates require PR with a reviewer from the back-end owner of every called system. Golden-task additions require sign-off from the AI lead and the product owner of the feature.

### Step 8: Write the spec

`AI_Agent_Eval_Spec.md` sections: 1) Per-feature Golden-Task Inventory, 2) Replay Environments, 3) Metrics & Thresholds, 4) Judge-LLM Rubrics, 5) CI Gate, 6) Scheduled Regression, 7) Operational Ownership, 8) Traceability.

## Standards

- OpenAI Evals (agents)
- Anthropic agent-eval patterns
- NIST AI RMF MEASURE
- ISO/IEC 42001 Clause 9

## Compliance evidence cross-link

Eval coverage is primary evidence for:

- SOC 2 PI1.2 (processing accuracy), CC4.1 (ongoing monitoring), CC8.1 (change management).
- ISO/IEC 27001:2022 A.8.25 (secure development lifecycle), A.8.29 (security testing).
- EU AI Act Art. 15 (accuracy and robustness).
- NIST AI RMF MEASURE.

The CI gate results, weekly regression report, and monthly calibration recheck are collected per `09-governance-compliance/25-ai-agent-evidence-pack-spec` (frequency-table rows 23, 24). Sampling: 25 PR eval results stratified across features and tiers per audit window.

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-eval-spec-template.md`.
