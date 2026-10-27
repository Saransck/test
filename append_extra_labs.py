def append_extra_labs():
    path = r"D:\vhdl\Complete_Study_Guide_Lec_and_Lab.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    extra_content = """

---

<a name="lab-9"></a>
# 📘 Lab 9 (Special): การออกแบบวงจร AES-128 Encryption ด้วย Generative AI
**แหล่งอ้างอิง:** [lab9_Lab_AES128_Encryption 1.pdf](file:///d:/vhdl/lab/lab9_Lab_AES128_Encryption%201.pdf) (หน้าที่ 1–12)

### 1. วัตถุประสงค์และสเปกมาตรฐาน (หน้าที่ 1–3)
- วงจรรับ Plaintext ขนาด 128 บิต (16 ไบต์) และ Cipher Key ขนาด 128 บิต เข้าคำนวณ Ciphertext ขนาด 128 บิต ตามมาตรฐาน NIST FIPS-197
- วงจรทำหน้าที่เข้ารหัส (Encryption) เพียงอย่างเดียว ทำงานแบบ Synchronous Sequential

### 2. ลำดับขั้นตอนการทำงาน 10 Rounds ของ AES-128 (หน้าที่ 3)
1. **Round 0:** `state = plaintext XOR round_key[0]` (ทำเฉพาะ **AddRoundKey** เท่านั้น)
2. **Round 1 ถึง 9:** ทำครบ 4 ขั้นตอน:
   - `SubBytes`: การแทนที่ไบต์แบบ Non-linear ผ่านตาราง S-Box
   - `ShiftRows`: การเลื่อนไบต์ในแต่ละแถวของ State Matrix
   - `MixColumns`: การคูณเชิงเมทริกซ์ในฟีลด์จำกัด Galois Field GF(2^8) เพื่อกระจายบิต (Diffusion)
   - `AddRoundKey`: นำ State มา XOR กับกุญแจย่อยประจำรอบ `round_key[r]`
3. **Round 10 (รอบสุดท้าย):** 
   - `state = AddRoundKey( ShiftRows( SubBytes(state) ), round_key[10] )`
   - **ข้อควรระวังสำคัญ:** ใน **Round 10 จะไม่มีขั้นตอน MixColumns** โดยเด็ดขาดตามมาตรฐานสากล

### 3. หลักการคณิตศาสตร์ของ S-Box (หน้าที่ 4)
- S-Box ไม่ใช่การสุ่มค่า แต่สร้างขึ้นจาก **GF(2^8) Multiplicative Inverse** ร่วมกับ **Affine Transformation** เหนือ $GF(2)$ เพื่อสร้างคุณสมบัติ Confusion ที่สูงสุด

---

<a name="lab-11"></a>
# 📘 Lab 11 (Special): ตัวนับขึ้น/ลงบน 7-Segment ด้วย RV32I SoC
**แหล่งอ้างอิง:** [Lab11_SoC_7seg_Counter.pdf](file:///d:/vhdl/lab/Lab11_SoC_7seg_Counter.pdf) (หน้าที่ 1–4)

### 1. โครงสร้างหน่วยประมวลผลและการจัดสรรหน่วยความจำ (Memory Map) (หน้าที่ 2)
- ระบบใช้ซอฟต์คอร์ซีพียู RISC-V สถาปัตยกรรม **RV32I Single-Cycle**
- **แผนที่หน่วยความจำ (Address Decoder `addr_decoder.v` จากบิต `addr[31:28]`):**
  - `0x0000_0000`: Instruction ROM (`imem.v`) โหลดจากไฟล์ไบนารี `main.hex`
  - `0x1000_0000`: Data RAM (`dmem.v`) สำหรับตัวแปรและ Stack
  - `0x2000_0000`: Memory-Mapped I/O Registers สำหรับควบคุมจอ 7-Segment และปุ่มกด

### 2. การแบ่งหน้าที่ระหว่างฮาร์ดแวร์และซอฟต์แวร์ (Hardware/Software Co-Design) (หน้าที่ 3–4)
- **ฮาร์ดแวร์ (`hex7seg.v`):** ทำหน้าที่ถอดรหัสเลขฐานสอง 4 บิต (0–F) ออกเป็นสัญญาณติดดับของแต่ละขีด 7 ส่วน (Common Anode Active-Low)
- **ซอฟต์แวร์ (ภาษา C บน RV32I):** โปรแกรมภาษา C มีหน้าที่เพียงเขียนค่าตัวเลขลงใน Memory-Mapped Register เช่น `HEX0 = count;` โดยไม่ต้องถอดรหัสบิตของ 7-segment เองในโค้ด C
- **การตรวจจับปุ่มกดในระดับซอฟต์แวร์ (Software Edge Detection):**
  - ความเร็ว Loop ของซีพียูเร็วกว่าการกดปุ่มของมนุษย์มาก
  - ในภาษา C ต้องเก็บค่าปุ่มของรอบก่อนหน้า (`KEY_prev`) เพื่อนำมาเปรียบเทียบกับรอบปัจจุบัน (`KEY_curr`) โดยนับเฉพาะจังหวะที่ปุ่มเปลี่ยนสถานะจากไม่กดเป็นกดเท่านั้น เพื่อป้องกันการนับซ้ำหลายรอบในการกดปุ่มค้าง
"""

    if "# 📘 Lab 9 (Special)" not in content:
        content = content + extra_content
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully appended Lab 9 and Lab 11 to Complete_Study_Guide_Lec_and_Lab.md")
    else:
        print("Lab 9 and Lab 11 already present in Complete_Study_Guide_Lec_and_Lab.md")

if __name__ == "__main__":
    append_extra_labs()
