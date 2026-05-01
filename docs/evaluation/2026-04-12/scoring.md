# Scoring

## Scorecard

| Dimension | Score | Rationale |
|---|---:|---|
| Coverage | 9/10 | The repository covers the full SDLC: strategy, requirements, design, development artifacts, testing, deployment, agile operations, end-user documentation, governance, domains, and reusable technical skills. The deduction is for uneven depth and weak implementation/runtime traceability. |
| Standards Alignment | 8/10 | Standards are not merely named; deterministic gate docs and `docs/standards-clause-registry.md` exist, and the engine has clause-linked findings. The deduction remains because clause-level proof is uneven and not yet complete across every artifact type and domain. |
| Methodology Support | 8/10 | Waterfall, Agile, and Hybrid are all represented. Hybrid has explicit documentation and validation logic. The deduction is for a still-thin shared model between formal requirements, agile artifacts, design baselines, governance evidence, and runtime evidence. |
| Instruction Quality | 8/10 | The skill layer is broad, mostly valid, and often operational. However, 15 of 240 `SKILL.md` files fail the repo quick validator, and root/path guidance still contains drift around `skills/world-class-engineering` versus `skills/skills/world-class-engineering`. |
| System Flow | 8/10 | The intended flow is coherent: scaffold, populate `_context`, sync registries, validate, waive/sign off, baseline, pack. The deduction is for missing committed proof workspace and unclean validation of visible project workspaces. |
| Validation & Governance | 8/10 | The kernel is real and strong, and `scripts/validate_engine.py` passes. But the full suite currently fails 2 tests because `projects/_demo-hybrid-regulated` is missing, so the governance proof chain is not clean. |
| AI Integration | 6/10 | The repository has many AI skills and AI-aware guidance, but the core kernel does not yet provide first-class AI evaluation, prompt/model regression testing, drift control, hallucination scoring, or AI output provenance. |
| Real-World Usability | 8/10 | A disciplined team can use the repo today as a serious documentation and delivery accelerator. Setup requires installing dev dependencies, and high-stakes use still requires expert review and manual assurance. |
| Output Quality Potential | 8/10 | The repository can produce high-quality SDLC artifacts when operated well. The deduction is for incomplete semantic assurance, missing clean project proof, incomplete skill normalization, and lack of requirements-to-code-to-run evidence. |

## Overall Score

**8.1 / 10**

## Why The Score Changed

The previous evaluation gave **8.4 / 10** and stated that:

- the full engine test suite passed
- coverage was 96%
- `projects/_demo-hybrid-regulated` existed and validated cleanly

The current checkout does not support those claims:

- full engine test run: 211 tests, 2 failures, 2 skips
- coverage: 95%
- failure cause: missing `projects/_demo-hybrid-regulated`
- visible project validation: `projects\AcademiaPro` returns multiple HIGH findings

The score therefore drops to **8.1 / 10**. The project remains strong because the engine and skill system are real, but the evidence chain has regressed.

## Score Justification by Theme

### Validation Kernel

The engine deserves a high score for actual implemented capabilities:

- CLI command surface
- phase gates
- artifact graphing
- identifier and glossary registries
- waiver and sign-off handling
- baseline snapshot and diff support
- evidence-pack assembly
- JUnit, Markdown, and SARIF reporters
- checks for traceability, NFR quality, ADRs, controls, obligations, compliance evidence, test oracles, and design sufficiency

The limitation is proof hygiene, not absence of machinery.

### Skill Catalog

The skill system is large and mostly valid:

- 240 total `SKILL.md` files
- 225 pass quick validation
- 15 fail quick validation
- 226 evidence contracts scanned by contract gate
- 0 contract errors, 17 warnings, 10 exempt

This is strong but not clean enough for a world-class portable skill system.

### Project Proof

This is the weakest current proof area. The repo references a canonical demo project that is absent, and at least one visible project workspace does not validate cleanly. A world-class engine needs one or more committed green proof workspaces.

### Standards and Auditability

The standards story is above average because the repository has a clause registry and deterministic gate documents. It is not yet audit-grade because the engine still emphasizes structure and linkage more than full substantive correctness, implementation evidence, and runtime observation.

### AI Layer

AI skills are broad, but AI quality control is not deeply integrated into the kernel. AI-generated documentation can be constrained after generation, but there is no central model/prompt evaluation loop, hallucination register, or regression harness.

## Current Maturity Band

**Strong enterprise-oriented internal platform.**

Not yet:

- a self-proving audit engine
- a complete requirements-to-code-to-runtime assurance graph
- a fully normalized portable skill catalog
- a green end-to-end proof distribution
