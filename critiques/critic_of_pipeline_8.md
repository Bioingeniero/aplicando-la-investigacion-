# CTO Technical Review of Pipeline 8.0

**To:** Head of Pipeline Design
**From:** Chief Technology Officer (CTO)
**Date:** 2026-01-22
**Subject:** CRITIQUE - Operational Details Missing for "Process Levers"

## Executive Summary
I have reviewed `pipeline_8.md`. The strategy is sound, and the "Process-First" approach is approved. However, the **execution detail is dangerously thin**.

You cannot simply tell a technician to "Test Furan Resin" or "Press at 350 MPa" without a specific protocol. Each of these 4 parameters requires its own dedicated investigation track with safety limits, equipment settings, and specific chemical handling procedures.

## Specific Gaps & Requirements for Pipeline 9.0

### 1. Lever 1: Binder Chemistry - The "Rheology" Gap
*   **Critique:** You list "Pitch" and "Furan" as if they are drop-in replacements for Phenolic. They are not.
*   **Requirement:** We need a protocol for **Viscosity Matching**. If you change the binder, you change the mixing torque.
*   **Appendage Needed:** **Appendix A: Binder Characterization Protocol.** (Viscosity, Softening Point, Coking Value).

### 2. Lever 2: Pressing Pressure - The "Lamination" Risk
*   **Critique:** You set a range of 150-350 MPa. At 350 MPa, an Isostatic Press can crush the green body or cause internal lamination cracks upon release (spring-back).
*   **Requirement:** We need a specific **Pressing Cycle Definition** (Ramp-up rate, Dwell time, Decompression rate). Decompression must be slow to prevent cracking.
*   **Appendage Needed:** **Appendix B: Isostatic Pressing Cycle Definition.**

### 3. Lever 3: Carbonization Temperature - The "Oxidation" Risk
*   **Critique:** "Push >950°C." If you do this with Furan resin without a perfect inert atmosphere, you will burn the brush to ash.
*   **Requirement:** Define the **Heating Profile** (°C/hour) and the **Atmosphere Control** (Nitrogen/Argon flow rates, Oxygen ppm limits).
*   **Appendage Needed:** **Appendix C: Thermal Treatment Profile.**

### 4. Lever 4: Impregnation - The "Vacuum" Variable
*   **Critique:** "Dip it in Silane." It's not a dip; it's a Vacuum-Pressure Impregnation (VPI).
*   **Requirement:** Define the VPI cycle: Vacuum level (mbar), Time under vacuum, Pressure injection (bar), and Curing temperature for the Silane/Oil.
*   **Appendage Needed:** **Appendix D: VPI (Vacuum Pressure Impregnation) Protocol.**

## Directive for Pipeline 9.0
Do not just update the summary. I want **Pipeline 9.0** to be the "Master Document" with **4 Technical Appendices** attached.

*   **Structure:**
    *   Main Body: Strategy & Logic (as in V8.0).
    *   **Appendix A:** Binder Protocol.
    *   **Appendix B:** Pressing Protocol.
    *   **Appendix C:** Carbonization Protocol.
    *   **Appendix D:** Impregnation Protocol.

This ensures that when we hand this to the lab manager, they don't have to ask "How fast do I heat this?" or "How much vacuum do I pull?"

**Signed,**
CTO
Morgan Advanced Materials
