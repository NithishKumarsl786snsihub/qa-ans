import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "extracted" / "question-bank.json"
CHEAT_SHEET_PATH = ROOT / "EXAM_CHEAT_SHEET.md"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

lines = []
lines.append("# 🔥 AI Apps & Agents on Azure — Master Pattern-Recognition Cheat Sheet\n")
lines.append("> **Exam Strategy**: Don't read whole paragraphs. Scan for **Primary Triggers** $\\rightarrow$ **Mark Answer in 5 Seconds**.\n\n---\n")

def get_answer_summary(q):
    options = q.get("options", [])
    if q.get("answerItems"):
        resolved_items = []
        for item in q["answerItems"]:
            lbl = item.get("label", "")
            val = item.get("value", "")
            if lbl.lower() in ["correct option", "answer"] and options:
                opt_match = next((o for o in options if o.get("id") == val), None)
                if opt_match:
                    resolved_items.append(f"**Option {val}** ({opt_match.get('text', '')})")
                else:
                    resolved_items.append(f"**{lbl}**: `{val}`")
            else:
                resolved_items.append(f"**{lbl}**: `{val}`")
        return ", ".join(resolved_items)
    if q.get("correctOptionIds") and options:
        opts = [f"**Option {opt['id']}** ({opt['text']})" for opt in options if opt['id'] in q["correctOptionIds"]]
        return ", ".join(opts)
    if options and q.get("answer"):
        opt_match = [f"**Option {opt['id']}** ({opt['text']})" for opt in options if opt["id"].strip().upper() == q.get("answer", "").strip().upper()]
        if opt_match:
            return ", ".join(opt_match)
    return f"**{q.get('answer', 'See question details')}**"

def extract_primary_triggers(q):
    kws = q.get("keywords", [])
    if kws:
        return kws[:4]
    return ["Review scenario context"]

for q in questions:
    num = q.get("number")
    if num == 76 or not q.get("prompt"):
        continue
    
    q_type = q.get("type", "Question")
    ans_text = get_answer_summary(q)
    triggers = extract_primary_triggers(q)
    
    lines.append(f"### 📌 Question {num} — {q_type}\n")
    
    # Trigger Table
    lines.append("| 🔥 If the Case / Prompt says... | ✅ Immediately Mark... |")
    lines.append("| :--- | :--- |")
    
    for tr in triggers:
        lines.append(f"| **\"{tr}\"** | $\\rightarrow$ {ans_text} |")
    
    # Short summary rule
    exp_snippet = q.get("explanation", "").strip()
    if exp_snippet:
        first_sentence = exp_snippet.split(". ")[0].replace("\n", " ").strip()
        if len(first_sentence) > 160:
            first_sentence = first_sentence[:160] + "..."
        lines.append(f"\n> 🧠 **Memory Anchor**: *{first_sentence}*\n")
    
    lines.append("\n---\n")

with open(CHEAT_SHEET_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Generated EXAM_CHEAT_SHEET.md with {len(questions)} questions.")
