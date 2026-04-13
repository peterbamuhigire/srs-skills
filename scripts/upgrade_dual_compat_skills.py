#!/usr/bin/env python3
"""Add a portable compatibility contract to every SKILL.md frontmatter.

This keeps the repository layout unchanged while giving Codex a predictable,
machine-readable skill shape that does not interfere with Claude Code's
existing body content.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_KEYS = [
    "use_when",
    "do_not_use_when",
    "required_inputs",
    "workflow",
    "quality_standards",
    "anti_patterns",
    "outputs",
    "references",
]


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def relative_skill_dir(skill_md: Path) -> Path:
    return skill_md.parent.relative_to(ROOT)


def infer_name(skill_md: Path) -> str:
    rel = relative_skill_dir(skill_md)
    if rel.name:
        return rel.name.lower()
    return "unknown-skill"


def infer_description(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    heading = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    if heading:
        title = heading.group(1).strip().rstrip(".")
        return f"Use when the task matches {title.lower()} and this skill's local workflow."
    return "Use when the task matches this skill's local workflow and repository context."


def list_support_assets(skill_dir: Path) -> str:
    candidates = []
    if (skill_dir / "references").is_dir():
        candidates.append("`references/`")
    if (skill_dir / "templates").is_dir():
        candidates.append("`templates/`")
    if (skill_dir / "protocols").is_dir():
        candidates.append("`protocols/`")
    if (skill_dir / "examples").is_dir():
        candidates.append("`examples/`")
    if (skill_dir / "documentation").is_dir():
        candidates.append("`documentation/`")
    if (skill_dir / "README.md").is_file():
        candidates.append("`README.md`")
    if (skill_dir / "logic.prompt").is_file():
        candidates.append("`logic.prompt`")
    if list(skill_dir.glob("*.py")):
        candidates.append("local scripts")
    if not candidates:
        candidates.append("sibling files in this directory")
    return ", ".join(candidates)


def family_defaults(skill_md: Path) -> dict[str, str]:
    rel = relative_skill_dir(skill_md)
    skill_dir = skill_md.parent
    support_assets = list_support_assets(skill_dir)
    description = infer_description(skill_md)

    if rel.parts and rel.parts[0] == "skills":
        return {
            "use_when": description,
            "do_not_use_when": (
                "Do not use when a narrower sibling skill is a better fit, or when "
                "the task does not need this skill's engineering judgment."
            ),
            "required_inputs": (
                "Provide the task goal, constraints, relevant code or documents, "
                "runtime or product context, and any domain-specific requirements."
            ),
            "workflow": (
                "Follow the ordered guidance, checklists, and decision rules in this "
                "file, then open deeper local references only when the task needs them."
            ),
            "quality_standards": (
                "Keep outputs concrete, technically defensible, and aligned with the "
                "standards, gates, and tradeoffs defined in this skill."
            ),
            "anti_patterns": (
                "Do not invent missing context, skip risk or validation gates, or "
                "replace task-specific execution logic with generic advice."
            ),
            "outputs": (
                "Produce the design, implementation guidance, review findings, plan, "
                "or code-oriented artifact this skill is meant to drive."
            ),
            "references": f"Use {support_assets} when deeper detail is needed.",
        }

    return {
        "use_when": description,
        "do_not_use_when": (
            "Do not use when a more specific upstream or downstream skill owns the "
            "task, or when the required project context has not been prepared."
        ),
        "required_inputs": (
            "Provide the target project or document, the relevant context files, "
            "scope constraints, and any domain or standards inputs referenced here."
        ),
        "workflow": (
            "Follow the ordered steps, review gates, and local generation logic in "
            "this file before consulting deeper support files as needed."
        ),
        "quality_standards": (
            "Keep outputs grounded in source context, traceable to stated standards, "
            "and specific enough to review or verify."
        ),
        "anti_patterns": (
            "Do not fabricate missing requirements, skip human review gates, or "
            "substitute vague prose for verifiable documentation."
        ),
        "outputs": (
            "Produce or update the document, scaffold, analysis, or phase artifact "
            "that this skill defines."
        ),
        "references": f"Use {support_assets} when deeper detail is needed.",
    }


def parse_frontmatter(text: str) -> tuple[str, str, str] | None:
    match = re.match(r"^(---\n)(.*?)(\n---\n?)", text, flags=re.DOTALL)
    if not match:
        return None
    return match.group(1), match.group(2), match.group(3)


def extract_simple_value(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", frontmatter)
    if not match:
        return None
    return match.group(1).strip()


def has_metadata_key(frontmatter: str, key: str) -> bool:
    return re.search(rf"(?m)^  {re.escape(key)}:", frontmatter) is not None


def ensure_frontmatter(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    parsed = parse_frontmatter(text)
    if parsed:
        return text

    name = infer_name(skill_md)
    description = infer_description(skill_md)
    frontmatter = (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "---\n\n"
    )
    return frontmatter + text.lstrip()


def inject_metadata(text: str, defaults: dict[str, str]) -> str:
    parsed = parse_frontmatter(text)
    if not parsed:
        raise ValueError("frontmatter expected before metadata injection")

    start, body, end = parsed
    lines = body.splitlines()

    if not any(line.strip() == "metadata:" for line in lines):
        lines.append("metadata:")

    for key in REQUIRED_KEYS:
        if has_metadata_key("\n".join(lines), key):
            continue
        lines.append(f"  {key}: {yaml_quote(defaults[key])}")

    new_frontmatter = "\n".join(lines)
    rest = text[len(start + body + end) :]
    return f"{start}{new_frontmatter}{end}{rest}"


def normalize_frontmatter_scalars(text: str) -> str:
    parsed = parse_frontmatter(text)
    if not parsed:
        return text

    start, body, end = parsed
    normalized = []
    for line in body.splitlines():
        if line.strip() == "metadata:":
            normalized.append(line)
            continue

        nested = re.match(r"^(  )([A-Za-z0-9_-]+):\s*(.*)$", line)
        if nested:
            indent, key, value = nested.groups()
            if value:
                normalized.append(f"{indent}{key}: {yaml_quote(value.strip().strip('\"'))}")
            else:
                normalized.append(line)
            continue

        top = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if top:
            key, value = top.groups()
            if key != "metadata" and value:
                normalized.append(f"{key}: {yaml_quote(value.strip().strip('\"'))}")
            else:
                normalized.append(line)
            continue

        normalized.append(line)

    rest = text[len(start + body + end) :]
    return f"{start}{'\n'.join(normalized)}{end}{rest}"


def upgrade_skill(skill_md: Path) -> bool:
    original = skill_md.read_text(encoding="utf-8", errors="ignore")
    ensured = ensure_frontmatter(skill_md)
    upgraded = inject_metadata(ensured, family_defaults(skill_md))
    upgraded = normalize_frontmatter_scalars(upgraded)
    if upgraded != original:
        skill_md.write_text(upgraded, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> int:
    changed = 0
    for skill_md in sorted(ROOT.rglob("SKILL.md")):
        if upgrade_skill(skill_md):
            changed += 1
    print(f"Updated {changed} SKILL.md files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
