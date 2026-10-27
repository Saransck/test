# ⚡ Digital Circuit Design with Verilog HDL (FPGA Altera DE0)

[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0284c7?style=for-the-badge&logo=github)](https://saransck.github.io/test/)
[![Verilog HDL](https://img.shields.io/badge/Language-Verilog%20HDL-blue?style=for-the-badge)](https://en.wikipedia.org/wiki/Verilog)
[![FPGA Device](https://img.shields.io/badge/FPGA-Altera%20Cyclone%20III-orange?style=for-the-badge)](https://www.intel.com/content/www/us/en/products/details/fpga/cyclone/iii.html)
[![Questions](https://img.shields.io/badge/Questions-48%2B%20Interactive-success?style=for-the-badge)](https://saransck.github.io/test/exam_practice.html)

ศูนย์รวมสื่อการเรียนรู้ ระบบจำลองสอบเสมือนจริง และคู่มือเฉลยข้อสอบปฏิบัติการอย่างละเอียด สำหรับวิชา **Digital Circuit Design with Verilog HDL** มุ่งเน้นการออกแบบและทดสอบวงจรดิจิทัลบนบอร์ด **Altera DE0 (Cyclone III `EP3C16F484C6`)** ครอบคลุมเนื้อหาตั้งแต่ **Week 2 ถึง Week 8** อ้างอิงสไลด์บรรยาย (Lecture) และใบงานปฏิบัติการ (Lab) ถูกต้อง 100%

---

## 🌐 เข้าใช้งานระบบออนไลน์ (GitHub Pages)

| เมนู | ลิงก์เข้าใช้งาน | รายละเอียด |
| :--- | :--- | :--- |
| 🏠 **Portal Hub (หน้าหลัก)** | [saransck.github.io/test/](https://saransck.github.io/test/) | แดชบอร์ดหลัก รวมทางเข้าสู่ทุกระบบและตารางสเปกฮาร์ดแวร์ |
| 🎯 **Exam Practice Simulator** | [เข้าทำแบบทดสอบ](https://saransck.github.io/test/exam_practice.html) | ระบบจำลองสอบ Interactive 48 ข้อ 3 รูปแบบ (Choice, Code, T/F) พร้อมโหมด Mock Exam |
| 📖 **Master Study Guide (Web)** | [อ่านคู่มือออนไลน์](https://saransck.github.io/test/guide.html) | คู่มือสรุปเนื้อหาทบทวนและเฉลยฉบับสมบูรณ์ (ครอบคลุมทั้ง Lecture และ Lab Week 2–8) |
| 📕 **Master Study Guide (PDF)** | [ดาวน์โหลดไฟล์ PDF](Complete_Study_Guide_Lec_and_Lab.pdf) | เอกสารคู่มือทบทวนและเฉลยฉบับสมบูรณ์ทั้ง Lec & Lab (ขนาดพิมพ์ A4 9 หน้า) |

---

## 📚 โครงสร้างเนื้อหารายสัปดาห์ (Week 2 - 8)

| สัปดาห์ | หัวข้อ Lecture | หัวข้อ Lab | แนวคิดและเนื้อหาสำคัญ |
| :---: | :--- | :--- | :--- |
| **Week 2** | **Quartus II & FPGA Flow** | **Practice Lab Sheet 2:** Project Setup | FPGA Design Flow, การเลือกชิป `EP3C16F484C6`, Pin Planner, การโปรแกรม `.sof` / `.pof` |
| **Week 3** | **Foundations & Basics** | **Lab 3:** Basic Gates & Modules | โครงสร้างโมดูล, Named vs Positional mapping, Data types (`wire` vs `reg`), 3-Input Majority |
| **Week 4** | **Combinational Logic** | **Lab 4:** Multiplexer & ALU | วงจร Combinational, `always @(*)`, การป้องกัน **Inferred Latch**, 7-Segment Active-Low |
| **Week 5** | **Sequential Logic** | **Lab 5:** Latches & Flip-Flops | Async vs Sync Reset, กฎเหล็ก **Non-blocking Assignment (`<=`)**, Race Condition |
| **Week 6** | **Counters & Shift Reg** | **Lab 6:** Divider & Running LED | วงจรหารความถี่ (50 MHz $\rightarrow$ 1 Hz นับ 26 บิต), Up/Down Counter, Shift Register |
| **Week 7** | **Finite State Machine** | **Lab 7:** Combination Lock | สถาปัตยกรรม **Moore 3-Always-Block**, State Encoding, Falling-Edge Detector |
| **Week 8** | **Testbench & Verification** | **Lab 8:** Self-Checking Testbench | การเขียน Testbench 4 ส่วน, การหน่วงเวลา `#1;` ป้องกัน Race condition, Case Equality (`===`) |

---

## ⚙️ สเปกฮาร์ดแวร์บอร์ด Altera DE0 (`EP3C16F484C6`)

```
+--------------------------------------------------------------------------------+
|                             Altera DE0 Board Cheat Sheet                       |
+---------------------+-------------------+--------------------------------------+
| Peripheral          | Pin / Signal      | Logic Characteristic                 |
+---------------------+-------------------+--------------------------------------+
| Slide Switches      | SW[9:0]           | Active-High (เลื่อนขึ้น = 1, ลง = 0)  |
| Push Buttons        | KEY[2:0]          | Active-Low  (กด = 0, ปล่อย = 1)      |
| Green LEDs          | LEDG[9:0]         | Active-High (1 = ไฟติด, 0 = ไฟดับ)   |
| 7-Segment Display   | HEX0 - HEX3       | Common Anode (Active-Low: 0=ติด)     |
| System Clock        | CLOCK_50 (50 MHz) | T = 20 ns ต่อเข้า Global Clock Net   |
| Logic Elements      | 15,408 LEs        | 56 M9K RAM blocks (504K bits)        |
+---------------------+-------------------+--------------------------------------+
```

---

## 📁 โครงสร้างไดเรกทอรีในคลังข้อมูล

```text
├── index.html                           # Landing Page & Portal Hub สำหรับ GitHub Pages
├── guide.html                           # เว็บสำหรับอ่านคู่มือเฉลยแล็บออนไลน์
├── Complete_Study_Guide_Lec_and_Lab.md # คู่มือสรุปเนื้อหาทบทวนและเฉลยฉบับสมบูรณ์ (ครอบคลุมทั้ง Lecture & Lab)
├── Complete_Study_Guide_Lec_and_Lab.pdf# ไฟล์ PDF คู่มือทบทวนสมบูรณ์ทั้ง Lec & Lab (9 หน้า A4)
├── exam_practice.html                  # ระบบจำลองสอบ Interactive Exam Simulator (48 ข้อ 3 รูปแบบ)
├── exam_practice.py                    # โปรแกรมทำข้อสอบผ่าน Terminal / Command Line (Python CLI)
├── exam_questions.json                 # คลังข้อมูลโจทย์และเฉลยข้อสอบทั้งหมดพร้อมแท็ก Lec/Lab (JSON)
├── Lab_Solutions_Comprehensive_Guide.md# เอกสารเฉลยและสรุปเนื้อหาเฉพาะแล็บ (Markdown)
├── Lab_Solutions_Comprehensive_Guide.pdf# ไฟล์ PDF คู่มือเฉลยเฉพาะแล็บ
├── .nojekyll                           # ปิด Jekyll บน GitHub Pages เพื่อให้โหลดไฟล์ static ตรงๆ
├── lab/                                 # โฟลเดอร์ใบงานแล็บและไฟล์เฉลยต้นฉบับ (PDF)
│   ├── Practice_Lab_Sheet_2_Answered.pdf
│   ├── lab3_Answered.pdf ... lab8_Answered.pdf
│   └── lab9, Lab11 ...
└── lec/                                 # โฟลเดอร์สไลด์ประกอบการบรรยาย (Week 2 ถึง Week 11)
    ├── Week2_software installation.pdf ... Week8.pdf
    └── Timing_Analysis, Chapter10, Week11 ...
```

---

## 💻 การทดสอบและรันบนเครื่อง Local

สามารถเปิดไฟล์ `.html` ผ่านเว็บบราวเซอร์ได้ทันทีโดยไม่ต้องติดตั้ง Server พิเศษ:
- ดับเบิลคลิกเปิด `index.html` เพื่อเข้าสู่ Portal Hub
- หรือใช้คำสั่ง Python Local Server:
```bash
python -m http.server 8000
```
จากนั้นเปิดบราวเซอร์ไปที่ `http://localhost:8000`
