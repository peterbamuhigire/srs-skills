import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate_decision_frontier.py"
SPEC = importlib.util.spec_from_file_location("decision_frontier", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def decision(decision_id, prerequisites=None, state="blocked"):
    return {
        "id": decision_id,
        "question": f"Choose {decision_id}",
        "owner": "sponsor",
        "prerequisites": prerequisites or [],
        "options": ["A", "B"],
        "evidence": [],
        "state": state,
        "downstream": ["requirement"],
    }


def test_ready_frontier_and_dependent_block():
    data = {"decisions": [
        decision("audience", state="confirmed"),
        decision("offer", ["audience"], state="frontier"),
        decision("price", ["offer"], state="blocked"),
    ]}
    findings, frontier = MODULE.validate(data)
    assert findings == []
    assert frontier == ["offer"]


def test_dependent_decision_cannot_enter_frontier_early():
    data = {"decisions": [decision("offer", state="frontier"), decision("price", ["offer"], state="frontier")]}
    findings, _ = MODULE.validate(data)
    assert any("unresolved prerequisites" in finding for finding in findings)


def test_ready_blocked_decision_is_rejected():
    findings, _ = MODULE.validate({"decisions": [decision("audience", state="blocked")]})
    assert any("should enter the frontier" in finding for finding in findings)


def test_unknown_prerequisite_fails():
    findings, _ = MODULE.validate({"decisions": [decision("price", ["missing"], state="blocked")]})
    assert any("unknown prerequisite" in finding for finding in findings)
