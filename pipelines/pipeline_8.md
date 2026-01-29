# Pipeline Version 8.0 (The "Process Optimization" Protocol)

**Company:** Morgan Advanced Materials (Electrical Carbon Division)
**Project:** MG1157-NextGen
**Strategy:** "Tune the Process, Don't Reinvent the Material."
**Objective:** Eliminate Swelling via Manufacturing Controls.

---

## Phase 1: The "4-Lever" Input Space
**Goal:** Optimize the manufacturing window to close porosity and reject water chemically.

### Lever 1: Binder Chemistry (The Chemical Shield)
*   **Baseline:** Standard Phenolic Novolac.
*   **Challenger 1:** **Coal Tar Pitch** (Naturally hydrophobic aromatic structure).
*   **Challenger 2:** **Furan Resin** (High char yield, low shrinkage).

### Lever 2: Pressing Pressure (The Mechanical Seal)
*   **Mechanism:** Higher compaction density reduces the *volume* of open pores available for water.
*   **Range:** **150 MPa to 350 MPa** (Isostatic).
*   *Constraint:* Must monitor against lamination cracks at high pressure.

### Lever 3: Carbonization Temperature (The Structural Seal)
*   **Mechanism:** Controls binder coke shrinkage and lattice ordering (crystallinity).
*   **Range:** **800°C to 1100°C**.
*   *Target:* Push >950°C to maximize hydrophobicity of the binder coke.

### Lever 4: Impregnation/Coating (The Final Barrier)
*   **Mechanism:** Post-process sealing of surface porosity.
*   **Candidates:**
    *   **Type A:** Hydrophobic Silane (Deep penetration).
    *   **Type B:** **Lubricating Oil** (Synthetic Perfluoropolyether - PFPE). *Dual function: Hydrophobicity + Lubrication.*

---

## Phase 2: High-Throughput Screening (Anisotropic)
**Experimental Design:** Full Factorial on Binder (3) x Impregnation (3) + DOE on Pressure/Temp.
**Critical Metric:**
*   **Swelling $Z_{\perp}$ (Perpendicular):** Target $< 0.1\%$.
*   **Test Protocol:** Accelerated Hydrothermal Aging (120°C / 2 bar / 48h).

---

## Phase 3: The "Safety Net" Validation (Tribology)
**Goal:** Ensure the "Dry Brush" risk is managed by the Impregnation.

*   **Metric:** Friction Coefficient ($\mu$).
*   **Success Criteria:**
    *   If $\mu < 0.25$: Pass.
    *   If $\mu > 0.25$: Fail -> Switch Impregnation to Type B (Lubricating Oil).

---

## Phase 4: The CEO's Decision Dashboard (Revised 3D Plots)
**Visual Output:** Comparative 3D Surface Plots for each Binder System.

1.  **X-Axis:** Pressing Pressure (MPa).
2.  **Y-Axis:** Carbonization Temp (°C).
3.  **Z-Axis:** **Swelling $Z_{\perp}$**.
4.  **Color Overlay:** Friction Coefficient ($\mu$).

*Decision Logic:* Find the Pressure/Temp window where Swelling is zero (Valley) and Color is Green/Yellow ($\mu < 0.25$).

---
**Signed:**
Head of Pipeline Design
Morgan Advanced Materials
