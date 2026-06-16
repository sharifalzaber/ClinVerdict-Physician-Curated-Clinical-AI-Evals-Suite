# ClinVerdict: Physician-Curated Clinical AI Evals Suite

Physician-curated adversarial evaluation suite designed to expose safety-critical failure modes in healthcare AI pipelines. Initial focus: ambient medical scribe agents, with planned expansion to broader medical AI use cases.

## 👨‍⚕️ Executive Overview
Standard automated natural language processing (NLP) evaluation metrics routinely fail to detect catastrophic clinical documentation errors. ClinVerdict is an adversarial evaluation suite developed from a specialized clinical perspective to isolate safety-critical failure modes in healthcare AI workflows prior to production deployment.

Instead of relying solely on automated benchmark metrics, this suite demonstrates a practical, multi-layer evaluation workflow applied to a baseline ambient Electronic Health Record (EHR) scribe pipeline.

### 💡 The Core Differentiator
ClinVerdict was independently designed, built, and evaluated by a practicing physician — from agent architecture and pipeline instrumentation to adversarial case curation and clinical meta-evaluation.<br>

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

## 🔬 Why Standard NLG Metrics Cannot Validate Clinical Safety

ROUGE-L and BERT score are the conventional baselines for text generation evaluation. They are also clinically blind.
→ [Full empirical analysis with data and physician rationale](analytics/why_standard_metrics_fail.md)

I tested them on three cases from this suite where one is clinically safe, two unsafe. All three scored in the overlapping "poor" range. No threshold separates safe from dangerous outputs.Standard metrics failed this suite. That is why we built the Multi-Layer Evaluation Workflow below to catch what metrics cannot see


---


## 🛠️ The Multi-Layer Evaluation Workflow
To track system-wide vulnerabilities, every clinical encounter in this suite is evaluated across 4 distinct dimensions:
1. **The Execution Layer:** Evaluating how faithfully the ambient clinical AI agent converts raw, spoken dialogue tokens into structured medical text.
2. **The Automated Judge Layer:** Auditing how effectively an automated LLM Judge tracks metric safety, completeness, and faithfulness via system tracing dashboards.
3. **The Clinical Validator Layer (Human-in-the-Loop):** A manual expert medical audit to identify automated judge blindness, rubric flaws, and underlying defects within human-annotated baseline datasets.
4. **The Pipeline Architecture Layer:** A cross-stage token propagation audit comparing extraction module(skill 1) output against SOAP generation (skill 2) — identifying tokens correctly extracted but silently dropped in the final result.

---

## 🏗️ Agent Architecture


```
[Conversation Input]
       │
       ▼
[Skill 1: Clinical Fact Extraction] (llama-3.3-70b-versatile)
       │
       ▼
[Skill 2: SOAP Note Generation]     (llama-3.3-70b-versatile)
       │
       ▼
[SOAP Output]
       │
       ▼
[LLM Judge]                         (gemini-2.5-flash)
       │
       ▼
[📋 Evaluated SOAP Output]
```

### 🔬 Live Pipeline Telemetry — Arize Phoenix
*Real-time span tracing across all three pipeline skills with token counts, 
latency, and cost monitoring.*

![Phoenix Tracing Dashboard](images/Phoenix%20Tracing.png)




---

## 📂 Suite Architecture & Contents

### 1. Scribe Agent Evaluation (Phase 1 Focus)
* **[`data_assets/`](data_assets/)**
  * Contains the open-access dataset tracking assets, raw encounter conversations, and human-annotated ground truth documentation utilized to run and test the baseline ambient scribe pipeline.
* **[`evaluators/`](evaluators/)**
  * Houses the execution codebase, core system prompts, and automated LLM judge rubrics designed to flag clinical safety failures.Full system prompts for Skill 1, Skill 2, and LLM Judge available in [prompts](evaluators/prompts.md)
* **[`analytics/`](analytics/)**
  * **[Master Evaluation Dashboard](analytics/README.md):** A data-dense matrix mapping all 10 complex clinical encounters, cross-referencing automated judge scores against manual clinical validation decisions.
  * **[Clinical & Medico-Legal Deep-Dives](analytics/deep_dives/):** Granular case reviews exposing high-severity clinical risk vectors across 5 public showcase cases.
  * **[Key Meta-Findings](analytics/key_meta_findings.md):** 6 nuanced, systemic discoveries revealing where automated evaluation metrics fall into blind spots.
  * **[System Recommendations](analytics/recommendations.md):** Engineering-focused remediation strategies addressing generation failures, judge architecture, dataset quality, and pipeline integrity.

### 2. Planned Future Expansions
* ⚠️ **Clinical Triage Evaluation Suite:** Curating adversarial datasets to stress-test acuity sorting, symptom prioritizing, and emergency red-flag sorting AI agents.
* 📋 **Discharge Summary Validation Suite:** Building evaluation workflows to audit continuity-of-care pipelines, specialized medication reconciliation, and post-discharge documentation.
* ⚖️ **Regulatory Alignment:** Evaluation workflow is informed by existing frameworks including the EU AI Act, GDPR, and HIPAA. Future expansion phases will progressively map evaluation frameworks to emerging global regulatory standards for high-risk clinical AI systems.


---

## 💼 Professional Profile & Objective
I am actively seeking roles within the Health-Tech and Clinical AI sectors, specifically focusing on **Clinical AI Evaluation, Safety Operations, Validation Architecture, and Human-in-the-Loop Oversight**. I bring a unique combination of clinical practice (MBBS), health sciences research (MSc), and hands-on LLM pipeline evaluation experience to engineering teams.

📫 **Let's Connect:** email: szaber@uef.fi & sharifalzaber57@gmail.com |  Linkedin: https://www.linkedin.com/in/sharif-al-zaber/

