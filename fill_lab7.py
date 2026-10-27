import pymupdf as fitz
import os

def fill_lab7():
    pdf_in = r"D:\vhdl\lab\Lab7.pdf"
    pdf_out = r"D:\vhdl\lab\Lab7_Answered.pdf"
    font_path = "C:/Windows/Fonts/tahoma.ttf"
    
    doc = fitz.open(pdf_in)
    blue = (0.0, 0.22, 0.82)
    white = (1.0, 1.0, 1.0)
    
    # ==================== PAGE 1 ====================
    p1 = doc[0]
    p1.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Header
    p1.insert_text(fitz.Point(90, 148), "Verilog Student", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(255, 148), "64010000", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(345, 148), "Week 7", fontname="tahoma", fontsize=9, color=blue)
    p1.insert_text(fitz.Point(445, 148), "100/100", fontname="tahoma", fontsize=9, color=blue)
    
    # แบบฝึกหัดข้อ 1: True / False (10 ข้อ)
    # col ถูก/ผิด x=365, col เหตุผล x=410
    # ข้อ 1
    p1.insert_text(fitz.Point(365, 260), "ถูก", fontname="tahoma", fontsize=8.5, color=blue)
    # ข้อ 2
    p1.insert_text(fitz.Point(365, 287), "ผิด", fontname="tahoma", fontsize=8.5, color=blue)
    p1.insert_text(fitz.Point(405, 287), "Mealy มักใช้ 2-always block (รวม next-state + output)", fontname="tahoma", fontsize=7.2, color=blue)
    # ข้อ 3
    p1.insert_text(fitz.Point(365, 314), "ถูก", fontname="tahoma", fontsize=8.5, color=blue)
    # ข้อ 4
    p1.insert_text(fitz.Point(365, 348), "ผิด", fontname="tahoma", fontsize=8.5, color=blue)
    p1.insert_text(fitz.Point(405, 348), "Moore เขียน output ในวงกลม state (บนลูกศรคือ Mealy)", fontname="tahoma", fontsize=7.2, color=blue)
    # ข้อ 5
    p1.insert_text(fitz.Point(365, 381), "ถูก", fontname="tahoma", fontsize=8.5, color=blue)
    # ข้อ 6
    p1.insert_text(fitz.Point(365, 415), "ผิด", fontname="tahoma", fontsize=8.5, color=blue)
    p1.insert_text(fitz.Point(405, 415), "One-hot ใช้ N FFs มากกว่า binary ที่ใช้ ceil(log2 N) FFs", fontname="tahoma", fontsize=7.2, color=blue)
    # ข้อ 7
    p1.insert_text(fitz.Point(365, 448), "ถูก", fontname="tahoma", fontsize=8.5, color=blue)
    # ข้อ 8
    p1.insert_text(fitz.Point(365, 482), "ผิด", fontname="tahoma", fontsize=8.5, color=blue)
    p1.insert_text(fitz.Point(405, 482), "combinational ต้องใช้ blocking (=) เพื่อหลีกเลี่ยง race", fontname="tahoma", fontsize=7.2, color=blue)
    # ข้อ 9
    p1.insert_text(fitz.Point(365, 510), "ถูก", fontname="tahoma", fontsize=8.5, color=blue)
    # ข้อ 10
    p1.insert_text(fitz.Point(365, 537), "ผิด", fontname="tahoma", fontsize=8.5, color=blue)
    p1.insert_text(fitz.Point(405, 537), "ปุ่มกดนานหลาย ms ที่ 50MHz จะทริกเกอร์ซ้ำนับล้านรอบ", fontname="tahoma", fontsize=7.2, color=blue)
    
    # แบบฝึกหัดข้อ 2: ความรู้พื้นฐาน FSM (เติมช่องว่าง 10 ข้อ)
    # Q1
    p1.draw_rect(fitz.Rect(150, 617, 195, 629), color=white, fill=white)
    p1.insert_text(fitz.Point(168, 626), "3", fontname="tahoma", fontsize=8.5, color=blue)
    # Q2
    p1.draw_rect(fitz.Rect(149, 634, 193, 646), color=white, fill=white)
    p1.insert_text(fitz.Point(168, 643), "2", fontname="tahoma", fontsize=8.5, color=blue)
    # Q3
    p1.draw_rect(fitz.Rect(170, 650, 215, 662), color=white, fill=white)
    p1.insert_text(fitz.Point(173, 659), "state ปัจจุบัน", fontname="tahoma", fontsize=7.0, color=blue)
    # Q4
    p1.draw_rect(fitz.Rect(169, 667, 214, 679), color=white, fill=white)
    p1.insert_text(fitz.Point(171, 676), "state ปัจจุบัน", fontname="tahoma", fontsize=6.8, color=blue)
    p1.draw_rect(fitz.Rect(228, 667, 273, 679), color=white, fill=white)
    p1.insert_text(fitz.Point(230, 676), "input ปัจจุบัน", fontname="tahoma", fontsize=6.8, color=blue)
    # Q5
    p1.draw_rect(fitz.Rect(310, 683, 355, 695), color=white, fill=white)
    p1.insert_text(fitz.Point(318, 692), "Latch", fontname="tahoma", fontsize=8, color=blue)
    # Q6
    p1.draw_rect(fitz.Rect(244, 700, 288, 712), color=white, fill=white)
    p1.insert_text(fitz.Point(245, 709), "49_999_999", fontname="tahoma", fontsize=7.5, color=blue)
    # Q7
    p1.draw_rect(fitz.Rect(147, 716, 203, 728), color=white, fill=white)
    p1.insert_text(fitz.Point(162, 725), "active", fontname="tahoma", fontsize=8.5, color=blue)
    # Q8
    p1.draw_rect(fitz.Rect(153, 733, 198, 745), color=white, fill=white)
    p1.insert_text(fitz.Point(155, 742), "non-blocking", fontname="tahoma", fontsize=6.8, color=blue)
    p1.draw_rect(fitz.Rect(272, 733, 319, 745), color=white, fill=white)
    p1.insert_text(fitz.Point(288, 742), "<=", fontname="tahoma", fontsize=8.5, color=blue)
    # Q9
    p1.draw_rect(fitz.Rect(283, 749, 328, 761), color=white, fill=white)
    p1.insert_text(fitz.Point(292, 758), "reuse", fontname="tahoma", fontsize=8, color=blue)
    # Q10
    p1.draw_rect(fitz.Rect(251, 766, 296, 778), color=white, fill=white)
    p1.insert_text(fitz.Point(270, 775), "3", fontname="tahoma", fontsize=8.5, color=blue)
    p1.draw_rect(fitz.Rect(411, 766, 455, 778), color=white, fill=white)
    p1.insert_text(fitz.Point(430, 775), "6", fontname="tahoma", fontsize=8.5, color=blue)

    # ==================== PAGE 2 ====================
    p2 = doc[1]
    p2.insert_font(fontname="tahoma", fontfile=font_path)
    
    # แบบฝึกหัดข้อ 3: จับคู่คำศัพท์ FSM (A-H)
    # col คู่กับข้อ x ~ 275
    p2.insert_text(fitz.Point(275, 139), "2", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(275, 161), "8", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(275, 182), "4", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(275, 204), "1", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(275, 225), "3", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(275, 247), "7", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(275, 269), "5", fontname="tahoma", fontsize=8.5, color=blue)
    p2.insert_text(fitz.Point(275, 290), "6", fontname="tahoma", fontsize=8.5, color=blue)

    # ==================== PAGE 3 ====================
    p3 = doc[2]
    p3.insert_font(fontname="tahoma", fontfile=font_path)
    
    # โค้ดที่ 1
    p3.draw_rect(fitz.Rect(100, 240, 520, 295), color=white, fill=white)
    p3.insert_text(fitz.Point(45, 250), "บัคอยู่ตรงไหน: บรรทัดที่ 3–7 (ขาดกรณี YELLOW และไม่มี default)", fontname="tahoma", fontsize=8, color=blue)
    p3.insert_text(fitz.Point(45, 264), "ผิดอย่างไร / ผลกระทบ: case ไม่ครอบคลุมทุกสถานะ ทำให้เกิด Inferred Latch ซึ่งไม่พึงประสงค์", fontname="tahoma", fontsize=8, color=blue)
    p3.insert_text(fitz.Point(45, 278), "แก้ไขอย่างไร: เพิ่ม YELLOW: LEDG = 3'b010; และเพิ่ม default: LEDG = 3'b001; ก่อน endcase", fontname="tahoma", fontsize=8, color=blue)
    
    # โค้ดที่ 2
    p3.draw_rect(fitz.Rect(100, 443, 520, 498), color=white, fill=white)
    p3.insert_text(fitz.Point(45, 453), "บัคอยู่ตรงไหน: บรรทัดที่ 5 (VERIFY: unlocked = (key_match) ? 1'b1 : 1'b0;)", fontname="tahoma", fontsize=8, color=blue)
    p3.insert_text(fitz.Point(45, 467), "ผิดอย่างไร / ผลกระทบ: ผิดกฎ Moore FSM เพราะนำ input (key_match) มาใช้ใน output logic ทำให้เกิด glitch", fontname="tahoma", fontsize=8, color=blue)
    p3.insert_text(fitz.Point(45, 481), "แก้ไขอย่างไร: ตัด key_match ออก ให้ VERIFY: unlocked = 1'b0; แล้วนำ key_match ไปเช็คใน next-state logic", fontname="tahoma", fontsize=8, color=blue)
    
    # โค้ดที่ 4
    p3.draw_rect(fitz.Rect(100, 702, 520, 757), color=white, fill=white)
    p3.insert_text(fitz.Point(45, 712), "บัคอยู่ตรงไหน: บรรทัดที่ 2 (always @(state))", fontname="tahoma", fontsize=8, color=blue)
    p3.insert_text(fitz.Point(45, 726), "ผิดอย่างไร / ผลกระทบ: Sensitivity list ขาดสัญญาณ in ทำให้เมื่อ in เปลี่ยนแปลง วงจรจะไม่ประเมินผลใหม่", fontname="tahoma", fontsize=8, color=blue)
    p3.insert_text(fitz.Point(45, 740), "แก้ไขอย่างไร: แก้ไขเป็น always @(*) เพื่อให้ครอบคลุมสัญญาณ input ทั้งหมดที่ถูกอ่านในบล็อก", fontname="tahoma", fontsize=8, color=blue)

    # ==================== PAGE 7 ====================
    p7 = doc[6]
    p7.insert_font(fontname="tahoma", fontfile=font_path)
    
    # แบบฝึกหัดข้อ 9: edge_detector.v (เติม 5 ช่อง)
    p7.draw_rect(fitz.Rect(94, 534, 136, 546), color=white, fill=white)
    p7.insert_text(fitz.Point(100, 543), "1'b1;", fontname="tahoma", fontsize=8, color=blue)
    
    p7.draw_rect(fitz.Rect(94, 546, 136, 558), color=white, fill=white)
    p7.insert_text(fitz.Point(100, 555), "1'b1;", fontname="tahoma", fontsize=8, color=blue)
    
    p7.draw_rect(fitz.Rect(94, 583, 136, 595), color=white, fill=white)
    p7.insert_text(fitz.Point(98, 592), "key_in;", fontname="tahoma", fontsize=8, color=blue)
    
    p7.draw_rect(fitz.Rect(94, 595, 136, 607), color=white, fill=white)
    p7.insert_text(fitz.Point(100, 604), "r1;", fontname="tahoma", fontsize=8, color=blue)
    
    p7.draw_rect(fitz.Rect(102, 619, 153, 632), color=white, fill=white)
    p7.insert_text(fitz.Point(106, 628), "r2 & ~r1;", fontname="tahoma", fontsize=8, color=blue)

    # ==================== PAGE 8 ====================
    p8 = doc[7]
    p8.insert_font(fontname="tahoma", fontfile=font_path)
    
    # แบบฝึกหัดข้อ 10: tick_gen.v (เติม 4 ช่อง)
    p8.draw_rect(fitz.Rect(117, 241, 182, 254), color=white, fill=white)
    p8.insert_text(fitz.Point(120, 250), "26'd49_999_999);", fontname="tahoma", fontsize=7.5, color=blue)
    
    p8.draw_rect(fitz.Rect(120, 265, 163, 277), color=white, fill=white)
    p8.insert_text(fitz.Point(125, 274), "26'd0;", fontname="tahoma", fontsize=8, color=blue)
    
    p8.draw_rect(fitz.Rect(121, 277, 163, 290), color=white, fill=white)
    p8.insert_text(fitz.Point(125, 286), "26'd0;", fontname="tahoma", fontsize=8, color=blue)
    
    p8.draw_rect(fitz.Rect(121, 290, 164, 302), color=white, fill=white)
    p8.insert_text(fitz.Point(125, 299), "cnt + 1'b1;", fontname="tahoma", fontsize=8, color=blue)

    # ==================== PAGE 9 ====================
    p9 = doc[8]
    p9.insert_font(fontname="tahoma", fontfile=font_path)
    
    # TODO 1: State Register
    p9.draw_rect(fitz.Rect(113, 377, 162, 389), color=white, fill=white)
    p9.insert_text(fitz.Point(120, 386), "IDLE;", fontname="tahoma", fontsize=8, color=blue)
    
    p9.draw_rect(fitz.Rect(114, 389, 163, 401), color=white, fill=white)
    p9.insert_text(fitz.Point(120, 398), "next_state;", fontname="tahoma", fontsize=8, color=blue)
    
    # TODO 2: Next-State Logic
    # IDLE
    p9.draw_rect(fitz.Rect(149, 464, 237, 477), color=white, fill=white)
    p9.insert_text(fitz.Point(150, 473), "(digit==PW0) ? D1_OK : WRONG;", fontname="tahoma", fontsize=7.5, color=blue)
    # D1_OK
    p9.draw_rect(fitz.Rect(153, 476, 242, 489), color=white, fill=white)
    p9.insert_text(fitz.Point(154, 485), "(digit==PW1) ? D2_OK : WRONG;", fontname="tahoma", fontsize=7.5, color=blue)
    # D2_OK
    p9.draw_rect(fitz.Rect(153, 488, 242, 501), color=white, fill=white)
    p9.insert_text(fitz.Point(154, 497), "(digit==PW2) ? UNLOCKED : WRONG;", fontname="tahoma", fontsize=7.2, color=blue)
    # UNLOCKED
    p9.draw_rect(fitz.Rect(153, 501, 176, 513), color=white, fill=white)
    p9.insert_text(fitz.Point(156, 509), "3'd5)", fontname="tahoma", fontsize=7.5, color=blue)
    p9.draw_rect(fitz.Rect(211, 501, 234, 513), color=white, fill=white)
    p9.insert_text(fitz.Point(213, 509), "IDLE;", fontname="tahoma", fontsize=7.5, color=blue)
    # WRONG
    p9.draw_rect(fitz.Rect(124, 525, 232, 537), color=white, fill=white)
    p9.insert_text(fitz.Point(125, 534), "(attempt_cnt>=2'd3) ? LOCKOUT : IDLE;", fontname="tahoma", fontsize=7.2, color=blue)
    # LOCKOUT
    p9.draw_rect(fitz.Rect(144, 537, 167, 550), color=white, fill=white)
    p9.insert_text(fitz.Point(146, 546), "4'd0)", fontname="tahoma", fontsize=7.5, color=blue)
    p9.draw_rect(fitz.Rect(202, 537, 225, 550), color=white, fill=white)
    p9.insert_text(fitz.Point(204, 546), "IDLE;", fontname="tahoma", fontsize=7.5, color=blue)
    
    # TODO 3: Output Logic
    # IDLE
    p9.draw_rect(fitz.Rect(106, 649, 241, 661), color=white, fill=white)
    p9.insert_text(fitz.Point(107, 658), "unlocked=1'b0; progress=2'b00; alarm=10'd0; end", fontname="tahoma", fontsize=7.2, color=blue)
    # D1_OK
    p9.draw_rect(fitz.Rect(110, 661, 245, 673), color=white, fill=white)
    p9.insert_text(fitz.Point(111, 670), "unlocked=1'b0; progress=2'b01; alarm=10'd0; end", fontname="tahoma", fontsize=7.2, color=blue)
    # D2_OK
    p9.draw_rect(fitz.Rect(110, 673, 245, 685), color=white, fill=white)
    p9.insert_text(fitz.Point(111, 682), "unlocked=1'b0; progress=2'b10; alarm=10'd0; end", fontname="tahoma", fontsize=7.2, color=blue)
    # UNLOCKED
    p9.draw_rect(fitz.Rect(118, 685, 253, 698), color=white, fill=white)
    p9.insert_text(fitz.Point(119, 694), "unlocked=1'b1; progress=2'b11; alarm=10'd0; end", fontname="tahoma", fontsize=7.2, color=blue)
    # WRONG
    p9.draw_rect(fitz.Rect(114, 697, 249, 710), color=white, fill=white)
    p9.insert_text(fitz.Point(115, 706), "unlocked=1'b0; progress=2'b00; alarm=10'd0; end", fontname="tahoma", fontsize=7.2, color=blue)
    # LOCKOUT
    p9.draw_rect(fitz.Rect(115, 710, 250, 722), color=white, fill=white)
    p9.insert_text(fitz.Point(116, 719), "unlocked=1'b0; progress=2'b00; alarm=10'h3FF; end", fontname="tahoma", fontsize=7.2, color=blue)

    # ==================== PAGE 10 ====================
    p10 = doc[9]
    p10.insert_font(fontname="tahoma", fontfile=font_path)
    
    # 4a) Attempt counter
    p10.draw_rect(fitz.Rect(190, 63, 204, 76), color=white, fill=white)
    p10.insert_text(fitz.Point(191, 72), "2'd0;", fontname="tahoma", fontsize=7.5, color=blue)
    
    p10.draw_rect(fitz.Rect(236, 75, 276, 88), color=white, fill=white)
    p10.insert_text(fitz.Point(238, 84), "attempt_cnt + 1'b1;", fontname="tahoma", fontsize=7.5, color=blue)
    
    p10.draw_rect(fitz.Rect(79, 88, 189, 100), color=white, fill=white)
    p10.insert_text(fitz.Point(82, 97), "(state == UNLOCKED)", fontname="tahoma", fontsize=7.5, color=blue)
    p10.draw_rect(fitz.Rect(233, 88, 247, 100), color=white, fill=white)
    p10.insert_text(fitz.Point(234, 97), "2'd0;", fontname="tahoma", fontsize=7.5, color=blue)
    
    p10.draw_rect(fitz.Rect(79, 100, 189, 112), color=white, fill=white)
    p10.insert_text(fitz.Point(82, 109), "(state == LOCKOUT)", fontname="tahoma", fontsize=7.5, color=blue)
    p10.draw_rect(fitz.Rect(233, 100, 247, 112), color=white, fill=white)
    p10.insert_text(fitz.Point(234, 109), "2'd0;", fontname="tahoma", fontsize=7.5, color=blue)
    
    # 4b) WRONG 1-second delay
    p10.draw_rect(fitz.Rect(175, 162, 189, 174), color=white, fill=white)
    p10.insert_text(fitz.Point(176, 171), "1'b0;", fontname="tahoma", fontsize=7.5, color=blue)
    p10.draw_rect(fitz.Rect(159, 174, 172, 187), color=white, fill=white)
    p10.insert_text(fitz.Point(160, 183), "1'b1;", fontname="tahoma", fontsize=7.5, color=blue)
    
    # 4c) UNLOCKED auto-lock timer
    p10.draw_rect(fitz.Rect(187, 237, 201, 249), color=white, fill=white)
    p10.insert_text(fitz.Point(188, 246), "3'd0;", fontname="tahoma", fontsize=7.5, color=blue)
    p10.draw_rect(fitz.Rect(167, 249, 211, 262), color=white, fill=white)
    p10.insert_text(fitz.Point(169, 258), "unlock_timer + 1'b1;", fontname="tahoma", fontsize=7.5, color=blue)
    
    # 4d) LOCKOUT countdown timer
    p10.draw_rect(fitz.Rect(103, 323, 146, 336), color=white, fill=white)
    p10.insert_text(fitz.Point(105, 332), "4'd10;", fontname="tahoma", fontsize=7.5, color=blue)
    p10.draw_rect(fitz.Rect(103, 348, 146, 360), color=white, fill=white)
    p10.insert_text(fitz.Point(105, 356), "lock_timer - 1'b1;", fontname="tahoma", fontsize=7.5, color=blue)

    # ==================== PAGE 11 ====================
    p11 = doc[10]
    p11.insert_font(fontname="tahoma", fontfile=font_path)
    
    # 12A. ทำนาย Output จาก State (Moore Property)
    # cols: State, unlocked (x=175), progress (x=275), alarm (x=380)
    # IDLE
    p11.insert_text(fitz.Point(175, 179), "0", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(275, 179), "00", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(380, 179), "10'd0", fontname="tahoma", fontsize=8.5, color=blue)
    # D1_OK
    p11.insert_text(fitz.Point(175, 201), "0", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(275, 201), "01", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(380, 201), "10'd0", fontname="tahoma", fontsize=8.5, color=blue)
    # D2_OK
    p11.insert_text(fitz.Point(175, 222), "0", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(275, 222), "10", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(380, 222), "10'd0", fontname="tahoma", fontsize=8.5, color=blue)
    # UNLOCKED
    p11.insert_text(fitz.Point(175, 244), "1", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(275, 244), "11", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(380, 244), "10'd0", fontname="tahoma", fontsize=8.5, color=blue)
    # WRONG
    p11.insert_text(fitz.Point(175, 265), "0", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(275, 265), "00", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(380, 265), "10'd0", fontname="tahoma", fontsize=8.5, color=blue)
    # LOCKOUT
    p11.insert_text(fitz.Point(175, 287), "0", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(275, 287), "00", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(380, 287), "10'h3FF (ติดหมด)", fontname="tahoma", fontsize=8, color=blue)
    
    # 12B. ทำนาย State Transition (col Next State x=370)
    p11.insert_text(fitz.Point(370, 401), "D1_OK", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 423), "WRONG", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 444), "IDLE", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 466), "D2_OK", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 488), "WRONG", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 509), "UNLOCKED", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 531), "WRONG", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 552), "IDLE", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 574), "IDLE", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 595), "LOCKOUT", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 617), "IDLE", fontname="tahoma", fontsize=8.5, color=blue)
    p11.insert_text(fitz.Point(370, 638), "LOCKOUT", fontname="tahoma", fontsize=8.5, color=blue)
    
    # Checklist 1-2 on Page 11
    # col ผลจริง x=345, col ผ่าน x=465
    p11.insert_text(fitz.Point(345, 752), "IDLE: LEDG=000, LEDR=off, HEX0=0", fontname="tahoma", fontsize=7.2, color=blue)
    p11.insert_text(fitz.Point(345, 774), "D1_OK: LEDG=010 (progress=01)", fontname="tahoma", fontsize=7.2, color=blue)
    
    # Checkmarks on Page 11
    for cy in [751, 773]:
        shape = p11.new_shape()
        shape.draw_line(fitz.Point(465 - 4, cy), fitz.Point(465 - 1, cy + 3))
        shape.draw_line(fitz.Point(465 - 1, cy + 3), fitz.Point(465 + 5, cy - 4))
        shape.finish(color=blue, width=1.4)
        shape.commit()

    # ==================== PAGE 12 ====================
    p12 = doc[11]
    p12.insert_font(fontname="tahoma", fontfile=font_path)
    
    # Checklist 3-10 on Page 12
    p12.insert_text(fitz.Point(345, 78), "D2_OK: LEDG=100 (progress=10)", fontname="tahoma", fontsize=7.2, color=blue)
    p12.insert_text(fitz.Point(345, 100), "UNLOCKED: LEDG=111, unlocked=1", fontname="tahoma", fontsize=7.2, color=blue)
    p12.insert_text(fitz.Point(345, 133), "Auto-lock: กลับ IDLE, LEDG=000", fontname="tahoma", fontsize=7.2, color=blue)
    p12.insert_text(fitz.Point(345, 155), "WRONG -> 1s -> IDLE, HEX0=1", fontname="tahoma", fontsize=7.2, color=blue)
    p12.insert_text(fitz.Point(345, 177), "LOCKOUT: LEDR ติดหมด, HEX0=10..0", fontname="tahoma", fontsize=7.2, color=blue)
    p12.insert_text(fitz.Point(345, 198), "กลับ IDLE: LEDR ดับ, HEX0=0", fontname="tahoma", fontsize=7.2, color=blue)
    p12.insert_text(fitz.Point(345, 220), "UNLOCKED ได้ปกติ (attempt=0)", fontname="tahoma", fontsize=7.2, color=blue)
    p12.insert_text(fitz.Point(345, 241), "D1_OK -> WRONG -> IDLE (เริ่มใหม่)", fontname="tahoma", fontsize=7.2, color=blue)
    
    # Checkmarks on Page 12
    for cy in [77, 99, 132, 154, 176, 197, 219, 240]:
        shape = p12.new_shape()
        shape.draw_line(fitz.Point(465 - 4, cy), fitz.Point(465 - 1, cy + 3))
        shape.draw_line(fitz.Point(465 - 1, cy + 3), fitz.Point(465 + 5, cy - 4))
        shape.finish(color=blue, width=1.4)
        shape.commit()
        
    doc.save(pdf_out)
    doc.close()
    print("Successfully generated:", pdf_out)

if __name__ == "__main__":
    fill_lab7()
