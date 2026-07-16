# Blender Content Pipeline Specification Structure

1. Scope, exclusions, project sources and decision owners.
2. Player/camera use and approved art/cultural direction.
3. Pinned Blender, add-ons, exporter, engine/importer and platform matrix.
4. Units, axes, transforms, scale, naming, folders, libraries and generated boundaries.
5. Asset-class contracts: brief, topology, UV, bake, material, hierarchy, pivot, collision, LOD and bounds.
6. Character contracts: deformation/export/control layers, naming/orientation, weights, correctives, facial, cloth/hair, sockets and props.
7. Animation contracts: clip ID, frame/rate, root motion, loops, events, interruption, compression and fallback.
8. Export/import automation, presets, clean re-import and dependency checks.
9. Runtime budgets and representative stress scenes.
10. Acceptance, traceability, change/version policy, evidence retention and stop conditions.

## `GASSET-*` record

Each record includes ID, source `GREQ-*`, asset class/owner, approved brief/provenance, source file/version, transform/geometry/material/rig/animation/collision/LOD requirements, engine import configuration, runtime metric/threshold/scenario/device, deterministic oracle, evidence path and unresolved caveat.

## Source discipline

The Blender books supplied in July 2026 are learning sources. Blender 2.x/3.5 and host-specific instructions are historical until verified against the pinned official toolchain. *Blender 3D for Jobseekers* was not admitted because the supplied Markdown contains no substantive text.
