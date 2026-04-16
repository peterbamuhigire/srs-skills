"""Glossary registry check."""
from __future__ import annotations
import re
from collections import defaultdict
from pathlib import Path
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.registry.glossary import GlossaryRegistry

_TERM_CANDIDATE = re.compile(r"\b([A-Z][a-z]{3,})\b")
_GLOSSARY_DEF_LINE = re.compile(r"^\s*-\s+\*\*[A-Z][A-Za-z0-9_-]+:\*\*")


class GlossaryRegistryCheck:
    def __init__(self, gate_id: str, registry_path: Path) -> None:
        self.gate_id = gate_id
        self._registry = GlossaryRegistry.load(registry_path)

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        glossary_terms = {e.term for e in self._registry}
        glossary_lower = {t.lower() for t in glossary_terms}

        # Collect term -> set of artifact paths in which it appears.
        usage: dict[str, set[str]] = defaultdict(set)
        for art in graph.artifacts:
            path_key = str(art.path)
            for line in art.body.splitlines():
                # Skip the glossary definition line itself so a term does
                # not self-match in its own definition file.
                if _GLOSSARY_DEF_LINE.search(line):
                    continue
                for m in _TERM_CANDIDATE.finditer(line):
                    usage[m.group(1)].add(path_key)

        # A "used" domain-specific term appears in at least 2 distinct files.
        used_terms = {t for t, files in usage.items() if len(files) >= 2}

        for term in sorted(used_terms):
            if term.lower() not in glossary_lower:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.missing_term",
                    severity=Severity.HIGH,
                    message=(
                        f"Term '{term}' used in artifacts but missing "
                        f"from _registry/glossary.yaml"
                    ),
                    location=None, line=None,
                ))

        # Orphan detection: glossary term never appears in any artifact body.
        body_all = "\n".join(a.body for a in graph.artifacts)
        for term in sorted(glossary_terms):
            if not re.search(rf"\b{re.escape(term)}\b", body_all):
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.orphan_term",
                    severity=Severity.MEDIUM,
                    message=(
                        f"Glossary term '{term}' is orphan \u2014 not "
                        f"referenced in any artifact"
                    ),
                    location=None, line=None,
                ))
