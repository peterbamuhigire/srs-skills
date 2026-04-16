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
