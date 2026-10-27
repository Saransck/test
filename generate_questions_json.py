import json

questions = [
    # ==================== WEEK 2 ====================
    {
        "id": "W2_01",
        "week": 2,
        "type": "choice",
        "topic": "FPGA Device & Board Specifications",
        "question": "ชิป FPGA ที่ติดตั้งอยู่บนบอร์ด Altera DE0 คือรุ่นใด และจัดอยู่ในตระกูล (Family) ใด?",
        "options": [
            "Cyclone III รุ่น EP3C16F484C6",
            "Cyclone IV รุ่น EP4CE22F17C6",
            "Cyclone II รุ่น EP2C20F484C7",
            "MAX 10 รุ่น 10M50DAF484C7G"
        ],
        "answer_index": 0,
        "explanation": "บนบอร์ด Altera DE0 ใช้ชิป FPGA ตระกูล Cyclone III หมายเลขรุ่น EP3C16F484C6 มี Logic Elements (LEs) จำนวน 15,408 ตัว และมีตัวถังแบบ 484-pin FBGA ความเร็วเกรด 6",
        "source": "Week2_software installation.pdf Slide 5 & Practice Lab Sheet 2.pdf หัวข้อที่ 2"
    },
    {
        "id": "W2_02",
        "week": 2,
        "type": "choice",
        "topic": "FPGA Design Flow",
        "question": "ลำดับขั้นตอนการประมวลผล (Compilation Flow) ที่ถูกต้องในโปรแกรม Quartus II คือข้อใด?",
        "options": [
            "Analysis & Synthesis -> Fitter (Place & Route) -> TimeQuest Timing Analyzer -> Assembler",
            "Fitter (Place & Route) -> Analysis & Synthesis -> Assembler -> TimeQuest",
            "Assembler -> Analysis & Synthesis -> Fitter -> Programmer",
            "Analysis & Synthesis -> Assembler -> Fitter -> TimeQuest"
        ],
        "answer_index": 0,
        "explanation": "ขั้นตอน FPGA Design Flow ใน Quartus II เริ่มจาก Analysis & Synthesis (ตรวจสอบไวยากรณ์และสังเคราะห์เกต) -> Fitter (จัดสรร LEs และเดินสายสัญญาณ) -> TimeQuest Timing Analyzer (วิเคราะห์ความเร็วและ Timing) -> Assembler (สร้างไฟล์ .sof/.pof สำหรับเบิร์น)",
        "source": "Week2_software installation.pdf Slide 7"
    },
    {
        "id": "W2_03",
        "week": 2,
        "type": "choice",
        "topic": "Programming Files (.sof vs .pof)",
        "question": "ไฟล์ประเภทใดที่ถูกสร้างจาก Assembler เพื่อใช้โปรแกรมลงหน่วยความจำ SRAM ของ FPGA โดยตรงผ่านโหมด JTAG ด้วยสาย USB-Blaster?",
        "options": [
            ".sof (SRAM Object File)",
            ".pof (Programmer Object File)",
            ".vcd (Value Change Dump)",
            ".qsf (Quartus Settings File)"
        ],
        "answer_index": 0,
        "explanation": "ไฟล์ .sof (SRAM Object File) ใช้สำหรับการโปรแกรมลงหน่วยความจำ SRAM ของ FPGA ในโหมด JTAG ซึ่งข้อมูลจะสูญหายเมื่อปิดสวิตช์ไฟ ส่วนไฟล์ .pof ใช้สำหรับโปรแกรมลงชิปแฟลชคอนฟิกูเรชัน (EPCS) ผ่านโหมด Active Serial",
        "source": "Week2_software installation.pdf Slide 14"
    },
    {
        "id": "W2_04",
        "week": 2,
        "type": "tf",
        "topic": "DE0 Board Push Buttons",
        "question": "ปุ่มกด KEY[2:0] บนบอร์ด Altera DE0 มีพฤติกรรมทางไฟฟ้าเป็นแบบ Active-Low กล่าวคือ ขณะไม่กดจะมีค่าลอจิกเป็น 1 และขณะกดปุ่มจะมีค่าลอจิกเป็น 0",
        "options": [
            "ถูก (True)",
            "ผิด (False)"
        ],
        "answer_index": 0,
        "explanation": "ถูกต้อง เพราะบนบอร์ด DE0 มีวงจร Pull-up Resistor ต่อดึงสัญญาณไว้ที่ไฟเลี้ยง VCC (3.3V) ทำให้เมื่อไม่ได้กดปุ่มจะได้ลอจิก 1 และเมื่อกดปุ่มหน้าสัมผัสจะต่อลง Ground ได้ลอจิก 0",
        "source": "Practice Lab Sheet 2.pdf หัวข้อที่ 2 & Lab7.pdf หน้า 1 ข้อ 7"
    },
    {
        "id": "W2_05",
        "week": 2,
        "type": "choice",
        "topic": "DE0 7-Segment Display",
        "question": "จอแสดงผล 7 ส่วน (HEX0-HEX3) บนบอร์ด Altera DE0 เป็นแบบ Common Anode (Active-Low) หากต้องการให้แสดงตัวเลข '8' (ติดครบทุก segment) ต้องส่งรหัสบิตใด?",
        "options": [
            "7'b0000000 (7'h00)",
            "7'b1111111 (7'h7F)",
            "7'b1000000 (7'h40)",
            "7'b0111111 (7'h3F)"
        ],
        "answer_index": 0,
        "explanation": "เนื่องจากเป็นแบบ Active-Low ลอจิก 0 จะทำให้หลอด LED ในแต่ละ segment สว่าง และลอจิก 1 จะทำให้ดับ ดังนั้นการแสดงตัวเลข 8 ซึ่งต้องติดครบทั้ง 7 ส่วน (a ถึง g) จึงต้องส่งรหัส 7'b0000000",
        "source": "Week2_software installation.pdf Slide 20 & Week4_Combinational_Design.pdf Slide 20"
    },

    # ==================== WEEK 3 ====================
    {
        "id": "W3_01",
        "week": 3,
        "type": "choice",
        "topic": "Verilog Port Mapping",
        "question": "เพราะเหตุใดการเชื่อมโยงพอร์ตแบบระบุชื่อ (Named Port Mapping: `.port(signal)`) จึงได้รับคำแนะนำมากกว่าแบบตามลำดับ (Positional Port Mapping)?",
        "options": [
            "ป้องกันความผิดพลาดเมื่อลำดับพอร์ตในโมดูลย่อยมีการเปลี่ยนแปลงหรือสลับตำแหน่ง",
            "ทำให้วงจรที่สังเคราะห์ได้ทำงานได้ความเร็วสัญญาณนาฬิกา (Fmax) สูงกว่า",
            "ช่วยลดจำนวน Logic Elements ที่ต้องใช้บนชิป FPGA",
            "เป็นรูปแบบเดียวที่โปรแกรม ModelSim สามารถจำลองการทำงานได้"
        ],
        "answer_index": 0,
        "explanation": "Named Port Mapping เป็นการจับคู่สัญญาณภายนอกเข้ากับชื่อพอร์ตของโมดูลย่อยโดยตรง ทำให้แม้ว่าจะเรียงลำดับพอร์ตสลับกัน หรือมีการแก้ไขโมดูลย่อยในอนาคต การเชื่อมต่อสายสัญญาณก็จะไม่ผิดพลาด",
        "source": "Week3_foundations and language basics.pdf Slide 8 & Week8.pdf Slide 6"
    },
    {
        "id": "W3_02",
        "week": 3,
        "type": "choice",
        "topic": "Data Types (wire vs reg)",
        "question": "ข้อใดอธิบายความแตกต่างระหว่าง `wire` และ `reg` ในภาษา Verilog ได้ถูกต้องที่สุด?",
        "options": [
            "`wire` แทนสายสัญญาณที่ต้องถูกขับอย่างต่อเนื่องด้วย assign/โมดูล, ส่วน `reg` เป็นตัวแปรที่รับค่าใน procedural block (always/initial)",
            "`wire` สังเคราะห์ได้เกต combinational เสมอ, ส่วน `reg` สังเคราะห์ได้ Flip-Flop เสมอ",
            "`wire` ใช้ได้เฉพาะในโมดูลระดับบน, ส่วน `reg` ใช้ได้เฉพาะใน testbench",
            "`wire` มีขนาดข้อมูลได้แค่ 1 บิต, ส่วน `reg` มีขนาดข้อมูลเป็นบัสหลายบิตได้เท่านั้น"
        ],
        "answer_index": 0,
        "explanation": "`wire` ใช้เชื่อมต่อทางกายภาพและไม่สามารถเก็บค่าได้ ส่วน `reg` เป็นตัวแปรที่รับค่าในบล็อก procedural อย่างไรก็ตามการประกาศเป็น `reg` ไม่ได้แปลว่าจะได้ Flip-Flop เสมอไป หากเขียนใน `always @(*)` ที่มีเงื่อนไขครบถ้วน จะสังเคราะห์ได้วงจร Combinational",
        "source": "Week3_foundations and language basics.pdf Slide 12"
    },
    {
        "id": "W3_03",
        "week": 3,
        "type": "choice",
        "topic": "Bitwise vs Logical Operators",
        "question": "กำหนดให้ `a = 4'b1010` และ `b = 4'b1100` ผลลัพธ์ของนิพจน์ `a & b` และ `a && b` มีค่าเท่ากับข้อใดตามลำดับ?",
        "options": [
            "4'b1000 และ 1'b1",
            "4'b1110 และ 1'b1",
            "4'b1000 และ 4'b1111",
            "1'b1 และ 4'b1000"
        ],
        "answer_index": 0,
        "explanation": "`&` คือ Bitwise AND: 1010 & 1100 = 1000 (ขนาด 4 บิต), ส่วน `&&` คือ Logical AND: ตรวจสอบความจริงของตัวแปร โดย a != 0 (จริง) และ b != 0 (จริง) ดังนั้น จริง && จริง ได้ผลลัพธ์เป็น 1'b1 (ขนาด 1 บิต)",
        "source": "Week3_foundations and language basics.pdf Slide 18"
    },
    {
        "id": "W3_04",
        "week": 3,
        "type": "choice",
        "topic": "Majority Circuit",
        "question": "สมการตรรกะของวงจรเสียงข้างมาก 3 อินพุต (3-Input Majority Circuit: M) ใน Lab 3 คือข้อใด?",
        "options": [
            "M = (A & B) | (B & C) | (A & C)",
            "M = A ^ B ^ C",
            "M = (A | B) & (B | C) & (A | C)",
            "M = A & B & C"
        ],
        "answer_index": 0,
        "explanation": "วงจรเสียงข้างมาก (Majority Voter) จะให้เอาต์พุต M = 1 เมื่อมีอินพุตเป็น 1 ตั้งแต่ 2 ตัวขึ้นไป (คือ AB=1 หรือ BC=1 หรือ AC=1) จึงเขียนสมการได้เป็น M = (A & B) | (B & C) | (A & C)",
        "source": "lab3.pdf Exercise 3 & Practice Lab Sheet 2.pdf"
    },
    {
        "id": "W3_05",
        "week": 3,
        "type": "tf",
        "topic": "Verilog Logic Values",
        "question": "ในระบบตรรกะ 4 ระดับของ Verilog ค่า 'X' หมายถึงสถานะความต้านทานสูง (High-Impedance) และค่า 'Z' หมายถึงสถานะที่ไม่ทราบค่าหรือเกิดการชนกันของสัญญาณ (Contention)",
        "options": [
            "ถูก (True)",
            "ผิด (False)"
        ],
        "answer_index": 1,
        "explanation": "ผิด สลับความหมายกันอย่างสิ้นเชิง: ใน Verilog ค่า 'X' คือ Unknown / Contention (ไม่ทราบค่า หรือสายสัญญาณถูกขับชนกัน) ส่วน 'Z' คือ High-Impedance / Tristate (สภาวะเปิดวงจร/ความต้านทานสูง)",
        "source": "Week3_foundations and language basics.pdf Slide 14"
    },

    # ==================== WEEK 4 ====================
    {
        "id": "W4_01",
        "week": 4,
        "type": "choice",
        "topic": "Combinational Logic Properties",
        "question": "ข้อใดเป็นคุณสมบัติพื้นฐานที่สำคัญที่สุดของวงจรตรรกะเชิงผสม (Combinational Logic)?",
        "options": [
            "เอาต์พุต ณ ขณะใดๆ ขึ้นอยู่กับค่าอินพุตปัจจุบันเท่านั้น ไม่มีหน่วยความจำ และไม่มี feedback loop",
            "เอาต์พุตขึ้นอยู่กับสถานะในอดีตและสัญญาณนาฬิกาเป็นหลัก",
            "ต้องใช้ Non-blocking assignment (<=) ในการเขียนโค้ดเสมอ",
            "ต้องมีสัญญาณ Reset เข้ามาควบคุมการทำงานของเกตเสมอ"
        ],
        "answer_index": 0,
        "explanation": "วงจร Combinational Logic เป็นวงจรที่ไม่มีหน่วยความจำและไม่มีเส้นทางป้อนกลับ ค่าเอาต์พุตจะถูกประเมินผลโดยตรงจากค่าอินพุตที่ป้อนเข้ามาในขณะนั้นเพียงอย่างเดียว",
        "source": "Week4_Combinational_Design.pdf Slide 4"
    },
    {
        "id": "W4_02",
        "week": 4,
        "type": "choice",
        "topic": "Inferred Latch Causes & Prevention",
        "question": "ปัญหา Inferred Latch ในการสังเคราะห์วงจรด้วยบล็อก `always @(*)` เกิดจากสาเหตุใด และแก้ไขได้อย่างไร?",
        "options": [
            "เกิดจากเงื่อนไข if ขาด else หรือ case ขาด default; แก้ไขโดยกำหนดค่าเริ่มต้น (default assignment) ไว้ที่ต้นบล็อก",
            "เกิดจากการใช้ตัวแปรชนิด reg; แก้ไขโดยเปลี่ยนไปใช้ชนิด wire ทั้งหมด",
            "เกิดจากการใช้เครื่องหมาย blocking (=); แก้ไขโดยเปลี่ยนไปใช้ non-blocking (<=)",
            "เกิดจากการลืมต่อสัญญาณ clock; แก้ไขโดยเพิ่ม @(posedge clk) เข้าไปใน sensitivity list"
        ],
        "answer_index": 0,
        "explanation": "เมื่อบล็อก combinational มีเงื่อนไขไม่ครบทุกกรณี ตัวแปรจะต้องคงค่าเดิมไว้ ทำให้คอมไพเลอร์สร้าง Latch ขึ้นมาโดยไม่ตั้งใจ การกำหนด default assignment ไว้ที่ต้นบล็อกหรือใส่ else/default ให้ครบจะป้องกันปัญหานี้ได้อย่างสมบูรณ์",
        "source": "Week4_Combinational_Design.pdf Slide 22-23 & lab 4.pdf Section 4"
    },
    {
        "id": "W4_03",
        "week": 4,
        "type": "choice",
        "topic": "Multiplexers",
        "question": "วงจร 4-to-1 Multiplexer ที่มีพอร์ตเลือก `sel[1:0]` จะส่งอินพุตขาใดออกไปยังเอาต์พุต เมื่อกำหนดให้ `sel = 2'b10`?",
        "options": [
            "in[2]",
            "in[0]",
            "in[1]",
            "in[3]"
        ],
        "answer_index": 0,
        "explanation": "รหัสเลือกขนาด 2 บิต `2'b10` มีค่าเท่ากับเลขฐานสิบคือ 2 ดังนั้น มัลติเพล็กเซอร์จะคัดเลือกสัญญาณจากช่องอินพุตหมายเลข 2 (`in[2]`) ส่งต่อไปยังเอาต์พุต",
        "source": "Week4_Combinational_Design.pdf Slide 8 & lab 4.pdf Exercise 1"
    },
    {
        "id": "W4_04",
        "week": 4,
        "type": "choice",
        "topic": "Priority Encoders (casez)",
        "question": "ในคำสั่ง `casez` ของภาษา Verilog เครื่องหมาย `?` มีหน้าที่และความหมายอย่างไร?",
        "options": [
            "แทนบิตที่ไม่ต้องสนใจ (Don't-Care bit) สามารถเทียบตรงกับค่า 0, 1, z หรือ x ได้ทุกค่า",
            "แทนเงื่อนไขที่ไม่สามารถสังเคราะห์เป็นฮาร์ดแวร์ได้",
            "แทนการตรวจสอบว่าตัวแปรมีสถานะเป็น High-Impedance หรือไม่",
            "ใช้เป็นตัวดำเนินการสามส่วน (Ternary Operator) ภายในคำสั่ง case"
        ],
        "answer_index": 0,
        "explanation": "คำสั่ง `casez` ยอมให้ใช้เครื่องหมาย `?` หรือตัวอักษร `z` เป็นตัวแทนของ Don't-Care บิต ซึ่งจะละเว้นการเปรียบเทียบบิตในตำแหน่งนั้น เหมาะอย่างยิ่งสำหรับการเขียน Priority Encoder ที่สนใจเฉพาะบิตที่มีนัยสำคัญสูงสุด",
        "source": "Week4_Combinational_Design.pdf Slide 16 & Lab8.pdf Case Study 2"
    },

    # ==================== WEEK 5 ====================
    {
        "id": "W5_01",
        "week": 5,
        "type": "choice",
        "topic": "Latch vs Flip-Flop",
        "question": "ความแตกต่างพื้นฐานที่สำคัญที่สุดระหว่าง Latch และ Flip-Flop คือข้อใด?",
        "options": [
            "Latch ทำงานตามระดับสัญญาณ (Level-Sensitive), ส่วน Flip-Flop ทำงานตามขอบสัญญาณนาฬิกา (Edge-Triggered)",
            "Latch มีสัญญาณรีเซ็ตเสมอ, ส่วน Flip-Flop ไม่มีสัญญาณรีเซ็ต",
            "Latch ใช้เฉพาะในวงจรอะซิงโครนัส, ส่วน Flip-Flop ใช้เฉพาะในวงจรคอมบิเนชันนัล",
            "Latch สังเคราะห์ได้เฉพาะบน FPGA, ส่วน Flip-Flop สังเคราะห์ได้เฉพาะบน ASIC"
        ],
        "answer_index": 0,
        "explanation": "Latch เป็นอุปกรณ์เก็บข้อมูลที่ตอบสนองตามระดับแรงดัน (Level-Sensitive) โดยจะส่งผ่านข้อมูลตลอดเวลาที่ Enable เป็นลอจิกสูง ส่วน Flip-Flop เป็นอุปกรณ์ที่ตอบสนองเฉพาะจังหวะขอบขาขึ้นหรือขอบขาลงของสัญญาณนาฬิกาเท่านั้น (Edge-Triggered)",
        "source": "Week5_sequential_logic.pdf Slide 5 & lab 5.pdf"
    },
    {
        "id": "W5_02",
        "week": 5,
        "type": "choice",
        "topic": "Asynchronous vs Synchronous Reset",
        "question": "โครงสร้างโค้ด Verilog ด้านล่างนี้ เป็นการทำงานของ Flip-Flop พร้อมระบบรีเซ็ตแบบใด?\n```verilog\nalways @(posedge clk or negedge rst_n) begin\n    if (!rst_n) q <= 1'b0;\n    else        q <= d;\nend\n```",
        "options": [
            "Active-Low Asynchronous Reset",
            "Active-High Synchronous Reset",
            "Active-Low Synchronous Reset",
            "Active-High Asynchronous Reset"
        ],
        "answer_index": 0,
        "explanation": "เนื่องจากสัญญาณ `rst_n` ปรากฏอยู่ใน Sensitivity list ด้วยเงื่อนไข `negedge rst_n` และทำงานเมื่อ `!rst_n` (เป็น 0) วงจรจึงสามารถรีเซ็ตได้ทันทีที่ rst_n ตกเป็น 0 โดยไม่ต้องรอสัญญาณนาฬิกา clk จึงเป็นแบบ Active-Low Asynchronous Reset",
        "source": "Week5_sequential_logic.pdf Slide 9 & lab 5.pdf Exercise 2"
    },
    {
        "id": "W5_03",
        "week": 5,
        "type": "choice",
        "topic": "Golden Rules of Assignment",
        "question": "ตามกฎมาตรฐานอุตสาหกรรม การกำหนดค่าตัวแปรใน sequential always block (`@(posedge clk)`) ควรใช้เครื่องหมายใด และเพื่อป้องกันปัญหาใด?",
        "options": [
            "Non-blocking (`<=`), เพื่อป้องกัน Race Condition ในการจำลองการทำงานของ Flip-Flop หลายตัวพร้อมกัน",
            "Blocking (`=`), เพื่อให้วงจรประเมินผลตามลำดับบรรทัดอย่างรวดเร็ว",
            "Continuous assignment (`assign`), เพื่อประหยัด Logic Elements",
            "Case Equality (`===`), เพื่อให้รองรับค่า X และ Z ได้อย่างถูกต้อง"
        ],
        "answer_index": 0,
        "explanation": "ใน sequential block ต้องใช้ Non-blocking assignment (`<=`) เสมอ เพราะจะคำนวณค่าฝั่งขวาแล้วอัปเดตลงตัวแปรพร้อมกันในเฟส NBA ป้องกันปัญหา Race Condition ที่เกิดจากลำดับการ execute ของ simulator",
        "source": "Week5_sequential_logic.pdf Slide 14-16 & Lab7.pdf หน้า 1 ข้อ 8"
    },
    {
        "id": "W5_04",
        "week": 5,
        "type": "tf",
        "topic": "Multiple Drivers Violation",
        "question": "ในภาษา Verilog การกำหนดค่า (assignment) ให้กับตัวแปร `reg` ตัวเดียวกันจากบล็อก `always` 2 บล็อกที่แยกจากกัน ถือเป็นข้อปฏิบัติที่ถูกต้องและแนะนำเพื่อแบ่งเบาภาระของสัญญาณนาฬิกา",
        "options": [
            "ถูก (True)",
            "ผิด (False)"
        ],
        "answer_index": 1,
        "explanation": "ผิด เป็นข้อห้ามเด็ดขาด (Illegal Multiple Drivers) เพราะในทางฮาร์ดแวร์จริงจะหมายถึงการนำเอาต์พุตของสองวงจรมาต่อชนกันโดยตรง ทำให้เกิดการลัดวงจร (Signal Contention) และ Quartus จะรายงานข้อผิดพลาดระหว่าง Compile",
        "source": "Week5_sequential_logic.pdf Slide 18"
    },

    # ==================== WEEK 6 ====================
    {
        "id": "W6_01",
        "week": 6,
        "type": "choice",
        "topic": "Clock Divider Calculations",
        "question": "หากต้องการสร้างสัญญาณพัลส์ความถี่ 1 Hz จากสัญญาณนาฬิกาหลัก CLOCK_50 (ความถี่ 50 MHz) ตัวนับจะต้องนับตั้งแต่ 0 ไปจนถึงค่าสูงสุด (Terminal Count) เท่าใด?",
        "options": [
            "49,999,999",
            "50,000,000",
            "24,999,999",
            "99,999,999"
        ],
        "answer_index": 0,
        "explanation": "จำนวนรอบที่ต้องการคือ 50,000,000 รอบต่อ 1 วินาที เมื่อเริ่มนับจาก 0 ค่าสูงสุดที่ต้องวนรอบกลับคือ N - 1 = 50,000,000 - 1 = 49,999,999",
        "source": "Week6_Counters_ShiftRegisters.pdf Slide 11 & Lab7.pdf หน้า 1 ข้อ 6"
    },
    {
        "id": "W6_02",
        "week": 6,
        "type": "choice",
        "topic": "Counter Bit Width",
        "question": "ตัวนับที่ต้องนับค่าตั้งแต่ 0 ถึง 49,999,999 ต้องประกาศตัวแปร Register ด้วยขนาดอย่างน้อยกี่บิต?",
        "options": [
            "26 บิต (`reg [25:0] cnt;`)",
            "25 บิต (`reg [24:0] cnt;`)",
            "24 บิต (`reg [23:0] cnt;`)",
            "32 บิต (`reg [31:0] cnt;`)"
        ],
        "answer_index": 0,
        "explanation": "เนื่องจาก 2^25 = 33,554,432 (นับได้ไม่ถึง 49,999,999) ส่วน 2^26 = 67,108,864 (ครอบคลุมได้) ดังนั้นจำนวนบิตขั้นต่ำคือ ceil(log2 50,000,000) = 26 บิต",
        "source": "Week6_Counters_ShiftRegisters.pdf Slide 12 & Lab7.pdf หน้า 8"
    },
    {
        "id": "W6_03",
        "week": 6,
        "type": "choice",
        "topic": "Shift Register Concatenation",
        "question": "คำสั่งในข้อใดเป็นการเลื่อนบิตไปทางซ้าย 1 ตำแหน่ง (Shift Left) โดยรับบิตข้อมูลอินพุต `sin` เข้ามาที่ตำแหน่ง LSB ของ Register ขนาด 8 บิต `q`?",
        "options": [
            "q <= {q[6:0], sin};",
            "q <= {sin, q[7:1]};",
            "q <= {q[7:1], sin};",
            "q <= {sin, q[6:0]};"
        ],
        "answer_index": 0,
        "explanation": "การเลื่อนข้อมูลไปทางซ้าย (Shift Left) บิตเดิมตำแหน่ง 6 ถึง 0 จะถูกขยับขึ้นไปอยู่ที่ตำแหน่ง 7 ถึง 1 และตำแหน่งบิตต่ำสุด (LSB) จะรับข้อมูลใหม่ `sin` เข้ามา จึงเขียนด้วย Concatenation operator ได้เป็น `{q[6:0], sin}`",
        "source": "Week6_Counters_ShiftRegisters.pdf Slide 17 & Lab6.pdf Section 4"
    },
    {
        "id": "W6_04",
        "week": 6,
        "type": "choice",
        "topic": "Ring vs Johnson Counter",
        "question": "Ring Counter ขนาด N บิต และ Johnson Counter ขนาด N บิต มีจำนวนสถานะการทำงาน (Number of States) ที่แตกต่างกันเท่าใดตามลำดับ?",
        "options": [
            "N สถานะ และ 2N สถานะ",
            "2^N สถานะ และ N สถานะ",
            "2N สถานะ และ N สถานะ",
            "N สถานะ และ 2^N สถานะ"
        ],
        "answer_index": 0,
        "explanation": "Ring Counter จะวนบิต 1 เพียงบิตเดียวไปตาม flip-flop จึงมี N สถานะ ส่วน Johnson Counter (Twisted Ring Counter) จะนำเอาต์พุตตัวสุดท้ายกลับค่า (Inverted feedback) วนกลับมาที่ตัวแรก ทำให้มีจำนวนสถานะเป็น 2 เท่าของจำนวน Flip-Flop คือ 2N สถานะ",
        "source": "Week6_Counters_ShiftRegisters.pdf Slide 20"
    },

    # ==================== WEEK 7 ====================
    {
        "id": "W7_01",
        "week": 7,
        "type": "choice",
        "topic": "Moore vs Mealy FSM Output Dependency",
        "question": "ข้อใดอธิบายความแตกต่างด้านฟังก์ชันของเอาต์พุตระหว่าง Moore FSM และ Mealy FSM ได้ถูกต้องที่สุด?",
        "options": [
            "Moore FSM เอาต์พุตขึ้นกับ Current State เท่านั้น, ส่วน Mealy FSM เอาต์พุตขึ้นกับทั้ง Current State และ Current Input",
            "Moore FSM เอาต์พุตขึ้นกับทั้ง State และ Input, ส่วน Mealy FSM เอาต์พุตขึ้นกับ State เท่านั้น",
            "Moore FSM ต้องทำงานแบบ Asynchronous, ส่วน Mealy FSM ต้องทำงานแบบ Synchronous",
            "Moore FSM มีความเร็วตอบสนองเร็วกว่า Mealy FSM 1 clock cycle เสมอ"
        ],
        "answer_index": 0,
        "explanation": "Moore FSM เอาต์พุตเป็นฟังก์ชันของสถานะปัจจุบันเพียงอย่างเดียว (Output = f(State)) ทำให้สัญญาณนิ่ง ปราศจาก Glitch ส่วน Mealy FSM เอาต์พุตเป็นฟังก์ชันของสถานะปัจจุบันร่วมกับอินพุตปัจจุบัน (Output = f(State, Input)) จึงตอบสนองได้เร็วกว่าแต่อาจเกิด Glitch ได้",
        "source": "Week7_FSM.pdf Slide 4 & Lab7.pdf หน้า 1 ข้อ 1-4"
    },
    {
        "id": "W7_02",
        "week": 7,
        "type": "choice",
        "topic": "Moore FSM 3-Always-Block Style",
        "question": "โครงสร้างโค้ดมาตรฐานแบบ 3-Always-Block ของ Moore FSM แบ่งหน้าที่การทำงานอย่างไร?",
        "options": [
            "Block 1 (Sequential): State Register, Block 2 (Combinational): Next-State Logic, Block 3 (Combinational): Output Logic",
            "Block 1: Input buffer, Block 2: Next-State Logic, Block 3: State Register",
            "Block 1: Clock divider, Block 2: State Register, Block 3: Mealy Output Logic",
            "Block 1: Reset Controller, Block 2: State Register, Block 3: 7-Segment Decoder"
        ],
        "answer_index": 0,
        "explanation": "ตามมาตรฐานอุตสาหกรรม Moore FSM จะแยกเป็น 3 บล็อกชัดเจน: 1) Sequential block อัปเดต state register ตาม clock/reset, 2) Combinational block คำนวณ next-state ตาม input, และ 3) Combinational block สร้าง output จาก current state",
        "source": "Week7_FSM.pdf Slide 11 & Lab7.pdf หน้า 1 ข้อ 1"
    },
    {
        "id": "W7_03",
        "week": 7,
        "type": "choice",
        "topic": "State Encoding Styles",
        "question": "FSM ที่มีจำนวนสถานะทั้งหมด 6 สถานะ หากเลือกใช้การเข้ารหัสแบบ One-Hot Encoding จะต้องใช้ Flip-Flop ทั้งหมดกี่ตัว และหากใช้ Binary Encoding จะต้องใช้กี่ตัว?",
        "options": [
            "One-hot ใช้ 6 ตัว, Binary ใช้ 3 ตัว",
            "One-hot ใช้ 3 ตัว, Binary ใช้ 6 ตัว",
            "One-hot ใช้ 8 ตัว, Binary ใช้ 3 ตัว",
            "One-hot ใช้ 6 ตัว, Binary ใช้ 6 ตัว"
        ],
        "answer_index": 0,
        "explanation": "One-Hot Encoding ใช้ Flip-Flop 1 ตัวต่อ 1 สถานะ สำหรับ 6 สถานะจึงต้องใช้ 6 ตัว ส่วน Binary Encoding ใช้ Flip-Flop จำนวน ceil(log2 N) = ceil(log2 6) = 3 ตัว",
        "source": "Week7_FSM.pdf Slide 7 & Lab7.pdf หน้า 1 ข้อ 10"
    },
    {
        "id": "W7_04",
        "week": 7,
        "type": "choice",
        "topic": "Edge Detector Circuit",
        "question": "ใน Lab 7 โมดูล `edge_detector.v` ตรวจจับขอบขาลง (Falling Edge) ของปุ่มกด Active-Low โดยใช้สมการลอจิกใดระหว่าง Flip-Flop ตัวที่ 1 (`r1`) และตัวที่ 2 (`r2`)?",
        "options": [
            "assign pulse_out = r2 & ~r1;",
            "assign pulse_out = ~r2 & r1;",
            "assign pulse_out = r1 ^ r2;",
            "assign pulse_out = r1 & r2;"
        ],
        "answer_index": 0,
        "explanation": "ปุ่มกดแบบ Active-Low ขณะที่เกิด Falling Edge สัญญาณจะเปลี่ยนจาก 1 ไปเป็น 0 ดังนั้นในรอบ clock นั้น `r1` (สถานะใหม่) จะเป็น 0 ขณะที่ `r2` (สถานะเก่าหน่วง 1 cycle) ยังเป็น 1 อยู่ เงื่อนไข `r2 & ~r1` จึงให้ค่าลอจิกเป็น 1 เพียง 1 clock cycle เท่านั้น",
        "source": "Week7_FSM.pdf Slide 31 & Lab7.pdf หน้า 7"
    },
    {
        "id": "W7_05",
        "week": 7,
        "type": "choice",
        "topic": "Combination Lock FSM States",
        "question": "ในระบบกลอนประตูดิจิทัล Lab 7 หากผู้ใช้งานป้อนรหัสผ่านผิดติดต่อกันครบ 3 ครั้ง ระบบจะเปลี่ยนสถานะไปยัง state ใด และมีพฤติกรรมอย่างไร?",
        "options": [
            "เข้าสู่สถานะ LOCKOUT เป็นเวลา 10 วินาที พร้อมเปิดสัญญาณเตือน alarm=10'h3FF (LEDR ติดทุกดวง)",
            "กลับสู่สถานะ IDLE ทันที และรีเซ็ตรหัสผ่านเป็นค่าเริ่มต้น",
            "เข้าสู่สถานะ UNLOCKED เพื่อให้ผู้ดูแลระบบเข้ามาแก้ไข",
            "เข้าสู่สถานะ WRONG ค้างไว้ตลอดกาลจนกว่าจะกดสวิตช์ปิดไฟบอร์ด"
        ],
        "answer_index": 0,
        "explanation": "ใน Lab 7 ตัวนับ `attempt_cnt` จะสะสมจำนวนครั้งที่ผิด เมื่อครบ 3 ครั้ง ระบบจะเปลี่ยนไปสถานะ `LOCKOUT` เป็นเวลา 10 วินาที โดยหลอด LEDR ทั้ง 10 ดวงจะติดสว่าง (`10'h3FF`) และหน้าจอ HEX0 จะนับถอยหลังจาก 10 สู่ 0",
        "source": "Lab7.pdf หน้า 9-10 & หน้า 11 ตาราง 12B ข้อ 10"
    },

    # ==================== WEEK 8 ====================
    {
        "id": "W8_01",
        "week": 8,
        "type": "choice",
        "topic": "Self-Checking Testbench Concept",
        "question": "หัวใจสำคัญของ Self-Checking Testbench ที่เหนือกว่าการทดสอบแบบดั้งเดิมคือข้อใด?",
        "options": [
            "โปรแกรมตัดสินผล PASS/FAIL ได้เองอัตโนมัติด้วยคำสั่งเปรียบเทียบและ $display โดยไม่ต้องอาศัยคนนั่งดู waveform ด้วยตา",
            "สามารถสังเคราะห์ลงชิป FPGA ได้เพื่อทดสอบความเร็วสูงสุดของฮาร์ดแวร์จริง",
            "ไม่ต้องใช้สัญญาณนาฬิกาในการทดสอบวงจร Sequential",
            "บังคับให้ใช้เฉพาะตัวดำเนินการ == และ != ในการตรวจสอบค่า"
        ],
        "answer_index": 0,
        "explanation": "Self-Checking Testbench จะเขียนเงื่อนไขเปรียบเทียบค่าเอาต์พุตจริงที่ได้จาก DUT กับค่าที่คาดหวังล่วงหน้า หากไม่ตรงกันจะรายงาน [FAIL] และบวกค่าตัวแปร errors อัตโนมัติ ทำให้รันชุดทดสอบขนาดใหญ่ได้รวดเร็วโดยไม่ต้องไล่ดูรูปคลื่นทีละเส้น",
        "source": "Week8.pdf Slide 3, 8 & Lab8.pdf หน้า 1 หัวข้อ 2.1"
    },
    {
        "id": "W8_02",
        "week": 8,
        "type": "choice",
        "topic": "Case Equality Operators (=== vs ==)",
        "question": "เพราะเหตุใดใน Testbench จึงแนะนำให้ใช้ Case Equality (`===` และ `!==`) แทน Logical Equality (`==` และ `!=`) ในการเปรียบเทียบค่า?",
        "options": [
            "เพราะ `===` และ `!==` ตรวจสอบสถานะบิต 'X' (Unknown) และ 'Z' (High-Z) ได้อย่างแม่นยำ ไม่มองข้ามบั๊กวงจรที่ลืมรีเซ็ต",
            "เพราะ `===` ทำงานเร็วกว่าในระดับฮาร์ดแวร์ FPGA จริง",
            "เพราะ `==` ไม่สามารถใช้เปรียบเทียบตัวแปรประเภท reg ได้",
            "เพราะคำสั่ง `$display` รองรับเฉพาะตัวดำเนินการ `===` เท่านั้น"
        ],
        "answer_index": 0,
        "explanation": "Logical Equality `==` หากมีบิตใดเป็น X หรือ Z ผลลัพธ์ที่ได้จะเป็น X ซึ่งในเงื่อนไข if จะถือว่าเป็นเท็จ แต่ Case Equality `===` จะเปรียบเทียบบิตต่อบิตตรงๆ ทั้ง 4 สถานะ (0, 1, X, Z) ทำให้ตรวจจับสัญญาณที่ไม่ถูกขับหรือลืมรีเซ็ตได้อย่างสมบูรณ์",
        "source": "Week8.pdf Slide 8, 30 & Lab8.pdf หน้า 5 ข้อ 2"
    },
    {
        "id": "W8_03",
        "week": 8,
        "type": "choice",
        "topic": "Race Condition in Testbench (#1 delay)",
        "question": "ใน Testbench ของวงจร Sequential การใส่การหน่วงเวลา `#1;` หลังขอบขา `@(posedge clk)` ก่อนทำการตรวจเช็คค่าเอาต์พุต มีวัตถุประสงค์เพื่ออะไร?",
        "options": [
            "ป้องกัน Race Condition โดยรอให้คำสั่ง Non-blocking (<=) ใน DUT อัปเดตค่าเสร็จสมบูรณ์ก่อนอ่านค่า",
            "หน่วงเวลาเพื่อรอให้ผู้ใช้กดปุ่มบนคีย์บอร์ดเพื่อยืนยันผล",
            "ลดความเร็วของสัญญาณนาฬิกาใน ModelSim ให้ช้าลงครึ่งหนึ่ง",
            "ป้องกันการเกิด Inferred Latch ภายในตัว Testbench"
        ],
        "answer_index": 0,
        "explanation": "คำสั่ง Non-blocking assignment ใน DUT จะอัปเดตค่าในคิวเฟส NBA หาก Testbench ตรวจสอบค่าทันที ณ ขอบ clk จะเป็นการอ่านค่าใน Active region ซึ่งจะได้ค่าเก่าก่อนอัปเดต การใส่ `#1;` จะขยับเวลาไปข้างหน้าเล็กน้อย ทำให้อ่านค่าใหม่ที่นิ่งแล้วได้อย่างถูกต้อง",
        "source": "Week8.pdf Slide 8, 30 & Lab8.pdf หน้า 4 Case Study 1, หน้า 5 ข้อ 5"
    },
    {
        "id": "W8_04",
        "week": 8,
        "type": "choice",
        "topic": "Simulation Levels",
        "question": "การจำลองการทำงานระดับใดที่รวมค่าความหน่วงเวลาจริงของลอจิกเกต (Gate Delay) และสายสัญญาณ (Routing Delay) จากไฟล์ SDF และใกล้เคียงฮาร์ดแวร์จริงที่สุด?",
        "options": [
            "Post-Implementation (Timing) Simulation",
            "RTL (Functional) Simulation",
            "Post-Synthesis Simulation",
            "Behavioral Architectural Simulation"
        ],
        "answer_index": 0,
        "explanation": "Post-Implementation (Timing) Simulation เป็นการจำลองหลังขั้นตอน Fitter (Place & Route) เสร็จสมบูรณ์ โดยจะดึงค่าหน่วงเวลาจริงจากชิปมาจำลอง ทำให้ตรวจพบปัญหา Glitch, Hazard, และ Setup/Hold Violation ร่วมกับ TimeQuest ได้",
        "source": "Week8.pdf Slide 19, 22 & Lab8.pdf หน้า 5 ข้อ 7"
    },
    {
        "id": "W8_05",
        "week": 8,
        "type": "choice",
        "topic": "ModelSim-Altera Workflow",
        "question": "ลำดับคำสั่งที่ถูกต้องในการสั่งงาน ModelSim-Altera ผ่าน Command Line ตั้งแต่เริ่มต้นจนจบการทดสอบคือข้อใด?",
        "options": [
            "vlib work -> vlog *.v -> vsim top_tb -> add wave -> run -all",
            "vsim top_tb -> vlib work -> vlog *.v -> run -all",
            "vlog *.v -> vlib work -> add wave -> vsim top_tb",
            "run -all -> vlib work -> vlog *.v -> vsim top_tb"
        ],
        "answer_index": 0,
        "explanation": "ขั้นตอนการรัน ModelSim มาตรฐานคือ: 1) `vlib work` (สร้างไลบรารี), 2) `vlog *.v` (คอมไพล์โค้ด RTL และ Testbench), 3) `vsim top_tb` (โหลดโมดูลทดสอบ), 4) `add wave` (เพิ่มสัญญาณลงหน้าต่าง waveform), 5) `run -all` (สั่งให้จำลองจนกว่าจะเจอ $finish)",
        "source": "Week8.pdf Slide 14 & Lab8.pdf หน้า 5 ข้อ 10, หน้า 12 ข้อ 5.3"
    },
    {
        "id": "W8_06",
        "week": 8,
        "type": "choice",
        "topic": "System Tasks ($display vs $monitor vs $strobe)",
        "question": "คำสั่ง System Task ตัวใดใน Verilog ที่รับประกันว่าจะพิมพ์ค่าตัวแปรที่ 'ท้ายสุดของรอบเวลา (Postponed region)' หลังจากสัญญาณ Non-blocking ทุกตัว settle เรียบร้อยแล้ว?",
        "options": [
            "$strobe",
            "$display",
            "$monitor",
            "$dumpvars"
        ],
        "answer_index": 0,
        "explanation": "`$strobe` จะถูกประเมินผลและพิมพ์ค่าใน Postponed region ที่ท้ายสุดของ time step นั้นๆ จึงรับประกันว่าจะได้ค่าที่อัปเดตเสร็จสิ้นและนิ่งจริงเสมอ แตกต่างจาก `$display` ที่พิมพ์ทันทีใน Active region",
        "source": "Week8.pdf Slide 11-12"
    },
    {
        "id": "W8_07",
        "week": 8,
        "type": "tf",
        "topic": "Functional Coverage vs Code Coverage",
        "question": "ในการทดสอบวงจร FSM การที่ชุดทดสอบสามารถทำ Code Coverage ได้ 100% (รันโค้ดครบทุกบรรทัด) มีความหมายเดียวกับและรับประกันได้ว่าทำ Functional Coverage ได้ 100% แล้ว",
        "options": [
            "ถูก (True)",
            "ผิด (False)"
        ],
        "answer_index": 1,
        "explanation": "ผิด Code coverage บอกเพียงว่าโค้ดทุกบรรทัดถูก execute แล้วหรือไม่ แต่ไม่ได้แปลว่าได้ทดสอบครบทุกสถานการณ์ตามข้อกำหนด เช่น ใน FSM แม้จะเข้าครบทุกสถานะ (State Coverage) แต่อาจยังทดสอบเส้นทางการเปลี่ยนสถานะ (Transition Coverage) ไม่ครบทุกกรณี",
        "source": "Week8.pdf Slide 29 & Lab8.pdf หน้า 5 ข้อ 9"
    },
    # ==================== WEEK 2 ADDITIONAL ====================
    {
        "id": "W2_06",
        "week": 2,
        "type": "choice",
        "topic": "Quartus Software Version Support",
        "question": "เหตุใดการพัฒนาโปรเจกต์สำหรับบอร์ด Altera DE0 (Cyclone III) จึงต้องใช้โปรแกรม Quartus II เวอร์ชัน 13.0sp1 หรือเก่ากว่า?",
        "options": [
            "เนื่องจาก Quartus II เวอร์ชัน 13.0sp1 เป็นเวอร์ชัน Web Edition สุดท้ายที่ยังคงรองรับชิปตระกูล Cyclone III ก่อนจะถูกตัดออกใน v13.1 เป็นต้นไป",
            "เนื่องจากสายดาวน์โหลด USB-Blaster ไม่รองรับระบบปฏิบัติการ 64 บิตในเวอร์ชันใหม่",
            "เนื่องจากภาษา Verilog HDL ถูกยกเลิกการรองรับใน Quartus Prime",
            "เนื่องจากชิป Cyclone III ต้องใช้ไลเซนส์แบบเสียเงินเท่านั้นในเวอร์ชันใหม่"
        ],
        "answer_index": 0,
        "explanation": "Altera ได้ตัดการรองรับชิปตระกูลรุ่นเก่ารวมถึง Cyclone III ออกจาก Quartus II Web Edition ตั้งแต่เวอร์ชัน 13.1 ขึ้นไป ดังนั้นเวอร์ชัน 13.0sp1 จึงเป็นเวอร์ชันฟรีสุดท้ายที่สามารถคอมไพล์และโปรแกรมบอร์ด DE0 ได้",
        "source": "Week2_software installation.pdf Slide 10"
    },

    # ==================== WEEK 3 ADDITIONAL ====================
    {
        "id": "W3_06",
        "week": 3,
        "type": "choice",
        "topic": "Reduction Operators",
        "question": "กำหนดให้ `data = 4'b1101` การประเมินค่านิพจน์ Reduction XOR `^data` ใน Verilog จะได้ผลลัพธ์เท่ากับข้อใด?",
        "options": [
            "1'b1",
            "1'b0",
            "4'b1101",
            "4'b0010"
        ],
        "answer_index": 0,
        "explanation": "Reduction operator `^` จะนำทุกบิตภายในตัวแปรมา XOR กันทีละบิต: 1 ^ 1 ^ 0 ^ 1 = 0 ^ 0 ^ 1 = 1'b1 (มักใช้สำหรับการคำนวณ Parity bit ขนาด 1 บิต)",
        "source": "Week3_foundations and language basics.pdf Slide 19"
    },

    # ==================== WEEK 4 ADDITIONAL ====================
    {
        "id": "W4_05",
        "week": 4,
        "type": "choice",
        "topic": "ALU Zero Flag",
        "question": "ในวงจร 4-bit ALU ของ Lab 4 สัญญาณแฟล็ก Zero (`zero`) ซึ่งบอกว่าผลลัพธ์เป็นศูนย์หรือไม่ สามารถเขียนด้วย Reduction Operator อย่างสั้นได้อย่างไร?",
        "options": [
            "assign zero = ~|result;",
            "assign zero = &result;",
            "assign zero = ^result;",
            "assign zero = |result;"
        ],
        "answer_index": 0,
        "explanation": "Reduction OR `|result` จะให้ผลเป็น 1 เมื่อมีบิตใดบิตหนึ่งเป็น 1 ดังนั้นเมื่อผลลัพธ์เป็น 0 ทุกบิต ค่า `|result` จะเป็น 0 และเมื่อนำมากลับค่าด้วย `~|result` จะได้ 1 (ตรงตามความหมายของ Zero flag)",
        "source": "Week4_Combinational_Design.pdf Slide 18 & lab 4.pdf Exercise 3"
    },

    # ==================== WEEK 5 ADDITIONAL ====================
    {
        "id": "W5_05",
        "week": 5,
        "type": "choice",
        "topic": "Register with Load Enable",
        "question": "ในโมดูล Register ขนาด 4 บิตพร้อมสัญญาณ Load Enable (`load`) หากสัญญาณนาฬิกาเกิด posedge แต่สัญญาณ `load == 0` วงจรควรมีพฤติกรรมอย่างไร?",
        "options": [
            "คงค่าเดิมไว้ไม่เปลี่ยนแปลง (Hold previous state: q <= q;)",
            "รีเซ็ตค่าเป็นศูนย์ทันที (q <= 4'd0;)",
            "กลับค่าบิตทุกบิต (Toggle: q <= ~q;)",
            "เอาต์พุตเข้าสู่สถานะความต้านทานสูง (q <= 4'bzzzz;)"
        ],
        "answer_index": 0,
        "explanation": "เมื่อสัญญาณ Load ไม่แอคทีฟ (load == 0) Register จะต้องคงค่าเดิมที่เก็บอยู่ไว้ โดยไม่มีการโหลดค่าใหม่จากอินพุต d เข้ามา",
        "source": "Week5_sequential_logic.pdf Slide 11 & lab 5.pdf Exercise 3"
    },

    # ==================== WEEK 6 ADDITIONAL ====================
    {
        "id": "W6_05",
        "week": 6,
        "type": "choice",
        "topic": "Mod-10 Counter Wrap Around",
        "question": "ในวงจร Mod-10 Up/Down Counter (นับ 0 ถึง 9) เมื่อตัวนับอยู่ที่ค่า 0 และเปิดสัญญาณนับลง (`updown == 0`) ในรอบ clock ถัดไป ตัวนับจะเปลี่ยนค่าเป็นเท่าใด?",
        "options": [
            "4'd9 (Wrap around จาก 0 สู่ 9)",
            "4'd15 (underflow สู่ 1111)",
            "4'd0 (ค้างอยู่ที่เดิม)",
            "4'd1"
        ],
        "answer_index": 0,
        "explanation": "ในระบบเลขมอดุโล 10 (Mod-10) เมื่อนับถอยหลังจาก 0 วงจรจะต้องวนกลับ (wrap around) ไปยังค่าสูงสุดของฐานมอดุโล คือ 9",
        "source": "Week6_Counters_ShiftRegisters.pdf Slide 7 & Lab6.pdf Section 2"
    },

    # ==================== WEEK 7 ADDITIONAL ====================
    {
        "id": "W7_06",
        "week": 7,
        "type": "choice",
        "topic": "FSM Sensitivity List Bug",
        "question": "ใน Lab 7 โค้ดที่ 4 พบข้อผิดพลาดในการเขียนบล็อก Mealy Next-state: `always @(state)` บั๊กนี้ส่งผลกระทบอย่างไรต่อการทำงาน?",
        "options": [
            "Sensitivity list ขาดสัญญาณอินพุต `in` ทำให้เมื่ออินพุตเปลี่ยนแต่วงจรยังอยู่ที่ state เดิม บล็อกนี้จะไม่ถูกประเมินผลใหม่",
            "ทำให้เกิด Inferred Latch บนสัญญาณนาฬิกา",
            "ทำให้ Quartus สังเคราะห์ได้วงจร Asynchronous Counter",
            "ทำให้ State Register ไม่สามารถรีเซ็ตได้"
        ],
        "answer_index": 0,
        "explanation": "ในวงจร Combinational ทุกสัญญาณที่ถูกอ่านค่าในบล็อก (รวมทั้ง state และ input) จะต้องอยู่ใน Sensitivity list การเขียน `always @(state)` จะทำให้วงจรไม่ตอบสนองต่อการเปลี่ยนแปลงของสัญญาณอินพุต ต้องแก้ไขเป็น `always @(*)`",
        "source": "Week7_FSM.pdf Slide 23 & Lab7.pdf หน้า 3 โค้ดที่ 4"
    },

    # ==================== WEEK 8 ADDITIONAL ====================
    {
        "id": "W8_08",
        "week": 8,
        "type": "choice",
        "topic": "Testbench Bug Finding (Case Study 2)",
        "question": "ใน Lab 8 แบบฝึกหัด Case Study 2 โค้ด Testbench ตรวจจับความถูกต้องผิดพลาดอย่างไรในคำสั่ง `if (out = exp_out && valid == exp_valid)`?",
        "options": [
            "มี 2 บั๊ก: 1) ใช้ `=` แทน `==` (เป็น assignment) และ 2) เมื่อเงื่อนไขเป็นจริงกลับสั่งรายงาน [FAIL] และเพิ่ม errors",
            "ลืมกำหนดค่าความถี่ของสัญญาณนาฬิกา",
            "ใช้ตัวแปร out ซ้ำซ้อนกับพอร์ตอินพุต",
            "เรียกใช้ task ก่อนประกาศชื่อโมดูล"
        ],
        "answer_index": 0,
        "explanation": "บั๊กจุดที่ 1 คือใช้เครื่องหมายเท่ากับตัวเดียว `=` ใน `out = exp_out` ซึ่งเป็นไวยากรณ์การกำหนดค่า และบั๊กจุดที่ 2 คือการสลับตรรกะ if-else โดยเมื่อค่าตรงกันกลับเข้าบล็อกรายงานข้อผิดพลาด `[FAIL]`",
        "source": "Lab8.pdf หน้า 4-5 Case Study 2"
    }
]

with open(r"D:\vhdl\exam_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully updated exam_questions.json with {len(questions)} questions.")
