# Architecture Overview

SRS-Skills uses `projects/<ProjectName>/` as the canonical runtime workspace. The project context source of truth is `projects/<ProjectName>/_context/`, while generated artifacts live under the appropriate phase/document directories inside the same project workspace.

For backward compatibility, many existing skill-local instructions still refer to `../project_context/` and `../output/`. Those relative paths are execution aliases into the active project workspace, not a separate architectural model.

The repository is arranged as a linear pipeline of independent skill modules (01-08). Each skill encapsulates:

1. **Input Context:** Reads specific project context files from the active workspace, canonically `projects/<ProjectName>/_context/*.md` (vision, features, tech stack, quality standards, etc.).
2. **Logic Core:** Executes a Python script (or LLM prompt) designed for a particular IEEE section.
3. **Output Target:** Writes or rewrites generated artifacts in the active project workspace, commonly through skill-local `../output/...` aliases.

The `skills/` directory stores utility skills, such as `update-documentation`, that coordinate documentation upkeep when the pipeline changes. This architecture enforces separation of concerns (introduction, interfaces, behavior, logic, attributes, and validation) while ensuring each phase consumes only the data projected by previous phases.
