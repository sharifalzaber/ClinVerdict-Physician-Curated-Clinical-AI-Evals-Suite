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

### 🩻 Case 3: Kideny Disease 
* **Failure Vector Targeted:** [e.g., Temporal Collapse / Documenting historical symptoms as current active vitals]
* **Raw Conversation Transcript:**
```text
Doctor: Hi there! I am Doctor Kim. Nice to meet you, miss. 
Patient: Hi! Nice to meet you. 
Doctor: How are you feeling today? 
Patient: I am feeling much better today. 
Doctor: How old are you? 
Patient: I am forty six. 
Doctor: How is your pain in the left side? 
Patient: It is much better. It is more like a dull pain now.
Doctor: Are you still having trouble with urination? 
Patient: It has gotten better but is still a little difficult. 
Doctor: Okay. It looks like Doctor X did an exam yesterday. Doctor X consulted me on your status but I have a question for you. I see in your medical history that you had a bruised left kidney. Can you tell me more about the bruised kidney? 
Patient:  Yes. I was in a car accident, years ago. The doctor told me that I had a bruised left kidney. They thought it was due to the accident, but they could not be certain
```
Ground Truth (Human Reference Note):
```
Symptoms: Left flank pain (now dull), difficulty urinating (improving)
Diagnosis: N/A
History of Patient: Presented to the emergency room with left flank pain and difficulty urinating, vague history of bruised left kidney in a motor vehicle accident, feeling much better today
Plan of Action: N/A
```
### 🩻 Case 4: A rare form of Blood Cancer (Polycythemia Vera)
* **Failure Vector Targeted:** [e.g., Temporal Collapse / Documenting historical symptoms as current active vitals]
* **Raw Conversation Transcript:**
```
Doctor: Hello Mister Strange, can you please confirm your age and ethnicity for the records.
Patient: Hi Doctor, I am fifty five now and would identify myself as a white male. 
Doctor: Let's first talk about your medical condition. There has been a diagnosis of polycythemia vera with secondary myelofibrosis. Also, you are J A K two positive. Do you remember when you were diagnosed?
Patient: It was sometimes between two thousand and five and six. 
Doctor: They did phlebotomy and then subsequently you got yourself transferred here in our healthcare. 
Patient: Yes.
Doctor: You have been on hydroxyurea and interferon, right?
Patient: Oh, it was a terrible time, I could not deal with anyone of them. I had numbness and tingling with burning pain in my hands.
Doctor: You do not have any siblings that we can try for transplant match?
Patient: That's right! 
Doctor: You were also considered for the Matched Unrelated Donor Transplant, but you couldn't be on the list due to social support and also health was in reasonably better state than other candidates normally on that transplant list.
Patient: We had some medications here as well when I first started my care here, I forgot the name. 
Doctor: Yes, here we started you on a trial of lenalidomide and prednisone for some time. You were doing great on that for a while, but then you developed intolerance to lenalidomide. 
Patient: Yes, I had severe diarrhea and I always felt tired like I have no energy left in me. Eventually it all stopped. 
Doctor: Yeah, here it says that you injured your leg? Tell me what happened. 
Patient: It all happened last week, I injured this left leg and got swelling. I had some prescribed steroids, so I took them for about three days only. The swelling is eventually gone now.
Doctor: Any other related complaints?
Patient: No.
Doctor: Do you smoke or drink?
Patient: I take marijuana. I feel really hungry after smoking it, so I eat a lot. In just the last few weeks I have gained a few pounds. 
Doctor: Okay, your overall performance status in the E C O G scale is one.
```
Ground Truth (Human Reference Note):
```
Symptoms: swelling in the left leg (resolved), severe fatigue, diarrhea
Diagnosis: polycythemia vera with secondary myelofibrosis, JAK2 positive
History of Patient: Diagnosis made between 2005 and 2006, underwent phlebotomy initially, transferred care to current healthcare institution, intolerance to hydroxyurea and interferon, considered for Matched Unrelated Donor Transplant but not a candidate due to social support and relatively good health, trial of lenalidomide and prednisone with subsequent intolerance to lenalidomide, injury to left leg with swelling (resolved)
Plan of Action: N/A
```
### 🩻 Case 7:  Pediatrics Case
* **Failure Vector Targeted:** [e.g., Temporal Collapse / Documenting historical symptoms as current active vitals]
* **Raw Conversation Transcript:**
```text
Doctor: How's the little one doing?
Guest_family: She is doing okay. 
Doctor: How long was your pregnancy?
Guest_family: Thirty six weeks.
Doctor: Was your delivery normal or C section?
Guest_family: It was a C section. 
Doctor: How much did she weigh? 
Guest_family: She was eight pounds and three ounces.
Doctor: Tell me what's the issue?
Guest_family: Yeah, she has a history of seizures. It looks like she is having pain in her tummy and is throwing up. 
Doctor: What else did you notice?
Guest_family: It looks like she is having some rashes on her skin. There is vomiting for sure. She also feels bloated. She also complains of pain in her tummy. Sometimes she does scratch her mouth. We also noticed some swelling around her lips, eyes and face.
Doctor: It looks like she's having some food intolerance.
```
Ground Truth (Human Reference Note):
```
Symptoms: Seizures, abdominal pain, vomiting, skin rash, bloating, scratching mouth, swelling around lips, eyes, and face.
Diagnosis: Food intolerance (suspected).
History of Patient: Born via C-section at 36 weeks, weighed 8 lbs 3 oz, history of seizures.
Plan of Action: N/A.
```

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
