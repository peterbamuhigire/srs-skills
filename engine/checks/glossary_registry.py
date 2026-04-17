"""Glossary registry check.

A domain-specific glossary candidate is a token that looks like jargon — not
every capitalised English word. We recognise two signals:

1. ALL-CAPS acronyms of 2 or more characters (NIN, UNEB, DPPA, API).
2. CamelCase compounds with internal uppercase (TenantScope, SchoolPay,
   MoMo, iOS, PIIScrubber).

Regular capitalised English words ("Action", "Access", "Claim") are not
candidates. If the team wants a non-acronym term to be glossary-required,
they define it in the canonical glossary — the check only raises findings
about *missing* definitions for tokens that carry a jargon signal.
"""
from __future__ import annotations
import re
from collections import defaultdict
from pathlib import Path
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.registry.glossary import GlossaryRegistry

# Signal 1: 2+ char ALL-CAPS acronym. Optional embedded digits allowed.
_ACRONYM = re.compile(r"\b([A-Z]{2,}[0-9]*[A-Z]*)\b")
# Signal 2: CamelCase compound — starts with capital, has at least one
# internal uppercase letter, optionally prefixed by a lowercase cluster
# (matches iOS, macOS too). Length >= 3 so it does not match generic
# sentence-start tokens like "It".
_CAMEL_CASE = re.compile(r"\b([a-z]*[A-Z][a-z]+[A-Z][A-Za-z0-9]*)\b")

_GLOSSARY_DEF_LINE = re.compile(r"^\s*-\s+\*\*[A-Z][A-Za-z0-9_-]+:\*\*")

# Strip identifier patterns (FR-NNN, FR-ACA-001, CTRL-UG-005, ADR-0001, etc.)
# before acronym scanning so the scanner does not flag identifier prefixes
# or module codes as standalone acronyms.
_IDENTIFIER = re.compile(r"\b[A-Z]{2,10}(?:-[A-Z0-9]{1,10}){1,3}\b")

# Markdown-skeleton acronyms and programming-language tokens that are too
# universal to be useful as project glossary entries, plus English words
# that appear fully uppercase for emphasis.
_ACRONYM_STOPLIST = frozenset({
    # universal technical
    "HTTP", "HTTPS", "URL", "URI", "HTML", "CSS", "JSON", "YAML", "XML",
    "PDF", "PNG", "JPG", "JPEG", "GIF", "SVG", "CSV", "TSV", "UTF",
    "ID", "IDS", "OK", "NA", "TBD", "TODO", "FIXME",
    "CRUD", "REST", "SOAP", "RPC", "SDK", "CLI", "GUI", "UI", "UX",
    "VM", "OS", "IO", "DB", "RAM", "CPU", "GPU",
    # English emphasis caps
    "AND", "OR", "NOT", "IF", "WHEN", "WHERE", "WHILE", "THEN", "ELSE",
    "BEFORE", "AFTER", "DURING", "ABOVE", "BELOW", "FROM", "TO", "WITH",
    "MUST", "SHALL", "SHOULD", "MAY", "WILL", "CAN",
    "ALL", "ANY", "NONE", "EACH", "EVERY", "ONE", "TWO", "BY",
    "YES", "NO", "TRUE", "FALSE",
    "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", "MAJOR", "DENIED",
    "DUPLICATE", "INVALID", "VALID", "REQUIRED", "OPTIONAL",
    # SQL keywords and DB terms
    "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER",
    "TRUNCATE", "WHERE", "ORDER", "GROUP", "LIMIT", "OFFSET",
    "JOIN", "LEFT", "RIGHT", "INNER", "OUTER", "OUTER", "FULL", "ON",
    "VARCHAR", "TEXT", "DATE", "TIMESTAMP", "DATETIME", "BOOLEAN", "INT",
    "BIGINT", "DECIMAL", "FLOAT", "DOUBLE", "ENUM", "BLOB", "NULL",
    "PRIMARY", "FOREIGN", "KEY", "INDEX", "UNIQUE", "CONSTRAINT",
    "DEFAULT", "AUTO", "CASCADE", "CHARACTER", "COLLATE", "REFERENCES",
    # CI/CD, DevOps idiom fragments
    "CI", "CD", "CS", "CT", "CSRF", "CORS", "TLS", "SSL", "SSH", "FTP",
    "SFTP", "SMTP", "IMAP", "POP",
    # Size/unit acronyms that are never domain terms worth glossing
    "AA", "BB", "CC", "DD", "EE", "GB", "KB", "MB", "TB", "PB",
    "GHZ", "MHZ", "HZ", "MS", "NS", "KG", "CM", "MM",
    # Roman numerals
    "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII",
    # HTTP verbs as acronyms
    "GET", "POST", "PUT", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE",
    # Common 2-3 char false positives (generic abbreviations)
    "BG", "BU", "HT", "HC", "HR", "IM", "IT", "PM", "QA", "OK",
    "IGNORE", "FAIL", "FAILED", "PASS", "PASSED", "WARN", "INFO",
    "ENGINE", "CHANGELOG", "UNAUTHENTICATED", "AUTHENTICATED",
    # More SQL / DB / shell keywords
    "LIKE", "SHOW", "SIGNAL", "STATUS", "RESTRICT", "PONG", "PING",
    "VARIABLES", "SQLSTATE",
    # Two-letter / three-letter state codes and generic noise
    "PA", "SA", "RC", "ST", "OW", "NYC", "UG", "US", "UK", "EU",
    # Additional SQL/shell/programming keywords discovered on real-project scan
    "SET", "TABLE", "VALUES", "INTO", "USING", "VIEW", "LOCK",
    # Sample IDs and file extensions that are not glossary candidates
    "MP4", "MP3", "WAV", "AAC", "WEBM", "TC",
    # Hash/crypto algorithm tokens that appear incidentally in prose
    "SHA", "SHA1", "SHA256", "SHA512", "AES", "RSA",
})

# Sample / placeholder identifiers from code blocks that leak into prose.
# Any token matching these regexes is treated as a sample ID, not a glossary
# candidate.
_SAMPLE_ID_PATTERNS = (
    re.compile(r"^[A-Z]{2}\d{3,}$"),   # ST1234567, RM1 (short), AB12345
    re.compile(r"^[A-Z]{2,3}\d+$"),    # RM1
)


def _is_sample_id(token: str) -> bool:
    return any(p.match(token) for p in _SAMPLE_ID_PATTERNS)


class GlossaryRegistryCheck:
    def __init__(self, gate_id: str, registry_path: Path) -> None:
        self.gate_id = gate_id
        self._registry = GlossaryRegistry.load(registry_path)

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        glossary_terms = {e.term for e in self._registry}
        glossary_lower = {t.lower() for t in glossary_terms}

        usage: dict[str, set[str]] = defaultdict(set)
        for art in graph.artifacts:
            path_key = str(art.path)
            for line in art.body.splitlines():
                if _GLOSSARY_DEF_LINE.search(line):
                    continue
                stripped = _IDENTIFIER.sub(" ", line)
                for m in _ACRONYM.finditer(stripped):
                    tok = m.group(1)
                    if tok in _ACRONYM_STOPLIST or _is_sample_id(tok):
                        continue
                    usage[tok].add(path_key)
                for m in _CAMEL_CASE.finditer(stripped):
                    usage[m.group(1)].add(path_key)

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
