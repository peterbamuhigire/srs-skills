# 06-Logic-Modeling Skill

## Objective

This skill builds the logical core of the SRS by translating `business_rules.md` and `tech_stack.md` into Sections 3.2.2 through 3.2.4, aligning with IEEE 1016 (Software Design Description) expectations. It enforces transition-model thinking, supplies the mathematical definitions, and locks data constructs into measurable metrics.

## Execution Steps

1. Run `python logic_modeling.py` from this directory. The script reads `../project_context/business_rules.md`, `../project_context/tech_stack.md`, and `../project_context/quality_standards.md`, decides whether MySQL or PostgreSQL is the primary store, and writes Sections 3.2.2 (Process Descriptions), 3.2.3 (Data Construct Specifications), and 3.2.4 (Data Dictionary) into `../output/SRS_Draft.md` without disturbing earlier sections.
2. Confirm that each process description uses a Transition Model narrative (input, algorithm with IF-THEN-ELSE, affected entities) and references the ISO/IEC 25010 reliability and analysability targets before moving on to interface or validation skills.
3. Review the data dictionary output and verify each field uses the database-specific representation (e.g., `DECIMAL(19,4)` for MySQL, `NUMERIC(19,4)` for PostgreSQL) that the script inferred from `tech_stack.md`.

## Engineering Rigor: The Logic Blueprint

- All formulas in the Logic Modeling skill are rendered in LaTeX (e.g., `$$Total = \sum (price \times tax)$$`).
- Precision expectations are enforced explicitly; every numerical result statement ends with "The system shall round the result to the nearest 2 decimal places using the 'Round Half Up' method." when currency or calculated totals are involved.
- Transition Models tie reliability to analysability: states, triggers, and outcomes are described so the logic layer keeps the system observable and diagnosable.
- The resulting documentation satisfies IEEE 1016 by documenting process flows, data constructs, and a data dictionary with measurable ranges and representations.

## Quality Reminder

Maintain direct, non-promotional prose. Log the files read and the sections overwritten. Avoid AI filler such as "intelligent" or "user-friendly". The quality of the SRS depends on the precision of these logic constructs—painstaking human quality matters.
