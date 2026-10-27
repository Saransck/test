import os

def update_exam_practice_py():
    path = r"D:\vhdl\exam_practice.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_block = """        if choice == "1":
            clear_screen()
            print_header("เลือกสัปดาห์ที่ต้องการฝึกทำ")
            for w in range(2, 9):
                w_count = sum(1 for q in questions if q['week'] == w)
                print(f"  [{w}] Week {w} (มีข้อสอบ {w_count} ข้อ)")
            print("  [0] กลับเมนูหลัก")
            print("-" * 80)
            w_choice = input("เลือกสัปดาห์ [2-8 หรือ 0]: ").strip()
            if w_choice in [str(i) for i in range(2, 9)]:
                target_w = int(w_choice)
                sub_q = [q for q in questions if q['week'] == target_w]
                run_quiz(sub_q, f"แบบทดสอบ Week {target_w}")"""

    new_block = """        if choice == "1":
            clear_screen()
            print_header("เลือกสัปดาห์ / แล็บที่ต้องการฝึกทำ")
            weeks_available = sorted(list(set(q["week"] for q in questions)))
            for w in weeks_available:
                w_count = sum(1 for q in questions if q["week"] == w)
                label = f"Lab {w} (AES)" if w == 9 else (f"Lab {w} (SoC)" if w == 11 else f"Week {w}")
                print(f"  [{w}] {label} (มีข้อสอบ {w_count} ข้อ)")
            print("  [0] กลับเมนูหลัก")
            print("-" * 80)
            avail_str = ", ".join(str(w) for w in weeks_available)
            w_choice = input(f"เลือกสัปดาห์ [{avail_str} หรือ 0]: ").strip()
            if w_choice.isdigit() and int(w_choice) in weeks_available:
                target_w = int(w_choice)
                sub_q = [q for q in questions if q["week"] == target_w]
                w_lbl = f"Lab {target_w} (AES)" if target_w == 9 else (f"Lab {target_w} (SoC)" if target_w == 11 else f"Week {target_w}")
                run_quiz(sub_q, f"แบบทดสอบ {w_lbl}")"""

    # Normalize line endings for replacement
    content_norm = content.replace("\r\n", "\n")
    old_block_norm = old_block.replace("\r\n", "\n")
    new_block_norm = new_block.replace("\r\n", "\n")

    if old_block_norm in content_norm:
        content_norm = content_norm.replace(old_block_norm, new_block_norm)
        content_norm = content_norm.replace("sample_size = min(20, len(questions))", "sample_size = min(25, len(questions))")
        content_norm = content_norm.replace("Mock Exam (20 ข้อ)", "Mock Exam (25 ข้อ)")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content_norm)
        print("Updated exam_practice.py successfully.")
    else:
        print("Could not find old_block in exam_practice.py.")

if __name__ == "__main__":
    update_exam_practice_py()
