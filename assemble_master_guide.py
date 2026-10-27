import json
import os
import re

def assemble_master_guide():
    transcript_path = r"C:\Users\User\.gemini\antigravity\brain\f7c936b0-2c8e-4337-a124-aaaa17e457e6\.system_generated\logs\transcript_full.jsonl"
    with open(transcript_path, "r", encoding="utf-8") as f:
        lines = [json.loads(l) for l in f]

    # 1. Week 2
    w2_lec = lines[19]["content"].strip()
    w2_lab_raw = lines[75]["content"].strip()
    w2_lab_start = w2_lab_raw.find("# 🧪 เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ: Practice Lab Sheet 2")
    if w2_lab_start != -1:
        w2_lab = w2_lab_raw[w2_lab_start:].strip()
    else:
        w2_lab = w2_lab_raw

    # 2. Week 3
    w3_raw = lines[123]["content"].strip()
    w3_split = "# 🧪 Week 3 – Lab 3: Foundations & Language Basics (BCD Adder on DE1)"
    w3_idx = w3_raw.find(w3_split)
    w3_lec = w3_raw[:w3_idx].strip()
    w3_lab = w3_raw[w3_idx:].strip()

    # 3. Week 4
    w4_raw = lines[153]["content"].strip()
    w4_split = "# 🧪 Week 4 – Lab 4: Combinational Logic (ALU & Decoders)"
    w4_idx = w4_raw.find(w4_split)
    w4_lec = w4_raw[:w4_idx].strip()
    w4_lab = w4_raw[w4_idx:].strip()

    # 4. Week 5
    w5_raw = lines[187]["content"].strip()
    w5_split = "# 🧪 Week 5 – Lab 5: Sequential Logic: Flip-Flops & Registers"
    w5_idx = w5_raw.find(w5_split)
    w5_lec = w5_raw[:w5_idx].strip()
    w5_lab = w5_raw[w5_idx:].strip()

    # 5. Week 6
    w6_raw = lines[324]["content"].strip()
    w6_split = "# 🧪 Week 6 – Lab 6: Counters, Clock/PLL & Shift Registers"
    w6_idx = w6_raw.find(w6_split)
    w6_lec = w6_raw[:w6_idx].strip()
    w6_lab = w6_raw[w6_idx:].strip()

    # 6. Week 7
    w7_raw = lines[407]["content"].strip()
    w7_split = "## 🧪 Week 7 – Lab 7: การออกแบบ Finite State Machine (FSM): Combination Lock System"
    w7_idx = w7_raw.find(w7_split)
    w7_lec = w7_raw[:w7_idx].strip()
    w7_lab = w7_raw[w7_idx:].strip()

    # 7. Week 8
    w8_raw = lines[461]["content"].strip()
    w8_split = "## 🧪 Week 8 – Lab 8: Testbench Design & Functional Verification"
    w8_idx = w8_raw.find(w8_split)
    w8_table_marker = "# 🎓 ตารางสรุปภาพรวมเนื้อหาการเรียนรู้ตลอดหลักสูตร (Week 2 – Week 8)"
    w8_table_idx = w8_raw.find(w8_table_marker)
    w8_lec = w8_raw[:w8_idx].strip()
    w8_lab = w8_raw[w8_idx:w8_table_idx].strip()
    summary_table = w8_raw[w8_table_idx:].strip()

    # Special Labs: Lab 9 & Lab 11
    lab9_text = """
---

<a name="lab-9"></a>
# 📘 Lab 9 (Special): การออกแบบวงจร AES-128 Encryption ด้วย Generative AI
**แหล่งอ้างอิง:** [lab9_Lab_AES128_Encryption 1.pdf](file:///d:/vhdl/lab/lab9_Lab_AES128_Encryption%201.pdf) (หน้าที่ 1–12)

### 1. วัตถุประสงค์และสเปกมาตรฐาน (หน้าที่ 1–3)
- วงจรรับ Plaintext ขนาด 128 บิต (16 ไบต์) และ Cipher Key ขนาด 128 บิต เข้าคำนวณ Ciphertext ขนาด 128 บิต ตามมาตรฐาน NIST FIPS-197
- วงจรทำหน้าที่เข้ารหัส (Encryption) เพียงอย่างเดียว ทำงานแบบ Synchronous Sequential

### 2. ลำดับขั้นตอนการทำงาน 10 Rounds ของ AES-128 (หน้าที่ 3)
1. **Round 0:** `state = plaintext XOR round_key[0]` (ทำเฉพาะ **AddRoundKey** เท่านั้น)
2. **Round 1 ถึง 9:** ทำครบ 4 ขั้นตอน:
   - `SubBytes`: การแทนที่ไบต์แบบ Non-linear ผ่านตาราง S-Box
   - `ShiftRows`: การเลื่อนไบต์ในแต่ละแถวของ State Matrix
   - `MixColumns`: การคูณเชิงเมทริกซ์ในฟีลด์จำกัด Galois Field GF(2^8) เพื่อกระจายบิต (Diffusion)
   - `AddRoundKey`: นำ State มา XOR กับกุญแจย่อยประจำรอบ `round_key[r]`
3. **Round 10 (รอบสุดท้าย):** 
   - `state = AddRoundKey( ShiftRows( SubBytes(state) ), round_key[10] )`
   - **ข้อควรระวังสำคัญ:** ใน **Round 10 จะไม่มีขั้นตอน MixColumns** โดยเด็ดขาดตามมาตรฐานสากล

### 3. หลักการคณิตศาสตร์ของ S-Box (หน้าที่ 4)
- S-Box ไม่ใช่การสุ่มค่า แต่สร้างขึ้นจาก **GF(2^8) Multiplicative Inverse** ร่วมกับ **Affine Transformation** เหนือ $GF(2)$ เพื่อสร้างคุณสมบัติ Confusion ที่สูงสุด
"""

    lab11_text = """
---

<a name="lab-11"></a>
# 📘 Lab 11 (Special): ตัวนับขึ้น/ลงบน 7-Segment ด้วย RV32I SoC
**แหล่งอ้างอิง:** [Lab11_SoC_7seg_Counter.pdf](file:///d:/vhdl/lab/Lab11_SoC_7seg_Counter.pdf) (หน้าที่ 1–4)

### 1. โครงสร้างหน่วยประมวลผลและการจัดสรรหน่วยความจำ (Memory Map) (หน้าที่ 2)
- ระบบใช้ซอฟต์คอร์ซีพียู RISC-V สถาปัตยกรรม **RV32I Single-Cycle**
- **แผนที่หน่วยความจำ (Address Decoder `addr_decoder.v` จากบิต `addr[31:28]`):**
  - `0x0000_0000`: Instruction ROM (`imem.v`) โหลดจากไฟล์ไบนารี `main.hex`
  - `0x1000_0000`: Data RAM (`dmem.v`) สำหรับตัวแปรและ Stack
  - `0x2000_0000`: Memory-Mapped I/O Registers สำหรับควบคุมจอ 7-Segment และปุ่มกด

### 2. การแบ่งหน้าที่ระหว่างฮาร์ดแวร์และซอฟต์แวร์ (Hardware/Software Co-Design) (หน้าที่ 3–4)
- **ฮาร์ดแวร์ (`hex7seg.v`):** ทำหน้าที่ถอดรหัสเลขฐานสอง 4 บิต (0–F) ออกเป็นสัญญาณติดดับของแต่ละขีด 7 ส่วน (Common Anode Active-Low)
- **ซอฟต์แวร์ (ภาษา C บน RV32I):** โปรแกรมภาษา C มีหน้าที่เพียงเขียนค่าตัวเลขลงใน Memory-Mapped Register เช่น `HEX0 = count;` โดยไม่ต้องถอดรหัสบิตของ 7-segment เองในโค้ด C
- **การตรวจจับปุ่มกดในระดับซอฟต์แวร์ (Software Edge Detection):**
  - ความเร็ว Loop ของซีพียูเร็วกว่าการกดปุ่มของมนุษย์มาก
  - ในภาษา C ต้องเก็บค่าปุ่มของรอบก่อนหน้า (`KEY_prev`) เพื่อนำมาเปรียบเทียบกับรอบปัจจุบัน (`KEY_curr`) โดยนับเฉพาะจังหวะที่ปุ่มเปลี่ยนสถานะจากไม่กดเป็นกดเท่านั้น เพื่อป้องกันการนับซ้ำหลายรอบในการกดปุ่มค้าง
"""

    # Assemble complete Master Document
    header = """# คู่มือทบทวนและเฉลยข้อสอบฉบับสมบูรณ์: ครอบคลุมทั้ง LECTURE และ LAB
## วิชา Digital Circuit Design with Verilog HDL (Week 2 ถึง Week 8 + Special Labs 9 & 11)

---

### บทนำ
เอกสารฉบับนี้จัดทำขึ้นเพื่อเป็น **คู่มือการเรียนการสอนและเตรียมสอบฉบับสมบูรณ์ที่สุด (Master Comprehensive Study Guide)** โดยรวบรวมและวิเคราะห์เนื้อหาเชิงทฤษฎีจาก **สไลด์บรรยาย (Lecture)** ควบคู่ไปกับ **เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ (Lab Sheet Exercises Solution)** ตั้งแต่ **Week 2 ถึง Week 8** ไว้อย่างครบถ้วน 100% 

ทุกแบบฝึกหัดมีรายละเอียดโจทย์ การเติมคำในช่องว่าง การค้นหาและแก้ไขบั๊กในโค้ด Verilog การจับคู่ตัวดำเนินการ ตารางความจริง ตารางการทดลอง และโค้ด Verilog HDL ฉบับสมบูรณ์ พร้อมการอธิบายหลักการทำงานและระบุแหล่งที่มาอย่างเคร่งครัด

---

# 📑 สารบัญ
1. [Week 2: Quartus II Design Flow & DE0 Setup (Lec & Practice Lab 2)](#week-2)
2. [Week 3: Foundations & Verilog Language Basics (Lec & Lab 3)](#week-3)
3. [Week 4: Combinational Logic Design (Lec & Lab 4)](#week-4)
4. [Week 5: Sequential Logic Design (Lec & Lab 5)](#week-5)
5. [Week 6: Counters & Shift Registers (Lec & Lab 6)](#week-6)
6. [Week 7: Finite State Machine (FSM) Design (Lec & Lab 7)](#week-7)
7. [Week 8: Testbench Design & Functional Verification (Lec & Lab 8)](#week-8)
8. [Lab 9 (Special): การออกแบบวงจร AES-128 Encryption ด้วย Generative AI](#lab-9)
9. [Lab 11 (Special): ตัวนับขึ้น/ลงบน 7-Segment ด้วย RV32I SoC](#lab-11)
10. [ตารางสรุปภาพรวมความเชื่อมโยงตลอดหลักสูตร (Week 2 – Week 8)](#summary-table)

---
"""

    # Format sections
    # Week 2
    w2_section = f"""
<a name="week-2"></a>
# 📘 Week 2: Quartus II Design Flow & DE0 Setup

## 📚 ส่วนที่ 1: สรุปเนื้อหา LECTURE
{w2_lec}

---

## 🧪 ส่วนที่ 2: เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ LAB 2
{w2_lab}
"""

    # Week 3
    w3_section = f"""
---

<a name="week-3"></a>
# 📘 Week 3: Foundations & Verilog Language Basics

## 📚 ส่วนที่ 1: สรุปเนื้อหา LECTURE
{w3_lec}

---

## 🧪 ส่วนที่ 2: เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ LAB 3
{w3_lab}
"""

    # Week 4
    w4_section = f"""
---

<a name="week-4"></a>
# 📘 Week 4: Combinational Logic Design

## 📚 ส่วนที่ 1: สรุปเนื้อหา LECTURE
{w4_lec}

---

## 🧪 ส่วนที่ 2: เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ LAB 4
{w4_lab}
"""

    # Week 5
    w5_section = f"""
---

<a name="week-5"></a>
# 📘 Week 5: Sequential Logic Design

## 📚 ส่วนที่ 1: สรุปเนื้อหา LECTURE
{w5_lec}

---

## 🧪 ส่วนที่ 2: เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ LAB 5
{w5_lab}
"""

    # Week 6
    w6_section = f"""
---

<a name="week-6"></a>
# 📘 Week 6: Counters & Shift Registers

## 📚 ส่วนที่ 1: สรุปเนื้อหา LECTURE
{w6_lec}

---

## 🧪 ส่วนที่ 2: เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ LAB 6
{w6_lab}
"""

    # Week 7
    w7_section = f"""
---

<a name="week-7"></a>
# 📘 Week 7: Finite State Machine (FSM) Design

## 📚 ส่วนที่ 1: สรุปเนื้อหา LECTURE
{w7_lec}

---

## 🧪 ส่วนที่ 2: เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ LAB 7
{w7_lab}
"""

    # Week 8
    w8_section = f"""
---

<a name="week-8"></a>
# 📘 Week 8: Testbench Design & Functional Verification

## 📚 ส่วนที่ 1: สรุปเนื้อหา LECTURE
{w8_lec}

---

## 🧪 ส่วนที่ 2: เฉลยและอธิบายแบบฝึกหัดปฏิบัติการ LAB 8
{w8_lab}
"""

    # Summary table section
    summary_section = f"""
---

<a name="summary-table"></a>
{summary_table}
"""

    full_md = (
        header +
        w2_section +
        w3_section +
        w4_section +
        w5_section +
        w6_section +
        w7_section +
        w8_section +
        lab9_text +
        lab11_text +
        summary_section
    )

    out_path = r"D:\vhdl\Complete_Study_Guide_Lec_and_Lab.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_md)

    print(f"Master Guide generated successfully at {out_path}")
    print(f"Total file size: {len(full_md):,} characters ({len(full_md.splitlines()):,} lines)")

if __name__ == "__main__":
    assemble_master_guide()
