# Recommendations

## System-Level Priorities

### 1. Restore a Green Proof Workspace

Highest priority:

- restore or regenerate `projects/_demo-hybrid-regulated`
- ensure it validates cleanly
- commit the workspace or replace tests with a deterministic fixture generator
- update `README.md` so every proof claim is reproducible

Acceptance criteria:

- `python -X utf8 -m pytest engine\tests -q` passes
- `python -X utf8 -m engine.cli validate projects\_demo-hybrid-regulated` passes
- the proof workspace includes `_context`, `_registry`, all phase directories, baseline evidence, and packable evidence output

### 2. Make Test Setup Frictionless

The declared package installs correctly, but a fresh environment cannot run the tests until dependencies are installed.

Recommended changes:

- document `python -m pip install -e ".[dev]"` as the first verification step
- optionally add `scripts/setup-dev.ps1` and `scripts/setup-dev.sh`
- add a short "fresh checkout verification" section to `README.md`
- consider a lock file or constraints file for reproducible CI

Acceptance criteria:

- a new operator can run setup and tests from README without inference
- CI runs the same command sequence as the docs

### 3. Fix Skill Catalog Validation Failures

Address the 15 quick-validator failures.

Priority fixes:

- repair legacy `../CLAUDE.md` and `../sdlc-lifecycle.md` links in SDLC skills
- add missing portable metadata and dual-compat markers where appropriate
- normalize `demand-forecasting`, `tabler-email-templates`, `color-theory`, `design-by-nature`, and `every-layout`
- resolve validator/root assumptions around `skills/00-meta-initialization`
- update root `AGENTS.md` to point to `skills/skills/world-class-engineering` or move the catalog to the documented path

Acceptance criteria:

- 240 of 240 quick validations pass, or documented exemptions are explicit and intentional
- `contract_gate.py --all --strict` is either clean or has tracked accepted warnings

### 4. Create a Clean Realistic Project Workspace

The repo should contain one realistic project that validates cleanly, not only a tiny fixture.

Recommended target:

- choose `AcademiaPro` or create a controlled `ReferenceEnterpriseApp`
- fill missing canonical artifacts
- run `engine sync`
- validate all gates
- build an evidence pack

Acceptance criteria:

- one realistic workspace passes `engine validate`
- evidence pack generation succeeds
- the workspace is used in docs as the real proof path

### 5. Extend the Artifact Graph into an Assurance Graph

Current artifact graphing is a strong foundation. Extend it to model:

- artifact type and subtype
- owner and approver state
- requirement, design, code, test, release, and runtime links
- baseline lineage
- evidence attachments
- stale-link detection

Acceptance criteria:

- validation can answer "what proves this requirement?"
- validation can detect when implementation or test evidence is missing or stale

## Skill-Level Improvements

### Requirements Skills

- require stable IDs at creation time
- require source, rationale, fit criterion, and verification intent
- detect compound, vague, unverifiable, and orphaned requirements
- require downstream trace targets before exit

### Design Skills

- enforce ADRs for irreversible or expensive design decisions
- require rejected alternatives where tradeoffs matter
- require quality-attribute scenarios for key architecture choices
- link components to requirements, interfaces, data, risks, and operational controls

### Development Skills

- introduce requirement-to-code mapping templates
- require module ownership and implementation evidence
- connect coding standards to actual repository structure
- add checks for stale implementation references

### Testing Skills

- ingest actual test-result artifacts
- map test cases and results back to requirement IDs
- distinguish test presence from meaningful oracle quality
- report unverified high-risk requirements

### Deployment and Maintenance Skills

- require release manifests and rollback evidence
- connect monitoring and SLOs to requirements and controls
- ingest incidents, operational checks, and post-deploy verification
- link maintenance changes back to baselines and change impact

## New Capabilities to Add

### 1. Fresh Checkout Verification Command

Add a single documented command or script that verifies:

- package install
- engine contract
- engine tests
- skill quick validation
- contract gate
- proof workspace validation
- evidence pack generation

### 2. Project Health Dashboard

Generate a `project-health.md` and `project-health.json` summary for each workspace:

- gate status
- HIGH/MEDIUM/LOW findings
- missing artifacts
- stale traces
- waiver status
- sign-off status
- evidence-pack readiness

### 3. Requirements-to-Code Traceability

Add machine-readable mappings from requirements to:

- modules
- APIs
- schema objects
- jobs/events
- UI flows
- tests
- releases

### 4. Runtime Evidence Integration

Add ingestion for:

- release manifests
- deployment markers
- smoke-test results
- SLO checks
- incident reports
- monitoring snapshots

### 5. AI Evaluation Harness

For the AI skill layer, add:

- prompt regression tests
- hallucination and unsupported-claim checks
- source-grounding checks
- model/version metadata
- drift review for generated documentation quality

## Implementation Order

1. Restore `_demo-hybrid-regulated` or replace it with generated fixtures.
2. Make the engine suite green.
3. Fix all quick-validator skill failures.
4. Align root and nested path documentation.
5. Create one realistic clean project workspace.
6. Add project health outputs.
7. Extend traceability into code, tests, releases, and runtime evidence.
8. Add AI-specific evaluation and provenance controls.

This sequence fixes reproducibility first, then deepens assurance.
