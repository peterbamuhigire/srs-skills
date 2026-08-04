<!-- Source basis: Designing for AI early release chapters 1-4; XP 2026 AI evaluation and architecture-uncertainty papers. Later chapters in the early release were unavailable. -->

# AI Architecture Oversight and Drift

Extend the AI plane with explicit control and learning paths.

## Required architecture views

- problem and non-AI alternative;
- human, affected non-user, reviewer and escalation map;
- model/system/input/output/data-flow map;
- policy, tool, retrieval, prompt, feature-flag and fallback boundaries;
- uncertainty, correction, contest, undo, consent, audit and notification paths;
- offline eval, shadow, supervised, canary and GA promotion gates;
- input drift, output drift, subgroup regression, cost, latency and incident signals;
- model/prompt/data/config versioning, rollback and re-promotion criteria.

## Decision rule

Keep the safest existing path when evidence is missing. Isolate experimental
models behind an adapter or flag. Make human override authoritative at the
system boundary. A dashboard without a response owner, threshold and rollback
action is not operational observability.
