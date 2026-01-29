# Pipeline Version 4.0 (Collaborative R&D Strategy)

**Context:** Corporate R&D Project (Summer School Scenario)
**Constraints:** Unlimited Funds, Pure I+D Focus.
**Core Philosophy:** Prioritization of the **Team Consensus Workflow** (`pipeline_colegas.md`). We respect the collective intelligence of the team, moving from broad screening to focused optimization.

---

## Phase 1: Parameter Identification (Step 1)
**Goal:** Define the four critical variables that influence the swelling of the MG1157 brush.
Based on technical analysis (`brian.md`, `colegas_2.md`), the four selected parameters are:
1.  **Binder Type/Chemistry:** (e.g., Phenolic vs. Pitch vs. Modified) - The primary source of swelling.
2.  **Metal/Graphite Ratio:** (Current: ~50% Ag) - Influences thermal expansion and mechanical structure.
3.  **Porosity/Compaction Pressure:** Controlled during the "Shaping" and "Mixing" stages.
4.  **Hydrophobic Additives:** (e.g., Silanes/PTFE) - A new variable to actively repel moisture.

## Phase 2: Screening Experiments - OFAT (Steps 2 & 3)
**Goal:** Determine which of the four parameters have the most significant impact on swelling.
**Methodology:** **One-Factor-At-a-Time (OFAT)**
*   **Action:**
    *   Run distinct experimental sets where only **one** variable is modified while keeping the other three constant.
    *   *Example:* Keep Metal, Porosity, and Additives constant; test 3 different Binders.
*   **Analysis:**
    *   Perform statistical analysis (ANOVA/Regression) on the results.
    *   **Output:** A ranking of the parameters by their statistical significance regarding dimensional change (swelling).

## Phase 3: Critical Optimization - The "2-Variable Matrix" (Steps 4 & 5)
**Goal:** Deep optimization of the two most dominant factors.
**Methodology:** **Factorial Design / Response Surface**
*   **Selection:** Pick the top **2 parameters** from Phase 2 (e.g., *Hypothetically*: Binder Type and Metal Ratio).
*   **Action:**
    *   Create a full experimental matrix varying these two parameters simultaneously across a range of values.
    *   Since funds are unlimited, we maximize resolution (more data points).
*   **Target Output:** A 3D Surface Graph or Contour Plot:
    *   **X-Axis:** Critical Variable 1
    *   **Y-Axis:** Critical Variable 2
    *   **Z-Axis:** Swelling (Dimensional Change %)

## Phase 4: Decision & Final Validation (Step 6)
**Goal:** Select the optimal formulation and validate operational viability.
**Decision Logic:**
*   Identify the region on the Phase 3 graph where **Swelling is minimized** (approaching zero or within tolerance).
*   **Constraint Check:** Ensure this "low swelling" region does not violate critical specs:
    *   *Conductivity:* Must maintain ~18 A/cm².
    *   *Friction:* Must maintain suitable tribological properties (no abrasive running).
*   **Deliverable:** The "Golden Prototype" specification ready for the hypothetical production line.

---
**Alignment Check:**
*   [x] Respects `pipeline_colegas.md` (6-step flow).
*   [x] Respects `colegas_2.md` (MG1157 specifics, 4D matrix concept).
*   [x] Respects `guidelines.md` (Company context, R&D focus).
