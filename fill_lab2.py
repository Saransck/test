import fitz

doc = fitz.open('D:/vhdl/lab/Practice Lab Sheet 2.pdf')
font_tahoma = 'C:/Windows/Fonts/tahoma.ttf'
font_arial = 'C:/Windows/Fonts/arial.ttf'

BLUE = (0.0, 0.22, 0.8)        # Clean sharp royal blue
DARK_BLUE = (0.0, 0.12, 0.55)

# --- PAGE 1: Header student info and score ---
p1 = doc[0]
p1.insert_font(fontname='tahoma', fontfile=font_tahoma)
p1.insert_text(fitz.Point(120, 160), "เฉลยแบบฝึกหัดปฏิบัติการ (Answer Key)", fontname='tahoma', fontsize=11, color=DARK_BLUE)
p1.insert_text(fitz.Point(340, 260), "10 / 10", fontname='tahoma', fontsize=11, color=BLUE)

# --- PAGE 2: Table answers & Question 2 ---
p2 = doc[1]
p2.insert_font(fontname='tahoma', fontfile=font_tahoma)
p2.insert_font(fontname='arial', fontfile=font_arial)

# Table 1: 0 (กด KEY[0])
p2.insert_text(fitz.Point(235, 312), "7'b1000000", fontname='arial', fontsize=10.5, color=BLUE)
p2.insert_text(fitz.Point(440, 312), "7'h40", fontname='arial', fontsize=10.5, color=BLUE)

# Table 1: 1 (กด KEY[1])
p2.insert_text(fitz.Point(235, 335), "7'b1111001", fontname='arial', fontsize=10.5, color=BLUE)
p2.insert_text(fitz.Point(440, 335), "7'h79", fontname='arial', fontsize=10.5, color=BLUE)

# Table 1: 2 (กด KEY[2])
p2.insert_text(fitz.Point(235, 358), "7'b0100100", fontname='arial', fontsize=10.5, color=BLUE)
p2.insert_text(fitz.Point(440, 358), "7'h24", fontname='arial', fontsize=10.5, color=BLUE)

# Table 1: 3 (กด KEY[3])
p2.insert_text(fitz.Point(235, 381), "7'b0110000", fontname='arial', fontsize=10.5, color=BLUE)
p2.insert_text(fitz.Point(440, 381), "7'h30", fontname='arial', fontsize=10.5, color=BLUE)

# Table 1: ดับ (ไม่กดปุ่ม)
p2.insert_text(fitz.Point(235, 404), "7'b1111111", fontname='arial', fontsize=10.5, color=BLUE)
p2.insert_text(fitz.Point(440, 404), "7'h7F", fontname='arial', fontsize=10.5, color=BLUE)

# Question 2 Explanation:
ans_q2_lines = [
    "1. สวิตช์ KEY บนบอร์ด DE0 เป็นวงจร Active-Low (มี Pull-up): เมื่อไม่กดจะมีค่าเป็น 1 (1'b1)",
    "   และเมื่อถูกกด หน้าสัมผัสจะต่อลงกราวด์ (GND) ทำให้สัญญาณตกลงเป็นลอจิก 0 (1'b0)",
    "2. เหตุผลที่ต้องใส่โอเปอเรเตอร์ Bitwise NOT (~) หน้าตัวแปร KEY (เขียนเป็น ~KEY):",
    "   - เพื่อกลับระดับสัญญาณ (Invert) ให้กลายเป็น Active-High ในระบบตรรกะภายในโมดูล",
    "   - ทำให้เมื่อปุ่มถูกกด (รับค่า 0 เข้ามา) จะถูกกลับค่าเป็น 1 ช่วยให้เขียนเงื่อนไข case เข้าใจง่าย",
    "   - เช่น 4'b0001 คือกด KEY[0], 4'b0010 คือกด KEY[1], 4'b0100 คือกด KEY[2], 4'b1000 คือกด KEY[3]"
]

y_q2 = 478
for line in ans_q2_lines:
    p2.insert_text(fitz.Point(95, y_q2), line, fontname='tahoma', fontsize=9.2, color=BLUE)
    y_q2 += 22

# --- PAGE 3: Question 3 - Draw RTL Schematic ---
p3 = doc[2]
p3.insert_font(fontname='tahoma', fontfile=font_tahoma)
p3.insert_font(fontname='arial', fontfile=font_arial)

shape = p3.new_shape()

# Title
p3.insert_text(fitz.Point(85, 95), "[RTL Schematic Diagram: KEY[3:0] to HEX0[6:0] Active-Low Decoder]", fontname='arial', fontsize=11, color=DARK_BLUE)

# Draw Input Port Box KEY[3:0]
shape.draw_rect(fitz.Rect(65, 140, 145, 290))
# Inverter / Bitwise NOT block
shape.draw_rect(fitz.Rect(185, 160, 245, 270))
# Decoder / Priority Case Mux Block
shape.draw_rect(fitz.Rect(285, 130, 425, 300))
# Output Port Box HEX0[6:0]
shape.draw_rect(fitz.Rect(465, 140, 545, 290))

# Bus lines
shape.draw_line(fitz.Point(145, 215), fitz.Point(185, 215)) # KEY -> Inverter
shape.draw_line(fitz.Point(245, 215), fitz.Point(285, 215)) # ~KEY -> Decoder
shape.draw_line(fitz.Point(425, 215), fitz.Point(465, 215)) # Decoder -> HEX0

shape.finish(color=BLUE, fill=(0.94, 0.97, 1.0), width=1.5)
shape.commit()

# Labels on Page 3
p3.insert_text(fitz.Point(75, 205), "INPUT", fontname='arial', fontsize=9, color=DARK_BLUE)
p3.insert_text(fitz.Point(70, 220), "KEY[3:0]", fontname='arial', fontsize=10, color=DARK_BLUE)
p3.insert_text(fitz.Point(70, 235), "(Active-Low)", fontname='arial', fontsize=7.5, color=BLUE)

p3.insert_text(fitz.Point(192, 210), "NOT / INV", fontname='arial', fontsize=8.5, color=DARK_BLUE)
p3.insert_text(fitz.Point(198, 225), "(~KEY)", fontname='arial', fontsize=9, color=DARK_BLUE)

p3.insert_text(fitz.Point(308, 160), "7-SEG DECODER", fontname='arial', fontsize=10.5, color=DARK_BLUE)
p3.insert_text(fitz.Point(305, 180), "case (~KEY)", fontname='arial', fontsize=9, color=BLUE)
p3.insert_text(fitz.Point(295, 202), "4'b0001 -> 7'b1000000 ('0')", fontname='arial', fontsize=8, color=BLUE)
p3.insert_text(fitz.Point(295, 218), "4'b0010 -> 7'b1111001 ('1')", fontname='arial', fontsize=8, color=BLUE)
p3.insert_text(fitz.Point(295, 234), "4'b0100 -> 7'b0100100 ('2')", fontname='arial', fontsize=8, color=BLUE)
p3.insert_text(fitz.Point(295, 250), "4'b1000 -> 7'b0110000 ('3')", fontname='arial', fontsize=8, color=BLUE)
p3.insert_text(fitz.Point(295, 266), "default -> 7'b1111111 (OFF)", fontname='arial', fontsize=8, color=BLUE)

p3.insert_text(fitz.Point(475, 205), "OUTPUT", fontname='arial', fontsize=9, color=DARK_BLUE)
p3.insert_text(fitz.Point(470, 220), "HEX0[6:0]", fontname='arial', fontsize=10, color=DARK_BLUE)
p3.insert_text(fitz.Point(468, 235), "(Active-Low)", fontname='arial', fontsize=7.5, color=BLUE)

# Description text below RTL
rtl_notes = [
    "คำอธิบายโครงสร้างวงจร RTL:",
    "1. Input Buffer: รับสัญญาณปุ่มกด 4 บิต KEY[3:0] ผ่านเกต NOT จำนวน 4 ตัว เพื่อกลับลอจิกเป็น Active-High",
    "2. Combinational Decoder Logic: สังเคราะห์ลงใน 4-Input LUT (Normal Mode) ของ Logic Element (LE)",
    "3. Output Buffer: ขับสัญญาณขนาด 7 บิต ออกทางพอร์ต HEX0[6:0] ไปยังหลอด 7-Segment Display ชนิด Common Anode"
]
y_rtl = 330
for note in rtl_notes:
    p3.insert_text(fitz.Point(70, y_rtl), note, fontname='tahoma', fontsize=9.2, color=BLUE)
    y_rtl += 20

# --- PAGE 4: Part 2 - Counter Prompt & Implementation ---
p4 = doc[3]
p4.insert_font(fontname='tahoma', fontfile=font_tahoma)

p4_prompt_lines = [
    "\"ฉันใช้บอร์ด Altera DE0 กับ Quartus II 13.0sp1 โดยมี Clock 50 MHz (CLOCK_50)",
    "ขอ Verilog module วงจรนับเลข 0-9 แสดงผลบน HEX0 (7-segment active-low) ดังนี้:",
    "1. Input: CLOCK_50 (50 MHz), KEY[0] (Active-Low push button: กด=0, ปล่อย=1)",
    "2. Output: HEX0[6:0] (7-segment active-low: gfedcba)",
    "3. พฤติกรรม: ออกแบบ Clock Divider 50MHz ให้เกิดพัลส์ 1 วินาที (1 Hz),",
    "   กด KEY[0] ค้างไว้: ให้นับขึ้นทีละ 1 ทุก 1 วินาที (0->9) เมื่อถึง 9 ให้ค้างที่ 9 ไม่นับเพิ่ม,",
    "   ปล่อย KEY[0]: ให้นับถอยหลังทีละ 1 ทุก 1 วินาที (9->0) เมื่อถึง 0 ให้ค้างที่ 0 ไม่นับลด,",
    "   มีโมดูลถอดรหัส HEX0 แปลงค่าตัวเลข 0-9 เป็นรหัส active-low 7-segment (Common Anode)\""
]

y_p4 = 268
for pl in p4_prompt_lines:
    p4.insert_text(fitz.Point(75, y_p4), pl, fontname='tahoma', fontsize=8.2, color=BLUE)
    y_p4 += 18.2

# Add Verilog summary snippet
p4.insert_text(fitz.Point(75, 432), "สรุปโค้ด Verilog และโครงสร้างฮาร์ดแวร์ที่สังเคราะห์ได้:", fontname='tahoma', fontsize=9.2, color=DARK_BLUE)
code_summary = [
    "// 1. Clock Divider 50MHz -> 1Hz: reg [25:0] clk_div = 0; reg tick_1s = 0;",
    "always @(posedge CLOCK_50) begin",
    "    if (clk_div == 26'd49_999_999) begin clk_div <= 0; tick_1s <= 1'b1; end",
    "    else begin clk_div <= clk_div + 1'b1; tick_1s <= 1'b0; end",
    "end",
    "// 2. Up/Down Saturating Counter (0 to 9)",
    "always @(posedge CLOCK_50) begin",
    "    if (tick_1s) begin",
    "        if (~KEY[0]) begin if (count < 4'd9) count <= count + 1'b1; end // กด KEY[0] -> นับขึ้น",
    "        else         begin if (count > 4'd0) count <= count - 1'b1; end // ปล่อย KEY[0] -> นับลง",
    "    end",
    "end",
    "// 3. HEX0 7-Seg Decoder: 0->7'h40, 1->7'h79, 2->7'h24, 3->7'h30, 4->7'h19, ..., 9->7'h10"
]
y_code = 450
for cl in code_summary:
    p4.insert_text(fitz.Point(75, y_code), cl, fontname='tahoma', fontsize=8.0, color=BLUE)
    y_code += 18.2

output_path = 'D:/vhdl/lab/Practice_Lab_Sheet_2_Answered.pdf'
doc.save(output_path)
print('Successfully saved answered PDF to:', output_path)
