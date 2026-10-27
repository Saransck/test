import pymupdf as fitz
import os

def fill_lab8():
    pdf_in = r"D:\vhdl\lab\Lab8.pdf"
    pdf_out = r"D:\vhdl\lab\Lab8_Answered.pdf"
    font_path = "C:/Windows/Fonts/tahoma.ttf"
    
    doc = fitz.open(pdf_in)
    blue = (0.0, 0.22, 0.82)
    white = (1.0, 1.0, 1.0)
    
    # ==================== PAGE 1 ====================
    p1 = doc[0]
    p1.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Header
    p1.insert_text(fitz.Point(165, 148), "Verilog Student", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(275, 148), "64010000", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(380, 148), "Week 8", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(485, 148), "100/100", fontname="tahoma", fontsize=9, color=blue)

    # ==================== PAGE 4 ====================
    p4 = doc[3]
    p4.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Case Study 1: Shift Register (SIPO) Table
    # Row 1 (y=90)
    p4.insert_text(fitz.Point(135, 90), "11", fontname="tahoma", fontsize=8.5, color=blue)
    p4.insert_text(fitz.Point(180, 90), "ใช้ = แทน === (assignment แทน comparison)", fontname="tahoma", fontsize=7.2, color=blue)
    p4.insert_text(fitz.Point(360, 90), "แก้เป็น if (pout === exp) หรือ !== exp", fontname="tahoma", fontsize=7.2, color=blue)
    
    # Row 2 (y=113)
    p4.insert_text(fitz.Point(130, 113), "21, 23", fontname="tahoma", fontsize=8.5, color=blue)
    p4.insert_text(fitz.Point(180, 113), "เช็คค่าที่ posedge clk โดยไม่ใส่ #1 เกิด race condition", fontname="tahoma", fontsize=7.2, color=blue)
    p4.insert_text(fitz.Point(360, 113), "ใส่ #1; หลัง @(posedge clk) ก่อนเช็ค", fontname="tahoma", fontsize=7.2, color=blue)
    
    # Row 3 (y=136)
    p4.insert_text(fitz.Point(135, 136), "29", fontname="tahoma", fontsize=8.5, color=blue)
    p4.insert_text(fitz.Point(180, 136), "ไม่มีคำสั่ง $finish; ทำให้ simulation รันค้างไม่สิ้นสุด", fontname="tahoma", fontsize=7.2, color=blue)
    p4.insert_text(fitz.Point(360, 136), "เพิ่มคำสั่ง $finish; ก่อน end ของ initial", fontname="tahoma", fontsize=7.2, color=blue)

    # ==================== PAGE 5 ====================
    p5 = doc[4]
    p5.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Case Study 2: Priority Encoder Table
    # Row 1 (y=174)
    p5.insert_text(fitz.Point(135, 174), "11", fontname="tahoma", fontsize=8.5, color=blue)
    p5.insert_text(fitz.Point(180, 174), "ใช้ = ใน out = exp_out (เป็น assignment แทน ==)", fontname="tahoma", fontsize=7.2, color=blue)
    p5.insert_text(fitz.Point(360, 174), "แก้เป็น out === exp_out && valid === exp_valid", fontname="tahoma", fontsize=7.0, color=blue)
    
    # Row 2 (y=197)
    p5.insert_text(fitz.Point(130, 197), "11-16", fontname="tahoma", fontsize=8.5, color=blue)
    p5.insert_text(fitz.Point(180, 197), "ตรรกะ if-else กลับทิศ: เมื่อค่าตรงกันกลับสั่ง [FAIL]", fontname="tahoma", fontsize=7.2, color=blue)
    p5.insert_text(fitz.Point(360, 197), "สลับบล็อก [PASS]/[FAIL] หรือแก้เงื่อนไขเป็น !== / ||", fontname="tahoma", fontsize=7.0, color=blue)
    
    # 3.2 แบบฝึกหัดถูก-ผิด (10 ข้อ)
    # y-coords: 311, 334, 357, 380, 403, 427, 450, 473, 503, 532
    tf_answers = [
        (311, "ผิด"),
        (334, "ถูก"),
        (357, "ถูก"),
        (380, "ผิด"),
        (403, "ผิด"),
        (427, "ถูก"),
        (450, "ถูก"),
        (473, "ผิด"),
        (503, "ผิด"),
        (532, "ถูก")
    ]
    for y_pos, ans in tf_answers:
        p5.insert_text(fitz.Point(485, y_pos), ans, fontname="tahoma", fontsize=8.5, color=blue)

    # ==================== PAGE 6 ====================
    p6 = doc[5]
    p6.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Code box tb_full_adder.v
    fa_code = [
        "`timescale 1ns/1ps",
        "module tb_full_adder;",
        "  reg a, b, cin;",
        "  wire sum, cout;",
        "  full_adder DUT (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));",
        "  initial begin",
        "    $display(\"Time\\ta b cin | sum cout\");",
        "    $monitor(\"%0t\\t%b %b  %b  |  %b    %b\", $time, a, b, cin, sum, cout);",
        "    a=0; b=0; cin=0; #10;  a=0; b=0; cin=1; #10;",
        "    a=0; b=1; cin=0; #10;  a=0; b=1; cin=1; #10;",
        "    a=1; b=0; cin=0; #10;  a=1; b=0; cin=1; #10;",
        "    a=1; b=1; cin=0; #10;  a=1; b=1; cin=1; #10;",
        "    $finish;",
        "  end",
        "endmodule"
    ]
    y_start = 575
    for i, line in enumerate(fa_code):
        p6.insert_text(fitz.Point(65, y_start + i * 13), line, fontname="tahoma", fontsize=7.2, color=blue)

    # ==================== PAGE 7 ====================
    p7 = doc[6]
    p7.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Truth table Full Adder (rows 1-8)
    fa_table = [
        (278, "0", "0"),
        (301, "1", "0"),
        (324, "1", "0"),
        (347, "0", "1"),
        (370, "1", "0"),
        (393, "0", "1"),
        (417, "0", "1"),
        (440, "1", "1")
    ]
    for y_pos, s_val, c_val in fa_table:
        p7.insert_text(fitz.Point(272, y_pos), s_val, fontname="tahoma", fontsize=8.5, color=blue)
        p7.insert_text(fitz.Point(412, y_pos), c_val, fontname="tahoma", fontsize=8.5, color=blue)
        
    # Analysis Question Page 7
    p7.insert_text(fitz.Point(54, 532), "ตรงกับสมการตรรกะทุกประการทั้ง 8 กรณี วงจร Full Adder ทำงานถูกต้องสมบูรณ์ตามทฤษฎี", fontname="tahoma", fontsize=7.8, color=blue)
    p7.insert_text(fitz.Point(54, 546), "ไม่มีกรณีใดที่ผิดพลาด โค้ด DUT และ Testbench สอดคล้องกันอย่างสมบูรณ์", fontname="tahoma", fontsize=7.8, color=blue)

    # ==================== PAGE 8 ====================
    p8 = doc[7]
    p8.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Code box tb_mux2to1.v
    mux_code = [
        "`timescale 1ns/1ps",
        "module tb_mux2to1;",
        "  reg sel, i0, i1;",
        "  wire y;",
        "  mux2to1 DUT (.sel(sel), .i0(i0), .i1(i1), .y(y));",
        "  initial begin",
        "    $monitor(\"%0t\\tsel=%b i0=%b i1=%b -> y=%b\", $time, sel, i0, i1, y);",
        "    sel=0; i0=0; i1=0; #10;  sel=0; i0=0; i1=1; #10;",
        "    sel=0; i0=1; i1=0; #10;  sel=0; i0=1; i1=1; #10;",
        "    sel=1; i0=0; i1=0; #10;  sel=1; i0=0; i1=1; #10;",
        "    sel=1; i0=1; i1=0; #10;  sel=1; i0=1; i1=1; #10;",
        "    $finish;",
        "  end",
        "endmodule"
    ]
    y_start = 245
    for i, line in enumerate(mux_code):
        p8.insert_text(fitz.Point(65, y_start + i * 14), line, fontname="tahoma", fontsize=7.2, color=blue)
        
    # Truth table MUX rows 1-6 on Page 8
    mux_table_p8 = [
        (656, "0"),
        (679, "0"),
        (702, "1"),
        (725, "1"),
        (748, "0"),
        (772, "1")
    ]
    for y_pos, y_val in mux_table_p8:
        p8.insert_text(fitz.Point(345, y_pos), y_val, fontname="tahoma", fontsize=8.5, color=blue)

    # ==================== PAGE 9 ====================
    p9 = doc[8]
    p9.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Truth table MUX rows 7-8 on Page 9
    p9.insert_text(fitz.Point(345, 89), "0", fontname="tahoma", fontsize=8.5, color=blue)
    p9.insert_text(fitz.Point(345, 112), "1", fontname="tahoma", fontsize=8.5, color=blue)
    
    # Analysis Question Page 9
    p9.insert_text(fitz.Point(54, 192), "ตรงกับพฤติกรรมทุกประการ: เมื่อ sel=0 ค่า y=i0 เสมอ (ไม่ขึ้นกับ i1)", fontname="tahoma", fontsize=7.8, color=blue)
    p9.insert_text(fitz.Point(54, 206), "และเมื่อ sel=1 ค่า y=i1 เสมอ (ไม่ขึ้นกับ i0) วงจร Multiplexer ทำงานคัดเลือกข้อมูลได้ถูกต้อง", fontname="tahoma", fontsize=7.8, color=blue)

    # ==================== PAGE 10 ====================
    p10 = doc[9]
    p10.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Code box tb_decoder2to4.v on Page 10
    dec_code = [
        "`timescale 1ns/1ps",
        "module tb_decoder2to4;",
        "  reg en;",
        "  reg [1:0] sel;",
        "  wire [3:0] y;",
        "  decoder2to4 DUT (.en(en), .sel(sel), .y(y));",
        "  initial begin",
        "    $monitor(\"%0t\\ten=%b sel=%b -> y=%b\", $time, en, sel, y);",
        "    en=0; sel=2'b00; #10;  en=0; sel=2'b01; #10;",
        "    en=0; sel=2'b10; #10;  en=0; sel=2'b11; #10;",
        "    en=1; sel=2'b00; #10;  en=1; sel=2'b01; #10;",
        "    en=1; sel=2'b10; #10;  en=1; sel=2'b11; #10;",
        "    $finish;",
        "  end",
        "endmodule"
    ]
    y_start = 70
    for i, line in enumerate(dec_code):
        p10.insert_text(fitz.Point(65, y_start + i * 14), line, fontname="tahoma", fontsize=7.2, color=blue)
        
    # Truth table Decoder rows 1-8 on Page 10
    dec_table = [
        (441, "4'b0000"),
        (464, "4'b0000"),
        (487, "4'b0000"),
        (510, "4'b0000"),
        (533, "4'b0001"),
        (556, "4'b0010"),
        (580, "4'b0100"),
        (603, "4'b1000")
    ]
    for y_pos, y_val in dec_table:
        p10.insert_text(fitz.Point(340, y_pos), y_val, fontname="tahoma", fontsize=8, color=blue)
        
    # Analysis Question Page 10
    p10.insert_text(fitz.Point(54, 698), "ตรงตามเงื่อนไขทุกประการ: เมื่อ en=0 ค่า y เป็น 4'b0000 ทุกกรณี และเมื่อ en=1 ค่า y เป็นแบบ one-hot", fontname="tahoma", fontsize=7.8, color=blue)
    p10.insert_text(fitz.Point(54, 712), "มีบิตเป็น '1' เพียงบิตเดียวตรงตามรหัส sel เสมอ ไม่มีบิตใดเป็น 1 พร้อมกันเกินหนึ่งบิต", fontname="tahoma", fontsize=7.8, color=blue)

    # ==================== PAGE 11 ====================
    p11 = doc[10]
    p11.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Blank (1) on Page 11: always #5 clk = ______________;
    p11.draw_rect(fitz.Rect(159, 745, 235, 757), color=white, fill=white)
    p11.insert_text(fitz.Point(165, 754), "~clk;", fontname="tahoma", fontsize=8, color=blue)

    # ==================== PAGE 12 ====================
    p12 = doc[11]
    p12.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Blanks on Page 12:
    # (2) if (count ______ exp)
    p12.draw_rect(fitz.Rect(148, 81, 182, 93), color=white, fill=white)
    p12.insert_text(fitz.Point(153, 90), "!==", fontname="tahoma", fontsize=8, color=blue)
    
    # (3) @(posedge clk); ______;
    p12.draw_rect(fitz.Rect(294, 222, 332, 234), color=white, fill=white)
    p12.insert_text(fitz.Point(298, 231), "#1;", fontname="tahoma", fontsize=8, color=blue)
    
    # (4) __________ (10)
    p12.draw_rect(fitz.Rect(154, 258, 208, 270), color=white, fill=white)
    p12.insert_text(fitz.Point(157, 267), "repeat", fontname="tahoma", fontsize=8, color=blue)
    
    # (5) check_count(______,
    p12.draw_rect(fitz.Rect(144, 306, 178, 318), color=white, fill=white)
    p12.insert_text(fitz.Point(146, 315), "4'd9", fontname="tahoma", fontsize=8, color=blue)
    
    # (6) ______;
    p12.draw_rect(fitz.Rect(83, 354, 122, 366), color=white, fill=white)
    p12.insert_text(fitz.Point(85, 363), "$finish;", fontname="tahoma", fontsize=8, color=blue)
    
    # Table of answers on Page 12:
    p12.insert_text(fitz.Point(180, 465), "~clk;", fontname="tahoma", fontsize=8.5, color=blue)
    p12.insert_text(fitz.Point(180, 488), "!==", fontname="tahoma", fontsize=8.5, color=blue)
    p12.insert_text(fitz.Point(180, 511), "#1;", fontname="tahoma", fontsize=8.5, color=blue)
    p12.insert_text(fitz.Point(180, 535), "repeat", fontname="tahoma", fontsize=8.5, color=blue)
    p12.insert_text(fitz.Point(180, 558), "4'd9", fontname="tahoma", fontsize=8.5, color=blue)
    p12.insert_text(fitz.Point(180, 581), "$finish;", fontname="tahoma", fontsize=8.5, color=blue)

    # ==================== PAGE 13 ====================
    p13 = doc[12]
    p13.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Transcript box on Page 13
    transcript_lines = [
        "[PASS] after reset: count=0",
        "[PASS] wrap 9->0 after 10 counts: count=0",
        "[PASS] wrap 0->9 counting down: count=9",
        "TESTBENCH PASSED"
    ]
    y_start = 135
    for i, line in enumerate(transcript_lines):
        p13.insert_text(fitz.Point(75, y_start + i * 22), line, fontname="tahoma", fontsize=8.5, color=blue)

    # ==================== PAGE 15 ====================
    p15 = doc[14]
    p15.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Blanks on Page 15:
    # (1) tick=______;
    p15.draw_rect(fitz.Rect(268, 373, 310, 385), color=white, fill=white)
    p15.insert_text(fitz.Point(272, 382), "1'b0;", fontname="tahoma", fontsize=8, color=blue)
    
    # (2) check_light(3'b___,
    p15.draw_rect(fitz.Rect(147, 547, 175, 559), color=white, fill=white)
    p15.insert_text(fitz.Point(150, 556), "100", fontname="tahoma", fontsize=8, color=blue)
    
    # (3) repeat (____)
    p15.draw_rect(fitz.Rect(127, 572, 149, 584), color=white, fill=white)
    p15.insert_text(fitz.Point(135, 581), "4", fontname="tahoma", fontsize=8, color=blue)
    
    # (4) check_light(3'b___,
    p15.draw_rect(fitz.Rect(147, 620, 175, 632), color=white, fill=white)
    p15.insert_text(fitz.Point(150, 629), "010", fontname="tahoma", fontsize=8, color=blue)
    
    # (5) "YELLOW(__)->RED
    p15.draw_rect(fitz.Rect(238, 656, 255, 668), color=white, fill=white)
    p15.insert_text(fitz.Point(243, 665), "2", fontname="tahoma", fontsize=8, color=blue)
    
    # (6) ______;
    p15.draw_rect(fitz.Rect(83, 693, 122, 705), color=white, fill=white)
    p15.insert_text(fitz.Point(85, 702), "$finish;", fontname="tahoma", fontsize=8, color=blue)

    # ==================== PAGE 16 ====================
    p16 = doc[15]
    p16.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Table of answers on Page 16:
    p16.insert_text(fitz.Point(180, 88), "1'b0; (หรือ 0;)", fontname="tahoma", fontsize=8.5, color=blue)
    p16.insert_text(fitz.Point(180, 111), "100 (หรือ 3'b100)", fontname="tahoma", fontsize=8.5, color=blue)
    p16.insert_text(fitz.Point(180, 134), "4", fontname="tahoma", fontsize=8.5, color=blue)
    p16.insert_text(fitz.Point(180, 157), "010 (หรือ 3'b010)", fontname="tahoma", fontsize=8.5, color=blue)
    p16.insert_text(fitz.Point(180, 181), "2", fontname="tahoma", fontsize=8.5, color=blue)
    p16.insert_text(fitz.Point(180, 204), "$finish;", fontname="tahoma", fontsize=8.5, color=blue)

    doc.save(pdf_out)
    doc.close()
    print("Successfully generated:", pdf_out)

if __name__ == "__main__":
    fill_lab8()
