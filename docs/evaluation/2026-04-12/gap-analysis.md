# Gap Analysis

## What Still Prevents World-Class Status

The project has the right architecture and much of the right machinery. The remaining blockers are concentrated in proof, normalization, semantic depth, and implementation/runtime linkage.

## 1. Missing End-to-End Proof Workspace

The most concrete gap is that `README.md` and engine tests reference `projects/_demo-hybrid-regulated`, but that workspace is absent.

Impact:

- two engine tests fail
- the claimed clean end-to-end proof path cannot be reproduced
- the old evaluation's strongest evidence claim is no longer valid

World-class expectation:

- at least one committed project workspace validates cleanly across all gates
- the test suite depends only on committed fixtures or generated fixtures
- README proof claims are reproducible from a fresh checkout

## 2. Engine Suite Is Not Green From Current Checkout

After installing declared dev dependencies, the suite runs but fails:

- 211 tests run
- 2 fail
- 2 skip
- 95% coverage

Impact:

- the kernel remains credible, but release confidence is reduced
- coverage is high, but passing status matters more than the percentage

World-class expectation:

- `pip install -e ".[dev]"`
- `python -X utf8 -m pytest engine\tests -q`
- zero failures
- documented fixture generation where committed examples are not stored

## 3. Project-Level Validation Is Not Clean

`projects\AcademiaPro` currently fails validation with many HIGH findings, including missing canonical context, ADR/threat model, development setup, test evidence, deployment docs, agile artifacts, end-user docs, and governance files.

Impact:

- the engine can detect defects, which is good
- but the repository does not currently demonstrate a clean client-scale workspace

World-class expectation:

- one small synthetic green workspace
- one realistic green workspace
- one intentionally broken fixture that proves failures are specific and useful

## 4. Skill-Layer Normalization Is Incomplete

The local quick validator found 15 failing skill entrypoints out of 240.

Observed failure types:

- missing portable metadata
- missing dual-compat markers
- broken local links
- legacy `../CLAUDE.md` and `../sdlc-lifecycle.md` assumptions
- validator assumptions tied to `skills/skills`
- root-level routing drift

Impact:

- most of the catalog is usable
- the system is not yet uniformly portable across Claude Code and Codex
- path drift increases operator confusion

World-class expectation:

- 100% quick-validator pass rate or explicit documented exemptions
- root docs and nested docs agree on canonical paths
- every skill with warnings has a planned owner and remediation path

## 5. Semantic Assurance Still Lags Structural Assurance

The engine catches many structural and governance issues:

- missing identifiers
- weak traceability
- glossary drift
- unresolved fail markers
- missing required artifacts
- waiver and sign-off defects
- baseline and change-impact issues

It still cannot reliably prove:

- whether a requirement is substantively correct
- whether a design truly satisfies the requirement
- whether a test would catch the important failure modes
- whether a compliance claim is complete
- whether runtime behavior matches documented intent

Impact:

- strong documentation governance
- limited substantive assurance

## 6. Requirements-to-Code-to-Run Traceability Is Missing

The current engine is strongest inside the documentation layer. It is weaker once the assurance chain should enter implementation, CI, releases, and operations.

Missing depth:

- requirement-to-module mapping
- requirement-to-API/schema mapping
- requirement-to-test-result mapping
- release manifest ingestion
- runtime SLO/incident evidence linkage

Impact:

- good document-to-document consistency
- incomplete engineering assurance for real products

## 7. Hybrid Synchronization Is Still Narrow

Hybrid support is present, but not yet rich enough for large programs.

Missing depth:

- shared model across formal requirements, backlog items, design baselines, test results, controls, and release evidence
- bidirectional change propagation
- drift reporting between agile delivery and formal baselines

Impact:

- useful Hybrid structure
- continued manual coordination at scale

## 8. Domain Packs Are Useful But Not Full Rule Engines

The domain packs provide features, controls, obligations, evidence expectations, and reference guidance. They are valuable context sources.

Remaining gap:

- they are not yet comprehensive compliance engines with full control verification, mandatory evidence scoring, review workflow, and jurisdiction-specific clause proof.

Impact:

- domain-aware documentation is credible
- domain assurance still requires specialist review

## Summary of Gaps

### High Severity

- Missing proof workspace
- Engine suite failing from current checkout
- No clean committed project validation proof
- Missing requirements-to-code-to-run assurance chain

### Medium Severity

- 15 skill quick-validation failures
- 17 contract-gate warnings
- root/path documentation drift
- narrow Hybrid synchronization
- domain packs not yet rule engines

### Bottom-Line Gap

The project has moved from "documentation generator" to "documentation operating system with validation." To become world-class, it must now move from **validation machinery** to **reproducible assurance evidence**.
