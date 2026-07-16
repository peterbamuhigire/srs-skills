---
name: 09-game-test-and-player-evidence-plan
description: "Use when planning game QA, playtesting, balance, deterministic simulation, save migration, multiplayer network conditions, device performance, accessibility, localisation, security, certification, and release-candidate evidence."
metadata: {portable: true, compatible_with: [claude-code, codex]}
---
# Game Test and Player Evidence Plan
<!-- dual-compat-start -->
## Use When
- A game milestone needs technical tests and observed-player evidence.
## Do Not Use When
- Programme testing policy is the task; use `01-test-strategy`.
- Do not substitute opinions for correctness or device evidence.
## Required Inputs
| Artefact | Source or provider | Required? | Behaviour when missing |
|---|---|---|---|
| Requirements, architecture, build manifest, targets and gates | Product, engineering, QA and release | Yes | Stop and issue a readiness gap. |
| Research, network, accessibility, localisation and threat cases | Specialist owners | Conditional | Mark coverage not assessed. |
## Workflow
1. Build a risk matrix across unit, integration, simulation, content, device, network, security and access layers.
2. Specify seeds, clocks, tolerances, replay and save corruption/migration/interruption.
3. Test latency, loss, jitter, reorder, duplication, disconnect, crash and version mismatch online.
4. Profile release builds on named hardware for pacing, CPU/GPU, memory, loading, storage and thermal behaviour.
5. Separate playtest questions, balance experiments and release acceptance.
6. Test critical verbs with alternative input and redundant feedback.
7. Stop on missing build identity or oracle; recover with an evidence plan.
## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Game test and player evidence plan | QA, design, engineering and release | Cases map to requirements, environments, oracles, evidence and decisions. |
## Evidence Produced
| Evidence | Reviewer | Acceptance condition |
|---|---|---|
| `GTEST-*` matrix | QA reviewer | Build, device, scene, seed, network and outcome are reproducible. |
## Capability and permission boundaries
Read and search are allowed; planning is read-only. Shared-service, player-data or security tests require authority and consent.
## Degraded mode
Return the narrowest qualified plan, mark unavailable checks `not assessed`, and retain blocked gates.
## Decision Rules
| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| Oracle absent | Redesign or classify exploratory. | False confidence. |
| Capture lacks identity | Reject release evidence. | Irreproducibility. |
| Core accessibility blocker | Block or approve explicit exclusion. | Menu-only claims. |
## Quality Standards
- Retain failed-path evidence; distinguish preference, comprehension, balance and correctness.
## Anti-Patterns
- Tautological tests. Fix: assert invariants.
- Editor-only testing. Fix: packaged builds.
- Average FPS only. Fix: frame pacing.
- Localhost multiplayer only. Fix: hostile profiles.
- Anecdotal playtests. Fix: question, cohort and disposition.
## References
- [Test evidence matrix](references/game-test-evidence-matrix.md)
<!-- dual-compat-end -->
