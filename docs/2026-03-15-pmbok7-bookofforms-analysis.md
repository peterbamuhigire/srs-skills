# PMBOK 7th Edition & Book of Forms — Full Extraction Analysis

**Date:** 2026-03-15
**Purpose:** Extract all insights from PMBOK® Guide 7th Edition and A Project Manager's Book of Forms (6th Ed. Companion) for improving the SRS-Skills documentation engine.
**Pending Improvements Mapped:** W-13, W-14, W-17, W-18, B-05, B-11

---

## SECTION 1: PMBOK® GUIDE — SEVENTH EDITION

### A. The 12 Project Management Principles

The 7th Edition shifts from a process-based standard to a principles-based standard. The 12 principles are not prescriptive rules; they are foundational behavioral guidelines for project practitioners.

| # | Principle Name | Core Meaning | Documentation Implication |
|---|----------------|-------------|---------------------------|
| 1 | **Stewardship** | Act responsibly for the organization, sponsors, team, and society. Uphold diligence, trustworthiness, and compliance. | Project charter must name an accountable steward. Governance docs must reference ethical obligations. |
| 2 | **Team** | Build a collaborative project team environment. Foster shared ownership, mutual respect, and diversity. | Team Charter (resource plan) must codify shared values and conflict resolution. |
| 3 | **Stakeholders** | Engage stakeholders proactively to understand their interests and needs. | Stakeholder Register + Engagement Plan are mandatory artifacts. Continuous engagement, not one-time analysis. |
| 4 | **Value** | Continually evaluate and adjust project alignment to achieve intended benefits. | Business value must be stated in the charter and traced through requirements to deliverables. |
| 5 | **Systems Thinking** | Recognize and respond to the dynamic interrelationships within and outside the project. | Requirements must capture external constraints and system interfaces. Cross-cutting risks need special attention. |
| 6 | **Leadership** | Motivate, influence, and coach teams. Adapt leadership style to situation. | Resource management plans and team charters should acknowledge leadership approach. |
| 7 | **Tailoring** | Deliberately tailor the approach for each project based on context, goals, and constraints. | Meta-initialization skill must ask methodology questions to select artifacts and workflow. [W-18] |
| 8 | **Quality** | Build quality into processes and deliverables; meet stakeholder acceptance criteria. | Quality Management Plan is mandatory. Acceptance criteria must appear in requirements documentation. |
| 9 | **Complexity** | Navigate complexity through continuous evaluation. Understand system behavior and uncertainty. | Risk Register must address emergent complexity. SRS must document interdependencies. |
| 10 | **Risk** | Identify and respond to both threats and opportunities. | Risk Register and Risk Report are mandatory throughout project lifecycle. [W-14] |
| 11 | **Adaptability & Resilience** | Build adaptability and resilience into the organization and the team. | Hybrid lifecycle options must be available. Iterative delivery supported. [W-18] |
| 12 | **Change** | Prepare those affected for adoption of the project output to achieve the expected value. | Change management artifacts (Change Request, Change Log, CCB Charter) are first-class outputs. [W-17] |

---

### B. The 8 Performance Domains

Performance Domains replace the 10 Knowledge Areas × 5 Process Groups structure from the 6th Edition. They represent interconnected areas of project work that collectively deliver outcomes.

#### 1. Stakeholders Performance Domain
- **Scope:** Identifying, analyzing, and engaging stakeholders continuously throughout the project.
- **Key Activities:** Identify stakeholders → Understand their interests → Analyze influence/power → Prioritize → Engage → Monitor engagement levels.
- **Engagement Levels (PMBOK 7th):** Unaware → Resistant → Neutral → Supportive → Leading
- **Key Artifacts:** Stakeholder Register, Stakeholder Engagement Plan, Communications Management Plan.
- **Implication for W-13:** The Stakeholder Register must capture Current (C) and Desired (D) engagement levels. The Engagement Plan must describe the strategy to move each stakeholder to the desired level.

#### 2. Team Performance Domain
- **Scope:** Establishing a high-performing project team with the right skills, behaviors, and culture.
- **Key Activities:** Define team structure, develop shared agreements, manage performance, resolve conflicts.
- **Key Artifacts:** Resource Management Plan, Team Charter, RACI Matrix, Team Performance Assessment.
- **Implication:** Team Charter is a mandatory output at project initialization. It must include values, meeting guidelines, communication protocols, decision-making process, and conflict resolution process.

#### 3. Development Approach & Life Cycle Performance Domain
- **Scope:** Selecting the development approach (predictive, adaptive, hybrid) and project life cycle phases.
- **Key Activities:** Select approach → Tailor for organization → Tailor for project → Implement ongoing improvement.
- **Predictive Indicators:** Fixed scope, stable requirements, clear technology, compliance-heavy.
- **Adaptive Indicators:** Evolving requirements, rapid change, stakeholder availability for continuous feedback.
- **Hybrid Indicators:** Predictive phases (planning, procurement) + adaptive development (sprints).
- **Key Artifacts:** Project Roadmap, Release Plan, Sprint Plans (for adaptive components).
- **Implication for W-18:** Meta-initialization must detect hybrid patterns. Water-Scrum-Fall = predictive planning phases + adaptive sprints + predictive deployment. Detection signals: mixed methodology answers, regulated environment + iterative development stated together.

#### 4. Planning Performance Domain
- **Scope:** Organizing and coordinating all planning activities to produce a viable project management plan.
- **Recommended Artifacts:**
  - Project Management Plan (umbrella)
  - Scope Management Plan
  - Requirements Management Plan
  - Schedule Management Plan
  - Cost Management Plan
  - Quality Management Plan
  - Resource Management Plan
  - Communications Management Plan
  - Risk Management Plan
  - Procurement Management Plan
  - Stakeholder Engagement Plan
  - Baselines: Scope Baseline, Schedule Baseline, Cost Baseline
- **Scope Definition:** Project Scope Statement → WBS → WBS Dictionary → Scope Baseline
- **Implication for B-05:** Each planning artifact represents a phase gate checkpoint. Skills must verify these are present before advancing to execution skills.

#### 5. Project Work Performance Domain
- **Scope:** Establishing project processes, managing physical resources, and fostering a learning environment.
- **Process Governance:** Change control process, issue escalation, decision logging.
- **Key Artifacts:** Issue Log, Decision Log, Change Request, Change Log.
- **Change Control:** All changes flow through Change Request → CCB Review → Change Log update. [W-17]

#### 6. Delivery Performance Domain
- **Scope:** Delivering project deliverables that realize business value and meet stakeholder requirements.
- **Key Activities:** Requirements elicitation → analysis → prioritization → validation → delivery → acceptance.
- **Key Artifacts:** Requirements Documentation, Requirements Traceability Matrix, Product Acceptance Form.
- **Implication:** Requirements must be traceable from business need → functional requirement → test case → acceptance.

#### 7. Measurement Performance Domain
- **Scope:** Assessing project performance and taking appropriate actions to maintain acceptable performance.
- **SMART Metrics Criteria:** Specific, Meaningful, Achievable, Relevant, Timely.
- **KPI Types:**
  - **Leading indicators:** Predict future performance (e.g., requirements volatility rate, defect injection rate)
  - **Lagging indicators:** Measure past results (e.g., defect density, schedule variance at phase end)
- **EVM Metrics:**
  - $SV = EV - PV$ (Schedule Variance)
  - $CV = EV - AC$ (Cost Variance)
  - $SPI = EV / PV$ (Schedule Performance Index)
  - $CPI = EV / AC$ (Cost Performance Index)
  - $EAC = BAC / CPI$ (Estimate at Completion, if CPI holds)
  - $TCPI = (BAC - EV) / (BAC - AC)$ (To-Complete Performance Index)
- **OKR Framework:** Objectives (qualitative outcomes) + Key Results (measurable indicators). Used for benefits realization tracking.
- **Cost of Quality (COQ):**
  - Prevention costs (training, process improvement)
  - Appraisal costs (testing, inspection)
  - Internal failure costs (rework, defects found before delivery)
  - External failure costs (warranty, support, customer dissatisfaction)
- **Implication for B-11:** The `metrics.md` scaffold must include: EVM baseline fields (BAC, PV, EV, AC), KPI table with Leading/Lagging classification, COQ breakdown, OKR objective + key result slots.

#### 8. Uncertainty Performance Domain
- **Scope:** Addressing risk, ambiguity, and complexity throughout the project.
- **Risk Cycle:** Identify → Analyze (qualitative + quantitative) → Plan Responses → Implement → Monitor.
- **Risk Response Strategies (Threats):** Avoid, Transfer, Mitigate, Accept (active/passive).
- **Risk Response Strategies (Opportunities):** Exploit, Share, Enhance, Accept.
- **Implication for W-14:** Risk Register must include both threats and opportunities. Revised probability and revised impact columns must be present (post-response).

---

### C. Tailoring Approach

The PMBOK 7th Edition presents a four-step tailoring process:

1. **Select the Initial Development Approach** — based on product characteristics, project characteristics, and organizational characteristics.
2. **Tailor for the Organization** — adapt to organizational culture, governance, and tooling.
3. **Tailor for the Project** — customize for team size, stakeholder complexity, risk profile.
4. **Implement Ongoing Improvement** — inspect and adapt throughout the project.

**Tailoring Questions for Meta-Initialization [W-18]:**

| Question | Signals Predictive | Signals Adaptive | Signals Hybrid |
|----------|-------------------|-----------------|----------------|
| Are requirements stable at project start? | Yes | No | Partially |
| Is the client available for continuous feedback? | No | Yes | Sometimes |
| Is the technology well-understood? | Yes | No/Cutting-edge | Mixed |
| Is there a regulatory/compliance driver? | Strong | Weak | Present but bounded |
| Are deliverables incremental or single-release? | Single release | Incremental | Both |
| Is the team experienced with agile? | No | Yes | Mixed |

**Water-Scrum-Fall Hybrid Pattern Detection:**
- Predictive planning (scope, schedule, budget defined upfront) + adaptive development sprints + predictive deployment/closeout
- Trigger phrase examples: "We use sprints but have a fixed budget," "We plan the full project then develop in iterations," "We have a deadline but requirements evolve"

---

### D. Value Delivery System

The PMBOK 7th Edition introduces a System for Value Delivery as the overarching context for all project work:

```
Organizational Strategy
    ↓
Portfolio (collection of programs and projects)
    ↓
Program (related projects managed for benefits)
    ↓
Project (temporary endeavor to create a unique product/service/result)
    ↓
Deliverables
    ↓
Outcomes (changes in behavior, state, or condition)
    ↓
Benefits (gain realized by the organization/stakeholder)
    ↓
Value (net worth of benefits)
```

**Documentation Implication:** The Project Charter must connect the project to organizational strategy. Section 1.2 of the SRS (Business Context) must trace requirements to benefits and benefits to organizational value. The CCB Charter [W-17] must reference whether approved changes preserve or threaten the value chain.

---

### E. Stakeholder Performance Domain — Detailed

**Stakeholder Identification Tools:**
- Stakeholder register (primary artifact)
- Stakeholder engagement assessment matrix (Current C vs. Desired D engagement level)
- Power/interest grid (high power + high interest = manage closely)
- Salience model (power + legitimacy + urgency)
- RACI matrix (Responsible, Accountable, Consulted, Informed)

**Stakeholder Register Fields [W-13]:**

| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name | Stakeholder name |
| Position/Role | Organizational role |
| Organization | Company or department |
| Contact Information | Email, phone |
| Major Requirements | What they need from the project |
| Expectations | What they expect as outcomes |
| Potential Influence | High/Medium/Low influence on project |
| Phase of Most Interest | When they are most actively involved |
| Engagement Level (Current) | Unaware/Resistant/Neutral/Supportive/Leading |
| Engagement Level (Desired) | Target engagement level |
| Comments | Additional notes |

**Communications Management Plan Fields [W-13]:**

| Field | Description |
|-------|-------------|
| Stakeholder/Group | Recipient of communications |
| Information | What is communicated (format, language, level of detail) |
| Method/Media | Email, meeting, web meeting, report, dashboard |
| Time Frame and Frequency | Weekly, monthly, at milestone, on exception |
| Sender | Person responsible for sending |
| Communication Constraints/Assumptions | Proprietary info handling, multi-timezone notes |
| Glossary of Common Terminology | Project-specific terms and acronyms |

---

### F. Planning Performance Domain — Detailed Artifacts

**Project Scope Statement Fields:**
- Project purpose/justification
- Product scope description
- Project deliverables
- Project acceptance criteria
- Project exclusions
- Project constraints
- Project assumptions

**WBS (Work Breakdown Structure):**
- Hierarchical decomposition of total scope
- Work packages at lowest level (assignable and estimable units)
- WBS Dictionary: for each work package — ID, name, description, responsible party, schedule dates, acceptance criteria, technical references

**Requirements Documentation Fields (Skill 05 input):**

| Field | Description |
|-------|-------------|
| ID | Unique requirement identifier |
| Requirement | Detailed description |
| Business Need | Originating business need |
| Stakeholder | Requesting stakeholder |
| Priority | High/Medium/Low or MoSCoW |
| Acceptance Criteria | Measurable pass/fail condition |
| Test Method | How verified |
| Status | Proposed/Approved/Deferred/Deleted |
| Phase/Release | When delivered |

**Requirements Traceability Matrix Fields:**
- Requirement ID
- Requirement Description
- Business Need/Objective
- WBS Reference
- Design Reference
- Test Case Reference
- Status

---

### G. Measurement Performance Domain — Detailed (B-11 metrics.md Scaffold)

**Recommended metrics.md structure:**

```markdown
# Project Metrics

## Earned Value Baseline
- Budget at Completion (BAC): [value]
- Reporting Period:

## EVM Table (per reporting period)
| Metric | Formula | Current Period | Cumulative |
|--------|---------|---------------|------------|
| PV (Planned Value) | — | | |
| EV (Earned Value) | — | | |
| AC (Actual Cost) | — | | |
| SV (Schedule Variance) | EV - PV | | |
| CV (Cost Variance) | EV - AC | | |
| SPI | EV / PV | | |
| CPI | EV / AC | | |
| EAC | BAC / CPI | | |
| TCPI | (BAC - EV) / (BAC - AC) | | |

## Key Performance Indicators (KPIs)
| KPI | Type | Target | Actual | Status |
|-----|------|--------|--------|--------|
| [Leading KPI] | Leading | | | |
| [Lagging KPI] | Lagging | | | |

## OKRs (Objectives and Key Results)
### Objective 1: [Qualitative outcome statement]
- KR1: [Measurable result + target value]
- KR2: [Measurable result + target value]

## Cost of Quality (COQ)
| Category | Planned | Actual |
|----------|---------|--------|
| Prevention (training, process design) | | |
| Appraisal (inspections, testing) | | |
| Internal Failure (rework, defects) | | |
| External Failure (warranty, escalations) | | |

## Phase Gate Criteria (B-05)
| Phase Gate | Exit Criteria | Status |
|-----------|--------------|--------|
| Phase 01 → 02 | Requirements baselined, stakeholders identified | |
| Phase 02 → 03 | SRS reviewed and signed off | |
| Phase 03 → 04 | Architecture reviewed, interfaces defined | |
| Phase 04 → 05 | Code review passed, unit tests > 80% | |
| Phase 05 → 06 | Acceptance tests passed | |
| Phase 06 → 07 | Production deployment validated | |
```

---

### H. Project Work Performance Domain — Change Control (W-17)

**CCB Charter Required Elements:**

| Element | Description |
|---------|-------------|
| Purpose | Describe the CCB's authority and mandate |
| Scope of Authority | What change categories require CCB review |
| Membership | Chair, voting members, advisory members, roles |
| Quorum Requirements | Minimum attendance for valid decisions |
| Meeting Cadence | Regular schedule + emergency procedures |
| Change Request Process | Submission → Triage → Impact Assessment → Vote → Log |
| Disposition Options | Approve / Defer / Reject |
| Escalation Path | Who receives escalated decisions |
| Record Keeping | Change Log maintenance, archival policy |
| Audit Trail | Version control reference for CCB decisions |

---

### I. Key Changes from 6th to 7th Edition

| Area | 6th Edition | 7th Edition |
|------|-------------|-------------|
| Structure | Process-based (49 processes × 5 groups × 10 KAs) | Principles-based (12 principles + 8 performance domains) |
| Prescriptiveness | Step-by-step process outputs | Outcome-focused with tailoring latitude |
| Methodology | Primarily predictive (Waterfall) | Methodology-agnostic (predictive + adaptive + hybrid) |
| Value Delivery | Project success = on time/budget/scope | Project success = delivery of intended value/outcomes |
| Tailoring | Section in each KA | Dedicated Tailoring section; tailoring is now a principle |
| Stakeholders | KA 13 (Stakeholder Management) | Full performance domain with engagement cycle |
| Agile | Agile Practice Guide supplement | Integrated throughout (adaptive + hybrid approaches) |
| Models/Methods/Artifacts | Not catalogued separately | Dedicated MMA (Models, Methods, Artifacts) section |

---

## SECTION 2: A PROJECT MANAGER'S BOOK OF FORMS (6th Edition Companion)

### A. Complete Forms Inventory

#### Process Group 1: Initiating (Forms 1.x)

| Form # | Form Name | PMBOK Process | Key Fields |
|--------|-----------|--------------|------------|
| 1.1 | Project Charter | 4.1 Develop Project Charter | Project purpose, objectives, success criteria, high-level scope, major deliverables, high-level timeline, budget summary, approval requirements, project manager authority |
| 1.2 | Assumption Log | 4.1 / ongoing | ID, assumption/constraint, category, impact, owner, resolution date |
| 1.3 | Stakeholder Register (initial) | 13.1 Identify Stakeholders | ID, name, role, organization, contact, major requirements, expectations, influence level, engagement level (C/D) |
| 1.4 | Stakeholder Analysis | 13.1 | Power/Interest grid, salience model entries, influence/impact analysis |

#### Process Group 2: Planning (Forms 2.x)

| Form # | Form Name | PMBOK Process | Key Fields |
|--------|-----------|--------------|------------|
| 2.1 | Project Management Plan | 4.2 | Component plans list, baseline references, change management approach, performance measurement baseline |
| 2.2 | Scope Management Plan | 5.1 | Scope definition process, WBS creation approach, scope baseline maintenance, scope control process |
| 2.3 | Requirements Management Plan | 5.1 | Requirements collection approach, configuration management, prioritization process, traceability matrix approach |
| 2.4 | Requirements Documentation | 5.2 | ID, requirement, business need, stakeholder, category, priority, acceptance criteria, test method, status, phase/release |
| 2.5 | Requirements Traceability Matrix | 5.2 | Req ID, description, business objective, WBS, design reference, test case, status |
| 2.6 | Project Scope Statement | 5.3 | Purpose/justification, product scope description, deliverables, acceptance criteria, exclusions, constraints, assumptions |
| 2.7 | WBS | 5.4 | Hierarchical decomposition, work package IDs |
| 2.8 | WBS Dictionary | 5.4 | Work package ID, name, description, responsible party, schedule dates, acceptance criteria, technical references |
| 2.9 | Schedule Management Plan | 6.1 | Scheduling tool, level of accuracy, units of measure, control thresholds, rules for performance measurement |
| 2.10 | Activity List | 6.2 | ID, WBS reference, activity name, description |
| 2.11 | Activity Attributes | 6.2 | ID, activity name, predecessor, successor, resource requirements, constraints, imposed dates, assumptions, notes |
| 2.12 | Milestone List | 6.2 | ID, milestone, schedule date, mandatory/discretionary |
| 2.13 | Network Diagram | 6.3 | Predecessor/successor relationships, FS/FF/SS/SF types, lead/lag |
| 2.14 | Resource Requirements | 6.4 | ID, WBS reference, resource type, quantity, skill level, notes |
| 2.15 | Resource Breakdown Structure | 6.4 | Hierarchical breakdown: labor, materials, equipment by category |
| 2.16 | Duration Estimates | 6.4 | ID, activity description, effort hours, duration estimate |
| 2.17 | Duration Estimating Worksheet | 6.4 | Parametric (effort/quantity/availability/factor), Analogous, Three-Point Beta Distribution |
| 2.18 | Project Schedule (Gantt) | 6.5 | WBS ID, task name, start, finish, resource, dependency bars |
| 2.19 | Milestone Chart | 6.5 | Milestone name, planned date, dependency |
| 2.20 | Cost Management Plan | 7.1 | Units of measure, level of precision, control thresholds, rules for EVM, reporting format, contingency protocols |
| 2.21 | Activity Cost Estimates | 7.2 | ID, WBS reference, resource type, quantity, unit cost, total cost, basis of estimate |
| 2.22 | Cost Estimating Worksheet | 7.2 | Analogous, parametric, bottom-up columns; contingency reserve |
| 2.23 | Cost Baseline | 7.3 | Time-phased budget, management reserve, project budget summary |
| 2.24 | Quality Management Plan | 8.1 | Quality standards, quality objectives, quality roles, quality tools, quality audits schedule, acceptance criteria |
| 2.25 | Quality Metrics | 8.1 | Metric, purpose, measurement method, target, actual, acceptable range |
| 2.26 | Resource Management Plan | 9.1 | Resource identification, acquisition approach, roles & responsibilities, RACI matrix, training needs, recognition/rewards, compliance, safety |
| 2.27 | Team Charter | 9.1 | Team values/principles, meeting guidelines, communication guidelines, decision-making process, conflict resolution process, other agreements |
| 2.28 | Responsibility Assignment Matrix (RAM/RACI) | 9.1 | Roles vs. deliverables/activities; R=Responsible, A=Accountable, C=Consulted, I=Informed |
| 2.29 | Resource Requirements | 9.2 | WBS ID, resource type, resource name, quantity, skill level, availability dates |
| 2.30 | Communications Management Plan | 10.1 | Stakeholder/group, information content, method/media, time frame/frequency, sender, constraints/assumptions, glossary |
| 2.31 | Risk Management Plan | 11.1 | Strategy, methodology, roles/responsibilities, risk categories, funding, frequency/timing, stakeholder risk appetite, probability/impact definitions and matrix, tracking/audit approach |
| 2.32 | Risk Register | 11.2 | Risk ID, risk statement (If/Then/Impact format), risk owner, probability, impact (scope/quality/schedule/cost), score, response strategy, revised probability, revised impact, revised score, actions, status, comments |
| 2.33 | Risk Report | 11.2 | Executive summary, overall project risk (trends/drivers/responses), individual risks matrix, metrics (active/closed by category), top 5 risks + responses, quantitative analysis summary, reserve status |
| 2.34 | Probability and Impact Assessment | 11.3 | Risk ID, description, probability rating, impact ratings per objective (scope/quality/schedule/cost), combined risk score, response strategy |
| 2.35 | Probability and Impact Matrix | 11.3 | 5×5 grid (VH/H/M/L/VL) with color-coded risk zones |
| 2.36 | Risk Data Sheet | 11.4 | Risk ID, category, trigger, current status, probability, impact, response, owner, actions, due dates |
| 2.37 | Procurement Management Plan | 12.1 | Integration approach (scope/schedule/docs/risk/reporting), timing of key activities, performance metrics, roles/responsibilities, assumptions/constraints, legal jurisdiction, independent estimates, prequalified sellers |
| 2.38 | Procurement Strategy | 12.1 | Delivery method, contract type (FFP/FPIF/CPFF/CPIF/T&M), procurement phases with entry/exit criteria |
| 2.39 | Source Selection Criteria | 12.1 | Criteria 1–N with rating scale (1–5), weights summing to 100%, scoring matrix per candidate |
| 2.40 | Stakeholder Engagement Plan | 13.2 | Engagement assessment matrix (C=Current/D=Desired, Unaware/Resistant/Neutral/Supportive/Leading), pending stakeholder changes, interrelationships, engagement approach per stakeholder |

#### Process Group 3: Executing (Forms 3.x)

| Form # | Form Name | PMBOK Process | Key Fields |
|--------|-----------|--------------|------------|
| 3.1 | Issue Log | 4.3 | ID, type/category, issue description, priority (Urgent/High/Medium/Low), impact on objectives, responsible party, status (Open/Closed), resolution date, final resolution, comments |
| 3.2 | Decision Log | Ongoing | ID, category, decision description, responsible party, date, comments (alternatives considered, rationale) |
| 3.3 | Change Request | 4.3 | Requestor, category (Scope/Quality/Requirements/Cost/Schedule/Documents), detailed description, justification, impacts (scope/quality/requirements/cost/schedule/stakeholder risk/project documents), comments |
| 3.4 | Change Log | 4.6 | ID, category, description, requestor, submission date, status (Open/Pending/Closed), disposition (Approved/Deferred/Rejected) |
| 3.5 | Lessons Learned Register | 4.4 | ID, category (process/technical/environmental/stakeholder/phase), trigger, lesson articulated, responsible party, comments |
| 3.6 | Quality Audit | 8.2 | Areas audited (checklist), good practices from similar projects, areas for improvement, deficiencies/defects (ID/defect/action/responsible/due date), comments |
| 3.7 | Team Performance Assessment | 9.4 | Technical performance (scope/quality/schedule/cost) rated Exceeds/Meets/Needs Improvement, interpersonal competency (communication/collaboration/conflict management/decision making), team morale, areas for development (area/approach/actions) |

#### Process Group 4: Monitoring & Controlling (Forms 4.x)

| Form # | Form Name | PMBOK Process | Key Fields |
|--------|-----------|--------------|------------|
| 4.1 | Team Member Status Report | 4.5 | Activities planned/accomplished/not accomplished (current period), root cause of variances, funds spent vs. planned, quality variances, corrective/preventive actions, plans for next period, new risks, new issues |
| 4.2 | Project Status Report | 4.5 | Accomplishments (current/planned next period), root cause of variances, milestone impact, funds spent, budget impact, corrective/preventive actions, new risks and issues |
| 4.3 | Variance Analysis | 4.5/6.6/7.4 | Schedule variance (planned/actual/variance/root cause/response), Cost variance (same), Quality variance (same) |
| 4.4 | Earned Value Analysis | 4.5/7.4 | BAC, PV, EV, AC, SV, CV, SPI, CPI, % planned/earned/spent, EAC (two methods), TCPI; root cause + impact narratives |
| 4.5 | Risk Audit | 11.7 | Risk event audit (event/cause/response/comment), risk response audit (event/response/successful/improvement actions), risk management process audit (Plan/Identify/Qualitative/Quantitative/Plan Responses/Monitor), good practices, areas for improvement |
| 4.6 | Contractor Status Report | 12.3 | Scope/quality/schedule/cost performance (current period), forecast performance, claims/disputes, risks, corrective/preventive actions, issues, comments |
| 4.7 | Procurement Audit | 12.3 | Vendor performance (what worked well/what can be improved per scope/quality/schedule/cost/other), procurement management process audit (Plan/Conduct/Control), good practices, areas for improvement |
| 4.8 | Contract Closeout | 12.3 | Vendor performance analysis (scope/quality/schedule/cost/other — well/improved), record of contract changes (ID/description/date approved), record of contract disputes (description/resolution/date resolved), completion date, signoff, final payment date |
| 4.9 | Product Acceptance Form | 5.5 | Req ID, requirement, acceptance criteria, validation method, status (Accepted/Not Accepted), sign-off |

#### Process Group 5: Closing (Forms 5.x)

| Form # | Form Name | PMBOK Process | Key Fields |
|--------|-----------|--------------|------------|
| 5.1 | Lessons Learned Summary | 4.7 | Project performance analysis table (what worked well / what can be improved) for: requirements definition, scope, schedule, cost, quality, physical resources, team, communications, reporting, risk management, procurement, stakeholder engagement, process improvement, product-specific; plus risks/issues table, quality defects table, vendor management table, areas of exceptional performance / areas for improvement |
| 5.2 | Project/Phase Closeout | 4.7 | Project description, performance summary (scope objectives + completion criteria + evidence, quality objectives + V&V info), variances (time/cost with explanation), benefits management, business needs satisfaction, risks and issues summary |

#### Section 6: Agile Forms (Forms 6.x)

| Form # | Form Name | Agile Equivalent | Key Fields |
|--------|-----------|-----------------|------------|
| 6.1 | Product Vision | Charter (Agile) | Target customer, needs addressed, product/key attributes, key benefit (buy motivation). Template: "We are developing [product] for [customer] to respond to [needs] by providing [attributes] because [benefit]." |
| 6.2 | Product Backlog | Requirements Documentation (Agile) | ID, summary description (1-2 sentences), priority (High/Med/Low or numbered), story (user story or reference), status (Not Started/In Progress/Complete) |
| 6.3 | Release Plan | Schedule Management Plan (Agile) | Release goal, sprint lanes (Sprint 1-N), user stories per sprint per team, milestone indicators |
| 6.4 | Retrospective | Lessons Learned Register (Agile) | Starfish model: Start / Stop / Keep / More / Less. Alternative: FLAP (Future Considerations, Lessons, Accomplishments, Problems) |

---

### B. Forms Most Relevant to SDLC/Requirements Engineering

#### Charter and Kickoff Forms

**Form 1.1 — Project Charter** (Critical baseline document)
- Purpose: Formally authorizes the project and the project manager's authority
- Fields: Title, date, project purpose/justification, measurable project objectives, high-level requirements, high-level project description, boundaries, deliverables, assumptions, constraints, high-level risks, project approval requirements, assigned PM + authority level, sponsor signature
- SDLC Link: Inputs to Skill 01 (initialization) and Skill 02 (project intro/vision)

**Form 1.2 — Assumption Log**
- Fields: ID, assumption or constraint, category (scope/schedule/cost/resource/etc.), impact if wrong, responsible owner, resolution date
- SDLC Link: Referenced in every subsequent planning form as input

**Form 1.3 & 1.4 — Stakeholder Register + Analysis** [W-13]
- Register Fields: ID, name, position, organization, contact, major requirements, expectations, influence level, current engagement level, desired engagement level
- Analysis: Power/Interest grid quadrant assignment, salience ratings
- SDLC Link: Input to Skill 03 (stakeholder analysis), Skill 05 (requirements generation)

#### Requirements and Scope Forms

**Form 2.3 — Requirements Management Plan**
- Fields: Requirements collection process, configuration management, prioritization process, traceability approach, change management for requirements, reporting format

**Form 2.4 — Requirements Documentation** (Core Skill 05 output)
- Fields: ID, requirement statement, business need, stakeholder, category (functional/non-functional), priority, acceptance criteria, test method, status, phase/release
- IEEE 830 compliance: Each requirement must be Correct, Unambiguous, Complete, Consistent, Ranked, Verifiable, Modifiable, Traceable

**Form 2.5 — Requirements Traceability Matrix**
- Fields: Requirement ID, description, business objective, project objective, WBS reference, product design reference, product development reference, test case reference, status

#### Change Control Forms [W-17]

**Form 3.3 — Change Request** (3-page form)
- Page 1: Requestor, category (Scope/Quality/Requirements/Cost/Schedule/Documents), detailed description, justification
- Page 2: Impacts — Scope (Increase/Decrease/Modify + description), Quality, Requirements, Cost, Schedule, Stakeholder Risk (High/Medium/Low), Project Documents list
- Page 3: Disposition (Approve/Defer/Reject) + Justification

**Form 3.4 — Change Log** (Tracking artifact)
- Fields: ID, category, description, requestor, submission date, status (Open/Pending/Closed), disposition (Approved/Deferred/Rejected)
- Note: Can be extended with: cost/schedule impact summary, mandatory/discretionary flag, bug fix indicator (IT), configuration item reference

**CCB Charter Requirements [W-17]:** The Book of Forms does not include a standalone CCB Charter form, but the Change Management Plan (Form 2.0 — part of Project Management Plan) addresses CCB structure. The CCB Charter must be created as a new Skill 09 artifact with the fields documented in Section 1.H above.

#### Risk Register [W-14]

**Form 2.32 — Risk Register** (Full field list)
- Risk ID, Risk Statement (If [condition] exists, [event] may occur, leading to [effect])
- Risk Owner
- Probability (VH/H/M/L/VL)
- Impact per objective: Scope, Quality, Schedule, Cost
- Risk Score (probability × impact)
- Response Strategy (Avoid/Transfer/Mitigate/Accept for threats; Exploit/Share/Enhance/Accept for opportunities)
- Revised Probability (post-response)
- Revised Impact (post-response)
- Revised Score
- Actions
- Responsible Party for actions
- Status (Open/Closed)
- Comments

**Form 2.31 — Risk Management Plan** (Prerequisite to Risk Register)
- Strategy, Methodology, Roles/Responsibilities
- Risk Categories (used for Risk Breakdown Structure)
- Funding, Frequency/Timing
- Stakeholder Risk Appetite/Tolerances
- Probability definitions (5-level scale with % thresholds)
- Impact definitions by objective (5-level scale with quantified thresholds)
- Probability × Impact matrix (5×5 with color zones)
- Tracking and Audit approach

**Enhancement for W-14:** Current srs-skills Risk Register scaffold should add: (1) separate impact columns per objective (scope/quality/schedule/cost), (2) opportunity tracking alongside threats, (3) revised probability/revised impact columns after response planning, (4) risk statement template in the `_context/risks.md` file guidance.

---

### C. Phase Gate Exit Criteria (B-05)

Based on PMBOK 7th and Book of Forms process group structure, the following phase gate exit criteria are recommended per skill:

| Skill | Phase Gate Name | Mandatory Exit Criteria |
|-------|----------------|------------------------|
| Skill 01 (Init) | Initialization Gate | Project name confirmed, domain identified, `_context/` directory populated, Project Charter stub present |
| Skill 02 (Intro) | Vision Gate | `vision.md` populated with business objectives, stakeholder list initial draft complete, SMART success criteria defined |
| Skill 03 (Overview) | Scope Gate | Product scope statement complete, high-level constraints documented, assumptions logged, project boundaries stated |
| Skill 04 (Interfaces) | Interface Gate | All external system interfaces defined, interface protocols specified, data formats documented |
| Skill 05 (Functional Req) | Requirements Gate | All functional requirements baselined, RTM populated, acceptance criteria present on all requirements, no `[CONTEXT-GAP]` flags unresolved |
| Skill 06 (Logic) | Logic Gate | All LaTeX formulas validated, decision tables/state diagrams complete, no `[V&V-FAIL]` tags unresolved |
| Skill 07 (Attributes) | NFR Gate | All non-functional requirements mapped to IEEE 982.1 metrics, NFR measurability verified |
| Skill 08 (Audit) | V&V Gate | RTM fully populated, all requirements traceable to business goals, all conflicts resolved, V&V Completion Certificate signed |

---

### D. Metrics Scaffold (B-11)

See Section 1.G above for the full `metrics.md` scaffold template. The Book of Forms adds these additional metric categories from the Measurement Performance Domain:

**From Form 2.25 — Quality Metrics:**
- Quality Metric ID
- Metric Name
- Purpose (why this is measured)
- Measurement Method (how collected)
- Target Value
- Acceptable Range (upper/lower tolerance)
- Actual Value (filled during execution)
- Status (In Control / Out of Control)

**From Form 4.4 — Earned Value Analysis:**
- EVM baseline (BAC, PV, EV, AC)
- Period and cumulative columns
- Root cause and impact narratives (narrative required, not just numbers)

**From Form 4.3 — Variance Analysis:**
- Schedule variance with root cause and planned response
- Cost variance with root cause and planned response
- Quality variance with root cause and planned response

---

## SECTION 3: PENDING IMPROVEMENT MAPPINGS

### W-13: Stakeholder Register + Communication Plan Upgrade (Phase 02 Skill 01)

**Key additions:**
1. Add Current (C) vs. Desired (D) engagement level columns to Stakeholder Register using 5-level scale: Unaware / Resistant / Neutral / Supportive / Leading
2. Add "Engagement Approach" column — strategy to move stakeholder from C to D
3. Add Stakeholder Engagement Assessment Matrix as second page of the register
4. Communications Management Plan must link to Stakeholder Register via shared stakeholder IDs
5. Comms Plan must include Glossary of Common Terminology field
6. Both documents must be kept in sync (feeds each other bidirectionally per PMBOK)

### W-14: Risk Register Improvements

**Key additions:**
1. Split Impact column into per-objective sub-columns: Scope / Quality / Schedule / Cost
2. Add Risk Statement template guidance: "If [CONDITION] exists, [EVENT] may occur, leading to [EFFECT]"
3. Add Revised Probability + Revised Impact + Revised Score columns (post-response assessment)
4. Add Responsible Party for actions (distinct from Risk Owner who monitors)
5. Add opportunity tracking (Exploit/Share/Enhance/Accept strategies)
6. Pre-populate `_context/risks.md` with risk statement template and category taxonomy from Risk Management Plan

### W-17: CCB Charter Sub-Skill (Phase 09)

**Required CCB Charter artifact fields (new sub-skill):**
1. CCB Purpose and authority scope
2. Membership list (Chair, voting members, advisory members)
3. Quorum requirements
4. Meeting cadence + emergency procedure
5. Change categories requiring CCB review vs. PM discretion
6. Change Request → CCB review → disposition → Change Log workflow
7. Escalation path beyond CCB
8. Record keeping and version control policy

**Supporting artifacts already in Book of Forms:**
- Form 3.3 Change Request (3 pages) — submit to CCB
- Form 3.4 Change Log — CCB maintains this
- CCB Charter itself is a new form not in the Book of Forms

### W-18: Water-Scrum-Fall Hybrid Detection (Meta-Initialization)

**Detection logic for meta-initialization Skill 01:**

```
IF (methodology == "Agile" OR methodology contains "scrum/sprint")
  AND (budget_type == "fixed" OR regulatory_compliance == true OR external_deadline == true)
THEN
  flag_hybrid = true
  lifecycle = "Water-Scrum-Fall"
  suggest: predictive planning artifacts + adaptive development artifacts + predictive closeout artifacts
```

**Artifacts to generate for hybrid:**
- Predictive: Project Charter, Scope Statement, Cost Baseline, Risk Management Plan, Communications Plan
- Adaptive: Product Backlog, Release Plan, Sprint Plans, Retrospective template
- Both: Change Request/Log, Lessons Learned Register, Issue Log

**Interview question additions to Skill 01 elicitation:**
- "Is your project budget fixed or flexible?"
- "Are requirements expected to change throughout the project?"
- "Is this project subject to regulatory approvals or compliance checkpoints?"
- "Do you use sprints or iterations for development?"
- "Is there a fixed delivery deadline regardless of scope changes?"

### B-05: Phase Gate Exit Criteria Per Skill Output

**Implementation approach:**
- Each skill's SKILL.md should end with a "Phase Gate Checklist" section
- The checklist items are the mandatory exit criteria before the next skill runs
- The Human Review Gate (per CLAUDE.md workflow Step 4) explicitly references these criteria
- A gate is not passed until: (a) no unresolved `[CONTEXT-GAP]` flags, (b) no `[V&V-FAIL]` tags, (c) consultant acknowledges review

**Gate implementation per skill:** See Section 2.C table above.

### B-11: Metrics.md Scaffold Content

**Implementation approach:**
- `_context/metrics.md` should be created at scaffold time with the template from Section 1.G
- Pre-populate the Phase Gate Criteria table from Section 2.C
- Pre-populate EVM baseline with `[CONTEXT-GAP: BAC not yet defined]` if budget not provided during initialization
- Quality Metrics table should be pre-populated from `domains/<domain>/references/nfr-defaults.md` where available

---

## APPENDIX: Book of Forms — Additional Details for Risk Register Forms

### Risk Data Sheet (Form 2.36) — Detail for Complex Risks

| Field | Description |
|-------|-------------|
| Risk ID | Unique identifier (matches Risk Register) |
| Risk Category | Category from risk breakdown structure |
| Risk Description | Detailed narrative of the risk event or condition |
| Trigger | Early warning indicators that the risk is about to occur |
| Status | Current status: Identified / Active / Occurred / Closed |
| Probability | Current probability rating |
| Impact | Current impact rating per objective |
| Response Strategy | Selected strategy (Avoid/Transfer/Mitigate/Exploit/Share/Enhance/Accept) |
| Response Description | Detailed description of the response actions |
| Risk Owner | Person responsible for monitoring and managing the risk |
| Action Items | List of specific tasks to implement the response |
| Due Dates | Deadline for each action item |
| Fallback Plan | Secondary response if primary response is ineffective |
| Comments | Additional notes |

*Use the Risk Data Sheet for the top 5-10 highest-priority risks as a supplement to the Risk Register.*

---

*Analysis compiled from full extraction of both source texts. All form field inventories are complete and accurate per the source material.*
