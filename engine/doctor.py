"""engine doctor: pre-flight diagnostics."""
from __future__ import annotations
import shutil
import subprocess
import sys
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class Check:
    name: str
    fn: Callable[[], "tuple[bool, str]"]
    fix_hint: str


def _check_python() -> "tuple[bool, str]":
    ok = sys.version_info >= (3, 11)
    return ok, f"Python {sys.version.split()[0]}"


def _check_pandoc() -> "tuple[bool, str]":
    p = shutil.which("pandoc")
    if not p:
        return False, "pandoc not on PATH"
    try:
        out = subprocess.check_output([p, "--version"], text=True).splitlines()[0]
    except Exception as exc:  # pragma: no cover
        return False, f"pandoc invocation failed: {exc}"
    return True, out


def _check_engine_imports() -> "tuple[bool, str]":
    try:
        import engine.cli as _  # noqa: F401
        return True, "engine package importable"
    except Exception as exc:  # pragma: no cover
        return False, f"engine import failed: {exc}"


def _check_submodule() -> "tuple[bool, str]":
    from pathlib import Path
    skills = Path("skills")
    if not skills.is_dir():
        return False, "skills/ submodule directory not present"
    if not any(skills.iterdir()):
        return False, "skills/ submodule is empty (run `git submodule update --init`)"
    return True, "skills submodule populated"


CHECKS: List[Check] = [
    Check("Python >= 3.11", _check_python, "Install Python 3.11 or newer."),
    Check("Pandoc available", _check_pandoc, "Install Pandoc: https://pandoc.org/installing.html"),
    Check("Engine package", _check_engine_imports, "Run `pip install -e .[dev]` from repo root."),
    Check("Skills submodule", _check_submodule, "Run `git submodule update --init --recursive`."),
]


def run() -> int:
    failed = 0
    for chk in CHECKS:
        ok, detail = chk.fn()
        status = "OK  " if ok else "FAIL"
        print(f"[{status}] {chk.name}: {detail}")
        if not ok:
            print(f"       fix: {chk.fix_hint}")
            failed += 1
    if failed:
        print(f"\n{failed} check(s) failed.")
        return 1
    print("\nAll checks passed.")
    return 0
