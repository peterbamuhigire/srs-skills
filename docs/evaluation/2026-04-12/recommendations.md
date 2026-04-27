# Recommendations

## System-Level Priorities

### 1. Deepen the Existing Validation Kernel

The repository no longer needs a first validation kernel. It has one. The next step is to deepen it.

Priority areas:

- semantic requirement-quality checks
- requirement-to-design sufficiency checks
- requirement-to-test-result linkage
- release/runtime evidence ingestion
- stronger clause-level standards proofs

Why this matters:

- the current engine is strong at structure and governance
- the next maturity step is substantive assurance

### 2. Extend the Artifact Graph into a Richer Assurance Graph

The current artifact graph is a real foundation. Expand it to track:

- artifact class and subtype
- review state and approver state
- baseline lineage
- trace categories
- evidence attachments
- implementation/runtime references

This should become the basis for deeper impact analysis and evidence reasoning.

This richer graph should also become the shared synchronization model for Hybrid work so that formal requirements, backlog artifacts, design baselines, and governance evidence are not coordinated only through narrow gate logic.

### 3. Finish Pathing and Skill-Layer Normalization

The canonical pathing model is much clearer now. Keep migrating skill-local assets and helper prompts so the whole repository behaves consistently under the current workspace/runtime model.

### 4. Add First-Class Validation Outputs

The engine already emits machine-actionable pass/fail behaviour. Make the validation outputs richer and more reusable:

- `validation-report.json`
- `validation-report.md`
- `gate-status.json`
- `evidence-index.json`

That will improve CI use, review-pack generation, and downstream integrations.

## Skill-Level Improvements

### 1. Strengthen Requirements Generation

- require stable IDs at first creation
- require explicit source/rationale fields
- require acceptance or verification intent on creation
- detect compound and weak requirements more aggressively

### 2. Strengthen Design Generation

- require ADR use for significant design choices
- require rejected alternatives where trade-offs matter
- require operability and testability notes per major component

### 3. Strengthen Testing Documentation

- bind tests more tightly to requirement IDs and result evidence
- add stronger environment fidelity controls
- ingest actual result artifacts where possible

### 4. Strengthen Compliance Documentation

- extend obligation-to-control-to-requirement-to-test-to-evidence chains
- deepen domain control libraries and review obligations

### 5. Strengthen End-User Documentation

- add task-verification workflows
- add release-note consistency checks
- add audience and usability validation metadata

## New Capabilities to Add

### 1. Requirements-to-Code Traceability

Purpose:

- connect requirement IDs to modules, APIs, schema objects, tests, and releases

Why:

- this is now the clearest missing segment in the assurance chain

### 2. Runtime Evidence Integration

Purpose:

- connect monitoring, release markers, incident reports, and operational checks back to documented controls and requirements

Why:

- world-class status requires proof beyond static documents

## Remediation Roadmap

### Stage 1: Normalize the Operating Model

- finish pathing and skill-local asset normalization against `projects/<ProjectName>/`
- remove compatibility-era execution assumptions from helper prompts and local references
- make validation outputs canonical inputs for downstream skills and evidence packs

### Stage 2: Deepen Hybrid Synchronization

- define a shared data model spanning requirement IDs, backlog items, design elements, baselines, and governance evidence
- extend sync checks from presence/consistency gates to change-aware bidirectional propagation rules
- make Hybrid deltas visible in baseline and change-impact outputs

### Stage 3: Close the Requirements-to-Code-to-Test Chain

- map requirement IDs to modules, interfaces, schema objects, test cases, and test-result artifacts
- require machine-readable evidence references where implementations and tests exist
- expose broken or stale links as first-class validation findings

### Stage 4: Add Release and Runtime Evidence

- ingest release manifests, deployment markers, operational checks, incidents, and monitoring evidence
- link operational signals back to requirements, controls, and waivers where applicable
- add gate logic that can distinguish documented intent from observed operational proof

### Stage 5: Raise Assurance to Audit Depth

- deepen clause-level standards proofs across more phases and artifact types
- add semantic sufficiency checks across requirement, design, test, and control chains
- generate reusable audit views that show requirement-to-code-to-run evidence continuity

### 3. Richer Standards Proof Packs

Purpose:

- generate clause-oriented evidence views for standards and regulatory reviews

Why:

- this is the most direct path from strong governance tooling to audit-grade defensibility

### 4. Semantic Consistency and Sufficiency Checks

Purpose:

- detect contradictions, weak coverage, shallow verification, and likely false completeness across the artifact estate

Why:

- the engine already checks shape well; it now needs deeper content reasoning

## Implementation Order

1. Deepen the existing validation kernel
2. Expand the artifact graph into a richer assurance graph
3. Finish pathing and skill-layer normalization
4. Add first-class validation output artifacts
5. Add requirements-to-code and runtime evidence tracing
6. Deepen standards proof and domain control packs

That sequence builds on the engine that already exists instead of redesigning from scratch.
