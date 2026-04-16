# Hybrid Synchronization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans.

**Goal:** Build a `hybrid-synchronization` skill plus a `HybridSyncGate` that together turn the current Hybrid prose contract into enforced reality — emitting `_context/methodology.md`, a baseline-to-backlog trace file, and DoR/DoD definitions that quote baseline IDs verbatim. Ensures Agile stories cannot silently drift from a Waterfall baseline. Closes Gap #3.

**Architecture:** A new top-level skill at `02-requirements-engineering/hybrid/hybrid-synchronization/SKILL.md` (parallel to `waterfall/` and `agile/`) generates three outputs: `methodology.md`, `baseline-trace.yaml`, `dor-dod.md`. A new `engine/gates/hybrid.py` enforces:

1. Every Agile US has a `traces:` field listing at least one baselined `FR-`/`NFR-` ID.
2. Every baselined `FR-` is either implemented in at least one US or appears in the `change-log.md` with a documented decision.
3. DoR/DoD reference compliance constraints from `_context/quality-standards.md` by ID.

**Tech Stack:** Skill = markdown + python helper templates. Gate = Python (kernel).

---

## File Structure

```
02-requirements-engineering/hybrid/
├── README.md
├── hybrid-synchronization/
│   ├── SKILL.md
│   ├── manifest.md
│   ├── templates/
│   │   ├── methodology.md.j2
│   │   ├── baseline-trace.yaml.j2
│   │   └── dor-dod.md.j2
│   └── references/
│       └── water-scrum-fall-patterns.md
engine/gates/hybrid.py
engine/checks/hybrid_traces.py
engine/tests/test_check_hybrid_traces.py
engine/tests/test_gate_hybrid.py
docs/deterministic-gate-hybrid.md   # New prose gate doc
```

---

### Task 1: Author the hybrid-synchronization skill

**Files:**

- Create: `02-requirements-engineering/hybrid/README.md`
- Create: `02-requirements-engineering/hybrid/hybrid-synchronization/SKILL.md`
- Create: `02-requirements-engineering/hybrid/hybrid-synchronization/manifest.md`
- Create: `02-requirements-engineering/hybrid/hybrid-synchronization/references/water-scrum-fall-patterns.md`
- Create three template files under `templates/`.

- [ ] **Step 1: Author `02-requirements-engineering/hybrid/README.md`**

Brief landing page that explains when to use Hybrid (refer to `docs/hybrid-operating-model.md`) and lists the available skills.

- [ ] **Step 2: Author the SKILL.md** — must follow `superpowers:writing-skills` conventions:

```markdown
---
name: hybrid-synchronization
description: Use when a project is Hybrid (Water-Scrum-Fall). Generates _context/methodology.md, _registry/baseline-trace.yaml, and 07-agile-artifacts/definitions/dor-dod.md so Agile execution stays bound to the Waterfall baseline.
---

# Hybrid Synchronization

## When to use

Invoke after Phase 02 Waterfall SRS is signed off and before the team starts sprint planning. Skip if the project is pure Waterfall or pure Agile.

## Inputs

Read from `projects/<ProjectName>/_context/`:

- `vision.md`
- `features.md`
- `quality-standards.md`
- `methodology.md` (if it exists; otherwise generate from prompts below)

Read from `projects/<ProjectName>/02-requirements-engineering/`:

- the SRS section files (any `*.md` with phase frontmatter `02`)

## Stimulus / Process / Response

1. Read inputs above.
2. Extract every baselined `FR-` and `NFR-` from the SRS sections.
3. Prompt the consultant for: (a) the change-control body, (b) the cadence (sprint length), (c) which features are baseline-locked vs flexible.
4. Render each template with the gathered values:
   - `methodology.md` → write to `projects/<ProjectName>/_context/methodology.md`
   - `baseline-trace.yaml` → write to `projects/<ProjectName>/_registry/baseline-trace.yaml`
   - `dor-dod.md` → write to `projects/<ProjectName>/07-agile-artifacts/definitions/dor-dod.md`
5. Run `python -m engine validate <project>` and report the result.

## Output Contract

After running this skill, the kernel's `HybridSyncGate` MUST pass. If it does not, do not proceed to Phase 07.
```

- [ ] **Step 3: Author the three Jinja-style templates** with placeholders that match the variables the SKILL.md prompts for. Keep them under 80 lines each.

- [ ] **Step 4: Author `references/water-scrum-fall-patterns.md`** summarising the three patterns from `docs/hybrid-operating-model.md` and citing it.

- [ ] **Step 5: Commit**

```bash
git add 02-requirements-engineering/hybrid/
git commit -m "feat(skills): add hybrid-synchronization skill"
```

---

### Task 2: Baseline trace YAML schema

**Files:**

- Create: `engine/registry/schemas/baseline-trace.schema.json`

- [ ] **Step 1: Schema**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["baseline", "stories"],
  "properties": {
    "baseline": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "locked_on"],
        "properties": {
          "id": {"type": "string", "pattern": "^(FR|NFR)-\\d{3,5}$"},
          "locked_on": {"type": "string", "format": "date"},
          "change_control_body": {"type": "string"}
        }
      }
    },
    "stories": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "traces"],
        "properties": {
          "id": {"type": "string", "pattern": "^US-\\d{3,5}$"},
          "traces": {
            "type": "array",
            "items": {"type": "string", "pattern": "^(FR|NFR)-\\d{3,5}$"},
            "minItems": 1
          },
          "delta_to_baseline": {"type": "string"}
        }
      }
    }
  }
}
```

- [ ] **Step 2: Commit**

---

### Task 3: `HybridTracesCheck`

**Files:**

- Create: `engine/checks/hybrid_traces.py`
- Create: `engine/tests/test_check_hybrid_traces.py`

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
import pytest
from engine.findings import FindingCollection
from engine.checks.hybrid_traces import HybridTracesCheck

def _trace(tmp_path: Path, body: str) -> Path:
    p = tmp_path / "baseline-trace.yaml"
    p.write_text(body)
    return p

def test_passes_when_every_story_traces_to_baseline(tmp_path: Path):
    p = _trace(tmp_path, """\
baseline:
  - id: FR-001
    locked_on: 2026-04-01
    change_control_body: Steering Committee
stories:
  - id: US-001
    traces: [FR-001]
""")
    findings = FindingCollection()
    HybridTracesCheck("phasehybrid.traces", p).run(None, findings)
    assert len(findings) == 0

def test_flags_orphan_baseline_item(tmp_path: Path):
    p = _trace(tmp_path, """\
baseline:
  - id: FR-001
    locked_on: 2026-04-01
    change_control_body: Steering Committee
  - id: FR-002
    locked_on: 2026-04-01
    change_control_body: Steering Committee
stories:
  - id: US-001
    traces: [FR-001]
""")
    findings = FindingCollection()
    HybridTracesCheck("phasehybrid.traces", p).run(None, findings)
    msgs = [f.message for f in findings]
    assert any("FR-002" in m for m in msgs)

def test_flags_unknown_trace_target(tmp_path: Path):
    p = _trace(tmp_path, """\
baseline:
  - id: FR-001
    locked_on: 2026-04-01
    change_control_body: SC
stories:
  - id: US-001
    traces: [FR-999]
""")
    findings = FindingCollection()
    HybridTracesCheck("phasehybrid.traces", p).run(None, findings)
    msgs = [f.message for f in findings]
    assert any("FR-999" in m for m in msgs)
```

- [ ] **Step 2: Implement**

```python
"""HybridTracesCheck: enforce baseline ↔ story trace integrity."""
from __future__ import annotations
from pathlib import Path
from ruamel.yaml import YAML
from engine.findings import Finding, FindingCollection, Severity

_yaml = YAML(typ="safe")

class HybridTracesCheck:
    def __init__(self, gate_id: str, trace_path: Path) -> None:
        self.gate_id = gate_id
        self._path = trace_path

    def run(self, _graph, findings: FindingCollection) -> None:
        if not self._path.exists():
            findings.add(Finding(
                gate_id=f"{self.gate_id}.missing",
                severity=Severity.HIGH,
                message=f"Hybrid project missing {self._path}",
                location=None, line=None,
            ))
            return
        data = _yaml.load(self._path.read_text(encoding="utf-8")) or {}
        baseline_ids = {b["id"] for b in data.get("baseline", [])}
        stories = data.get("stories", [])
        # All trace targets exist
        for s in stories:
            for tgt in s.get("traces", []):
                if tgt not in baseline_ids:
                    findings.add(Finding(
                        gate_id=f"{self.gate_id}.unknown_trace",
                        severity=Severity.HIGH,
                        message=f"Story {s['id']} traces to {tgt} which is not in the baseline",
                        location=self._path, line=None,
                    ))
        # Every baseline item is implemented
        traced = {tgt for s in stories for tgt in s.get("traces", [])}
        for bid in sorted(baseline_ids - traced):
            findings.add(Finding(
                gate_id=f"{self.gate_id}.orphan_baseline",
                severity=Severity.HIGH,
                message=f"Baseline item {bid} has no implementing story",
                location=self._path, line=None,
            ))
```

- [ ] **Step 3: Verify pass + commit**

---

### Task 4: `HybridSyncGate`

**Files:**

- Create: `engine/gates/hybrid.py`
- Create: `engine/tests/test_gate_hybrid.py`
- Create: `docs/deterministic-gate-hybrid.md`

The gate runs only if `_context/methodology.md` declares `methodology: hybrid`. Otherwise it is a no-op.

- [ ] **Step 1: Failing test asserting gate is no-op when methodology ≠ hybrid; runs HybridTracesCheck when it is.**

- [ ] **Step 2: Implement**

```python
"""Hybrid Sync gate."""
from __future__ import annotations
from pathlib import Path
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.checks.hybrid_traces import HybridTracesCheck

class HybridSyncGate(Gate):
    id = "hybrid"
    title = "Hybrid (Water-Scrum-Fall) synchronisation gate"
    severity = Severity.HIGH

    def __init__(self, project_root: Path) -> None:
        self._root = project_root

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        meth = next((a for a in graph.artifacts if a.path.name == "methodology.md"), None)
        if not meth or "methodology: hybrid" not in meth.body.lower():
            return
        HybridTracesCheck(
            f"{self.id}.traces",
            self._root / "_registry" / "baseline-trace.yaml",
        ).run(graph, findings)
        # DoR/DoD must reference compliance constraints by ID
        dor_dod = next((a for a in graph.artifacts if a.path.name == "dor-dod.md"), None)
        if dor_dod is None:
            findings.add(Finding(
                gate_id=f"{self.id}.dor_dod_missing",
                severity=Severity.HIGH,
                message="Hybrid project missing 07-agile-artifacts/definitions/dor-dod.md",
                location=None, line=None,
            ))
            return
        if "FR-" not in dor_dod.body and "NFR-" not in dor_dod.body and "CTRL-" not in dor_dod.body:
            findings.add(Finding(
                gate_id=f"{self.id}.dor_dod_decoupled",
                severity=Severity.HIGH,
                message="dor-dod.md does not reference any baseline FR/NFR/CTRL by ID",
                location=dor_dod.path, line=None,
            ))
```

- [ ] **Step 3: Author the prose gate `docs/deterministic-gate-hybrid.md`**:

```markdown
---
gate: hybrid
checks:
  - hybrid.traces.unknown_trace
  - hybrid.traces.orphan_baseline
  - hybrid.dor_dod_missing
  - hybrid.dor_dod_decoupled
clause_refs:
  - standard: "PMI Disciplined Agile (DAD)"
    clause: "Hybrid Lifecycle"
---

# Hybrid Deterministic Gate

This gate is active only when `_context/methodology.md` declares the project as Hybrid.

1. **Baseline Trace Integrity**
   - `_registry/baseline-trace.yaml` exists and validates against the schema.
   - Every story's `traces:` list points to a baseline ID.
   - Every baseline ID is implemented by at least one story (or has a documented change-log entry).

2. **DoR/DoD Bound to Baseline**
   - `dor-dod.md` references baseline FR/NFR/CTRL identifiers verbatim.
   - Compliance constraints from `_context/quality-standards.md` appear in DoD.

3. **Exit Evidence**
   - Reviewer can prove every backlog item maps to a baselined obligation.
```

- [ ] **Step 4: Register `HybridSyncGate` in `engine/cli.py` validate command** (instantiate with `Workspace.root`).

- [ ] **Step 5: Update `scripts/validate_engine.py`** to require `docs/deterministic-gate-hybrid.md` exists (add it to `gate_files`).

- [ ] **Step 6: Verify pass + commit**

---

### Task 5: Extend `00-meta-initialization/new-project` to seed Hybrid scaffolding

**Files:**

- Modify: `00-meta-initialization/new-project/SKILL.md`

When the methodology answer is `hybrid` (or hybrid is detected via the heuristic in CLAUDE.md), the new-project flow should:

1. Create `projects/<X>/_registry/` with an empty `baseline-trace.yaml` containing the schema-required keys.
2. Create `projects/<X>/_context/methodology.md` with `methodology: hybrid` and pre-populated change-control body prompt.
3. Create `projects/<X>/07-agile-artifacts/definitions/` directory.

- [ ] **Step 1: Add a "Hybrid Branch" subsection to the new-project SKILL** under the existing scaffold flow.

- [ ] **Step 2: Add an empty-state template for `baseline-trace.yaml`**:

```yaml
# Populated by `python -m engine sync <project>` and the hybrid-synchronization skill.
baseline: []
stories: []
```

- [ ] **Step 3: Commit**

---

### Task 6: Update CLAUDE.md hybrid heuristic

**Files:**

- Modify: `CLAUDE.md`

The current "hybrid-detection heuristic" in the New Project Protocol asks the user; extend it to also auto-invoke the `hybrid-synchronization` skill after Phase 02 sign-off.

- [ ] **Step 1: Find the section** "Build Document Protocol" — add a new subsection above it called "Hybrid Cross-Cutting Trigger":

```markdown
## Hybrid Cross-Cutting Trigger

If `projects/<ProjectName>/_context/methodology.md` declares `methodology: hybrid`, the assistant MUST invoke the `hybrid-synchronization` skill after the Phase 02 Waterfall SRS is signed off and before any Phase 07 Agile artifact is generated. The kernel will block Phase 07 outputs until `python -m engine validate <project>` passes the `hybrid` gate.
```

- [ ] **Step 2: Commit**

---

## Self-Review

1. **Spec coverage:** Hybrid contract from `docs/hybrid-operating-model.md` is now machine-enforced via `HybridSyncGate`. Backlog cannot silently diverge from baseline.
2. **Placeholder scan:** None.
3. **Type consistency:** YAML schema mirrors the kernel's existing schema-validation pattern (Plan 03). Gate `id` namespace is `hybrid.*` (distinct from `phaseNN.*`).
4. **Operability:** New projects auto-scaffold with empty trace files; the engineer is never asked to invent the file from scratch.
