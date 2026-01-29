# CTO Critique of Pipeline Version 4.0

**To:** R&D Project Lead
**From:** Chief Technology Officer (CTO)
**Date:** 2026-01-22
**Subject:** CRITICAL REVIEW - Pipeline 4.0 Lacks Operational Detail

## Executive Summary
I have reviewed `pipeline_4.md`. While I appreciate the alignment with the team's consensus flow (`pipeline_colegas.md`) and the strategic focus on the MG1157 material, **this document is currently a "wish list," not an execution plan.**

You have defined *what* to do (OFAT, Factorial Design), but you have completely failed to define *how* to do it. In an R&D environment—even one with unlimited funds—reproducibility and data integrity are paramount. We cannot throw money at vague protocols.

## Specific Gaps & Requirements

### 1. Phase 1: Parameter Identification - "The What" is clear, "The Range" is missing.
*   **Critique:** You list "Binder Type" and "Metal Ratio." Good. But what are the bounds?
*   **Requirement:** Define the specific chemical candidates and numerical ranges.
    *   *Binders:* Are we testing Novolac vs. Resole? Are we sourcing Pitch from coal tar or petroleum?
    *   *Metal Ratio:* "Current ~50% Ag." What is the test range? 30-70%? 45-55%? This defines the scope of our machinery setup.
    *   *Additives:* "Silanes/PTFE." Which specific CAS numbers? What concentration % are we starting with? 0.1% or 5%?

### 2. Phase 2: OFAT Screening - Where is the "Standard Operating Procedure" (SOP)?
*   **Critique:** "Run distinct experimental sets." How? How do you manufacture a single prototype with a different binder without changing the porosity? These variables are coupled.
*   **Requirement:**
    *   **Decoupling Strategy:** Explain how you will isolate "Porosity" from "Compaction Pressure" when they are physically linked.
    *   **Sample Size:** How many samples per data point? n=3? n=10? With unlimited funds, I expect high statistical power.
    *   **Swelling Protocol:** How exactly are we measuring swelling? Is it ASTM C559? Is it a custom environmental chamber test?
        *   *Temperature:* What T (ºC)?
        *   *Humidity:* What RH (%)?
        *   *Duration:* 24h? 1000h?

### 3. Phase 3: Critical Optimization - The "Black Box" Matrix
*   **Critique:** "Maximize resolution." This is lazy engineering.
*   **Requirement:**
    *   **DoE Framework:** Are we using a Central Composite Design (CCD)? Box-Behnken? Full Factorial?
    *   **Step Size:** If the range is 30-50% Ag, what is the increment? 1%? 5%?
    *   **Response Variables:** Swelling is the primary Z-axis, but you must simultaneously record Conductivity and Hardness. If you optimize for zero swelling but create an insulator, the prototype is trash.

### 4. Phase 4: Validation - The "Real World" Gap
*   **Critique:** "Tribological properties." Too vague.
*   **Requirement:**
    *   **Dynamic Testing:** We need a "Pin-on-Disc" or "Brush-on-Ring" test protocol.
    *   **Current Density:** Testing at 0 A/cm² is useless. We need to test *under load* (18 A/cm²) because Joule heating drives the swelling equilibrium!

## Action Items
1.  **Rewrite the Pipeline:** Expand each phase with specific technical protocols.
2.  **Define the Test Rig:** Describe the equipment needed (Climate Chamber + Current Source + Dynamometer).
3.  **Safety Check:** Some silanes are volatile. Add a safety protocol for the chemical handling.

**Verdict:** **REJECTED PENDING DETAIL.** Do not proceed to the lab until the *methodology* is as precise as the *strategy*.

**Signed,**
The CTO
