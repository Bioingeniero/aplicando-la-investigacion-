# Appendix 11A: Data Strategy & Experimental Design (The "Analysis" Engine)
**Presentation Section:** 3. Experimental Proposal (Analysis Methodology)
**Slide Mapping:** Slides 15-17 (Sensitivity, Factorial, Pareto)

## 1. The Data Workflow (Jupyter/Python)
We strictly follow the team's consensus flow:

*   **Step 1: Raw Data Ingestion**
    *   Standardized CSV logs from the Lab (Dimensions, Weights, Friction).
*   **Step 2: Sensitivity Analysis (Phase 2)**
    *   *Goal:* Identify density drivers.
    *   *Tool:* **ANOVA (Analysis of Variance)** via `scipy.stats`.
    *   *Visual:* Correlation Matrix Heatmap.
*   **Step 3: Response Surface (Phase 3)**
    *   *Goal:* Map interactions between Pressure, Temp, and Swelling.
    *   *Tool:* 3D Plotting via `matplotlib.pyplot` / `plotly`.
*   **Step 4: Decision Support (Phase 4)**
    *   *Goal:* Select the "Golden Recipe".
    *   *Visual:* **Pareto Chart** ranking the 4 Process Levers by impact.

## 2. Infrastructure
*   **Repository:** `notebooks/analysis_v11.ipynb`
*   **Libraries:** `pandas`, `numpy`, `statsmodels`, `seaborn`.
