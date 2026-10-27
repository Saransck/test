import json

def fix_topics():
    with open(r"D:\vhdl\exam_questions.json", "r", encoding="utf-8") as f:
        qs = json.load(f)

    for q in qs:
        if "topic" not in q:
            q["topic"] = q.get("origin_th", f"Week {q['week']}")

    with open(r"D:\vhdl\exam_questions.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    print("All questions now have 'topic' field.")

if __name__ == "__main__":
    fix_topics()
