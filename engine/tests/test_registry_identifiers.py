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
