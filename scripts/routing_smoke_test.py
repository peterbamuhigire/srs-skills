#!/usr/bin/env python3
"""Rank active skills against representative prompts and enforce top-three routing."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from ruamel.yaml import YAML


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "routing-fixtures.json"
STOP = {
    "a", "an", "and", "are", "as", "at", "be", "before", "by", "do", "for", "from",
    "in", "into", "is", "it", "of", "on", "or", "the", "this", "to", "with", "write",
    "create", "generate", "prepare", "produce", "document", "skill",
}
SYNONYMS = {
    "prioritize": "prioritization", "prioritise": "prioritization", "audit": "auditing",
    "review": "validation", "validate": "validation", "install": "installation",
    "deploy": "deployment", "monitor": "monitoring", "stories": "story",
    "requirements": "requirement", "risks": "risk", "tests": "test",
}


def tokens(text: str) -> set[str]:
    found = set(re.findall(r"[a-z0-9]+", text.lower()))
    normal = {SYNONYMS.get(word, word) for word in found if word not in STOP and len(word) > 1}
    return normal


def read_catalogue() -> list[dict[str, str]]:
    yaml = YAML(typ="safe")
    catalogue: list[dict[str, str]] = []
    for root in sorted(path for path in ROOT.iterdir() if path.is_dir() and re.match(r"^0[1-9]-", path.name)):
        for skill in sorted(root.rglob("SKILL.md")):
            raw = skill.read_text(encoding="utf-8")
            match = re.match(r"^---\n(.*?)\n---", raw, re.S)
            if not match:
                continue
            try:
                fm = yaml.load(match.group(1)) or {}
            except Exception:
                continue
            name = fm.get("name")
            description = fm.get("description")
            if isinstance(name, str) and isinstance(description, str):
                catalogue.append({"name": name, "description": description, "path": skill.parent.relative_to(ROOT).as_posix()})
    return catalogue


def rank(prompt: str, catalogue: list[dict[str, str]]) -> list[tuple[float, str]]:
    prompt_tokens = tokens(prompt)
    ranked: list[tuple[float, str]] = []
    lower = prompt.lower()
    for item in catalogue:
        name_words = tokens(item["name"].replace("-", " "))
        description_words = tokens(item["description"])
        overlap_name = len(prompt_tokens & name_words)
        overlap_description = len(prompt_tokens & description_words)
        phrase = item["name"].replace("-", " ")
        score = overlap_name * 5 + overlap_description * 2 + (8 if phrase in lower else 0)
        specificity = len(name_words) / 1000
        ranked.append((score + specificity, item["name"]))
    return sorted(ranked, key=lambda pair: (-pair[0], pair[1]))


def main() -> int:
    data = json.loads(FIXTURES.read_text(encoding="utf-8"))
    catalogue = read_catalogue()
    top_k = int(data.get("top_k", 3))
    failures: list[tuple[str, str, list[str]]] = []
    for fixture in data["fixtures"]:
        top = [name for _, name in rank(fixture["prompt"], catalogue)[:top_k]]
        if fixture["expected"] not in top:
            failures.append((fixture["id"], fixture["expected"], top))
    total = len(data["fixtures"])
    passed = total - len(failures)
    precision = passed / total if total else 0.0
    threshold = float(data["threshold"])
    print(f"routing-smoke: {passed}/{total} fixtures; top-{top_k} precision={precision:.3f}; threshold={threshold:.3f}")
    for fixture_id, expected, top in failures:
        print(f"- {fixture_id}: expected {expected}; got {', '.join(top)}")
    return 1 if failures or precision < threshold else 0


if __name__ == "__main__":
    sys.exit(main())
