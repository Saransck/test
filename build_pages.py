import re
import os
import json

def generate_index_html():
    html = """<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Circuit Design with Verilog HDL | Portal Hub</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;600;700&family=Sarabun:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #0b0f19;
            --bg-card: #111827;
            --bg-card-hover: #17223b;
            --border: #1f293d;
            --border-glow: #2563eb;
            --accent-blue: #38bdf8;
            --accent-cyan: #06b6d4;
            --accent-green: #10b981;
            --accent-purple: #818cf8;
            --accent-amber: #f59e0b;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --font-display: 'Chakra Petch', sans-serif;
            --font-body: 'Sarabun', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-body);
            line-height: 1.6;
            min-height: 100vh;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 85% 75%, rgba(129, 140, 248, 0.08) 0%, transparent 40%);
            background-attachment: fixed;
            padding: 30px 20px;
        }

        .container {
            max-width: 1180px;
            margin: 0 auto;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.8));
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 40px;
            backdrop-filter: blur(12px);
            margin-bottom: 35px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue), var(--accent-purple));
        }

        .badge-chip {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(56, 189, 248, 0.12);
            color: var(--accent-blue);
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 4px 12px;
            border-radius: 999px;
            font-size: 13px;
            font-family: var(--font-mono);
            margin-bottom: 15px;
            font-weight: 600;
        }

        .hero h1 {
            font-family: var(--font-display);
            font-size: 32px;
            font-weight: 700;
            letter-spacing: -0.5px;
            margin-bottom: 12px;
            background: linear-gradient(135deg, #ffffff, #cbd5e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            color: var(--text-muted);
            font-size: 16px;
            max-width: 800px;
            margin-bottom: 25px;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .stat-item {
            background: rgba(17, 24, 39, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 16px;
            border-radius: 12px;
        }

        .stat-item .val {
            font-family: var(--font-mono);
            font-size: 24px;
            font-weight: 700;
            color: var(--accent-blue);
        }

        .stat-item .lbl {
            font-size: 13px;
            color: var(--text-muted);
            margin-top: 2px;
        }

        /* Main Hub Cards */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: rgba(56, 189, 248, 0.4);
            box-shadow: 0 12px 30px -10px rgba(56, 189, 248, 0.2);
            background: var(--bg-card-hover);
        }

        .card-icon {
            width: 52px;
            height: 52px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            margin-bottom: 20px;
        }

        .card-icon.blue { background: rgba(56, 189, 248, 0.15); color: var(--accent-blue); }
        .card-icon.purple { background: rgba(129, 140, 248, 0.15); color: var(--accent-purple); }
        .card-icon.green { background: rgba(16, 185, 129, 0.15); color: var(--accent-green); }

        .card h2 {
            font-family: var(--font-display);
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .card p {
            color: var(--text-muted);
            font-size: 14.5px;
            margin-bottom: 20px;
            flex-grow: 1;
        }

        .card-features {
            list-style: none;
            margin-bottom: 25px;
            font-size: 13.5px;
        }

        .card-features li {
            padding: 5px 0;
            color: #cbd5e1;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .card-features li::before {
            content: "✓";
            color: var(--accent-green);
            font-weight: bold;
        }

        .btn-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px 20px;
            border-radius: 10px;
            font-family: var(--font-body);
            font-size: 14px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
            cursor: pointer;
            flex: 1;
            min-width: 140px;
        }

        .btn-primary {
            background: linear-gradient(135deg, #0284c7, #2563eb);
            color: white;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
        }

        .btn-primary:hover {
            background: linear-gradient(135deg, #0369a1, #1d4ed8);
            transform: translateY(-1px);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.06);
            color: var(--text-main);
            border: 1px solid var(--border);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.12);
            border-color: rgba(255, 255, 255, 0.2);
        }

        /* Hardware Reference Section */
        .hardware-sec {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 30px;
            margin-bottom: 40px;
        }

        .sec-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 10px;
        }

        .sec-header h3 {
            font-family: var(--font-display);
            font-size: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .hw-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 16px;
        }

        .hw-item {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 16px;
        }

        .hw-item .hw-title {
            font-family: var(--font-mono);
            font-size: 14px;
            font-weight: 600;
            color: var(--accent-blue);
            margin-bottom: 6px;
        }

        .hw-item .hw-desc {
            font-size: 13.5px;
            color: var(--text-muted);
        }

        .hw-item .hw-tag {
            display: inline-block;
            font-family: var(--font-mono);
            font-size: 11px;
            padding: 2px 8px;
            border-radius: 4px;
            background: rgba(245, 158, 11, 0.15);
            color: var(--accent-amber);
            margin-top: 8px;
        }

        /* Resource Directory Section */
        .resource-sec {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 30px;
            margin-bottom: 40px;
        }

        .file-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 12px;
            margin-top: 15px;
        }

        .file-link {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 12px 16px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            color: var(--text-main);
            text-decoration: none;
            font-size: 13.5px;
            transition: all 0.2s;
        }

        .file-link:hover {
            background: rgba(56, 189, 248, 0.1);
            border-color: rgba(56, 189, 248, 0.3);
            color: var(--accent-blue);
        }

        footer {
            text-align: center;
            padding: 30px 0;
            color: var(--text-muted);
            font-size: 13px;
            border-top: 1px solid var(--border);
        }

        footer a {
            color: var(--accent-blue);
            text-decoration: none;
        }

        @media (max-width: 768px) {
            .hero { padding: 25px; }
            .hero h1 { font-size: 24px; }
            .cards-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Hero Section -->
        <section class="hero">
            <div class="badge-chip">
                <span>⚡ FPGA DE0</span>
                <span>•</span>
                <span>Altera Cyclone III EP3C16F484C6</span>
            </div>
            <h1>Digital Circuit Design with Verilog HDL</h1>
            <p>ศูนย์รวมสื่อการเรียนรู้ ระบบจำลองสอบเสมือนจริง และคู่มือสรุปเนื้อหาทบทวนฉบับสมบูรณ์ ครอบคลุมทั้ง LECTURE และ LAB ตั้งแต่ Week 2 ถึง Week 8 พร้อมการอ้างอิงแหล่งที่มา 100%</p>

            <div class="stats-grid">
                <div class="stat-item">
                    <div class="val">48</div>
                    <div class="lbl">คลังข้อสอบ 3 รูปแบบ (Choice, Code, T/F)</div>
                </div>
                <div class="stat-item">
                    <div class="val">Week 2-8</div>
                    <div class="lbl">ขอบเขตเนื้อหา Lec & Lab</div>
                </div>
                <div class="stat-item">
                    <div class="val">50 MHz</div>
                    <div class="lbl">CLOCK_50 System Base</div>
                </div>
                <div class="stat-item">
                    <div class="val">15,408</div>
                    <div class="lbl">Logic Elements (LEs)</div>
                </div>
            </div>
        </section>

        <!-- Main Cards Grid -->
        <div class="cards-grid">
            <!-- Card 1: Exam Simulator -->
            <div class="card">
                <div class="card-icon blue">🎯</div>
                <h2>ระบบจำลองทำข้อสอบ (Exam Practice Simulator)</h2>
                <p>ระบบฝึกทำโจทย์แบบโต้ตอบ มีการตรวจคำตอบพร้อมแสดงคำอธิบายเฉลยและระบุแหล่งที่มา (Lec / Lab) ทันที รองรับโจทย์ 3 รูปแบบ</p>
                <ul class="card-features">
                    <li>รูปแบบ 1: ปรนัย 4 ตัวเลือก (A, B, C, D)</li>
                    <li>รูปแบบ 2: เติมโค้ด Verilog มีตัวเลือก (A, B, C, D)</li>
                    <li>รูปแบบ 3: ถูก / ผิด (True / False)</li>
                    <li>บอกแหล่งที่มาชัดเจน (Lec / Lab / Both) พร้อมเลขหน้า/สไลด์</li>
                    <li>โหมดสุ่ม Mock Exam 20 ข้อ พร้อมสรุปคะแนน Real-time</li>
                </ul>
                <div class="btn-group">
                    <a href="exam_practice.html" class="btn btn-primary">🚀 เริ่มทำข้อสอบ</a>
                </div>
            </div>

            <!-- Card 2: Comprehensive Guide -->
            <div class="card">
                <div class="card-icon purple">📖</div>
                <h2>คู่มือทบทวนและเฉลยฉบับสมบูรณ์ (Lec & Lab Master Guide)</h2>
                <p>คู่มือรวมสรุปเนื้อหาบรรยาย (Lecture) ควบคู่กับเฉลยใบงานปฏิบัติการ (Lab Sheet) Week 2 ถึง Week 8 ไว้อย่างละเอียดครบถ้วน 100%</p>
                <ul class="card-features">
                    <li>ครอบคลุมทั้ง 2 ส่วน: ส่วนที่ 1 Lecture + ส่วนที่ 2 Lab</li>
                    <li>เนื้อหาครบทุกสัปดาห์ (Quartus, HDL, MUX, D-FF, FSM, Testbench)</li>
                    <li>สมการตรรกะ, ตารางความจริง, โค้ด Verilog สมบูรณ์</li>
                    <li>ดาวน์โหลดเอกสาร PDF (9 หน้า A4 จัดรูปเล่มพร้อมอ่าน)</li>
                </ul>
                <div class="btn-group">
                    <a href="guide.html" class="btn btn-primary">📖 เปิดอ่านออนไลน์</a>
                    <a href="Complete_Study_Guide_Lec_and_Lab.pdf" target="_blank" class="btn btn-secondary">📥 ดาวน์โหลด PDF</a>
                </div>
            </div>

            <!-- Card 3: Files & Resources Archive -->
            <div class="card">
                <div class="card-icon green">📁</div>
                <h2>คลังเอกสาร & สไลด์ (Resource Archive)</h2>
                <p>รวบรวมไฟล์ต้นฉบับ สไลด์บรรยายรายสัปดาห์ ใบงานปฏิบัติการต้นฉบับ และเฉลยแล็บฉบับเต็ม พร้อมดาวน์โหลดใช้งาน</p>
                <ul class="card-features">
                    <li>สไลด์เลกเชอร์ Week 2 ถึง Week 11 (SoC, RISC-V, Timing)</li>
                    <li>ใบงานแล็บพร้อมเฉลย (Lab 2, 3, 4, 5, 6, 7, 8 Answered)</li>
                    <li>ไฟล์คำถามข้อสอบ JSON และสคริปต์แบบจำลอง CLI Python</li>
                    <li>ดูโค้ดและดาวน์โหลดผ่าน GitHub Repo โดยตรง</li>
                </ul>
                <div class="btn-group">
                    <a href="#resources" class="btn btn-secondary">📂 ดูไฟล์ทั้งหมด</a>
                    <a href="https://github.com/Saransck/test" target="_blank" class="btn btn-secondary">🔗 GitHub Repo</a>
                </div>
            </div>
        </div>

        <!-- Hardware Specs Cheat Sheet -->
        <section class="hardware-sec">
            <div class="sec-header">
                <h3>⚙️ Altera DE0 Hardware Specification Cheat Sheet</h3>
                <span class="badge-chip" style="margin: 0;">Cyclone III EP3C16F484C6</span>
            </div>
            <div class="hw-grid">
                <div class="hw-item">
                    <div class="hw-title">Slide Switches SW[9:0]</div>
                    <div class="hw-desc">สวิตช์เลื่อนแบบสองตำแหน่ง สำหรับป้อนข้อมูลตรรกะแบบแมนนวล</div>
                    <div class="hw-tag">Active-High (ขึ้น=1, ลง=0)</div>
                </div>
                <div class="hw-item">
                    <div class="hw-title">Push Buttons KEY[2:0]</div>
                    <div class="hw-desc">ปุ่มกดสำหรับสัญญาณ Reset หรือ Trigger ต่อร่วมกับ Pull-up resistor</div>
                    <div class="hw-tag" style="background: rgba(239, 68, 68, 0.15); color: #f87171;">Active-Low (กด=0, ปล่อย=1)</div>
                </div>
                <div class="hw-item">
                    <div class="hw-title">Green LEDs LEDG[9:0]</div>
                    <div class="hw-desc">หลอดไฟแสดงสถานะเอาต์พุต เช่น บิตเคาน์เตอร์ หรือสถานะ FSM</div>
                    <div class="hw-tag">Active-High (1=ติด, 0=ดับ)</div>
                </div>
                <div class="hw-item">
                    <div class="hw-title">7-Segment HEX[3:0]</div>
                    <div class="hw-desc">จอแสดงผล 7 ส่วน 4 หลัก ขั้วแอโนดร่วม (Common Anode)</div>
                    <div class="hw-tag" style="background: rgba(239, 68, 68, 0.15); color: #f87171;">Active-Low (0=ติด, 1=ดับ)</div>
                </div>
                <div class="hw-item">
                    <div class="hw-title">Clock Oscillator</div>
                    <div class="hw-desc">สัญญาณนาฬิกาอ้างอิงความถี่ 50 MHz คาบเวลา T = 20 ns ต่อเข้าขา CLOCK_50</div>
                    <div class="hw-tag">50 MHz System Clock</div>
                </div>
                <div class="hw-item">
                    <div class="hw-title">FPGA Resources</div>
                    <div class="hw-desc">15,408 Logic Elements (LEs), 56 บล็อก M9K RAM (504K bits), 4 PLLs</div>
                    <div class="hw-tag">Speed Grade 6 / 484-FBGA</div>
                </div>
            </div>
        </section>

        <!-- Resources Section -->
        <section class="resource-sec" id="resources">
            <div class="sec-header">
                <h3>📚 คลังเอกสารแล็บ & สไลด์บรรยาย (Download Links)</h3>
            </div>
            
            <h4 style="font-size: 15px; color: var(--accent-blue); margin-bottom: 10px;">🌟 คู่มือสรุปเนื้อหาและเฉลยฉบับสมบูรณ์ (Master Guides):</h4>
            <div class="file-list" style="margin-bottom: 25px;">
                <a href="Complete_Study_Guide_Lec_and_Lab.pdf" target="_blank" class="file-link" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(56, 189, 248, 0.1);">📕 <strong>คู่มือสมบูรณ์ Lec & Lab (PDF)</strong></a>
                <a href="Complete_Study_Guide_Lec_and_Lab.md" target="_blank" class="file-link">📝 คู่มือสมบูรณ์ Lec & Lab (Markdown)</a>
                <a href="Lab_Solutions_Comprehensive_Guide.pdf" target="_blank" class="file-link">📄 เฉพาะเฉลยแล็บฉบับละเอียด (PDF)</a>
                <a href="exam_questions.json" target="_blank" class="file-link">📊 คลังข้อสอบ 48 ข้อ (JSON)</a>
            </div>

            <h4 style="font-size: 15px; color: var(--accent-green); margin-bottom: 10px;">🧪 เอกสารแล็บพร้อมเฉลย (Answered Labs):</h4>
            <div class="file-list">
                <a href="lab/Practice_Lab_Sheet_2_Answered.pdf" target="_blank" class="file-link">📄 Practice Lab 2 (Quartus Flow)</a>
                <a href="lab/lab3_Answered.pdf" target="_blank" class="file-link">📄 Lab 3 (Verilog Basics)</a>
                <a href="lab/lab4_Answered.pdf" target="_blank" class="file-link">📄 Lab 4 (Combinational ALU)</a>
                <a href="lab/lab5_Answered.pdf" target="_blank" class="file-link">📄 Lab 5 (Sequential D-FF)</a>
                <a href="lab/Lab6_Answered.pdf" target="_blank" class="file-link">📄 Lab 6 (Clock Divider & Counter)</a>
                <a href="lab/Lab7_Answered.pdf" target="_blank" class="file-link">📄 Lab 7 (FSM Combination Lock)</a>
                <a href="lab/Lab8_Answered.pdf" target="_blank" class="file-link">📄 Lab 8 (Self-Checking Testbench)</a>
            </div>

            <h4 style="font-size: 15px; color: var(--accent-purple); margin: 25px 0 10px 0;">🏛️ สไลด์ประกอบการบรรยาย (Lecture Slides):</h4>
            <div class="file-list">
                <a href="lec/Week2_software installation.pdf" target="_blank" class="file-link">📑 Week 2: Software Installation</a>
                <a href="lec/Week3_foundations and language basics.pdf" target="_blank" class="file-link">📑 Week 3: Foundations & Verilog</a>
                <a href="lec/Week4_Combinational_Design.pdf" target="_blank" class="file-link">📑 Week 4: Combinational Logic</a>
                <a href="lec/Week5_sequential_logic.pdf" target="_blank" class="file-link">📑 Week 5: Sequential Circuits</a>
                <a href="lec/Week6_Counters_ShiftRegisters.pdf" target="_blank" class="file-link">📑 Week 6: Counters & Shift Reg</a>
                <a href="lec/Week7_FSM.pdf" target="_blank" class="file-link">📑 Week 7: Finite State Machines</a>
                <a href="lec/Week8.pdf" target="_blank" class="file-link">📑 Week 8: Testbench & Verification</a>
            </div>
        </section>

        <!-- Footer -->
        <footer>
            <p>Digital Circuit Design with Verilog HDL Study Suite &bull; Altera DE0 Edition</p>
            <p style="margin-top: 6px;">Hosted on <a href="https://github.com/Saransck/test" target="_blank">GitHub Pages</a></p>
        </footer>
    </div>
</body>
</html>
"""
    with open(r"d:\vhdl\index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html created successfully.")

def generate_guide_html():
    with open(r"d:\vhdl\Complete_Study_Guide_Lec_and_Lab.md", "r", encoding="utf-8") as f:
        md_content = f.read()

    md_json = json.dumps(md_content, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>คู่มือทบทวนและเฉลยข้อสอบฉบับสมบูรณ์ (Lecture & Lab Guide)</title>
    <!-- Marked for Markdown parsing -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <!-- Highlight.js for Verilog and code styling -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/verilog.min.js"></script>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Sarabun:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #f8fafc;
            --bg-surface: #ffffff;
            --border: #e2e8f0;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --primary: #0284c7;
            --primary-dark: #0369a1;
            --font-display: 'Chakra Petch', sans-serif;
            --font-body: 'Sarabun', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-body);
            line-height: 1.7;
        }}

        /* Top Navbar */
        .topbar {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border);
            padding: 12px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .brand {{
            font-family: var(--font-display);
            font-weight: 700;
            font-size: 17px;
            color: var(--text-main);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .top-links {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .nav-btn {{
            text-decoration: none;
            font-size: 13.5px;
            font-weight: 600;
            padding: 8px 14px;
            border-radius: 8px;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}

        .nav-btn-outline {{
            background: #f1f5f9;
            color: #334155;
            border: 1px solid var(--border);
        }}

        .nav-btn-outline:hover {{
            background: #e2e8f0;
            color: #0f172a;
        }}

        .nav-btn-primary {{
            background: var(--primary);
            color: white;
        }}

        .nav-btn-primary:hover {{
            background: var(--primary-dark);
        }}

        /* Layout Container */
        .layout {{
            max-width: 1280px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 30px;
            padding: 30px 24px;
        }}

        /* Sidebar TOC */
        .sidebar {{
            position: sticky;
            top: 80px;
            height: calc(100vh - 100px);
            overflow-y: auto;
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 20px;
        }}

        .sidebar h4 {{
            font-family: var(--font-display);
            font-size: 15px;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        }}

        .toc-list {{
            list-style: none;
        }}

        .toc-item {{
            margin-bottom: 6px;
        }}

        .toc-link {{
            display: block;
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 13.5px;
            color: #475569;
            text-decoration: none;
            transition: all 0.15s;
        }}

        .toc-link:hover {{
            background: #f0f9ff;
            color: var(--primary);
            font-weight: 600;
        }}

        /* Content Area */
        .content-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 45px 50px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            min-width: 0;
        }}

        /* Markdown Styles */
        .markdown-body h1 {{
            font-family: var(--font-display);
            font-size: 26px;
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 12px;
            margin-top: 35px;
            margin-bottom: 20px;
        }}

        .markdown-body h1:first-child {{
            margin-top: 0;
        }}

        .markdown-body h2 {{
            font-family: var(--font-display);
            font-size: 21px;
            color: #1e293b;
            margin-top: 28px;
            margin-bottom: 14px;
        }}

        .markdown-body h3 {{
            font-family: var(--font-display);
            font-size: 18px;
            color: #334155;
            margin-top: 22px;
            margin-bottom: 10px;
        }}

        .markdown-body h4 {{
            font-size: 16px;
            color: #475569;
            margin-top: 18px;
            margin-bottom: 8px;
        }}

        .markdown-body p {{
            margin-bottom: 16px;
            font-size: 15px;
            color: #334155;
        }}

        .markdown-body ul, .markdown-body ol {{
            margin-bottom: 16px;
            padding-left: 24px;
        }}

        .markdown-body li {{
            margin-bottom: 6px;
            font-size: 15px;
            color: #334155;
        }}

        .markdown-body hr {{
            border: 0;
            height: 1px;
            background: #e2e8f0;
            margin: 30px 0;
        }}

        .markdown-body code {{
            font-family: var(--font-mono);
            font-size: 13.5px;
            background: #f1f5f9;
            color: #0369a1;
            padding: 2px 6px;
            border-radius: 4px;
        }}

        .markdown-body pre {{
            background: #282c34 !important;
            border-radius: 10px;
            padding: 16px;
            overflow-x: auto;
            margin: 18px 0;
        }}

        .markdown-body pre code {{
            background: transparent !important;
            color: #abb2bf !important;
            padding: 0;
            font-size: 13px;
            line-height: 1.5;
        }}

        .markdown-body table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 14px;
        }}

        .markdown-body th, .markdown-body td {{
            border: 1px solid #cbd5e1;
            padding: 10px 14px;
            text-align: left;
        }}

        .markdown-body th {{
            background: #f1f5f9;
            font-weight: 600;
            color: #1e293b;
        }}

        .markdown-body tr:nth-child(even) {{
            background: #f8fafc;
        }}

        .markdown-body blockquote {{
            border-left: 4px solid var(--primary);
            padding: 10px 18px;
            background: #f0f9ff;
            color: #0369a1;
            border-radius: 0 8px 8px 0;
            margin: 18px 0;
        }}

        .markdown-body a {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
        }}

        .markdown-body a:hover {{
            text-decoration: underline;
        }}

        @media (max-width: 900px) {{
            .layout {{
                grid-template-columns: 1fr;
            }}
            .sidebar {{
                display: none;
            }}
            .content-card {{
                padding: 25px 20px;
            }}
        }}
    </style>
</head>
<body>
    <header class="topbar">
        <a href="index.html" class="brand">
            <span>⚡</span>
            <span>Digital Circuit Design Study Guide (Lec & Lab)</span>
        </a>
        <div class="top-links">
            <a href="index.html" class="nav-btn nav-btn-outline">🏠 หน้าหลัก</a>
            <a href="exam_practice.html" class="nav-btn nav-btn-outline">🎯 ระบบสอบ (48 ข้อ)</a>
            <a href="Complete_Study_Guide_Lec_and_Lab.pdf" target="_blank" class="nav-btn nav-btn-primary">📕 โหลด PDF สมบูรณ์</a>
            <a href="Lab_Solutions_Comprehensive_Guide.pdf" target="_blank" class="nav-btn nav-btn-outline">📄 เฉลยแล็บละเอียด (PDF)</a>
        </div>
    </header>

    <div class="layout">
        <!-- Sidebar Navigation -->
        <aside class="sidebar">
            <h4>📑 สารบัญเนื้อหา</h4>
            <ul class="toc-list">
                <li class="toc-item"><a href="#week-2" class="toc-link">Week 2: Quartus Flow (Lec & Lab)</a></li>
                <li class="toc-item"><a href="#week-3" class="toc-link">Week 3: Verilog Basics (Lec & Lab)</a></li>
                <li class="toc-item"><a href="#week-4" class="toc-link">Week 4: Combinational (Lec & Lab)</a></li>
                <li class="toc-item"><a href="#week-5" class="toc-link">Week 5: Sequential (Lec & Lab)</a></li>
                <li class="toc-item"><a href="#week-6" class="toc-link">Week 6: Counters & Regs (Lec & Lab)</a></li>
                <li class="toc-item"><a href="#week-7" class="toc-link">Week 7: FSM Design (Lec & Lab)</a></li>
                <li class="toc-item"><a href="#week-8" class="toc-link">Week 8: Testbench (Lec & Lab)</a></li>
                <li class="toc-item"><a href="#summary-table" class="toc-link">📊 ตารางสรุปภาพรวม</a></li>
            </ul>
        </aside>

        <!-- Main Content -->
        <main class="content-card">
            <div id="content" class="markdown-body">กำลังโหลดคู่มือ...</div>
        </main>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", () => {{
            hljs.highlightAll();
        }});
    </script>
</body>
</html>
"""
    with open(r"d:\vhdl\complete_guide_body.html", "r", encoding="utf-8") as bf:
        rendered_body = bf.read()

    html = html.replace('<div id="content" class="markdown-body">กำลังโหลดคู่มือ...</div>', '<div id="content" class="markdown-body">\n' + rendered_body + '\n</div>')

    with open(r"d:\vhdl\guide.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("guide.html created successfully with pre-rendered Complete_Study_Guide_Lec_and_Lab HTML.")

def update_exam_practice_html():
    with open(r"d:\vhdl\exam_practice.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Update PDF download link in exam_practice.html navbar if present
    content = content.replace("Lab_Solutions_Comprehensive_Guide.pdf", "Complete_Study_Guide_Lec_and_Lab.pdf")
    content = content.replace("คู่มือเฉลยแล็บ (Lab Guide)", "คู่มือทบทวน Lec & Lab (Guide)")

    with open(r"d:\vhdl\exam_practice.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("exam_practice.html updated navbar links.")

def create_nojekyll():
    with open(r"d:\vhdl\.nojekyll", "w", encoding="utf-8") as f:
        f.write("")
    print(".nojekyll created.")

if __name__ == "__main__":
    generate_index_html()
    generate_guide_html()
    update_exam_practice_html()
    create_nojekyll()
