---
name: logic-modeling
description: Capture Section 3.2.2, 3.2.3, and 3.2.4 by transforming business rules, the technology stack, and quality standards into transition-aware logic and data constructs.
---

# Logic Modeling Skill Guidance

## Overview
Use this skill after Sections 1.0–3.1 exist. It reads `business_rules.md`, `tech_stack.md`, and `quality_standards.md` to produce the logical and mathematical foundations required by IEEE 1016 before moving on to validation, traceability, or testing chapters.

## Quick Reference
- Inputs: `../project_context/business_rules.md`, `../project_context/tech_stack.md`, `../project_context/quality_standards.md`
- Output: `../output/SRS_Draft.md` (Sections 3.2.2–3.2.4)
- Tone: Precise, formal, transition-model oriented. Use IF-THEN-ELSE prose where logic branches exist, and avoid subjective adjectives.

## Core Instructions
1. Run `python logic_modeling.py` from this directory or trigger the `logic.prompt`; the script logs each read and writes only the logic sections without deleting previously authored content.
2. Confirm the technology stack contains either MySQL or PostgreSQL so the script can assign `DECIMAL(19,4)` or `NUMERIC(19,4)` types, respectively. Document this dialect choice in the log output.
3. Each process description must list Input, Algorithm (with structured IF-THEN-ELSE paths), and Affected Entities, mention the ISO/IEC 25010 reliability and analysability targets, and enclose calculations in LaTeX.
4. The Data Construct Specifications section describes each record type that supports the Transition Models, and the Data Dictionary tabulates every field with its representation, units/format, and range/accuracy.
5. Track precision behavior explicitly: any monetary or derived numeric value shall be described with the phrase “The system shall round the result to the nearest 2 decimal places using the 'Round Half Up' method.”

## Resources
- `README.md`: Intent, steps, and quality reminders for this skill.
- `logic_modeling.py`: The automation that builds the logic model sections from business rules and technology stack files.
- `logic.prompt`: LLM instructions that enforce reliability/analysability checks, LaTeX formulas, and transition-model thinking.