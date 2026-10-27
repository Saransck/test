import fitz

doc = fitz.open('D:/vhdl/lab/lab 4.pdf')
font_tahoma = 'C:/Windows/Fonts/tahoma.ttf'
font_arial = 'C:/Windows/Fonts/arial.ttf'

BLUE = (0.0, 0.22, 0.82)       # Clean royal blue
DARK_BLUE = (0.0, 0.12, 0.55)

# =============================================================================
# PAGE 1: Sign-off
# =============================================================================
p1 = doc[0]
p1.insert_font(fontname='tahoma', fontfile=font_tahoma)
p1.insert_font(fontname='arial', fontfile=font_arial)

p1.insert_text(fitz.Point(125, 156), "Asst. Dr. Tamnuwat", fontname='arial', fontsize=9.5, color=DARK_BLUE)
p1.insert_text(fitz.Point(235, 156), "2026-10-27", fontname='arial', fontsize=9.5, color=DARK_BLUE)
p1.insert_text(fitz.Point(345, 156), "69", fontname='arial', fontsize=10, color=BLUE)

# =============================================================================
# PAGE 2: Exercise 1 (4-to-1 MUX Blanks)
# =============================================================================
p2 = doc[1]
p2.insert_font(fontname='tahoma', fontfile=font_tahoma)
p2.insert_font(fontname='arial', fontfile=font_arial)

p2.insert_text(fitz.Point(125, 93), "sel", fontname='arial', fontsize=9, color=BLUE)
p2.insert_text(fitz.Point(92, 103), "reg", fontname='arial', fontsize=9, color=BLUE)
p2.insert_text(fitz.Point(98, 131), "sel", fontname='arial', fontsize=9, color=BLUE)
p2.insert_text(fitz.Point(115, 161), "y = in2", fontname='arial', fontsize=9, color=BLUE)
p2.insert_text(fitz.Point(145, 180), "1'b0", fontname='arial', fontsize=9, color=BLUE)

# =============================================================================
# PAGE 3: Exercise 2 (5 Bugs Table) & Exercise 3 (Match)
# =============================================================================
p3 = doc[2]
p3.insert_font(fontname='tahoma', fontfile=font_tahoma)
p3.insert_font(fontname='arial', fontfile=font_arial)

# Exercise 2 Bug Log:
bug_rows = [
    (240, "Line 3: output [3:0] out", "Missing 'reg' type for always-driven output", "output reg [3:0] out"),
    (260, "Line 5: always @(sel[0])", "Incomplete sensitivity list (missing sel[1])", "always @(*)"),
    (280, "Line 8: 2'd0: out = 4'b0010;", "Duplicate case label (2'd0 appears twice)", "2'd1: out = 4'b0010;"),
    (300, "Line 9: 2'd2: out = 4'b0010;", "Wrong one-hot constant for sel=2 (bit 1 set)", "2'd2: out = 4'b0100;"),
    (320, "Lines 9-10: case end", "Missing 2'd3 branch & default (inferred latch)", "2'd3: out=4'b1000; default: out=4'b0000;")
]

for y_pos, loc, wrong, corr in bug_rows:
    p3.insert_text(fitz.Point(62, y_pos), loc, fontname='arial', fontsize=7.2, color=BLUE)
    p3.insert_text(fitz.Point(195, y_pos), wrong, fontname='arial', fontsize=7.2, color=BLUE)
    fs_c = 6.6 if "default" in corr else 7.2
    p3.insert_text(fitz.Point(365, y_pos), corr, fontname='arial', fontsize=fs_c, color=BLUE)

# Exercise 3: Match Table
p3.insert_text(fitz.Point(170, 448), "E", fontname='arial', fontsize=10.5, color=BLUE)
p3.insert_text(fitz.Point(170, 466), "D", fontname='arial', fontsize=10.5, color=BLUE)
p3.insert_text(fitz.Point(170, 485), "B", fontname='arial', fontsize=10.5, color=BLUE)
p3.insert_text(fitz.Point(170, 503), "C", fontname='arial', fontsize=10.5, color=BLUE)
p3.insert_text(fitz.Point(170, 522), "A", fontname='arial', fontsize=10.5, color=BLUE)

# =============================================================================
# PAGE 4: Exercise 4 (Predict) & Exercise 5 (Short Answer)
# =============================================================================
p4 = doc[3]
p4.insert_font(fontname='tahoma', fontfile=font_tahoma)
p4.insert_font(fontname='arial', fontfile=font_arial)

# Exercise 4: Predict table
pred_rows = [
    (248, "4'b1001", "9"),
    (267, "4'b0011", "3"),
    (285, "4'b0010", "2"),
    (304, "4'b0111", "7"),
    (322, "4'b0000", "0")
]

for y_pos, b_val, d_val in pred_rows:
    p4.insert_text(fitz.Point(270, y_pos), b_val, fontname='arial', fontsize=9, color=BLUE)
    p4.insert_text(fitz.Point(405, y_pos), d_val, fontname='arial', fontsize=9, color=BLUE)

# Exercise 5: Short Answer (Why ALU is a big MUX)
p4.insert_text(fitz.Point(55, 470), "แต่ละบล็อกฟังก์ชัน (Adder, Subtractor, Logic) คำนวณอินพุต A และ B ขนานพร้อมกันตลอดเวลา", fontname='tahoma', fontsize=8, color=BLUE)
p4.insert_text(fitz.Point(55, 496), "สัญญาณ Opcode ทำหน้าที่เป็น Select line เลือกผลลัพธ์ของฟังก์ชันที่ต้องการเพียงค่าเดียวส่งออก", fontname='tahoma', fontsize=8, color=BLUE)
p4.insert_text(fitz.Point(55, 522), "โครงสร้างนี้ตรงกับฮาร์ดแวร์ Multiplexer ขนานกันจริงที่เชื่อมวงจรคำนวณเข้ากับพอร์ตเอาต์พุต", fontname='tahoma', fontsize=8, color=BLUE)

# =============================================================================
# PAGE 5: Exercise 6 (Priority Encoder Code)
# =============================================================================
p5 = doc[4]
p5.insert_font(fontname='tahoma', fontfile=font_tahoma)
p5.insert_font(fontname='arial', fontfile=font_arial)

pe_code = [
    "module priority_encoder (",
    "    input  wire [3:0] in,    // 4 request lines (in[3] highest)",
    "    output reg        val,   // 1 if any input asserted",
    "    output reg  [1:0] code   // Binary index of highest priority",
    ");",
    "",
    "    always @(*) begin",
    "        if (in[3]) begin",
    "            val  = 1'b1;  code = 2'b11; // in[3] active -> 3",
    "        end else if (in[2]) begin",
    "            val  = 1'b1;  code = 2'b10; // in[2] active -> 2",
    "        end else if (in[1]) begin",
    "            val  = 1'b1;  code = 2'b01; // in[1] active -> 1",
    "        end else if (in[0]) begin",
    "            val  = 1'b1;  code = 2'b00; // in[0] active -> 0",
    "        end else begin",
    "            val  = 1'b0;  code = 2'b00; // no request",
    "        end",
    "    end",
    "",
    "endmodule"
]
y_pe = 345
for line in pe_code:
    p5.insert_text(fitz.Point(60, y_pe), line, fontname='arial', fontsize=9, color=BLUE)
    y_pe += 15

# =============================================================================
# PAGE 8: Exercise 7A (ALU Code), 7B (BCD Correction) & 8 (Verification)
# =============================================================================
p8 = doc[7]
p8.insert_font(fontname='tahoma', fontfile=font_tahoma)
p8.insert_font(fontname='arial', fontfile=font_arial)

alu_code = [
    "module alu (",
    "    input  wire [4:0] a, b,    // 5-bit Operands",
    "    input  wire [2:0] op,      // 3-bit Operation select",
    "    output reg  [5:0] result   // 6-bit result",
    ");",
    "    always @(*) begin",
    "        case (op)",
    "            3'b000: result = {1'b0, a} + {1'b0, b}; // ADD",
    "            3'b001: result = {1'b0, a} - {1'b0, b}; // SUB",
    "            3'b010: result = {1'b0, a & b};         // AND",
    "            3'b011: result = {1'b0, a | b};         // OR",
    "            3'b100: result = {1'b0, a ^ b};         // XOR",
    "            3'b101: result = {1'b0, ~a};            // NOT A",
    "            3'b110: result = a << 1;                // SHL",
    "            3'b111: result = {1'b0, a >> 1};        // SHR",
    "            default: result = 6'd0;",
    "        endcase",
    "    end",
    "endmodule"
]
y_alu = 95
for line in alu_code:
    p8.insert_text(fitz.Point(60, y_alu), line, fontname='arial', fontsize=7.6, color=BLUE)
    y_alu += 11.2

# Exercise 7B Blanks
p8.insert_text(fitz.Point(180, 467), "/", fontname='arial', fontsize=10.5, color=BLUE)
p8.insert_text(fitz.Point(180, 477), "%", fontname='arial', fontsize=10.5, color=BLUE)

# Exercise 8: Verification Table on Page 8
verif_p8 = [
    (655, "08"),
    (674, "02"),
    (692, "01"),
    (711, "07"),
    (729, "06"),
    (748, "26")
]
for y_pos, val in verif_p8:
    p8.insert_text(fitz.Point(305, y_pos), val, fontname='arial', fontsize=9.5, color=BLUE)

# =============================================================================
# PAGE 9: Exercise 8 (Verification Table cont.)
# =============================================================================
p9 = doc[8]
p9.insert_font(fontname='arial', fontfile=font_arial)

p9.insert_text(fitz.Point(305, 67), "10", fontname='arial', fontsize=9.5, color=BLUE)
p9.insert_text(fitz.Point(305, 86), "15", fontname='arial', fontsize=9.5, color=BLUE)

output_path = 'D:/vhdl/lab/lab4_Answered.pdf'
doc.save(output_path)
print('Successfully saved cleanly answered lab4 PDF to:', output_path)
