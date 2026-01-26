# Architecture Overview

SRS-Skills is arranged as a linear pipeline of independent skill modules (01-08). Each skill encapsulates:

1. **Input Context:** Reads specific `../project_context/*.md` files (vision, features, tech stack, quality standards, etc.).
2. **Logic Core:** Executes a Python script (or LLM prompt) designed for a particular IEEE section.
3. **Output Target:** Writes or rewrites a dedicated section inside `../output/SRS_Draft.md` or generates auxiliary artifacts (e.g., `Audit_Report.md`).

The `skills/` directory stores utility skills, such as `update-documentation`, that coordinate documentation upkeep when the pipeline changes. This architecture enforces separation of concerns (introduction, interfaces, behavior, logic, attributes, and validation) while ensuring each phase consumes only the data projected by previous phases.
