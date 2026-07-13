from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.removesuffix(".py"), path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_zero_debt_baseline_and_routing_fixture_contract() -> None:
    baseline = json.loads((ROOT / "tests" / "skill-quality-baseline.json").read_text(encoding="utf-8"))
    fixtures = json.loads((ROOT / "tests" / "routing-fixtures.json").read_text(encoding="utf-8"))

    assert baseline["failure_counts"] == {}
    assert baseline["active_skill_count"] == 147
    assert baseline["template_count"] == 1
    assert len(fixtures["fixtures"]) == baseline["routing"]["fixture_count"]
    assert fixtures["threshold"] == baseline["routing"]["minimum_precision"] == 1.0
    assert {item["kind"] for item in fixtures["fixtures"]} == {
        "positive",
        "collision",
        "limited-capability",
        "failure-path",
    }
    assert len({item["id"] for item in fixtures["fixtures"]}) == len(fixtures["fixtures"])


def test_validator_rejects_an_empty_nonportable_skill(tmp_path: Path) -> None:
    validator = load_script("validate_skill_engine.py")
    skill_dir = tmp_path / "bad-skill"
    skill_dir.mkdir()
    skill = skill_dir / "SKILL.md"
    skill.write_text("---\nname: wrong\ndescription: vague\n---\n\n# Bad\n", encoding="utf-8")

    findings = validator.assess(skill, tmp_path)

    assert "name_mismatch" in findings
    assert "description_contract" in findings
    assert "portable_metadata" in findings
    assert "portable_markers" in findings
    assert "input_contract" in findings
    assert "output_contract" in findings
    assert "degraded_mode" in findings


def test_routing_catalogue_is_unique_and_complete() -> None:
    routing = load_script("routing_smoke_test.py")
    catalogue = routing.read_catalogue()
    names = [item["name"] for item in catalogue]

    assert len(catalogue) == 147
    assert len(names) == len(set(names))
