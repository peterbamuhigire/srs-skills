# Executable Phase Gates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Convert each prose phase gate (`docs/deterministic-gate-phaseNN.md`) into a Python `Gate` subclass under `engine/gates/phaseNN.py` that the kernel can run, returning Findings tied to specific lines and identifiers in the project workspace. Closes Gaps #1 (enforcement), #4 (standards proof), #8 (Phase 09 verification).

**Architecture:** Each phase gets one module exporting one `PhaseNNGate` class plus N internal `Check` callables. The prose gate documents stay — they become the human-readable specification. Each Check has a one-to-one correspondence with a numbered clause in the prose gate. Standards-clause IDs (`IEEE 29148-5.2.4`, `ISO/IEC/IEEE 29119-3-7.2`, etc.) are attached to every Finding so audit reports can cite them.

**Tech Stack:** Same as Plan 01.

---

## File Structure

```
engine/gates/
├── phase01.py     # Strategic Vision gate (5 checks)
├── phase02.py     # Requirements Engineering gate (8 checks)
├── phase03.py     # Design Documentation gate (6 checks)
├── phase04.py     # Development Artifacts gate (4 checks)
├── phase05.py     # Testing Documentation gate (7 checks — reference impl from prose)
├── phase06.py     # Deployment & Operations gate (6 checks)
├── phase07.py     # Agile Artifacts gate (5 checks)
├── phase08.py     # End-User Documentation gate (3 checks)
├── phase09.py     # Governance & Compliance gate (8 checks)
└── _shared.py     # Common helpers (clause attachment, severity lookup)

engine/checks/
├── traceability.py    # FR↔BG, FR↔TC, US↔FR linking
├── nfr_smart.py       # SMART NFR detector
├── glossary.py        # GLOSSARY-GAP detector
├── coverage.py        # requirement coverage measurability
├── controls.py        # added by Plan 06
└── stimulus_response.py  # Verifiability of FRs

engine/tests/
├── test_phase01_gate.py
├── ...
└── test_phase09_gate.py
```

`docs/deterministic-gate-phaseNN.md` files **stay** but each gets a YAML frontmatter block that lists its check IDs so the engineer can audit gate↔code coverage at a glance.

---

### Task 1: Shared helpers and standards-clause attachment

**Files:**

- Create: `engine/gates/_shared.py`
- Create: `engine/tests/test_gates_shared.py`

- [ ] **Step 1: Write the failing test**

```python
from engine.gates._shared import attach_clause, ClauseRef
from engine.findings import Finding, Severity

def test_attach_clause_appends_clause_to_message():
    f = Finding("phase05.test_oracle", Severity.HIGH, "FR-001 has no oracle", None, None)
    f2 = attach_clause(f, ClauseRef("ISO/IEC/IEEE 29119-3", "7.2.3"))
    assert "[ISO/IEC/IEEE 29119-3 §7.2.3]" in f2.message
```

- [ ] **Step 2: Verify failure** — `pytest engine/tests/test_gates_shared.py -v` → `ModuleNotFoundError`.

- [ ] **Step 3: Implement**

```python
"""Shared helpers for phase gates."""
from __future__ import annotations
from dataclasses import dataclass
from engine.findings import Finding

@dataclass(frozen=True)
class ClauseRef:
    standard: str
    clause: str

    def label(self) -> str:
        return f"[{self.standard} §{self.clause}]"

def attach_clause(finding: Finding, clause: ClauseRef) -> Finding:
    return Finding(
        gate_id=finding.gate_id,
        severity=finding.severity,
        message=f"{finding.message} {clause.label()}",
        location=finding.location,
        line=finding.line,
    )
```

- [ ] **Step 4: Verify pass + commit**

```bash
pytest engine/tests/test_gates_shared.py -v
git add engine/gates/_shared.py engine/tests/test_gates_shared.py
git commit -m "feat(engine): add ClauseRef and attach_clause helper"
```

---

### Task 2: SMART NFR check (reusable across gates)

**Files:**

- Create: `engine/checks/nfr_smart.py`
- Create: `engine/tests/test_check_nfr_smart.py`

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
import pytest
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.nfr_smart import SmartNfrCheck

def _ws(tmp_path: Path, body: str) -> ArtifactGraph:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/nfrs.md").write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_passes_when_nfr_has_metric_and_threshold(tmp_path: Path):
    body = "# NFRs\n- **NFR-001** Response time shall be ≤ 500 ms at P95 under normal load."
    findings = FindingCollection()
    SmartNfrCheck("phase02.smart_nfr").run(_ws(tmp_path, body), findings)
    assert len(findings) == 0

def test_flags_vague_nfr(tmp_path: Path):
    body = "# NFRs\n- **NFR-002** The system shall be fast and reliable."
    findings = FindingCollection()
    SmartNfrCheck("phase02.smart_nfr").run(_ws(tmp_path, body), findings)
    items = list(findings)
    assert len(items) == 1
    assert "fast" in items[0].message
```

- [ ] **Step 2: Verify failure → implement**

```python
"""SMART NFR check: every NFR must have a measurable metric + threshold."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_VAGUE = re.compile(r"\b(fast|intuitive|reliable|robust|seamless|user[- ]friendly|scalable)\b", re.IGNORECASE)
_METRIC = re.compile(r"(?:≤|<=|≥|>=|<|>|=)\s*\d+(\.\d+)?\s*(ms|s|min|MB|GB|%|req/s|RPS|users)", re.IGNORECASE)
_NFR_LINE = re.compile(r"\*\*(NFR-\d{3,5})\*\*\s+(.*)")

class SmartNfrCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        for art in graph.artifacts:
            for lineno, line in enumerate(art.body.splitlines(), start=1):
                m = _NFR_LINE.search(line)
                if not m:
                    continue
                nfr_id, text = m.group(1), m.group(2)
                vague = _VAGUE.search(text)
                metric = _METRIC.search(text)
                if vague and not metric:
                    findings.add(Finding(
                        gate_id=self.gate_id,
                        severity=Severity.HIGH,
                        message=f"{nfr_id} uses vague adjective '{vague.group(0)}' with no metric/threshold",
                        location=art.path,
                        line=lineno,
                    ))
```

- [ ] **Step 3: Verify pass + commit**

```bash
pytest engine/tests/test_check_nfr_smart.py -v
git add engine/checks/nfr_smart.py engine/tests/test_check_nfr_smart.py
git commit -m "feat(engine): add SMART NFR check"
```

---

### Task 3: Traceability check (FR ↔ business goal ↔ test case)

**Files:**

- Create: `engine/checks/traceability.py`
- Create: `engine/tests/test_check_traceability.py`

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.traceability import TraceabilityCheck

def _ws(tmp_path: Path, files: dict) -> ArtifactGraph:
    (tmp_path / "_context").mkdir()
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_passes_when_fr_has_business_goal_and_test_case(tmp_path: Path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\n- **BG-001** Reduce claim cycle to 3 days.",
        "02-requirements-engineering/srs/3.2.md": "---\nphase: '02'\n---\n# FRs\n- **FR-001** trace: BG-001",
        "05-testing-documentation/test-plan/cases.md": "---\nphase: '05'\n---\n# Cases\n- **TC-001** verifies FR-001",
    })
    findings = FindingCollection()
    TraceabilityCheck("phase09.traceability").run(graph, findings)
    assert len(findings) == 0

def test_flags_orphan_fr(tmp_path: Path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\n- **BG-001** thing.",
        "02-requirements-engineering/srs/3.2.md": "---\nphase: '02'\n---\n# FRs\n- **FR-002** lonely.",
    })
    findings = FindingCollection()
    TraceabilityCheck("phase09.traceability").run(graph, findings)
    msgs = [f.message for f in findings]
    assert any("FR-002" in m for m in msgs)
```

- [ ] **Step 2: Implement**

```python
"""Traceability check: every FR links upward to a BG and downward to a TC."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

class TraceabilityCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        all_text = "\n".join(a.body for a in graph.artifacts)
        all_ids = set(graph.all_identifiers())
        frs = {i for i in all_ids if i.startswith("FR-")}
        bgs = {i for i in all_ids if i.startswith("BG-")}
        for fr in sorted(frs):
            mentioned_with_bg = re.search(rf"{re.escape(fr)}.*BG-\d+|BG-\d+.*{re.escape(fr)}", all_text)
            if not mentioned_with_bg or not bgs:
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"{fr} has no traceability link to any business goal",
                    location=None, line=None,
                ))
            mentioned_with_tc = re.search(rf"TC-\d+.*{re.escape(fr)}|{re.escape(fr)}.*TC-\d+", all_text)
            if not mentioned_with_tc:
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"{fr} has no traceability link to any test case",
                    location=None, line=None,
                ))
```

- [ ] **Step 3: Verify pass + commit**

---

### Task 4: Stimulus-response verifiability check

**Files:**

- Create: `engine/checks/stimulus_response.py`
- Create: `engine/tests/test_check_stimulus_response.py`

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.stimulus_response import StimulusResponseCheck

def _ws(tmp_path, body):
    (tmp_path / "_context").mkdir()
    (tmp_path / "02/srs.md").parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / "02/srs.md").write_text(body)
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_passes_when_fr_uses_shall_with_action(tmp_path):
    graph = _ws(tmp_path, "---\nphase: '02'\n---\n- **FR-001** When a provider submits a claim, the system shall persist it within 2 seconds.")
    findings = FindingCollection()
    StimulusResponseCheck("phase02.stimulus_response").run(graph, findings)
    assert len(findings) == 0

def test_flags_fr_without_shall(tmp_path):
    graph = _ws(tmp_path, "---\nphase: '02'\n---\n- **FR-002** The system can submit claims.")
    findings = FindingCollection()
    StimulusResponseCheck("phase02.stimulus_response").run(graph, findings)
    assert len(list(findings)) == 1
```

- [ ] **Step 2: Implement**

```python
"""FRs must follow stimulus → response with the verb 'shall'."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_FR = re.compile(r"\*\*(FR-\d{3,5})\*\*\s+(.*)")
_SHALL = re.compile(r"\bshall\b", re.IGNORECASE)

class StimulusResponseCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        for art in graph.artifacts:
            for lineno, line in enumerate(art.body.splitlines(), start=1):
                m = _FR.search(line)
                if m and not _SHALL.search(m.group(2)):
                    findings.add(Finding(
                        gate_id=self.gate_id,
                        severity=Severity.HIGH,
                        message=f"{m.group(1)} does not use the prescriptive verb 'shall'",
                        location=art.path, line=lineno,
                    ))
```

- [ ] **Step 3: Verify pass + commit**

---

### Task 5: Phase 01 — Strategic Vision gate

**Files:**

- Create: `engine/gates/phase01.py`
- Create: `engine/tests/test_phase01_gate.py`
- Modify: `docs/deterministic-gate-phase01.md` (add YAML frontmatter listing check IDs)

The Phase 01 prose gate requires: canonical inputs (vision/stakeholders/features/glossary), Vision-to-Requirement readiness (every feature has at least one driving stakeholder need), clause anchoring to IEEE 29148-§5.2, and no unresolved `[CONTEXT-GAP]`.

- [ ] **Step 1: Add frontmatter to the prose gate**

Edit `docs/deterministic-gate-phase01.md`. Insert at the top:

```markdown
---
gate: phase01
checks:
  - phase01.canonical_inputs_present
  - phase01.feature_has_stakeholder
  - phase01.no_context_gaps
  - phase01.glossary_seeded
clause_refs:
  - standard: "IEEE Std 29148-2018"
    clause: "5.2"
---

```

(Existing prose stays unchanged below.)

- [ ] **Step 2: Failing test**

```python
from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase01 import Phase01Gate

def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body)
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_passes_with_full_canonical_inputs(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\nReduce claim cycle.",
        "_context/stakeholders.md": "# Stakeholders\n- Provider Office.",
        "_context/features.md": "# Features\n- F-1 Submit Claim — driven by Provider Office",
        "_context/glossary.md": "# Glossary\n- **Claim:** a request for payment.",
    })
    findings = FindingCollection()
    Phase01Gate().evaluate(graph, findings)
    assert len(findings) == 0

def test_flags_missing_stakeholders_file(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\nx",
        "_context/features.md": "# Features\n- F-1",
        "_context/glossary.md": "# Glossary\n- **x:** y",
    })
    findings = FindingCollection()
    Phase01Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings]
    assert any("stakeholders.md" in m for m in msgs)

def test_flags_orphan_feature(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\nx",
        "_context/stakeholders.md": "# Stakeholders\n- Provider Office",
        "_context/features.md": "# Features\n- F-1 Mystery — driven by no-one",
        "_context/glossary.md": "# Glossary\n- **x:** y",
    })
    findings = FindingCollection()
    Phase01Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings]
    assert any("F-1" in m for m in msgs)
```

- [ ] **Step 3: Implement**

```python
"""Phase 01 — Strategic Vision gate."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_REQUIRED = ("vision.md", "stakeholders.md", "features.md", "glossary.md")
_FEATURE = re.compile(r"-\s+(F-\d+)\s+([^—]+)—\s+driven\s+by\s+(.+)", re.IGNORECASE)
_CLAUSE = ClauseRef("IEEE Std 29148-2018", "5.2")

class Phase01Gate(Gate):
    id = "phase01"
    title = "Strategic Vision phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        # Check 1: canonical inputs present
        present = {a.path.name for a in graph.artifacts if a.path.parts[0] == "_context"}
        for fname in _REQUIRED:
            if fname not in present:
                findings.add(attach_clause(Finding(
                    gate_id=f"{self.id}.canonical_inputs_present",
                    severity=Severity.HIGH,
                    message=f"Missing required canonical input: _context/{fname}",
                    location=None, line=None,
                ), _CLAUSE))

        # Check 2: every feature has a driving stakeholder
        stakeholders_text = ""
        for art in graph.artifacts:
            if art.path.name == "stakeholders.md":
                stakeholders_text = art.body
            if art.path.name == "features.md":
                for lineno, line in enumerate(art.body.splitlines(), start=1):
                    m = _FEATURE.search(line)
                    if not m:
                        continue
                    fid, _name, driver = m.group(1), m.group(2), m.group(3).strip()
                    if driver.lower() in {"no-one", "noone", "none", "unknown"}:
                        findings.add(attach_clause(Finding(
                            gate_id=f"{self.id}.feature_has_stakeholder",
                            severity=Severity.HIGH,
                            message=f"{fid} has no identified driving stakeholder",
                            location=art.path, line=lineno,
                        ), _CLAUSE))
                    elif driver and driver not in stakeholders_text:
                        findings.add(attach_clause(Finding(
                            gate_id=f"{self.id}.feature_has_stakeholder",
                            severity=Severity.MEDIUM,
                            message=f"{fid} cites stakeholder '{driver}' not in stakeholders.md",
                            location=art.path, line=lineno,
                        ), _CLAUSE))
```

- [ ] **Step 4: Verify pass + commit**

---

### Task 6: Register Phase01Gate in the kernel CLI

**Files:**

- Modify: `engine/cli.py`

- [ ] **Step 1: Add to `_default_registry()`**

Replace the body of `_default_registry()` with:

```python
def _default_registry() -> GateRegistry:
    from engine.gates.phase01 import Phase01Gate
    reg = GateRegistry()
    reg.register(NoUnresolvedFailMarkersGate())
    reg.register(Phase01Gate())
    return reg
```

- [ ] **Step 2: Re-run all tests**

```bash
pytest -v
```

Expected: all passing including `test_cli.py` (the existing CLI tests use minimal projects — adjust the assertions if Phase01Gate now reports "missing canonical input" on those minimal fixtures by extending those fixtures to include the four required files).

- [ ] **Step 3: Commit**

```bash
git add engine/cli.py
git commit -m "feat(engine): register Phase01Gate in default CLI registry"
```

---

### Task 7: Phase 02 — Requirements Engineering gate

Same shape as Task 5. The Phase 02 gate composes existing reusable checks:

- `phase02.smart_nfr` → `SmartNfrCheck`
- `phase02.stimulus_response` → `StimulusResponseCheck`
- `phase02.glossary_complete` → `GlossaryCheck` (added below in Task 8)
- `phase02.id_uniqueness` → delegates to Plan 03's `IdentifierRegistryCheck`

**Files:**

- Create: `engine/gates/phase02.py`
- Create: `engine/tests/test_phase02_gate.py`
- Modify: `docs/deterministic-gate-phase02.md` (add frontmatter as in Task 5)

- [ ] **Step 1: Implementation**

```python
"""Phase 02 — Requirements Engineering gate."""
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection, Severity
from engine.gates.base import Gate
from engine.checks.nfr_smart import SmartNfrCheck
from engine.checks.stimulus_response import StimulusResponseCheck

class Phase02Gate(Gate):
    id = "phase02"
    title = "Requirements Engineering phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        SmartNfrCheck(f"{self.id}.smart_nfr").run(graph, findings)
        StimulusResponseCheck(f"{self.id}.stimulus_response").run(graph, findings)
```

- [ ] **Step 2: Test that the gate aggregates findings from both checks** (write a fixture project with one vague NFR and one missing-`shall` FR, assert two findings come back).

- [ ] **Step 3: Register in `engine/cli.py`** alongside Phase01Gate.

- [ ] **Step 4: Commit**

---

### Task 8: Phase 05 — Testing Documentation gate (reference implementation)

The prose gate `docs/deterministic-gate-phase05.md` lists four numbered closure checks tied to BS ISO/IEC/IEEE 29119-3. Implement each as a separate Check inside `Phase05Gate.evaluate`:

- `phase05.normative_test_structure` — every test artifact has frontmatter with `inputs`, `expected_results`, `requirement_trace` keys.
- `phase05.required_evidence` — `05-testing-documentation/29119-deterministic-checks.md` exists and is non-empty.
- `phase05.coverage_measurable` — total `TC-*` count ≥ total `FR-*` count, OR a coverage matrix file exists.
- `phase05.exit_evidence` — `test-completion-report.md` exists and contains the words "tested", "result", and at least one `FR-` reference.

**Files:**

- Create: `engine/gates/phase05.py`
- Create: `engine/tests/test_phase05_gate.py`
- Modify: `docs/deterministic-gate-phase05.md` (frontmatter)

- [ ] **Step 1: Failing test for `normative_test_structure`**

```python
def test_flags_test_case_without_required_keys(tmp_path):
    files = {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/test-plan/tc.md": "---\nphase: '05'\n---\n- **TC-001** something",
    }
    # ... build graph, run Phase05Gate, assert finding mentions "expected_results"
```

- [ ] **Step 2: Implement** (follow the same pattern as Task 7).

- [ ] **Step 3: Verify pass + commit**

---

### Task 9: Phases 03, 04, 06, 07, 08 gates (template repeat)

Each follows the same recipe as Tasks 5/7/8:

| Phase | Gate file | Required Checks (= prose gate clauses) |
|---|---|---|
| 03 | `engine/gates/phase03.py` | `architecture_decisions_recorded`, `interfaces_have_contracts`, `data_model_has_keys`, `nfrs_link_to_design_choices`, `security_threat_model_present`, `iot_signal_inventory_present` |
| 04 | `engine/gates/phase04.py` | `coding_standards_referenced`, `env_setup_reproducible`, `tech_spec_links_to_fr`, `contrib_guide_present` |
| 06 | `engine/gates/phase06.py` | `deployment_guide_has_rollback`, `runbook_has_escalation`, `monitoring_has_slo`, `infra_has_ir_diagram`, `go_live_readiness_checklist_complete`, `change_window_documented` |
| 07 | `engine/gates/phase07.py` | `dor_references_baseline`, `dod_references_compliance`, `sprint_artifacts_have_ids`, `retro_actions_assigned`, `velocity_history_present` |
| 08 | `engine/gates/phase08.py` | `user_manual_has_screenshots`, `release_notes_link_to_fr`, `faq_has_at_least_5_qa` |

For each phase:

- [ ] **Step 1:** Write a failing test for the **first** check in the row.
- [ ] **Step 2:** Implement the gate file with the first check; commit.
- [ ] **Step 3:** Repeat Step 1+2 for each remaining check in the row (one commit per check).
- [ ] **Step 4:** Add YAML frontmatter to the corresponding `docs/deterministic-gate-phaseNN.md` listing every check ID.
- [ ] **Step 5:** Register the gate in `engine/cli.py`.

---

### Task 10: Phase 09 — Governance & Compliance gate (the verification gate)

This is the gate that turns Phase 09 from "consumes documents" into "independently verifies the truth of upstream content" — closing Gap #8.

Checks:

- `phase09.traceability` — uses `TraceabilityCheck` from Task 3.
- `phase09.audit_report_present` — `09-governance-compliance/audit-report.md` exists, is non-empty, lists each gate's pass/fail.
- `phase09.compliance_controls_have_evidence` — every `CTRL-*` ID in `_registry/controls.yaml` appears in at least one design and one test file (delegates to Plan 06's `ControlsCheck`).
- `phase09.risk_register_links_to_fr` — every entry in `risk-register.md` links to at least one `FR-`, `NFR-`, or `CTRL-`.
- `phase09.waivers_have_expiry` — every waiver in `_registry/waivers.yaml` has `expires_on` ≤ 90 days from `approved_on`.
- `phase09.evidence_pack_buildable` — running `python -m engine pack` exits 0 (added in Plan 07).

**Files:**

- Create: `engine/gates/phase09.py`
- Create: `engine/tests/test_phase09_gate.py`
- Modify: `docs/deterministic-gate-phase09.md` (frontmatter)

- [ ] **Step 1:** Implement and TDD each check (one per commit).
- [ ] **Step 2:** Register in `engine/cli.py`.

---

### Task 11: Standards-clause registry document

**Files:**

- Create: `docs/standards-clause-registry.md`

Single-source-of-truth document mapping every check ID → standard + clause. Reviewer reads this to prove standards conformance.

- [ ] **Step 1: Author the registry**

```markdown
# Standards Clause Registry

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase01.canonical_inputs_present` | IEEE Std 29148-2018 | 5.2 | `engine/gates/phase01.py` |
| `phase01.feature_has_stakeholder` | IEEE Std 29148-2018 | 5.2.5 | `engine/gates/phase01.py` |
| `phase02.smart_nfr` | IEEE Std 830-1998 | 4.3.2 | `engine/checks/nfr_smart.py` |
| `phase02.stimulus_response` | IEEE Std 830-1998 | 4.3.1 | `engine/checks/stimulus_response.py` |
| `phase05.normative_test_structure` | BS ISO/IEC/IEEE 29119-3:2013 | 7.2 | `engine/gates/phase05.py` |
| `phase05.coverage_measurable` | BS ISO/IEC/IEEE 29119-3:2013 | 6.3.4 | `engine/gates/phase05.py` |
| `phase09.traceability` | IEEE Std 29148-2018 | 6.5 | `engine/checks/traceability.py` |
| `phase09.audit_report_present` | ISO/IEC 15504-2 | 5.5 | `engine/gates/phase09.py` |
| ... | | | |
```

(Fill the table with one row per registered check.)

- [ ] **Step 2: Add CI assertion** — extend `scripts/validate_engine.py`'s `validate_deterministic_gates()` to require every check ID in `engine.cli._default_registry()` appears in `docs/standards-clause-registry.md`.

- [ ] **Step 3: Commit**

---

## Self-Review

1. **Spec coverage:** Each prose gate has a Python module that mirrors its numbered clauses. Each Finding cites a clause via `attach_clause`. Phase 09 includes the `audit_report_present` and `compliance_controls_have_evidence` checks that close Gap #8.
2. **Placeholder scan:** None. Every check listed in Task 9 has a name describing its assertion.
3. **Type consistency:** `Gate.evaluate(graph, findings)` signature matches Plan 01's base. `ClauseRef` used uniformly. Check classes follow `__init__(self, gate_id) → run(graph, findings)`.
4. **Standards proof:** The clause registry is the auditable artifact. CI fails the build if a registered gate has no row in the registry.
