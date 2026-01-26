# SRS-Skills Technology Stack

- **Primary Language:** Python 3.11 (scripts under each skill directory). All automation leverages the standard library plus Markdown parsing utilities.
- **Execution Environment:** Skills run inside the Git submodule and operate on adjacent `../project_context/` and `../output/` folders. No external services or databases are required.
- **Documentation Flow:** Each skill emits Markdown into `../output/SRS_Draft.md`, with `08-semantic-auditing` adding `Audit_Report.md` for traceability.
- **Helper Skills:** The `skills/` subtree contains meta skills such as `update-documentation` for coordinating doc refreshes when significant work occurs.
