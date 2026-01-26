"""Generate Section 1.0 (Introduction) by synthesizing the parent project's context files."""

from pathlib import Path
import os
import sys

MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
PROJECT_CONTEXT = PARENT_ROOT / "project_context"
OUTPUT_DIR = PARENT_ROOT / "output"
SRS_FILE = OUTPUT_DIR / "SRS_Draft.md"
VISION_FILE = PROJECT_CONTEXT / "vision.md"
GLOSSARY_FILE = PROJECT_CONTEXT / "glossary.md"
PROJECT_NAME = os.environ.get("SRS_PROJECT_NAME", "KampusPad")
LARGE_SYSTEMS = "OCI compute fabric and the Ugandan University Ecosystem"


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required context file missing: {path.relative_to(PARENT_ROOT)}")
    return path.read_text(encoding="utf-8")


def extract_section(content: str, heading: str) -> str:
    lines = content.splitlines()
    capture = False
    block_lines = []
    for line in lines:
        stripped = line.strip()
        if not capture:
            if stripped.lower() == heading.lower():
                capture = True
            continue
        if stripped.startswith("## ") and stripped.lower() != heading.lower():
            break
        block_lines.append(line)
    return "\n".join(block_lines).strip()


def extract_bullets(section_text: str) -> list[str]:
    bullets = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("-"):
            bullets.append(stripped.lstrip("- ").strip())
    return bullets


def parse_markdown_table(section_text: str) -> list[dict[str, str]]:
    rows = []
    table_lines = [line.strip() for line in section_text.splitlines() if line.strip().startswith("|")]
    if len(table_lines) < 3:
        return rows
    header_cells = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    for data_line in table_lines[2:]:
        if not data_line.startswith("|"):
            continue
        cells = [cell.strip() for cell in data_line.strip("|").split("|")]
        if len(cells) < len(header_cells):
            cells.extend([""] * (len(header_cells) - len(cells)))
        row = {header_cells[i]: cells[i] for i in range(len(header_cells))}
        rows.append(row)
    return rows


def build_scope_from_stakeholders(stakeholders: list[dict[str, str]]) -> list[str]:
    scope_lines = []
    for entry in stakeholders:
        stakeholder = entry.get("Stakeholder") or entry.get("Stakeholder Group") or "Stakeholder"
        need = (
            entry.get("Need")
            or entry.get("Primary Concerns")
            or entry.get("Key Roles")
            or entry.get("Primary Concerns")
        )
        if not need:
            continue
        scope_lines.append(f"- Deliver capabilities that satisfy {stakeholder} by {need}.")
    return scope_lines


def build_definitions_table(definitions: list[dict[str, str]]) -> str:
    if not definitions:
        return """| Term | Definition |
|-| - |
| TBD | Definitions will be inserted once glossary is populated. |"""
    lines = ["| Term | Definition |", "|------|------------|"]
    for row in definitions:
        term = row.get("Term", "").strip()
        definition = row.get("Definition", "").strip()
        if term and definition:
            lines.append(f"| {term} | {definition} |")
    return "\n".join(lines)


def write_srs(purpose: str, scope_block: str, definitions: str, references: str, overview: str) -> None:
    header = "# Section 1.0 – Introduction\n" + "The following section captures the formal introduction that guides the IEEE/ISO SRS downstream work.\n\n"
    body = (
        f"## 1.1 Purpose\n{purpose}\n\n"
        f"## 1.2 Scope\n{scope_block}\n\n"
        f"## 1.3 Definitions, Acronyms, and Abbreviations\n{definitions}\n\n"
        f"## 1.4 References\n{references}\n\n"
        f"## 1.5 Overview\n{overview}\n"
    )
    SRS_FILE.write_text(header + body, encoding="utf-8")
    print(f"Wrote Section 1.0 to {SRS_FILE.relative_to(PARENT_ROOT)}")


def first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        clean = line.strip()
        if clean:
            return clean
    return ""


def build_purpose(problem_statement: str, technical_scope: str) -> str:
    business_line = first_non_empty_line(problem_statement.replace("**", "")) or "addresses the business intent documented in vision.md."
    technical_line = first_non_empty_line(technical_scope.replace("**", ""))
    purpose_lines = [
        f"{PROJECT_NAME} provides the platform that {business_line}",
        "This SRS records the requirements for Version 1.0, enabling developers, testers, and stakeholders to agree on behavior, quality criteria, and traceability links.",
    ]
    if technical_line:
        purpose_lines.append(
            f"Technical scope is limited to the infrastructure, APIs, and governance processes described in System Constraints: {technical_line}."
        )
    purpose_lines.append(
        "Business intent statements originate from the Problem Statement block, while Technical Scope statements come from the System Constraints section; each scope item remains traceable to that Stakeholder Needs table."
    )
    return "\n".join(purpose_lines)


def build_scope(stakeholders: list[dict[str, str]], constraint_bullets: list[str]) -> str:
    scope_items = build_scope_from_stakeholders(stakeholders)
    if constraint_bullets:
        for bullet in constraint_bullets:
            scope_items.append(f"- Respect the constraint that {bullet} (per System Constraints).")
    if not scope_items:
        scope_items.append("- Scope details will be populated once stakeholder needs and system constraints are clarified.")
    scope_items.append(f"- Integrate {PROJECT_NAME} with {LARGE_SYSTEMS} so the platform can exchange data with university ecosystems and OCI-hosted services.")
    scope_items.append("- Traceability is maintained by linking each item to the Stakeholder Needs table in vision.md.")
    return "\n".join(scope_items)


def build_references() -> str:
    standards = [
        "IEEE Std 830-1998: Software Requirements Specifications",
        "IEEE Std 1233-1998: System Requirements Development",
        "IEEE Std 610.12-1990: Software Engineering Terminology",
        "ASTM E1340-96: Rapid Prototyping of Computerized Systems",
        "US ISO/IEC 25010: Systems and Software Quality Requirements and Evaluation (SQuaRE) - Quality Model",
        "US ISO/IEC 25023: Systems and Software Quality Requirements and Evaluation (SQuaRE) - Measurement of System and Software Product Quality",
        "US ISO/IEC 25051: Systems and Software Engineering - Requirements for Procuring Off-the-Shelf Software",
        "US ISO/IEC 15504-1: Information Technology — Process Assessment - Concepts and Terminology",
    ]
    project_docs = ["vision.md", "glossary.md", "quality_standards.md"]
    lines = [f"- {std}" for std in standards]
    lines.append("- Project context files: " + ", ".join(project_docs))
    return "\n".join(lines)


def build_overview() -> str:
    return (
        "Section 2.0 will document the system description and user needs.\n"
        "Section 3.0 will cover specific system features converted from the Feature Set template.\n"
        "Sections 4.0 through 8.0 will address interfaces, requirements, non-functional constraints, validation, and traceability matrices.\n"
        "The roadmap reinforces the IEEE Std 830 structure and keeps the team aligned."
    )


def main() -> None:
    try:
        print(f"Reading {VISION_FILE.relative_to(PARENT_ROOT)}")
        vision_text = read_file(VISION_FILE)
        print(f"Reading {GLOSSARY_FILE.relative_to(PARENT_ROOT)}")
        glossary_text = read_file(GLOSSARY_FILE)
    except FileNotFoundError as exc:
        print(exc)
        sys.exit(1)

    problem_statement = extract_section(vision_text, "## 1. Problem Statement")
    system_constraints = extract_section(vision_text, "## System Constraints")
    stakeholder_section = extract_section(vision_text, "## Stakeholder Needs (ISO/IEC 1233)")
    stakeholder_rows = parse_markdown_table(stakeholder_section)
    glossary_rows = parse_markdown_table(glossary_text)
    constraint_bullets = extract_bullets(system_constraints)
    print(f"Parsed {len(stakeholder_rows)} stakeholder entries.")
    print(f"Parsed {len(constraint_bullets)} system constraint bullets.")
    print(f"Parsed {len(glossary_rows)} glossary definitions.")

    ensure_output_dir()

    purpose = build_purpose(problem_statement, system_constraints)
    scope = build_scope(stakeholder_rows, constraint_bullets)
    definitions = build_definitions_table(glossary_rows)
    references = build_references()
    overview = build_overview()

    write_srs(purpose, scope, definitions, references, overview)


if __name__ == "__main__":
    main()
