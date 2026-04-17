# Phase 7 — AI Intelligence Module

## 11.1 Overview

Phase 7 is a contract extension that activates after Phases 1–6 are fully operational and BIRDC has accumulated at least 12 months of production records, quality inspection results, cooperative farmer delivery history, and equipment service logs. This operational data is the foundation Phase 7 requires. Without it, the AI models have nothing to learn from.

Phase 7 converts BIRDC's accumulated operational data into five predictive intelligence capabilities. Each capability is described below with the business problem it solves, how BIRDC benefits, and the data readiness trigger that must be met before activation.

The Phase 7 scope is quoted as a separate lump-sum contract extension. An indicative cost addendum will be issued on request following Phase 4 go-live.

---

## 11.2 Capability 1 — Know Before You Cook: Production Yield Prediction

**Business problem:** The production team commits to an output tonnage based on the recipe and nominal input quality. When actual raw material quality differs from nominal — as it frequently does with agricultural inputs — actual yield deviates. The deviation is discovered at completion: too late to adjust.

**How BIRDC benefits:** When a production order is initiated, the system reads the quality grades (A, B, C) recorded during goods receipt for the specific batches allocated to the order and predicts the actual output tonnage before production begins. The Production Manager can adjust the batch mix, source additional raw material, or revise the committed output quantity — before the cook, not after.

**Data readiness trigger:** Activate when Phase 4 has 6 months of completed production order records with quality grade data.

**FR-AI-001** — see SRS Phase 6 Section 3.4, FR-AI-001 for full technical specification.

---

## 11.3 Capability 2 — Catch Recurring Quality Failures Before They Reach the Export Market

**Business problem:** A quality defect pattern — for example, moisture content consistently out of specification — may appear across 5 consecutive production batches before a lab analyst notices the trend. Each failed export shipment costs BIRDC in rejected goods, logistics expense, and customer relationship damage.

**How BIRDC benefits:** After each production batch is quality-graded, the system compares the result against the statistical baseline for that product and parameter using Shewhart control chart rules. When a parameter has trended outside its control limits for 2 or more consecutive batches — or a single point falls beyond 3 standard deviations — the system generates a Process Alert for the Quality Manager and Production Director. Intervention occurs at the third batch rather than the fifth.

**Data readiness trigger:** Activate when Phase 4 has 3 months of quality inspection records for baseline computation.

**FR-AI-002** — see SRS Phase 6 Section 3.4, FR-AI-002 for full technical specification.

---

## 11.4 Capability 3 — Plan Raw Material Supply 3 Months Out

**Business problem:** BIRDC's production plan depends on a steady supply of bananas from cooperative farmers. Seasonal variation, weather events, and market conditions cause supply shocks that leave the factory under-utilised or unable to fulfil export orders already committed.

**How BIRDC benefits:** Based on 3 years of cooperative delivery records and historical seasonal patterns, the system generates a quarterly Farmer Supply Forecast per cooperative: expected delivery volume, confidence interval, and recommended advance purchase order quantities. Procurement can issue advance commitments to cooperatives based on the forecast, incentivising supply stability and enabling better production planning.

**Data readiness trigger:** Activate when Phase 3 has 12 months of cooperative delivery records.

**FR-AI-003** — see SRS Phase 6 Section 3.4, FR-AI-003 for full technical specification.

---

## 11.5 Capability 4 — Predict Equipment Maintenance Windows, Not Emergency Repairs

**Business problem:** Factory equipment fails during production runs committed to export shipment deadlines. Emergency repairs cost 3–5× more than scheduled maintenance. Downtime during a committed production run is more costly still.

**How BIRDC benefits:** The system tracks equipment runtime hours per production order and maintenance service records. When a machine's accumulated runtime approaches its historical average service interval — specifically when the Maintenance Proximity Score exceeds 80% — the Maintenance Manager receives an alert with the asset name, current score, and recommended service window. Maintenance is scheduled around production commitments rather than disrupting them.

**Data readiness trigger:** Activate when Phase 4 has 6 months of equipment service log data for each tracked asset.

**FR-AI-004** — see SRS Phase 6 Section 3.4, FR-AI-004 for full technical specification.

---

## 11.6 Capability 5 — Optimise Production Scheduling Against Export Demand

**Business problem:** Export orders arrive with committed delivery dates. BIRDC must backward-plan from the shipment date through production, QC, packaging, and logistics. When multiple export orders overlap in a constrained production calendar, conflicts go undetected until it is too late to renegotiate dates or source additional capacity.

**How BIRDC benefits:** When a new export order is entered, the system immediately runs a Production Feasibility Check: it compares the required production tonnage against available factory capacity in the 8-week window preceding the delivery date, accounting for committed production already scheduled and the Farmer Supply Forecast for raw material availability. If a capacity gap is detected, the system flags it at order entry — before confirmation — with the gap size and three resolution options: advance the production start date, request supplementary cooperative delivery, or negotiate the shipment date.

**Data readiness trigger:** Activate when FR-AI-003 (supply forecasting) is operational and the production schedule module has at least 2 months of order history.

**FR-AI-005** — see SRS Phase 6 Section 3.4, FR-AI-005 for full technical specification.

---

## 11.7 Phase 7 Scope Summary

| Capability | FR Reference | Data Trigger | Estimated Activation |
|---|---|---|---|
| Production Yield Prediction | FR-AI-001 | Phase 4 operational + 6 months production data | Month 30 post-contract |
| Quality Defect Pattern Detection | FR-AI-002 | Phase 4 operational + 3 months QC data | Month 27 post-contract |
| Farmer Supply Forecasting | FR-AI-003 | Phase 3 operational + 12 months delivery data | Month 30 post-contract |
| Predictive Equipment Maintenance | FR-AI-004 | Phase 4 operational + 6 months equipment logs | Month 30 post-contract |
| Export Demand Intelligence | FR-AI-005 | FR-AI-003 operational + 2 months order history | Month 32 post-contract |

Phase 7 is quoted as a separate lump-sum contract extension. Cost addendum issued on request following Phase 4 go-live.
