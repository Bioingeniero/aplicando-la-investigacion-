# Appendix 10A: Data Strategy & Experimental Design (The "Brain")
**Role:** Defines the statistical engine of the pipeline (Jupyter/Python Integration).

## 1. Experimental Methodology (4 Phases)
We strictly follow the team's consensus flow:

*   **Phase 1: Variable Definition (The 4 Levers)**
    1.  Binder Type (Categorical: Phenolic, Pitch, Furan).
    2.  Pressing Pressure (Numerical: 150 - 350 MPa).
    3.  Carbonization Temp (Numerical: 800 - 1100°C).
    4.  Impregnation (Categorical: None, Silane, PFPE Oil).

*   **Phase 2: Sensitivity Analysis (Screening)**
    *   *Design:* Fractional Factorial ($2^{4-1}$) or Taguchi L9.
    *   *Goal:* Filter noise. Identify which of the 4 variables actually drives Density and Swelling.
    *   *Tool:* **Python (Statsmodels/SciPy) -> ANOVA Calculation.**

*   **Phase 3: Full Factorial Optimization**
    *   *Design:* Central Composite Design (CCD) on the top 2-3 significant variables.
    *   *Goal:* Map the Response Surface (3D Plots).
    *   *Tool:* **Python (Matplotlib/Plotly) -> 3D Surface Generation.**

*   **Phase 4: Decision Support**
    *   *Tool:* **Python -> Pareto Chart Generation.**
    *   *Output:* A clear ranking of effects to justify the final formulation to the Board.

## 2. Digital Infrastructure
*   **Jupyter Notebooks:** All raw lab data (Dimensions, Weights, Friction Logs) is fed directly into a standardized `.ipynb` template for automated processing.
