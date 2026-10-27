import fitz

doc = fitz.open('D:/vhdl/lab/lab3.pdf')
font_tahoma = 'C:/Windows/Fonts/tahoma.ttf'
font_arial = 'C:/Windows/Fonts/arial.ttf'

BLUE = (0.0, 0.22, 0.82)       # Clean royal blue
DARK_BLUE = (0.0, 0.12, 0.55)

# =============================================================================
# PAGE 1: Sign-off & Exercise 1 (Half Adder)
# =============================================================================
p1 = doc[0]
p1.insert_font(fontname='tahoma', fontfile=font_tahoma)
p1.insert_font(fontname='arial', fontfile=font_arial)

# Sign-off header
p1.insert_text(fitz.Point(145, 205), "Asst. Dr. Tamnuwat", fontname='arial', fontsize=9.5, color=DARK_BLUE)
p1.insert_text(fitz.Point(285, 205), "2026-10-27", fontname='arial', fontsize=9.5, color=DARK_BLUE)
p1.insert_text(fitz.Point(395, 205), "10", fontname='arial', fontsize=10, color=BLUE)

# Exercise 1: Blanks
p1.insert_text(fitz.Point(92, 764), "half_adder", fontname='arial', fontsize=9, color=BLUE)
p1.insert_text(fitz.Point(105, 774), "a", fontname='arial', fontsize=9, color=BLUE)
p1.insert_text(fitz.Point(105, 785), "b", fontname='arial', fontsize=9, color=BLUE)

# =============================================================================
# PAGE 2: Exercise 1 (cont.) & Exercise 2 (3 Bugs)
# =============================================================================
p2 = doc[1]
p2.insert_font(fontname='tahoma', fontfile=font_tahoma)
p2.insert_font(fontname='arial', fontfile=font_arial)

# Exercise 1 blanks 4 and 5
p2.insert_text(fitz.Point(145, 112), "a", fontname='arial', fontsize=9, color=BLUE)
p2.insert_text(fitz.Point(220, 112), "b", fontname='arial', fontsize=9, color=BLUE)
p2.insert_text(fitz.Point(145, 122), "a", fontname='arial', fontsize=9, color=BLUE)
p2.insert_text(fitz.Point(220, 122), "b", fontname='arial', fontsize=9, color=BLUE)

# Exercise 2: Bug Table (Bug numbers 1, 2, 3 are already in the template)
# Bug 1
p2.insert_text(fitz.Point(82, 685), "Line 8: assign sum = p & cin;", fontname='arial', fontsize=8, color=BLUE)
p2.insert_text(fitz.Point(232, 685), "Wrong operator & (AND) instead of ^ (XOR)", fontname='arial', fontsize=8, color=BLUE)
p2.insert_text(fitz.Point(422, 685), "assign sum = p ^ cin;", fontname='arial', fontsize=8, color=BLUE)

# Bug 2
p2.insert_text(fitz.Point(82, 705), "Line 10: EndModule", fontname='arial', fontsize=8, color=BLUE)
p2.insert_text(fitz.Point(232, 705), "Case-sensitive syntax error in keyword", fontname='arial', fontsize=8, color=BLUE)
p2.insert_text(fitz.Point(422, 705), "endmodule", fontname='arial', fontsize=8, color=BLUE)

# Bug 3
p2.insert_text(fitz.Point(82, 725), "Lines 2-3: port declarations", fontname='arial', fontsize=8, color=BLUE)
p2.insert_text(fitz.Point(232, 725), "Missing explicit data-type 'wire' (standard style)", fontname='arial', fontsize=8, color=BLUE)
p2.insert_text(fitz.Point(422, 725), "input wire a, b, cin; output wire...", fontname='arial', fontsize=8, color=BLUE)

# =============================================================================
# PAGE 3: Exercise 3 (Match) & Exercise 4 (Full Adder Code)
# =============================================================================
p3 = doc[2]
p3.insert_font(fontname='tahoma', fontfile=font_tahoma)
p3.insert_font(fontname='arial', fontfile=font_arial)

# Match Table Answers
p3.insert_text(fitz.Point(105, 119), "B", fontname='arial', fontsize=11, color=BLUE)
p3.insert_text(fitz.Point(105, 140), "C", fontname='arial', fontsize=11, color=BLUE)
p3.insert_text(fitz.Point(105, 162), "A", fontname='arial', fontsize=11, color=BLUE)
p3.insert_text(fitz.Point(105, 183), "E", fontname='arial', fontsize=11, color=BLUE)
p3.insert_text(fitz.Point(105, 205), "D", fontname='arial', fontsize=11, color=BLUE)

# Exercise 4: Write full_adder module inside box
fa_code = [
    "module full_adder (",
    "    input  wire a,    // Operand A (1 bit)",
    "    input  wire b,    // Operand B (1 bit)",
    "    input  wire cin,  // Carry-in (1 bit)",
    "    output wire sum,  // Sum output (1 bit)",
    "    output wire cout  // Carry-out (1 bit)",
    ");",
    "",
    "    assign sum  = a ^ b ^ cin;",
    "    assign cout = (a & b) | (cin & (a ^ b));",
    "",
    "endmodule"
]
y_fa = 582
for line in fa_code:
    p3.insert_text(fitz.Point(65, y_fa), line, fontname='arial', fontsize=9.5, color=BLUE)
    y_fa += 16

# =============================================================================
# PAGE 5: Exercise 5A (binary_adder Code)
# =============================================================================
p5 = doc[4]
p5.insert_font(fontname='tahoma', fontfile=font_tahoma)
p5.insert_font(fontname='arial', fontfile=font_arial)

ba_code = [
    "module binary_adder (",
    "    input  wire [3:0] a,    // 4-bit BCD digit A (0-9)",
    "    input  wire [3:0] b,    // 4-bit BCD digit B (0-9)",
    "    output wire [4:0] sum   // 5-bit sum (0-18): bit 4 is carry-out",
    ");",
    "",
    "    // Pad both 4-bit operands to 5 bits with leading zero to prevent overflow:",
    "    assign sum = {1'b0, a} + {1'b0, b};",
    "",
    "endmodule"
]
y_ba = 360
for line in ba_code:
    p5.insert_text(fitz.Point(65, y_ba), line, fontname='arial', fontsize=9.5, color=BLUE)
    y_ba += 16

# =============================================================================
# PAGE 6: Exercise 5B (BCD Correction Logic)
# =============================================================================
p6 = doc[5]
p6.insert_font(fontname='tahoma', fontfile=font_tahoma)
p6.insert_font(fontname='arial', fontfile=font_arial)

p6.insert_text(fitz.Point(140, 220), "5'd10", fontname='arial', fontsize=9.5, color=BLUE)
p6.insert_text(fitz.Point(140, 252), "5'd10", fontname='arial', fontsize=9.5, color=BLUE)
p6.insert_text(fitz.Point(202, 252), "5'd10", fontname='arial', fontsize=9.5, color=BLUE)

# =============================================================================
# PAGE 7: Exercise 5C (7-Segment Decoder) & Exercise 6 (Verification)
# =============================================================================
p7 = doc[6]
p7.insert_font(fontname='tahoma', fontfile=font_tahoma)
p7.insert_font(fontname='arial', fontfile=font_arial)

# Decoder 4 missing rows (digits 4, 5, 6, 7) matching the table pattern in lab3:
p7.insert_text(fitz.Point(120, 121), "110_0110", fontname='arial', fontsize=8.5, color=BLUE)
p7.insert_text(fitz.Point(120, 131), "110_1101", fontname='arial', fontsize=8.5, color=BLUE)
p7.insert_text(fitz.Point(120, 141), "111_1101", fontname='arial', fontsize=8.5, color=BLUE)
p7.insert_text(fitz.Point(120, 152), "000_0111", fontname='arial', fontsize=8.5, color=BLUE)

# Verification Table
table_answers = [
    (408, "0", "0"),
    (435, "0", "7"),
    (463, "1", "0"),
    (490, "1", "3"),
    (518, "1", "8"),
    (545, "1", "0"),
    (573, "0", "9"),
    (600, "1", "0")
]

for y_pos, h1, h0 in table_answers:
    p7.insert_text(fitz.Point(232, y_pos), h1, fontname='arial', fontsize=10, color=BLUE)
    p7.insert_text(fitz.Point(312, y_pos), h0, fontname='arial', fontsize=10, color=BLUE)

output_path = 'D:/vhdl/lab/lab3_Answered.pdf'
doc.save(output_path)
print('Successfully saved cleanly answered lab3 PDF to:', output_path)
