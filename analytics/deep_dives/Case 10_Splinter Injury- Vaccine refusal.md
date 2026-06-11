**Pipeline Telemetry**<br>
Arize Phoenix trace — capturing token consumption, latency, and per-skill cost breakdown for this encounter.
![Case 10 Splinter Injury Vaccine Refusal Screen](../../images/Case%2010_Splinter%20Injury-%20Vaccine%20refusal.jpeg)


# Case 10: Splinter in finger with vaccine refusal

A 72-year-old farmer presenting to the ER with a wooden splinter lodged beneath the left fifth fingernail, with an outdated tetanus status exceeding 10 years, a documented horse serum allergy, a prior failed home extraction attempt, and an explicit, repetitive refusal of the tetanus vaccine due to prior adverse reactions.

---

## 🤖 1. Telemetry & AI Note Analysis:
The patient stated three critical facts: an outdated tetanus status (>10 years), a specific allergy to horse serum, and an explicit, repetitive refusal. While the agent correctly documented the tetanus status and horse serum allergy, it completely erased the third and  legally significant fact of the patient's hard refusal.
Additionally the agent omitted the patient's prior home removal attempt using tweezers, a critical procedural history that directly impacts the clinical approach.

•	Propagation Note: Patient’s vaccine refusal omission was confirmed as an inter-skill propagation failure, the token was present in Skill 1 extraction output but dropped at SOAP generation stage.

---

## ⚖️ 2. Meta-Evaluation: Judge & Dataset Audit
This final case perfectly highlights the limitations of an automated judge's ability to evaluate a note's context strictly within the boundaries of a raw transcript:<br>
•	The Judge's External Expectation Fallacy: <br> 
The llm-judge penalizes the agent under Completeness and Safety for omitting a splinter removal plan. However, the transcript proves the clinician never articulated a removal strategy in the room. By demanding this, the judge commits a Boundary Violation, evaluating based on clinical expectations rather than text-matching constraints.<br>

•	The Ground-Truth Contamination Defect:<br> The clinician explicitly committed to finding a tetanus vaccine alternative—a critical Plan of Action. The human annotator completely erases this by designating the plan as "N/A." Furthermore, the baseline omits the patient's age (72), occupation (farmer), allergy, and clinical timeline, rendering it useless as a gold standard.<br>

•	Asymmetric Safety Constraint Override(Successful Gatekeeping): <br>
Despite the human reference note containing no mention of patient’ allergy and vaccine refusal, the judge successfully bypassed the flawed baseline, looked directly at the raw transcript, and penalized the agent for missing the dissent detail. Instead of succumbing to Reference Bias the judge's internal safety alignment weights overrode the explicit prompt constraint ("cross-check against the human note") to protect clinical continuity—mirroring the exact mechanical behavior observed during the kidney injury evaluation in Case #3.

---

## ⚠️ 3. Clinical Liability & Medico-Legal Systemic Risk:
•	The Erasure of Informed Dissent:<br>
The patient explicitly refused the vaccine due to prior adverse reactions. By smoothing this directive into generic boilerplate text ("weighing risks and benefits of alternatives"), the agent obliterates the patient's legal right to refuse treatment. A covering clinician relying on this note could proceed with alternative formulations assuming implied consent, directly violating informed dissent and exposing the health system to a battery-of-care lawsuit. Ambient tools must treat explicit patient refusals as non-negotiable tokens that can never be synthesized.<br>

•	Omission of Procedural Risk Context:<br>
The agent omitted the patient's failed home extraction attempt with tweezers. A prior failed mechanical intervention significantly increases the baseline risk profile—raising the likelihood of fragment breakage, deeper embedding, and bacterial inoculation. Leaving this out deprives the clinical team of a critical contextual defense in the event of procedural complications, transforming an inherent medical risk into avoidable documentation liability.

---

## Key Takeway:
An ambient scribe that compresses explicit patient refusal into generic boilerplate does not create a documentation gap — it obliterates informed consent and exposes the health system to direct battery-of-care liability.
