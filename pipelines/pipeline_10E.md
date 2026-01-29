# Appendix 10E: Validation Gates (The "Pass/Fail" Criteria)
**Role:** Defining success for the Morgan Board.

## 1. Gate 1: Swelling Resistance (The Problem)
*   **Test:** **Accelerated Hydrothermal Aging (AHA)**.
*   **Condition:** Autoclave @ 120°C / 2 bar vapor / 48 Hours. (Simulates >2000h operational life).
*   **Metric:** **Anisotropic Swelling ($Z_{\perp}$)**.
    *   *Reasoning:* We only care about expansion *perpendicular* to pressing, as this is what jams the holder.
*   **Target:** $< 0.1\%$ dimensional change.

## 2. Gate 2: Tribological Safety (The Risk)
*   **Test:** Dynamic Run (Pin-on-Disc).
*   **Load:** 20 A/cm² (Overload).
*   **Metric:** Friction Coefficient ($\mu$).
*   **Target:** **$\mu < 0.25$**.
    *   *Logic:* If the brush is too dry (hydrophobic), friction spikes. If $\mu > 0.25$, the formulation is rejected regardless of swelling performance.
