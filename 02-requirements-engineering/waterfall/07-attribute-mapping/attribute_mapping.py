"""Generate Section 3.3–3.5.* by mapping quality characteristics to measurable system attributes."""

from pathlib import Path
import re
import sys

MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
PROJECT_CONTEXT = PARENT_ROOT / "project_context"
OUTPUT_DIR = PARENT_ROOT / "output"
SRS_FILE = OUTPUT_DIR / "SRS_Draft.md"
QUALITY_FILE = PROJECT_CONTEXT / "quality_standards.md"
TECH_STACK_FILE = PROJECT_CONTEXT / "tech_stack.md"


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required context file missing: {path.relative_to(PARENT_ROOT)}")
    print(f"Reading {path.relative_to(PARENT_ROOT)}")
    return path.read_text(encoding="utf-8")


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    table_lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(table_lines) < 3:
        return rows
    headers = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    for line in table_lines[2:]:
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))
        rows.append({headers[i]: cells[i] for i in range(len(headers))})
    return rows


def extract_priority_map(rows: list[dict[str, str]]) -> dict[str, int]:
    return {row.get("Characteristic", f"Characteristic {idx}"): idx + 1 for idx, row in enumerate(rows)}


def find_characteristic(rows: list[dict[str, str]], keyword: str) -> dict[str, str] | None:
    keyword_lower = keyword.lower()
    for row in rows:
        if keyword_lower in row.get("Characteristic", "").lower():
            return row
    return None


def detect_environment(text: str) -> list[str]:
    flags = []
    if re.search(r"intermittent\s+connectivity", text, flags=re.I):
        flags.append("Intermittent Connectivity")
    if re.search(r"power\s+instability", text, flags=re.I):
        flags.append("Power Instability")
    return flags


def parse_tech_stack(text: str) -> list[dict[str, str]]:
    return parse_markdown_table(text)


def summarize_hardware(rows: list[dict[str, str]]) -> str:
    summaries = []
    for row in rows:
        device = row.get("Device") or row.get("Component") or row.get("Hosting") or row.get("Infrastructure") or "hardware"
        detail = row.get("Specification") or row.get("Details") or row.get("Notes") or row.get("Description") or "standard configuration"
        if device and detail:
            summaries.append(f"{device} ({detail})")
    if not summaries:
        return "reference hardware (OCI compute nodes and local workstations)"
    return "; ".join(summaries)


def extract_time_target(measurement: str) -> str | None:
    match = re.search(r"(<=|<|≤|≥|>|=)?\s*(\d+(?:\.\d+)?)\s*(ms|s|seconds?)", measurement, flags=re.I)
    if match:
        value = match.group(2)
        unit = match.group(3)
        normalized = unit.lower()
        if normalized.startswith("ms"):
            return f"{value} ms"
        return f"{value} {unit}"
    return None


def extract_availability_target(measurement: str) -> float | None:
    match = re.search(r"(\d+(?:\.\d+)?)\s*%", measurement)
    if match:
        return float(match.group(1))
    return None


def build_quality_scenario(attribute: str, importance_rank: int, stimulus: str, environment: str, artifact: str, response: str, measure: str) -> list[str]:
    scenario = [f"- Quality Attribute Scenario ({attribute}):"]
    scenario.append(f"  - Ranked Importance: {importance_rank} (IEEE 830 §4.3.5)")
    scenario.append(f"  - Source: {artifact} owner")
    scenario.append(f"  - Stimulus: {stimulus}")
    scenario.append(f"  - Environment: {environment}")
    scenario.append(f"  - Artifact: {artifact}")
    scenario.append(f"  - Response: {response}")
    scenario.append(f"  - Response Measure (ISO/IEC 25023): {measure}")
    return scenario


def build_performance_section(perf_row: dict[str, str] | None, hardware_desc: str, env_flags: list[str], priority_map: dict[str, int]) -> list[str]:
    lines: list[str] = []
    measurement = perf_row.get("Measurement & Target", "Not defined") if perf_row else "Not defined"
    time_target = extract_time_target(measurement) or "500 ms"
    load_condition = (
        measurement.split("under")[-1].strip()
        if perf_row and "under" in measurement
        else "under 100 concurrent analytical users"
    )
    env_note = ", ".join(env_flags) if env_flags else "stable compute and network environment"
    importance = priority_map.get(perf_row.get("Characteristic", "Performance Efficiency"), 1) if perf_row else 1
    lines.append(f"- The system shall respond to requirement traceability queries within {time_target} {load_condition}.")
    lines.append(f"  - Environment Constraint: {env_note}; hardware ceiling: {hardware_desc}.")
    lines.extend(
        build_quality_scenario(
            "Performance",
            importance,
            "Analysts request dashboards",
            env_note,
            "Traceability Dashboard Service",
            f"Response time {time_target} for the dashboard",
            measurement,
        )
    )
    lines.append(f"- The system shall synchronize new requirements data within {time_target} of ingest {load_condition}.")
    lines.append(f"  - Measurement (ISO/IEC 25023): {measurement}")
    lines.extend(
        build_quality_scenario(
            "Performance",
            importance,
            "New requirements arrive via ingestion pipeline",
            env_note,
            "Requirement Ingestion Service",
            f"Data synchronized and indexed within {time_target}",
            measurement,
        )
    )
    if not perf_row:
        lines.append("- Flag: Performance target not measurable; specify latency and load per ISO/IEC 25023.")
    return lines


def build_design_constraints(tech_rows: list[dict[str, str]]) -> list[str]:
    constraints: list[str] = []
    text = " ".join([" ".join(row.values()) for row in tech_rows])
    languages = re.findall(r"(PHP|Python|Node|Java|Go|Rust)\s+(\d+(?:\.\d+)*)", text)
    for lang, version in languages:
        constraints.append(f"- Language: {lang} {version} per technology stack definition.")
    if not languages:
        constraints.append("- Language: Maintain current supported versions defined by stakeholders.")
    dbs = re.findall(r"(MySQL|PostgreSQL)\s+(\d+(?:\.\d+)*)", text)
    for db, version in dbs:
        constraints.append(
            f"- Database: {db} {version} with ACID integrity policies enforced via prepared statements and transaction logging."
        )
    if not dbs:
        constraints.append("- Database: Enforce ACID transactions with per-table integrity guards.")
    constraints.append("- Implementation standards: Follow ISO/IEC 25010 design guidance, enforce TLS 1.3, and log schema changes.")
    return constraints


def build_system_attributes(rows: list[dict[str, str]], env_flags: list[str], priority_map: dict[str, int]) -> list[str]:
    lines: list[str] = []
    reliability = find_characteristic(rows, "Reliability")
    availability = find_characteristic(rows, "Availability") or reliability
    security = find_characteristic(rows, "Security")
    maintainability = find_characteristic(rows, "Maintainability")
    env_note = ", ".join(env_flags) if env_flags else "Standard site power and connectivity"

    def spec_attribute(title: str, row: dict[str, str] | None, default: str) -> list[str]:
        attr_lines = [f"#### 3.5.{title[0]} {title}"]
        measurement = row.get("Measurement & Target", "Not defined") if row else "Not defined"
        importance = priority_map.get(row.get("Characteristic", title) if row else title, 2)
        if title == "Reliability":
            mtbf_hours = re.search(r"(\d+(?:\.\d+)?)\s*(hours|hrs|h)", measurement)
            mtbf_text = f"MTBF ≥ {mtbf_hours.group(1)} hours" if mtbf_hours else "MTBF ≥ 4,500 hours"
            attr_lines.append(f"- {mtbf_text}; measurement via ISO/IEC 25023 reliability tests.")
            attr_lines.append(f"- Quality Attribute Scenario: {title}")
            attr_lines.extend(build_quality_scenario(title, importance, "Subsystem operations continue", env_note, "Operational Services", mtbf_text, measurement))
        elif title == "Availability":
            avail_pct = extract_availability_target(measurement) or (99.9 if reliability else 99.0)
            downtime_hours = (1 - avail_pct / 100) * 8760
            attr_lines.append(f"- The system shall maintain availability ≥ {avail_pct}% per ISO/IEC 25023, implying downtime ≤ {downtime_hours:.1f} hours/year.")
            attr_lines.extend(build_quality_scenario(title, importance, "Users access services", env_note, "Platform Services", f"Availability ≥ {avail_pct}%", measurement))
        elif title == "Security":
            attr_lines.append("- Encryption: AES-256 for data at rest and in transit + TLS 1.3, access control via RBAC.")
            attr_lines.append("- Auditing: Log all privilege changes with ISO timestamp precision.")
            attr_lines.extend(build_quality_scenario(title, importance, "Admin configures access", env_note, "Security Services", "AES-256/RBAC enforced", measurement))
        elif title == "Maintainability":
            attr_lines.append("- Documentation: ISO/IEC 25023 analyzability reports updated each sprint; modularity goals require < 200 LOC modules.")
            attr_lines.append("- Quality gates: Code review coverage ≥ 90% and automated dependency checks.")
            attr_lines.extend(build_quality_scenario(title, importance, "Engineers update modules", env_note, "Maintenance Playbooks", "Documentation refresh and modular refactors", measurement))
        else:
            attr_lines.append(f"- {default}")
        return attr_lines

    lines.extend(spec_attribute("Reliability", reliability, "Define MTBF via monitoring data."))
    lines.extend(spec_attribute("Availability", availability, "Define percentage and downtime."))
    lines.extend(spec_attribute("Security", security, "AES-256 + RBAC combined with ISO/IEC 25023 vulnerability measures."))
    lines.extend(spec_attribute("Maintainability", maintainability, "Define documentation and modularity goals."))
    return lines


def insert_sections(existing: str, block: str) -> str:
    marker = "# Section 3.3 – Performance Requirements"
    cleaned = existing
    if marker in existing:
        start = existing.index(marker)
        next_section = existing.find("\n# Section", start + len(marker))
        if next_section == -1:
            cleaned = existing[:start].rstrip()
        else:
            cleaned = (existing[:start].rstrip() + "\n" + existing[next_section:]).strip()
    insert_point = cleaned.find("# Section 3.2")
    if insert_point == -1:
        return (cleaned.strip() + "\n\n" + block).strip() + "\n"
    next_after_3_2 = cleaned.find("\n# Section", insert_point + len("# Section 3.2"))
    if next_after_3_2 == -1:
        prefix = cleaned[:insert_point].rstrip()
        return (prefix + "\n" + block).strip() + "\n"
    prefix = cleaned[:next_after_3_2].rstrip()
    suffix = cleaned[next_after_3_2:].lstrip()
    return (prefix + "\n\n" + block + "\n\n" + suffix).strip() + "\n"


def main() -> None:
    try:
        quality_text = read_file(QUALITY_FILE)
        tech_text = read_file(TECH_STACK_FILE)
    except FileNotFoundError as exc:
        print(exc)
        sys.exit(1)

    ensure_output_dir()
    quality_rows = parse_markdown_table(quality_text)
    tech_rows = parse_tech_stack(tech_text)
    priority_map = extract_priority_map(quality_rows)
    hardware_desc = summarize_hardware(tech_rows)
    env_flags = detect_environment(quality_text + tech_text)
    perf_row = find_characteristic(quality_rows, "Performance")

    performance_block = build_performance_section(perf_row, hardware_desc, env_flags, priority_map)
    design_block = build_design_constraints(tech_rows)
    attributes_block = build_system_attributes(quality_rows, env_flags, priority_map)

    new_block_lines = [
        "# Section 3.3 – Performance Requirements",
        *performance_block,
        "",
        "# Section 3.4 – Design Constraints",
        *design_block,
        "",
        "# Section 3.5 – Software System Attributes",
        *attributes_block,
    ]
    new_block = "\n".join(new_block_lines)

    existing_text = SRS_FILE.read_text(encoding="utf-8") if SRS_FILE.exists() else ""
    final_text = insert_sections(existing_text, new_block)
    SRS_FILE.write_text(final_text.strip() + "\n", encoding="utf-8")
    print(f"Detected hardware context: {hardware_desc}")
    print(f"Environment constraints: {', '.join(env_flags) if env_flags else 'None'}")
    print("Prioritized characteristics: " + ", ".join(priority_map.keys()))
    print(f"Updated {SRS_FILE.relative_to(PARENT_ROOT)} with attribute mapping sections.")


if __name__ == "__main__":
    main()