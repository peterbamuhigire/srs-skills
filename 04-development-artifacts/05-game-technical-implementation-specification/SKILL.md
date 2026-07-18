---
name: 05-game-technical-implementation-specification
description: "Use when turning approved game requirements and architecture into implementable Unity, Godot, Unreal, Apple-native, multiplayer, content-pipeline, build, and telemetry work packages with code and asset contracts."
metadata: {portable: true, compatible_with: [claude-code, codex]}
---
# Game Technical Implementation Specification
<!-- dual-compat-start -->
## Use When
- Game architecture needs module, scene, data, asset, protocol, build and test seams.
## Do Not Use When
- Architecture or authority is undecided.
- Do not copy legacy tutorial code without version verification.
## Required Inputs
| Artefact | Source or provider | Required? | Behaviour when missing |
|---|---|---|---|
| `GREQ-*`, `GARCH-*`, ADRs, toolchain locks and acceptance tests | Architecture, engineering and QA | Yes | Stop the work package and return missing contracts. |
| Asset/UI handoff, data/ads/privacy schemas, adapters, protocol and build interface | Design and specialist owners | Conditional | Exclude or mark integration blocked. |
## Workflow
1. Decompose modules, scenes/worlds, data, assets and adapters with owners.
2. Define responsibilities, interfaces, events, lifetime and dependency rules.
3. Specify save/content/protocol versions, migrations, identifiers and idempotency.
4. Add engine-specific notes only for the pinned version.
5. Make every `GIMPL-*` consume `GREQ-*`, `GARCH-*`, relevant `VCLAIM-*`, approved game-design handoff, exact files/modules/assets or a bounded discovery task, and named exclusions.
6. Specify unit, integration, network, asset/UI, ad/privacy, accessibility/localisation, performance, security and device evidence per work package, including retained failed paths.
7. Define instrumentation purpose, errors, config, secrets, migrations, rollback/kill switches, owner role, estimate range/confidence and recalibration trigger.
8. Stop on an untestable interface, unresolved child/culture/privacy/ad decision or absent build target; recover with a spike and exit criteria.
## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Game technical implementation specification | Client, backend, content, build and QA engineers | Packages have interfaces, versions, failures, tests and traces. |
## Evidence Produced
| Evidence | Reviewer | Acceptance condition |
|---|---|---|
| `GIMPL-*` trace | Technical lead | Packages map requirements and architecture to code/assets, tests and build evidence. |
## Capability and permission boundaries
Read and search are allowed. Source edits, installs, services and releases require explicit authority.
## Degraded mode
Return qualified interface stubs, mark validation `not assessed`, and do not claim buildability.
## Decision Rules
| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| Pure logic uses engine objects | Invert dependency. | Fragile tests. |
| Import is manual | Define presets and validation. | Content drift. |
| Schema is incompatible | Add migration or recovery rejection. | Stranded state. |
## Quality Standards
- No invented packages, hidden globals or placeholder methods; require failed-path evidence.
## Anti-Patterns
- Rules in scene components. Fix: isolate domain logic.
- Singleton sprawl. Fix: scoped composition.
- Manual import folklore. Fix: presets and validators.
- Editor test as completion. Fix: packaged evidence.
- Unbounded frame work. Fix: frequency budgets.
- Visual handoff reduced to a screenshot. Fix: consume states, tokens, content, input/access rules and binary acceptance from the design engine.
## References
- [Work-package schema](references/game-work-package-schema.md)
<!-- dual-compat-end -->
