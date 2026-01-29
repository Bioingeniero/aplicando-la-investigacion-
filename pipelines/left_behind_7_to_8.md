# Deprecated Project Elements: Pipeline 7.0 -> 8.0 Transition

**Date:** 2026-01-22
**Status:** Archived for Future Reference
**Reason for Removal:** Strategic simplification to focus on "Process Levers" rather than material reformulation.

---

## 1. Excluded Variables (The "Material Re-Engineering" Track)

### A. Metal Content (Ag %)
*   **Original Plan:** Sweep from 30% to 70% Silver.
*   **Reason for Removal:** Changing Silver content triggers a massive re-qualification of the brush's electrical rating (Current Density). Pipeline 8.0 keeps this constant at ~50% (Standard MG1157).

### B. Solid Lubricants (MoS₂)
*   **Original Plan:** Add 0.5% - 5.0% Molybdenum Disulfide.
*   **Reason for Removal:** Contamination risk for mixing lines. The lubrication function will now be handled by the **Impregnation Oil** (Variable 4) if needed.

### C. PEG Pore Formers
*   **Original Plan:** Use sacrificial Polyethylene Glycol to artificially tune porosity.
*   **Reason for Removal:** Too complex for standard manufacturing. Porosity will now be controlled directly by **Pressing Pressure** (Variable 2).

### D. Synthetic vs. Natural Graphite
*   **Original Plan:** Compare graphite sources.
*   **Status:** Reverted to standard MG1157 Graphite blend to isolate process variables first.

## 2. Superseded Visualizations
*   **4D Surface Plot (Metal vs. Porosity):** Since Metal is now constant, the X-Axis of the primary decision graph has changed.

---
**Note:** These elements are technically valid but strategically paused. If Pipeline 8.0 fails to solve the swelling, these variables can be reactivated.
