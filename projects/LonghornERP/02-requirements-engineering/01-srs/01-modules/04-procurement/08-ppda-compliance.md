# PPDA Compliance

## 8.1 Procurement Method Selection

**FR-PROC-046** — When a user creates a PO for a government or parastatal tenant, the system shall evaluate the estimated procurement value against configurable PPDA method thresholds `[CONTEXT-GAP: GAP-006 — current PPDA threshold values for micro, small, restricted, and open tender methods]` and enforce the minimum procurement method required by law.

**FR-PROC-047** — The system shall support the following PPDA procurement methods as selectable options on PRs and POs: direct procurement, quotation solicitation, restricted tender, and open tender; the method label shall be printed on the LPO document.

## 8.2 PPDA Reports

**FR-PROC-048** — The system shall provide a PPDA procurement register report listing all POs within a specified date range with columns: PO number, supplier name, supplier TIN, procurement method, estimated value, actual value, and award date; the report shall be exportable as XLSX for submission to PPDA.

**FR-PROC-049** — When a procurement transaction is processed using the open tender method, the system shall store the tender advertisement reference, tender committee member names, evaluation report reference, and best-evaluated bidder score as mandatory fields before PO issuance.

## 8.3 Evaluation Committee Records

**FR-PROC-050** — The system shall maintain an evaluation committee record per tender exercise, capturing: committee members (name, role, department), evaluation criteria (quality score weight and price score weight), individual scores per bidder per criterion, and the final combined score.

**FR-PROC-051** — Evaluation committee records shall be read-only after PO award and shall be retained for a minimum of 7 years per PPDA record-keeping requirements.
