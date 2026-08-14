from __future__ import annotations

import json
import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "Developing AI Apps and Agents on Azure - dump.pdf"
OUT_DIR = ROOT / "extracted"
OUT_JSON = OUT_DIR / "question-bank.json"
OUT_MD = OUT_DIR / "question-bank.md"
OUT_TS = ROOT / "lib" / "questions.ts"

QUESTION_RE = re.compile(r"(?m)^Question:\s*(\d+)\s*$")
ANSWER_RE = re.compile(r"(?m)^[ \t]*Answer:[ \t]*(.*)$")
EXPLANATION_RE = re.compile(r"(?m)^[ \t]*Explanation:[ \t]*$")
OPTION_RE = re.compile(r"^\s*([A-H])\.\s+(.+)")

MANUAL_OVERRIDES: dict[int, dict] = {
    1: {
        "answer": "Deployment type: Standard; Version update policy: Once the current version expires",
    },
    4: {
        "answer": "Statement 1: No; Statement 2: Yes; Statement 3: No",
    },
    5: {
        "answer": "Pipeline1: Single-file task in standard mode; Pipeline2: Multi-file task in pro mode",
    },
    6: {
        "answer": "First dropdown: DefaultAzureCredential; Second dropdown: create",
    },
    7: {
        "answer": "If/else condition expression: Not(IsBlank(Local.Var01)); Send message expression: Upper(Local.Var01)",
    },
    8: {
        "answer": "Guardrails: User input, Output, Tool response, and Tool call with Action set to Block; Storage access: System-assigned managed identity assigned Storage Blob Data Reader",
    },
    11: {
        "answer": "Approval step type: ask_question; Refund condition: approval == \"approved\"",
        "explanation": "ask_question pauses workflow execution to collect human approval. The execute_refund step should run only when the approval output equals \"approved\".",
    },
    15: {
        "answer": "Unsupported responses: Groundedness evaluation metrics; Policy violations: Risk and safety metrics",
    },
    18: {
        "answer": "Metrics to enable: Model Availability Rate and Provisioned Utilization; Diagnostic log to collect: Request Response",
    },
    20: {
        "answer": "Set tool_choice to required; configure the tool to authenticate by using a distinct agent identity bound to the client application",
    },
    30: {
        "answer": "Parameter: tool_choice; Value: required",
    },
    32: {
        "answer": "Access up-to-date public information: Grounding with Bing Search; Perform calculations: Code interpreter; Retrieve uploaded documents: File search",
    },
    35: {
        "answer": "temperature: 1; output_config effort: low",
    },
    37: {
        "answer": "Retain user preferences: Agent memory that uses persistent storage; Contextual grounding during chats: File search tool",
    },
    40: {
        "answer": "Authentication method: Azure Login action that uses OpenID Connect (OIDC); Workflow action on failure: Fail",
    },
    49: {
        "answer": "Prompt Shields action: Set action to block; Additional mitigation: Enable Spotlighting",
    },
    79: {
        "answer": "Workflow logic: Condition/decision branch for risk; Approval checkpoint: Ask for approval / Ask a question node",
    },
    86: {
        "answer": "Field value type: string; Field method: generate; Prompt: Describe the color scheme of the video segment",
    },
    117: {
        "answer": "JSON data: Object projection; Extracted text data: Table projection",
    },
}


def page_text_blocks(doc: fitz.Document) -> list[tuple[int, float, str]]:
    blocks: list[tuple[int, float, str]] = []
    for page_index, page in enumerate(doc, start=1):
        page_blocks = sorted(page.get_text("blocks"), key=lambda item: (item[1], item[0]))
        for block in page_blocks:
            x0, y0, _x1, _y1, text, *_rest = block
            normalized = "\n".join(line.rstrip() for line in text.splitlines()).strip()
            if normalized:
                blocks.append((page_index, y0, normalized))
    return blocks


def normalized_document_text(doc: fitz.Document) -> str:
    chunks: list[str] = []
    for page_no, _y, text in page_text_blocks(doc):
        chunks.append(f"\n[[PAGE {page_no}]]\n{text}")
    return "\n".join(chunks)


def clean_lines(text: str) -> list[str]:
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("[[PAGE "):
            continue
        lines.append(line)
    return lines


def parse_options(lines: list[str]) -> tuple[list[dict], list[str]]:
    options: list[dict] = []
    body: list[str] = []
    current: dict | None = None
    for line in lines:
        match = OPTION_RE.match(line)
        if match:
            current = {"id": match.group(1), "text": match.group(2).strip()}
            options.append(current)
            continue
        if current and not line.startswith(("Answer:", "Explanation:")):
            # Wrapped option text usually follows directly after its option marker.
            if not re.match(r"^[A-H]\b", line) and len(line.split()) <= 18:
                current["text"] = f"{current['text']} {line}".strip()
                continue
        body.append(line)
    return options, body


def answer_ids(answer: str) -> list[str]:
    answer = answer.strip()
    if not answer:
        return []
    if not re.fullmatch(r"[A-H](?:\s*[,;/&]?\s*[A-H])*", answer.upper()):
        return []
    compact = re.sub(r"[^A-H]", "", answer.upper())
    if compact:
        return list(dict.fromkeys(compact))
    return []


def answer_items(answer: str, correct_ids: list[str]) -> list[dict]:
    answer = answer.strip()
    if not answer:
        return []
    if ";" in answer:
        rows = []
        for part in answer.split(";"):
            part = part.strip()
            if not part:
                continue
            if ":" in part:
                label, value = part.split(":", 1)
                rows.append({"label": label.strip(), "value": value.strip()})
            else:
                rows.append({"label": "Answer", "value": part})
        return rows
    if correct_ids and answer.upper().replace(" ", "") == "".join(correct_ids):
        label = "Correct option" if len(correct_ids) == 1 else "Correct options"
        return [{"label": label, "value": ", ".join(correct_ids)}]
    if ":" in answer and len(answer) < 220:
        label, value = answer.split(":", 1)
        return [{"label": label.strip(), "value": value.strip()}]
    return [{"label": "Answer", "value": answer}]


def question_type(text: str, correct_ids: list[str]) -> str:
    upper = text.upper()
    if "DRAG DROP" in upper:
        return "Drag Drop"
    if "HOTSPOT" in upper:
        return "Hotspot"
    if len(correct_ids) > 1:
        return "Multiple Choice"
    return "Single Choice"


def split_sections(block: str) -> tuple[str, str, str]:
    answer = ""
    explanation = ""
    before_answer = block
    answer_match = ANSWER_RE.search(block)
    if answer_match:
        before_answer = block[: answer_match.start()]
        after_answer = block[answer_match.end() :]
        answer = answer_match.group(1).strip()
        explanation_match = EXPLANATION_RE.search(after_answer)
        if explanation_match:
            if not answer:
                answer = "\n".join(clean_lines(after_answer[: explanation_match.start()])).strip()
            explanation = after_answer[explanation_match.end() :].strip()
        elif not answer:
            answer = "\n".join(clean_lines(after_answer)).strip()
    return before_answer.strip(), answer.strip(), explanation.strip()


def extract_questions() -> list[dict]:
    doc = fitz.open(str(PDF))
    text = normalized_document_text(doc)
    matches = list(QUESTION_RE.finditer(text))
    parsed: list[dict] = []

    for index, match in enumerate(matches):
        number = int(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        pages = sorted({int(p) for p in re.findall(r"\[\[PAGE (\d+)\]\]", block)})
        question_block, answer, explanation = split_sections(block)
        lines = clean_lines(question_block)
        options, prompt_lines = parse_options(lines)
        prompt = " ".join(prompt_lines)
        correct_ids = answer_ids(answer)
        parsed.append(
            {
                "id": f"q-{number:03d}",
                "number": number,
                "type": question_type(question_block, correct_ids),
                "prompt": prompt,
                "options": options,
                "answer": answer,
                "correctOptionIds": correct_ids,
                "answerItems": answer_items(answer, correct_ids),
                "explanation": " ".join(clean_lines(explanation)) if explanation else "",
                "reasoning": [],
                "keywords": [],
                "sourcePages": pages,
                "warnings": [],
            }
        )

    seen = {item["number"] for item in parsed}
    missing = [number for number in range(1, 118) if number not in seen]
    # The PDF contains an unlabeled question 11 on page 17. Preserve it explicitly.
    if 11 in missing:
        page17 = doc[16].get_text("text", sort=True)
        before_answer, answer, explanation = split_sections(page17)
        lines = clean_lines(before_answer)
        options, prompt_lines = parse_options(lines)
        parsed.append(
            {
                "id": "q-011",
                "number": 11,
                "type": "Hotspot",
                "prompt": " ".join(prompt_lines),
                "options": options,
                "answer": answer,
                "correctOptionIds": answer_ids(answer),
                "answerItems": answer_items(answer, answer_ids(answer)),
                "explanation": "",
                "reasoning": [],
                "keywords": [],
                "sourcePages": [17, 18],
                "warnings": ["Question label was missing in the PDF text; reconstructed from page 17."],
            }
        )

    parsed.sort(key=lambda item: item["number"])
    for item in parsed:
        override = MANUAL_OVERRIDES.get(item["number"])
        if not override:
            continue
        for key, value in override.items():
            item[key] = value
        item["correctOptionIds"] = answer_ids(item["answer"])
        item["answerItems"] = answer_items(item["answer"], item["correctOptionIds"])
        item["warnings"].append("Answer manually captured from the rendered PDF visual answer area.")

    seen = {item["number"] for item in parsed}
    for item in parsed:
        if not item["prompt"]:
            item["warnings"].append("Prompt text is empty or not extractable from PDF text layer.")
        if not item["answer"]:
            item["warnings"].append("Answer is blank or uses a visual answer area.")
        if not item["options"] and item["type"] in {"Single Choice", "Multiple Choice"}:
            item["warnings"].append("Options were not detected as A./B./C. text.")
        if item["answer"] and not item["correctOptionIds"] and item["type"] in {"Single Choice", "Multiple Choice"}:
            item["warnings"].append("Answer text is not a simple option id.")

    if 76 not in seen:
        parsed.append(
            {
                "id": "q-076",
                "number": 76,
                "type": "Unknown",
                "prompt": "",
                "options": [],
                "answer": "",
                "correctOptionIds": [],
                "answerItems": [],
                "explanation": "",
                "reasoning": [],
                "keywords": [],
                "sourcePages": [],
                "warnings": ["Question 76 is not present in the PDF numbering; source jumps from 75 to 77."],
            }
        )
        parsed.sort(key=lambda item: item["number"])

    return parsed


def ts_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_ts(questions: list[dict]) -> None:
    lines = [
        "export type Option = {",
        "  id: string;",
        "  text: string;",
        "  whyIncorrect?: string;",
        "};",
        "",
        "export type Question = {",
        "  id: string;",
        "  number: number;",
        '  type: "Single Choice" | "Multiple Choice" | "Hotspot" | "Drag Drop" | "Unknown";',
        "  prompt: string;",
        "  options: Option[];",
        "  answer: string;",
        "  answerItems?: Array<{ label: string; value: string }>;",
        "  correctOptionIds: string[];",
        "  explanation: string;",
        "  reasoning: string[];",
        "  keywords: string[];",
        "  sourcePages?: number[];",
        "  warnings?: string[];",
        "};",
        "",
        "export const questions: Question[] = [",
    ]
    for q in questions:
        lines.append("  {")
        lines.append(f'    id: {ts_string(q["id"])},')
        lines.append(f'    number: {q["number"]},')
        lines.append(f'    type: {ts_string(q["type"])},')
        lines.append(f'    prompt: {ts_string(q["prompt"])},')
        lines.append("    options: [")
        for option in q["options"]:
            lines.append(
                f'      {{ id: {ts_string(option["id"])}, text: {ts_string(option["text"])}, whyIncorrect: "" }},'
            )
        lines.append("    ],")
        lines.append(f'    answer: {ts_string(q["answer"])},')
        lines.append(f'    answerItems: {json.dumps(q["answerItems"], ensure_ascii=False)},')
        lines.append(f'    correctOptionIds: {json.dumps(q["correctOptionIds"])},')
        lines.append(f'    explanation: {ts_string(q["explanation"])},')
        lines.append("    reasoning: [],")
        lines.append("    keywords: [],")
        lines.append(f'    sourcePages: {json.dumps(q["sourcePages"])},')
        lines.append(f'    warnings: {json.dumps(q["warnings"])},')
        lines.append("  },")
    lines.append("];")
    OUT_TS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_markdown(questions: list[dict]) -> None:
    lines = ["# Extracted Question Bank", ""]
    lines.append(f"Source PDF: `{PDF.name}`")
    lines.append("")
    for q in questions:
        lines.append(f"## Question {q['number']}")
        lines.append("")
        if q["sourcePages"]:
            lines.append(f"Source pages: {', '.join(str(page) for page in q['sourcePages'])}")
            lines.append("")
        if q["warnings"]:
            lines.append("Extraction notes:")
            for warning in q["warnings"]:
                lines.append(f"- {warning}")
            lines.append("")
        lines.append(q["prompt"] or "_No prompt text extracted._")
        lines.append("")
        if q["options"]:
            lines.append("Options:")
            for option in q["options"]:
                lines.append(f"- {option['id']}. {option['text']}")
            lines.append("")
        lines.append(f"Answer: {q['answer'] or '_No answer text extracted._'}")
        lines.append("")
        if q["explanation"]:
            lines.append("Explanation:")
            lines.append(q["explanation"])
            lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    questions = extract_questions()
    OUT_JSON.write_text(json.dumps(questions, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(questions)
    write_ts(questions)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"wrote {OUT_TS}")
    print(f"items: {len(questions)}")
    print("warnings:", sum(1 for q in questions if q["warnings"]))
    print("missing prompts:", [q["number"] for q in questions if not q["prompt"]])


if __name__ == "__main__":
    main()
