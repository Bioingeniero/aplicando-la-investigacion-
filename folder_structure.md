# Folder Structure Documentation

This document provides a comprehensive overview of the directory structure and file organization for the **Morgan Advanced Materials (Grade MG1157 Upgrade)** R&D project.

## 1. Root Directory: Project Strategy & Management

The root directory contains the primary documentation, strategic planning, and presentation generation tools.

### Core Documentation
*   **`GEMINI.md`**: The central context file. It defines the project goal (eliminating swelling in MG1157 brushes), the company context (Morgan Advanced Materials), and technical mandates.
*   **`guidelines.md`**: Outlines the operational constraints (Unlimited R&D funds) and strategic focus.
*   **`pptx_structure.md`**: The blueprint for the final project presentation, defining the narrative flow (Problem -> Theory -> Experiment).
*   **`folder_structure.md`**: This file, explaining the organization of the project.
*   **`log.md`**: A chronological record of actions, decisions, and updates.
*   **`guia_basica.ipynb`**: A basic guide notebook (likely for onboarding or tool usage).

## 2. Organized Subdirectories

To ensure navigability, the project files are organized into specific context folders:

### `communications/` (Stakeholder Management)
Contains formal correspondence, mandates, and approval documents from executive leadership.
*   **`CEO_Approval_and_Mandates.md`**: Consolidated mandates.
*   **`CEO_to_Head.md`, `CEO_to_CTO.md`, `CTO_2_CEO.md`**: Strategic directives chain.
*   **`answer_to_CEO.md`**: Response strategies.

### `pipelines/` (Iterative R&D Workflows)
Contains the evolutionary history of the experimental plan.
*   **`pipeline_0.md` to `pipeline_11E.md`**: Sequential versions of the R&D pipeline.
*   **`pipeline_colegas.md`**: The core workflow agreed upon with the engineering team.
*   **`left_behind_7_to_8.md`**: Documentation of discarded variables.
*   **`pipeline2v1.md`, `pipeline3_esp.md`**: Variant versions.

### `critiques/` (Review & Feedback)
Contains critical analyses of specific pipeline versions used to drive the iterative process.
*   **`critic_of_pipeline*.md`**: Reviews from various perspectives (CEO, CTO, Investor).

### `technical_context/` (Material & Process Base)
Contains the foundational technical data, specifications, and team notes.
*   **`colegas_3.md` (Key File)**: Defines the execution plan (4-Phase DOE).
*   **`colegas_2.md`**: Technical specifications for MG1157.
*   **`colegas.md`**: General team notes/context.
*   **`brian.md`**: Manufacturing process analysis.
*   **`Patente_EP1780876A1.md`**: IP Reference material.
*   **`Documento de trabajo con los colegas.pdf`**: Original team documentation.

## 3. Presentation Automation

This project includes tools to automate the generation of HTML-based presentation slides.

*   **`generate_slides.py`**: A Python script that reads markdown content and generates HTML slides.
*   **`scripts_for_html/`**: A directory containing the raw Markdown text for each slide (e.g., `script_for_diapositiva_1.md`).
*   **`htmls/`**: The output directory containing the generated HTML presentation slides.
*   **`PPT.ipynb`, `PPT2.ipynb`, `para_presentar.ipynb`**: Jupyter notebooks used for drafting or presenting content interactively.

## 4. Other Directories & Files

*   **`TEST/`**: A testing directory for experimental scripts or file generation.
*   **`TEST.ipynb`**: A notebook for testing purposes.
*   **`.venv/`**: The Python virtual environment directory.
*   **`.ipynb_checkpoints/`**: Auto-generated Jupyter notebook checkpoints.

## 5. Miscellaneous Assets
*   **`puppy.jpg`**: Asset file (image).
*   **`cubo_rotatorio.html`**: An HTML visualization artifact.
