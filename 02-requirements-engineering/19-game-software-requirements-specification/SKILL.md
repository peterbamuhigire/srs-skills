---
name: 19-game-software-requirements-specification
description: "Use when specifying testable game software requirements for player experience, gameplay state, platforms, multiplayer, saves, content, performance, accessibility, telemetry, security, builds, release, or live operations."
metadata: {portable: true, compatible_with: [claude-code, codex]}
---
# Game Software Requirements Specification
<!-- dual-compat-start -->
## Use When
- A game needs a controlled SRS across client, server, content and operations.
## Do Not Use When
- The concept is unbounded; use the game product brief first.
- Do not prescribe engine or service APIs without a pinned decision.
## Required Inputs
| Artefact | Source or provider | Required? | Behaviour when missing |
|---|---|---|---|
| Approved brief, journeys, target matrix, rules and risks | Product, design, engineering and production | Yes | Stop affected requirements and issue a gap record. |
| Online, economy, data, safety, rights and platform obligations | Specialist owners | Conditional | Exclude or mark the feature blocked. |
## Workflow
1. Establish boundaries across client, authoritative services, platform services, content/build pipeline and operations.
2. Assign `GREQ-*` and specify action, precondition, authoritative transition, feedback, failure and oracle.
3. Specify saves, time/randomness, input, content, accessibility and localisation.
4. For online play specify authority, sessions, replication intent, reconnect, version skew and abuse cases.
5. Add conditioned device performance, memory, loading, thermal, network and storage measures.
6. Specify telemetry purpose, economy integrity, privacy, build provenance and rollback.
7. Stop on an ownerless transition or unverifiable threshold; recover with a decision request.
## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Game SRS and register | Architecture, implementation, QA and operations | Every behaviour has owner, boundary, condition, oracle and trace. |
## Evidence Produced
| Evidence | Reviewer | Acceptance condition |
|---|---|---|
| Requirement-source-oracle trace | Requirements reviewer | No requirement rests only on assumption or editor behaviour. |
## Capability and permission boundaries
Read and search are allowed. Editing baselines requires authority; paid services, policy or certification require approval.
## Degraded mode
Return the narrowest qualified subsystem, mark unavailable evidence `not assessed`, and block dependent claims.
## Decision Rules
| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| Mutable field has no authority | Block and assign ownership. | Desynchronisation or exploit. |
| NFR lacks conditions | Replace or mark provisional. | Decorative requirements. |
| Trust/money boundary exists | Add validation, idempotency and recovery. | Fraud or lost state. |
## Quality Standards
- Use stimulus, condition, response, measure, tolerance and verification method.
## Anti-Patterns
- “Fun” as requirement. Fix: define research evidence.
- “Runs smoothly.” Fix: name hardware, build and metric.
- Client-authoritative economy. Fix: trusted validation.
- Save migration omitted. Fix: add corruption and interruption cases.
- Menu-only accessibility. Fix: cover gameplay verbs.
## References
- [Game requirement catalogue](references/game-requirement-catalogue.md)
<!-- dual-compat-end -->
