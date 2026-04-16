from pathlib import Path
import pytest
from engine.registry.glossary import GlossaryRegistry, GlossaryEntry
from engine.registry.identifiers import RegistryError


def test_loads_valid_registry(tmp_path: Path):
    yaml = """\
terms:
  - term: Claim
    definition: A formal request for payment against an insurance policy.
    source: IEEE 610.12
    first_introduced_in: 02-requirements-engineering/srs/3.2.md
"""
    p = tmp_path / "glossary.yaml"
    p.write_text(yaml)
    reg = GlossaryRegistry.load(p)
    assert len(reg) == 1
    # Case-insensitive lookup
    assert reg["Claim"].definition.startswith("A formal request")
    assert reg["claim"].term == "Claim"


def test_rejects_duplicate_terms_case_insensitive(tmp_path: Path):
    yaml = """\
terms:
  - term: Claim
    definition: A formal request for payment.
  - term: claim
    definition: A different definition for the same term.
"""
    p = tmp_path / "glossary.yaml"
    p.write_text(yaml)
    with pytest.raises(RegistryError) as exc:
        GlossaryRegistry.load(p)
    assert "duplicate" in str(exc.value).lower()


def test_rejects_empty_definition(tmp_path: Path):
    yaml = """\
terms:
  - term: Claim
    definition: ""
"""
    p = tmp_path / "glossary.yaml"
    p.write_text(yaml)
    with pytest.raises(RegistryError):
        GlossaryRegistry.load(p)
