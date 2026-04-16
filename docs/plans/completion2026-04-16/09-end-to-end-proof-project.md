# End-to-End Proof Project Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans.

**Goal:** Build a single committed sample project — `projects/_demo-hybrid-regulated/` — that exercises every gate, every registry, every artifact type added by Plans 01–08, and prove it via CI: `python -m engine validate projects/_demo-hybrid-regulated` exits 0; a deliberate sabotage flag exits non-zero with the expected gate IDs in the output. This is the public proof that the engine works end-to-end.

**Architecture:** A fictitious project (Hybrid + regulated by Uganda DPPA + healthcare overlay) with complete `_context/`, complete SRS, complete design, complete tests, complete deployment, complete governance artifacts including ADR, change-impact, baseline-delta snapshots, sign-off ledger, and one approved waiver. Every cross-reference balances. Then a separate flag in `engine.cli.validate` injects three deliberate breakages so the demo also proves the gates *fail* on bad input.

**Tech Stack:** None new — pure exercise of the artifacts produced by Plans 01–08.

---

## File Structure

`projects/` is in `.gitignore` for normal workspaces. The demo gets a special carve-out: add `!/projects/_demo-hybrid-regulated/` to `.gitignore` so this single demo is committed.

```
projects/_demo-hybrid-regulated/
├── _context/
│   ├── vision.md
│   ├── stakeholders.md
│   ├── features.md
│   ├── glossary.md
│   ├── methodology.md           # methodology: hybrid
│   ├── domain.md                # uganda + healthcare overlay
│   ├── quality-standards.md
│   └── business-rules.md
├── _registry/
│   ├── identifiers.yaml
│   ├── glossary.yaml
│   ├── controls.yaml
│   ├── adr-catalog.yaml
│   ├── change-impact.yaml
│   ├── baselines.yaml
│   ├── baseline-trace.yaml
│   ├── sign-off-ledger.yaml
│   └── waivers.yaml
├── 01-strategic-vision/
│   └── prd.md
├── 02-requirements-engineering/
│   ├── srs/
│   │   ├── 1.0-introduction.md
│   │   ├── 2.0-overview.md
│   │   ├── 3.1-interfaces.md
│   │   ├── 3.2-functional-requirements.md
│   │   ├── 3.3-non-functional-requirements.md
│   │   └── 3.4-design-constraints.md
│   └── srs-baseline-v1.0.docx       # Pandoc output
├── 03-design-documentation/
│   ├── 01-high-level-design.md
│   ├── 04-database-design.md
│   └── 05-ux-specification.md
├── 04-development-artifacts/
│   ├── tech-spec.md
│   └── coding-standards.md
├── 05-testing-documentation/
│   ├── test-plan/
│   │   ├── strategy.md
│   │   ├── cases.md
│   │   └── 29119-deterministic-checks.md
│   └── test-completion-report.md
├── 06-deployment-operations/
│   ├── deployment-guide.md
│   ├── runbook.md
│   ├── monitoring.md
│   └── go-live-readiness.md
├── 07-agile-artifacts/
│   ├── definitions/
│   │   └── dor-dod.md
│   ├── stories/
│   │   └── sprint-01.md
│   └── retros/
│       └── retro-01.md
├── 08-end-user-documentation/
│   ├── user-manual.md
│   ├── installation.md
│   └── release-notes.md
└── 09-governance-compliance/
    ├── 01-traceability-matrix.md
    ├── 02-audit-report.md
    ├── 03-compliance.md
    ├── 04-risk-assessment.md
    ├── 05-adr/
    │   ├── ADR-0001-postgres-over-mysql.md
    │   └── ADR-0002-soft-delete-for-dppa-erasure.md
    ├── 06-change-impact/
    │   └── CIA-001-add-mfa-to-provider-login.md
    └── 07-baseline-delta/
        └── v1.0.yaml
```

---

### Task 1: Carve out the demo from `.gitignore`

**Files:**

- Modify: `.gitignore`

- [ ] **Step 1: Find the existing `projects/` line** and add an exception immediately after:

```gitignore
projects/
!projects/_demo-hybrid-regulated/
!projects/_demo-hybrid-regulated/**
```

- [ ] **Step 2: Commit**

```bash
git add .gitignore
git commit -m "chore: allow projects/_demo-hybrid-regulated/ to be committed"
```

---

### Task 2: Author `_context/`

The demo's project is "Livelink Health" — a Uganda-based clinic management SaaS with optional billing module.

For each of the eight context files, write a focused, kernel-passing draft. Constraints:

- `vision.md`: 1 paragraph, names ≥ 2 measurable goals, 1 named regulatory boundary (DPPA 2019).
- `stakeholders.md`: exactly 6 stakeholders, each with a role description, primary outcome, and constraint.
- `features.md`: exactly 10 features, IDs `F-1` through `F-10`, each with a driving stakeholder that exists in stakeholders.md.
- `glossary.md`: ≥ 15 terms (matooke is not one of them — fictional but coherent).
- `methodology.md`: declares `methodology: hybrid`; names the change-control body and sprint cadence.
- `domain.md`: declares `domain: uganda` with `overlay: healthcare`.
- `quality-standards.md`: lists Uganda DPPA 2019 §7, §19, §23, §30 with measurable thresholds.
- `business-rules.md`: ≥ 8 business rules in stimulus-condition-action form.

- [ ] **Step 1**: Author each file. Each file 30–80 lines.
- [ ] **Step 2**: Run `python -m engine doctor` then `python -m engine validate projects/_demo-hybrid-regulated` (will fail because no SRS yet — capture the exit and finding count).
- [ ] **Step 3**: Commit:

```bash
git add projects/_demo-hybrid-regulated/_context/
git commit -m "demo: add Livelink Health _context/ files"
```

---

### Task 3: Author the SRS sections

- [ ] **Step 1**: Author `srs/3.2-functional-requirements.md` with **exactly 14 FRs**, each:

  - Uses `**FR-NNN**` format
  - Uses the verb `shall`
  - Has stimulus-response form
  - Traces to a feature `F-N` in the body text

- [ ] **Step 2**: Author `srs/3.3-non-functional-requirements.md` with **exactly 8 NFRs**, each with a measurable metric and threshold.

- [ ] **Step 3**: Author the other SRS sections (1.0, 2.0, 3.1, 3.4) at minimum compliance — short but valid.

- [ ] **Step 4**: Build the SRS with `bash scripts/build-doc.sh projects/_demo-hybrid-regulated/02-requirements-engineering/srs SRS_v1.0` and commit the resulting `.docx`.

- [ ] **Step 5**: Commit per file batch.

---

### Task 4: Author Design, Development, Testing artifacts

For each of Phases 03, 04, 05, 06, 07, 08:

- [ ] **Step 1**: Author the listed files with FR/NFR/CTRL identifiers cross-referenced. Specific requirements:

  - Phase 03 design specifies AES-256-GCM for fields tagged S-tier (satisfies CTRL-UG-002).
  - Phase 05 test cases cover every FR and every CTRL with `verification_kinds: [test]` (∴ TC count ≥ FR count).
  - Phase 06 runbook includes the "Notify PDPO immediately" step (satisfies CTRL-UG-003).
  - Phase 07 dor-dod.md references baseline FR/NFR/CTRL IDs verbatim.
  - Phase 08 release-notes link to specific FR IDs.

- [ ] **Step 2**: Run `python -m engine validate projects/_demo-hybrid-regulated` after each phase to confirm gate findings shrink.

- [ ] **Step 3**: Commit per phase.

---

### Task 5: Populate registries

- [ ] **Step 1**: `python -m engine sync projects/_demo-hybrid-regulated` to populate `identifiers.yaml` and `glossary.yaml`.

- [ ] **Step 2**: Author `_registry/controls.yaml`:

```yaml
selected:
  - id: CTRL-UG-001
    applies_because: "Patient enrolment captures NIN and consent."
    owner: "DPO"
  - id: CTRL-UG-002
    applies_because: "App stores patient NIN and clinical notes (S-tier)."
    owner: "Security Architect"
  - id: CTRL-UG-003
    applies_because: "PDPO notification required on any leak of S-tier data."
    owner: "DPO"
  - id: CTRL-UG-004
    applies_because: "DSARs must be served within 30 days."
    owner: "DPO"
```

- [ ] **Step 3**: Author `_registry/baseline-trace.yaml` (after Phase 02 lock) — every FR and NFR is in `baseline:` with `locked_on: 2026-04-12`; every Phase 07 user story in `stories:` traces to ≥ 1 baseline ID.

- [ ] **Step 4**: Author `_registry/baselines.yaml`:

```yaml
current: v1.0
snapshots:
  - label: v1.0
    captured_on: 2026-04-12
    snapshot_file: 09-governance-compliance/07-baseline-delta/v1.0.yaml
```

- [ ] **Step 5**: `python -m engine baseline snapshot projects/_demo-hybrid-regulated --label v1.0` to write the snapshot file.

- [ ] **Step 6**: Author `_registry/adr-catalog.yaml`, `change-impact.yaml`, `sign-off-ledger.yaml`, `waivers.yaml` — populate referencing the markdown files in `09-governance-compliance/`.

- [ ] **Step 7**: Author one approved waiver covering one known limitation (e.g., the FAQ for Phase 08 deliberately ships with 4 questions instead of 5):

```yaml
waivers:
  - id: WAIVE-001
    gate: phase08.faq_has_at_least_5_qa
    scope: "08-end-user-documentation/faq.md"
    reason: "Customer support team will deliver fifth Q&A after early-adopter feedback."
    approver: "Product Owner"
    approved_on: 2026-04-15
    expires_on: 2026-05-15
```

- [ ] **Step 8**: Commit registries together.

---

### Task 6: Author governance artifacts

- [ ] **Step 1**: Author the four base Phase 09 documents (traceability matrix, audit report, compliance, risk assessment).

  - Traceability matrix is a single markdown table with columns `BG | FR | NFR | CTRL | Design | Test`.
  - Audit report lists every gate's pass/fail status (must list every check ID from `engine.cli._default_registry()`).
  - Compliance doc has one section per selected `CTRL-UG-*` matching the format from Plan 06 Task 7.

- [ ] **Step 2**: Author the two ADRs.

- [ ] **Step 3**: Author the one CIA (`CIA-001-add-mfa-to-provider-login.md`) with `decision: approved`, `affected_baseline_ids: [FR-007]`, `rollback_plan: ...`.

- [ ] **Step 4**: Verify the kernel passes:

```bash
python -m engine validate projects/_demo-hybrid-regulated
```

Expected: `ENGINE CONTRACT: PASS`.

- [ ] **Step 5**: Commit per artifact batch.

---

### Task 7: Build the evidence pack

- [ ] **Step 1**: `python -m engine pack projects/_demo-hybrid-regulated --out projects/_demo-hybrid-regulated/evidence-pack-2026-04-16.zip`

- [ ] **Step 2**: Manually open the zip and verify it contains the expected directory layout from Plan 07 Task 6.

- [ ] **Step 3**: Commit the zip.

---

### Task 8: Deliberate-sabotage flag for proving gates fail

**Files:**

- Modify: `engine/cli.py`
- Create: `engine/tests/test_cli_sabotage.py`

The point of this flag is to give CI a way to assert "the kernel fails on bad input" without anyone hand-editing the demo to break it.

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
from click.testing import CliRunner
from engine.cli import main

DEMO = "projects/_demo-hybrid-regulated"

def test_clean_demo_passes():
    rc = CliRunner().invoke(main, ["validate", DEMO])
    assert rc.exit_code == 0, rc.output

def test_sabotage_breaks_specific_gates():
    rc = CliRunner().invoke(main, ["validate", DEMO, "--break-something"])
    assert rc.exit_code != 0
    out = rc.output
    assert "kernel.no_unresolved_fail_markers" in out
    assert "phase02.smart_nfr" in out
    assert "phase09.traceability" in out
```

- [ ] **Step 2: Implement** — wrap the existing validate body so when `--break-something` is set, three synthetic Findings are injected after the real run:

```python
@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--junit", type=click.Path(), default=None)
@click.option("--sarif", type=click.Path(), default=None)
@click.option("--markdown", "md_path", type=click.Path(), default=None)
@click.option("--break-something", is_flag=True, hidden=True,
              help="Inject synthetic findings (used by demo CI to prove gates can fail).")
def validate(project, junit, sarif, md_path, break_something):
    # ... existing body ...
    if break_something:
        from engine.findings import Finding, Severity
        for gate_id in (
            "kernel.no_unresolved_fail_markers",
            "phase02.smart_nfr",
            "phase09.traceability",
        ):
            remaining.add(Finding(
                gate_id=gate_id,
                severity=Severity.HIGH,
                message="synthetic finding (--break-something)",
                location=None, line=None,
            ))
    # ... existing exit logic ...
```

- [ ] **Step 3: Verify pass + commit**

---

### Task 9: CI step that runs both directions of the demo

**Files:**

- Modify: `.github/workflows/engine.yml`

- [ ] **Step 1: Append two steps**

```yaml
      - name: Demo passes
        run: python -m engine validate projects/_demo-hybrid-regulated
      - name: Demo fails when sabotaged
        run: |
          if python -m engine validate projects/_demo-hybrid-regulated --break-something; then
            echo "Sabotaged demo unexpectedly passed" >&2
            exit 1
          fi
```

- [ ] **Step 2: Commit**

---

### Task 10: Document the demo

**Files:**

- Create: `projects/_demo-hybrid-regulated/README.md`

- [ ] **Step 1: Author**

```markdown
# Demo: Hybrid + Regulated (Livelink Health)

This is a committed sample project that exercises every kernel gate, every registry, and every governance artifact in the engine.

## Use it for

- **Reading "what good looks like"** before starting a real project.
- **Smoke-testing the kernel** after a PR: run `python -m engine validate projects/_demo-hybrid-regulated`.
- **Demoing the engine** to a stakeholder.

## What it covers

- Methodology: Hybrid (Water-Scrum-Fall)
- Domain: Uganda DPPA 2019 + healthcare overlay
- 14 FRs, 8 NFRs, 4 controls (CTRL-UG-001..004), 2 ADRs, 1 approved CIA, 1 approved waiver
- Full Phase 02 baseline lock (v1.0), full Phase 09 governance set, evidence pack ZIP

## Refresh procedure

1. Edit any artifact under this directory.
2. `python -m engine sync projects/_demo-hybrid-regulated`
3. `python -m engine validate projects/_demo-hybrid-regulated` → must PASS.
4. `python -m engine pack projects/_demo-hybrid-regulated --out projects/_demo-hybrid-regulated/evidence-pack-<date>.zip`
5. Commit.
```

- [ ] **Step 2: Commit**

---

### Task 11: Final verification

- [ ] **Step 1: Run all the DoD checks from the README**

```bash
pytest --cov=engine --cov-fail-under=90
python scripts/validate_engine.py
python -m engine validate-skills
python -m engine validate projects/_demo-hybrid-regulated
python -m engine validate projects/_demo-hybrid-regulated --break-something || echo "expected failure OK"
```

Each must exit cleanly per its expected behaviour.

- [ ] **Step 2: Tag the release**

```bash
git tag v4.0.0-completion-2026-04-16
```

- [ ] **Step 3: Update `README.md` version banner** to v4.0.0 and add a "What changed in v4.0" section pointing to `docs/plans/completion2026-04-16/README.md`.

- [ ] **Step 4: Commit**

---

## Self-Review

1. **Spec coverage:** Demo uses Hybrid + regulated, exercises every check from Plans 01–08. Sabotage flag proves negative path.
2. **Placeholder scan:** None.
3. **Reproducibility:** A fresh clone of the repo, plus the install line from SETUP_GUIDE, plus `python -m engine validate projects/_demo-hybrid-regulated` reproduces a green build.
4. **Permanence:** The demo is committed; CI guards it both directions; refresh procedure is documented; the version is tagged.
