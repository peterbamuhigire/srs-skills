# Survey Design for Requirements Gathering

## Purpose

This reference provides templates and guidelines for designing questionnaires and surveys as a requirements elicitation technique. Surveys are the primary tool when stakeholders are geographically distributed, numerous, or available only asynchronously.

## Reference Standard

- IEEE 29148-2018 Section 6.3: Elicitation techniques
- Wiegers Practice 6: Survey and questionnaire design

## When to Use Questionnaires

| Condition | Suitability |
|-----------|-------------|
| Large stakeholder population (>10 respondents) | Excellent |
| Stakeholders are geographically distributed | Excellent |
| Need quantitative data on priorities or satisfaction | Excellent |
| Validating findings from interviews or workshops | Excellent |
| Deep exploration of complex, unknown requirements | Poor (use interviews) |
| Requirements need real-time discussion and negotiation | Poor (use JAD) |

## Question Type Reference

### Closed-Ended Questions

| Type | Format | Best For | Example |
|------|--------|----------|---------|
| **Yes/No** | Binary choice | Confirming existence of a need | "Do you currently track inventory manually?" |
| **Multiple Choice** | Select one from list | Categorical classification | "Which department do you work in?" |
| **Multi-Select** | Select all that apply | Feature preference gathering | "Which reports do you use? (select all)" |
| **Ranking** | Order items by preference | Priority determination | "Rank these features from most to least important" |

### Likert Scale Questions

Use a 5-point scale for consistency:

| Value | Label | Meaning |
|-------|-------|---------|
| 1 | Strongly Disagree | Definitive negative |
| 2 | Disagree | Negative |
| 3 | Neutral | No opinion |
| 4 | Agree | Positive |
| 5 | Strongly Agree | Definitive positive |

**Example**: "The current system meets my daily workflow needs."

| Strongly Disagree | Disagree | Neutral | Agree | Strongly Agree |
|--------------------|----------|---------|-------|----------------|
| 1 | 2 | 3 | 4 | 5 |

### Open-Ended Questions

| Type | Format | Best For | Example |
|------|--------|----------|---------|
| **Short Answer** | 1-2 sentence response | Specific feedback | "What is the most frustrating part of the current process?" |
| **Long Answer** | Paragraph response | Detailed exploration | "Describe your ideal workflow for order processing." |

Use only the open-ended questions needed for the decision frontier. Pilot the completion time and
analysis burden rather than applying a universal question-count rule.

## Survey Design Template

### Section 1: Demographics (3-5 questions)

```
1. What is your primary role? [Multiple Choice]
   - [ ] Manager
   - [ ] End User
   - [ ] Administrator
   - [ ] Other: ________

2. How long have you been in this role? [Multiple Choice]
   - [ ] Less than 1 year
   - [ ] 1-3 years
   - [ ] 3-5 years
   - [ ] More than 5 years

3. How frequently do you use the current system? [Multiple Choice]
   - [ ] Multiple times daily
   - [ ] Daily
   - [ ] Weekly
   - [ ] Monthly
   - [ ] Rarely
```

### Section 2: Current State Assessment (5-8 questions)

```
4. Rate your satisfaction with the current [process/system]: [Likert 1-5]

5. The current system supports my daily tasks effectively. [Likert 1-5]

6. I frequently encounter errors or issues with the current system. [Likert 1-5]

7. What are the top 3 pain points with the current process? [Multi-Select from list]

8. Describe a recent situation where the current system failed to meet your needs. [Open-ended]
```

### Section 3: Future State Requirements (5-8 questions)

```
9. Rank the following proposed features by importance: [Ranking]
   - Feature A: [description]
   - Feature B: [description]
   - Feature C: [description]

10. Which capabilities would most improve your daily workflow? [Multi-Select]

11. What is the maximum acceptable time to complete [task]? [Multiple Choice]
    - [ ] Under 1 second
    - [ ] 1-3 seconds
    - [ ] 3-5 seconds
    - [ ] 5-10 seconds
    - [ ] Over 10 seconds

12. Are there any features not listed above that you consider essential? [Open-ended]
```

### Section 4: Closing (1-2 questions)

```
13. Would you be available for a follow-up interview? [Yes/No]

14. Any additional comments or concerns? [Open-ended]
```

## Distribution Strategies

| Strategy | Channel | Best For | Required control |
|----------|---------|----------|------------------|
| **Email distribution** | Direct email with survey link | Known stakeholder list | consent, sender identity, deadline, reminder policy |
| **Meeting embed** | Scheduled meeting | Immediate clarification | protect dissent and avoid coerced consensus |
| **Intranet post** | Company collaboration space | Broad internal reach | define population and selection bias |
| **Facilitated session** | Guided completion | Access or literacy support | facilitator neutrality and private-response option |

Set the completion threshold from the decision risk, population, sampling method, subgroup coverage,
and planned analysis. A response percentage alone does not establish statistical validity. If coverage
is inadequate, report the missing groups and uncertainty, then follow up or switch method.

## Analysis Templates

### Quantitative Analysis

```
#### Survey Results Summary

**Distribution**: [Date sent] to [Date closed]
**Target Population**: [N] stakeholders
**Responses Received**: [n] ([n/N * 100]% response rate)

#### Likert Scale Results

| Question | Mean | Median | Std Dev | Interpretation |
|----------|------|--------|---------|----------------|
| Q4: Satisfaction | 2.3 | 2 | 0.8 | Below neutral -- improvement needed |
| Q5: Task support | 3.1 | 3 | 1.2 | Neutral -- mixed opinions |
| Q6: Error frequency | 3.8 | 4 | 0.6 | Agreement -- errors are common |

#### Feature Ranking Results

| Feature | Avg Rank | #1 Votes | Priority |
|---------|----------|----------|----------|
| Feature A | 1.4 | 12 | Critical |
| Feature B | 2.1 | 5 | High |
| Feature C | 2.5 | 3 | Medium |
```

### Qualitative Analysis

For open-ended responses, group by theme:

```
#### Theme: [Theme Name]
- **Frequency**: [N] respondents mentioned this theme
- **Representative Quotes**:
  - "[Quote 1]" -- [Role]
  - "[Quote 2]" -- [Role]
- **Derived Requirement**: The system shall [requirement].
- **Confidence**: [Based on frequency and consistency]
```

## Recording Format

For each finding derived from survey analysis:

```
#### EL-XXX: [Finding Title]

- **Source**: Survey -- [N] respondents ([response rate]%)
- **Technique**: Questionnaire
- **Question**: [Question number and text]
- **Result**: [Quantitative result or qualitative theme]
- **Derived Requirement**: The system shall [requirement].
- **Type**: Functional | Non-Functional | Constraint
- **Confidence**: Confirmed (>80% agreement) | Likely (50-80%) | Uncertain (<50%)
- **Statistical Basis**: Mean=[X], Median=[Y], N=[Z]
```

## Anti-Patterns to Avoid

| Anti-Pattern | Description | Correction |
|--------------|-------------|------------|
| Survey fatigue | More than 20 questions or 15 minutes to complete | Keep to 12-15 questions, 10 minutes max |
| Double-barreled questions | "Is the system fast and reliable?" | Split into two separate questions |
| Leading questions | "How much do you love Feature X?" | Use neutral phrasing |
| All open-ended | Survey of only open-ended questions | Mix quantitative and qualitative |
| No pilot test | Distributing without testing for clarity | Pilot with 2-3 people first |
