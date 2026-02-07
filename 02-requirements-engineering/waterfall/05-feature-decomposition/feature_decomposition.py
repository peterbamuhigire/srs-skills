"""Generate Section 3.2 (Feature Decomposition) by transforming features.md into stimulus/response requirements."""

import re
from pathlib import Path
import sys

MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
PROJECT_CONTEXT = PARENT_ROOT / "project_context"
OUTPUT_DIR = PARENT_ROOT / "output"
SRS_FILE = OUTPUT_DIR / "SRS_Draft.md"
FEATURES_FILE = PROJECT_CONTEXT / "features.md"
QUALITY_FILE = PROJECT_CONTEXT / "quality_standards.md"


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
    for row_line in table_lines[2:]:
        if not row_line.startswith("|"):
            continue
        cells = [cell.strip() for cell in row_line.strip("|").split("|")]
        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))
        rows.append({headers[i]: cells[i] for i in range(len(headers))})
    return rows


def split_bullets(cell: str) -> list[str]:
    if not cell:
        return []
    separators = re.split(r"<br\s*/?>|\n", cell)
    clean = []
    for snippet in separators:
        snippet = snippet.replace("- ", "").strip()
        if snippet:
            clean.append(snippet)
    return clean


def priority_ranking(priority: str) -> str:
    mapping = {"high": "Essential", "medium": "Conditional", "low": "Optional"}
    return mapping.get(priority.lower(), "Conditional")


def has_functional_suitability(quality_text: str) -> bool:
    return "Functional Suitability" in quality_text


def build_feature_section(index: int, row: dict[str, str], quality_text: str) -> str:
    feature_name = row.get("Feature Name", "Unnamed Feature").strip()
    if not feature_name:
        feature_name = "Unnamed Feature"
    user_story = row.get("User Story", "").strip()
    priority = priority_ranking(row.get("Priority", ""))
    functional = split_bullets(row.get("Functional Requirements", ""))
    non_functional = split_bullets(row.get("Non-Functional Requirements", ""))
    acceptance = split_bullets(row.get("Acceptance Criteria", ""))

    sentences = []
    description = f"{feature_name} delivers capabilities described by the stakeholder need: {user_story or 'Not provided'}."
    sentences.append(description)
    suitability_clause = (
        "It addresses the ISO/IEC 25010 Functional Suitability characteristic by ensuring each requirement maps back to measurable behavior."
        if has_functional_suitability(quality_text)
        else "Priority ranking confirms the behavior stays aligned with measurable project goals."
    )
    sentences.append(f"Priority classification: {priority}. {suitability_clause}")

    description_block = "\n".join(sentences)

    stimulus_lines = []
    stimulus_base = user_story or f"A stakeholder requests the {feature_name} capability." 
    for idx, func_req in enumerate(functional[:2], start=1):
        text = func_req.rstrip(".")
        stimulus_lines.append(f"{idx}. When {stimulus_base}, the system shall {text}." if func_req else f"{idx}. {stimulus_base}")
    if not stimulus_lines:
        stimulus_lines.append(f"1. When the {feature_name} trigger occurs, the system shall perform the documented behavior.")

    functional_lines = []
    for req in functional:
        text = req.rstrip(".")
        functional_lines.append(f"- The system shall {text}.")
    if not functional_lines:
        functional_lines.append("- The system shall execute the documented capability when activated.")

    error_lines = []
    if non_functional:
        error_lines.extend([f"- If {entry.lower()}, the system shall return Error Code 503." for entry in non_functional[:2]])
    else:
        error_lines.append("- If the primary data service is unreachable, the system shall return Error Code 503.")

    if acceptance:
        error_lines.extend([f"- If {entry.lower()}, the system shall log the anomaly and notify operations." for entry in acceptance[:2]])

    section = [f"### 3.2.{index} {feature_name}"]
    section.append(f"#### 3.2.{index}.1 Description and Priority\n{description_block}")
    section.append("#### 3.2.{index}.2 Stimulus/Response Sequences")
    section.extend([line for line in stimulus_lines])
    section.append("#### 3.2.{index}.3 Functional Requirements")
    section.append("- Detailed Requirements:")
    section.extend(functional_lines)
    section.append("- Error Handling Requirements:")
    section.extend(error_lines)
    section.append("- Functional Decomposition Tree Note: Map this branch back to the tree node representing the feature category and ensure all child behaviors are traceable.")
    return "\n".join(section)


def replace_section(existing: str, new_section: str) -> str:
    marker = "# Section 3.2 – Feature Decomposition"
    if marker in existing:
        start = existing.index(marker)
        end = existing.find("\n# Section", start + len(marker))
        if end == -1:
            existing = existing[:start].rstrip() + "\n" + existing[end:].lstrip()
        else:
            existing = existing[:start].rstrip() + "\n" + existing[end:].lstrip()
    existing = existing.strip()
    if not existing:
        return new_section.strip() + "\n"
    section2_marker = "# Section 2.0"
    pos = existing.find(section2_marker)
    if pos == -1:
        return existing.rstrip() + "\n\n" + new_section.strip() + "\n"
    next_section = existing.find("\n# Section", pos + len(section2_marker))
    if next_section == -1:
        return existing.rstrip() + "\n\n" + new_section.strip() + "\n"
    return existing[:next_section].rstrip() + "\n\n" + new_section.strip() + "\n\n" + existing[next_section:].lstrip()


def main() -> None:
    try:
        features_text = read_file(FEATURES_FILE)
        quality_text = read_file(QUALITY_FILE)
    except FileNotFoundError as exc:
        print(exc)
        sys.exit(1)

    ensure_output_dir()
    feature_rows = parse_markdown_table(features_text)
    print(f"Parsed {len(feature_rows)} feature rows from {FEATURES_FILE.relative_to(PARENT_ROOT)}")
    sections = []
    counter = 0
    for row in feature_rows:
        name = row.get("Feature Name", "").strip()
        if not name:
            continue
        counter += 1
        sections.append(build_feature_section(counter, row, quality_text))
        print(f"Built subsection 3.2.{counter} for '{name}'")

    if not sections:
        print("No populated features found; aborting Section 3.2 generation.")
        return

    new_section = "# Section 3.2 – Feature Decomposition\n" + "\n\n".join(sections)
    existing_text = SRS_FILE.read_text(encoding="utf-8") if SRS_FILE.exists() else ""
    final = replace_section(existing_text, new_section)
    SRS_FILE.write_text(final.strip() + "\n", encoding="utf-8")
    print(f"Updated {SRS_FILE.relative_to(PARENT_ROOT)} with Section 3.2 containing {counter} features.")


if __name__ == "__main__":
    main()