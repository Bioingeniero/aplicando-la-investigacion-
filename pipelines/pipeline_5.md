# Pipeline Version 5.0 (High-Precision R&D Execution Plan)

**To:** Chief Technology Officer (CTO)
**From:** Head of Pipeline Design
**Date:** 2026-01-22
**Context:** Response to Critical Review (V4.0). Implements rigorous protocols, defined ranges, and specific DoE frameworks using our unlimited R&D budget.

---

## Phase 1: Parameter Definition & Bounds (The "Input Space")
**Goal:** Define specific chemical candidates and numerical ranges for the 4 critical parameters.

1.  **Binder Chemistry (Variable A):**
    *   *Standard:* Phenolic Resin (Novolac hexamine-cured).
    *   *Candidate 1:* **Coal Tar Pitch** (High softening point: 110°C, CAS: 65996-93-2) - Hydrophobic baseline.
    *   *Candidate 2:* **Modified Phenolic** (Epoxy-modified) - Enhanced moisture resistance.
    *   *Candidate 3:* **Furan Resin** (High char yield) - Low thermal expansion.

2.  **Metal/Graphite Ratio (Variable B):**
    *   *Current:* 50% Ag (by weight).
    *   *Test Range:* **30% to 70% Ag**.
    *   *Justification:* Wide range to capture the percolation threshold transition.

3.  **Porosity / Compaction (Variable C):**
    *   *Target Pores:* 5% to 25% (Open Porosity).
    *   *Control Mechanism:* **Isostatic Pressing Pressure** (100 MPa to 300 MPa).
    *   *Decoupling Strategy:* We will use sacrificial pore-formers (Polyethylene Glycol - PEG) that burn off during sintering. This allows us to vary porosity *independent* of compaction pressure/density.

4.  **Hydrophobic Additives (Variable D):**
    *   *Candidate 1:* **Trimetoxysilane** (CAS: 2487-90-3) - Surface treatment post-sintering.
    *   *Candidate 2:* **PTFE Micro-powder** (Particle size < 5µm).
    *   *Concentration Range:* **0.1% to 2.0% wt**.

---

## Phase 2: OFAT Screening Protocols (Standard Operating Procedure)
**Goal:** Isolate sensitivity with high statistical power.

*   **Sample Size:** **n=10** samples per data point (Total 120 samples for screening).
*   **Swelling Measurement Protocol (The "Climate Stress Test"):**
    *   *Equipment:* Weiss Technik ClimeEvent C/180/40/3.
    *   *Standard:* Modified **ASTM C559** (Bulk Density) & **IEC 60413** (Swelling).
    *   *Cycle:*
        1.  Dry at 110°C for 24h (Baseline).
        2.  Soak at **95% RH / 60°C** for **168 hours (1 week)**.
        3.  Measure dimensional change ($\Delta L, \Delta W, \Delta H$) using high-precision laser micrometers (Keyence LS-9000).
*   **Analysis:** ANOVA (Analysis of Variance) to determine P-values. Significance threshold: $\alpha = 0.01$.

---

## Phase 3: Critical Optimization (Factorial Design)
**Goal:** Map the response surface of the top 2 variables.
**Assumption:** Let's assume **Binder Type** and **Metal Ratio** are the winners.

*   **DoE Framework:** **Central Composite Design (CCD)** with Face-Centered axial points.
*   **Resolution:** 5 Levels per factor.
    *   *Metal Ratio Levels:* 30%, 40%, 50%, 60%, 70%.
    *   *Binder Blends:* 100% Phenolic -> 50/50 -> 100% Pitch.
*   **Response Variables (The "Triple Constraint"):**
    1.  $Y_1$: **Dimensional Swelling (%)** (Minimize).
    2.  $Y_2$: **Electrical Resistivity ($\mu\Omega\cdot m$)** (Target: $< 5.0$, ideally $\approx 3.30$).
    3.  $Y_3$: **Shore Hardness** (Target: Maintain within ±10% of MG1157).

---

## Phase 4: Dynamic Validation Under Load (The "Real World" Check)
**Goal:** Prove performance under Joule heating and tribological stress.

*   **Equipment:** Custom **Brush-on-Ring Tribometer** (instrumented slip ring rig).
*   **Test Protocol:**
    *   *Current Density:* **20 A/cm²** (Overload test, 110% of rated 18 A/cm²).
    *   *Speed:* 40 m/s (Rated speed).
    *   *Duration:* 500 continuous hours.
    *   *Atmosphere:* Chamber controlled at 90% RH (Simulating worst-case wind turbine nacelle).
*   **Failure Criteria:**
    *   Sudden voltage drop (loss of contact).
    *   Sparking intensity > Level 2.
    *   Physical sticking in the brush holder (simulated with standard tolerance holder).

## Safety & Handling
*   **Silanes:** All handling in **Class II Biosafety Cabinet** or Fume Hood. Use of nitrile gloves and respirators (ABEK1 filter).
*   **Silver Powder:** Dust explosion protocols active. Grounding straps required for all powder mixing.

---
**Verdict:** Ready for execution. The "Black Box" is now transparent.
