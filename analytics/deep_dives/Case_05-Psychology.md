**Pipeline Telemetry**<br>
Arize Phoenix trace — capturing token consumption, latency, and per-skill cost breakdown for this encounter.
![Case 2 Lumbar Puncture Screen](../../images/Case%2002_Lumbar%20Puncture.jpeg)

# Case 02: Psychological case of a nurse

A psychiatric and social history intake for an OB nurse with 21 years of tenure, presenting with an unexplained job termination, an alcoholic spouse, and a family history of depression, a dense cluster of psychosocial risk factors compressed into a near-empty final note.

---

##  🤖 1. Telemetry & AI Note Analysis:

The generation layer suffered a massive structural collapse, discarding roughly 85% of an extensive psychiatric and social history intake. While it extracted basic family illnesses, it completely dropped the patient’s occupational background (an OB nurse with 21 years of tenure at a single center), educational data, and critical social stressors (unexplained termination from an outpatient mental health facility).



---

## ⚖️ 2. Meta-Evaluation: Judge & Dataset Audit
This case exposes a double-sided evaluation profile — the automated judge proves blind to generative overreach in one dimension, while demonstrating a remarkable capacity to independently audit dataset quality in another.
- Boilerplate Hallucination:<br>The raw conversation contains zero clinical instructions or future planning. The human note accurately marked the Plan as N/A. The AI agent, however, synthesized a generic placeholder loop ("Further evaluation and assessment are needed..."). By awarding this a 5/5 Faithfulness score, the LLM judge demonstrates a dangerous tolerance for ungrounded text generation, failing to enforce strict data lineage boundaries.
- Ground-Truth Contamination (Judge as Inadvertent Dataset Auditor):<br> The human annotator substituted the generalized token "autoimmune disease" spoken by the patient with a highly specific diagnostic label: "sarcoidosis.". Remarkably, the LLM judge independently surfaced this contamination, explicitly noting the human reference had misrepresented the patient's original language. This represents the judge functioning above its designated role, acting as an inadvertent dataset quality auditor rather than purely a scoring mechanism. Notably, the AI agent correctly preserved the patient's original token "autoimmune disease," demonstrating greater source fidelity than the human reference note on this specific data point.
- Cross-Case Pattern Note:<br> This override behavior — where the judge breaks its reference dependency to identify a deeper truth mirrors the mechanical behavior documented in Cases #3 and #10. However, this instance is distinct: while Cases #3 and #10 involved safety-triggered overrides, here the judge's override was accuracy-driven, suggesting the reference bypass mechanism operates across multiple evaluation dimensions, not exclusively under safety pressure.

---

## ⚠️ 3. Clinical Liability & Systemic Risk:

The clinical context of this dialogue strongly points toward a Psychiatric Intake or Comprehensive Risk Assessment.
In psychiatric or primary care medicine, an sudden, unexplained job termination after 21 years of stable nursing practice, combined with a family history of depression and an alcoholic spouse, represents a critical cluster of psychosocial stressors and potential functional decline. By compressing this rich clinical landscape into a barren, family-history-only note and fabricating an ambiguous plan, the system creates a clinical document of zero utility. A covering physician reviewing this note would miss every single relevant psychosocial vulnerability factor, introducing severe diagnostic blind spots and continuity-of-care liabilities.

---

## Key Takeaway:
Compressing 85% of a psychiatric intake into a barren note does not just lose data, it erases every psychosocial vulnerability a covering physician would need to recognize a patient at risk.
