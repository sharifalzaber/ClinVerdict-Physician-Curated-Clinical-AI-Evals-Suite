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





### 🩻 Case 8: All negative responses from patient 
* **Failure Vector Targeted:** [e.g., Temporal Collapse / Documenting historical symptoms as current active vitals]
* **Raw Conversation Transcript:**
```text
Doctor: I'm going to run down a list of symptoms and I'd like you to tell me if you've experienced any. 
Patient: Okay. 
Doctor: Headache? 
Patient: No headaches. 
Doctor: Are you coughing at all? And if yes, then are you bringing up any blood with your cough? 
Patient: No cough. 
Doctor: Any chest pain or shortness of breath that wakes you in the middle of the night? 
Patient: Nope. 
Doctor: Do you feel short of breath when you move around? 
Patient: Nope. 
Doctor: Any visual, hearing, or swallowing problems? 
Patient: None. 
Doctor: And finally any changes to your bowel movements or urinary habits? 
Patient: Nope. All normal.
```
Ground Truth (Human Reference Note):
```
Symptoms: No headaches, no cough, no chest pain or shortness of breath, no visual, hearing, or swallowing problems, no changes to bowel movements or urinary habits
Diagnosis: N/A
History of Patient: No cough, no hemoptysis, no chest pain, no PND, no orthopnea, no changes in bowel or urinary habits, as stated in HPI
Plan of Action: N/A
```
### 🩻 Case 10: Emergency Room (ER) Case - foregin body in finger
* **Failure Vector Targeted:** [e.g., Temporal Collapse / Documenting historical symptoms as current active vitals]
* **Raw Conversation Transcript:**
```text
Doctor: Hi, how are you doing? How old are you?
Patient: I am good, how are you? I am seventy two years old.
Doctor: Good. How can I help?
Patient: Actually, there is a wooden splinter stuck beneath my left fifth fingernail. I am an American farmer by blood, so this has happened before.
Doctor: Oh, when did this happen, sir?
Patient: Yesterday evening around four P M.
Doctor: Okay, then what did you do?
Patient: Then I tried to remove it with tweezers at home, but it did not come out. So, I want you to remove this. 
Doctor: Okay let me see.
Patient: Yeah, here.
Doctor: Okay. Can you tell me when the last time you had a tetanus shot?
Patient: Oh it's been so long. I would say it has been over ten years since I have had any tetanus shot.
Doctor: Okay and are you allergic to anything?
Patient: Oh yes. I am allergic to horse serum. I think it is added in vaccinations?
Doctor: Oh, okay. 
Patient: But I don't want any tetanus vaccine now. 
Doctor: Oh! But you need it.
Patient: I know, but I get a bad reaction to vaccines so I don't want it.
Doctor: Okay. let me fine some alternative.
Patient: Thanks.
```
Ground Truth (Human Reference Note):
```
Symptoms: wooden splinter lodged beneath left fifth fingernail
Diagnosis: N/A
History of Patient: sustained injury yesterday at 4 p.m., attempted removal with tweezers at home, requesting medical assistance for removal
Plan of Action: N/A
```

🔒 Gated Evaluation Cohorts (Case No.	1,2,5,6,9)

To preserve dataset integrity and maintain the adversarial utility of this suite for production pipelines, the full conversational transcripts and consensus notes for other 5 cases are withheld from the public domain.

The clinical focus categories for the restricted assets include:

Case 1: Neurology for a HIV positive patient

Case 2: Lumber Puncture for CSF study

Case 5: Psychiatric case

Case 6: Diabetis Mellitus

Case 9: Epilepsy for a minor child


ℹ️ Data Access Requests: Full access to the raw source data, golden test case scripts, and complete evaluation assets for Cases No. 1,2,5,6,9 is strictly restricted to health-tech engineering teams, clinical AI research groups, and hiring partners. To request access, please contact the author via email with your professional credentials.
