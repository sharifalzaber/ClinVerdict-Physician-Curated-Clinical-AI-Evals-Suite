# 📂 AI Execution & Automated Evaluation Layers

This directory houses the computational core of the evaluation suite. It contains the operational codebase for the ambient clinical scribe agent, the system prompt architectures, and the structured LLM judge rubrics utilized to automate pipeline tracing.

---

## 🤖 1. The Execution Layer (Agent Logic)
The baseline ambient EHR scribe is engineered as a target pipeline designed to process unstructured, multi-turn clinical dialogue tokens and synthesize them into standard, structured SOAP (Subjective, Objective, Assessment, Plan) notes. 

**System Architecture:** A dual-stage, split-context pipeline engineered to decouple clinical fact-extraction from final document synthesis.
* Stage 1 operates as a deterministic *Clinical Fact Extractor* to isolate explicit historical and physiological milestones from text transcripts.
* Stage 2 consumes these isolated facts to construct the finalized, structured SOAP note.
This structural separation minimizes context drift and suppresses generative hallucinations.


**Core Codebase:** The complete implementation script is available in this directory at `clinical_scribe_agent.py`.

---


## ⚖️ 2. The Automated Judge Layer (Evaluation Rubrics)
To evaluate the agent's outputs at scale before human validation, an automated **LLM Judge** framework was deployed. The judge utilizes a zero-shot prompt with strict criteria forcing the model to generate a structured clinical rationale alongside every numeric score.

The system evaluates every generated SOAP note across three core dimensions:

### 🛡️ A. Faithfulness (Score: 1–5)
* **Objective:** Guarantees that the agent does not fabricate, extrapolate, or guess clinical information not explicitly verified in the transcript.
* **Rubric Logic:** Cross-references the generated note against the raw conversation to detect any clinical "hallucinations" or phantom assertions.

### 🎯 B. Completeness (Score: 1–5)
* **Objective:** Ensures no critical clinical data explicitly stated in the dialogue (vitals, symptoms, active medications, key history) is omitted from the final documentation.
* **Rubric Logic:** Evaluates if the agent captured all clinically relevant milestones required to maintain continuity of care.

### ⚠️ C. Safety & Risk Mitigation (Score: 1–5)
* **Objective:** Acts as a critical medico-legal filter to isolate dangerous errors.
* **Rubric Logic:** Specifically flags high-risk documentation failures, such as missed red flags, incorrect medication dosages, or erroneous diagnostic assertions that could result in clinical harm if exported directly into a patient's electronic health record (EHR).


## 📊 3. Telemetry & Tracing Configuration
Automated execution traces and evaluation metrics are captured and visualized using **Arize Phoenix**. This telemetry layer allows for real-time tracking of:
* Input token sequences vs. Output response structures.
* LLM Judge scoring outputs across the entire evaluation cohort.
* Structural trace debugging to isolate exactly where latency or context-window drift occurs during extended clinical dialogues.

---

## 📄 File Index
* **[`README.md`](README.md):** This documentation homepage.
* **`clinical_scribe_agent.py`**: The complete python codebase executing both the scribe agent skills and the automated judge evaluation loops.
