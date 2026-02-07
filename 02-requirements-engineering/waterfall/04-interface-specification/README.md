# 04-Interface-Specification Skill

## Objective

This skill produces Section 3.1 (Interface Specification) of the SRS by scanning `tech_stack.md`, `features.md`, and `quality_standards.md` to expose every interface, protocol, and actor required for integration. It moves the project from descriptive context into a detailed connectivity map.

## Execution Steps

1. Run `python interface_specification.py` from this directory. The script reads the three context files, identifies external actors, validates protocol compatibility (e.g., OCI APIs, MySQL ports), and writes Section 3.1 into `../output/SRS_Draft.md`.
2. The output contains subsections for User Interfaces, Hardware Interfaces, Software Interfaces, and Communications Interfaces. Each subsection adheres to the ISO/IEEE mandates (ISO/IEC 25062 input validation, ISO/IEC 25010 Usability) and avoids vague adjectives.
3. The Hardware Interfaces subsection uses a Markdown table to describe device pinouts or connectivity requirements when available. The Communications section describes the connectivity map, network stack (IEEE 802.11ax, TLS 1.3), and port allocations.
4. Confirm that Section 3.1 in `SRS_Draft.md` aligns with the previously generated Sections 1.0 and 2.0 before moving on to the core logic skills.

## Quality Note

Maintain direct, technical prose. Each statement SHALL reference actual hardware, software, or protocol definitions. This is the final step before defining the logic model, so the interfaces must be precise and traceable.
