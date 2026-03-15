# Book Analysis: Software Maintenance Concepts and Practice — Grubb & Takang (2nd Ed.)
**Analyzed:** 2026-03-15
**Feeds:** W-15 (SMP skill), W-16 (Post-Deployment Evaluation Report skill)

---

## Key Numbers

- Maintenance = **40–75%** of total software lifecycle cost (multiple empirical studies)
- Type distribution (Lientz/Swanson, n=487 orgs): Corrective 20% | Adaptive 25% | Perfective 50% | Preventive 5%
- Grubb & Takang use the **four-type** taxonomy (no "additive"); ISO 14764:2022 adds a fifth type

---

## Four Maintenance Types (Grubb & Takang)

| Type | Definition |
|------|------------|
| Corrective | Modification initiated by defects (design errors, logic errors, coding errors) |
| Adaptive | Change driven by modifications in the software's environment (OS, hardware, business rules, govt policy) |
| Perfective | Changes to expand existing requirements; enhancements or improvements in efficiency |
| Preventive | Changes to prevent future malfunctions or improve maintainability |

**Note:** ISO 14764:2022 adds "Additive" (new capability without specific user request). SMP skill should use the ISO five-type taxonomy; note this book uses four types.

---

## Lehman's Laws (All Eight)

| Law | Year | Statement |
|-----|------|-----------|
| I. Continuing Change | 1974 | Systems must be continually adapted or become progressively less satisfactory |
| II. Increasing Complexity | 1974 | As a system evolves, its complexity increases unless work is done to reduce it |
| III. Self-Regulation | 1974 | Evolutionary process aspects display statistical regularity |
| IV. Conservation of Organisational Stability | 1978 | Average work rate tends to remain constant over periods of evolution |
| V. Conservation of Familiarity | 1978 | Average incremental growth tends to remain constant or decline |
| VI. Continuing Growth | 1991 | Functional capability must be continually increased to maintain user satisfaction |
| VII. Declining Quality | 1996 | Unless rigorously adapted, system quality will appear to decline |
| VIII. Feedback Systems | 1996 | Evolution processes are multi-level, multi-loop, multi-agent feedback systems |

Laws I and VII are the primary justification for why a Software Maintenance Plan is mandatory.

---

## Maintenance Process Models (W-15 selection criteria)

| Model | When to use | Key gap |
|-------|-------------|---------|
| Quick-Fix | Single-maintainer, low-risk tactical only | No documentation; "spaghetti syndrome" |
| Boehm's | Management-driven cost-benefit decisions | No detailed process steps |
| Osborne's | Non-ideal environments with missing docs; explicit post-install review | Complex |
| Iterative Enhancement | Well-documented, reuse-oriented systems | Assumes complete documentation |
| Reuse-Oriented (Basili) | Component-based systems | Requires classification framework |

**Osborne's model explicitly names "Post-installation review of changes" as step 14** — the only named post-deployment gate in any model.

---

## Change Request Form Fields (Figure 11.5)

- Name of system
- Version
- Revision
- Date
- Requested by
- Summary of change
- Reasons for change
- Software components requiring change
- Documents requiring change
- Estimated cost

**Gap vs. ISO 14764:** Add priority, severity, and maintenance type classification fields.

---

## Maintainability Metrics

| Metric | Formula |
|--------|---------|
| McCabe's Cyclomatic Complexity | $v(F) = e - n + 2$ (above 10 = very complex) |
| Halstead Program Length | $N = N_1 + N_2$ |
| Halstead Effort | $E = \frac{\eta_1 N_2 (N_1 + N_2) \log_2(\eta_1 + \eta_2)}{2\eta_2}$ |
| MTTR | Recognition time + admin delay + tools collection + analysis + specification + change times |
| Change requests / KLOC | Unique customer requests in year 1 / KLOC |
| Schedule variance | (Planned − Actual) / Planned as % |
| Productivity | Delta LOC / staff-days |

**Note:** MTBF (Mean Time Between Failures) is NOT covered — must come from ISO 14764.

---

## Post-Deployment Evaluation Fields (W-16 Template)

Grubb & Takang have no dedicated post-deployment report template but the following fields are derivable:

- System version / release number
- Deployment date
- Reporting period end date
- Change requests per KLOC (first year — primary health indicator)
- Post-operational fault count (with user-weighting for severity)
- MTTR (broken into 6 sub-components)
- Schedule variance (%)
- Productivity (delta LOC / staff-days)
- Documentation currency status
- User satisfaction (with caveat: insufficient alone; must pair with structural metrics)
- Recommended type mix for next period (corrective / adaptive / perfective / preventive targets)

---

## Required Documentation Set (Table 7.1)

**User documentation:** System overview | Installation guide | Tutorial | Reference guide | Enhancement booklet | Quick reference | System administration

**System documentation:** System rationale | Requirements spec | Design spec | Implementation guide | System test plan | Acceptance test plan | Data dictionaries

---

## W-15 (SMP Skill): What Grubb & Takang add to ISO 14764

1. Empirical cost data (40–75%) — use as SMP justification
2. Change Request Form template (Figure 11.5)
3. Lehman's Laws I and VII — theoretical justification for why SMP is mandatory
4. Process model selection criteria — SMP should specify which process model applies
5. Cost estimation methods: COCOMO II, historical data, person-months
6. Lientz/Swanson type distribution — use as effort budgeting reference

## W-16 (Post-Deployment Evaluation): What Grubb & Takang add

1. Osborne's post-installation review step (confirms this is a recognized gate)
2. First-year field quality metric (change requests per KLOC)
3. Post-operational fault count with user-weighting
4. Schedule variance formula
5. MTTR sub-component decomposition
6. User satisfaction caveat
7. Ongoing support framework (communication, training, business information)

---

## Anti-Patterns for W-15

| Anti-Pattern | Source | Why It Fails |
|-------------|--------|--------------|
| Using quick-fix exclusively | ACME case study (pp.77–79) | Array overflow undetected; emergency fix violated requirements |
| No CCB for live system changes | Section 11.4.1 | Changes approved by wrong criteria (technical not strategic) |
| Source code diverges from documentation | Section 11.3 | Maintainers cannot understand code; MTTR increases |
| Corrective maintenance only | Chapter 3 | Perfective is 50% of real workload; planning ignores majority of effort |
| No process model declared | Chapter 5 | Team defaults to quick-fix under pressure |
