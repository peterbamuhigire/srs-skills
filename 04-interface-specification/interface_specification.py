"""Generate Section 3.1 (Interface Specification) by mapping context files to interface details."""

import re
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


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    rows = []
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


def detect_infrastructure(text: str) -> dict[str, list[str]]:
    keywords = ["Ubuntu", "Debian", "OCI", "MySQL", "PostgreSQL", "HP Z440", "NVMe", "RAM", "TPM", "Bluetooth", "BLE"]
    matches = {kw: [] for kw in keywords}
    for line in text.splitlines():
        trimmed = line.strip()
        if not trimmed:
            continue
        for kw in keywords:
            if kw.lower() in trimmed.lower():
                matches[kw].append(trimmed)
    return {k: v for k, v in matches.items() if v}


def extract_external_actors(rows: list[dict[str, str]]) -> list[str]:
    actors = set()
    pattern = re.compile(r"As an? ([^,\.]+)")
    for row in rows:
        story = row.get("User Story", "")
        if match := pattern.search(story):
            actors.add(match.group(1).strip())
    if not actors:
        actors.update(["Product Owner", "Systems Engineer", "QA Lead"])
    return sorted(actors)


def external_actor_sentence(actors: list[str], infra: dict[str, list[str]]) -> str:
    services = []
    if "OCI" in infra:
        services.append("OCI REST APIs")
    if "MySQL" in infra:
        services.append("MySQL 8.0 instance")
    if "PostgreSQL" in infra:
        services.append("PostgreSQL 16.1 analytics store")
    service_clause = f" and the services ({', '.join(services)})" if services else ""
    return f"External actors include {', '.join(actors)}{service_clause}."


def build_user_interfaces(actors: list[str]) -> str:
    lines = ["### 3.1.1 User Interfaces"]
    lines.append("- Interfaces shall implement a web-based responsive design with role-based dashboards that span traceability, Fit Criteria reporting, and maintenance controls exposed to the registered actors.")
    lines.append("- Input validation SHALL follow ISO/IEC 25062, delivering field-level constraints, format hints, and structured error messaging tied to logged ticket IDs.")
    lines.append("- Error notifications SHALL reference ISO/IEC 25062 guidance, avoid vague ‘friendly’ adjectives, and provide corrective actions aligned with the active actor persona.")
    lines.append(f"- Supported actors: {', '.join(actors)}.")
    return "\n".join(lines)


def build_hardware_interfaces(infra: dict[str, list[str]]) -> str:
    lines = ["### 3.1.2 Hardware Interfaces"]
    lines.append("- Hardware interfaces shall honor the HP Z440 workstations, TPM 2.0 modules, and OCI compute shapes detailed in tech_stack.md.")
    lines.append("| Device | Interface | Notes |")
    lines.append("|--------|-----------|-------|")
    if "HP Z440" in infra:
        lines.append("| HP Z440 workstation | USB 3.0, serial console, TPM 2.0 | Governance tooling runs on-premise via this host. |")
    if "OCI" in infra:
        lines.append("| OCI VM.Standard.E3.Flex | Virtual NICs, NVMe bus | OCI nodes present virtualized Ethernet and NVMe storage. |")
    lines.append("| Bluetooth / BLE peripherals | BLE 5.2 radios | Optional peripheral devices such as kiosks or printers interface through BLE. |")
    lines.append("| Network infrastructure | IEEE 802.11ax, Gigabit Ethernet | Wireless and wired connectivity for admin consoles and on-site devices. |")
    lines.append("- Memory constraints reference the stated RAM guidance; production nodes SHALL provision at least 32 GB ECC. ")
    return "\n".join(lines)


def build_software_interfaces(infra: dict[str, list[str]]) -> str:
    lines = ["### 3.1.3 Software Interfaces"]
    lines.append("- Software interfaces list every external database, API, or library plus its protocol, version, and interaction mode.")
    lines.append("| Interface | Version | Protocol | Description |")
    lines.append("|-----------|---------|----------|-------------|")
    if "MySQL" in infra:
        lines.append("| MySQL database | 8.0 Enterprise | SQL/TCP over TLS 1.3 (Port 3306) | Central requirements store with row-level security and concurrency tuning. |")
    if "PostgreSQL" in infra:
        lines.append("| PostgreSQL database | 16.1 | Native TCP (Port 5432) | Analytics workloads and reporting services. |")
    if "OCI" in infra:
        lines.append("| OCI REST APIs | 2026-01 | HTTPS/TLS 1.3 (Port 443) | Identity and orchestration via RFC 7519 (JWT) bearer tokens. |")
    lines.append("| KampusPad Traceability API | 1.0 | RESTful JSON over HTTPS (Port 443) | Exposes requirements and verification links for stakeholders. |")
    lines.append("| Logging & Monitoring Suite | v3.5 | gRPC/TLS 1.3 | Streams telemetry to Ops dashboards and alert pipelines. |")
    return "\n".join(lines)


def build_communications(infra: dict[str, list[str]], quality_text: str) -> str:
    lines = ["### 3.1.4 Communications Interfaces"]
    lines.append("- Communications SHALL use IPv4/IPv6 stacks with TLS 1.3 enforced end-to-end and JWT tokens for API authentication.")
    lines.append("- Ports include 443 for HTTPS, 3306 for MySQL, and 5432 for PostgreSQL; additional ports require documented risk approvals.")
    lines.append("- The connectivity map describes client dashboards -> load balancer -> application services -> MySQL/PostgreSQL clusters -> OCI services over private peering.")
    lines.append("- Wireless access for administration consoles SHALL comply with IEEE 802.11ax and operate inside compliance VLANs that mirror the security posture of the wired stack.")
    if "Compatibility" in quality_text:
        lines.append("- ISO/IEC 25010 Compatibility requirements further constrain the communication interfaces so that API contracts remain stable across supported OS/browser combinations.")
    return "\n".join(lines)


def insert_section(existing: str, section_text: str) -> str:
    marker = "# Section 3.1 – Interface Specification"
    if marker in existing:
        start = existing.index(marker)
        end = existing.find("\n# Section", start + len(marker))
        if end == -1:
            existing = existing[:start].rstrip()
        else:
            existing = existing[:start].rstrip() + "\n" + existing[end:].lstrip()
    existing = existing.strip()
    if not existing:
        return section_text.strip() + "\n"
    section2 = "# Section 2.0"
    idx = existing.find(section2)
    if idx == -1:
        return existing.rstrip() + "\n\n" + section_text.strip() + "\n"
    next_idx = existing.find("\n# Section", idx + len(section2))
    if next_idx == -1:
        return existing.rstrip() + "\n\n" + section_text.strip() + "\n"
    return existing[:next_idx].rstrip() + "\n\n" + section_text.strip() + "\n\n" + existing[next_idx:].lstrip()


def main() -> None:
    try:
        tech_text = read_file(TECH_STACK)
        features_text = read_file(FEATURES)
        quality_text = read_file(QUALITY)
    except FileNotFoundError as exc:
        print(exc)
        sys.exit(1)

    ensure_output_dir()
    existing_text = SRS_FILE.read_text(encoding="utf-8") if SRS_FILE.exists() else ""
    infra = detect_infrastructure(tech_text)
    print(f"Detected keywords: {', '.join(infra.keys())}")
    feature_rows = parse_markdown_table(features_text)
    print(f"Parsed {len(feature_rows)} feature rows for actor extraction.")
    actors = extract_external_actors(feature_rows)
    print(f"External actors identified: {', '.join(actors)}")

    section_parts = ["# Section 3.1 – Interface Specification", external_actor_sentence(actors, infra)]
    section_parts.append(build_user_interfaces(actors))
    section_parts.append(build_hardware_interfaces(infra))
    section_parts.append(build_software_interfaces(infra))
    section_parts.append(build_communications(infra, quality_text))

    new_section = "\n\n".join(section_parts)
    final_text = insert_section(existing_text, new_section)
    SRS_FILE.write_text(final_text.strip() + "\n", encoding="utf-8")
    print(f"Wrote Section 3.1 to {SRS_FILE.relative_to(PARENT_ROOT)}")


if __name__ == "__main__":
    main()
