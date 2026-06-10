# ClinVerdict: Physician-Curated Clinical AI Evaluation Suite
Physician-curated clinical AI evaluation suite designed to identify safety-critical failure modes in healthcare AI workflows. Initial focus: medical scribes, with planned expansion to broader clinical AI use cases.

## 👨‍⚕️ Executive Overview
Standard automated natural language processing (NLP) evaluation metrics routinely fail to detect catastrophic clinical documentation errors. ClinVerdict is an adversarial evaluation suite developed from a specialized clinical perspective to isolate safety-critical failure modes in healthcare AI workflows prior to production deployment.

Instead of relying solely on uncalibrated benchmark metrics, this suite demonstrates a practical, multi-layer evaluation workflow applied to a baseline ambient Electronic Health Record (EHR) scribe pipeline.

### 💡 The Core Differentiator
While AI engineers can build automated LLM judges, they lack the clinical intuition to isolate hidden medical liabilities. The value of ClinVerdict lies in **physician-led adversarial case selection**. By auditing large datasets, a small set of clinically deceptive, high-variance, and high-acuity encounters were isolated as a "Golden Test Case Suite" to expose exactly where automated AI validation gates collapse.

---
## 🎯 Golden Suite Curation Criteria

The 10 golden test cases were hand-curated from a larger open-access dataset after 
systematic review. Selection criteria prioritized:

- **Clinical specialty diversity:**<br>neurology, pediatrics, diabetes, nephrology, oncology,
  psychiatry, infectious disease, clinical intervention, emergency.
- **Documentation complexity:** <br> proxy historians, informed refusal, multi-system 
  presentations, temporal complexity, complicated family history
- **Adversarial potential:** <br> cases where standard NLP metrics would pass but 
  clinical validators would fail

This deliberate curation strategy is what transforms a benchmark into an adversarial evaluation suite.

---

## 🛠️ The Multi-Layer Evaluation Workflow
To track system-wide vulnerabilities, every clinical encounter in this suite is evaluated across three distinct dimensions:
1. **The Execution Layer:** Evaluating how faithfully the ambient clinical AI agent converts raw, spoken dialogue tokens into structured medical text.
2. **The Automated Judge Layer:** Auditing how effectively an automated LLM Judge tracks metric safety, completeness, and faithfulness via system tracing dashboards.
3. **The Clinical Validator Layer (Human-in-the-Loop):** A manual expert medical audit to identify automated judge blindness, rubric flaws, and underlying defects within human-annotated baseline datasets.
4. **The Pipeline Architecture Layer:** A cross-stage token propagation audit comparing extraction module(skill 1) output against SOAP generation (skill 2) — identifying tokens correctly extracted but silently dropped in the final result.

---

## 🏗️ System & Evaluation Architecture
*(Placeholder for your multi-agent architecture diagram/text explanation and your Arize Phoenix tracing dashboard screenshots. This section proves you successfully hooked up automated telemetry tools to monitor your pipelines in real-time.)*

---

## 📂 Suite Architecture & Contents

### 1. Scribe Agent Evaluation (Phase 1 Focus)
* **[`data_assets/`](data_assets/)**
  * Contains the open-access dataset tracking assets, raw encounter conversations, and human-annotated ground truth documentation utilized to run and test the baseline ambient scribe pipeline.
* **[`evaluators/`](evaluators/)**
  * Houses the execution codebase, core system prompts, and automated LLM judge rubrics designed to flag clinical safety failures.
* **[`analytics/`](analytics/)**
  * **[Master Evaluation Dashboard](analytics/README.md):** A data-dense matrix mapping all 10 complex clinical encounters, cross-referencing automated judge scores against manual clinical validation decisions.
  * **[Clinical & Medico-Legal Deep-Dives](analytics/deep_dives/):** Granular case reviews exposing high-severity clinical risk vectors across 5 protected showcase cohorts.
  * **[Key Meta-Findings](analytics/key_meta_findings.md):** 5 nuanced, systemic discoveries revealing where automated evaluation metrics fall into blind spots.
  * **[System Recommendations](analytics/recommendations.md):** Engineering-focused solutions to patch pipeline defects, including prompt-layer guardrails and Dual-Track UI layouts.

### 2. Planned Future Expansions
* ⚠️ **Clinical Triage Evaluation Suite:** Curating adversarial datasets to stress-test acuity sorting, symptom prioritizing, and emergency red-flag sorting AI agents.
* 📋 **Discharge Summary Validation Suite:** Building evaluation workflows to audit continuity-of-care pipelines, specialized medication reconciliation, and post-discharge documentation.
* 🇪🇺 **Regulatory Alignment:** Progressively mapping these evaluation workflows to comply directly with the human oversight, risk management, and dataset quality requirements mandated for high-risk systems under the **EU AI Act** and **GDPR**.

---

## 💼 Professional Profile & Objective
I am actively seeking roles within the Health-Tech and Clinical AI sectors, specifically focusing on **Clinical AI Evaluation, Safety Operations, Validation Architecture, and Human-in-the-Loop Oversight**. I bring a unique combination of clinical practice (MBBS), health sciences research (MSc), and hands-on LLM pipeline evaluation experience to engineering teams.

📫 **Let's Connect:** [Your Email Address] | [Your LinkedIn Profile Link]
