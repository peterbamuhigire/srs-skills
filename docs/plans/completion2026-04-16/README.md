# Completion Plan — 2026-04-16

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement each sub-plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close every structural gap identified in the 2026-04-16 enterprise-grade gap analysis by converting the engine's normative prose into executable governance, without breaking any existing skill, project workspace, or build flow.

**Architecture:** A new Python package `engine/` becomes the **single canonical validation kernel** that loads any `projects/<ProjectName>/` workspace, builds a project-wide artifact graph, runs deterministic phase gates against it, and blocks downstream progression on failures unless a waiver is on file. All other gaps (path migration, hybrid sync, domain controls, enterprise artifacts, operator UX, demo project) plug into this kernel as data — gates, checks, registry entries — rather than as parallel validation logic.

**Tech Stack:** Python 3.11+, `pytest`, `ruamel.yaml`, `mistune` (markdown AST), `jsonschema`, `click` (CLI), Pandoc (existing). No new runtime services. CI via GitHub Actions + `pre-commit`.

---

## Map of Gaps to Sub-Plans

The gap analysis lists ten gap categories. Each is closed by exactly one sub-plan listed below. Where a gap touches two sub-plans, the primary owner is bolded.

| # | Gap (from analysis) | Severity | Owning sub-plan | Co-touched by |
|---|---|---|---|---|
| 1 | Enforcement Is Too Soft | High | **`01-validation-kernel.md`** | 02, 03 |
| 2 | Skill-Level Path Migration Incomplete | Medium | **`04-skill-pathing-migration.md`** | 01 |
| 3 | Hybrid Sync Weak | High | **`05-hybrid-synchronization.md`** | 01, 02 |
| 4 | Standards Compliance Not Proven | High | **`02-executable-phase-gates.md`** | 06 |
| 5 | Validation Layer Fragmented | High | **`01-validation-kernel.md`** | 02 |
| 6 | Domain Layer Not Deep Enough | Medium | **`06-domain-control-libraries.md`** | 02 |
| 7 | Output Consistency Risk | High | **`03-identifier-and-glossary-registry.md`** | 01 |
| 8 | Phase 09 Strong in Shape, Weak in Proof | Medium | **`02-executable-phase-gates.md`** | 07 |
| 9 | Missing Enterprise Capabilities (ADR, change-impact, baseline-delta, waivers, sign-off, evidence packs) | Medium | **`07-enterprise-artifacts.md`** | 01 |
| 10 | Too Dependent on Senior Human Operators | Medium | **`08-operator-experience.md`** | All |
| — | End-to-end proof that hybrid + regulated work together | — | **`09-end-to-end-proof-project.md`** | All |

---

## Sub-Plans

Each sub-plan stands alone — it produces a working, testable deliverable on its own. They share a build order because later plans reuse the kernel built in plan 01.

| Order | File | Deliverable | Depends on |
|---|---|---|---|
| 1 | `01-validation-kernel.md` | `engine/` Python package, CLI, artifact graph, check primitives, waiver loader, JUnit + SARIF reporters | — |
| 2 | `02-executable-phase-gates.md` | Phase 01–09 gates expressed as `engine.gates.phaseNN` Python modules with TDD coverage; existing prose `.md` files become specifications, not enforcement | 01 |
| 3 | `03-identifier-and-glossary-registry.md` | `_registry/identifiers.yaml` and `_registry/glossary.yaml` schemas, parsers that populate them from project artifacts, uniqueness + cross-reference checks | 01 |
| 4 | `04-skill-pathing-migration.md` | All skill-local files use canonical `projects/<ProjectName>/` pathing (or explicit alias notice); deterministic CI check that blocks future drift | 01 |
| 5 | `05-hybrid-synchronization.md` | New `hybrid-synchronization` skill that emits `_context/methodology.md`, baseline-to-backlog trace files, DoR/DoD bound to baseline IDs; gate enforcement in `engine.gates.hybrid` | 01, 03 |
| 6 | `06-domain-control-libraries.md` | `domains/<domain>/controls/` directory schema (control register, obligation map, evidence expectations, required reviews); kernel check `engine.checks.controls` | 01, 03 |
| 7 | `07-enterprise-artifacts.md` | New skills `architecture-decision-records`, `change-impact-analysis`, `baseline-delta`, `waiver-management`, `sign-off-ledger`, `evidence-pack-builder` under `09-governance-compliance/` plus matching kernel checks | 01, 03 |
| 8 | `08-operator-experience.md` | `engine doctor` pre-flight, scaffold golden defaults, `[CONTEXT-GAP]` autofill prompts, opinionated worked example next to every skill | 01, 02 |
| 9 | `09-end-to-end-proof-project.md` | `projects/_demo-hybrid-regulated/` worked example exercising every gate, every registry, every artifact type; CI runs the demo and asserts `ENGINE CONTRACT: PASS` | 01–08 |

---

## Sequencing and Parallelism

- **Strictly sequential:** Plan 01 must finish before any other plan starts. Every other plan calls into the kernel.
- **Parallel after 01:** Plans 02, 03, 04 can run in parallel. Plans 05, 06, 07 should wait for 03 (registry) and 02 (gate framework).
- **Plan 08** can run as soon as 02 is in place.
- **Plan 09** is the closer — it cannot be written until 01–08 are merged because it asserts behavior across all of them.

A reasonable single-engineer order is `01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09`. A parallelisable order with two engineers is `01`, then `(02 + 04)`, `(03 + 05 + 06)`, `(07 + 08)`, `09`.

---

## Out of Scope

The following deliberately stay out of this completion programme to keep the scope shippable:

1. **External rules engine.** No JSON-Logic, no OPA, no Drools. The kernel is plain Python. If we ever need a pluggable rule store, retrofit it later.
2. **GUI for the kernel.** CLI + JUnit/SARIF reports + Pandoc-rendered evidence packs only.
3. **Auto-generation of regulatory text.** The kernel checks that controls and verifications exist; it does not author the regulatory clauses themselves. Domain control libraries (Plan 06) seed those.
4. **Live integration with external GRC platforms.** Export formats (SARIF, CSV) are produced; integrations to ServiceNow / Vanta / Drata are out of scope.
5. **Re-architecting the existing skills.** Skill bodies are edited only for path migration (Plan 04), domain control hooks (Plan 06), and registry hooks (Plan 03 / 07). Their human-facing prose stays.

---

## Definition of Done for the Programme

The completion programme is done when **all** of the following are true and proven by automated checks:

1. `python -m engine validate projects/_demo-hybrid-regulated` exits `0` with `ENGINE CONTRACT: PASS`.
2. `python -m engine validate projects/_demo-hybrid-regulated --break-something` (a deliberate sabotage flag wired into the demo) exits non-zero with at least one specific gate name in the failure list.
3. `pytest engine/tests/` passes, with at least 90% line coverage of `engine/`.
4. `python scripts/validate_engine.py` (the legacy contract) still passes after delegation to `engine.cli`.
5. CI runs both the demo and the kernel test suite on every PR; failure blocks merge.
6. Every sub-plan's "Self-Review" checklist at the bottom of its file is checked off in a final commit.

---

## Conventions Followed by All Sub-Plans

- **TDD.** Every behaviour change is preceded by a failing test that describes it. Steps follow Red → verify Red → Green → verify Green → Commit.
- **Small commits.** Each task ends with a single commit named in the imperative mood (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`).
- **Exact paths.** Every step lists the absolute repo-relative path it touches.
- **No placeholders.** No `TODO`, no "implement later", no "similar to". If a step needs code, the code is in the step.
- **One concern per file.** Files do one thing; if a file grows past ~250 lines, split it.

---

## Self-Review of the README

- **Coverage:** Every gap (1–10) maps to exactly one owning sub-plan. The table is the contract.
- **Buildability:** The DoD has six measurable exit criteria. None are aspirational.
- **Sequencing:** Dependencies are explicit and the parallel-build option is laid out.
- **No placeholders:** No `TBD`. The Out-of-Scope list keeps later plans honest.
