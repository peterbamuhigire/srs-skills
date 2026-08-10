---
name: 31-kaizen-engine-and-product-improvement
description: Use when auditing or improving the SDLC documentation engine or any PRD, SRS, architecture, test, deployment, governance, or game documentation product it produces.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Kaizen Engine and Product Improvement
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Auditing this catalogue or any SDLC, AI, SaaS, agent, game, regulated, or hybrid delivery document.
- Turning retrospectives, failed gates, change requests, incident evidence, or user feedback into a standardised improvement.

## Do Not Use When

- A single skill safety audit is sufficient.
- A current legal, standards, finance, security, or platform claim has not been independently verified.

## Required Inputs

| Artefact | Source/provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Project phase/methodology, product/output type, requirements/evidence, current score, constraints, reviewers, and target outcomes | Project context and engine | yes | Set audit scope and improvement target | Stop or mark unassessed |

## Workflow

1. Read `docs/continuous-improvement/kaizen-adoption-2026-08.md` and the portfolio standard.
2. Inventory phase routes, traceability, templates, examples, deterministic gates, project evidence, and cross-engine handoffs.
3. Score each applicable dimension and output type. Publish `min(raw score, 65)` and list blockers separately.
4. Audit purpose, requirements quality, traceability, architecture/design coherence, test and failed-path evidence, accessibility, security, deployment, operations, governance, and handoff.
5. Build a P0/P1/P2 remediation plan targeting 95/100 with named files, owners, measures, acceptance evidence, and rollback.
6. Run one small PDCA or retrospective experiment. If a gate fails, stop, recover the last safe artefact, and rerun the affected checks.
7. Promote successful learning into the relevant skill, addendum, template, fixture, routing rule, or governance gate; schedule re-audit.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Capped scorecard, traceability/evidence gaps, blockers, 95/100 plan, experiment record, and standardisation change | Project owner, reviewer, and release owner | Every gap has evidence, owner, action, acceptance proof, rollback, and next review |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Inventory, score calculation, trace links, deterministic gate results, failed-path evidence, and before/after review | Markdown, validator output, or project evidence pack | Another reviewer can reproduce the conclusion and verify the change |

## Capability and permission boundaries

Read and search are required. Audits are read-only by default; editing project artefacts, publishing, certification, production changes, or risk acceptance require explicit authority and permission. Route implementation to skills-web-dev, visual work to design-system-skills, finance to Chwezi, and current evidence to Digital Research.

## Degraded mode

If project evidence, renders, tools, reviewers, or current sources are unavailable, return the narrowest qualified result, mark the check not assessed, and do not certify readiness.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A requirement cannot be traced to acceptance evidence | Stop dependent release and add the trace | Unverifiable delivery |
| A process addition increases ceremony without reducing defects, rework, or decision latency | Reject or simplify it | Process waste |
| A change passes affected gates and improves the target measure | Standardise it and re-audit | Lost learning |

## Quality Standards

Documentation never substitutes for executable, rendered, user, security, or release evidence. Preserve Waterfall, Agile, and Hybrid distinctions.

## Mandatory 65-to-95 gate

The first review is an initial analysis: show raw findings but publish only
`min(raw_score, 65)` and list unassessed evidence and release blockers separately.
After freezing that baseline, target 95/100 through a traceable improvement cycle.
Each action must identify its root cause, exact document/template/gate/fixture,
owner, measure, guardrail, stop/rollback rule, acceptance evidence, and re-audit date.
Run it at engine level (routes, templates, standards, fixtures, validators, and
handoffs) and product level (PRD, SRS, architecture, test, deployment, governance,
or game document). Each product must carry its own traceability evidence.

## Anti-Patterns

- A retrospective with no action owner. Fix: create a dated experiment and evidence.
- Requirements that cannot be tested. Fix: add measurable acceptance criteria and trace links.
- Calling a template compliant without project proof. Fix: verify authority and evidence.
- Adding process without reducing waste. Fix: measure cycle time, defects, rework, or decision latency.
- Closing a gap without re-running gates. Fix: require before/after proof.

## Worked Example

If a game SRS has a complete feature list but no failed-path, accessibility, performance, or player-evidence links, keep the readiness gate blocked, add the missing evidence plan, run it, and then re-score.

## References

- [Local adoption plan](../../docs/continuous-improvement/kaizen-adoption-2026-08.md)
- Portfolio standard: `C:\wamp64\www\digital-research-engine\docs\continuous-improvement\portfolio-kaizen-standard-2026-08.md`
- `07-agile-artifacts/04-retrospective-template/`
- `09-governance-compliance/29-ai-slop-audit/`
- [Product audit evidence matrix](references/product-audit-evidence-matrix.md)

<!-- dual-compat-end -->
