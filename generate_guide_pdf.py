import pymupdf as fitz
import os

def create_guide_pdf():
    pdf_out = r"D:\vhdl\Lab_Solutions_Comprehensive_Guide.pdf"
    font_path = "C:/Windows/Fonts/tahoma.ttf"
    font_bold_path = "C:/Windows/Fonts/tahomabd.ttf"
    font_code_path = "C:/Windows/Fonts/consola.ttf"
    
    doc = fitz.open()
    
    dark_blue = (0.0, 0.15, 0.45)
    med_blue = (0.0, 0.30, 0.70)
    charcoal = (0.15, 0.15, 0.15)
    light_grey = (0.94, 0.95, 0.97)
    border_grey = (0.80, 0.82, 0.86)
    
    # We will read the markdown file and parse sections
    with open(r"D:\vhdl\Lab_Solutions_Comprehensive_Guide.md", "r", encoding="utf-8") as f:
        md_text = f.read()

    lines = md_text.split("\n")
    
    page = doc.new_page(width=595.32, height=841.92) # A4
    page.insert_font(fontname="tahoma", fontfile=font_path)
    page.insert_font(fontname="tahoma-bold", fontfile=font_bold_path)
    page.insert_font(fontname="consola", fontfile=font_code_path)
    
    y = 50.0
    page_num = 1
    
    def check_page(needed_height=20):
        nonlocal page, y, page_num
        if y + needed_height > 780:
            # Add footer
            page.insert_text(fitz.Point(270, 810), f"หน้า {page_num}", fontname="tahoma", fontsize=8, color=charcoal)
            page = doc.new_page(width=595.32, height=841.92)
            page.insert_font(fontname="tahoma", fontfile=font_path)
            page.insert_font(fontname="tahoma-bold", fontfile=font_bold_path)
            page.insert_font(fontname="consola", fontfile=font_code_path)
            page_num += 1
            y = 50.0
            # Header on subsequent pages
            page.insert_text(fitz.Point(50, 35), "คู่มือเฉลยและคำอธิบายข้อสอบปฏิบัติการ Digital Circuit Design (Week 2 - 8)", fontname="tahoma", fontsize=7.5, color=med_blue)
            shape = page.new_shape()
            shape.draw_line(fitz.Point(50, 40), fitz.Point(545, 40))
            shape.finish(color=border_grey, width=0.6)
            shape.commit()

    in_code_block = False
    code_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Code block toggle
        if line.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_lines = []
            else:
                in_code_block = False
                # Render accumulated code block
                code_height = len(code_lines) * 11 + 12
                check_page(code_height)
                # Background box
                shape = page.new_shape()
                shape.draw_rect(fitz.Rect(50, y, 545, y + code_height))
                shape.finish(fill=light_grey, color=border_grey, width=0.6)
                shape.commit()
                
                cy = y + 10
                for cline in code_lines:
                    page.insert_text(fitz.Point(58, cy), cline[:85], fontname="consola", fontsize=7.2, color=(0.1, 0.1, 0.1))
                    cy += 11
                y += code_height + 8
            i += 1
            continue
            
        if in_code_block:
            code_lines.append(line)
            i += 1
            continue
            
        # Empty line
        if not line.strip():
            y += 5
            i += 1
            continue
            
        # Title (# )
        if line.startswith("# "):
            title_text = line[2:].strip()
            check_page(35)
            # Decorative bar
            shape = page.new_shape()
            shape.draw_rect(fitz.Rect(50, y, 545, y + 26))
            shape.finish(fill=dark_blue, color=dark_blue)
            shape.commit()
            page.insert_text(fitz.Point(58, y + 17), title_text, fontname="tahoma-bold", fontsize=11, color=(1, 1, 1))
            y += 34
            i += 1
            continue
            
        # Section H2 (## )
        if line.startswith("## "):
            h2_text = line[3:].strip()
            check_page(28)
            page.insert_text(fitz.Point(50, y + 15), h2_text, fontname="tahoma-bold", fontsize=10.5, color=dark_blue)
            shape = page.new_shape()
            shape.draw_line(fitz.Point(50, y + 18), fitz.Point(545, y + 18))
            shape.finish(color=med_blue, width=1.0)
            shape.commit()
            y += 26
            i += 1
            continue
            
        # Sub-section H3 (### )
        if line.startswith("### "):
            h3_text = line[4:].strip()
            check_page(22)
            page.insert_text(fitz.Point(50, y + 13), h3_text, fontname="tahoma-bold", fontsize=9.2, color=med_blue)
            y += 18
            i += 1
            continue
            
        # H4 (#### )
        if line.startswith("#### "):
            h4_text = line[5:].strip()
            check_page(18)
            page.insert_text(fitz.Point(50, y + 11), h4_text, fontname="tahoma-bold", fontsize=8.5, color=charcoal)
            y += 15
            i += 1
            continue
            
        # Table Row (|)
        if line.startswith("|"):
            # Check if separator row
            if "---" in line:
                i += 1
                continue
            cells = [c.strip() for c in line.split("|")[1:-1]]
            check_page(16)
            # Render simple table row
            is_header = (i > 0 and i + 1 < len(lines) and "---" in lines[i+1])
            bg_color = (0.90, 0.93, 0.98) if is_header else (0.98, 0.98, 0.99)
            
            shape = page.new_shape()
            shape.draw_rect(fitz.Rect(50, y, 545, y + 15))
            shape.finish(fill=bg_color, color=border_grey, width=0.5)
            shape.commit()
            
            # Divide width evenly
            if len(cells) > 0:
                col_w = 495.0 / len(cells)
                for c_idx, cell_text in enumerate(cells):
                    cx = 55 + c_idx * col_w
                    fname = "tahoma-bold" if is_header else "tahoma"
                    fsize = 7.2 if is_header else 7.0
                    fcol = dark_blue if is_header else charcoal
                    clean_cell = cell_text.replace("**", "").replace("*", "")[:35]
                    page.insert_text(fitz.Point(cx, y + 10.5), clean_cell, fontname=fname, fontsize=fsize, color=fcol)
            y += 15
            i += 1
            continue

        # Bullet point or Normal paragraph
        is_bullet = line.startswith("- ") or line.startswith("* ") or line.startswith("• ")
        clean_line = line[2:].strip() if is_bullet else line.strip()
        clean_line = clean_line.replace("**", "").replace("*", "").replace("`", "")
        
        # Word wrap using insert_textbox
        indent = 62 if is_bullet else 50
        w = 545 - indent
        # Estimate height
        est_lines = max(1, len(clean_line) // 65 + 1)
        block_h = est_lines * 12 + 2
        check_page(block_h)
        
        if is_bullet:
            page.insert_text(fitz.Point(52, y + 9), "•", fontname="tahoma-bold", fontsize=8.5, color=med_blue)
            
        rect = fitz.Rect(indent, y, 545, y + block_h + 10)
        page.insert_textbox(rect, clean_line, fontname="tahoma", fontsize=8.0, color=charcoal)
        y += block_h
        i += 1

    # Final footer
    page.insert_text(fitz.Point(270, 810), f"หน้า {page_num}", fontname="tahoma", fontsize=8, color=charcoal)
    
    doc.save(pdf_out)
    doc.close()
    print("Successfully created PDF guide:", pdf_out, "Total pages:", page_num)

if __name__ == "__main__":
    create_guide_pdf()
