# Contextual Inquiry and Task Analysis

## Purpose

This reference provides a structured approach to requirements elicitation through direct observation of users in their work environment. Observation captures tacit knowledge, workarounds, and pain points that stakeholders may not articulate in interviews because they have become habitual or invisible.

## Reference Standard

- IEEE 29148-2018 Section 6.3: Elicitation through observation
- Wiegers Practice 5: Contextual inquiry
- Beyer & Holtzblatt: Contextual Design (1997)

## When to Use Observation

| Condition | Suitability |
|-----------|-------------|
| Replacing or modernizing an existing system | Excellent |
| Complex manual workflows with many steps | Excellent |
| Stakeholders say "it's hard to explain, let me show you" | Excellent |
| No existing system or process to observe | Poor |
| Remote stakeholders who cannot be visited | Limited (screen sharing) |

## Observation Checklist

### Pre-Observation Preparation

- [ ] Identify the process or workflow to observe from `features.md`
- [ ] Select observation targets from the stakeholder register (primary/secondary users)
- [ ] Obtain permission from the stakeholder and their manager
- [ ] Define observation duration (typically 1-4 hours per session)
- [ ] Prepare observation recording sheet (template below)
- [ ] Confirm whether photography, screen recording, or audio recording is permitted
- [ ] Review any existing process documentation for baseline context

### During Observation

- [ ] Arrive before the stakeholder begins the target workflow
- [ ] Observe silently for the first 15 minutes (do not interrupt)
- [ ] Record each task step, including substeps and decision points
- [ ] Note timestamps for each major step (for duration analysis)
- [ ] Mark error-prone steps where the user hesitates, backtracks, or makes mistakes
- [ ] Identify workarounds: unofficial tools, manual calculations, sticky notes, spreadsheets
- [ ] Note environmental factors: interruptions, noise, multi-tasking
- [ ] Ask clarifying questions only during natural pauses in the workflow

### Post-Observation

- [ ] Review notes within 4 hours while memory is fresh
- [ ] Validate observations with the stakeholder ("Did I capture this correctly?")
- [ ] Classify findings by type (requirement, constraint, pain point, workaround)
- [ ] Cross-reference with interview findings for consistency

## Workflow Documentation Template

For each observed workflow:

```
### Observed Workflow: [Process Name]

**Observer**: [Name/Role]
**Stakeholder**: SH-XXX -- [Role]
**Date**: [Date]
**Duration**: [Total observation time]
**Location**: [Physical or virtual workspace]

#### Task Steps

| Step | Action | Actor | Duration | Tools Used | Notes |
|------|--------|-------|----------|------------|-------|
| 1 | [Description] | [Role] | [mm:ss] | [System/Tool] | |
| 2 | [Description] | [Role] | [mm:ss] | [System/Tool] | |
| 3 | [Description] | [Role] | [mm:ss] | [System/Tool] | [Error-prone] |
| ... | ... | ... | ... | ... | ... |

#### Decision Points

| Decision | Options | Criteria | Frequency |
|----------|---------|----------|-----------|
| [Decision description] | [Option A, Option B] | [How the user decides] | [How often this occurs] |

#### Pain Points Identified

| # | Pain Point | Impact | Current Workaround | Frequency |
|---|------------|--------|--------------------|-----------|
| 1 | [Description] | [Time lost, errors, frustration] | [How user copes] | [Daily/Weekly/etc.] |
| 2 | [Description] | [Impact] | [Workaround] | [Frequency] |

#### Workarounds Documented

| # | Workaround | Purpose | Risk | Replacement Opportunity |
|---|------------|---------|------|------------------------|
| 1 | [Description] | [Why the user does this] | [What could go wrong] | [System feature to replace] |
```

## Finding Recording Format

For each finding derived from observation:

```
#### EL-XXX: [Finding Title]

- **Source**: SH-XXX -- [Role] (Observation)
- **Technique**: Observation / Contextual Inquiry
- **Workflow**: [Process name observed]
- **Task Step**: [Step number where finding emerged]
- **Observation**: "[What was observed]"
- **Derived Requirement**: The system shall [requirement].
- **Type**: Functional | Non-Functional | Constraint
- **Confidence**: Confirmed | Likely | Uncertain
- **Pain Point Addressed**: [Yes/No -- reference pain point #]
```

## Task Analysis Decomposition

For complex tasks, decompose into a hierarchical task analysis:

```
Task: [Top-level task name]
  1. [Subtask 1]
    1.1 [Action]
    1.2 [Action]
    1.3 [Decision: If X, go to 1.4; else go to 1.5]
    1.4 [Action]
    1.5 [Action]
  2. [Subtask 2]
    2.1 [Action]
    2.2 [Action]
  3. [Subtask 3]
    ...
Plan: Do 1, then 2, then 3. Within 1, do 1.1, 1.2, then decide.
```

## Observation Ethics

- Always obtain informed consent before observing
- Do not observe without the stakeholder's knowledge
- Do not record personal conversations or non-work activities
- Share observation notes with the stakeholder for validation
- Anonymize findings when reporting to broader audiences if requested
- Do not use observations to evaluate employee performance

## Anti-Patterns to Avoid

| Anti-Pattern | Description | Correction |
|--------------|-------------|------------|
| Hawthorne Effect | Stakeholder changes behavior because they know they are being observed | Observe over multiple sessions to normalize |
| Interpretation Bias | Recording what you expect to see rather than what actually happens | Record objectively; validate with stakeholder |
| Interrupting | Asking questions during critical workflow moments | Wait for natural pauses |
| Single Session | Drawing conclusions from one observation period | Observe the same workflow at least twice |
| Ignoring Environment | Focusing only on the screen/tool, not the physical/social context | Note interruptions, collaboration, and workspace factors |
