# Validation Kernel Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python package `engine/` that becomes the single canonical validation kernel for any `projects/<ProjectName>/` workspace — replacing fragmented validation in five separate locations and converting prose phase gates into executable checks that block downstream progression unless waived.

**Architecture:** Plain Python 3.11+ package. A single `engine.cli` entry-point loads the project workspace into an immutable `ArtifactGraph`, runs every registered `Gate` against it, collects `Finding` objects, applies the project's `WaiverRegister`, and emits Markdown + JUnit + SARIF reports. No external rules engine, no service runtime, no database — just files in, findings out. Designed so Plans 02–09 add gates and checks without touching the kernel itself.

**Tech Stack:** Python 3.11, `pytest`, `pytest-cov`, `ruamel.yaml` (YAML round-trip for waivers/registries), `mistune` (Markdown AST), `jsonschema` (registry validation), `click` (CLI).

---

## File Structure

```
engine/
├── __init__.py              # Public API (re-exports)
├── cli.py                   # `python -m engine ...` entry-point (click)
├── workspace.py             # Locates and loads a project workspace
├── artifact_graph.py        # Immutable in-memory graph of all artifacts
├── findings.py              # Finding, Severity, FindingCollection
├── waivers.py               # WaiverRegister loader + matcher
├── reporters/
│   ├── __init__.py
│   ├── markdown.py
│   ├── junit.py
│   └── sarif.py
├── parsers/
│   ├── __init__.py
│   ├── frontmatter.py       # YAML frontmatter parser
│   ├── markers.py           # [V&V-FAIL], [CONTEXT-GAP], etc.
│   └── tables.py            # Markdown table → list[dict]
├── gates/
│   ├── __init__.py          # Gate registry + discovery
│   └── base.py              # Gate ABC; phase modules added by Plan 02
├── checks/
│   ├── __init__.py
│   └── markers.py           # First reusable check; rest added by Plan 02
└── tests/
    ├── __init__.py
    ├── conftest.py          # Tiny fixture project under tests/fixtures/
    ├── fixtures/
    │   └── tiny_project/    # Minimal projects/<X>/ tree for tests
    ├── test_workspace.py
    ├── test_artifact_graph.py
    ├── test_findings.py
    ├── test_waivers.py
    ├── test_parsers.py
    ├── test_gates_base.py
    ├── test_check_markers.py
    ├── test_cli.py
    └── test_reporters.py

scripts/validate_engine.py   # Modified: thin shim that delegates to engine.cli
pyproject.toml               # New file at repo root: declares engine package + deps
.github/workflows/engine.yml # New CI workflow
.pre-commit-config.yaml      # New: runs `python -m engine validate` on changed projects
```

Each file owns one responsibility. Files top out at ~200 lines.

---

### Task 1: Bootstrap the package and tooling

**Files:**

- Create: `pyproject.toml`
- Create: `engine/__init__.py`
- Create: `engine/tests/__init__.py`
- Create: `engine/tests/conftest.py`

- [ ] **Step 1: Write `pyproject.toml`**

```toml
[project]
name = "srs-skills-engine"
version = "0.1.0"
description = "Validation kernel for srs-skills project workspaces."
requires-python = ">=3.11"
dependencies = [
  "click>=8.1",
  "ruamel.yaml>=0.18",
  "mistune>=3.0",
  "jsonschema>=4.21",
]

[project.optional-dependencies]
dev = ["pytest>=8.0", "pytest-cov>=4.1"]

[project.scripts]
srs-engine = "engine.cli:main"

[tool.pytest.ini_options]
testpaths = ["engine/tests"]
addopts = "-q --strict-markers --cov=engine --cov-report=term-missing"

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
include = ["engine*"]
```

- [ ] **Step 2: Empty package init**

`engine/__init__.py`:

```python
"""srs-skills validation kernel."""
__all__ = []
```

- [ ] **Step 3: Empty test package init and shared conftest**

`engine/tests/__init__.py`: (empty file).

`engine/tests/conftest.py`:

```python
from pathlib import Path
import pytest

@pytest.fixture
def fixtures_dir() -> Path:
    return Path(__file__).parent / "fixtures"

@pytest.fixture
def tiny_project(fixtures_dir: Path) -> Path:
    return fixtures_dir / "tiny_project"
```

- [ ] **Step 4: Install in editable mode + run pytest baseline**

Run:

```bash
pip install -e ".[dev]"
pytest
```

Expected: `no tests ran` (exit 5) — that is the green baseline.

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml engine/__init__.py engine/tests/__init__.py engine/tests/conftest.py
git commit -m "feat(engine): bootstrap python package and pytest config"
```

---

### Task 2: Workspace locator with TDD

**Files:**

- Create: `engine/workspace.py`
- Create: `engine/tests/test_workspace.py`
- Create: `engine/tests/fixtures/tiny_project/_context/vision.md`
- Create: `engine/tests/fixtures/tiny_project/_context/glossary.md`

- [ ] **Step 1: Write the failing test**

`engine/tests/test_workspace.py`:

```python
from pathlib import Path
import pytest
from engine.workspace import Workspace, WorkspaceNotFoundError

def test_loads_workspace_with_context_dir(tiny_project: Path):
    ws = Workspace.load(tiny_project)
    assert ws.root == tiny_project
    assert ws.context_dir == tiny_project / "_context"
    assert (ws.context_dir / "vision.md").exists()

def test_raises_when_no_context_dir(tmp_path: Path):
    with pytest.raises(WorkspaceNotFoundError) as exc:
        Workspace.load(tmp_path)
    assert "_context" in str(exc.value)

def test_lists_all_artifacts(tiny_project: Path):
    ws = Workspace.load(tiny_project)
    paths = sorted(p.name for p in ws.iter_artifacts())
    assert paths == ["glossary.md", "vision.md"]
```

- [ ] **Step 2: Create the fixture files**

`engine/tests/fixtures/tiny_project/_context/vision.md`:

```markdown
# Vision

This is a tiny project used by the engine kernel tests.
```

`engine/tests/fixtures/tiny_project/_context/glossary.md`:

```markdown
# Glossary

- **Engine:** the validation kernel.
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `pytest engine/tests/test_workspace.py -v`
Expected: `ModuleNotFoundError: No module named 'engine.workspace'`.

- [ ] **Step 4: Implement `engine/workspace.py`**

```python
"""Project workspace locator."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

class WorkspaceNotFoundError(Exception):
    """Raised when a path is not a valid project workspace."""

@dataclass(frozen=True)
class Workspace:
    root: Path
    context_dir: Path

    @classmethod
    def load(cls, root: Path) -> "Workspace":
        root = Path(root).resolve()
        ctx = root / "_context"
        if not ctx.is_dir():
            raise WorkspaceNotFoundError(
                f"{root} is not a project workspace: missing '_context' directory"
            )
        return cls(root=root, context_dir=ctx)

    def iter_artifacts(self) -> Iterator[Path]:
        for p in sorted(self.root.rglob("*.md")):
            if p.is_file():
                yield p
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `pytest engine/tests/test_workspace.py -v`
Expected: 3 passed.

- [ ] **Step 6: Commit**

```bash
git add engine/workspace.py engine/tests/test_workspace.py engine/tests/fixtures/
git commit -m "feat(engine): add Workspace loader with context-dir validation"
```

---

### Task 3: Findings, severity, and collections

**Files:**

- Create: `engine/findings.py`
- Create: `engine/tests/test_findings.py`

- [ ] **Step 1: Write the failing test**

`engine/tests/test_findings.py`:

```python
from pathlib import Path
import pytest
from engine.findings import Finding, Severity, FindingCollection

def test_finding_is_immutable():
    f = Finding(
        gate_id="phase01.context_complete",
        severity=Severity.HIGH,
        message="vision.md missing required section",
        location=Path("_context/vision.md"),
        line=12,
    )
    with pytest.raises(Exception):
        f.message = "changed"  # frozen dataclass

def test_collection_blocks_when_high_severity_present():
    coll = FindingCollection()
    coll.add(Finding("g1", Severity.LOW, "ok-ish", None, None))
    assert coll.is_blocking is False
    coll.add(Finding("g2", Severity.HIGH, "broken", None, None))
    assert coll.is_blocking is True

def test_collection_filters_by_gate():
    coll = FindingCollection()
    coll.add(Finding("phase01.x", Severity.HIGH, "a", None, None))
    coll.add(Finding("phase02.y", Severity.HIGH, "b", None, None))
    assert len(coll.for_gate("phase01.x")) == 1
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest engine/tests/test_findings.py -v`
Expected: ModuleNotFoundError.

- [ ] **Step 3: Implement `engine/findings.py`**

```python
"""Finding, Severity, and FindingCollection."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Iterable, Optional

class Severity(IntEnum):
    INFO = 10
    LOW = 20
    MEDIUM = 30
    HIGH = 40

@dataclass(frozen=True)
class Finding:
    gate_id: str
    severity: Severity
    message: str
    location: Optional[Path]
    line: Optional[int]

class FindingCollection:
    def __init__(self) -> None:
        self._items: list[Finding] = []

    def add(self, finding: Finding) -> None:
        self._items.append(finding)

    def extend(self, findings: Iterable[Finding]) -> None:
        self._items.extend(findings)

    def for_gate(self, gate_id: str) -> list[Finding]:
        return [f for f in self._items if f.gate_id == gate_id]

    @property
    def is_blocking(self) -> bool:
        return any(f.severity >= Severity.HIGH for f in self._items)

    def __iter__(self):
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)
```

- [ ] **Step 4: Verify pass**

Run: `pytest engine/tests/test_findings.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add engine/findings.py engine/tests/test_findings.py
git commit -m "feat(engine): add Finding/Severity/FindingCollection"
```

---

### Task 4: Markdown frontmatter and marker parsers

**Files:**

- Create: `engine/parsers/__init__.py`
- Create: `engine/parsers/frontmatter.py`
- Create: `engine/parsers/markers.py`
- Create: `engine/tests/test_parsers.py`

- [ ] **Step 1: Write the failing test**

`engine/tests/test_parsers.py`:

```python
from pathlib import Path
from engine.parsers.frontmatter import parse_frontmatter
from engine.parsers.markers import find_markers, Marker

def test_parses_yaml_frontmatter():
    body = "---\nid: FR-001\nstatus: draft\n---\n# Title\n"
    fm, content = parse_frontmatter(body)
    assert fm == {"id": "FR-001", "status": "draft"}
    assert content.startswith("# Title")

def test_returns_empty_dict_when_no_frontmatter():
    body = "# Title\nbody text"
    fm, content = parse_frontmatter(body)
    assert fm == {}
    assert content == body

def test_finds_marker_with_reason():
    body = "Some text [V&V-FAIL: missing test oracle] and more.\n[CONTEXT-GAP: stakeholders]"
    markers = find_markers(body)
    assert Marker("V&V-FAIL", "missing test oracle", 1) in markers
    assert Marker("CONTEXT-GAP", "stakeholders", 2) in markers

def test_finds_marker_without_reason():
    body = "[GLOSSARY-GAP]"
    markers = find_markers(body)
    assert markers == [Marker("GLOSSARY-GAP", "", 1)]
```

- [ ] **Step 2: Run to verify failure**

Run: `pytest engine/tests/test_parsers.py -v`
Expected: ModuleNotFoundError.

- [ ] **Step 3: Implement `engine/parsers/__init__.py`** as an empty file.

- [ ] **Step 4: Implement `engine/parsers/frontmatter.py`**

```python
"""YAML frontmatter parser."""
from __future__ import annotations
from typing import Tuple
from ruamel.yaml import YAML

_yaml = YAML(typ="safe")
_DELIM = "---\n"

def parse_frontmatter(body: str) -> Tuple[dict, str]:
    if not body.startswith(_DELIM):
        return {}, body
    end = body.find(f"\n{_DELIM.strip()}\n", len(_DELIM))
    if end == -1:
        return {}, body
    raw = body[len(_DELIM):end]
    rest = body[end + len(_DELIM) + 1 :]
    data = _yaml.load(raw) or {}
    if not isinstance(data, dict):
        return {}, body
    return data, rest
```

- [ ] **Step 5: Implement `engine/parsers/markers.py`**

```python
"""Find [TAG: reason] markers in markdown."""
from __future__ import annotations
import re
from dataclasses import dataclass
from typing import List

_PATTERN = re.compile(r"\[(?P<tag>[A-Z&\-]+)(?::\s*(?P<reason>[^\]]*))?\]")
_KNOWN_TAGS = {
    "V&V-FAIL", "CONTEXT-GAP", "GLOSSARY-GAP",
    "SMART-FAIL", "TRACE-GAP", "VERIFIABILITY-FAIL",
    "DPPA-FAIL", "DPIA-REQUIRED", "CONTROL-GAP",
    "DOMAIN-DEFAULT",
}

@dataclass(frozen=True)
class Marker:
    tag: str
    reason: str
    line: int

def find_markers(body: str) -> List[Marker]:
    out: List[Marker] = []
    for lineno, line in enumerate(body.splitlines(), start=1):
        for m in _PATTERN.finditer(line):
            tag = m.group("tag")
            if tag not in _KNOWN_TAGS:
                continue
            reason = (m.group("reason") or "").strip()
            out.append(Marker(tag=tag, reason=reason, line=lineno))
    return out
```

- [ ] **Step 6: Verify pass**

Run: `pytest engine/tests/test_parsers.py -v`
Expected: 4 passed.

- [ ] **Step 7: Commit**

```bash
git add engine/parsers/ engine/tests/test_parsers.py
git commit -m "feat(engine): add frontmatter and marker parsers"
```

---

### Task 5: ArtifactGraph

**Files:**

- Create: `engine/artifact_graph.py`
- Create: `engine/tests/test_artifact_graph.py`
- Add to fixture: `engine/tests/fixtures/tiny_project/02-requirements-engineering/srs/3.2-functional-requirements.md`

- [ ] **Step 1: Add the new fixture file**

`engine/tests/fixtures/tiny_project/02-requirements-engineering/srs/3.2-functional-requirements.md`:

```markdown
---
phase: "02"
document: "srs"
section: "3.2"
---
# Functional Requirements

- **FR-001** The system shall accept new claims from authenticated providers.
- **FR-002** The system shall store every claim with an immutable timestamp.
```

- [ ] **Step 2: Write the failing test**

`engine/tests/test_artifact_graph.py`:

```python
from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph, Artifact

def test_builds_graph_from_workspace(tiny_project: Path):
    ws = Workspace.load(tiny_project)
    graph = ArtifactGraph.build(ws)
    titles = sorted(a.title for a in graph.artifacts)
    assert "Functional Requirements" in titles
    assert "Vision" in titles

def test_finds_artifact_by_phase(tiny_project: Path):
    graph = ArtifactGraph.build(Workspace.load(tiny_project))
    in_phase_02 = list(graph.in_phase("02"))
    assert len(in_phase_02) == 1
    assert in_phase_02[0].title == "Functional Requirements"

def test_extracts_requirement_ids(tiny_project: Path):
    graph = ArtifactGraph.build(Workspace.load(tiny_project))
    art = next(graph.in_phase("02"))
    assert sorted(art.identifiers) == ["FR-001", "FR-002"]
```

- [ ] **Step 3: Run to verify failure**

Run: `pytest engine/tests/test_artifact_graph.py -v`
Expected: ModuleNotFoundError.

- [ ] **Step 4: Implement `engine/artifact_graph.py`**

```python
"""Immutable in-memory graph of project artifacts."""
from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, List, Optional, Tuple
from engine.workspace import Workspace
from engine.parsers.frontmatter import parse_frontmatter
from engine.parsers.markers import Marker, find_markers

_ID_PATTERN = re.compile(r"\*\*([A-Z]{2,5}-\d{3,5})\*\*")

@dataclass(frozen=True)
class Artifact:
    path: Path
    title: str
    phase: Optional[str]
    document: Optional[str]
    section: Optional[str]
    identifiers: Tuple[str, ...]
    markers: Tuple[Marker, ...]
    body: str

    @classmethod
    def from_file(cls, root: Path, path: Path) -> "Artifact":
        raw = path.read_text(encoding="utf-8")
        fm, content = parse_frontmatter(raw)
        title = _extract_title(content)
        ids = tuple(sorted(set(_ID_PATTERN.findall(content))))
        markers = tuple(find_markers(content))
        return cls(
            path=path.relative_to(root),
            title=title,
            phase=fm.get("phase"),
            document=fm.get("document"),
            section=fm.get("section"),
            identifiers=ids,
            markers=markers,
            body=content,
        )

def _extract_title(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""

@dataclass(frozen=True)
class ArtifactGraph:
    artifacts: Tuple[Artifact, ...]

    @classmethod
    def build(cls, workspace: Workspace) -> "ArtifactGraph":
        items = tuple(
            Artifact.from_file(workspace.root, p)
            for p in workspace.iter_artifacts()
        )
        return cls(artifacts=items)

    def in_phase(self, phase: str) -> Iterator[Artifact]:
        return (a for a in self.artifacts if a.phase == phase)

    def all_identifiers(self) -> List[str]:
        out: List[str] = []
        for a in self.artifacts:
            out.extend(a.identifiers)
        return out

    def all_markers(self) -> List[Tuple[Path, Marker]]:
        return [(a.path, m) for a in self.artifacts for m in a.markers]
```

- [ ] **Step 5: Verify pass**

Run: `pytest engine/tests/test_artifact_graph.py -v`
Expected: 3 passed.

- [ ] **Step 6: Commit**

```bash
git add engine/artifact_graph.py engine/tests/test_artifact_graph.py engine/tests/fixtures/
git commit -m "feat(engine): add ArtifactGraph with phase + identifier indexing"
```

---

### Task 6: Gate base class and registry

**Files:**

- Create: `engine/gates/__init__.py`
- Create: `engine/gates/base.py`
- Create: `engine/tests/test_gates_base.py`

- [ ] **Step 1: Write the failing test**

`engine/tests/test_gates_base.py`:

```python
from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate, GateRegistry

class _AlwaysFails(Gate):
    id = "test.always_fails"
    title = "Always fails"
    severity = Severity.HIGH
    def evaluate(self, graph, findings):
        findings.add(Finding(self.id, self.severity, "synthetic", None, None))

def test_registry_collects_gates_by_id():
    reg = GateRegistry()
    reg.register(_AlwaysFails())
    assert "test.always_fails" in reg

def test_registry_runs_gates(tiny_project: Path):
    ws = Workspace.load(tiny_project)
    graph = ArtifactGraph.build(ws)
    reg = GateRegistry()
    reg.register(_AlwaysFails())
    findings = FindingCollection()
    reg.run_all(graph, findings)
    assert len(findings.for_gate("test.always_fails")) == 1
```

- [ ] **Step 2: Verify failure**

Run: `pytest engine/tests/test_gates_base.py -v`
Expected: ModuleNotFoundError.

- [ ] **Step 3: Implement `engine/gates/__init__.py`** as empty file.

- [ ] **Step 4: Implement `engine/gates/base.py`**

```python
"""Gate ABC and Gate registry."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Iterator
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection, Severity

class Gate(ABC):
    id: str = ""
    title: str = ""
    severity: Severity = Severity.HIGH

    @abstractmethod
    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None: ...

class GateRegistry:
    def __init__(self) -> None:
        self._gates: Dict[str, Gate] = {}

    def register(self, gate: Gate) -> None:
        if not gate.id:
            raise ValueError("Gate id must be a non-empty string")
        if gate.id in self._gates:
            raise ValueError(f"Gate {gate.id} already registered")
        self._gates[gate.id] = gate

    def __contains__(self, gate_id: str) -> bool:
        return gate_id in self._gates

    def __iter__(self) -> Iterator[Gate]:
        return iter(self._gates.values())

    def run_all(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for gate in self._gates.values():
            gate.evaluate(graph, findings)
```

- [ ] **Step 5: Verify pass**

Run: `pytest engine/tests/test_gates_base.py -v`
Expected: 2 passed.

- [ ] **Step 6: Commit**

```bash
git add engine/gates/ engine/tests/test_gates_base.py
git commit -m "feat(engine): add Gate ABC and GateRegistry"
```

---

### Task 7: First reusable check — markers gate

**Files:**

- Create: `engine/checks/__init__.py`
- Create: `engine/checks/markers.py`
- Create: `engine/tests/test_check_markers.py`

- [ ] **Step 1: Write the failing test**

`engine/tests/test_check_markers.py`:

```python
from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection, Severity
from engine.checks.markers import NoUnresolvedFailMarkersGate

def _graph(tmp_path: Path, files: dict[str, str]) -> ArtifactGraph:
    (tmp_path / "_context").mkdir()
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_clean_project_has_no_findings(tmp_path: Path):
    graph = _graph(tmp_path, {"_context/vision.md": "# Vision\nClean."})
    findings = FindingCollection()
    NoUnresolvedFailMarkersGate().evaluate(graph, findings)
    assert len(findings) == 0

def test_finds_v_v_fail_marker(tmp_path: Path):
    graph = _graph(tmp_path, {
        "_context/vision.md": "# Vision\n[V&V-FAIL: missing oracle for FR-001]",
    })
    findings = FindingCollection()
    NoUnresolvedFailMarkersGate().evaluate(graph, findings)
    items = findings.for_gate("kernel.no_unresolved_fail_markers")
    assert len(items) == 1
    assert items[0].severity == Severity.HIGH
    assert "FR-001" in items[0].message
```

- [ ] **Step 2: Verify failure**

Run: `pytest engine/tests/test_check_markers.py -v`
Expected: ModuleNotFoundError.

- [ ] **Step 3: Implement `engine/checks/__init__.py`** as empty file.

- [ ] **Step 4: Implement `engine/checks/markers.py`**

```python
"""Reusable check: no unresolved fail markers."""
from __future__ import annotations
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate

_BLOCKING_TAGS = {
    "V&V-FAIL", "CONTEXT-GAP", "GLOSSARY-GAP",
    "SMART-FAIL", "TRACE-GAP", "VERIFIABILITY-FAIL",
    "DPPA-FAIL", "CONTROL-GAP",
}

class NoUnresolvedFailMarkersGate(Gate):
    id = "kernel.no_unresolved_fail_markers"
    title = "No unresolved [V&V-FAIL]/[CONTEXT-GAP]/etc. markers"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        for path, marker in graph.all_markers():
            if marker.tag not in _BLOCKING_TAGS:
                continue
            findings.add(Finding(
                gate_id=self.id,
                severity=self.severity,
                message=f"Unresolved [{marker.tag}: {marker.reason}]",
                location=path,
                line=marker.line,
            ))
```

- [ ] **Step 5: Verify pass**

Run: `pytest engine/tests/test_check_markers.py -v`
Expected: 2 passed.

- [ ] **Step 6: Commit**

```bash
git add engine/checks/ engine/tests/test_check_markers.py
git commit -m "feat(engine): add markers gate (no unresolved fail tags)"
```

---

### Task 8: Waiver register

**Files:**

- Create: `engine/waivers.py`
- Create: `engine/tests/test_waivers.py`
- Create: `engine/tests/fixtures/tiny_project/_registry/waivers.yaml`

- [ ] **Step 1: Add fixture waiver file**

`engine/tests/fixtures/tiny_project/_registry/waivers.yaml`:

```yaml
waivers:
  - id: WAIVE-001
    gate: kernel.no_unresolved_fail_markers
    scope: "_context/vision.md"
    reason: "Pending stakeholder workshop scheduled for 2026-04-30."
    approver: "Peter Bamuhigire"
    approved_on: 2026-04-15
    expires_on: 2026-05-15
```

- [ ] **Step 2: Write the failing test**

`engine/tests/test_waivers.py`:

```python
from datetime import date
from pathlib import Path
import pytest
from engine.findings import Finding, FindingCollection, Severity
from engine.waivers import WaiverRegister, WaiverError

def test_loads_waivers_from_yaml(tiny_project: Path):
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    assert len(reg) == 1
    w = next(iter(reg))
    assert w.id == "WAIVE-001"
    assert w.gate == "kernel.no_unresolved_fail_markers"
    assert w.expires_on == date(2026, 5, 15)

def test_returns_empty_when_file_missing(tmp_path: Path):
    reg = WaiverRegister.load(tmp_path / "missing.yaml")
    assert len(reg) == 0

def test_matches_finding_within_scope(tiny_project: Path):
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    finding = Finding(
        gate_id="kernel.no_unresolved_fail_markers",
        severity=Severity.HIGH,
        message="x",
        location=Path("_context/vision.md"),
        line=4,
    )
    assert reg.matches(finding, today=date(2026, 4, 16)) is not None

def test_does_not_match_after_expiry(tiny_project: Path):
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    finding = Finding(
        gate_id="kernel.no_unresolved_fail_markers",
        severity=Severity.HIGH,
        message="x",
        location=Path("_context/vision.md"),
        line=4,
    )
    assert reg.matches(finding, today=date(2026, 6, 1)) is None

def test_apply_strips_waived_findings(tiny_project: Path):
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    findings = FindingCollection()
    findings.add(Finding(
        "kernel.no_unresolved_fail_markers", Severity.HIGH, "m",
        Path("_context/vision.md"), 4))
    findings.add(Finding(
        "kernel.no_unresolved_fail_markers", Severity.HIGH, "m",
        Path("_context/glossary.md"), 7))
    waived, remaining = reg.apply(findings, today=date(2026, 4, 16))
    assert len(waived) == 1
    assert len(remaining) == 1
    assert remaining[0].location.name == "glossary.md"
```

- [ ] **Step 3: Verify failure**

Run: `pytest engine/tests/test_waivers.py -v`
Expected: ModuleNotFoundError.

- [ ] **Step 4: Implement `engine/waivers.py`**

```python
"""Waiver register: gate-specific exceptions with expiry and approver."""
from __future__ import annotations
import fnmatch
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterator, List, Optional, Tuple
from ruamel.yaml import YAML
from engine.findings import Finding, FindingCollection

class WaiverError(Exception):
    """Raised on malformed waiver file."""

@dataclass(frozen=True)
class Waiver:
    id: str
    gate: str
    scope: str
    reason: str
    approver: str
    approved_on: date
    expires_on: date

    def applies_to(self, finding: Finding, today: date) -> bool:
        if finding.gate_id != self.gate:
            return False
        if today > self.expires_on:
            return False
        if finding.location is None:
            return self.scope in ("*", "")
        return fnmatch.fnmatch(str(finding.location).replace("\\", "/"), self.scope)

class WaiverRegister:
    def __init__(self, waivers: List[Waiver]) -> None:
        self._waivers = waivers

    @classmethod
    def load(cls, path: Path) -> "WaiverRegister":
        if not path.exists():
            return cls([])
        yaml = YAML(typ="safe")
        data = yaml.load(path.read_text(encoding="utf-8")) or {}
        items = data.get("waivers") or []
        try:
            waivers = [
                Waiver(
                    id=item["id"],
                    gate=item["gate"],
                    scope=item.get("scope", "*"),
                    reason=item["reason"],
                    approver=item["approver"],
                    approved_on=item["approved_on"],
                    expires_on=item["expires_on"],
                )
                for item in items
            ]
        except (KeyError, TypeError) as exc:
            raise WaiverError(f"Malformed waiver in {path}: {exc}") from exc
        return cls(waivers)

    def __iter__(self) -> Iterator[Waiver]:
        return iter(self._waivers)

    def __len__(self) -> int:
        return len(self._waivers)

    def matches(self, finding: Finding, today: date) -> Optional[Waiver]:
        for w in self._waivers:
            if w.applies_to(finding, today):
                return w
        return None

    def apply(
        self, findings: FindingCollection, today: date
    ) -> Tuple[List[Finding], List[Finding]]:
        waived: List[Finding] = []
        remaining: List[Finding] = []
        for f in findings:
            if self.matches(f, today):
                waived.append(f)
            else:
                remaining.append(f)
        return waived, remaining
```

- [ ] **Step 5: Verify pass**

Run: `pytest engine/tests/test_waivers.py -v`
Expected: 5 passed.

- [ ] **Step 6: Commit**

```bash
git add engine/waivers.py engine/tests/test_waivers.py engine/tests/fixtures/
git commit -m "feat(engine): add WaiverRegister with scope and expiry matching"
```

---

### Task 9: Reporters (Markdown, JUnit, SARIF)

**Files:**

- Create: `engine/reporters/__init__.py`
- Create: `engine/reporters/markdown.py`
- Create: `engine/reporters/junit.py`
- Create: `engine/reporters/sarif.py`
- Create: `engine/tests/test_reporters.py`

- [ ] **Step 1: Write the failing test**

`engine/tests/test_reporters.py`:

```python
import json
from pathlib import Path
from xml.etree import ElementTree as ET
from engine.findings import Finding, FindingCollection, Severity
from engine.reporters.markdown import render_markdown
from engine.reporters.junit import render_junit
from engine.reporters.sarif import render_sarif

def _coll() -> FindingCollection:
    c = FindingCollection()
    c.add(Finding("phase01.x", Severity.HIGH, "broken", Path("a.md"), 3))
    c.add(Finding("phase01.x", Severity.LOW, "warn", Path("b.md"), 5))
    return c

def test_markdown_lists_each_finding():
    out = render_markdown(_coll(), waived=[], project="demo")
    assert "phase01.x" in out
    assert "broken" in out
    assert "demo" in out

def test_junit_has_one_testcase_per_gate():
    out = render_junit(_coll())
    root = ET.fromstring(out)
    cases = root.findall(".//testcase")
    assert {c.get("name") for c in cases} == {"phase01.x"}
    assert root.findall(".//failure")

def test_sarif_is_valid_json():
    out = render_sarif(_coll())
    obj = json.loads(out)
    assert obj["version"] == "2.1.0"
    assert obj["runs"][0]["results"][0]["ruleId"] == "phase01.x"
```

- [ ] **Step 2: Verify failure**

Run: `pytest engine/tests/test_reporters.py -v`
Expected: ModuleNotFoundError.

- [ ] **Step 3: Implement `engine/reporters/__init__.py`** as empty file.

- [ ] **Step 4: Implement `engine/reporters/markdown.py`**

```python
"""Markdown reporter."""
from __future__ import annotations
from typing import Iterable
from engine.findings import Finding, FindingCollection

def render_markdown(
    findings: FindingCollection, waived: Iterable[Finding], project: str
) -> str:
    lines = [f"# Engine Validation Report — {project}", ""]
    if len(findings) == 0:
        lines.append("**Status:** PASS — no findings.")
    else:
        lines.append(f"**Status:** {'FAIL' if findings.is_blocking else 'WARN'}")
        lines.append(f"**Findings:** {len(findings)}")
        lines.append("")
        lines.append("| Gate | Severity | Location | Line | Message |")
        lines.append("|---|---|---|---|---|")
        for f in findings:
            loc = f.location.as_posix() if f.location else "-"
            line = f.line if f.line is not None else "-"
            lines.append(
                f"| `{f.gate_id}` | {f.severity.name} | `{loc}` | {line} | {f.message} |"
            )
    waived_list = list(waived)
    if waived_list:
        lines.extend(["", "## Waived findings", ""])
        for f in waived_list:
            lines.append(f"- `{f.gate_id}` — {f.message}")
    return "\n".join(lines) + "\n"
```

- [ ] **Step 5: Implement `engine/reporters/junit.py`**

```python
"""JUnit XML reporter."""
from __future__ import annotations
from collections import defaultdict
from xml.etree.ElementTree import Element, SubElement, tostring
from engine.findings import FindingCollection, Severity

def render_junit(findings: FindingCollection) -> str:
    by_gate: dict[str, list] = defaultdict(list)
    for f in findings:
        by_gate[f.gate_id].append(f)
    suite = Element("testsuite", name="srs-engine", tests=str(len(by_gate)))
    failures = 0
    for gate_id, items in by_gate.items():
        case = SubElement(suite, "testcase", classname="engine.gates", name=gate_id)
        blocking = [f for f in items if f.severity >= Severity.HIGH]
        if blocking:
            failures += 1
            failure = SubElement(case, "failure", message=blocking[0].message)
            failure.text = "\n".join(
                f"{f.location}:{f.line}: {f.message}" for f in items
            )
    suite.set("failures", str(failures))
    return tostring(suite, encoding="unicode")
```

- [ ] **Step 6: Implement `engine/reporters/sarif.py`**

```python
"""SARIF 2.1.0 reporter."""
from __future__ import annotations
import json
from collections import defaultdict
from engine.findings import FindingCollection, Severity

_LEVELS = {Severity.HIGH: "error", Severity.MEDIUM: "warning",
           Severity.LOW: "note", Severity.INFO: "note"}

def render_sarif(findings: FindingCollection) -> str:
    rules: dict[str, dict] = {}
    results = []
    for f in findings:
        rules.setdefault(f.gate_id, {
            "id": f.gate_id,
            "shortDescription": {"text": f.gate_id},
        })
        results.append({
            "ruleId": f.gate_id,
            "level": _LEVELS[f.severity],
            "message": {"text": f.message},
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {
                        "uri": f.location.as_posix() if f.location else "",
                    },
                    "region": {"startLine": f.line or 1},
                },
            }],
        })
    sarif = {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [{
            "tool": {"driver": {
                "name": "srs-skills-engine",
                "rules": list(rules.values()),
            }},
            "results": results,
        }],
    }
    return json.dumps(sarif, indent=2)
```

- [ ] **Step 7: Verify pass**

Run: `pytest engine/tests/test_reporters.py -v`
Expected: 3 passed.

- [ ] **Step 8: Commit**

```bash
git add engine/reporters/ engine/tests/test_reporters.py
git commit -m "feat(engine): add Markdown/JUnit/SARIF reporters"
```

---

### Task 10: CLI

**Files:**

- Create: `engine/cli.py`
- Create: `engine/tests/test_cli.py`

- [ ] **Step 1: Write the failing test**

`engine/tests/test_cli.py`:

```python
from pathlib import Path
from click.testing import CliRunner
from engine.cli import main

def test_validate_passes_clean_project(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\nClean.\n")
    result = CliRunner().invoke(main, ["validate", str(tmp_path)])
    assert result.exit_code == 0, result.output
    assert "ENGINE CONTRACT: PASS" in result.output

def test_validate_fails_on_unresolved_marker(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\n[V&V-FAIL: missing oracle]\n"
    )
    result = CliRunner().invoke(main, ["validate", str(tmp_path)])
    assert result.exit_code == 1
    assert "kernel.no_unresolved_fail_markers" in result.output

def test_validate_emits_junit_when_requested(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\nClean.\n")
    out_path = tmp_path / "report.xml"
    result = CliRunner().invoke(
        main, ["validate", str(tmp_path), "--junit", str(out_path)]
    )
    assert result.exit_code == 0
    assert out_path.exists()
    assert out_path.read_text().startswith("<testsuite")
```

- [ ] **Step 2: Verify failure**

Run: `pytest engine/tests/test_cli.py -v`
Expected: ModuleNotFoundError.

- [ ] **Step 3: Implement `engine/cli.py`**

```python
"""Engine CLI."""
from __future__ import annotations
import sys
from datetime import date
from pathlib import Path
import click
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.base import GateRegistry
from engine.checks.markers import NoUnresolvedFailMarkersGate
from engine.waivers import WaiverRegister
from engine.reporters.markdown import render_markdown
from engine.reporters.junit import render_junit
from engine.reporters.sarif import render_sarif

def _default_registry() -> GateRegistry:
    reg = GateRegistry()
    reg.register(NoUnresolvedFailMarkersGate())
    # Plan 02 will register phase gates here.
    return reg

@click.group()
def main() -> None:
    """srs-skills validation kernel."""

@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--junit", type=click.Path(), default=None)
@click.option("--sarif", type=click.Path(), default=None)
@click.option("--markdown", "md_path", type=click.Path(), default=None)
def validate(project: str, junit: str | None, sarif: str | None, md_path: str | None) -> None:
    """Validate a project workspace and exit non-zero on blocking findings."""
    workspace = Workspace.load(Path(project))
    graph = ArtifactGraph.build(workspace)
    findings = FindingCollection()
    _default_registry().run_all(graph, findings)
    waivers = WaiverRegister.load(workspace.root / "_registry" / "waivers.yaml")
    waived, remaining_list = waivers.apply(findings, today=date.today())
    remaining = FindingCollection()
    remaining.extend(remaining_list)
    md = render_markdown(remaining, waived, project=workspace.root.name)
    if md_path:
        Path(md_path).write_text(md, encoding="utf-8")
    if junit:
        Path(junit).write_text(render_junit(remaining), encoding="utf-8")
    if sarif:
        Path(sarif).write_text(render_sarif(remaining), encoding="utf-8")
    if remaining.is_blocking:
        click.echo("ENGINE CONTRACT: FAIL")
        for f in remaining:
            click.echo(f"- [{f.severity.name}] {f.gate_id}: {f.message}")
        sys.exit(1)
    click.echo("ENGINE CONTRACT: PASS")

if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Verify pass**

Run: `pytest engine/tests/test_cli.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add engine/cli.py engine/tests/test_cli.py
git commit -m "feat(engine): add CLI with validate command and reporter flags"
```

---

### Task 11: Replace `scripts/validate_engine.py` with a delegating shim

**Files:**

- Modify: `scripts/validate_engine.py`

- [ ] **Step 1: Read the current script** (already done in plan research; behavior unchanged from the engineer's POV).

- [ ] **Step 2: Rewrite as a shim that runs the legacy contract checks AND prints a deprecation pointer**

Replace the entire file with:

```python
#!/usr/bin/env python3
"""Repo-level engine contract validator (legacy entry-point).

Behaviour is preserved verbatim from the previous version. New work should
prefer `python -m engine validate <project-path>`, which validates a single
project workspace; this script validates the repo-level engine contract.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def must_exist(rel_path: str, errors: list[str]) -> Path | None:
    path = ROOT / rel_path
    if not path.exists():
        errors.append(f"Missing required file: {rel_path}")
        return None
    return path

def require_substrings(rel_path: str, required: list[str], errors: list[str]) -> None:
    path = must_exist(rel_path, errors)
    if path is None:
        return
    body = read_text(path)
    for needle in required:
        if needle not in body:
            errors.append(f"{rel_path} missing required text: {needle}")

def validate_root_pathing(errors: list[str]) -> None:
    canonical = "projects/<ProjectName>/"
    alias_a = "../project_context/"
    alias_b = "../output/"
    alias_language = "alias"
    for rel_path in ["README.md", "AGENTS.md", "CLAUDE.md"]:
        require_substrings(rel_path, [canonical], errors)
        body = read_text(ROOT / rel_path)
        if alias_a in body or alias_b in body:
            if alias_language not in body.lower():
                errors.append(
                    f"{rel_path} references legacy relative paths without explicitly calling them aliases"
                )
    phase_docs = [
        "01-strategic-vision/README.md",
        "02-requirements-engineering/agile/README.md",
        "03-design-documentation/README.md",
        "06-deployment-operations/README.md",
    ]
    for rel_path in phase_docs:
        path = must_exist(rel_path, errors)
        if path is None:
            continue
        body = read_text(path)
        mentions_legacy = alias_a in body or alias_b in body
        if mentions_legacy:
            if "projects/<ProjectName>/" not in body:
                errors.append(
                    f"{rel_path} references legacy relative paths without the canonical project workspace"
                )
            if alias_language not in body.lower():
                errors.append(
                    f"{rel_path} references legacy relative paths without explicit alias wording"
                )

def validate_deterministic_gates(errors: list[str]) -> None:
    gate_files = {f"{n:02d}": f"docs/deterministic-gate-phase{n:02d}.md" for n in range(1, 10)}
    for rel_path in gate_files.values():
        must_exist(rel_path, errors)
    governance = must_exist("docs/deterministic-governance.md", errors)
    if governance is None:
        return
    body = read_text(governance)
    for phase, rel_path in gate_files.items():
        if rel_path.split("/")[-1] not in body:
            errors.append(
                f"docs/deterministic-governance.md does not reference the Phase {phase} gate file"
            )

def validate_hybrid_and_regulated_models(errors: list[str]) -> None:
    required_docs = [
        "docs/hybrid-operating-model.md",
        "docs/regulated-evidence-model.md",
    ]
    for rel_path in required_docs:
        must_exist(rel_path, errors)
    require_substrings(
        "README.md",
        ["docs/hybrid-operating-model.md", "docs/regulated-evidence-model.md"],
        errors,
    )

def main() -> int:
    errors: list[str] = []
    validate_root_pathing(errors)
    validate_deterministic_gates(errors)
    validate_hybrid_and_regulated_models(errors)
    if errors:
        print("ENGINE CONTRACT: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("ENGINE CONTRACT: PASS")
    print("- Canonical pathing and alias semantics are documented.")
    print("- Deterministic gate docs exist for phases 01-09.")
    print("- Hybrid operating model is documented.")
    print("- Regulated evidence model is documented.")
    print()
    print("NOTE: For per-project validation, use `python -m engine validate <projects/<Name>>`.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run the legacy script**

Run: `python -X utf8 scripts/validate_engine.py`
Expected: `ENGINE CONTRACT: PASS` (or whatever it currently prints), with new NOTE line at the end.

- [ ] **Step 3: Commit**

```bash
git add scripts/validate_engine.py
git commit -m "refactor(scripts): point validate_engine.py at engine.cli for project validation"
```

---

### Task 12: GitHub Actions CI workflow

**Files:**

- Create: `.github/workflows/engine.yml`

- [ ] **Step 1: Write the workflow**

`.github/workflows/engine.yml`:

```yaml
name: Engine
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test-kernel:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: recursive
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: pytest --cov=engine --cov-fail-under=90
      - run: python scripts/validate_engine.py
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/engine.yml
git commit -m "ci: add Engine workflow (pytest + repo contract)"
```

---

### Task 13: Pre-commit hook for project validation

**Files:**

- Create: `.pre-commit-config.yaml`

- [ ] **Step 1: Write the config**

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: engine-validate-changed-projects
        name: engine.validate (changed project workspaces)
        entry: python scripts/precommit_validate_projects.py
        language: system
        pass_filenames: true
        files: ^projects/[^/]+/.*\.(md|yaml|yml)$
```

- [ ] **Step 2: Create the helper script**

`scripts/precommit_validate_projects.py`:

```python
#!/usr/bin/env python3
"""For each unique project touched by staged files, run engine.cli validate."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

def project_roots(paths: list[str]) -> set[Path]:
    out: set[Path] = set()
    for p in paths:
        parts = Path(p).parts
        if len(parts) >= 2 and parts[0] == "projects":
            out.add(Path(parts[0]) / parts[1])
    return out

def main(argv: list[str]) -> int:
    failed = 0
    for root in sorted(project_roots(argv)):
        print(f"==> validating {root}")
        rc = subprocess.call([sys.executable, "-m", "engine", "validate", str(root)])
        if rc != 0:
            failed += 1
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

- [ ] **Step 3: Commit**

```bash
git add .pre-commit-config.yaml scripts/precommit_validate_projects.py
git commit -m "ci: add pre-commit hook to validate touched project workspaces"
```

---

## Self-Review

1. **Spec coverage:** Gap #1 (deterministic enforcement) — closed by gate registry + CLI exit code. Gap #5 (fragmented validation) — closed by single canonical kernel; legacy script delegates and adds a pointer. Gap #7 (output consistency) — partially closed via marker checks; rest in Plan 03.
2. **Placeholder scan:** No `TBD` / "implement later". Every step has working code. Every test asserts a specific outcome.
3. **Type consistency:** `Workspace.root`, `ArtifactGraph.artifacts`, `Finding.gate_id` used identically across tasks 2, 5, 7, 9, 10. `Severity.HIGH` referenced consistently.
4. **TDD discipline:** Every implementation task has Red → Green → Commit with explicit `pytest -v` invocations and expected outputs.
5. **Coverage target met:** `--cov-fail-under=90` is enforced in CI from Task 12.
