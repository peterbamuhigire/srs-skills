# Fagan Inspection Process for Requirements

**Purpose:** Structured inspection process adapted from Fagan's method for detecting defects in requirements artifacts before baselining.

**Standards:** IEEE 1012-2016, IEEE 1028-2008 (Reviews and Audits), Wiegers Practice 14

---

## 1. Inspection Overview

Fagan inspection is the most rigorous form of peer review. When applied to requirements, it detects defects at the earliest and cheapest point in the lifecycle. Studies show that formal inspections find 60-90% of defects before testing begins.

### 1.1 Key Principles

- **Defect detection, not correction:** The inspection meeting identifies defects; correction happens afterward.
- **Rate-controlled:** Review rates are capped to ensure thoroughness.
- **Metrics-driven:** Defect counts and rates are tracked to measure process effectiveness.
- **Ego-free:** The focus is on the artifact, not the author.

---

## 2. Inspection Roles

| Role        | Responsibility                                                   | Count    |
|-------------|------------------------------------------------------------------|----------|
| Moderator   | Plans and facilitates the inspection; ensures process compliance  | 1        |
| Author      | Created the requirements artifact; answers clarifying questions   | 1        |
| Inspector   | Reviews the artifact and identifies defects                      | 2-4      |
| Recorder    | Documents defects during the inspection meeting                  | 1        |
| Reader      | Paraphrases the requirements during the meeting (optional)       | 0-1      |

### Role Rules

- The author SHALL NOT serve as moderator or recorder
- The moderator SHALL be trained in the inspection process
- At least two inspectors SHALL participate (in addition to the moderator and author)
- One inspector may also serve as the reader

---

## 3. Inspection Phases

### Phase 1: Planning

**Moderator responsibilities:**
1. Verify the artifact is ready for inspection (author considers it complete)
2. Select inspectors with appropriate domain expertise
3. Assemble the inspection package:
   - The requirements artifact under inspection
   - The review checklist (`review-checklist.md`)
   - Supporting context files (`vision.md`, `features.md`, `business_rules.md`)
   - Any prior inspection findings
4. Schedule the inspection meeting (maximum 2 hours)
5. Distribute the package at least 48 hours before the meeting

### Phase 2: Individual Preparation

**Inspector responsibilities:**
1. Read the requirements artifact thoroughly
2. Apply the review checklist to each requirement
3. Record potential defects on the preparation log:

| Prep Finding ID | Requirement ID | Checklist Check | Potential Defect Description |
|-----------------|----------------|-----------------|------------------------------|
| PF-001          | FR-012         | A-02            | "Quickly" used without metric|

**Preparation Rate Guidelines:**

| Artifact Type              | Maximum Rate            |
|----------------------------|-------------------------|
| Functional requirements    | 20 requirements per hour|
| Non-functional requirements| 15 requirements per hour|
| Data model entities        | 10 entities per hour    |
| Decision tables            | 5 tables per hour       |
| State transition models    | 3 models per hour       |

If the artifact exceeds these rates within the available preparation time, the moderator SHALL split the inspection into multiple sessions.

### Phase 3: Inspection Meeting

**Meeting Protocol:**

1. **Opening (5 min):** Moderator states the objective, confirms all participants prepared, and reviews the ground rules.

2. **Ground Rules:**
   - Focus on defect identification, not solutions
   - Critique the artifact, not the author
   - Every participant has equal voice
   - The moderator controls pacing and discussion scope
   - If a defect requires more than 2 minutes of discussion, table it for offline resolution

3. **Walkthrough (60-90 min):** The reader (or moderator) paraphrases each requirement. Inspectors raise defects. The recorder logs each defect with:
   - Defect ID
   - Requirement ID
   - Defect type (see Section 4)
   - Severity (Critical / Major / Minor)
   - Brief description

4. **Summary (10 min):** Moderator summarizes:
   - Total defects found by severity
   - Decision: Accept, Accept with minor rework, Major rework required, Re-inspect required
   - Action items assigned

**Meeting Rate Guidelines:**

| Artifact Type              | Maximum Rate             |
|----------------------------|--------------------------|
| Functional requirements    | 10 requirements per hour |
| Non-functional requirements| 8 requirements per hour  |
| Decision tables            | 3 tables per hour        |

### Phase 4: Rework

**Author responsibilities:**
1. Address every defect in the defect log
2. For each defect, record:
   - The correction made
   - The rationale (if the defect was rejected, document why)
3. Update the requirements artifact with corrections
4. Submit the corrected artifact and defect resolution log to the moderator

### Phase 5: Follow-Up

**Moderator responsibilities:**
1. Verify every defect has been addressed (corrected or justified rejection)
2. If the inspection decision was "Re-inspect," schedule a new inspection
3. If the decision was "Accept with minor rework," verify corrections without a full meeting
4. Close the inspection and archive all artifacts

---

## 4. Defect Classification

### 4.1 Defect Types

| Type          | Code | Definition                                                   |
|---------------|------|--------------------------------------------------------------|
| Missing       | MI   | Information required by the checklist is absent              |
| Wrong         | WR   | Information is present but incorrect                          |
| Ambiguous     | AM   | Information can be interpreted in more than one way          |
| Inconsistent  | IN   | Information contradicts another part of the artifact         |
| Extraneous    | EX   | Information is present but not needed (gold-plating)         |
| Untestable    | UT   | No deterministic test can be written for the requirement     |

### 4.2 Severity Levels

| Severity  | Definition                                             | Action Required           |
|-----------|--------------------------------------------------------|---------------------------|
| Critical  | Prevents correct implementation or creates compliance risk | Must fix before downstream work |
| Major     | Causes ambiguity or gaps that will result in rework    | Must fix before baselining|
| Minor     | Cosmetic or style issue with no functional impact      | Fix before final release  |

---

## 5. Inspection Metrics

### 5.1 Core Metrics

| Metric                | Formula                                                | Target              |
|-----------------------|--------------------------------------------------------|---------------------|
| Defect Density        | $\frac{TotalDefects}{TotalRequirements}$               | < 0.5 defects/req   |
| Critical Defect Rate  | $\frac{CriticalDefects}{TotalRequirements} \times 100$ | < 2%                |
| Preparation Rate      | $\frac{RequirementsReviewed}{PreparationHours}$        | <= 20 req/hr        |
| Meeting Rate          | $\frac{RequirementsReviewed}{MeetingHours}$            | <= 10 req/hr        |
| Inspection Efficiency | $\frac{DefectsFound}{TotalInspectionEffort(hrs)}$      | > 5 defects/hr      |

### 5.2 Process Improvement Signals

| Signal                              | Indicates                                      | Action                           |
|-------------------------------------|-------------------------------------------------|----------------------------------|
| Defect density > 1.0                | Artifact is not ready for inspection            | Return to author for major rework|
| Critical defect rate > 5%           | Fundamental requirements engineering problems   | Escalate to project management   |
| Preparation rate exceeded           | Inspectors were rushed; defects may be missed   | Reduce scope or add sessions     |
| Very low defect density (< 0.05)    | Either high quality or insufficient preparation | Verify preparation thoroughness  |

---

## 6. Inspection Decision Criteria

| Decision                  | Criteria                                                      |
|---------------------------|---------------------------------------------------------------|
| Accept                    | Zero critical defects, fewer than 3 major defects             |
| Accept with minor rework  | Zero critical defects, 3-5 major defects, all correctable     |
| Major rework required     | 1-2 critical defects or more than 5 major defects             |
| Re-inspect required       | 3+ critical defects or defect density > 1.0                   |

---

## 7. Inspection Checklist

- [ ] Inspection package distributed 48+ hours before the meeting
- [ ] All inspectors completed individual preparation
- [ ] Preparation rates were within guidelines
- [ ] Meeting duration did not exceed 2 hours
- [ ] Meeting rates were within guidelines
- [ ] All defects logged with type, severity, and description
- [ ] Inspection decision recorded with rationale
- [ ] Rework completed and verified by moderator
- [ ] Metrics calculated and archived for process improvement

---

**Last Updated:** 2026-03-07
