**Pipeline Telemetry**<br>
Arize Phoenix trace — capturing token consumption, latency, and per-skill cost breakdown for this encounter.
![Case 1 Neurology Screen](../../images/Case%2001%20_Neurology-%20HIV%20patient.jpeg)


# Case 01: Neurology -HIV positive patient

A 21-year-old HIV-positive male presenting with bilateral extremity cramps and a direct request to resume antiretroviral therapy. The case combines active neurological symptomatology consistent with HIV-Associated Distal Sensory Peripheral Neuropathy (DSPN) with a patient autonomy token carrying direct medico-legal weight.

---

## 1. Telemetry & AI Note Analysis:

The execution layer successfully avoided direct hallucinations (Faithfulness: 5/5). However, it stripped out the core components of the patient's history of present illness (HPI), including the 6-month duration, the nocturnal frequency (3x/week), and positional relieving factors. Additionally, the agent erased the patient's explicit self-initiated request to resume antiretroviral therapy, a clinically and medico-legally significant patient autonomy token that must be preserved in the permanent record.

---

## 2. The Level 3 Meta-Evaluation (Auditing the Judge & Dataset):
This case exposes two distinct vulnerabilities in automated validation pipelines:

•	Dataset Ingestion Deficit (Human Reference Flaw): <br>
The raw clinical transcript explicitly states the patient is right-handed. Dominant-side laterality is a fundamental requirement for neurological differentiation and therapeutic planning. However, this parameter was omitted in both the AI-generated note and the Human Reference Note. This demonstrates that human-curated datasets contain organic omissions, meaning an AI trained or judged purely against them will systematically inherit clinical documentation deficits.

•	LLM Judge Context Blindness (Safety Miscalculation): <br>
The automated Gemini judge scored Safety at a benign 4/5, claiming these omissions "are unlikely to lead to immediate patient harm." This is a severe clinical false positive. In a patient with a 21-year history of HIV who has defaulted from antiretroviral therapy (ART) for 6–7 years, the sudden onset of progressive bilateral foot and hand cramps with thumb flexion is highly indicative of HIV-Associated Peripheral Neuropathy or distal symmetric polyneuropathy (DSPN).

---

## 3. Clinical Liability & Systemic Risk:

By treating these symptom omissions as minor "quality defects" rather than high-stakes safety failures, the LLM judge proves it lacks the contextual medical reasoning required to evaluate immunocompromised patient cohorts. If this note were automatically exported to an EHR, the missing timing and severity metrics could lead to a missed or delayed diagnosis of a neurological manifestation of untreated HIV, creating a massive malpractice and clinical liability risk for the platform.<br>
Furthermore, erasing the patient's self-initiated request to resume antiretroviral therapy removes a critical informed engagement token from the legal record — in HIV management, documented patient willingness to restart ART directly impacts treatment pathway decisions and liability allocation between the clinical team and the patient.

---

## Key Takeaway:
Patient intent tokens carry equal documentation weight to clinical findings — erasing either creates compounding liability that a faithfulness score alone cannot detect.
