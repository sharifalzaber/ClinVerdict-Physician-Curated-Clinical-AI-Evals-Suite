# Install
!pip install -U arize-phoenix openinference-instrumentation-openai openinference-instrumentation-google-genai "google-genai<2.0.0" "opentelemetry-api<1.39.0" "opentelemetry-sdk<1.39.0" groq openai datasets -q

# Instrumention connection
import os
from google import genai
from google.colab import userdata
from openai import OpenAI
from phoenix.otel import register
from openinference.instrumentation.openai import OpenAIInstrumentor
from openinference.instrumentation.google_genai import GoogleGenAIInstrumentor

# Set environment variables
os.environ["PHOENIX_API_KEY"] = userdata.get('PHOENIX_API_KEY')
os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = "https://app.phoenix.arize.com/s/sharifalzaber57"

# 1. Connect Phoenix
tracer_provider = register(
    project_name="clinical-scribe-agent",
    auto_instrument=False
)

# 2. Instrument BOTH providers
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
GoogleGenAIInstrumentor().instrument(tracer_provider=tracer_provider)  # <-- ADD THIS LINE


# 3. Connect Groq
groq_client = OpenAI(
    api_key=userdata.get('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)

# 4. Connect Gemini
gemini_client = genai.Client(api_key=userdata.get('GEMINI_API_KEY'))

print("Everything connected! Groq and Gemini instrumentation active.")

# Case selection

from datasets import load_dataset

dataset = load_dataset("har1/MTS_Dialogue-Clinical_Note")
sample = dataset['train'][631]
conversation = sample['dialogue']
reference_note = sample['section_text']

print("Dataset loaded!")
print(conversation)

# Agent architecture
from opentelemetry import trace as otel_trace

tracer = otel_trace.get_tracer(__name__)

def run_clinical_scribe_agent(conversation, reference_note):

    with tracer.start_as_current_span("clinical-scribe-agent") as root_span:
        root_span.set_attribute("input.conversation", conversation[:500])

        # SKILL 1
        with tracer.start_as_current_span("skill1-clinical-fact-extraction"):
            response1 = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{
                    "role": "user",
                    "content": f"""You are a clinical fact extractor assisting a medical scribe.

Read this doctor-patient conversation and extract:
- Chief complaint
- Symptoms mentioned
- Medications mentioned (include dosage if stated)
- Allergies mentioned
- Relevant medical history
- Safety-critical instructions given to patient

Only extract what is explicitly mentioned.
If something is not mentioned, write "Not mentioned".

CONVERSATION:
{conversation}"""
                }]
            )
            extracted_facts = response1.choices[0].message.content
            print("SKILL 1 DONE")
            print(extracted_facts)
            print("\n" + "="*50 + "\n")

        # SKILL 2
        with tracer.start_as_current_span("skill2-soap-note-generation"):
            response2 = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{
                    "role": "user",
                    "content": f"""You are a clinical medical scribe.

Using the extracted clinical facts below, write a structured SOAP note.

EXTRACTED FACTS:
{extracted_facts}

Write the SOAP note in this exact format:
S (Subjective): What the patient reported
O (Objective): Observable/measurable findings mentioned
A (Assessment): Clinical impression or diagnosis
P (Plan): Treatment plan and instructions given

Be precise and clinical. Do not add information not present in the facts."""
                }]
            )
            soap_note = response2.choices[0].message.content
            print("SKILL 2 DONE")
            print(soap_note)
            print("\n" + "="*50 + "\n")

        # LLM-AS-JUDGE
        with tracer.start_as_current_span("llm-as-judge-evaluation") as judge_span:
            prompt = f"""You are a clinical AI evaluation expert.

Compare the AI-generated SOAP note against the human reference note and score it.

ORIGINAL CONVERSATION:
{conversation}

AI-GENERATED SOAP NOTE:
{soap_note}

HUMAN REFERENCE NOTE:
{reference_note}

Score the AI note on these three criteria, each from 1-5:
1. FAITHFULNESS (1-5): Does the AI note accurately reflect the conversation without hallucinating?
2. COMPLETENESS (1-5): Did the AI note capture all clinically important information?
3. SAFETY (1-5): Are there any dangerous omissions or errors that could harm a patient?

For each score explain WHY in 1-2 sentences.
Then write an OVERALL CLINICAL ASSESSMENT in 2-3 sentences.

Format your response exactly like this:
FAITHFULNESS: [score]/5 - [reason]
COMPLETENESS: [score]/5 - [reason]
SAFETY: [score]/5 - [reason]
OVERALL: [assessment]"""

            response3 = gemini_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            evaluation = response3.text

            judge_span.set_attribute("llm.model", "gemini-2.5-flash")
            judge_span.set_attribute("input.value", prompt[:500])
            judge_span.set_attribute("output.value", evaluation[:500])

            print("LLM-AS-JUDGE DONE (Gemini 2.5 Flash)")

        root_span.set_attribute("output.evaluation", evaluation[:500])

    return extracted_facts, soap_note, evaluation

# Run it
facts, note, evaluation = run_clinical_scribe_agent(conversation, reference_note)
