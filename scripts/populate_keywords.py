import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "extracted" / "question-bank.json"
TS_PATH = ROOT / "lib" / "questions.ts"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

# Helper function to extract trigger keywords from prompt, explanation, and answers
def extract_smart_keywords(q):
    keywords = set()
    prompt = q.get("prompt", "")
    explanation = q.get("explanation", "")
    answer = q.get("answer", "")
    answer_items = q.get("answerItems", [])
    options = q.get("options", [])
    c_opts = q.get("correctOptionIds", [])
    q_num = q.get("number")

    # 1. Add correct answer values/labels
    for item in answer_items:
        val = item.get("value", "").strip()
        lbl = item.get("label", "").strip()
        if val and val.lower() not in ["yes", "no", "true", "false", "a", "b", "c", "d"]:
            keywords.add(val)
        if lbl and len(lbl) > 4 and lbl.lower() not in ["correct option", "question"]:
            keywords.add(lbl)

    for cid in c_opts:
        for opt in options:
            if opt.get("id") == cid:
                text = opt.get("text", "").strip()
                if len(text) <= 80:
                    keywords.add(text)
                else:
                    # extract lead noun phrase
                    match = re.match(r"^([^,.;\n]+)", text)
                    if match and len(match.group(1)) > 3:
                        keywords.add(match.group(1).strip())

    # 2. Add question-specific high-impact triggers based on question content & explanation
    # Identify key triggers in prompt that match explanation concepts
    key_patterns = [
        r"(?:without requiring|no)\s+(?:reserved throughput|PTU|capacity)",
        r"variable\s+(?:customer support\s+)?traffic",
        r"dynamically scale",
        r"remain consistent(?:\s+to ensure stable responses)?",
        r"data(?:\s+processed by the model)?\s+must remain within the (?:EU|region)",
        r"Prompt Shields?",
        r"malicious instructions(?:\s+potentially hidden within the images)?",
        r"centrally manage(?:\s+the Azure AI Search credentials)?",
        r"connection to the Azure AI Search resource",
        r"OTEL_SERVICE_NAME",
        r"enable_content_recording\s*=\s*False",
        r"DefaultAzureCredential",
        r"Principle of least privilege",
        r"Managed Identity",
        r"Semantic and vector search",
        r"Azure AI Document Intelligence",
        r"Evaluation metrics",
        r"Groundedness",
        r"Coherence",
        r"Relevance",
        r"Fluency",
        r"Simulated chat",
        r"Human-in-the-loop",
        r"System-assigned managed identity",
        r"Storage Blob Data Reader",
        r"Azure OpenAI",
        r"Cosmos DB",
        r"Vector index",
        r"Hybrid search",
        r"Semantic ranker",
        r"Tool invocation",
        r"Custom skill",
        r"Content Safety",
        r"Prompt injection",
        r"Jailbreak",
        r"Fine-tuning",
        r"RAG",
        r"Retrieval Augmented Generation",
        r"Token limit",
        r"Rate limit",
        r"TPM",
        r"RPM",
        r"Deployment type",
        r"Version update policy",
        r"Once the current version expires",
        r"Standard",
        r"Global Standard",
        r"Provisioned"
    ]

    for pat in key_patterns:
        matches = re.findall(pat, prompt, re.IGNORECASE)
        for m in matches:
            if len(m.strip()) > 3:
                keywords.add(m.strip())
        exp_matches = re.findall(pat, explanation, re.IGNORECASE)
        for m in exp_matches:
            if len(m.strip()) > 3:
                keywords.add(m.strip())

    # 3. Extract key technical phrases from explanation highlights
    # E.g. "Why ... is the best option", "Selected as ... because ..."
    because_matches = re.findall(r"(?:because|Selected as|Why\s+[A-Z0-9\s]+is)\s+([^.\n]{10,90})", explanation, re.IGNORECASE)
    for bm in because_matches[:3]:
        cleaned = re.sub(r"^(the|a|an|to|for)\s+", "", bm.strip(), flags=re.IGNORECASE)
        # pick key noun/verb phrases
        if len(cleaned) < 50 and len(cleaned) > 5:
            keywords.add(cleaned)

    # 4. Clean and filter keywords
    filtered = []
    for kw in sorted(keywords, key=lambda x: -len(x)):
        kw_clean = kw.strip().strip(":;\"'()[]")
        if (
            len(kw_clean) >= 3
            and not kw_clean.lower() in ["why", "because", "the", "and", "that", "this", "with", "from", "for", "select", "note", "question", "correct", "option", "statements"]
            and not any(kw_clean.lower() == existing.lower() for existing in filtered)
        ):
            # verify it exists in prompt, explanation, or options
            in_prompt = kw_clean.lower() in prompt.lower()
            in_exp = kw_clean.lower() in explanation.lower()
            in_opts = any(kw_clean.lower() in o.get("text", "").lower() for o in options)
            in_ans = any(kw_clean.lower() in item.get("value", "").lower() for item in answer_items)
            
            if in_prompt or in_exp or in_opts or in_ans:
                filtered.append(kw_clean)

    # Deduplicate substrings if redundant
    final_kws = []
    for f in filtered:
        # Keep high-quality tokens (cap at top 8 per question to avoid noise)
        if len(final_kws) < 8:
            final_kws.append(f)

    # Fallback if empty
    if not final_kws:
        if answer_items:
            final_kws = [item["value"] for item in answer_items if item.get("value")][:5]
        elif c_opts and options:
            final_kws = [opt["text"] for opt in options if opt["id"] in c_opts][:3]

    return final_kws

updated_count = 0
for q in questions:
    kws = extract_smart_keywords(q)
    q["keywords"] = kws
    if kws:
        updated_count += 1

print(f"Assigned keywords to {updated_count} / {len(questions)} questions.")

# Save back to JSON
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

# Update lib/questions.ts
ts_content = """export type Option = {
  id: string;
  text: string;
  whyIncorrect?: string;
};

export type AnswerItem = {
  label: string;
  value: string;
  options?: string[];
};

export type QuestionUIFormat = "single-choice" | "multi-choice" | "dropdown-matrix" | "yes-no-matrix" | "drag-drop";

export type Question = {
  id: string;
  number: number;
  type: "Single Choice" | "Multiple Choice" | "Hotspot" | "Drag Drop" | "Unknown";
  uiFormat?: QuestionUIFormat;
  prompt: string;
  options: Option[];
  answer: string;
  answerItems?: AnswerItem[];
  correctOptionIds: string[];
  explanation: string;
  reasoning: string[];
  keywords: string[];
  sourcePages?: number[];
  warnings?: string[];
};

export const questions: Question[] = """ + json.dumps(questions, indent=2, ensure_ascii=False) + ";\n"

with open(TS_PATH, "w", encoding="utf-8") as f:
    f.write(ts_content)

print(f"Successfully synced question-bank.json and lib/questions.ts!")
