import pymupdf as fitz
import os

def fill_lab6():
    pdf_in = r"D:\vhdl\lab\Lab6.pdf"
    pdf_out = r"D:\vhdl\lab\Lab6_Answered.pdf"
    font_path = "C:/Windows/Fonts/tahoma.ttf"
    
    doc = fitz.open(pdf_in)
    blue = (0.0, 0.22, 0.82)
    white = (1.0, 1.0, 1.0)
    
    # ---------------- PAGE 1 ----------------
    p1 = doc[0]
    p1.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Header
    p1.insert_text(fitz.Point(120, 148), "Verilog Student", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(280, 148), "64010000", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(380, 148), "Week 6", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(490, 148), "100/100", fontname="tahoma", fontsize=9, color=blue)
    
    # Ex 1: True / False
    p1.insert_text(fitz.Point(315, 250), "T", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(315, 276), "F", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(340, 276), "นับได้ 16 ค่า (0–15) เพราะ 2^4 = 16", fontname="tahoma", fontsize=8, color=blue)
    p1.insert_text(fitz.Point(315, 291), "F", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(340, 291), "ใช้ 4 bits เพราะ $clog2(10) = 4 (2^4=16 >= 10)", fontname="tahoma", fontsize=8, color=blue)
    p1.insert_text(fitz.Point(315, 305), "F", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(340, 305), "สลับกัน: Skew คือถึง FF ต่างกัน, Jitter คือขอบ clock สั่น", fontname="tahoma", fontsize=7.5, color=blue)
    p1.insert_text(fitz.Point(315, 331), "F", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(340, 331), "หารได้อย่างเดียว (f ลดลง) คูณไม่ได้ (ต้องใช้ PLL)", fontname="tahoma", fontsize=8, color=blue)
    p1.insert_text(fitz.Point(315, 347), "T", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(315, 373), "T", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(315, 399), "F", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(340, 399), "สลับกัน: UART TX ใช้ PISO, UART RX ใช้ SIPO", fontname="tahoma", fontsize=8, color=blue)
    p1.insert_text(fitz.Point(315, 425), "T", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(315, 451), "T", fontname="tahoma", fontsize=9, color=blue)
    
    # Ex 2 blanks on code (Page 1)
    p1.draw_rect(fitz.Rect(120, 580, 160, 592), color=white, fill=white)
    p1.insert_text(fitz.Point(125, 588), "reg", fontname="tahoma", fontsize=8.5, color=blue)
    
    p1.draw_rect(fitz.Rect(120, 602, 185, 614), color=white, fill=white)
    p1.insert_text(fitz.Point(125, 610), "posedge", fontname="tahoma", fontsize=8.5, color=blue)
    
    p1.draw_rect(fitz.Rect(102, 613, 172, 625), color=white, fill=white)
    p1.insert_text(fitz.Point(115, 621), "(!rst_n)", fontname="tahoma", fontsize=8.5, color=blue)
    
    p1.draw_rect(fitz.Rect(125, 634, 195, 646), color=white, fill=white)
    p1.insert_text(fitz.Point(135, 642), "(enable)", fontname="tahoma", fontsize=8.5, color=blue)
    
    p1.draw_rect(fitz.Rect(192, 655, 240, 668), color=white, fill=white)
    p1.insert_text(fitz.Point(195, 664), "1'b1;", fontname="tahoma", fontsize=8.5, color=blue)
    
    p1.draw_rect(fitz.Rect(192, 676, 240, 689), color=white, fill=white)
    p1.insert_text(fitz.Point(195, 685), "1'b1;", fontname="tahoma", fontsize=8.5, color=blue)

    # ---------------- PAGE 2 ----------------
    p2 = doc[1]
    p2.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Ex 2 Table on Page 2
    p2.insert_text(fitz.Point(130, 60), "reg", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(210, 60), "ถูก assign ค่าใน sequential always block ต้องใช้ชนิด reg", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(130, 77), "posedge", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(210, 77), "เป็น synchronous circuit ทำงานตามขอบขาขึ้นของ clock", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(130, 95), "!rst_n", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(210, 95), "Active-low reset (KEY[0]) ค่า 0 คือสั่ง reset ให้ count เป็น 0", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(130, 113), "enable", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(210, 113), "นับเมื่อ enable=1 หากเป็น 0 จะคงค่าเดิมไว้ (hold state)", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(130, 131), "1 (หรือ 1'b1)", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(210, 131), "dir=1 คือนับขึ้น (Up Counter) เพิ่มค่า count ทีละ 1", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(130, 149), "1 (หรือ 1'b1)", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(210, 149), "dir=0 คือนับลง (Down Counter) ลดค่า count ทีละ 1", fontname="tahoma", fontsize=8, color=blue)

    # Ex 3: Find 4 Bugs table (Page 2)
    p2.insert_text(fitz.Point(115, 437), "3", fontname="tahoma", fontsize=8, color=blue)
    p2.insert_text(fitz.Point(145, 437), "output clk_1hz ประกาศเป็น wire แต่ถูกกำหนดค่าใน always", fontname="tahoma", fontsize=7.2, color=blue)
    p2.insert_text(fitz.Point(365, 437), "output reg clk_1hz", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(115, 455), "5", fontname="tahoma", fontsize=8, color=blue)
    p2.insert_text(fitz.Point(145, 455), "divider 24-bit นับได้แค่ 16.7M ไม่พอนับถึง 25,000,000", fontname="tahoma", fontsize=7.2, color=blue)
    p2.insert_text(fitz.Point(365, 455), "reg [24:0] divider;", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(110, 473), "8, 9, 14", fontname="tahoma", fontsize=7.5, color=blue)
    p2.insert_text(fitz.Point(145, 473), "ใช้ blocking assignment (=) ใน sequential clocked block", fontname="tahoma", fontsize=7.2, color=blue)
    p2.insert_text(fitz.Point(365, 473), "ใช้ <= เช่น divider <= 0;", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(115, 491), "10", fontname="tahoma", fontsize=8, color=blue)
    p2.insert_text(fitz.Point(145, 491), "นับ 0 ถึง 25_000_000 รวมเป็น 25_000_001 cycles เกิน 1 รอบ", fontname="tahoma", fontsize=7.2, color=blue)
    p2.insert_text(fitz.Point(365, 491), "divider == 24_999_999", fontname="tahoma", fontsize=8, color=blue)

    # Ex 4: PLL Calculation table (Page 2)
    p2.insert_text(fitz.Point(212, 713), "1", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(248, 713), "6", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(285, 713), "300 MHz", fontname="tahoma", fontsize=8, color=blue)
    p2.insert_text(fitz.Point(348, 713), "3", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(385, 713), "100 MHz", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(212, 730), "1", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(248, 730), "6", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(285, 730), "300 MHz", fontname="tahoma", fontsize=8, color=blue)
    p2.insert_text(fitz.Point(348, 730), "12", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(385, 730), "25 MHz", fontname="tahoma", fontsize=8, color=blue)
    
    p2.insert_text(fitz.Point(212, 748), "1", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(248, 748), "6", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(285, 748), "300 MHz", fontname="tahoma", fontsize=8, color=blue)
    p2.insert_text(fitz.Point(348, 748), "4", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(385, 748), "75 MHz", fontname="tahoma", fontsize=8, color=blue)

    # ---------------- PAGE 3 ----------------
    p3 = doc[2]
    p3.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Ex 4 cont. (Page 3)
    p3.insert_text(fitz.Point(212, 60), "1", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(248, 60), "8", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(285, 60), "400 MHz", fontname="tahoma", fontsize=8, color=blue)
    p3.insert_text(fitz.Point(348, 60), "10", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(385, 60), "40 MHz", fontname="tahoma", fontsize=8, color=blue)
    
    p3.insert_text(fitz.Point(212, 77), "1", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(248, 77), "7", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(285, 77), "350 MHz", fontname="tahoma", fontsize=8, color=blue)
    p3.insert_text(fitz.Point(348, 77), "5", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(385, 77), "70 MHz", fontname="tahoma", fontsize=8, color=blue)

    # Ex 5 (a): Shift Register Types (Page 3)
    p3.insert_text(fitz.Point(240, 191), "PISO", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(285, 191), "รับข้อมูลขนาน 8 บิต แล้วเลื่อนส่งออกทีละบิตผ่านสายเดียว", fontname="tahoma", fontsize=7.2, color=blue)
    
    p3.insert_text(fitz.Point(240, 209), "SIPO", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(285, 209), "รับข้อมูลอนุกรมจาก MCU แปลงออกขนาน 8 ขาคุม LED", fontname="tahoma", fontsize=7.2, color=blue)
    
    p3.insert_text(fitz.Point(240, 226), "SISO", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(285, 226), "เข้าทีละบิต ออกทีละบิต เพื่อหน่วงเวลาสัญญาณตาม clock", fontname="tahoma", fontsize=7.2, color=blue)
    
    p3.insert_text(fitz.Point(240, 244), "PIPO", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(285, 244), "โหลดข้อมูลเข้าขนานพร้อมกันและอ่านออกขนานพร้อมกันทันที", fontname="tahoma", fontsize=7.2, color=blue)

    # Ex 5 (b) blanks on code box (Page 3)
    p3.draw_rect(fitz.Rect(99, 298, 140, 310), color=white, fill=white)
    p3.insert_text(fitz.Point(105, 307), "q[6:0]", fontname="tahoma", fontsize=8, color=blue)
    
    p3.draw_rect(fitz.Rect(125, 338, 166, 350), color=white, fill=white)
    p3.insert_text(fitz.Point(131, 347), "q[7:1]", fontname="tahoma", fontsize=8, color=blue)
    
    p3.draw_rect(fitz.Rect(124, 379, 165, 391), color=white, fill=white)
    p3.insert_text(fitz.Point(135, 388), "q[7]", fontname="tahoma", fontsize=8, color=blue)
    
    p3.draw_rect(fitz.Rect(99, 419, 170, 431), color=white, fill=white)
    p3.insert_text(fitz.Point(105, 428), "q[0] , q[3:1]", fontname="tahoma", fontsize=8, color=blue)
    
    # Ex 5 (b) Table on Page 3
    p3.insert_text(fitz.Point(245, 478), "q[6:0]", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(245, 497), "q[7:1]", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(245, 516), "q[7]", fontname="tahoma", fontsize=8.5, color=blue)
    p3.insert_text(fitz.Point(245, 535), "q[0] , q[3:1]", fontname="tahoma", fontsize=8.5, color=blue)

    # ---------------- PAGE 5 ----------------
    p5 = doc[4]
    p5.insert_font(fontname="tahoma", fontfile=font_path)
    
    # File 2: pwm.v
    p5.draw_rect(fitz.Rect(80, 95, 460, 204), color=white, fill=white)
    pwm_code = [
        "  reg [3:0] cnt;",
        "  always @(posedge clk) begin",
        "    if (!rst_n)",
        "      cnt <= 4'd0;",
        "    else",
        "      cnt <= cnt + 1'b1;",
        "  end",
        "  assign pwm_out = (cnt < level);"
    ]
    y_start = 108
    for line in pwm_code:
        p5.insert_text(fitz.Point(85, y_start), line, fontname="tahoma", fontsize=8, color=blue)
        y_start += 12

    # File 3: tick_gen.v
    p5.insert_text(fitz.Point(238, 271), "9_999_999, // 20MHz/2Hz - 1", fontname="tahoma", fontsize=7.5, color=blue)
    p5.insert_text(fitz.Point(238, 283), "1_999_999  // 20MHz/10Hz - 1", fontname="tahoma", fontsize=7.5, color=blue)
    p5.insert_text(fitz.Point(195, 394), "speed ? CNT_FAST : CNT_SLOW;", fontname="tahoma", fontsize=7.5, color=blue)
    p5.insert_text(fitz.Point(155, 444), "24'd0;", fontname="tahoma", fontsize=7.5, color=blue)
    p5.insert_text(fitz.Point(142, 456), "(cnt >= limit)", fontname="tahoma", fontsize=7.5, color=blue)
    p5.insert_text(fitz.Point(155, 468), "24'd0;", fontname="tahoma", fontsize=7.5, color=blue)
    p5.insert_text(fitz.Point(155, 492), "cnt + 1'b1;", fontname="tahoma", fontsize=7.5, color=blue)
    p5.insert_text(fitz.Point(165, 518), "(cnt == limit);", fontname="tahoma", fontsize=7.5, color=blue)

    # File 4: ring_counter.v
    p5.draw_rect(fitz.Rect(140, 663, 235, 676), color=white, fill=white)
    p5.insert_text(fitz.Point(142, 672), "8'b1000_0000;", fontname="tahoma", fontsize=8, color=blue)
    
    p5.draw_rect(fitz.Rect(135, 674, 215, 687), color=white, fill=white)
    p5.insert_text(fitz.Point(140, 683), "(!pause_n)", fontname="tahoma", fontsize=8, color=blue)
    
    p5.draw_rect(fitz.Rect(135, 695, 195, 708), color=white, fill=white)
    p5.insert_text(fitz.Point(140, 704), "(tick)", fontname="tahoma", fontsize=8, color=blue)
    
    p5.draw_rect(fitz.Rect(198, 707, 232, 719), color=white, fill=white)
    p5.insert_text(fitz.Point(200, 716), "led[6:0]", fontname="tahoma", fontsize=7.5, color=blue)
    p5.draw_rect(fitz.Rect(244, 707, 278, 719), color=white, fill=white)
    p5.insert_text(fitz.Point(246, 716), "led[7]", fontname="tahoma", fontsize=7.5, color=blue)
    
    p5.draw_rect(fitz.Rect(198, 718, 232, 730), color=white, fill=white)
    p5.insert_text(fitz.Point(200, 726), "led[0]", fontname="tahoma", fontsize=7.5, color=blue)
    p5.draw_rect(fitz.Rect(244, 718, 278, 730), color=white, fill=white)
    p5.insert_text(fitz.Point(246, 726), "led[7:1]", fontname="tahoma", fontsize=7.5, color=blue)

    # ---------------- PAGE 6 ----------------
    p6 = doc[5]
    p6.insert_font(fontname="tahoma", fontfile=font_path)
    
    # File 5: heartbeat.v - safe whiteout between y=117 and 268 (does not touch ); or endmodule)
    p6.draw_rect(fitz.Rect(80, 117, 460, 268), color=white, fill=white)
    hb_code = [
        "  reg [22:0] cnt;",
        "  always @(posedge clk) begin",
        "    if (!rst_n) begin",
        "      cnt <= 23'd0;",
        "      led <= 1'b0;",
        "    end else if (cnt == 23'd2_499_999) begin // 5MHz / (2 x 1Hz) - 1",
        "      cnt <= 23'd0;",
        "      led <= ~led; // toggle 1 Hz",
        "    end else begin",
        "      cnt <= cnt + 1'b1;",
        "    end",
        "  end"
    ]
    y_start = 126
    for line in hb_code:
        p6.insert_text(fitz.Point(85, y_start), line, fontname="tahoma", fontsize=8, color=blue)
        y_start += 12

    # ---------------- PAGE 7 ----------------
    p7 = doc[6]
    p7.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Synthesis table
    p7.insert_text(fitz.Point(280, 210), "~65 / 15,408 (< 1%)", fontname="tahoma", fontsize=8, color=blue)
    p7.insert_text(fitz.Point(280, 227), "59 registers", fontname="tahoma", fontsize=8, color=blue)
    p7.insert_text(fitz.Point(280, 245), "1 / 4 (25%)", fontname="tahoma", fontsize=8, color=blue)
    p7.insert_text(fitz.Point(280, 263), "> 100 MHz (Restricted to 100.0 MHz)", fontname="tahoma", fontsize=8, color=blue)
    p7.insert_text(fitz.Point(280, 281), "> 200 MHz", fontname="tahoma", fontsize=8, color=blue)
    p7.insert_text(fitz.Point(280, 299), "> 250 MHz", fontname="tahoma", fontsize=8, color=blue)
    
    # Vector Checkmarks
    check_ys = [368, 386, 403, 421, 440, 458]
    cx = 508
    for cy in check_ys:
        shape = p7.new_shape()
        shape.draw_line(fitz.Point(cx - 4, cy), fitz.Point(cx - 1, cy + 3))
        shape.draw_line(fitz.Point(cx - 1, cy + 3), fitz.Point(cx + 5, cy - 4))
        shape.finish(color=blue, width=1.4)
        shape.commit()
    
    doc.save(pdf_out)
    doc.close()
    print("Successfully generated:", pdf_out)

if __name__ == "__main__":
    fill_lab6()
