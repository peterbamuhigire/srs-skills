"""Create Sections 3.2.2-3.2.4 of the SRS by modeling business rules and data constructs."""

from pathlib import Path
import re
import sys

MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
PROJECT_CONTEXT = PARENT_ROOT / "project_context"
OUTPUT_DIR = PARENT_ROOT / "output"
SRS_FILE = OUTPUT_DIR / "SRS_Draft.md"
BUSINESS_RULES_FILE = PROJECT_CONTEXT / "business_rules.md"
TECH_STACK_FILE = PROJECT_CONTEXT / "tech_stack.md"
QUALITY_FILE = PROJECT_CONTEXT / "quality_standards.md"


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


def parse_list_items(section_text: str) -> list[str]:
    return [line.strip()[2:].strip() for line in section_text.splitlines() if line.strip().startswith("- ")]


def extract_section(text: str, header_keyword: str) -> str:
    section_lines: list[str] = []
    capture = False
    keyword_lower = header_keyword.lower()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and keyword_lower in stripped.lower():
            capture = True
            continue
        if capture and stripped.startswith("#") and keyword_lower not in stripped.lower():
            break
        if capture:
            section_lines.append(line)
    return "\n".join(section_lines).strip()


def extract_condition_action(text: str) -> tuple[str, str]:
    condition = ""
    action = ""
    if match := re.search(r"(?:if|when)\s+(.+?)(?:,|then|$)", text, flags=re.I):
        condition = match.group(1).strip()
    if match := re.search(r"(?:then|->|⇒)\s*(.+)", text, flags=re.I):
        action = match.group(1).strip()
    return condition, action


def parse_decision_points(section_text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    table_rows = parse_markdown_table(section_text)
    for row in table_rows:
        name = row.get("Decision Point") or row.get("Decision") or row.get("Name") or row.get("Process") or "Decision"
        trigger = (row.get("Trigger") or row.get("Condition") or row.get("Input") or row.get("When") or "").strip()
        action = (row.get("Action") or row.get("Outcome") or row.get("Response") or "").strip()
        notes = row.get("Notes") or row.get("Description") or ""
        affected = row.get("Affected Entities") or row.get("Entities") or ""
        condition, act = extract_condition_action(notes)
        trigger = trigger or condition or notes or "Documented decision trigger"
        action = action or act or notes or "Engage the documented response"
        entities = [entity.strip() for entity in affected.split(",") if entity.strip()]
        entries.append({
            "name": name.strip(),
            "trigger": trigger,
            "action": action,
            "notes": notes.strip(),
            "entities": entities,
        })
    for item in parse_list_items(section_text):
        if not item:
            continue
        name, rest = (item.split(":", 1) + [""])[:2]
        trigger, action = extract_condition_action(rest or item)
        entries.append({
            "name": name.strip() or "Decision",
            "trigger": trigger or rest or "Documented decision trigger",
            "action": action or rest or "Engage the documented response",
            "notes": rest.strip(),
            "entities": [],
        })
    return entries


def parse_calculations(section_text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    table_rows = parse_markdown_table(section_text)
    for row in table_rows:
        name = row.get("Calculation") or row.get("Formula Name") or row.get("Name") or row.get("Process") or "Calculation"
        description = row.get("Description") or row.get("Detail") or ""
        formula = row.get("Formula") or row.get("Expression") or row.get("Equation") or ""
        if not formula and (match := re.search(r"=[^\n]+", row.get("Notes", ""))):
            formula = match.group(0).lstrip("=").strip()
        triggered_by = row.get("Trigger") or description or row.get("Input") or "Scheduled execution"
        entries.append({
            "name": name.strip(),
            "trigger": triggered_by.strip(),
            "action": description or "Produce the required numeric output",
            "formula": formula.strip(),
            "notes": description.strip(),
            "entities": [],
        })
    for item in parse_list_items(section_text):
        if not item:
            continue
        if "=" in item:
            name_part, formula_part = item.split("=", 1)
            name = name_part.strip()
            formula = formula_part.strip()
        else:
            name = item
            formula = ""
        entries.append({
            "name": name.strip() or "Calculation",
            "trigger": "Referenced by business rule",
            "action": "Compute the documented value",
            "formula": formula,
            "notes": item,
            "entities": [],
        })
    return entries


def latex_wrap(expression: str) -> str:
    cleaned = expression.strip()
    if not cleaned:
        return ""
    cleaned = cleaned.replace("sum(", "\\sum(").replace("Sum(", "\\sum(")
    cleaned = cleaned.replace(" * ", " \\times ")
    cleaned = cleaned.replace("*", " \\times ")
    cleaned = cleaned.replace(" / ", " \\div ")
    cleaned = cleaned.replace("=", " = ")
    cleaned = re.sub(r"\s+", " ", cleaned)
    if cleaned.startswith("$$") and cleaned.endswith("$$"):
        return cleaned
    return f"$$ {cleaned.strip()} $$"


def deduce_database(tech_text: str) -> str:
    lowered = tech_text.lower()
    if "postgresql" in lowered:
        return "PostgreSQL"
    if "mysql" in lowered:
        return "MySQL"
    return "MySQL"


def find_metric(rows: list[dict[str, str]], characteristic: str) -> str:
    for row in rows:
        key = row.get("Characteristic", "").strip().lower()
        if key == characteristic.lower():
            return row.get("Measurement & Target") or row.get("Description") or ""
    return ""


def detect_entities(text: str) -> set[str]:
    matches = set(re.findall(r"\b[A-Z][a-zA-Z]+(?:Record|Session|Entity|Account|Profile|Event|Payment)\b", text))
    if not matches:
        matches.update({"TenantRecord", "TutorSession", "PaymentEvent"})
    return matches


def data_type(kind: str, db_choice: str) -> str:
    mysql_types = {
        "uuid": "CHAR(36)",
        "currency": "DECIMAL(19,4)",
        "text": "VARCHAR(255)",
        "enum": "ENUM('Scheduled','InProgress','Completed','Cancelled')",
        "timestamp": "TIMESTAMP",
        "integer": "INT",
    }
    postgres_types = {
        "uuid": "UUID",
        "currency": "NUMERIC(19,4)",
        "text": "VARCHAR(255)",
        "enum": "TEXT CHECK (status IN ('Scheduled','InProgress','Completed','Cancelled'))",
        "timestamp": "TIMESTAMP WITH TIME ZONE",
        "integer": "INTEGER",
    }
    pool = postgres_types if db_choice.lower() == "postgresql" else mysql_types
    return pool.get(kind.lower(), "VARCHAR(255)")


def build_fields_for_entity(entity: str, db_choice: str) -> list[tuple[str, str, str, str]]:
    lower = entity.lower()
    if "tenant" in lower:
        return [
            ("tenant_id", data_type("uuid", db_choice), "UUID string", "Primary key; non-null."),
            ("name", data_type("text", db_choice), "UTF-8 string", "Non-empty; maximal 255 chars."),
            ("subscription_level", data_type("text", db_choice), "UTF-8 string", "Enum: Free, Standard, Premium."),
            ("account_balance", data_type("currency", db_choice), "UGX currency", ">= 0.00; two-decimal precision."),
            ("created_at", data_type("timestamp", db_choice), "UTC timestamp", "Captured to the second."),
        ]
    if "session" in lower:
        return [
            ("session_id", data_type("uuid", db_choice), "UUID string", "Primary key; non-null."),
            ("tenant_id", data_type("uuid", db_choice), "UUID string", "Foreign key to TenantRecord."),
            ("tutor_id", data_type("uuid", db_choice), "UUID string", "Foreign key to TutorRecord."),
            ("start_time", data_type("timestamp", db_choice), "UTC timestamp", ">= current time; second precision."),
            ("end_time", data_type("timestamp", db_choice), "UTC timestamp", ">= start_time; second precision."),
            ("status", data_type("enum", db_choice), "Enumerated token", "Scheduled, InProgress, Completed, Cancelled."),
            ("fee_amount", data_type("currency", db_choice), "UGX currency", "> 0.00; Round Half Up to two decimals."),
        ]
    if "payment" in lower or "invoice" in lower or "order" in lower:
        return [
            ("payment_id", data_type("uuid", db_choice), "UUID string", "Primary key; audit trail."),
            ("tenant_id", data_type("uuid", db_choice), "UUID string", "Linked tenant record."),
            ("amount", data_type("currency", db_choice), "UGX currency", "> 0.00; Round Half Up."),
            ("created_at", data_type("timestamp", db_choice), "UTC timestamp", "Captured to the second."),
            ("status", data_type("text", db_choice), "UTF-8 string", "Pending, Completed, Failed."),
        ]
    return [
        ("record_id", data_type("uuid", db_choice), "UUID string", "Primary key."),
        ("description", data_type("text", db_choice), "UTF-8 string", "250-character summary."),
        ("created_at", data_type("timestamp", db_choice), "UTC timestamp", "Captured to the second."),
    ]


def build_process_section(processes: list[dict[str, str]], reliability: str, analysability: str, entity_pool: list[str]) -> str:
    lines: list[str] = ["### 3.2.2 Process Descriptions"]
    reliability_note = reliability or "Reliability target not specified in quality standards."
    analysability_note = analysability or "Analysability metric absent; default to modular trace logs."
    lines.append(
        f"Per ISO/IEC 25010 reliability ({reliability_note}) and analysability ({analysability_note}), each Transition Model below details input, algorithm, and affected entities."
    )
    for index, process in enumerate(processes, start=1):
        cond = process.get("trigger", "Documented trigger state.")
        action = process.get("action", "Execute the documented response.")
        condition_clause = cond if cond.endswith(".") else cond + "."
        action_clause = action if action.endswith(".") else action + "."
        entity_list = process.get("entities") or entity_pool
        entity_text = ", ".join(entity_list) if entity_list else "Operations, data services, and monitoring actors"
        lines.append(f"#### 3.2.2.{index} {process.get('name', 'Unnamed Process')}")
        lines.append(f"- Input: {condition_clause}")
        lines.append("- Algorithm:")
        lines.append(f"  1. Establish the current state defined by the trigger; honor the documented inputs so reliability remains visible.")
        lines.append(f"  2. IF {condition_clause} THEN {action_clause} ELSE escalate to operations with contextual logs for analysability.")
        if process.get("formula"):
            formula_text = latex_wrap(process["formula"])
            if formula_text:
                lines.append(
                    f"  3. The system shall evaluate the expression {formula_text} and round the result to the nearest 2 decimal places using the 'Round Half Up' method."
                )
            else:
                lines.append("  3. The system shall persist the computed outcome with Round Half Up precision for downstream verification.")
        else:
            lines.append("  3. The system shall record the executed branch so analysts can reproduce the Transition Model pathway.")
        lines.append(f"- Affected Entities: {entity_text}")
        lines.append("- Transition Model Note: This logic represents a state transition that feeds the next decision or calculation while staying aligned with reliability and analysability expectations.")
    return "\n".join(lines)


def build_construct_section(record_specs: list[dict[str, list[str] | str]], reliability: str, analysability: str) -> str:
    lines = ["### 3.2.3 Data Construct Specifications"]
    reliability_note = reliability or "Reliability target pending."
    analysability_note = analysability or "Analysability metric pending."
    lines.append(
        f"Reliability ({reliability_note}) and analysability ({analysability_note}) information requirements drive these constructs; each record keeps trace logs and well-documented fields."
    )
    for spec in record_specs:
        lines.append(f"- **{spec['name']}**: {spec['description']}")
        lines.append(f"  - Core fields: {', '.join(spec['fields'])}.")
        lines.append("  - Structural note: The record is part of the data layer in the Transition Models described in 3.2.2.")
    return "\n".join(lines)


def build_data_dictionary_section(dictionary_rows: list[dict[str, str]]) -> str:
    lines = [
        "### 3.2.4 Data Dictionary",
        "Below is the field-level data dictionary tied to the constructs described above.",
        "| Name | Representation | Units/Format | Range/Accuracy |",
        "| ---- | -------------- | ------------ | -------------- |",
    ]
    for row in dictionary_rows:
        lines.append(
            f"| {row['Name']} | {row['Representation']} | {row['Units/Format']} | {row['Range/Accuracy']} |"
        )
    return "\n".join(lines)


def remove_existing_logic_subsections(section_text: str) -> str:
    sanitized = section_text
    for header in [
        "### 3.2.2 Process Descriptions",
        "### 3.2.3 Data Construct Specifications",
        "### 3.2.4 Data Dictionary",
    ]:
        pattern = rf"{re.escape(header)}[\s\S]*?(?=(###\s+3\.2\.\d|#\s+Section|$))"
        sanitized = re.sub(pattern, "", sanitized)
    return sanitized.rstrip()


def insert_logic_sections(existing_text: str, logic_block: str) -> str:
    marker = "# Section 3.2 – Feature Decomposition"
    if marker not in existing_text:
        existing_text = existing_text.strip()
        if existing_text:
            existing_text += "\n\n"
        existing_text += marker + "\n\n"
    start = existing_text.index(marker)
    next_section = existing_text.find("\n# Section", start + len(marker))
    if next_section == -1:
        section_body = existing_text[start:]
        after = ""
    else:
        section_body = existing_text[start:next_section]
        after = existing_text[next_section:]
    sanitized_section = remove_existing_logic_subsections(section_body)
    combined_section = sanitized_section.rstrip() + "\n\n" + logic_block.strip() + "\n"
    return existing_text[:start] + combined_section + after


def main() -> None:
    try:
        business_text = read_file(BUSINESS_RULES_FILE)
        tech_text = read_file(TECH_STACK_FILE)
        quality_text = read_file(QUALITY_FILE)
    except FileNotFoundError as exc:
        print(exc)
        sys.exit(1)

    ensure_output_dir()
    db_choice = deduce_database(tech_text)
    print(f"Detected primary database platform: {db_choice}")

    quality_rows = parse_markdown_table(quality_text)
    reliability_metric = find_metric(quality_rows, "Reliability")
    analysability_metric = find_metric(quality_rows, "Analysability") or find_metric(quality_rows, "Maintainability")

    decision_section = extract_section(business_text, "Decision Points")
    calculation_section = extract_section(business_text, "Calculations")
    decision_points = parse_decision_points(decision_section)
    calculations = parse_calculations(calculation_section)

    processes: list[dict[str, str]] = []
    for entry in decision_points:
        entry["type"] = "Decision"
        processes.append(entry)
    for entry in calculations:
        entry["type"] = "Calculation"
        processes.append(entry)

    if not processes:
        processes.append({
            "name": "Default Business Decision",
            "trigger": "A documented business rule requires evaluation.",
            "action": "Route the action through the fallback workflow.",
            "entities": ["Operations", "Monitoring"],
        })

    entity_pool = sorted(detect_entities(business_text) | {"TenantRecord", "TutorSession", "PaymentEvent"})

    record_specs: list[dict[str, list[str] | str]] = []
    data_dictionary: list[dict[str, str]] = []
    for entity in entity_pool:
        fields = build_fields_for_entity(entity, db_choice)
        if not fields:
            continue
        description = (
            "Captures identity, accounting, and control data for the listed entity." if "record" in entity.lower() else
            "Represents the lifecycle of the entity as it flows through processes."
        )
        record_specs.append({
            "name": entity,
            "description": description,
            "fields": [field[0] for field in fields],
        })
        for field_name, rep, units, accuracy in fields:
            data_dictionary.append(
                {
                    "Name": f"{entity}.{field_name}",
                    "Representation": rep,
                    "Units/Format": units,
                    "Range/Accuracy": accuracy,
                }
            )

    process_block = build_process_section(processes, reliability_metric, analysability_metric, entity_pool)
    construct_block = build_construct_section(record_specs, reliability_metric, analysability_metric)
    dictionary_block = build_data_dictionary_section(data_dictionary)
    logic_block = "\n\n".join([process_block, construct_block, dictionary_block])

    existing_text = SRS_FILE.read_text(encoding="utf-8") if SRS_FILE.exists() else ""
    final_text = insert_logic_sections(existing_text, logic_block)
    SRS_FILE.write_text(final_text.strip() + "\n", encoding="utf-8")
    print(
        f"Updated {SRS_FILE.relative_to(PARENT_ROOT)} with logic-modeling content (Processes: {len(processes)}, Records: {len(record_specs)})."
    )


if __name__ == "__main__":
    main()