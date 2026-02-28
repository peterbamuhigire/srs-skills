# 02-Low-Level-Design Skill

## Objective

This skill produces a Low-Level Design document that decomposes high-level architectural components into implementable modules with class diagrams, sequence diagrams, state machines, and formalized algorithms. It bridges the gap between architectural intent (HLD) and code-level implementation per IEEE 1016-2009 Sec 6.

## Execution Steps

1. Verify `../output/HLD.md`, `../output/SRS_Draft.md`, and `../project_context/business_rules.md` exist. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill decomposes HLD components, generates Mermaid diagrams, formalizes algorithms, and writes `../output/LLD.md`.
3. Review class diagrams for typed attributes and parameterized methods, sequence diagrams for error-path coverage, and state machines for terminal-state completeness.
4. Proceed to `03-api-specification` to define API contracts from module interfaces, or to `04-database-design` to derive schemas from entity models.

## Quality Reminder

Every class diagram shall use precise data types including `DECIMAL(19,4)` for monetary values. Every sequence diagram shall include at least one error path alongside the happy path. Every state machine shall account for all terminal states with explicit transition guards. Every algorithm shall handle edge cases including null inputs, empty collections, division by zero, and boundary values. Flag gaps rather than fabricating design decisions.

## Standards

- IEEE 1016-2009 Sec 6 (Software Design Descriptions)
- ISO/IEC 25010 (Software Quality Models)
- ISO/IEC 25062 (Data Validation Documentation)
