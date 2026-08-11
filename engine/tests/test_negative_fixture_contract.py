from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "engine" / "tests" / "fixtures" / "tiny_project"


def test_tiny_project_is_an_explicit_negative_fixture() -> None:
    manifest = json.loads(
        (FIXTURE / "fixture-manifest.json").read_text(encoding="utf-8")
    )

    assert manifest["classification"] == "negative"
    assert manifest["data_classification"] == "synthetic-test-only"
    assert manifest["expected_high_findings"] == 28

    environment = os.environ.copy()
    environment["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(
        [sys.executable, "-m", "engine", "validate", str(FIXTURE)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=environment,
        check=False,
    )
    output = result.stdout + result.stderr

    assert result.returncode == manifest["expected_exit_code"]
    assert output.count("[HIGH]") == manifest["expected_high_findings"]
    assert output.count("[HIGH]") >= manifest["expected_minimum_high_findings"]
    for gate_id in manifest["expected_gate_ids"]:
        assert gate_id in output
