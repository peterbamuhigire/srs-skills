"""NFR threshold deduplication check."""
from __future__ import annotations
import re
from collections import defaultdict
from dataclasses import dataclass
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity


@dataclass(frozen=True)
class _Threshold:
    nfr_id: str
    comparator: str
    raw_value: float
    raw_unit: str
    canonical_value: float


# Ordered: longest phrases first so "concurrent users" wins before "users" alone.
_METRIC_ALIASES = [
    ("concurrent users", "concurrency"),
    ("concurrent sessions", "concurrency"),
    ("response time", "response_time"),
    ("error rate", "error_rate"),
    ("page size", "payload_size"),
    ("concurrency", "concurrency"),
    ("throughput", "throughput"),
    ("availability", "availability"),
    ("uptime", "availability"),
    ("latency", "response_time"),
    ("memory", "memory"),
    ("storage", "storage"),
    ("payload", "payload_size"),
    ("cpu", "cpu"),
]

_NFR_LINE = re.compile(r"\*\*(NFR-\d{3,5})\*\*\s+(.*)")
_COMPARATOR = r"(?:≤|<=|≥|>=|<|>|=)"
_NUMBER = r"\d+(?:\.\d+)?"
_UNIT = (
    r"ms|seconds?|secs?|s\b|minutes?|mins?|hours?"
    r"|bytes?|KB|MB|GB|TB"
    r"|%"
    r"|req/s|RPS|qps"
    r"|users|sessions|connections"
)
_THRESHOLD = re.compile(
    rf"({_COMPARATOR})\s*({_NUMBER})\s*(?P<unit>(?:{_UNIT}))",
    re.IGNORECASE,
)

_TIME_TO_MS = {
    "ms": 1.0,
    "s": 1000.0, "sec": 1000.0, "secs": 1000.0,
    "second": 1000.0, "seconds": 1000.0,
    "min": 60_000.0, "mins": 60_000.0,
    "minute": 60_000.0, "minutes": 60_000.0,
    "hour": 3_600_000.0, "hours": 3_600_000.0,
}
_SIZE_TO_MB = {
    "byte": 1.0 / (1024 * 1024), "bytes": 1.0 / (1024 * 1024),
    "kb": 1.0 / 1024, "mb": 1.0,
    "gb": 1024.0, "tb": 1024.0 * 1024.0,
}
_PAYLOAD_TO_KB = {
    "byte": 1.0 / 1024, "bytes": 1.0 / 1024,
    "kb": 1.0, "mb": 1024.0,
    "gb": 1024.0 * 1024.0,
}


def _canonicalize(metric: str, value: float, unit: str) -> float:
    u = unit.lower()
    if metric == "response_time":
        return value * _TIME_TO_MS.get(u, 1.0)
    if metric in ("memory", "storage"):
        return value * _SIZE_TO_MB.get(u, 1.0)
    if metric == "payload_size":
        return value * _PAYLOAD_TO_KB.get(u, 1.0)
    # Percentages, counts, throughput use the value directly.
    return value


class NfrThresholdDedupCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        thresholds: dict[str, list[_Threshold]] = defaultdict(list)
        # raw_by_key maps metric -> list of (nfr_id, raw_threshold_string).
        raw_by_key: dict[str, list[tuple[str, str]]] = defaultdict(list)
        for art in graph.artifacts:
            for line in art.body.splitlines():
                m = _NFR_LINE.search(line)
                if not m:
                    continue
                nfr_id, text = m.group(1), m.group(2)
                text_lower = text.lower()
                metric_token = None
                for phrase, canonical in _METRIC_ALIASES:
                    if phrase in text_lower:
                        metric_token = canonical
                        break
                if metric_token is None:
                    continue
                t_match = _THRESHOLD.search(text)
                if not t_match:
                    continue
                comparator = t_match.group(1)
                value = float(t_match.group(2))
                unit = t_match.group("unit")
                canonical_value = _canonicalize(metric_token, value, unit)
                thresholds[metric_token].append(_Threshold(
                    nfr_id=nfr_id,
                    comparator=comparator,
                    raw_value=value,
                    raw_unit=unit,
                    canonical_value=canonical_value,
                ))
                raw_by_key[metric_token].append(
                    (nfr_id, f"{comparator} {value:g} {unit}")
                )

        for metric_token, items in thresholds.items():
            if len(items) < 2:
                continue
            # A "contradiction" exists if the set of
            # (comparator, canonical_value) pairs has more than one distinct
            # element.
            distinct = {(t.comparator, t.canonical_value) for t in items}
            if len(distinct) < 2:
                continue
            summary = ", ".join(
                f"{nid} ({raw})"
                for nid, raw in sorted(raw_by_key[metric_token])
            )
            findings.add(Finding(
                gate_id=f"{self.gate_id}.contradiction",
                severity=Severity.HIGH,
                message=(
                    f"NFR threshold contradiction on '{metric_token}': "
                    f"{summary}"
                ),
                location=None,
                line=None,
            ))
