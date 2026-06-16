# 📂 Clinical Evaluation Datasets & Test Assets

This directory houses the foundational clinical text assets used to benchmark the ambient EHR scribe pipeline. It acts as an adversarial filter, isolating high-acuity and deceptively complex medical encounters from large, open-source documentation datasets.

---

## 🔬 Source Dataset & Selection Methodology
* **Baseline Corpus:** The primary raw conversational data is derived from the open-access **MTS_Dialogue-Clinical_Note** dataset (consisting of 1,301 clinical dialogues and human-annotated consensus summaries).
* **Physician-Led Filtering:** Rather than evaluating the agent against thousands of standard, low-variance encounters (e.g., routine prescription refills), a manual review was conducted across hundreds of transcripts. 
* **The "Golden Test Suite":** Exactly 10 specific encounters were isolated to form a curated "adversarial suite." These cases contain complex clinical phenomena—such as high-acuity pediatric presentations, multi-system chronic disease management, and implicit patient dissent—specifically chosen because they expose systemic failure modes in LLM architectures.

---
