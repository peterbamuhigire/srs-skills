"""Audit the SRS, verify IEEE 830 qualities, and create a traceability matrix."""

from pathlib import Path
import re
import sys

MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
PROJECT_CONTEXT = PARENT_ROOT / "project_context"
OUTPUT_DIR = PARENT_ROOT / "output"
SRS_FILE = OUTPUT_DIR / "SRS_Draft.md"
AUDIT_REPORT = PARENT_ROOT / "Audit_Report.md"


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required file missing: {path.relative_to(PARENT_ROOT)}")
    print(f"Reading {path.relative_to(PARENT_ROOT)}")
    return path.read_text(encoding="utf-8")


def list_project_context() -> dict[str, str]:
    contents: dict[str, str] = {}
    for path in sorted(PROJECT_CONTEXT.glob("*")):
        if path.is_file():
            contents[path.name] = read_file(path)
    return contents


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    lines = [line for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return rows
    headers = [cell.strip() for cell in lines[0].strip("|").split("|")]
    for line in lines[2:]:
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))
        rows.append({headers[i]: cells[i] for i in range(len(headers))})
    return rows


def extract_goals(text: str) -> list[str]:
    goals = []
    for line in text.splitlines():
        candidate = line.strip().lstrip("- ").strip()
        if not candidate:
            continue
        lowered = candidate.lower()
        if "goal" in lowered or "need" in lowered or "objective" in lowered:
            goals.append(candidate)
    return goals or ["Vision and stakeholder goals" ]


def assign_feature(requirement: str, features: list[dict[str, str]]) -> str:
    requirement_lower = requirement.lower()
    for feature in features:
        name = feature.get("Feature Name", "").strip()
        if not name:
            continue
        if " " not in name:
            keyword = name.lower()
        else:
            keyword = name.lower()
        if keyword in requirement_lower:
            return name
    return "General"


def quality_tag(requirement: str) -> str:
    mapping = {
        "Performance Efficiency": ["performance", "response", "latency", "throughput", "load", "ms", "seconds"],
        "Reliability": ["reliability", "fail", "fault", "recover", "uptime", "availability"],
        "Availability": ["availability", "downtime", "failover"],
        "Security": ["security", "encrypt", "rbac", "access control", "audit", "auth"],
        "Maintainability": ["maintain", "documentation", "modular", "traceability", "refactor", "analysis"],
    }
    text = requirement.lower()
    for tag, keywords in mapping.items():
        if any(keyword in text for keyword in keywords):
            return tag
    return "Functional Suitability"


def verification_method(requirement: str) -> str:
    requirement_lower = requirement.lower()
    if "test" in requirement_lower or "latency" in requirement_lower or "verify" in requirement_lower:
        return "Test"
    if "inspect" in requirement_lower or "log" in requirement_lower or "audit" in requirement_lower:
        return "Inspection"
    return "Demonstration"


def detect_weak_words(text: str) -> list[str]:
    weak_words = ["should", "might", "could", "may", "possibly", "preferably", "ideally", "somewhat", "user-friendly", "highly", "intelligent", "optimized"]
    return [word for word in weak_words if word in text.lower()]


def has_measurement(text: str) -> bool:
    if re.search(r"\d+(?:\.\d+)?\s*(ms|s|seconds?|minutes?|%)", text, flags=re.I):
        return True
    if re.search(r"(round|precision|two decimal)", text, flags=re.I):
        return True
    return False


def parse_requirements(srs_text: str) -> list[dict[str, str | bool]]:
    requirements = []
    current_section = "Unknown Section"
    for line in srs_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            current_section = stripped
        if "the system shall" not in stripped.lower():
            continue
        requirement_text = stripped.lstrip("- ").strip()
        if not requirement_text.endswith("."):
            requirement_text += "."
        req_id = f"R-REQ-{len(requirements) + 1:03d}"
        weak_hits = detect_weak_words(requirement_text)
        measurement_flag = has_measurement(requirement_text)
        requirements.append({
            "id": req_id,
            "text": requirement_text,
            "section": current_section,
            "weak_words": weak_hits,
            "measurement": measurement_flag,
        })
    return requirements


def build_rtm(requirements: list[dict[str, str | bool]], features: list[dict[str, str]], goals: list[str]) -> tuple[list[str], list[str]]:
    feature_lookup = {feature.get("Feature Name", "").strip(): feature for feature in features if feature.get("Feature Name")}
    used_features = set()
    rtm_lines = ["| Req ID | Feature Name | Source/Vision Goal | ISO 25010 Quality Tag | Verification Method |",
                 "|--------|--------------|-------------------|----------------------|----------------------|"]
    for req in requirements:
        feature_name = assign_feature(req["text"], features)
        if feature_name != "General":
            used_features.add(feature_name)
        source = feature_lookup.get(feature_name, {}).get("User Story") if feature_name in feature_lookup else None
        if not source:
            source = goals[0]
        tag = quality_tag(req["text"])
        verification = verification_method(req["text"])
        rtm_lines.append(
            f"| {req['id']} | {feature_name} | {source} | {tag} | {verification} |"
        )
        req["feature"] = feature_name
        req["quality_tag"] = tag
        req["verification"] = verification
        req["source"] = source
    return rtm_lines, sorted(used_features)


def gap_analysis(requirements: list[dict[str, str | bool]], features: list[dict[str, str]]) -> tuple[list[str], list[str]]:
    feature_names = [feature.get("Feature Name", "General") for feature in features if feature.get("Feature Name")]
    used = {req.get("feature") for req in requirements if req.get("feature") and req.get("feature") != "General"}
    orphans = [req for req in requirements if req.get("feature") == "General"]
    unmet = [feature for feature in feature_names if feature not in used]
    return [f"- {req['id']}: {req['text']}" for req in orphans], [f"- {goal}" for goal in unmet]


def requirements_audit(requirements: list[dict[str, str | bool]], orphan_count: int, unmet_goal_count: int) -> list[str]:
    weak_words_total = sum(1 for req in requirements if req["weak_words"])
    missing_measurements = sum(1 for req in requirements if not req["measurement"])
    duplicate_texts = len(requirements) != len({req["text"] for req in requirements})
    design_terms = ["module", "class", "interface", "implementation", "UI"]
    design_mention = any(any(term in req["text"].lower() for term in design_terms) for req in requirements)
    lines = ["## Requirements Audit (IEEE 830)"]
    lines.append(f"- Correctness: {'PASS' if requirements else 'FAIL'} – {len(requirements)} requirements detected.")
    lines.append(f"- Unambiguous: {'FAIL' if weak_words_total else 'PASS'} – {weak_words_total} requirement(s) contain weak wording.")
    lines.append(f"- Completeness: {'PASS' if unmet_goal_count == 0 else 'FAIL'} – {unmet_goal_count} goal(s) lack mappings.")
    lines.append(f"- Consistency: {'FAIL' if duplicate_texts else 'PASS'} – duplicate statements {'found' if duplicate_texts else 'not found'}." )
    lines.append(f"- Verifiability: {'FAIL' if missing_measurements else 'PASS'} – {missing_measurements} requirement(s) miss measurable targets.")
    lines.append(f"- Modifiability: {'FAIL' if design_mention else 'PASS'} – design terms {'present' if design_mention else 'absent'} in requirements.")
    lines.append(f"- Traceability: {'FAIL' if orphan_count else 'PASS'} – {orphan_count} orphan requirement(s)." )
    lines.append(f"- Design Independence: {'FAIL' if design_mention else 'PASS'} – requirements should avoid design decisions.")
    return lines


def build_ambiguity_report(requirements: list[dict[str, str | bool]]) -> list[str]:
    lines = ["## Ambiguity & Weak Word Report"]
    flagged = []
    for req in requirements:
        reasons = []
        if req["weak_words"]:
            reasons.append(f"weak wording ({', '.join(req['weak_words'])})")
        if not req["measurement"]:
            reasons.append("missing measurable target")
        if reasons:
            flagged.append(f"- {req['id']} FAIL – {req['text']} ({'; '.join(reasons)}).")
    if not flagged:
        lines.append("- No ambiguity detected; all requirements use precise language.")
    else:
        lines.extend(flagged)
    return lines


def build_gap_section(orphans: list[str], unmet: list[str]) -> list[str]:
    lines = ["## Gap Analysis", "### Orphan Requirements"]
    lines.extend(orphans or ["- None."])
    lines.append("### Unmet Goals")
    lines.extend(unmet or ["- None."])
    return lines


def standard_conformance_statement() -> list[str]:
    return [
        "## Standard Conformance Statement",
        "- This audit verifies the SRS against IEEE 830 and US ISO/IEC 25010 by enforcing clear requirements, traceability links, and measurability.",
        "- Requirements are cross-referenced to vision goals, features, and quality characteristics; verification methods and standard references are documented herein.",
    ]


def compose_report(requirements: list[dict[str, str | bool]], rtm_lines: list[str], ambiguity_lines: list[str], gap_lines: list[str], audit_lines: list[str]) -> str:
    sections = [
        "# Semantic Auditing Report",
        *audit_lines,
        "## Requirement Traceability Matrix",
        *rtm_lines,
        *ambiguity_lines,
        *gap_lines,
        *standard_conformance_statement(),
    ]
    return "\n".join(sections)


def main() -> None:
    try:
        ensure_output_dir()
        context_texts = list_project_context()
        srs_text = read_file(SRS_FILE)
    except FileNotFoundError as exc:
        print(exc)
        sys.exit(1)

    features = parse_markdown_table(context_texts.get("features.md", ""))
    quality_rows = parse_markdown_table(context_texts.get("quality_standards.md", ""))
    vision_text = context_texts.get("vision.md", "")
    goals = extract_goals(vision_text)

    requirements = parse_requirements(srs_text)
    if not requirements:
        print("No requirements found; audit cannot proceed.")
        sys.exit(1)

    rtm_lines, used_features = build_rtm(requirements, features, goals)
    orphans, unmet = gap_analysis(requirements, features)
    audit_lines = requirements_audit(requirements, len(orphans), len(unmet))
    ambiguity_lines = build_ambiguity_report(requirements)
    gap_lines = build_gap_section(orphans, unmet)
    report_body = compose_report(requirements, rtm_lines, ambiguity_lines, gap_lines, audit_lines)

    AUDIT_REPORT.write_text(report_body + "\n", encoding="utf-8")
    print(f"Wrote audit report to {AUDIT_REPORT.relative_to(PARENT_ROOT)}")


if __name__ == "__main__":
    main()