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

OPTION_PREFIX_RE = re.compile(r"^\s*([A-H])[\.\:\)]\s+(.+)")
FORMAT_HEADERS_RE = re.compile(r"^(?:HOTSPOT|DRAG\s+DROP|MULTIPLE\s+CHOICE|SINGLE\s+CHOICE)(?:\s*[-:])?\s*", re.IGNORECASE)
FORMAT_HEADERS = {"HOTSPOT", "DRAG DROP", "MULTIPLE CHOICE", "SINGLE CHOICE"}
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H"]

INTERACTIVE_SCENARIOS = {
    1: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Deployment type",
                "value": "Standard",
                "options": ["Standard", "Global Standard", "Provisioned", "Global Provisioned"]
            },
            {
                "label": "Version update policy",
                "value": "Once the current version expires",
                "options": ["Once the current version expires", "Opt out of automatic model version upgrades", "Upgrade once a new default version becomes available"]
            }
        ]
    },
    4: {
        "uiFormat": "yes-no-matrix",
        "answerItems": [
            {
                "label": "The LangChain service will appear in Traces without configuring a tracer.",
                "value": "No",
                "options": ["Yes", "No"]
            },
            {
                "label": "Setting different OTEL_SERVICE_NAME values separates the services in Application Insights.",
                "value": "Yes",
                "options": ["Yes", "No"]
            },
            {
                "label": "When using enable_content_recording=False, prompts and tool data will be captured in the telemetry.",
                "value": "No",
                "options": ["Yes", "No"]
            }
        ]
    },
    5: {
        "uiFormat": "drag-drop",
        "answerItems": [
            {
                "label": "Pipeline1",
                "value": "Single-file task in standard mode",
                "options": ["Single-file task in standard mode", "Single-file task in pro mode", "Multi-file task in standard mode", "Multi-file task in pro mode"]
            },
            {
                "label": "Pipeline2",
                "value": "Multi-file task in pro mode",
                "options": ["Single-file task in standard mode", "Single-file task in pro mode", "Multi-file task in standard mode", "Multi-file task in pro mode"]
            }
        ]
    },
    6: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "First Dropdown (credential =)",
                "value": "DefaultAzureCredential",
                "options": ["DefaultAzureCredential", "AzureKeyVaultCredential", "ManagedIdentityCredential", "ClientSecretCredential"]
            },
            {
                "label": "Second Dropdown (response = openai_client.responses.)",
                "value": "create",
                "options": ["create", "compact", "retrieve", "execute"]
            }
        ]
    },
    7: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "If/else condition expression",
                "value": "Not(IsBlank(Local.Var01))",
                "options": ["Not(IsBlank(Local.Var01))", "IsBlank(Local.Var01)", "IsEmpty(Local.Var01)", "Not(IsEmpty(Local.Var01))"]
            },
            {
                "label": "Send message expression",
                "value": "Upper(Local.Var01)",
                "options": ["Upper(Local.Var01)", "Text.Upper(Local.Var01)", "String.ToUpper(Local.Var01)", "Capitalize(Local.Var01)"]
            }
        ]
    },
    8: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Guardrails configuration",
                "value": "Select User input, Output, Tool response, and Tool call; set Action to Block",
                "options": [
                    "Select User input, Output, Tool response, and Tool call; set Action to Block",
                    "Select User input and Output; set Action to Allow",
                    "Select Tool response only; set Action to Audit",
                    "Select User input only; set Action to Mask"
                ]
            },
            {
                "label": "Storage access configuration",
                "value": "System-assigned managed identity assigned Storage Blob Data Reader",
                "options": [
                    "System-assigned managed identity assigned Storage Blob Data Reader",
                    "Account API Key with full access",
                    "User-assigned identity with Owner role",
                    "Anonymous public read access"
                ]
            }
        ]
    },
    11: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Approval step type",
                "value": "ask_question",
                "options": ["ask_question", "basic_chat", "data_transformation"]
            },
            {
                "label": "Refund condition",
                "value": "approval == \"approved\"",
                "options": ["approval == \"approved\"", "propose_refund.output != null", "true"]
            }
        ]
    },
    15: {
        "uiFormat": "drag-drop",
        "answerItems": [
            {
                "label": "Unsupported responses",
                "value": "Groundedness evaluation metrics",
                "options": ["Groundedness evaluation metrics", "Risk and safety metrics", "Latency breakdown traces", "Indexer status history"]
            },
            {
                "label": "Policy violations",
                "value": "Risk and safety metrics",
                "options": ["Groundedness evaluation metrics", "Risk and safety metrics", "Latency breakdown traces", "Indexer status history"]
            }
        ]
    },
    18: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Metrics to enable",
                "value": "Model Availability Rate and Provisioned Utilization",
                "options": [
                    "Model Availability Rate and Provisioned Utilization",
                    "HTTP Status Codes and Error Rate",
                    "Latency Breakdown and Token Count",
                    "Request Volume and Active Connections"
                ]
            },
            {
                "label": "Diagnostic log to collect",
                "value": "Request Response",
                "options": ["Request Response", "Audit Logs", "Trace Spans", "Error Traces"]
            }
        ]
    },
    20: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Parameter",
                "value": "tool_choice",
                "options": ["tool_choice", "function_call", "run_option", "execution_mode"]
            },
            {
                "label": "Value",
                "value": "required",
                "options": ["required", "auto", "none", "forced"]
            }
        ]
    },
    30: {
        "uiFormat": "drag-drop",
        "answerItems": [
            {
                "label": "Parameter",
                "value": "tool_choice",
                "options": ["tool_choice", "function_call", "tool_mode", "execution_policy"]
            },
            {
                "label": "Value",
                "value": "required",
                "options": ["required", "auto", "none", "strict"]
            }
        ]
    },
    32: {
        "uiFormat": "drag-drop",
        "answerItems": [
            {
                "label": "Access up-to-date public information",
                "value": "Grounding with Bing Search",
                "options": ["Grounding with Bing Search", "Code interpreter", "File search", "Custom Web Search"]
            },
            {
                "label": "Perform calculations",
                "value": "Code interpreter",
                "options": ["Grounding with Bing Search", "Code interpreter", "File search", "Math Engine"]
            },
            {
                "label": "Retrieve uploaded documents",
                "value": "File search",
                "options": ["Grounding with Bing Search", "Code interpreter", "File search", "Document Store"]
            }
        ]
    },
    35: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "temperature",
                "value": "1",
                "options": ["0", "0.5", "0.7", "1"]
            },
            {
                "label": "output_config effort",
                "value": "low",
                "options": ["low", "medium", "high", "none"]
            }
        ]
    },
    37: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Retain user preferences across chat sessions",
                "value": "Agent memory that uses persistent storage",
                "options": [
                    "Agent memory that uses persistent storage",
                    "File search tool",
                    "Session context cache",
                    "Browser local storage"
                ]
            },
            {
                "label": "Contextual grounding during chats",
                "value": "File search tool",
                "options": [
                    "Agent memory that uses persistent storage",
                    "File search tool",
                    "Bing Grounding tool",
                    "Code Interpreter tool"
                ]
            }
        ]
    },
    40: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Authentication method",
                "value": "Azure Login action that uses OpenID Connect (OIDC)",
                "options": [
                    "Azure Login action that uses OpenID Connect (OIDC)",
                    "Service Principal with client secret",
                    "Personal Access Token (PAT)",
                    "API Key in GitHub Secrets"
                ]
            },
            {
                "label": "Workflow action on failure",
                "value": "Fail",
                "options": ["Fail", "Continue", "Skip", "Warn"]
            }
        ]
    },
    49: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Prompt Shields action",
                "value": "Set action to block",
                "options": ["Set action to block", "Set action to audit", "Set action to warn", "Set action to ignore"]
            },
            {
                "label": "Additional mitigation",
                "value": "Enable Spotlighting",
                "options": ["Enable Spotlighting", "Enable PII Masking", "Enable Content Filter", "Enable Rate Limiting"]
            }
        ]
    },
    77: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "session_id",
                "value": "user_id",
                "options": ["user_id", "session_context", "auto_id", "client_guid"]
            },
            {
                "label": "storage_type",
                "value": "session",
                "options": ["session", "global", "ephemeral", "temporary"]
            }
        ]
    },
    79: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "Workflow logic",
                "value": "Condition/decision branch for risk",
                "options": [
                    "Condition/decision branch for risk",
                    "Loop iterator node",
                    "Parallel execution branch",
                    "Exception handler node"
                ]
            },
            {
                "label": "Approval checkpoint",
                "value": "Ask for approval / Ask a question node",
                "options": [
                    "Ask for approval / Ask a question node",
                    "Auto-approve node",
                    "Send email notification node",
                    "Log event node"
                ]
            }
        ]
    },
    86: {
        "uiFormat": "drag-drop",
        "answerItems": [
            {
                "label": "Field value type",
                "value": "string",
                "options": ["string", "object", "array", "boolean"]
            },
            {
                "label": "Field method",
                "value": "generate",
                "options": ["generate", "extract", "lookup", "transform"]
            },
            {
                "label": "Prompt",
                "value": "Describe the color scheme of the video segment",
                "options": [
                    "Describe the color scheme of the video segment",
                    "Extract text overlay from the video",
                    "Identify keyframes in the video",
                    "Detect faces in the video"
                ]
            }
        ]
    },
    93: {
        "uiFormat": "yes-no-matrix",
        "answerItems": [
            {
                "label": "Can detect custom objects without model deployment",
                "value": "Yes",
                "options": ["Yes", "No"]
            },
            {
                "label": "Can extract structured JSON from unstructured text",
                "value": "No",
                "options": ["Yes", "No"]
            },
            {
                "label": "Can preserve document layout and table bounds",
                "value": "Yes",
                "options": ["Yes", "No"]
            }
        ]
    },
    94: {
        "uiFormat": "drag-drop",
        "answerItems": [
            {
                "label": "Telemetry tracking signal 1",
                "value": "Trace context",
                "options": ["Trace context", "Custom dimensions", "Event log", "Metric payload"]
            },
            {
                "label": "Telemetry tracking signal 2",
                "value": "Custom dimensions",
                "options": ["Trace context", "Custom dimensions", "Event log", "Metric payload"]
            }
        ]
    },
    95: {
        "uiFormat": "drag-drop",
        "answerItems": [
            {
                "label": "HTTP 429 Error Resolution",
                "value": "Implement exponential backoff retry logic",
                "options": [
                    "Implement exponential backoff retry logic",
                    "Validate file size against model limits before upload",
                    "Increase VM vCPU quota",
                    "Switch to key-based auth"
                ]
            },
            {
                "label": "HTTP 400 Error Resolution",
                "value": "Validate file size against model limits before upload",
                "options": [
                    "Implement exponential backoff retry logic",
                    "Validate file size against model limits before upload",
                    "Increase VM vCPU quota",
                    "Switch to key-based auth"
                ]
            }
        ]
    },
    101: {
        "uiFormat": "yes-no-matrix",
        "answerItems": [
            {
                "label": "Vision API detects brand logos in images",
                "value": "Yes",
                "options": ["Yes", "No"]
            },
            {
                "label": "Returns confidence scores for brand detection",
                "value": "Yes",
                "options": ["Yes", "No"]
            },
            {
                "label": "Requires pre-training custom vision model",
                "value": "No",
                "options": ["Yes", "No"]
            }
        ]
    },
    107: {
        "uiFormat": "yes-no-matrix",
        "answerItems": [
            {
                "label": "Redacts PII before sending prompt to model",
                "value": "Yes",
                "options": ["Yes", "No"]
            },
            {
                "label": "Stores unmasked PII in Application Insights",
                "value": "No",
                "options": ["Yes", "No"]
            },
            {
                "label": "Preserves original sentence context for model",
                "value": "Yes",
                "options": ["Yes", "No"]
            }
        ]
    },
    108: {
        "uiFormat": "drag-drop",
        "answerItems": [
            {
                "label": "Step 1",
                "value": "Create a project",
                "options": ["Create a project", "Upload and tag images", "Train and publish the model", "Configure API endpoint"]
            },
            {
                "label": "Step 2",
                "value": "Upload and tag images",
                "options": ["Create a project", "Upload and tag images", "Train and publish the model", "Configure API endpoint"]
            },
            {
                "label": "Step 3",
                "value": "Train and publish the model",
                "options": ["Create a project", "Upload and tag images", "Train and publish the model", "Configure API endpoint"]
            }
        ]
    },
    117: {
        "uiFormat": "dropdown-matrix",
        "answerItems": [
            {
                "label": "JSON data projection type",
                "value": "Object projection",
                "options": ["Object projection", "Table projection", "File projection", "Vector projection"]
            },
            {
                "label": "Extracted text data projection type",
                "value": "Table projection",
                "options": ["Object projection", "Table projection", "File projection", "Vector projection"]
            }
        ]
    }
}


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


def get_all_blocks(doc: fitz.Document) -> list[dict]:
    all_blocks = []
    for page_idx, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")
        sorted_blocks = sorted(blocks, key=lambda b: (b[1], b[0]))
        for b in sorted_blocks:
            x0, y0, _x1, _y1, text, *_rest = b
            clean_t = text.strip()
            if clean_t:
                all_blocks.append({"page": page_idx, "x0": x0, "y0": y0, "text": clean_t})
    return all_blocks


def extract_questions() -> list[dict]:
    doc = fitz.open(str(PDF))
    all_blocks = get_all_blocks(doc)

    q_indices = []
    expected_q_num = 1

    for idx, b in enumerate(all_blocks):
        m = re.match(r"^Question:\s*(\d+)$", b["text"])
        if m:
            found_num = int(m.group(1))
            q_indices.append((idx, found_num))
            expected_q_num = found_num + 1
        else:
            first_line = b["text"].splitlines()[0].strip().upper() if b["text"] else ""
            if first_line.startswith("HOTSPOT") or first_line.startswith("DRAG DROP") or first_line.startswith("MULTIPLE CHOICE"):
                prev_b = all_blocks[idx - 1] if idx > 0 else None
                if prev_b and ("Answer:" in prev_b["text"] or "Explanation:" in prev_b["text"] or prev_b["page"] < b["page"]):
                    if not any(q[1] == expected_q_num for q in q_indices):
                        q_indices.append((idx, expected_q_num))
                        expected_q_num += 1

    q_indices.sort(key=lambda item: item[0])
    parsed_questions = []

    for i, (b_idx, q_num) in enumerate(q_indices):
        next_b_idx = q_indices[i + 1][0] if i + 1 < len(q_indices) else len(all_blocks)

        hdr_text = all_blocks[b_idx]["text"]
        hdr_clean_prompt = FORMAT_HEADERS_RE.sub("", hdr_text).strip()
        if hdr_clean_prompt.startswith("Question:"):
            hdr_clean_prompt = ""

        q_block_range = all_blocks[b_idx + 1 : next_b_idx]
        pages = sorted(list(set(b["page"] for b in [all_blocks[b_idx]] + q_block_range)))

        ans_idx = -1
        ans_str = ""
        for r_idx, b in enumerate(q_block_range):
            if b["text"].startswith("Answer:") or b["text"].startswith("Answer :") or "\nAnswer:" in b["text"]:
                ans_idx = r_idx
                m_ans = re.search(r"Answer:\s*(.*)", b["text"])
                if m_ans:
                    ans_str = m_ans.group(1).strip()
                break

        if ans_idx == -1:
            before_ans = q_block_range
            after_ans = []
        else:
            before_ans = q_block_range[:ans_idx]
            after_ans = q_block_range[ans_idx:]
            if not ans_str and ans_idx + 1 < len(q_block_range):
                next_text = q_block_range[ans_idx + 1]["text"]
                if not next_text.startswith("Explanation:") and not next_text.startswith("Question:"):
                    ans_str = next_text

        explanation_parts = []
        in_exp = False
        for b in after_ans:
            if "Explanation:" in b["text"]:
                in_exp = True
                exp_text = b["text"].split("Explanation:", 1)[1].strip()
                if exp_text:
                    explanation_parts.append(exp_text)
            elif in_exp:
                if not b["text"].startswith("Question:"):
                    explanation_parts.append(b["text"])

        explanation = " ".join(explanation_parts).strip()

        if not ans_str and explanation:
            m_exp_ans = re.search(
                r"(?i)^(Approval step type:[^\n]+|First Dropdown:[^\n]+(?:\nSecond Dropdown:[^\n]+)?|Pipeline1[^\n]+|Guardrails[^\n]+|Set tool_choice[^\n]+|Authentication method[^\n]+|Prompt shields action[^\n]+|Deployment type:[^\n]+)",
                explanation,
            )
            if m_exp_ans:
                ans_str = m_exp_ans.group(1).strip()

        prompt_parts = []
        if hdr_clean_prompt:
            prompt_parts.append(hdr_clean_prompt)

        options = []

        prefixed_opts = []
        for b in before_ans:
            for line in b["text"].splitlines():
                m_opt = OPTION_PREFIX_RE.match(line)
                if m_opt:
                    prefixed_opts.append({"id": m_opt.group(1), "text": m_opt.group(2).strip()})

        if prefixed_opts:
            options = prefixed_opts
            for b in before_ans:
                is_opt = False
                for line in b["text"].splitlines():
                    if OPTION_PREFIX_RE.match(line):
                        is_opt = True
                        break
                if not is_opt:
                    prompt_parts.append(b["text"])
        else:
            cand_opts = []
            for b in before_ans:
                if b["x0"] > 45 and not b["text"].startswith("DRAG DROP") and not b["text"].startswith("HOTSPOT"):
                    lines = [l.strip() for l in b["text"].splitlines() if l.strip()]
                    for l in lines:
                        cand_opts.append(l)
                else:
                    prompt_parts.append(b["text"])

            if cand_opts:
                for opt_idx, opt_text in enumerate(cand_opts):
                    if opt_idx < len(LETTERS):
                        options.append({"id": LETTERS[opt_idx], "text": opt_text})

            # Generic Missing Option Fallback (DEF-002 Fix Part 3 & 4)
            if not options and explanation:
                exp_opts = re.findall(r"(?m)^\s*([A-D])[\.\:]\s+([^\n\r]+)", explanation)
                if exp_opts:
                    seen_opt_ids = set()
                    dedup_opts = []
                    for opt_id, opt_txt in exp_opts:
                        opt_txt = re.sub(r"\s*\(Correct Answer\)", "", opt_txt, flags=re.IGNORECASE).strip()
                        if opt_id not in seen_opt_ids and opt_txt and not opt_txt.startswith("Technical") and not opt_txt.startswith("Why"):
                            seen_opt_ids.add(opt_id)
                            dedup_opts.append({"id": opt_id, "text": opt_txt})
                    if len(dedup_opts) >= 2:
                        options = dedup_opts

        c_ids = answer_ids(ans_str)

        full_text = "\n".join([b["text"] for b in [all_blocks[b_idx]] + q_block_range])
        q_type = "Single Choice"
        if "DRAG DROP" in full_text.upper():
            q_type = "Drag Drop"
        elif "HOTSPOT" in full_text.upper():
            q_type = "Hotspot"
        elif len(c_ids) > 1:
            q_type = "Multiple Choice"

        # Generic Option Reconciliation for missing answer IDs and incomplete choice lists
        if c_ids and q_type in ["Single Choice", "Multiple Choice"]:
            valid_opt_ids = {opt["id"] for opt in options}
            for cid in c_ids:
                if cid not in valid_opt_ids and explanation:
                    m = re.search(fr"(?:^|\n|\s)({cid})[\.\:]\s*([^\n\r\:\.\(\)]+)", explanation)
                    if m:
                        opt_text = re.sub(r"\s*\(Correct Answer\)", "", m.group(2), flags=re.IGNORECASE).strip()
                        if opt_text and not opt_text.startswith("Technical") and not opt_text.startswith("Why"):
                            options.append({"id": cid, "text": opt_text})
                            valid_opt_ids.add(cid)

            # Determine required letter range (e.g. up to 'E' if 'E' is in c_ids, otherwise 'A'..'D')
            max_idx = max(3, max(LETTERS.index(c) for c in c_ids if c in LETTERS) if c_ids else 3)
            needed_letters = LETTERS[: max_idx + 1]

            for letter in needed_letters:
                if letter not in valid_opt_ids and (letter in c_ids or len(options) < len(needed_letters)):
                    options.append({"id": letter, "text": f"Option {letter} (Visual Block)"})
                    valid_opt_ids.add(letter)

            options.sort(key=lambda o: o["id"])

        warnings = []
        if not options and q_type in ["Single Choice", "Multiple Choice"]:
            warnings.append("Options extracted via visual graphic fallback.")
            if c_ids or ans_str in LETTERS:
                options = [
                    {"id": "A", "text": "Option A (Visual Image Block)"},
                    {"id": "B", "text": "Option B (Visual Image Block)"},
                    {"id": "C", "text": "Option C (Visual Image Block)"},
                    {"id": "D", "text": "Option D (Visual Image Block)"},
                ]

        a_items = answer_items(ans_str, c_ids)

        ui_format = "single-choice"
        if q_type == "Multiple Choice":
            ui_format = "multi-choice"

        if q_num in INTERACTIVE_SCENARIOS:
            a_items = INTERACTIVE_SCENARIOS[q_num]["answerItems"]
            ui_format = INTERACTIVE_SCENARIOS[q_num]["uiFormat"]

        parsed_questions.append({
            "id": f"q-{q_num:03d}",
            "number": q_num,
            "type": q_type,
            "uiFormat": ui_format,
            "prompt": " ".join(prompt_parts).strip(),
            "options": options,
            "answer": ans_str,
            "answerItems": a_items,
            "correctOptionIds": c_ids,
            "explanation": explanation,
            "reasoning": [],
            "keywords": [],
            "sourcePages": pages,
            "warnings": warnings,
        })

    seen_nums = {q["number"] for q in parsed_questions}
    if 76 not in seen_nums:
        parsed_questions.append({
            "id": "q-076",
            "number": 76,
            "type": "Unknown",
            "uiFormat": "single-choice",
            "prompt": "",
            "options": [],
            "answer": "",
            "answerItems": [],
            "correctOptionIds": [],
            "explanation": "",
            "reasoning": [],
            "keywords": [],
            "sourcePages": [],
            "warnings": ["Question 76 is not present in the PDF numbering; source jumps from 75 to 77."],
        })

    parsed_questions.sort(key=lambda item: item["number"])
    return parsed_questions


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
        "export type AnswerItem = {",
        "  label: string;",
        "  value: string;",
        "  options?: string[];",
        "};",
        "",
        'export type QuestionUIFormat = "single-choice" | "multi-choice" | "dropdown-matrix" | "yes-no-matrix" | "drag-drop";',
        "",
        "export type Question = {",
        "  id: string;",
        "  number: number;",
        '  type: "Single Choice" | "Multiple Choice" | "Hotspot" | "Drag Drop" | "Unknown";',
        "  uiFormat?: QuestionUIFormat;",
        "  prompt: string;",
        "  options: Option[];",
        "  answer: string;",
        "  answerItems?: AnswerItem[];",
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
        lines.append(f'    uiFormat: {ts_string(q.get("uiFormat", "single-choice"))},')
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
    lines = ["# Extracted Question Bank", "", f"Source PDF: `{PDF.name}`", ""]
    for q in questions:
        lines.append(f"## Question {q['number']}")
        lines.append("")
        if q["sourcePages"]:
            lines.append(f"Source pages: {', '.join(str(page) for page in q['sourcePages'])}")
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


if __name__ == "__main__":
    main()
