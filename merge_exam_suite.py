import json
import os
import generate_exhaustive_exam

def merge_and_update():
    # 1. Load existing 48 questions
    with open(r"D:\vhdl\exam_questions.json", "r", encoding="utf-8") as f:
        existing_questions = json.load(f)

    # 2. Generate the 56 new lab questions
    new_questions = generate_exhaustive_exam.build_questions()

    # 3. Combine without duplicate IDs
    seen_ids = set()
    combined = []
    
    # Add new lab questions first or combine
    for q in existing_questions:
        if q["id"] not in seen_ids:
            seen_ids.add(q["id"])
            combined.append(q)

    for q in new_questions:
        if q["id"] not in seen_ids:
            seen_ids.add(q["id"])
            combined.append(q)

    # Sort by week, then by type
    combined.sort(key=lambda x: (x.get("week", 0), x.get("type", "")))

    print(f"Total unified questions: {len(combined)}")

    # Statistics
    by_week = {}
    by_type = {}
    by_origin = {}
    for q in combined:
        w = q.get("week", 0)
        by_week[w] = by_week.get(w, 0) + 1
        t = q.get("type", "")
        by_type[t] = by_type.get(t, 0) + 1
        orig = q.get("origin", "")
        by_origin[orig] = by_origin.get(orig, 0) + 1

    print("Questions by Week:", sorted(by_week.items()))
    print("Questions by Type:", by_type)
    print("Questions by Origin:", by_origin)

    # 4. Save to exam_questions.json
    with open(r"D:\vhdl\exam_questions.json", "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print("Successfully updated D:\\vhdl\\exam_questions.json")

    # 5. Update exam_practice.html with embedded questions
    with open(r"D:\vhdl\exam_practice.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    json_str = json.dumps(combined, ensure_ascii=False)
    
    # Replace the allQuestions array in HTML
    prefix = "const allQuestions = "
    start_pos = html_content.find(prefix)
    if start_pos != -1:
        start_idx = start_pos + len(prefix)
        # find the ending semicolon of const allQuestions = [...];
        # parse json to find length
        decoder = json.JSONDecoder()
        _, end_offset = decoder.raw_decode(html_content[start_idx:])
        end_idx = start_idx + end_offset
        if html_content[end_idx] == ';':
            end_idx += 1
        new_html = html_content[:start_pos] + f"const allQuestions = {json_str};" + html_content[end_idx:]
        with open(r"D:\vhdl\exam_practice.html", "w", encoding="utf-8") as f:
            f.write(new_html)
        print("Successfully updated D:\\vhdl\\exam_practice.html with all questions!")
    else:
        print("ERROR: Could not find const allQuestions in exam_practice.html")

if __name__ == "__main__":
    merge_and_update()
