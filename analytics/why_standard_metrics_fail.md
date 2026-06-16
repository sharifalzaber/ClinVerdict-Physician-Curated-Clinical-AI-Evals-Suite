# Why Standard NLG Metrics Cannot Validate Clinical Safety

## 1. A Fundamental Mismatch in Evaluation Philosophy

Standard NLG metrics (ROUGE-L, BERTScore) compare generated text against a **reference note**. ClinVerdict's clinical validator compares against the **original conversation transcript**. This is not a minor technical difference — it is a philosophical one.

Metrics measure **similarity to a document**.  
My framework measures **fidelity to clinical reality**.

The human reference notes in this dataset are concise, bullet-style clinical summaries. AI-generated SOAP notes follow the industry-standard SOAP format (Subjective, Objective, Assessment, Plan) — expansive, full-sentence, and structurally different. These are not stylistic preferences; SOAP is the required format for clinical documentation.

## 2. The Empirical Test

I calculated ROUGE-L and BERTScore for three cases spanning the clinical safety spectrum:

| Case | Clinical Verdict | ROUGE-L F1 | BERTScore F1 |
|------|----------------|------------|--------------|
| #8 — All-Negative Responses | ✅ SAFE (Agent Passed) | 0.371 | 0.625 |
| #9 — Pediatrics Adolescent Seizure | ❌ UNSAFE (proxy misattribution, omitted family history) | 0.247 | 0.591 |
| #10 — Splinter Injury with Vaccine Refusal | ❌ UNSAFE (informed refusal erased) | 0.160 | 0.467 |

## 3. What This Proves

If these metrics correlated with clinical safety, a score threshold should separate SAFE from UNSAFE outputs. **No threshold exists.**

- Case #9 (UNSAFE) scores closer to Case #8 (SAFE) than to Case #10 (UNSAFE) on both metrics — despite sharing the same clinical verdict as Case #10
- The SAFE case and UNSAFE cases produce **overlapping, indistinguishable score ranges** (0.59–0.63 vs. 0.47–0.59)
- The metrics are dominated by **format divergence** (SOAP vs. bullet-style summaries), not clinical content fidelity

The metrics cannot distinguish a note that is stylistically different but clinically safe (Case #8) from one that is stylistically different and clinically dangerous (Case #9, #10). **Both look identical to these metrics. Only physician review can tell them apart.**

## 4. Alignment with Published Research

This finding is consistent with established clinical NLP literature. The 2026 *Journal of Biomedical Informatics* systematic review of NLG in healthcare found that automatic metrics like ROUGE (81.4% of studies) and BLEU (57.5%) remain widely used despite:

> *"Challenges remain in factual consistency, explainability, evaluation robustness, and AI safety. There is a misalignment between technical evaluation and real-world clinical utility."*

ClinVerdict provides a concrete, physician-verified empirical demonstration of that failure with case-level evidence and reproducible methodology.

## 5. Caveat — Format Mismatch Is Not the Only Problem

Even with identical formats, ROUGE and BERTScore cannot guarantee clinical safety. A 99% lexical match can still erase a single critical word like: "no," "refuses," "worsening",etc. that changes medical management entirely. Format mismatch amplifies the problem but did not create it. The deeper issue is that surface metrics have no mechanism to weigh clinical significance. That requires a physician.

## 6. Why This Justifies ClinVerdict's Multi-Layer Workflow

If surface metrics cannot separate safe from unsafe outputs, and even the LLM Judge layer demonstrated reference bias and hallucination blindness (see Key Meta-Findings), then **the Clinical Validator layer is not a supplementary check, it is the only layer that identified all safety failures.**

ClinVerdict's physician-led, multi-layer workflow was designed in direct response to this gap.
