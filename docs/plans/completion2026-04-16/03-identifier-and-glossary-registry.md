# Identifier & Glossary Registry Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans.

**Goal:** Eliminate identifier drift, terminology drift, and duplicated thresholds by storing project identifiers and glossary terms in machine-readable registries (`projects/<X>/_registry/identifiers.yaml` and `_registry/glossary.yaml`), populating them from project artifacts via a `sync` command, and enforcing uniqueness + cross-reference completeness via kernel checks. Closes Gap #7.

**Architecture:** Two YAML registries with JSON Schemas. A `python -m engine sync <project>` command parses every artifact, extracts identifiers and glossary entries, writes the registries, and aborts if it detects collisions. Two new checks (`IdentifierRegistryCheck`, `GlossaryRegistryCheck`) compare the registry against artifact contents and raise Findings on drift.

**Tech Stack:** Same as Plan 01 (`ruamel.yaml`, `jsonschema`).

---

## File Structure

```
engine/
├── registry/
│   ├── __init__.py
│   ├── identifiers.py       # IdentifierRegistry (load/save/validate)
│   ├── glossary.py          # GlossaryRegistry
│   └── schemas/
│       ├── identifiers.schema.json
│       └── glossary.schema.json
├── checks/
│   ├── identifier_registry.py
│   └── glossary_registry.py
├── cli.py                    # Add `sync` subcommand
└── tests/
    ├── test_registry_identifiers.py
    ├── test_registry_glossary.py
    ├── test_check_identifier_registry.py
    ├── test_check_glossary_registry.py
    └── test_cli_sync.py

projects/<X>/_registry/
├── identifiers.yaml
└── glossary.yaml
```

---

### Task 1: Identifier registry schema and loader

**Files:**

- Create: `engine/registry/__init__.py` (empty)
- Create: `engine/registry/schemas/identifiers.schema.json`
- Create: `engine/registry/identifiers.py`
- Create: `engine/tests/test_registry_identifiers.py`

- [ ] **Step 1: Write the schema**

`engine/registry/schemas/identifiers.schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Project identifier registry",
  "type": "object",
  "required": ["identifiers"],
  "properties": {
    "identifiers": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "kind", "defined_in"],
        "properties": {
          "id": {"type": "string", "pattern": "^[A-Z]{2,5}-\\d{3,5}$"},
          "kind": {"enum": ["BG", "FR", "NFR", "US", "TC", "CTRL", "RISK", "ADR", "WAIVE"]},
          "defined_in": {"type": "string"},
          "title": {"type": "string"},
          "links": {"type": "array", "items": {"type": "string"}}
        },
        "additionalProperties": false
      }
    }
  }
}
```

- [ ] **Step 2: Failing test**

```python
from pathlib import Path
import pytest
from engine.registry.identifiers import IdentifierRegistry, IdentifierEntry, RegistryError

def test_loads_valid_registry(tmp_path: Path):
    yaml = """\
identifiers:
  - id: FR-001
    kind: FR
    defined_in: 02-requirements-engineering/srs/3.2.md
    title: Submit claim
    links: [BG-001, TC-001]
"""
    p = tmp_path / "identifiers.yaml"
    p.write_text(yaml)
    reg = IdentifierRegistry.load(p)
    assert len(reg) == 1
    assert reg["FR-001"].title == "Submit claim"

def test_rejects_duplicate_ids(tmp_path: Path):
    yaml = """\
identifiers:
  - id: FR-001
    kind: FR
    defined_in: a.md
  - id: FR-001
    kind: FR
    defined_in: b.md
"""
    p = tmp_path / "identifiers.yaml"
    p.write_text(yaml)
    with pytest.raises(RegistryError) as exc:
        IdentifierRegistry.load(p)
    assert "duplicate" in str(exc.value).lower()

def test_rejects_invalid_id_format(tmp_path: Path):
    yaml = "identifiers:\n  - id: notvalid\n    kind: FR\n    defined_in: a.md\n"
    p = tmp_path / "identifiers.yaml"
    p.write_text(yaml)
    with pytest.raises(RegistryError):
        IdentifierRegistry.load(p)
```

- [ ] **Step 3: Implement**

```python
"""Identifier registry for a project."""
from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Tuple
import jsonschema
from ruamel.yaml import YAML

class RegistryError(Exception):
    """Malformed or inconsistent registry."""

@dataclass(frozen=True)
class IdentifierEntry:
    id: str
    kind: str
    defined_in: str
    title: str = ""
    links: Tuple[str, ...] = ()

_SCHEMA = json.loads(
    (Path(__file__).parent / "schemas" / "identifiers.schema.json").read_text()
)
_yaml = YAML(typ="safe")

class IdentifierRegistry:
    def __init__(self, entries: dict[str, IdentifierEntry]) -> None:
        self._entries = entries

    @classmethod
    def load(cls, path: Path) -> "IdentifierRegistry":
        if not path.exists():
            return cls({})
        data = _yaml.load(path.read_text(encoding="utf-8")) or {"identifiers": []}
        try:
            jsonschema.validate(data, _SCHEMA)
        except jsonschema.ValidationError as exc:
            raise RegistryError(f"Schema violation in {path}: {exc.message}") from exc
        entries: dict[str, IdentifierEntry] = {}
        for item in data["identifiers"]:
            if item["id"] in entries:
                raise RegistryError(f"Duplicate identifier: {item['id']}")
            entries[item["id"]] = IdentifierEntry(
                id=item["id"],
                kind=item["kind"],
                defined_in=item["defined_in"],
                title=item.get("title", ""),
                links=tuple(item.get("links", [])),
            )
        return cls(entries)

    def save(self, path: Path) -> None:
        items = [
            {"id": e.id, "kind": e.kind, "defined_in": e.defined_in,
             "title": e.title, "links": list(e.links)}
            for e in self._entries.values()
        ]
        _yaml.dump({"identifiers": items}, path.open("w", encoding="utf-8"))

    def __len__(self) -> int:
        return len(self._entries)

    def __getitem__(self, ident: str) -> IdentifierEntry:
        return self._entries[ident]

    def __iter__(self) -> Iterator[IdentifierEntry]:
        return iter(self._entries.values())
```

- [ ] **Step 4: Verify pass + commit**

```bash
pytest engine/tests/test_registry_identifiers.py -v
git add engine/registry/ engine/tests/test_registry_identifiers.py
git commit -m "feat(engine): add IdentifierRegistry with schema validation"
```

---

### Task 2: Glossary registry (mirror of Task 1)

**Files:**

- Create: `engine/registry/schemas/glossary.schema.json`
- Create: `engine/registry/glossary.py`
- Create: `engine/tests/test_registry_glossary.py`

- [ ] **Step 1: Schema**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["terms"],
  "properties": {
    "terms": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["term", "definition"],
        "properties": {
          "term": {"type": "string", "minLength": 2},
          "definition": {"type": "string", "minLength": 5},
          "source": {"type": "string"},
          "first_introduced_in": {"type": "string"}
        },
        "additionalProperties": false
      }
    }
  }
}
```

- [ ] **Step 2: Failing test then implement** following the same pattern as Task 1. Tests assert: load round-trip, reject duplicate term (case-insensitive), reject empty definition.

- [ ] **Step 3: Commit**

---

### Task 3: `engine sync` command

**Files:**

- Modify: `engine/cli.py` (add `sync` group)
- Create: `engine/sync.py`
- Create: `engine/tests/test_cli_sync.py`

The sync command parses every `*.md` artifact in the project, extracts every `**XX-NNN**` identifier and every `**Term:**` glossary entry, and writes the registries. Collisions abort with exit code 1.

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
from click.testing import CliRunner
from engine.cli import main
from engine.registry.identifiers import IdentifierRegistry

def test_sync_extracts_ids_from_artifacts(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\n- **BG-001** Cycle ≤ 3 days")
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text("---\nphase: '02'\n---\n- **FR-001** trace BG-001")
    rc = CliRunner().invoke(main, ["sync", str(tmp_path)])
    assert rc.exit_code == 0, rc.output
    reg = IdentifierRegistry.load(tmp_path / "_registry" / "identifiers.yaml")
    assert "FR-001" in {e.id for e in reg}
    assert "BG-001" in {e.id for e in reg}

def test_sync_aborts_on_collision(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/a.md").write_text("- **FR-001** in a")
    (tmp_path / "_context/b.md").write_text("- **FR-001** in b")
    rc = CliRunner().invoke(main, ["sync", str(tmp_path)])
    assert rc.exit_code == 1
    assert "FR-001" in rc.output
```

- [ ] **Step 2: Implement `engine/sync.py`**

```python
"""Extract identifiers and glossary terms into _registry/."""
from __future__ import annotations
import re
from collections import defaultdict
from pathlib import Path
from typing import Tuple
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph, Artifact
from engine.registry.identifiers import IdentifierEntry, IdentifierRegistry, RegistryError
from engine.registry.glossary import GlossaryRegistry, GlossaryEntry

_ID = re.compile(r"\*\*([A-Z]{2,5}-\d{3,5})\*\*\s*(.*)")
_TERM = re.compile(r"-\s+\*\*([A-Z][A-Za-z0-9_-]{1,40}):\*\*\s+(.+)")
_KIND_PREFIXES = {"BG": "BG", "FR": "FR", "NFR": "NFR", "US": "US", "TC": "TC",
                  "CTRL": "CTRL", "RISK": "RISK", "ADR": "ADR", "WAIVE": "WAIVE"}

def sync(workspace: Workspace) -> Tuple[IdentifierRegistry, GlossaryRegistry, list[str]]:
    graph = ArtifactGraph.build(workspace)
    seen: dict[str, list[Artifact]] = defaultdict(list)
    titles: dict[str, str] = {}
    glossary: dict[str, GlossaryEntry] = {}
    for art in graph.artifacts:
        for line in art.body.splitlines():
            for m in _ID.finditer(line):
                ident = m.group(1)
                seen[ident].append(art)
                if ident not in titles:
                    titles[ident] = m.group(2).strip()[:120]
            for m in _TERM.finditer(line):
                term = m.group(1)
                key = term.lower()
                if key in glossary:
                    continue  # first occurrence wins
                glossary[key] = GlossaryEntry(
                    term=term,
                    definition=m.group(2).strip(),
                    source="",
                    first_introduced_in=str(art.path),
                )
    errors: list[str] = []
    entries: dict[str, IdentifierEntry] = {}
    for ident, arts in seen.items():
        if len(arts) > 1:
            paths = ", ".join(str(a.path) for a in arts)
            errors.append(f"Identifier collision: {ident} appears in {paths}")
            continue
        kind_prefix = ident.split("-")[0]
        entries[ident] = IdentifierEntry(
            id=ident,
            kind=_KIND_PREFIXES.get(kind_prefix, kind_prefix),
            defined_in=str(arts[0].path),
            title=titles.get(ident, ""),
        )
    return IdentifierRegistry(entries), GlossaryRegistry(glossary), errors
```

- [ ] **Step 3: Wire up `engine.cli.sync`**

Add to `engine/cli.py`:

```python
@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
def sync(project: str) -> None:
    """Populate _registry/identifiers.yaml and _registry/glossary.yaml."""
    from engine.sync import sync as do_sync
    ws = Workspace.load(Path(project))
    ids, gloss, errors = do_sync(ws)
    if errors:
        for e in errors:
            click.echo(e)
        sys.exit(1)
    reg_dir = ws.root / "_registry"
    reg_dir.mkdir(exist_ok=True)
    ids.save(reg_dir / "identifiers.yaml")
    gloss.save(reg_dir / "glossary.yaml")
    click.echo(f"Wrote {len(ids)} identifiers and {len(gloss)} glossary terms.")
```

- [ ] **Step 4: Verify pass + commit**

---

### Task 4: `IdentifierRegistryCheck`

Validates that every identifier mentioned in any artifact is in the registry, and every registry entry is mentioned in at least one artifact (no orphans).

**Files:**

- Create: `engine/checks/identifier_registry.py`
- Create: `engine/tests/test_check_identifier_registry.py`

- [ ] **Step 1: Failing test asserting**

  - Pass when every artifact ID is in the registry.
  - Flag when artifact references `FR-999` not in registry.
  - Flag when registry has `FR-001` but no artifact mentions it.

- [ ] **Step 2: Implement**

```python
"""Identifier registry check."""
from __future__ import annotations
from pathlib import Path
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.registry.identifiers import IdentifierRegistry

class IdentifierRegistryCheck:
    def __init__(self, gate_id: str, registry_path: Path) -> None:
        self.gate_id = gate_id
        self._registry = IdentifierRegistry.load(registry_path)

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        registry_ids = {e.id for e in self._registry}
        artifact_ids = set(graph.all_identifiers())
        for ident in artifact_ids - registry_ids:
            findings.add(Finding(
                gate_id=f"{self.gate_id}.unknown_id",
                severity=Severity.HIGH,
                message=f"Artifact references {ident} but it is not in _registry/identifiers.yaml",
                location=None, line=None,
            ))
        for ident in registry_ids - artifact_ids:
            findings.add(Finding(
                gate_id=f"{self.gate_id}.orphan_id",
                severity=Severity.MEDIUM,
                message=f"Registry contains {ident} but no artifact references it",
                location=None, line=None,
            ))
```

- [ ] **Step 3: Wire into Phase 02 and Phase 09 gates** by adding `IdentifierRegistryCheck("phase09.id_registry", ws.root/"_registry/identifiers.yaml").run(graph, findings)` inside each gate's `evaluate`.

- [ ] **Step 4: Commit**

---

### Task 5: `GlossaryRegistryCheck`

Mirror of Task 4 for glossary terms. Asserts:

- Every domain-specific term used in artifacts (case-sensitive ≥ 2 occurrences across distinct files) is in the glossary.
- No glossary term is unused.

- [ ] **Step 1: Failing test → implement → commit** following Task 4 pattern.

---

### Task 6: NFR threshold deduplication check

**Files:**

- Create: `engine/checks/nfr_threshold_dedup.py`
- Create: `engine/tests/test_check_nfr_threshold_dedup.py`

Catches contradictions like NFR-001 saying "≤ 500 ms" and NFR-007 saying "≤ 1 second" for the same metric ("response time").

- [ ] **Step 1: Failing test asserting both NFR IDs are reported when their metric matches.**

- [ ] **Step 2: Implement** by parsing each NFR for `(metric_phrase, comparator, value, unit)`, normalising units to a base, and grouping by metric_phrase. Any group with ≥ 2 distinct values raises a Finding listing every contradicting ID.

- [ ] **Step 3: Wire into Phase 02 gate; commit**

---

### Task 7: Update CLAUDE.md V&V SOP

**Files:**

- Modify: `CLAUDE.md`

- [ ] **Step 1: Append a new section** under "V&V Standard Operating Procedure":

```markdown
### Project Registries

Every project workspace MUST contain `_registry/identifiers.yaml` and `_registry/glossary.yaml`. Generate or refresh them with:

```bash
python -m engine sync projects/<ProjectName>
```

Manual edits to these files are allowed for `links:` and `title:` fields. Identifier `id`, `kind`, and `defined_in` fields are derived from the artifacts and will be overwritten on the next sync.

The validation kernel (`python -m engine validate <project>`) will fail if:

- An artifact references an ID that is not in `identifiers.yaml`.
- A registry entry is orphaned (no artifact mentions it).
- A glossary term is used in artifacts but missing from `glossary.yaml`.
```

- [ ] **Step 2: Commit**

---

## Self-Review

1. **Spec coverage:** Identifier drift (`unknown_id`, `orphan_id`), terminology drift (`GlossaryRegistryCheck`), and threshold contradictions (`NfrThresholdDedupCheck`) are each closed by one machine-checkable rule.
2. **Placeholder scan:** None.
3. **Type consistency:** `IdentifierEntry` and `GlossaryEntry` use the same dataclass-frozen pattern as the kernel's other dataclasses. `RegistryError` mirrors `WaiverError` from Plan 01.
4. **Round-tripping:** YAML files are loaded and saved through the same `ruamel.yaml` configuration; format stays stable across sync cycles.
