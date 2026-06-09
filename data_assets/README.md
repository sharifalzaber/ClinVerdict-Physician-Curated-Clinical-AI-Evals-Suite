# 📂 Clinical Evaluation Datasets & Test Assets

This directory houses the foundational clinical text assets used to benchmark the ambient EHR scribe pipeline. It acts as an adversarial filter, isolating high-acuity and deceptively complex medical encounters from large, open-source documentation datasets.

---

## 🔬 Source Dataset & Selection Methodology
* **Baseline Corpus:** The primary raw conversational data is derived from the open-access **MTS_Dialogue-Clinical_Note** dataset (consisting of 1,301 clinical dialogues and human-annotated consensus summaries).
* **Physician-Led Filtering:** Rather than evaluating the agent against thousands of standard, low-variance encounters (e.g., routine prescription refills), a manual review was conducted across hundreds of transcripts. 
* **The "Golden Test Suite":** Exactly 10 specific encounters were isolated to form a curated "adversarial suite." These cases contain complex clinical phenomena—such as high-acuity pediatric presentations, multi-system chronic disease management, and implicit patient dissent—specifically chosen because they expose systemic failure modes in LLM architectures.

---

## 🏆 Public Showcase Cases (Vulnerability Cohort)
To demonstrate the clinical validation framework without exposing the entire proprietary testing suite, 5 distinct adversarial cases are published in full below.
(Showcase cases are listed by their original cohort IDs to maintain consistency with the automated evaluation logs.)
Deep-dive clinical analysis is publicly available for 5 showcase cases. Full case materials for all 10 are available here. Extended analysis available upon professional inquiry.








🔒 Gated Evaluation Cohorts (Case No.	1,2,5,6,9)

To preserve dataset integrity and maintain the adversarial utility of this suite for production pipelines, the full conversational transcripts and consensus notes for other 5 cases are withheld from the public domain.

The clinical focus categories for the restricted assets include:

Case 1: Neurology for a HIV positive patient

Case 2: Lumber Puncture for CSF study

Case 5: Psychiatric case

Case 6: Diabetis Mellitus

Case 9: Epilepsy for a minor child


ℹ️ Data Access Requests: Full access to the raw source data, golden test case scripts, and complete evaluation assets for Cases No. 1,2,5,6,9 is strictly restricted to health-tech engineering teams, clinical AI research groups, and hiring partners. To request access, please contact the author via email with your professional credentials.
