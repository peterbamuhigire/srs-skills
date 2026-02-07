"""Generate Section 2.0 (Descriptive Modeling) by analyzing tech stack, features, and quality context."""

from pathlib import Path
import sys

MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
PROJECT_CONTEXT = PARENT_ROOT / "project_context"
OUTPUT_DIR = PARENT_ROOT / "output"
SRS_FILE = OUTPUT_DIR / "SRS_Draft.md"
TECH_STACK = PROJECT_CONTEXT / "tech_stack.md"
FEATURES = PROJECT_CONTEXT / "features.md"
QUALITY = PROJECT_CONTEXT / "quality_standards.md"


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required context file missing: {path.relative_to(PARENT_ROOT)}")
    print(f"Reading {path.relative_to(PARENT_ROOT)}")
    return path.read_text(encoding="utf-8")


def strip_section(text: str) -> str:
    if "# Section 2.0" in text:
        index = text.index("# Section 2.0")
        return text[:index]
    return text


def parse_markdown_table(content: str) -> list[dict[str, str]]:
    rows = []
    table_lines = [line.strip() for line in content.splitlines() if line.strip().startswith("|")]
    if len(table_lines) < 3:
        return rows
    header_cells = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    for data_line in table_lines[2:]:
        if not data_line.startswith("|"):
            continue
        cells = [cell.strip() for cell in data_line.strip("|").split("|")]
        if len(cells) < len(header_cells):
            cells.extend([""] * (len(header_cells) - len(cells)))
        rows.append({header_cells[i]: cells[i] for i in range(len(header_cells))})
    return rows


def detect_infrastructure(text: str) -> dict[str, list[str]]:
    keywords = ["Ubuntu", "Debian", "OCI", "MySQL", "PostgreSQL", "HP Z440", "NVMe", "RAM", "TPM"]
    found = {kw: [] for kw in keywords}
    for line in text.splitlines():
        for kw in keywords:
            if kw.lower() in line.lower():
                found[kw].append(line.strip().replace('\t', ' '))
    return {k: v for k, v in found.items() if v}


def group_features(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    groups = {
        "Verification & Traceability": ["traceability", "requirements"],
        "Maintenance & Operations": ["maintenance", "seeder", "documentation"],
        "Performance & Alerting": ["performance", "alert"],
        "Stakeholder Compliance": ["fit", "sign-off", "workflow"],
    }
    categorized = {group: [] for group in groups}
    categorized["General Capabilities"] = []
    for row in rows:
        name = row.get("Feature Name", "Unknown Feature")
        assigned = False
        lower = name.lower()
        for group, keywords in groups.items():
            if any(keyword in lower for keyword in keywords):
                categorized[group].append(name)
                assigned = True
                break
        if not assigned:
            categorized["General Capabilities"].append(name)
    return categorized


def build_product_perspective(infra: dict[str, list[str]]) -> str:
    lines = ["### 2.1 Product Perspective"]
    lines.append("#### System Interfaces")
    if infra.get("OCI"):
        lines.append("- OCI compute nodes and networking are referenced as the primary hosting fabric; the system communicates with OCI-managed services via HTTPS APIs and private peering.")
    else:
        lines.append("- Primary hosting fabric is the configured on-premise environment plus documented third-party platforms.")
    if infra.get("MySQL"):
        lines.append("- System interfaces include a MySQL 8.0 instance optimized for concurrency and row-level security.")
    elif infra.get("PostgreSQL"):
        lines.append("- System interfaces include PostgreSQL 16.1 with synchronous replication for data services.")
    lines.append("#### User Interfaces")
    lines.append("- Web-based dashboards provide traceability visibility, Fit Criteria reporting, and workflow controls for stakeholders and QA leads.")
    lines.append("- Role-based UI flows present limited operations per persona (admin, reviewer, operator).")
    lines.append("#### Hardware Interfaces")
    if infra.get("HP Z440"):
        lines.append("- HP Z440 workstations host governance tooling; connectors expose USB/serial for local instrumentation.")
    if infra.get("TPM"):
        lines.append("- TPM 2.0 modules on the hardware provide secure boot and key storage.")
    if infra.get("NVMe"):
        lines.append("- NVMe SSDs meet storage throughput requirements, delivering the write endurance noted in tech_stack.md.")
    lines.append("#### Memory Constraints")
    ram_lines = [line for line in infra.get("RAM", [])]
    if ram_lines:
        lines.append(f"- RAM constraints follow the stated requirement: {ram_lines[0]}.")
    else:
        lines.append("- Memory key points were not explicitly captured; maintain at least 32 GB ECC for production nodes.")
    lines.append("#### System Block Diagram Description")
    lines.append("- The diagram represents users interacting with the KampusPad portal, leading into the application layer (authentication, requirement tracking, traceability), which connects via secure APIs to data services (MySQL/Postgres) and monitoring nodes hosted on OCI or HP Z440 hardware.")
    return "\n".join(lines)


def build_product_functions(groups: dict[str, list[str]]) -> str:
    lines = ["### 2.2 Product Functions"]
    for capability, features in groups.items():
        if not features:
            continue
        lines.append(f"- {capability}:")
        for feature in features:
            lines.append(f"  - {feature}")
    if not any(groups.values()):
        lines.append("- Product functions will be detailed once additional feature documentation is provided.")
    return "\n".join(lines)


def build_user_characteristics() -> str:
    personas = [
        ("System Admin", "Expert-level proficiency with OCI console, Linux shell, and configuration enforcement tasks."),
        ("End User", "Proficient with browser-based dashboards and able to interpret traceability reports with minimal training."),
        ("QA Lead", "Comfortable assessing requirement/test linkage and verifying Fit Criteria through provided dashboards."),
    ]
    lines = ["### 2.3 User Characteristics"]
    for persona, proficiency in personas:
        lines.append(f"- {persona}: {proficiency}")
    return "\n".join(lines)


def build_constraints(quality_content: str) -> str:
    lines = ["### 2.4 Constraints"]
    lines.append("- ISO/IEC 25051 mandates ready-to-use software; the platform SHALL deliver fully packaged deployments with documented configuration tables and no custom build steps.")
    lines.append("- Local environmental factors (intermittent power and variable internet stability in Uganda) REQUIRE offline logging, resume capabilities, and tolerance for reconnecting workflows.")
    if "Portability" in quality_content:
        lines.append("- Portability requirements demand documented deployment rehearsals within 45 minutes to prove transferability.")
    return "\n".join(lines)


def build_assumptions_dependencies(infra: dict[str, list[str]]) -> str:
    lines = ["### 2.5 Assumptions and Dependencies"]
    lines.append("- Assumes OCI compute fabric or HP Z440 hardware remains available for deployment; any change triggers a new infrastructure review.")
    lines.append("- Depends on MySQL 8.0 (or PostgreSQL 16.1) with row-level security and synchronous replication to satisfy data consistency.")
    lines.append("- Relies on readily available monitoring and logging suites referenced in quality_standards.md for traceability and security checks.")
    lines.append("- Assumes power/internet resilience plans include UPS backups and scheduled maintenance notifications.")
    return "\n".join(lines)


def write_section(existing: str, body: str) -> None:
    content = strip_section(existing)
    new_section = "# Section 2.0 – Descriptive Modeling\n" + body + "\n"
    final = content.rstrip() + "\n\n" + new_section
    SRS_FILE.write_text(final.strip() + "\n", encoding="utf-8")
    print(f"Updated {SRS_FILE.relative_to(PARENT_ROOT)} with Section 2.0")


def main() -> None:
    try:
        tech_text = read_file(TECH_STACK)
        features_text = read_file(FEATURES)
        quality_text = read_file(QUALITY)
    except FileNotFoundError as exc:
        print(exc)
        sys.exit(1)

    ensure_output_dir()
    existing = SRS_FILE.read_text(encoding="utf-8") if SRS_FILE.exists() else ""
    infra = detect_infrastructure(tech_text)
    feature_rows = parse_markdown_table(features_text)
    print(f"Parsed {len(feature_rows)} feature rows.")
    feature_groups = group_features(feature_rows)
    for capability, features in feature_groups.items():
        if features:
            print(f"Capability '{capability}' includes: {', '.join(features)}")

    perspective = build_product_perspective(infra)
    functions = build_product_functions(feature_groups)
    users = build_user_characteristics()
    constraints = build_constraints(quality_text)
    assumptions = build_assumptions_dependencies(infra)

    body = "\n\n".join([perspective, functions, users, constraints, assumptions])
    write_section(existing, body)


if __name__ == "__main__":
    main()