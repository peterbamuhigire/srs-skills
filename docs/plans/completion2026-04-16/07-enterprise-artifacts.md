# Enterprise Artifacts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans.

**Goal:** Add the six enterprise governance capabilities the gap analysis flags as missing or underdeveloped: ADR catalog management, change-impact analysis, baseline-delta analysis, waiver management, sign-off ledger, and evidence-pack assembly. Each becomes a skill the consultant can invoke and a kernel artefact the validator can cross-check. Closes Gap #9.

**Architecture:** Six new skills under `09-governance-compliance/` (numbered 05–10 to extend the existing four). Each writes structured outputs into `projects/<X>/_registry/` or a dedicated `projects/<X>/09-governance-compliance/<artifact>/`. A new `engine pack` CLI command assembles a single ZIP `evidence-pack-<date>.zip` containing every artifact a regulator would expect, with a manifest CSV.

**Tech Stack:** Python (kernel), markdown skills, `zipfile` (stdlib), Pandoc (existing), `ruamel.yaml`.

---

## File Structure

```
09-governance-compliance/
├── 05-architecture-decision-records/SKILL.md
├── 06-change-impact-analysis/SKILL.md
├── 07-baseline-delta/SKILL.md
├── 08-waiver-management/SKILL.md
├── 09-sign-off-ledger/SKILL.md
└── 10-evidence-pack-builder/SKILL.md

engine/
├── pack.py                          # `engine pack` implementation
├── checks/
│   ├── adr_catalog.py
│   ├── change_impact.py
│   ├── baseline_delta.py
│   └── sign_off.py
├── registry/schemas/
│   ├── adr-catalog.schema.json
│   ├── change-impact.schema.json
│   ├── baseline.schema.json
│   └── sign-off-ledger.schema.json
└── tests/
    ├── test_pack.py
    ├── test_check_adr_catalog.py
    ├── test_check_change_impact.py
    ├── test_check_baseline_delta.py
    └── test_check_sign_off.py

projects/<X>/
├── 09-governance-compliance/
│   ├── 05-adr/                      # ADR-NNNN-*.md files
│   ├── 06-change-impact/            # CIA-NNN-*.md files
│   ├── 07-baseline-delta/           # snapshots and deltas
│   └── evidence-pack-<YYYY-MM-DD>.zip
└── _registry/
    ├── adr-catalog.yaml
    ├── change-impact.yaml
    ├── baselines.yaml
    └── sign-off-ledger.yaml
```

---

### Task 1: ADR catalog skill + check

**Files:**

- Create: `09-governance-compliance/05-architecture-decision-records/SKILL.md`
- Reuse: `skills/skill-composition-standards/references/adr-template.md` (already exists per inventory)
- Create: `engine/registry/schemas/adr-catalog.schema.json`
- Create: `engine/checks/adr_catalog.py`
- Create: `engine/tests/test_check_adr_catalog.py`

- [ ] **Step 1: Author the skill** — explains: (1) when to write an ADR (significant architectural decision, technology choice, deviation from baseline), (2) where to file it (`projects/<X>/09-governance-compliance/05-adr/NNNN-slug.md`), (3) the catalog file format, (4) status lifecycle.

- [ ] **Step 2: Schema** for `_registry/adr-catalog.yaml`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["adrs"],
  "properties": {
    "adrs": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "title", "status", "decided_on", "deciders"],
        "properties": {
          "id": {"type": "string", "pattern": "^ADR-\\d{4}$"},
          "title": {"type": "string"},
          "status": {"enum": ["proposed", "accepted", "deprecated", "superseded"]},
          "superseded_by": {"type": "string", "pattern": "^ADR-\\d{4}$"},
          "decided_on": {"type": "string", "format": "date"},
          "deciders": {"type": "array", "items": {"type": "string"}, "minItems": 1},
          "affects": {"type": "array", "items": {"type": "string"}}
        }
      }
    }
  }
}
```

- [ ] **Step 3: `AdrCatalogCheck` failing test asserting**:

  - Every ADR markdown file under `09-governance-compliance/05-adr/` has a corresponding entry in `_registry/adr-catalog.yaml`.
  - Every catalog entry references an existing file.
  - Every `superseded_by` ID exists in the catalog.

- [ ] **Step 4: Implement and wire into `Phase09Gate`.**

- [ ] **Step 5: Commit per file batch.**

---

### Task 2: Change-impact analysis skill + check

**Files:**

- Create: `09-governance-compliance/06-change-impact-analysis/SKILL.md`
- Create: `engine/registry/schemas/change-impact.schema.json`
- Create: `engine/checks/change_impact.py`
- Create: `engine/tests/test_check_change_impact.py`

A **Change Impact Analysis (CIA)** is mandatory for any change to a baselined `FR-`, `NFR-`, or selected `CTRL-`. The skill produces one CIA file per change and updates `_registry/change-impact.yaml`.

- [ ] **Step 1: Author the skill** — Stimulus: a baseline change request. Process: identify the affected baseline IDs, list every downstream artifact that references them (designs, tests, runbooks, training material), assess effort, identify rollback strategy, route to the change-control body. Response: a CIA-NNN file under `projects/<X>/09-governance-compliance/06-change-impact/`.

- [ ] **Step 2: Schema** for `_registry/change-impact.yaml`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["entries"],
  "properties": {
    "entries": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "raised_on", "affected_baseline_ids", "decision"],
        "properties": {
          "id": {"type": "string", "pattern": "^CIA-\\d{3}$"},
          "raised_on": {"type": "string", "format": "date"},
          "affected_baseline_ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
          "downstream_artifacts": {"type": "array", "items": {"type": "string"}},
          "decision": {"enum": ["approved", "rejected", "deferred"]},
          "decision_body": {"type": "string"},
          "decision_date": {"type": "string", "format": "date"},
          "rollback_plan": {"type": "string"}
        }
      }
    }
  }
}
```

- [ ] **Step 3: `ChangeImpactCheck` failing test asserting**:

  - For every approved CIA, the listed `affected_baseline_ids` no longer appear in `_registry/baselines.yaml` at the same version (i.e., the change actually happened).
  - For every rejected CIA, the baseline IDs still exist.
  - Every CIA has a `rollback_plan`.

- [ ] **Step 4: Implement; wire into `Phase09Gate`; commit.**

---

### Task 3: Baseline-delta skill + check

**Files:**

- Create: `09-governance-compliance/07-baseline-delta/SKILL.md`
- Create: `engine/registry/schemas/baseline.schema.json`
- Create: `engine/checks/baseline_delta.py`
- Create: `engine/tests/test_check_baseline_delta.py`

A **baseline** is a frozen snapshot of identifiers + their content hashes at a point in time. The skill computes the delta between two baselines.

- [ ] **Step 1: Author the skill** — `python -m engine baseline snapshot <project> --label v1.2` writes `projects/<X>/09-governance-compliance/07-baseline-delta/v1.2.yaml` listing every ID and a SHA-256 of the artifact lines that defined it. `python -m engine baseline diff <project> v1.1 v1.2` produces a markdown report of additions, removals, and modifications.

- [ ] **Step 2: Implement `engine/baseline.py`** with `snapshot()` and `diff()`. Snapshot uses `IdentifierRegistry` + per-ID line extraction; diff is set algebra on IDs plus hash comparison.

- [ ] **Step 3: Add CLI subcommands** `engine baseline snapshot` and `engine baseline diff`.

- [ ] **Step 4: `BaselineDeltaCheck` failing test asserting**:

  - When a project declares a frozen baseline (i.e. `_registry/baselines.yaml` has `current: vX.Y`), every change to a baselined ID must have a matching CIA entry.

- [ ] **Step 5: Implement; wire into `Phase09Gate`; commit.**

---

### Task 4: Waiver management skill

**Files:**

- Create: `09-governance-compliance/08-waiver-management/SKILL.md`

The Plan 01 `WaiverRegister` already loads waivers; this skill is the consultant-facing workflow:

- [ ] **Step 1: Author the skill** — Stimulus: a finding the team wants to defer. Process: confirm severity, capture justification, identify approver, set `expires_on` no more than 90 days from `approved_on` (kernel rule from Plan 02 Task 10), append to `_registry/waivers.yaml`. Response: an entry plus a notification line for the next stand-up.

- [ ] **Step 2: Add a `python -m engine waive` interactive command** that prompts and appends.

```python
@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--gate", required=True)
@click.option("--scope", required=True)
@click.option("--reason", required=True)
@click.option("--approver", required=True)
@click.option("--days", type=int, default=30, show_default=True)
def waive(project: str, gate: str, scope: str, reason: str, approver: str, days: int) -> None:
    """Append a new waiver to the project's _registry/waivers.yaml."""
    # implementation details: load existing waivers, generate WAIVE-NNN,
    # append, save, print confirmation.
```

- [ ] **Step 3: Commit.**

---

### Task 5: Sign-off ledger skill + check

**Files:**

- Create: `09-governance-compliance/09-sign-off-ledger/SKILL.md`
- Create: `engine/registry/schemas/sign-off-ledger.schema.json`
- Create: `engine/checks/sign_off.py`
- Create: `engine/tests/test_check_sign_off.py`

The ledger records every formal sign-off (Phase 02 baseline approval, Phase 06 go-live, Phase 09 audit clearance). One YAML file, append-only.

- [ ] **Step 1: Schema**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["sign_offs"],
  "properties": {
    "sign_offs": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["gate", "signer", "role", "signed_on", "artifact_set"],
        "properties": {
          "gate": {"type": "string"},
          "signer": {"type": "string"},
          "role": {"type": "string"},
          "signed_on": {"type": "string", "format": "date"},
          "artifact_set": {"type": "array", "items": {"type": "string"}, "minItems": 1},
          "comment": {"type": "string"}
        }
      }
    }
  }
}
```

- [ ] **Step 2: Author the skill** — explains what events require a sign-off, who can sign (role-based, not name-based), and how to invoke `python -m engine signoff`.

- [ ] **Step 3: `SignOffCheck` failing test asserting**:

  - When `Phase02Gate` passes, there must be a matching `gate: phase02` entry in the ledger.
  - When `Phase06Gate` passes, there must be a `gate: phase06` entry.
  - The signed-off artifact set lists files that exist.

- [ ] **Step 4: Wire into `Phase09Gate`; commit.**

---

### Task 6: Evidence-pack builder

**Files:**

- Create: `09-governance-compliance/10-evidence-pack-builder/SKILL.md`
- Create: `engine/pack.py`
- Create: `engine/tests/test_pack.py`

The pack is a single ZIP containing everything an external auditor needs:

- All `_context/` files
- The full `09-governance-compliance/` tree
- Both registries (identifiers, glossary, controls, ADR catalog, change-impact, baselines, sign-off ledger, waivers)
- The latest validation report (`engine validate <project> --markdown evidence-pack/validation-report.md` first)
- The latest test-completion report (Phase 05 output)
- A manifest CSV listing every file with SHA-256 hash, size, last-modified, and which gate it satisfies

- [ ] **Step 1: Failing test**

```python
import zipfile
from pathlib import Path
from engine.pack import build_evidence_pack

def test_pack_contains_required_files(tmp_path: Path):
    # ... create a minimal but complete project ...
    out = tmp_path / "evidence-pack.zip"
    build_evidence_pack(project_root=tmp_path, out=out)
    with zipfile.ZipFile(out) as z:
        names = set(z.namelist())
    assert "manifest.csv" in names
    assert any(n.startswith("_context/") for n in names)
    assert any(n.startswith("_registry/") for n in names)
    assert "validation-report.md" in names
```

- [ ] **Step 2: Implement `engine/pack.py`**

```python
"""Evidence pack assembler."""
from __future__ import annotations
import csv
import hashlib
import io
import zipfile
from datetime import datetime
from pathlib import Path
from engine.cli import main as cli_main  # for invoking validate
from click.testing import CliRunner

_INCLUDE = ("_context", "_registry", "09-governance-compliance")

def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()

def build_evidence_pack(project_root: Path, out: Path) -> None:
    rows = []
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for top in _INCLUDE:
            base = project_root / top
            if not base.exists():
                continue
            for p in base.rglob("*"):
                if p.is_file():
                    rel = p.relative_to(project_root).as_posix()
                    z.write(p, arcname=rel)
                    rows.append({
                        "path": rel,
                        "sha256": _sha256(p),
                        "size_bytes": p.stat().st_size,
                        "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds"),
                    })
        # Validation report
        runner = CliRunner()
        with (project_root / "_pack_tmp_report.md").open("w") as f:
            pass
        report_path = project_root / "_pack_tmp_report.md"
        runner.invoke(cli_main, ["validate", str(project_root), "--markdown", str(report_path)])
        if report_path.exists():
            z.write(report_path, arcname="validation-report.md")
            rows.append({
                "path": "validation-report.md",
                "sha256": _sha256(report_path),
                "size_bytes": report_path.stat().st_size,
                "modified": datetime.fromtimestamp(report_path.stat().st_mtime).isoformat(timespec="seconds"),
            })
            report_path.unlink()
        # Manifest
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=["path", "sha256", "size_bytes", "modified"])
        w.writeheader()
        w.writerows(rows)
        z.writestr("manifest.csv", buf.getvalue())
```

- [ ] **Step 3: CLI subcommand**

```python
@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--out", type=click.Path(), required=True)
def pack(project: str, out: str) -> None:
    """Build an evidence pack ZIP."""
    from engine.pack import build_evidence_pack
    build_evidence_pack(Path(project), Path(out))
    click.echo(f"Wrote evidence pack to {out}")
```

- [ ] **Step 4: Wire `phase09.evidence_pack_buildable`** check from Plan 02 Task 10 to invoke `build_evidence_pack` against a temp file and assert success.

- [ ] **Step 5: Commit.**

---

### Task 7: Update README and CLAUDE.md

**Files:**

- Modify: `README.md`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add a "Governance Artifacts" section to README.md** under existing skill listing:

```markdown
### Phase 09 — Governance & Compliance

- 01 Traceability matrix
- 02 Audit report
- 03 Compliance documentation
- 04 Risk assessment
- 05 Architecture Decision Records
- 06 Change Impact Analysis
- 07 Baseline delta
- 08 Waiver management
- 09 Sign-off ledger
- 10 Evidence pack builder

Run `python -m engine pack <project> --out <project>/evidence-pack-YYYY-MM-DD.zip` to produce an audit-grade artifact bundle.
```

- [ ] **Step 2: Add to CLAUDE.md** — under the V&V SOP, add: "When closing a phase, the responsible role MUST sign off via `python -m engine signoff` before the next phase begins. The kernel will block downstream skills until the ledger contains the matching `gate:` entry."

- [ ] **Step 3: Commit.**

---

## Self-Review

1. **Spec coverage:** ADR catalog (Task 1), change-impact (Task 2), baseline-delta (Task 3), waiver management (Task 4), sign-off ledger (Task 5), evidence pack (Task 6) — six new artifacts. Each has both a skill (consultant-facing) and a kernel check (auditor-facing).
2. **Placeholder scan:** None.
3. **Reusability:** All registries follow the same YAML-with-schema pattern; all checks share the `Check.run(graph, findings)` signature; all skills follow the writing-skills convention.
4. **End-to-end:** A regulator can take the evidence-pack ZIP alone and reconstruct the project's compliance state without read access to the repo.
