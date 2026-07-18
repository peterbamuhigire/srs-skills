---
name: 30-game-delivery-evidence-and-greenlight-pack
description: "Use when assembling or reviewing game greenlight, milestone, release, rights, security, player-research, build, test, live-operations, and independent-replication evidence without inflating capability claims."
metadata: {portable: true, compatible_with: [claude-code, codex]}
---
# Game Delivery Evidence and Greenlight Pack
<!-- dual-compat-start -->
## Use When
- A milestone, release, acceptance or capability claim needs traceable evidence.
## Do Not Use When
- Evidence does not exist; prose cannot replace proof.
- This skill does not certify stores, security, access or law.
## Required Inputs
| Artefact | Source or provider | Required? | Behaviour when missing |
|---|---|---|---|
| Brief, traces, builds, manifests, risks and approvals | Product, engineering, QA and governance | Yes | Stop the gate and record missing evidence. |
| Player, learning, culture/rights, wellbeing, ads/privacy, commercial, security, access, platform and independent evidence | Specialist owners | Conditional | Mark claim not assessed or fail its gate. |
## Workflow
1. Inventory evidence by identity, source, version, owner, date and integrity.
2. Trace promise through requirements, architecture, implementation, tests, build and operations.
3. Check rights/culture, device, player/learning, online, security, access, data/economy/ads, commercial, release and support gates.
4. Separate documented, prototype-observed, build-executed, device-measured, player-observed, accountable-expert-approved and independently replicated evidence.
5. Pair commercial evidence with fairness, privacy, child safety, culture, wellbeing, trust, refunds/complaints and stopping; revenue or retention cannot override a failed guardrail.
6. Record greenlight, pivot, narrow, hold or stop with blockers, assumptions, waivers, approver, expiry and rollback.
7. Stop on fabricated, mismatched, source-shaped or copyright-unsafe evidence; recover by removing the claim and rerunning ingestion checks.
## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Game evidence and greenlight pack | Sponsor, client, release board and auditor | Decisions link to inspectable evidence, gaps and approval. |
## Evidence Produced
| Evidence | Reviewer | Acceptance condition |
|---|---|---|
| Evidence manifest and gate ledger | Independent reviewer | Identity, provenance, result, limitation and disposition are explicit. |
## Capability and permission boundaries
Read and search are allowed; review is read-only. Editing evidence, waiving blockers or approving release requires authority.
## Degraded mode
Return the narrowest qualified report, mark unavailable checks `not assessed`, and never infer a pass.
## Decision Rules
| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| Build identity mismatches | Fail release gate. | Untested approval. |
| Prose exists without execution | Withhold proof credit. | Inflated maturity. |
| Waiver lacks expiry | Reject waiver. | Permanent exception. |
## Quality Standards
- Preserve negative results; world-class claims require reproducibility, independent review, failed paths and repeatability.
## Anti-Patterns
- File count as maturity. Fix: grade execution.
- Screenshot without identity. Fix: link checksum.
- Self-approval. Fix: independent reviewers.
- Waiver without expiry. Fix: time-bound it.
- Inflated case study. Fix: cite evidence and limits.
- Documentation passed as player/device proof. Fix: grade every claim by the strongest matching evidence actually retained.
## References
- [Evidence manifest](references/game-evidence-manifest.md)
<!-- dual-compat-end -->
