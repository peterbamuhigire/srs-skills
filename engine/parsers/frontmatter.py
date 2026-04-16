"""YAML frontmatter parser."""
from __future__ import annotations
from typing import Tuple
from ruamel.yaml import YAML

_yaml = YAML(typ="safe")
_DELIM = "---\n"

def parse_frontmatter(body: str) -> Tuple[dict, str]:
    if not body.startswith(_DELIM):
        return {}, body
    end = body.find(f"\n{_DELIM.strip()}\n", len(_DELIM))
    if end == -1:
        return {}, body
    raw = body[len(_DELIM):end]
    rest = body[end + len(_DELIM) + 1 :]
    data = _yaml.load(raw) or {}
    if not isinstance(data, dict):
        return {}, body
    return data, rest
