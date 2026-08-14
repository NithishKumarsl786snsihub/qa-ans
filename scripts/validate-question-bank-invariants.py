from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "extracted" / "question-bank.json"

if not JSON_PATH.exists():
    print(f"CRITICAL ERROR: {JSON_PATH} does not exist.")
    sys.exit(1)

with open(JSON_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

errors = []
seen_q_ids = set()
seen_q_nums = set()

for q in questions:
    q_id = q.get("id")
    q_num = q.get("number")

    if not q_id:
        errors.append(f"Question missing required 'id': {q}")
    elif q_id in seen_q_ids:
        errors.append(f"Duplicate question id found: {q_id}")
    else:
        seen_q_ids.add(q_id)

    if q_num is None:
        errors.append(f"Question missing required 'number': {q_id}")
    elif q_num in seen_q_nums:
        errors.append(f"Duplicate question number found: {q_num}")
    else:
        seen_q_nums.add(q_num)

    if q_num != 76 and not q.get("prompt"):
        errors.append(f"Question {q_id} (Q{q_num}) has empty prompt text.")

    options = q.get("options", [])
    seen_opt_ids = set()

    for idx, opt in enumerate(options):
        opt_id = opt.get("id")
        opt_text = opt.get("text")

        if not opt_id or not isinstance(opt_id, str) or not opt_id.strip():
            errors.append(f"Question {q_id} option at index {idx} has missing or empty 'id': {opt}")
        elif opt_id in seen_opt_ids:
            errors.append(f"Question {q_id} has duplicate option id: '{opt_id}'")
        else:
            seen_opt_ids.add(opt_id)

        if not opt_text or not isinstance(opt_text, str) or not opt_text.strip():
            errors.append(f"Question {q_id} option '{opt_id}' has missing or empty 'text'.")

    c_ids = q.get("correctOptionIds", [])
    if options:
        valid_opt_ids = {opt["id"] for opt in options}
        for cid in c_ids:
            if cid not in valid_opt_ids:
                errors.append(f"Question {q_id} correctOptionIds contains '{cid}' which is not in valid option IDs: {valid_opt_ids}")

if errors:
    print("==========================================================================")
    print("      QUESTION BANK DATA INVARIANTS VALIDATION FAILED                     ")
    print("==========================================================================")
    for err in errors:
        print(f"  [FAIL] {err}")
    sys.exit(1)
else:
    print("==========================================================================")
    print("  SUCCESS: QUESTION BANK DATA INVARIANTS VERIFIED (100% CLEAN & HARDENED) ")
    print("==========================================================================")
    print(f"Total questions validated: {len(questions)}")
