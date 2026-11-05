#!/usr/bin/env python3
import json
import os
import subprocess
import sys

BASE_DIR = "/home/cgslinde/DrillRoom/DrillRoom"
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch/cars9")
if SCRATCH_DIR not in sys.path:
    sys.path.insert(0, SCRATCH_DIR)

from validator import validate_passage, count_words
from p1 import passage_data as p1
from p2 import passage_data as p2
from p3 import passage_data as p3
from p4 import passage_data as p4
from p5 import passage_data as p5
from p6 import passage_data as p6
from p7 import passage_data as p7
from p8 import passage_data as p8
from p9 import passage_data as p9

passages = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

def main():
    print("=" * 70)
    print("COMPILING & VALIDATING EXAM 9 (CARS 90-MIN, 9 PASSAGES, 53 QUESTIONS)")
    print("=" * 70)

    total_errors = []
    total_qs = 0
    answer_dist = {0: 0, 1: 0, 2: 0, 3: 0}
    letters = ['A', 'B', 'C', 'D']
    expected_q_counts = [6, 6, 6, 6, 6, 6, 6, 6, 5]

    for i, p in enumerate(passages, 1):
        target_qc = expected_q_counts[i - 1]
        wc, errs = validate_passage(p, target_qc)
        total_errors.extend(errs)
        n_qs = len(p["qs"])
        total_qs += n_qs
        print(f"Passage {i} ({p['id']}): {wc} words, {n_qs} questions — Topic: {p['topic']}")
        for q in p["qs"]:
            answer_dist[q["a"]] += 1

    print("-" * 70)
    print(f"Total Passages: {len(passages)}")
    print(f"Total Questions: {total_qs}")
    print(f"Answer Key Distribution: A={answer_dist[0]}, B={answer_dist[1]}, C={answer_dist[2]}, D={answer_dist[3]}")

    actual_q_counts = [len(p["qs"]) for p in passages]
    if actual_q_counts != expected_q_counts:
        total_errors.append(f"Question distribution error: expected {expected_q_counts}, got {actual_q_counts}")

    if total_qs != 53:
        total_errors.append(f"Total questions error: expected 53, got {total_qs}")

    # Verify target distribution: exactly 13 A, 13 B, 14 C, 13 D
    expected_dist = {0: 13, 1: 13, 2: 14, 3: 13}
    if answer_dist != expected_dist:
        total_errors.append(f"Answer distribution mismatch: expected {expected_dist}, got {answer_dist}")

    if total_errors:
        print("\nVALIDATION ERRORS:")
        for err in total_errors:
            print("  [ERROR]", err)
        sys.exit(1)

    print("\nALL 9 PASSAGES AND 53 QUESTIONS PASSED SPECIFICATION VALIDATION!")

    # Write exam_cars90_9.js
    output_js_path = os.path.join(BASE_DIR, "exam_cars90_9.js")
    js_content = "/* ---- exam_cars90_9.js ---- */\n/* Full 90-minute CARS Practice Exam 9: 9 passages (53 Qs) */\nconst EXAM_CARS90_9 = "
    js_content += json.dumps(passages, indent=2, ensure_ascii=False)
    js_content += ";\n"

    with open(output_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"\nWritten {output_js_path} ({os.path.getsize(output_js_path)} bytes)")

    # Syntax check with Node
    node_bin = "/home/cgslinde/node-v24.22.0-linux-x64/bin/node"
    node_res = subprocess.run([node_bin, "-c", output_js_path], capture_output=True, text=True)
    if node_res.returncode != 0:
        print("\nNODE SYNTAX ERROR:")
        print(node_res.stderr)
        sys.exit(1)
    print("Node.js syntax validation: SUCCESSFUL (-c passed)")

    # Deep verification in node
    node_verify_code = f"""
    const fs = require('fs');
    const content = fs.readFileSync('{output_js_path}', 'utf8');
    let EXAM_CARS90_9;
    eval(content.replace('const EXAM_CARS90_9 =', 'EXAM_CARS90_9 ='));
    if (!Array.isArray(EXAM_CARS90_9)) {{
        console.error('EXAM_CARS90_9 is not an array');
        process.exit(1);
    }}
    if (EXAM_CARS90_9.length !== 9) {{
        console.error('Expected 9 passages, got ' + EXAM_CARS90_9.length);
        process.exit(1);
    }}
    let totalQs = 0;
    const keys = {{0: 0, 1: 0, 2: 0, 3: 0}};
    EXAM_CARS90_9.forEach((p, pIdx) => {{
        if (!p.id || !p.sec || !p.topic || !p.label || !p.examId || !p.passage || !Array.isArray(p.qs)) {{
            console.error('Passage ' + pIdx + ' missing required keys');
            process.exit(1);
        }}
        totalQs += p.qs.length;
        p.qs.forEach((q, qIdx) => {{
            if (!q.q || !Array.isArray(q.ch) || q.ch.length !== 4 || typeof q.a !== 'number' || !q.e) {{
                console.error('Passage ' + pIdx + ' Q ' + qIdx + ' malformed');
                process.exit(1);
            }}
            keys[q.a]++;
        }});
    }});
    if (totalQs !== 53) {{
        console.error('Expected 53 questions, got ' + totalQs);
        process.exit(1);
    }}
    console.log('Node verification passed: 9 passages, 53 questions. Key dist:', keys);
    """
    node_verify_res = subprocess.run([node_bin, "-e", node_verify_code], capture_output=True, text=True)
    if node_verify_res.returncode != 0:
        print("\nNODE EXECUTION VERIFICATION ERROR:")
        print(node_verify_res.stderr)
        sys.exit(1)
    print("Node.js runtime evaluation: SUCCESSFUL")
    print(node_verify_res.stdout.strip())

if __name__ == "__main__":
    main()
