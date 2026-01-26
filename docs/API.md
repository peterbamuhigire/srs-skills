# API Summary

SRS-Skills does not expose a runtime API; instead, each skill is executed by running its dedicated Python script (e.g., `python 05-feature-decomposition/feature_decomposition.py`) or triggering the associated `logic.prompt`. Users integrate the skills into their IDE or CI/CD pipeline by invoking the scripts from within the submodule so the automation can target the parent project via `../project_context/` and `../output/`.
