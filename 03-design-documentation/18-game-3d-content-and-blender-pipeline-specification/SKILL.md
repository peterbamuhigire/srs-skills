---
name: 18-game-3d-content-and-blender-pipeline-specification
description: Use when specifying a game's 3D asset and Blender source-to-engine pipeline, including asset briefs, rigs, animation clips, UV/bakes, materials, LODs, collision, export/import, lineage, automation, runtime budgets, and acceptance evidence; use game-system-architecture for whole-system boundaries.
metadata: {portable: true, compatible_with: [claude-code, codex]}
---
# Game 3D Content and Blender Pipeline Specification

Define the project-specific, versioned contract that turns approved 3D content intent into reproducible Blender sources and verified runtime assets.

<!-- dual-compat-start -->
## Use When
- A game SRS and art direction require a Blender/DCC-to-engine production specification.
- Characters, props, environments, vehicles, rigs, animation, LODs, collision or export evidence need deterministic acceptance criteria.

## Do Not Use When
- The decision is whole-game architecture; use `17-game-system-architecture-specification`.
- The work is class/module implementation; use `05-game-technical-implementation-specification`.
- Blender has not been selected; keep the contract DCC-neutral and record the unresolved ADR.

## Required Inputs
| Artefact | Source or provider | Required? | Behaviour when missing |
|---|---|---:|---|
| Approved `GREQ-*`, game architecture, art direction and player/camera use | Project workspace | Yes | Stop and list missing decisions. |
| Pinned Blender, exporter, engine/importer and platform versions | Technical art/engineering | Yes | Produce only a provisional spike contract. |
| Asset inventory, runtime budgets and simultaneous-count envelopes | Art, performance, production | Yes | Block numeric acceptance and scale claims. |
| Cultural provenance, rights, safeguarding and reference approvals | Research/governance | Conditional | Block affected asset production. |

## Workflow
1. Inspect `_context/`, requirements, architecture, art direction, asset inventory, budgets, rights and source register; record exact sources used.
2. Specify toolchain versions, extensions, units/axes, transforms, colour management, names, folders, source-control and generated boundaries.
3. Create `GASSET-*` contracts for each asset class: use/camera distance, silhouette, topology, UV/bake/material, hierarchy/pivot, rig/animation, collision, LOD, import and runtime envelope.
4. Define export skeleton/control separation, clip/event/root-motion/socket rules, influence/corrective limits and deformation stress poses where applicable.
5. Define pinned export/import presets, clean re-import, deterministic automation, validation reports and source→export→import→build lineage.
6. Specify engine stress scenes, target-device budgets and failure/recovery behaviour. Tutorial figures are never project budgets.
7. Trace each `GASSET-*` to `GREQ-*`, `GARCH-*`, `GIMPL-*`, `GTEST-*`, owner and retained evidence.
8. Run anti-slop and source/version checks; stop on missing rights, owner, target hardware, measurable oracle or reproducible import.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| 3D content and Blender pipeline specification | Art, technical art, engineering, QA | Version, source, export/import, runtime and failure contracts are explicit. |
| Asset acceptance/trace matrix | QA, performance, release | Every requirement has owner, oracle, build/device and evidence path. |

## Evidence Produced
| Evidence | Reviewer | Acceptance condition |
|---|---|---|
| Toolchain and asset-lineage manifest | Technical art/release | Source revision, exporter/importer, engine build and dependencies are reproducible. |
| Clean re-import and runtime acceptance report | QA/performance | Structure, deformation, material, collision, LOD and measured budgets have pass/fail results. |
<!-- dual-compat-end -->

## Capability and permission boundaries
Read and search are required. Editing project specs is allowed by the request; modifying `.blend` files, installing add-ons, accepting licences, publishing content or changing release imports requires separate authority.

## Degraded mode
Without Blender execution or target-engine import, produce a qualified specification and mark export fidelity, deformation, materials and runtime cost `not assessed`; do not infer them from screenshots.

## Decision Rules
| Choice or condition | Action | Risk avoided |
|---|---|---|
| Blender/exporter version unknown | Freeze a versioned spike first. | Irreproducible assets. |
| Detail has no silhouette/deformation/gameplay value | Bake, instance, texture or remove. | Unmeasured complexity. |
| Rig feature cannot export | Bake to a stable deformation skeleton or reproduce in engine. | DCC-only motion. |
| Historic tutorial conflicts with official pinned docs | Use official behaviour and record divergence. | Obsolete implementation. |

## Quality Standards
- Every `GASSET-*` is singular, uniquely identified, traced and paired with a deterministic oracle.
- Include target build, scene, hardware, simultaneous count, percentile/window where performance is claimed.
- Keep project canon and cultural claims tied to approved provenance and named review.
- Apply `09-governance-compliance/28-anti-ai-slop` before release.

## Anti-Patterns
- “Optimised asset” without budget. Fix: name metric, scene, device and threshold.
- Beauty render as proof. Fix: clean re-import plus runtime evidence.
- Control rig exported wholesale. Fix: stable export skeleton and baked contract.
- One generic LOD value. Fix: measure asset class, coverage and simultaneous scene.
- Book path as runtime dependency. Fix: retain self-contained rules and source limits.

## References
- [Specification structure](references/blender-content-pipeline-specification.md)
- [Asset verification matrix](references/blender-asset-verification-matrix.md)
- [Skill authoring and release standard](../../docs/skill-authoring-standard.md)
