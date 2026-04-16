"""CI test: every golden-path example project passes `engine validate`."""
from pathlib import Path
import subprocess
import sys
import pytest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES_DIR = ROOT / "00-meta-initialization" / "new-project" / "examples"
EXAMPLES = sorted([p for p in EXAMPLES_DIR.iterdir() if p.is_dir()]) if EXAMPLES_DIR.is_dir() else []


@pytest.mark.parametrize("example", EXAMPLES, ids=lambda p: p.name)
def test_example_passes_engine_validation(example: Path) -> None:
    rc = subprocess.call(
        [sys.executable, "-m", "engine", "validate", str(example)],
        cwd=ROOT,
    )
    assert rc == 0, f"Example {example.name} fails engine validate"
