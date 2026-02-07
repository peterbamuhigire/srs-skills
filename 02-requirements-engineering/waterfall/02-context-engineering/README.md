# 02-Context-Engineering Skill

## Objective

This skill synthesizes the introduction (Section 1.0) of the SRS by transforming `vision.md` and `glossary.md` into a high-density introduction that respects IEEE 830 and ISO/IEC conventions. It captures the difference between the software purpose and the SRS purpose, defines scope with traceability to stakeholder needs, renders standardized definitions, lists the governing standards, and delivers a roadmap for the remainder of the document.

## Execution Steps

1. Run `python context_engineering.py` from this directory. The script reads `../project_context/vision.md` and `../project_context/glossary.md`, then writes a standardized `SRS_Draft.md` in `../output/` that contains Section 1.0.
2. The script follows the Standardized Document Header format for Section 1.0, ensuring the introduction looks like an engineered artifact rather than conversational prose.
3. The output lists Purpose, Scope, Definitions, References, and Overview subsections, reusing ISS/IEEE definitions and linking every scope item to the Stakeholder Needs matrix.
4. Review `../output/SRS_Draft.md` after running the skill to confirm all scope items and definitions meet the traceability and ISO/IEC requirements.

## Quality Commitment

Keep tone direct and active. Each generated sentence SHALL connect back to project intent, scope, or traceability sources. Use the script output as a foundation before populating Sections 2.0+.
