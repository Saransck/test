import fitz

doc = fitz.open('D:/vhdl/lab/lab 5.pdf')
font_tahoma = 'C:/Windows/Fonts/tahoma.ttf'
font_arial = 'C:/Windows/Fonts/arial.ttf'

BLUE = (0.0, 0.22, 0.82)       # Clean royal blue
DARK_BLUE = (0.0, 0.12, 0.55)

# =============================================================================
# PAGE 1: Sign-off & Exercise 1 (Match)
# =============================================================================
p1 = doc[0]
p1.insert_font(fontname='tahoma', fontfile=font_tahoma)
p1.insert_font(fontname='arial', fontfile=font_arial)

p1.insert_text(fitz.Point(165, 199), "Asst. Dr. Tamnuwat", fontname='arial', fontsize=9.5, color=DARK_BLUE)
p1.insert_text(fitz.Point(275, 199), "2026-10-27", fontname='arial', fontsize=9.5, color=DARK_BLUE)
p1.insert_text(fitz.Point(380, 199), "10", fontname='arial', fontsize=10, color=BLUE)

# Exercise 1 Match (column Match (A-E) at x=135)
p1.insert_text(fitz.Point(135, 638), "A", fontname='arial', fontsize=10.5, color=BLUE)
p1.insert_text(fitz.Point(135, 658), "B", fontname='arial', fontsize=10.5, color=BLUE)
p1.insert_text(fitz.Point(135, 680), "D", fontname='arial', fontsize=10.5, color=BLUE)
p1.insert_text(fitz.Point(135, 708), "C", fontname='arial', fontsize=10.5, color=BLUE)
p1.insert_text(fitz.Point(135, 730), "E", fontname='arial', fontsize=10.5, color=BLUE)

# =============================================================================
# PAGE 2: Exercise 2 (Find 5 Bugs)
# =============================================================================
p2 = doc[1]
p2.insert_font(fontname='tahoma', fontfile=font_tahoma)
p2.insert_font(fontname='arial', fontfile=font_arial)

bug_rows = [
    (597, "Line 2: port list", "Syntax error: missing comma after en", "input clk, rst_n, en,"),
    (618, "Line 7: always @(...)", "Sensitivity-list error: missing negedge for rst_n", "always @(posedge clk or negedge rst_n)"),
    (638, "Line 8: if (rst_n)", "Reset-polarity error: rst_n is active-low", "if (!rst_n)"),
    (659, "Line 11: q = d;", "Blocking-assignment error in sequential block", "q <= d;"),
    (680, "Line 23: .Q(q_wire)", "Wiring case-sensitivity error: port is lower 'q'", ".q(q_wire)")
]

for y_pos, loc, wrong, corr in bug_rows:
    p2.insert_text(fitz.Point(95, y_pos), loc, fontname='arial', fontsize=7.2, color=BLUE)
    p2.insert_text(fitz.Point(180, y_pos), wrong, fontname='arial', fontsize=7.2, color=BLUE)
    p2.insert_text(fitz.Point(360, y_pos), corr, fontname='arial', fontsize=7.0, color=BLUE)

# =============================================================================
# PAGE 4: Exercise 4 Table & Exercise 5 Table
# =============================================================================
p4 = doc[3]
p4.insert_font(fontname='tahoma', fontfile=font_tahoma)
p4.insert_font(fontname='arial', fontfile=font_arial)

# Table 1: Signal values after edges
sig_rows = [
    (130, "1", "1", "1"),
    (151, "1", "0", "1"),
    (172, "1", "0", "0"),
    (193, "1", "0", "0"),
    (214, "1", "0", "0")
]

for y_pos, b_val, nb1_val, nb2_val in sig_rows:
    p4.insert_text(fitz.Point(160, y_pos), b_val, fontname='arial', fontsize=9.5, color=BLUE)
    p4.insert_text(fitz.Point(285, y_pos), nb1_val, fontname='arial', fontsize=9.5, color=BLUE)
    p4.insert_text(fitz.Point(420, y_pos), nb2_val, fontname='arial', fontsize=9.5, color=BLUE)

# Table 2: Shift register trace (Exercise 5)
sr_rows = [
    (603, "0000 0001  (8'h01)"),
    (623, "0000 0010  (8'h02)"),
    (644, "0000 0101  (8'h05)"),
    (664, "0000 1011  (8'h0B)"),
    (685, "0001 0110  (8'h16)")
]

for y_pos, val_str in sr_rows:
    p4.insert_text(fitz.Point(365, y_pos), val_str, fontname='arial', fontsize=9.5, color=BLUE)

# =============================================================================
# PAGE 6: round_function blanks & Exercise 7A (input_reg)
# =============================================================================
p6 = doc[5]
p6.insert_font(fontname='tahoma', fontfile=font_tahoma)
p6.insert_font(fontname='arial', fontfile=font_arial)

# round_function blanks
p6.insert_text(fitz.Point(205, 133), "sbox(data_in[3:0]);", fontname='arial', fontsize=8.5, color=BLUE)
p6.insert_text(fitz.Point(205, 154), "{substituted[3:0], substituted[7:4]};", fontname='arial', fontsize=8.5, color=BLUE)
p6.insert_text(fitz.Point(235, 165), "ROUND_KEY", fontname='arial', fontsize=8.5, color=BLUE)

# Exercise 7A: input_reg.v blanks
p6.insert_text(fitz.Point(165, 702), "posedge", fontname='arial', fontsize=8.5, color=BLUE)
p6.insert_text(fitz.Point(250, 715), "8'b0", fontname='arial', fontsize=8.5, color=BLUE)
p6.insert_text(fitz.Point(245, 727), "<=", fontname='arial', fontsize=8.5, color=BLUE)

# =============================================================================
# PAGE 7: Exercise 7B (register.v) & 7D (mini_cipher_top.v)
# =============================================================================
p7 = doc[6]
p7.insert_font(fontname='tahoma', fontfile=font_tahoma)
p7.insert_font(fontname='arial', fontfile=font_arial)

# Exercise 7B blanks: line 143.9 for if and 154.9 for else
p7.insert_text(fitz.Point(130, 151), "!rst_n", fontname='arial', fontsize=8.5, color=BLUE)
p7.insert_text(fitz.Point(235, 151), "{W{1'b0}}", fontname='arial', fontsize=8.5, color=BLUE)
p7.insert_text(fitz.Point(220, 162), "d", fontname='arial', fontsize=8.5, color=BLUE)

# Exercise 7D wiring code onto lines y=567 down to 701
top_lines = [
    (567, "input_reg u_in (.clk(clk), .rst_n(rst_n), .sw(SW), .data_in_reg(data_in_reg));"),
    (589, "round_function #(.ROUND_KEY(8'hA5)) u_r1 (.data_in(data_in_reg), .data_out(round1_c));"),
    (612, "register #(.W(8)) u_reg1 (.clk(clk), .rst_n(rst_n), .d(round1_c), .q(reg1_q));"),
    (634, "round_function #(.ROUND_KEY(8'h3C)) u_r2 (.data_in(reg1_q), .data_out(round2_c));"),
    (656, "register #(.W(8)) u_reg2 (.clk(clk), .rst_n(rst_n), .d(round2_c), .q(reg2_q));"),
    (679, "hex7seg u_h1 (.value(reg2_q[7:4]), .seg(HEX1)); // Hi nibble -> HEX1"),
    (701, "hex7seg u_h0 (.value(reg2_q[3:0]), .seg(HEX0)); // Lo nibble -> HEX0")
]

for y_pos, code_str in top_lines:
    p7.insert_text(fitz.Point(82, y_pos), code_str, fontname='arial', fontsize=7.8, color=BLUE)

# =============================================================================
# PAGE 8: Exercise 8 Verification Table
# =============================================================================
p8 = doc[7]
p8.insert_font(fontname='arial', fontfile=font_arial)

p8.insert_text(fitz.Point(250, 105), "D0", fontname='arial', fontsize=11, color=BLUE)
p8.insert_text(fitz.Point(250, 126), "FE", fontname='arial', fontsize=11, color=BLUE)
p8.insert_text(fitz.Point(250, 146), "E5", fontname='arial', fontsize=11, color=BLUE)
p8.insert_text(fitz.Point(250, 167), "5D", fontname='arial', fontsize=11, color=BLUE)
p8.insert_text(fitz.Point(250, 188), "23", fontname='arial', fontsize=11, color=BLUE)

output_path = 'D:/vhdl/lab/lab5_Answered.pdf'
doc.save(output_path)
print('Successfully saved cleanly answered lab5 PDF to:', output_path)
