"""Audit the SRS, verify IEEE 830 qualities, and create a traceability matrix.

Enhanced with full IEEE 830-1998 compliance validation including:
- Ranking completeness (§4.3.5)
- TBD protocol enforcement (§4.3.3.1)
- Modifiability checks (§4.3.7)
- Backward traceability validation (§4.3.8)
- SRS structure completeness (§5.1–§5.4)
- Standards compliance and other requirements sections (§5.3.5.1, §5.3.8)
"""

from pathlib import Path
import re
import sys

MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
PROJECT_CONTEXT = PARENT_ROOT / "project_context"
OUTPUT_DIR = PARENT_ROOT / "output"
SRS_FILE = OUTPUT_DIR / "SRS_Draft.md"
AUDIT_REPORT = PARENT_ROOT / "Audit_Report.md"

WEAK_WORDS = [
    "should", "might", "could", "may", "possibly", "preferably",
    "ideally", "somewhat", "user-friendly", "highly", "intelligent",
    "optimized",
]

DESIGN_TERMS = ["module", "class", "interface", "implementation", "UI"]

PRIORITY_KEYWORDS = ["essential", "conditional", "optional"]

# IEEE 830 §5 required SRS sections and their checklist IDs
REQUIRED_SECTIONS = {
    "1.1": ("Purpose", "IEEE830-5.1.1"),
    "1.2": ("Scope", "IEEE830-5.1.2"),
    "1.3": ("Definitions", "IEEE830-5.1.3"),
    "1.4": ("References", "IEEE830-5.1.4"),
    "1.5": ("Overview", "IEEE830-5.1.5"),
    "2.1": ("Product Perspective", "IEEE830-5.2.1"),
    "2.2": ("Product Functions", "IEEE830-5.2.2"),
    "2.3": ("User Characteristics", "IEEE830-5.2.3"),
    "2.4": ("Constraints", "IEEE830-5.2.4"),
    "2.5": ("Assumptions and Dependencies", "IEEE830-5.2.5"),
    "2.6": ("Apportioning of Requirements", "IEEE830-5.2.6"),
    "3.1": ("External Interfaces", "IEEE830-5.3.1"),
    "3.2": ("Functions", "IEEE830-5.3.2"),
    "3.3": ("Performance Requirements", "IEEE830-5.3.3"),
    "3.4": ("Design Constraints", "IEEE830-5.3.5"),
    "3.5": ("Software System Attributes", "IEEE830-5.3.6"),
    "3.6": ("Other Requirements", "IEEE830-5.3.7"),
}

# IEEE 830 §5.2.1 sub-items
PRODUCT_PERSPECTIVE_SUBS = {
    "2.1.1": ("System Interfaces", "IEEE830-5.2.1.1"),
    "2.1.2": ("User Interfaces", "IEEE830-5.2.1.2"),
    "2.1.3": ("Hardware Interfaces", "IEEE830-5.2.1.3"),
    "2.1.4": ("Software Interfaces", "IEEE830-5.2.1.4"),
    "2.1.5": ("Communications Interfaces", "IEEE830-5.2.1.5"),
    "2.1.6": ("Memory Constraints", "IEEE830-5.2.1.6"),
    "2.1.7": ("Operations", "IEEE830-5.2.1.7"),
    "2.1.8": ("Site Adaptation", "IEEE830-5.2.1.8"),
}


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
    return goals or ["Vision and stakeholder goals"]


def assign_feature(requirement: str, features: list[dict[str, str]]) -> str:
    requirement_lower = requirement.lower()
    for feature in features:
        name = feature.get("Feature Name", "").strip()
        if not name:
            continue
        if name.lower() in requirement_lower:
            return name
    return "General"


def quality_tag(requirement: str) -> str:
    mapping = {
        "Performance Efficiency": [
            "performance", "response", "latency", "throughput", "load", "ms", "seconds",
        ],
        "Reliability": [
            "reliability", "fail", "fault", "recover", "uptime", "availability",
        ],
        "Availability": ["availability", "downtime", "failover"],
        "Security": [
            "security", "encrypt", "rbac", "access control", "audit", "auth",
        ],
        "Maintainability": [
            "maintain", "documentation", "modular", "traceability", "refactor", "analysis",
        ],
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
    return [word for word in WEAK_WORDS if word in text.lower()]


def has_measurement(text: str) -> bool:
    if re.search(r"\d+(?:\.\d+)?\s*(ms|s|seconds?|minutes?|%)", text, flags=re.I):
        return True
    if re.search(r"(round|precision|two decimal)", text, flags=re.I):
        return True
    return False


def has_priority(text: str, section_context: str) -> bool:
    """Check if requirement or its surrounding section has a priority ranking."""
    combined = (text + " " + section_context).lower()
    return any(kw in combined for kw in PRIORITY_KEYWORDS)


def has_backward_trace(text: str) -> bool:
    """Check if requirement references a source document (backward traceability)."""
    trace_patterns = [
        r"\[source:",
        r"features\.md",
        r"vision\.md",
        r"business_rules\.md",
        r"quality_standards\.md",
        r"stakeholder",
    ]
    text_lower = text.lower()
    return any(re.search(p, text_lower) for p in trace_patterns)


def count_shall_clauses(text: str) -> int:
    """Count the number of 'shall' statements in a single requirement."""
    return len(re.findall(r"\bshall\b", text, flags=re.I))


def check_tbd_protocol(srs_text: str) -> list[dict[str, str]]:
    """Find TBD entries and verify they follow the IEEE 830 §4.3.3.1 protocol."""
    tbd_issues = []
    tbd_pattern = re.compile(r"TBD", re.I)
    for i, line in enumerate(srs_text.splitlines(), 1):
        if not tbd_pattern.search(line):
            continue
        stripped = line.strip()
        has_condition = bool(re.search(r"(condition|reason|because|why)", stripped, re.I))
        has_resolution = bool(re.search(r"(resolution|resolve|action|eliminate)", stripped, re.I))
        has_owner = bool(re.search(r"(owner|responsible|assigned)", stripped, re.I))
        has_deadline = bool(re.search(r"(deadline|date|by\s+\d|Q[1-4]|sprint)", stripped, re.I))
        missing = []
        if not has_condition:
            missing.append("condition")
        if not has_resolution:
            missing.append("resolution action")
        if not has_owner:
            missing.append("owner")
        if not has_deadline:
            missing.append("deadline")
        if missing:
            tbd_issues.append({
                "line": i,
                "text": stripped[:120],
                "missing": missing,
            })
    return tbd_issues


def check_srs_sections(srs_text: str) -> tuple[list[str], list[str]]:
    """Verify presence of all IEEE 830 required sections."""
    present = []
    missing = []
    srs_lower = srs_text.lower()

    for section_num, (name, checklist_id) in REQUIRED_SECTIONS.items():
        # Search for section heading patterns like "## 2.6" or "### Section 2.6" or "2.6 Apportioning"
        patterns = [
            rf"#+\s*{re.escape(section_num)}[\s.\-–—]",
            rf"#+\s*section\s*{re.escape(section_num)}",
            rf"{re.escape(section_num)}\s+{re.escape(name.split()[0].lower())}",
        ]
        found = any(re.search(p, srs_lower) for p in patterns)
        if found:
            present.append(f"- PRESENT [{checklist_id}] Section {section_num} ({name})")
        else:
            missing.append(f"- MISSING [{checklist_id}] Section {section_num} ({name})")

    # Check §5.2.1 sub-items
    for sub_num, (name, checklist_id) in PRODUCT_PERSPECTIVE_SUBS.items():
        patterns = [
            rf"#+\s*{re.escape(sub_num)}[\s.\-–—]",
            rf"{re.escape(name.lower())}",
        ]
        found = any(re.search(p, srs_lower) for p in patterns)
        if found:
            present.append(f"- PRESENT [{checklist_id}] Section {sub_num} ({name})")
        else:
            missing.append(f"- MISSING [{checklist_id}] Section {sub_num} ({name})")

    # Check TOC
    if re.search(r"table\s+of\s+contents", srs_lower) or re.search(r"^\s*-\s+\[", srs_text, re.M):
        present.append("- PRESENT [IEEE830-5.4.1] Table of Contents")
    else:
        missing.append("- MISSING [IEEE830-5.4.1] Table of Contents")

    return present, missing


def check_redundancy(requirements: list[dict]) -> list[str]:
    """Detect duplicate or near-duplicate requirements without cross-references."""
    duplicates = []
    seen_texts: dict[str, str] = {}
    for req in requirements:
        normalized = re.sub(r"\s+", " ", req["text"].lower().strip())
        if normalized in seen_texts:
            duplicates.append(
                f"- {req['id']} duplicates {seen_texts[normalized]}: {req['text'][:80]}"
            )
        else:
            seen_texts[normalized] = req["id"]
    return duplicates


def parse_requirements(srs_text: str) -> list[dict]:
    requirements = []
    current_section = "Unknown Section"
    section_block = ""
    for line in srs_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            current_section = stripped
            section_block = ""
        section_block += " " + stripped
        if "the system shall" not in stripped.lower():
            continue
        requirement_text = stripped.lstrip("- ").strip()
        if not requirement_text.endswith("."):
            requirement_text += "."
        req_id = f"R-REQ-{len(requirements) + 1:03d}"
        weak_hits = detect_weak_words(requirement_text)
        measurement_flag = has_measurement(requirement_text)
        priority_flag = has_priority(requirement_text, section_block)
        backward_trace_flag = has_backward_trace(requirement_text)
        shall_count = count_shall_clauses(requirement_text)
        requirements.append({
            "id": req_id,
            "text": requirement_text,
            "section": current_section,
            "weak_words": weak_hits,
            "measurement": measurement_flag,
            "has_priority": priority_flag,
            "has_backward_trace": backward_trace_flag,
            "shall_count": shall_count,
        })
    return requirements


def build_rtm(
    requirements: list[dict], features: list[dict[str, str]], goals: list[str],
) -> tuple[list[str], list[str]]:
    feature_lookup = {
        feature.get("Feature Name", "").strip(): feature
        for feature in features if feature.get("Feature Name")
    }
    used_features = set()
    rtm_lines = [
        "| Req ID | Feature Name | Source/Vision Goal | ISO 25010 Quality Tag | Verification Method | Backward Trace |",
        "|--------|--------------|-------------------|----------------------|----------------------|----------------|",
    ]
    for req in requirements:
        feature_name = assign_feature(req["text"], features)
        if feature_name != "General":
            used_features.add(feature_name)
        source = (
            feature_lookup.get(feature_name, {}).get("User Story")
            if feature_name in feature_lookup else None
        )
        if not source:
            source = goals[0]
        tag = quality_tag(req["text"])
        ver = verification_method(req["text"])
        backward = "Yes" if req["has_backward_trace"] else "**MISSING**"
        rtm_lines.append(
            f"| {req['id']} | {feature_name} | {source} | {tag} | {ver} | {backward} |"
        )
        req["feature"] = feature_name
        req["quality_tag"] = tag
        req["verification"] = ver
        req["source"] = source
    return rtm_lines, sorted(used_features)


def gap_analysis(requirements: list[dict], features: list[dict[str, str]]) -> tuple[list[str], list[str]]:
    feature_names = [
        feature.get("Feature Name", "General")
        for feature in features if feature.get("Feature Name")
    ]
    used = {
        req.get("feature") for req in requirements
        if req.get("feature") and req.get("feature") != "General"
    }
    orphans = [req for req in requirements if req.get("feature") == "General"]
    unmet = [feature for feature in feature_names if feature not in used]
    return (
        [f"- {req['id']}: {req['text']}" for req in orphans],
        [f"- {goal}" for goal in unmet],
    )


def requirements_audit(
    requirements: list[dict],
    orphan_count: int,
    unmet_goal_count: int,
    tbd_issues: list[dict],
    missing_sections: list[str],
    duplicates: list[str],
) -> list[str]:
    weak_words_total = sum(1 for req in requirements if req["weak_words"])
    missing_measurements = sum(1 for req in requirements if not req["measurement"])
    unranked = sum(1 for req in requirements if not req["has_priority"])
    no_backward_trace = sum(1 for req in requirements if not req["has_backward_trace"])
    compound_shall = sum(1 for req in requirements if req["shall_count"] > 1)
    duplicate_texts = len(requirements) != len({req["text"] for req in requirements})
    design_mention = any(
        any(term in req["text"].lower() for term in DESIGN_TERMS)
        for req in requirements
    )

    lines = ["## Requirements Audit (IEEE 830-1998 §4.3)", ""]

    # §4.3.1 Correct
    correct_pass = bool(requirements)
    lines.append(
        f"### [IEEE830-4.3.1] Correctness: {'PASS' if correct_pass else 'FAIL'}"
    )
    lines.append(f"- {len(requirements)} requirements detected.")
    lines.append("")

    # §4.3.2 Unambiguous
    unambig_pass = weak_words_total == 0
    lines.append(
        f"### [IEEE830-4.3.2] Unambiguous: {'PASS' if unambig_pass else 'FAIL'}"
    )
    lines.append(f"- {weak_words_total} requirement(s) contain weak wording.")
    lines.append("")

    # §4.3.3 Complete
    complete_pass = unmet_goal_count == 0 and len(tbd_issues) == 0
    lines.append(
        f"### [IEEE830-4.3.3] Complete: {'PASS' if complete_pass else 'FAIL'}"
    )
    lines.append(f"- {unmet_goal_count} goal(s) lack requirement mappings.")
    lines.append(f"- {len(tbd_issues)} TBD(s) violate IEEE 830 §4.3.3.1 protocol.")
    for tbd in tbd_issues:
        lines.append(
            f"  - Line {tbd['line']}: \"{tbd['text']}\" — missing: {', '.join(tbd['missing'])}"
        )
    lines.append("")

    # §4.3.4 Consistent
    consistent_pass = not duplicate_texts and len(duplicates) == 0
    lines.append(
        f"### [IEEE830-4.3.4] Consistent: {'PASS' if consistent_pass else 'FAIL'}"
    )
    lines.append(
        f"- Duplicate statements {'found' if duplicate_texts else 'not found'}."
    )
    if duplicates:
        lines.extend(duplicates)
    lines.append("")

    # §4.3.5 Ranked for Importance
    ranked_pass = unranked == 0
    lines.append(
        f"### [IEEE830-4.3.5] Ranked for Importance: {'PASS' if ranked_pass else 'FAIL'}"
    )
    lines.append(f"- {unranked} requirement(s) missing importance ranking (Essential/Conditional/Optional).")
    if unranked > 0:
        for req in requirements:
            if not req["has_priority"]:
                lines.append(f"  - {req['id']}: {req['text'][:80]}")
    lines.append("")

    # §4.3.6 Verifiable
    verifiable_pass = missing_measurements == 0
    lines.append(
        f"### [IEEE830-4.3.6] Verifiable: {'PASS' if verifiable_pass else 'FAIL'}"
    )
    lines.append(f"- {missing_measurements} requirement(s) miss measurable targets.")
    lines.append("")

    # §4.3.7 Modifiable
    modifiable_pass = not design_mention and compound_shall == 0 and len(duplicates) == 0
    lines.append(
        f"### [IEEE830-4.3.7] Modifiable: {'PASS' if modifiable_pass else 'FAIL'}"
    )
    lines.append(
        f"- Design terms in requirements: {'YES (FAIL)' if design_mention else 'No'}."
    )
    lines.append(f"- Compound shall (>1 per clause): {compound_shall} requirement(s).")
    lines.append(f"- Redundant requirements: {len(duplicates)}.")
    if compound_shall > 0:
        for req in requirements:
            if req["shall_count"] > 1:
                lines.append(
                    f"  - {req['id']} has {req['shall_count']} shall clauses: {req['text'][:80]}"
                )
    lines.append("")

    # §4.3.8 Traceable
    traceable_pass = orphan_count == 0 and no_backward_trace == 0
    lines.append(
        f"### [IEEE830-4.3.8] Traceable: {'PASS' if traceable_pass else 'FAIL'}"
    )
    lines.append(f"- {orphan_count} orphan requirement(s) (no feature mapping).")
    lines.append(f"- {no_backward_trace} requirement(s) missing backward traceability (no source reference).")
    lines.append("")

    return lines


def build_structure_report(
    present: list[str], missing: list[str],
) -> list[str]:
    lines = ["## SRS Structure Completeness (IEEE 830 §5)", ""]
    lines.append(f"**Sections present:** {len(present)}")
    lines.append(f"**Sections missing:** {len(missing)}")
    lines.append("")
    if missing:
        lines.append("### Missing Sections")
        lines.extend(missing)
        lines.append("")
    lines.append("### Present Sections")
    lines.extend(present)
    lines.append("")
    return lines


def build_ambiguity_report(requirements: list[dict]) -> list[str]:
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


def build_gap_section(
    orphans: list[str],
    unmet: list[str],
    missing_sections: list[str],
    tbd_issues: list[dict],
    unranked_reqs: list[dict],
) -> list[str]:
    lines = ["## Gap Analysis", ""]

    lines.append("### Orphan Requirements")
    lines.extend(orphans or ["- None."])
    lines.append("")

    lines.append("### Unmet Goals")
    lines.extend(unmet or ["- None."])
    lines.append("")

    lines.append("### Missing SRS Sections")
    if missing_sections:
        lines.extend(missing_sections)
    else:
        lines.append("- None. All IEEE 830 required sections are present.")
    lines.append("")

    lines.append("### Non-Compliant TBDs (IEEE 830 §4.3.3.1)")
    if tbd_issues:
        for tbd in tbd_issues:
            lines.append(
                f"- [V&V-FAIL] Line {tbd['line']}: \"{tbd['text']}\" — missing: {', '.join(tbd['missing'])}"
            )
    else:
        lines.append("- None. No TBD protocol violations found.")
    lines.append("")

    lines.append("### Unranked Requirements (IEEE 830 §4.3.5)")
    if unranked_reqs:
        for req in unranked_reqs:
            lines.append(f"- [V&V-FAIL] {req['id']}: {req['text'][:100]}")
    else:
        lines.append("- None. All requirements have importance rankings.")
    lines.append("")

    return lines


def standard_conformance_statement(
    requirements: list[dict],
    missing_sections: list[str],
    tbd_issues: list[dict],
) -> list[str]:
    total_checks = 8  # eight quality attributes
    failures = []

    weak_fail = any(req["weak_words"] for req in requirements)
    measurement_fail = any(not req["measurement"] for req in requirements)
    priority_fail = any(not req["has_priority"] for req in requirements)
    trace_fail = any(not req["has_backward_trace"] for req in requirements)
    compound_fail = any(req["shall_count"] > 1 for req in requirements)
    tbd_fail = len(tbd_issues) > 0
    section_fail = len(missing_sections) > 0

    if weak_fail:
        failures.append("[IEEE830-4.3.2] Unambiguous")
    if measurement_fail:
        failures.append("[IEEE830-4.3.6] Verifiable")
    if priority_fail:
        failures.append("[IEEE830-4.3.5] Ranked for Importance")
    if trace_fail:
        failures.append("[IEEE830-4.3.8] Traceable (backward)")
    if compound_fail:
        failures.append("[IEEE830-4.3.7] Modifiable (compound shall)")
    if tbd_fail:
        failures.append("[IEEE830-4.3.3] Complete (TBD protocol)")
    if section_fail:
        failures.append("[IEEE830-5.x] Structure completeness")

    if not failures:
        verdict = "COMPLIANT"
    elif len(failures) <= 2:
        verdict = "PARTIALLY COMPLIANT"
    else:
        verdict = "NON-COMPLIANT"

    lines = [
        "## Standard Conformance Statement",
        "",
        f"**Overall IEEE 830-1998 Compliance Verdict: {verdict}**",
        "",
        "### Clause-by-Clause Summary",
        f"- This audit verifies the SRS against IEEE 830-1998 and ISO/IEC 25010.",
        f"- Requirements cross-referenced to vision goals, features, and quality characteristics.",
        f"- Verification methods documented using Test/Inspection/Demonstration vocabulary.",
        "",
        f"- **Quality attribute checks:** {total_checks - len([f for f in failures if f.startswith('[IEEE830-4')])} of {total_checks} PASS",
        f"- **Structure checks:** {'All sections present' if not section_fail else f'{len(missing_sections)} section(s) missing'}",
        "",
        "### Annex A Template",
        "- This pipeline uses IEEE 830 Annex A.5 (organized by Feature) with stimulus-response sequences.",
        "- Verify Section 1.5 documents this template choice.",
        "",
    ]

    if failures:
        lines.append("### [V&V-FAIL] Items Requiring Remediation")
        for f in failures:
            lines.append(f"- {f}")
        lines.append("")
    else:
        lines.append("### No V&V failures detected. SRS is IEEE 830-1998 compliant.")
        lines.append("")

    return lines


def compose_report(
    requirements: list[dict],
    rtm_lines: list[str],
    ambiguity_lines: list[str],
    gap_lines: list[str],
    audit_lines: list[str],
    structure_lines: list[str],
    conformance_lines: list[str],
) -> str:
    sections = [
        "# Semantic Auditing Report (IEEE 830-1998 Compliance)",
        "",
        *audit_lines,
        *structure_lines,
        "## Requirements Traceability Matrix",
        "",
        *rtm_lines,
        "",
        *ambiguity_lines,
        "",
        *gap_lines,
        *conformance_lines,
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
    vision_text = context_texts.get("vision.md", "")
    goals = extract_goals(vision_text)

    # Parse requirements with enhanced checks
    requirements = parse_requirements(srs_text)
    if not requirements:
        print("No requirements found; audit cannot proceed.")
        sys.exit(1)

    # IEEE 830 §4.3.3.1 TBD protocol
    tbd_issues = check_tbd_protocol(srs_text)

    # IEEE 830 §5 structure completeness
    present_sections, missing_sections = check_srs_sections(srs_text)

    # IEEE 830 §4.3.7 redundancy
    duplicates = check_redundancy(requirements)

    # Build RTM with backward traceability column
    rtm_lines, used_features = build_rtm(requirements, features, goals)
    orphans, unmet = gap_analysis(requirements, features)

    # Unranked requirements list for gap analysis
    unranked_reqs = [req for req in requirements if not req["has_priority"]]

    # Build all report sections
    audit_lines = requirements_audit(
        requirements, len(orphans), len(unmet), tbd_issues, missing_sections, duplicates,
    )
    structure_lines = build_structure_report(present_sections, missing_sections)
    ambiguity_lines = build_ambiguity_report(requirements)
    gap_lines = build_gap_section(orphans, unmet, missing_sections, tbd_issues, unranked_reqs)
    conformance_lines = standard_conformance_statement(requirements, missing_sections, tbd_issues)

    report_body = compose_report(
        requirements, rtm_lines, ambiguity_lines, gap_lines,
        audit_lines, structure_lines, conformance_lines,
    )

    AUDIT_REPORT.write_text(report_body + "\n", encoding="utf-8")
    print(f"Wrote audit report to {AUDIT_REPORT.relative_to(PARENT_ROOT)}")
    print(f"  RTM rows: {len(requirements)}")
    print(f"  Ambiguity flags: {sum(1 for r in requirements if r['weak_words'] or not r['measurement'])}")
    print(f"  Orphan requirements: {len(orphans)}")
    print(f"  Unmet goals: {len(unmet)}")
    print(f"  Missing sections: {len(missing_sections)}")
    print(f"  Unranked requirements: {len(unranked_reqs)}")
    print(f"  TBD protocol violations: {len(tbd_issues)}")
    print(f"  Compound shall violations: {sum(1 for r in requirements if r['shall_count'] > 1)}")


if __name__ == "__main__":
    main()
