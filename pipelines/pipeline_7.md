# Pipeline Version 7.0 (The "Morgan-Totankako" Benchmark Protocol)

**Company:** Morgan Advanced Materials (Electrical Carbon Division)
**Project:** MG1157-NextGen (Wind Turbine Generator Brush)
**Status:** **FINAL EXECUTION PLAN**
**Context:** Integrated CEO Mandates (Tribo-Safety) + CTO Technical Revisions (Solid Lubes + Anisotropy).

---

## Phase 1: The "5-Variable" Input Space
**Goal:** Define the comprehensive variable set, now including Solid Lubrication to prevent dry-running.

### Variable A: Binder Chemistry (Hydrophobicity)
*   **Candidates:** Phenolic (Baseline) vs. **Coal Tar Pitch** vs. **Furan Resin**.

### Variable B: Carbon Source (Structure)
*   **Candidates:** Natural Flake Graphite vs. **Synthetic Electro-Graphite** (High Density).

### Variable C: Metal Content (Thermal Balance)
*   **Range:** 30% to 70% Silver (Ag).

### Variable D: Porosity Control (Expansion Buffer)
*   **Range:** 5% to 20% Open Porosity (Controlled via PEG).

### Variable E: Solid Lubricant (Tribo-Stabilizer) - **NEW**
*   **Material:** **Molybdenum Disulfide (MoS₂)** (Grade: Technical Fine).
*   **Range:** **0.5% to 5.0% wt**.
*   *Purpose:* To replace water vapor lubrication in hydrophobic formulations, preventing ring destruction (as per CEO mandate).

---

## Phase 2: High-Throughput Screening (The "Anisotropic" Filter)
**Timeline:** Weeks 1-4
**Goal:** Identify the primary drivers of *Directional* Swelling.

*   **Experimental Design:** Taguchi L18 Orthogonal Array (Efficient screening of 5 factors).
*   **Critical Measurement Protocol:**
    *   **Dimension $Z_{\perp}$ (Perpendicular):** Expansion *against* the pressing direction (The "Killer" dimension that jams the holder).
    *   **Dimension $Z_{\parallel}$ (Parallel):** Expansion *along* the pressing direction (Harmless lengthening).
    *   *Pass Criteria:* Only formulations where $Z_{\perp} < 0.2\%$ proceed.

---

## Phase 3: Critical Optimization & Accelerated Aging
**Goal:** Find the true equilibrium point (not just the 1-week point).

*   **Protocol:** **Accelerated Hydrothermal Aging (AHA)**
    *   *Equipment:* Pressure Vessel (Autoclave).
    *   *Condition:* 120°C / 2 bar Water Vapor Pressure.
    *   *Duration:* 48 Hours (Equivalent to >2000 hours at standard 60°C/95%RH based on Arrhenius scaling).
    *   *Reference:* Method derived from Patent EP 1 780 876 A1.

---

## Phase 4: The Final 3D Visualizations
**Goal:** The CEO's Decision Dashboard.

We will generate **Comparative 4D Surface Plots** (3 Spatial Axes + Color):

1.  **X-Axis:** Metal Content (Ag %)
2.  **Y-Axis:** Porosity %
3.  **Z-Axis (Vertical):** **Swelling $Z_{\perp}$ (Perpendicular)**
    *   *Visual Target:* Flat valley near Z=0.
4.  **Color Scale (The Safety Overlay):** **Friction Coefficient ($\mu$)**
    *   *Green:* $\mu < 0.15$ (Ideal)
    *   *Yellow:* $0.15 < \mu < 0.25$ (Acceptable)
    *   *Red:* $\mu > 0.25$ (FAIL - Dry Running Risk)

**Comparative Series:**
*   **Plot A:** Phenolic + Natural Graphite (Baseline).
*   **Plot B:** Pitch + Synthetic Graphite + MoS₂ (The Solution).

---

## Phase 5: Production & Hardness Validation
**Goal:** Validate performance without artificial hardness constraints.

*   **Hardness Target:** **UNCONSTRAINED.** We will accept Shore < 30 if wear rates are low.
*   **Rig Test:** 20 A/cm² Overload Test (500 hours) measuring brush wear rate (mm/1000h) and commutator roughness ($R_a$).

---
**Signed:**
Head of Pipeline Design
Morgan Advanced Materials
