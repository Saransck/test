#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
โปรแกรมฝึกทำข้อสอบ Digital Circuit Design with Verilog HDL (Week 2 - Week 8)
ระบุแหล่งที่มาชัดเจนว่ามาจาก LECTURE (สไลด์บรรยาย) หรือ LAB (ใบงานปฏิบัติการ)
รองรับข้อสอบ 3 รูปแบบ:
1. ปรนัย 4 ตัวเลือก (A, B, C, D)
2. เติมโค้ด Verilog โดยมีตัวเลือก (A, B, C, D)
3. ข้อสอบ ถูก / ผิด (True / False)
"""

import json
import os
import random
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_questions():
    filepath = os.path.join(os.path.dirname(__file__), "exam_questions.json")
    if not os.path.exists(filepath):
        print(f"Error: ไม่พบไฟล์ {filepath}")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def print_header(title=""):
    print("=" * 80)
    print("  ระบบทดสอบความรู้: Digital Circuit Design with Verilog HDL (Week 2-8)")
    if title:
        print(f"  >> {title}")
    print("=" * 80)

def run_quiz(selected_questions, title="แบบทดสอบ"):
    if not selected_questions:
        print("ไม่มีข้อสอบในหมวดที่เลือก!")
        input("\nกด Enter เพื่อกลับสู่เมนูหลัก...")
        return

    score = 0
    total = len(selected_questions)
    week_stats = {}
    origin_stats = {"lec": [0, 0], "lab": [0, 0], "both": [0, 0]}
    type_stats = {"choice": [0, 0], "code_fill": [0, 0], "tf": [0, 0]}

    for idx, q in enumerate(selected_questions, 1):
        clear_screen()
        w = q["week"]
        q_type = q["type"]
        q_origin = q.get("origin", "both")

        week_stats.setdefault(w, {"total": 0, "correct": 0})
        week_stats[w]["total"] += 1
        type_stats[q_type][1] += 1
        origin_stats[q_origin][1] += 1

        type_names = {
            "choice": "🔤 ปรนัย 4 ตัวเลือก (A B C D)",
            "code_fill": "💻 เติมโค้ด Verilog โดยมีตัวเลือก (A B C D)",
            "tf": "⚖️ ถูก / ผิด (True / False)"
        }

        origin_badges = {
            "lec": "📚 มาจาก: LECTURE (สไลด์บรรยาย)",
            "lab": "🧪 มาจาก: LAB (ใบงานปฏิบัติการ)",
            "both": "📘 มาจาก: ทั้ง LECTURE และ LAB"
        }

        print("=" * 80)
        print(f" ข้อที่ {idx}/{total}  |  Week {q['week']}  |  {type_names.get(q_type, q_type)}")
        print(f" ที่มา: {origin_badges.get(q_origin, q.get('origin_th', ''))}")
        print(f" หัวข้อ: {q['topic']}")
        print("=" * 80)
        print(f"\n{q['question']}\n")

        opt_labels = ["A", "B", "C", "D"] if q_type in ['choice', 'code_fill'] else ["1", "2"]
        for opt_idx, opt in enumerate(q['options']):
            lbl = opt_labels[opt_idx]
            print(f"   [{lbl}]  {opt}")

        print("\n" + "-" * 80)
        while True:
            choice = input(f" คำตอบของคุณ ({'/'.join(opt_labels)} หรือ Q เพื่อออก): ").strip().upper()
            if choice == "Q":
                print("\nยกเลิกการทำข้อสอบ กลับสู่เมนูหลัก...")
                return
            if choice in opt_labels:
                chosen_idx = opt_labels.index(choice)
                break
            print(" >> กรุณาพิมพ์ตัวเลือกที่ถูกต้อง!")

        correct_idx = q["answer_index"]
        is_correct = (chosen_idx == correct_idx)

        print("\n" + "=" * 80)
        if is_correct:
            score += 1
            week_stats[w]["correct"] += 1
            type_stats[q_type][0] += 1
            origin_stats[q_origin][0] += 1
            print(" [ ✓ ถูกต้อง! / CORRECT ]")
        else:
            print(f" [ ✗ ไม่ถูกต้อง! / INCORRECT ]")
            print(f"   คำตอบที่ถูกต้องคือ: [{opt_labels[correct_idx]}] {q['options'][correct_idx]}")

        print("\n 💡 คำอธิบายเชิงเทคนิค:")
        print(f"   {q['explanation']}")
        print(f"\n 📌 แหล่งอ้างอิงชัดเจนตามเอกสาร:")
        print(f"   [{q.get('origin_th', '')}]")
        print(f"   รายละเอียด: {q['source']}")
        print("=" * 80)

        if idx < total:
            input("\nกด Enter เพื่อไปข้อถัดไป...")

    # Summary
    clear_screen()
    print_header("สรุปผลการทดสอบ")
    percent = (score / total) * 100
    print(f"\n คะแนนรวมของคุณ: {score} / {total} ข้อ ({percent:.1f}%)\n")
    
    if percent >= 80:
        grade = "ยอดเยี่ยม (Excellent) - มีความพร้อมสอบระดับสูงมาก"
    elif percent >= 60:
        grade = "ผ่านเกณฑ์ดี (Good) - ควรอ่านทบทวนหัวข้อที่ผิดพลาดเพิ่มเติม"
    else:
        grade = "ต้องปรับปรุง (Needs Review) - แนะนำให้อ่านคู่มือสรุป Lab และ Lec อีกครั้ง"

    print(f" การประเมิน: {grade}\n")

    print("-" * 65)
    print(" สรุปผลแยกตามแหล่งที่มา (Lec / Lab):")
    print("-" * 65)
    for o_key, o_label in [("lec", "📚 มาจาก LECTURE (สไลด์บรรยาย)"), 
                          ("lab", "🧪 มาจาก LAB (ใบงานปฏิบัติการ)"), 
                          ("both", "📘 มาจากทั้ง LECTURE และ LAB")]:
        c, t = origin_stats[o_key]
        if t > 0:
            print(f"  • {o_label}: {c}/{t} ข้อ ({(c/t)*100:.0f}%)")

    print("\n" + "-" * 65)
    print(" สรุปผลแยกตามรูปแบบข้อสอบ:")
    print("-" * 65)
    for t_key, t_label in [("choice", "🔤 ปรนัย 4 ตัวเลือก (A B C D)"), 
                          ("code_fill", "💻 เติมโค้ด Verilog (A B C D)"), 
                          ("tf", "⚖️ ถูก / ผิด (True / False)")]:
        c, t = type_stats[t_key]
        if t > 0:
            print(f"  • {t_label}: {c}/{t} ข้อ ({(c/t)*100:.0f}%)")

    print("\n" + "-" * 65)
    print(" สรุปผลแยกตามสัปดาห์ (Week 2 - Week 8):")
    print("-" * 65)
    for w in sorted(week_stats.keys()):
        st = week_stats[w]
        w_pct = (st['correct'] / st['total']) * 100 if st['total'] > 0 else 0
        print(f"  • Week {w}: ได้ {st['correct']}/{st['total']} ข้อ ({w_pct:.0f}%)")
    print("=" * 80)
    input("\nกด Enter เพื่อกลับสู่เมนูหลัก...")

def review_mode(questions):
    clear_screen()
    print_header("โหมดทบทวนเฉลยและแหล่งอ้างอิงทั้งหมด")
    for idx, q in enumerate(questions, 1):
        print(f"\n[{idx}/{len(questions)}] Week {q['week']} | {q['topic']}")
        print(f"ที่มา: {q.get('origin_th', '')}")
        print(f"รูปแบบ: {q['type']}")
        print(f"โจทย์: {q['question']}")
        corr_idx = q['answer_index']
        opt_lbl = ["A", "B", "C", "D"] if q['type'] in ['choice', 'code_fill'] else ["1", "2"]
        print(f"เฉลย: [{opt_lbl[corr_idx]}] {q['options'][corr_idx]}")
        print(f"คำอธิบาย: {q['explanation']}")
        print(f"แหล่งอ้างอิง: {q['source']}")
        print("-" * 80)
        if idx % 5 == 0 and idx < len(questions):
            cont = input("พิมพ์ C เพื่ออ่านต่อ หรือ Q เพื่อออก: ").strip().upper()
            if cont == "Q":
                break
    input("\nกด Enter เพื่อกลับสู่เมนูหลัก...")

def main():
    questions = load_questions()

    while True:
        clear_screen()
        print_header("เมนูหลัก")
        print("  1. 📘 ฝึกทำข้อสอบแยกตามสัปดาห์ (Week 2 ถึง Week 8)")
        print("  2. 🏛️ ฝึกทำข้อสอบแยกตามแหล่งที่มา (เฉพาะ LECTURE หรือเฉพาะ LAB)")
        print("  3. 🔍 ฝึกทำเฉพาะรูปแบบข้อสอบ (A B C D, เติมโค้ด, หรือ ถูก/ผิด)")
        print("  4. 📝 จำลองสอบ Comprehensive Mock Exam (สุ่ม 20 ข้อจากทุกหมวด)")
        print("  5. 📖 โหมดทบทวนเฉลยและแหล่งอ้างอิงทั้งหมด (Review Mode)")
        print("  6. 🚪 ออกจากโปรแกรม")
        print("=" * 80)
        
        lec_c = sum(1 for q in questions if q.get('origin') == 'lec')
        lab_c = sum(1 for q in questions if q.get('origin') == 'lab')
        both_c = sum(1 for q in questions if q.get('origin') == 'both')
        print(f"  คลังข้อสอบทั้งหมด: {len(questions)} ข้อ (Lec: {lec_c}, Lab: {lab_c}, ทั้งสองส่วน: {both_c})")
        print("-" * 80)
        
        choice = input("กรุณาเลือกเมนู [1-6]: ").strip()

        if choice == "1":
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
                run_quiz(sub_q, f"แบบทดสอบ {w_lbl}")

        elif choice == "2":
            clear_screen()
            print_header("เลือกแหล่งที่มาของข้อสอบ")
            print("  [1] 📚 ข้อสอบจาก LECTURE (สไลด์บรรยาย) เท่านั้น")
            print("  [2] 🧪 ข้อสอบจาก LAB (ใบงานปฏิบัติการ) เท่านั้น")
            print("  [3] 📘 ข้อสอบที่เชื่อมโยงทั้ง LECTURE และ LAB")
            print("  [0] กลับเมนูหลัก")
            print("-" * 80)
            o_choice = input("เลือกแหล่งที่มา [1-3 หรือ 0]: ").strip()
            if o_choice == "1":
                sub_q = [q for q in questions if q.get('origin') == 'lec']
                run_quiz(sub_q, "แบบทดสอบเฉพาะเนื้อหา LECTURE (สไลด์บรรยาย)")
            elif o_choice == "2":
                sub_q = [q for q in questions if q.get('origin') == 'lab']
                run_quiz(sub_q, "แบบทดสอบเฉพาะเนื้อหา LAB (ใบงานปฏิบัติการ)")
            elif o_choice == "3":
                sub_q = [q for q in questions if q.get('origin') == 'both']
                run_quiz(sub_q, "แบบทดสอบเนื้อหาที่เชื่อมโยงทั้ง LECTURE และ LAB")

        elif choice == "3":
            clear_screen()
            print_header("เลือกรูปแบบข้อสอบที่ต้องการฝึก")
            print("  [1] 🔤 ปรนัย 4 ตัวเลือก (A, B, C, D) [ทฤษฎี & วิเคราะห์]")
            print("  [2] 💻 เติมโค้ด Verilog โดยมีตัวเลือก (A, B, C, D) [Code Completion]")
            print("  [3] ⚖️ ข้อสอบ ถูก / ผิด (True / False)")
            print("  [0] กลับเมนูหลัก")
            print("-" * 80)
            t_choice = input("เลือกรูปแบบ [1-3 หรือ 0]: ").strip()
            if t_choice == "1":
                sub_q = [q for q in questions if q['type'] == 'choice']
                run_quiz(sub_q, "แบบทดสอบเฉพาะ ปรนัย 4 ตัวเลือก (A, B, C, D)")
            elif t_choice == "2":
                sub_q = [q for q in questions if q['type'] == 'code_fill']
                run_quiz(sub_q, "แบบทดสอบเฉพาะ เติมโค้ด Verilog โดยมีตัวเลือก (A, B, C, D)")
            elif t_choice == "3":
                sub_q = [q for q in questions if q['type'] == 'tf']
                run_quiz(sub_q, "แบบทดสอบเฉพาะ ถูก / ผิด (True / False)")

        elif choice == "4":
            sample_size = min(25, len(questions))
            mock_q = random.sample(questions, sample_size)
            run_quiz(mock_q, f"Comprehensive Mock Exam ({sample_size} ข้อ)")

        elif choice == "5":
            review_mode(questions)

        elif choice == "6":
            print("\nขอบคุณที่ใช้งาน ขอให้โชคดีในการสอบครับ!\n")
            break

if __name__ == "__main__":
    main()
