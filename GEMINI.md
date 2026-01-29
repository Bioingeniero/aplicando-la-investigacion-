# Directory Overview

This directory contains documentation and guidelines for a critical R&D project at **Morgan Advanced Materials (Electrical Carbon Division)**. The project focuses on upgrading the **Grade MG1157** phase brush to eliminate **loss of contact due to swelling** in wind turbine generators.

## Key Files

*   **`guidelines.md`**: The central document outlining the project's mandates. It specifies:
    *   The goal is the **pipeline** creation for the next-generation brush.
    *   The operational context is **Morgan Advanced Materials** (Corporate R&D).
    *   **Constraints:** The pipeline focuses solely on **R&D (I+D)** with **unlimited funds**.
*   **`colegas_3.md` (TOP PRIORITY):** Defines the team's specific execution plan for the "Summer School" project.
    *   **Diagnosis:** Internal Swelling caused by Binder/Process interaction.
    *   **Methodology:** 4-Phase DOE (Variables -> Sensitivity Analysis -> Factorial Design -> Pareto Selection).
    *   **Tools:** Explicit use of **Jupyter (Python)** for ANOVA and Pareto analysis.
    *   **Variables:** Binder Type, Pressing Pressure, Carbonization Temp, Impregnation.
*   **`pptx_structure.md`:** The blueprint for the final presentation.
    *   **Section 1:** Problem Definition (Internal Swelling).
    *   **Section 2:** Theoretical Framework (4 Critical Mfg Stages).
    *   **Section 3:** Experimental Proposal (DOE + Jupyter Analysis).
*   **`brian.md`**: Detailed breakdown of our manufacturing process (Stages 0-8), highlighting the role of binders and porosity in swelling.
*   **`colegas_2.md`**: Technical context defining the specific material properties of our **MG1157** grade.
*   **`pipeline_colegas.md`**: The core experimental workflow proposed by the engineering team (6-step optimization).

## Technical Context (Updated 2026-01-22)

*   **Company:** Morgan Advanced Materials.
*   **Target Product:** Grade MG1157 (Metal-Graphite: ~50% Ag, Carbon, Binder).
*   **Core Problem:** Swelling due to thermodynamic equilibrium (moisture absorption/thermal expansion) leading to mechanical lock-up.
*   **Alignment:** The project strictly follows the **4-Phase DOE methodology** defined in `colegas_3.md` and the **Presentation Structure** defined in `pptx_structure.md`.
*   **Strategy:** Optimization of 4 Process Levers (Binder, Pressure, Temperature, Impregnation) utilizing Python/Jupyter for all statistical validation.

## Usage

This directory serves as the root for project planning and strategy. Future documents and artifacts should align with the corporate pipeline principles defined in `guidelines.md`.
