# Remediation Roadmap

## Purpose

This roadmap turns the April 12, 2026 evaluation gaps into a practical sequence of repository upgrades. It focuses on the three limitations that most clearly separate the current engine from world-class status:

- Hybrid synchronization exists, but remains narrow
- requirements-to-code-to-run evidence is still incomplete
- skill-layer normalization is not finished

## Design Principle

Do not redesign the repository around a new abstraction first. Build forward from the kernel that already exists:

- workspace model
- artifact graph
- phase gates
- registries
- baseline and evidence-pack workflows

## Stage 1: Finish Skill-Layer Normalization

Goal:

- make the canonical `projects/<ProjectName>/` execution model consistent across root guidance, skill-local entrypoints, helper prompts, and supporting assets

Concrete outputs:

- eliminate obsolete pathing assumptions in skill-local references
- align helper assets with `_context/`, `_registry/`, and canonical output locations
- make validation and evidence outputs reusable inputs for downstream skills

Success condition:

- the same project behaves consistently whether invoked from root guidance, a phase skill, or a helper asset

## Stage 2: Expand Hybrid Synchronization into a Shared Model

Goal:

- replace narrow synchronization checks with a richer shared model spanning formal and agile artifacts

Concrete outputs:

- shared identifiers linking requirements, backlog items, design baselines, and governance evidence
- explicit synchronization rules for forward and backward change propagation
- baseline and change-impact views that show Hybrid drift and unresolved deltas

Success condition:

- Hybrid programmes no longer depend mainly on manual coordination once artifact volume and change frequency increase

## Stage 3: Build the Requirements-to-Code-to-Test Chain

Goal:

- extend traceability beyond document references into implementation and verification structures

Concrete outputs:

- requirement-to-module, API, schema, and interface mappings
- requirement-to-test-case and test-result mappings
- validation findings for broken, stale, or missing implementation/test evidence links

Success condition:

- a reviewer can trace a requirement through design, implementation, and executed verification evidence without relying on narrative interpretation alone

## Stage 4: Add Release and Runtime Evidence

Goal:

- connect the documented system to release events and operational reality

Concrete outputs:

- release manifest and deployment evidence ingestion
- operational check, incident, monitoring, and SLI/SLO evidence linkage
- trace paths from runtime signals back to requirements, controls, and waivers

Success condition:

- the engine can distinguish "documented" from "implemented and observed"

## Stage 5: Deepen Assurance Quality

Goal:

- convert strong structural governance into stronger engineering assurance

Concrete outputs:

- broader clause-level standards proof across more phases and artifact classes
- semantic sufficiency checks across requirement, design, test, and control chains
- audit-oriented evidence views showing end-to-end continuity

Success condition:

- the engine can defend not only artifact structure and linkage, but also a materially stronger claim of implementation-grounded assurance

## Recommended Order

1. Finish skill-layer normalization
2. Expand Hybrid synchronization into a shared model
3. Build the requirements-to-code-to-test chain
4. Add release and runtime evidence
5. Deepen assurance quality

## Why This Order

The sequence keeps the repository coherent while increasing assurance depth:

- normalization removes local execution inconsistency before adding more coupling
- Hybrid synchronization becomes easier once the operating model is stable
- code and test traceability should exist before runtime evidence is layered on top
- audit-depth reasoning is strongest after the evidence graph is richer
