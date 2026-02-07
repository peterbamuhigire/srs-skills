---
name: interface-specification
description: Define Section 3.1 by mapping tech_stack.md and features.md into detailed user, hardware, software, and communications interfaces that cite ISO/IEEE requirements.
---

# Interface Specification Skill Guidance

## Overview
Use this skill after Sections 1.0 and 2.0 are generated. It analyzes the technology stack, feature set, and quality standards to produce Section 3.1 (Interface Specification), ensuring the project transitions from descriptive modeling to explicit connectivity requirements.

## Quick Reference
- Inputs: `../project_context/tech_stack.md`, `../project_context/features.md`, `../project_context/quality_standards.md`
- Output: `../output/SRS_Draft.md` (Section 3.1 only)
- Tone: Technical, precise, employing SHALL statements; avoid subjective adjectives and mention standards such as ISO/IEC 25010 and ISO/IEC 25062.

## Core Instructions
1. Run `python interface_specification.py` from this directory or invoke the `logic.prompt` through your skill runner.
2. Detect infrastructure keywords (Ubuntu, OCI, MySQL, HP Z440, etc.), extract external actors from feature user stories, and log all parsing steps.
3. Write Section 3.1 with subsections 3.1.1–3.1.4. Include Markdown tables for hardware and software interfaces when applicable, list ports/protocols explicitly (e.g., 443/TLS 1.3, 3306, 5432, IEEE 802.11ax, RFC 7519 JWT), and describe the communication stack connectivity map.
4. Confirm Section 3.1 references ISO/IEC 25062 input validation and ISO/IEC 25010 usability, and mention ISO/IEC 25051 Ready-to-Use expectations if needed.
5. Validate that the updated `SRS_Draft.md` retains Sections 1.0 and 2.0 content while replacing or appending Section 3.1.

## Resources
- `README.md`: Explains the intent and quality expectation for this skill.
- `interface_specification.py`: Automation script that performs detection, grouping, and writing of Section 3.1.
- `logic.prompt`: Provides meta instructions for Claude to orchestrate the process.
