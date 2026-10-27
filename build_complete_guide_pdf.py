import os
import re
import pymupdf as fitz

def clean_text_for_tahoma(text):
    # Replace emojis and unsupported glyphs with clean text representations
    replacements = {
        '📘': '[WEEK]',
        '📚': '[LECTURE]',
        '🧪': '[LAB]',
        '📑': '[สารบัญ]',
        '📊': '[ตาราง]',
        '💡': '[ข้อสังเกต]',
        '⚠️': '[ข้อควรระวัง]',
        '✅': '[ผ่าน]',
        '❌': '[ไม่ผ่าน]',
        '🔍': '[วิเคราะห์]',
        '📝': '[หมายเหตุ]',
        '—': '-',
        '–': '-',
        '“': '"',
        '”': '"',
        '’': "'",
        '‘': "'",
        '≤': '<=',
        '≥': '>=',
        '≠': '!=',
        '≈': '~=',
        '×': 'x',
        '÷': '/',
        '⌈': '[',
        '⌉': ']',
        '⌊': '[',
        '⌋': ']'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def build_complete_guide_pdf():
    md_path = r"D:\vhdl\Complete_Study_Guide_Lec_and_Lab.md"
    pdf_out = r"D:\vhdl\Complete_Study_Guide_Lec_and_Lab.pdf"
    font_path = "C:/Windows/Fonts/tahoma.ttf"
    font_bold_path = "C:/Windows/Fonts/tahomabd.ttf"
    font_code_path = "C:/Windows/Fonts/consola.ttf"

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    md_text = clean_text_for_tahoma(md_text)
    lines = md_text.splitlines()

    doc = fitz.open()

    # Colors
    c_primary = (0.05, 0.20, 0.50)      # Dark Navy
    c_secondary = (0.10, 0.40, 0.75)    # Medium Blue
    c_accent = (0.02, 0.50, 0.45)       # Teal/Lab
    c_dark = (0.12, 0.14, 0.18)         # Charcoal text
    c_muted = (0.40, 0.45, 0.50)        # Muted text
    c_code_bg = (0.95, 0.96, 0.98)      # Light grey code block
    c_code_border = (0.80, 0.84, 0.90)  # Border
    c_table_hdr = (0.88, 0.92, 0.98)    # Table header bg

    left_margin = 48.0
    right_margin = 547.0
    content_width = right_margin - left_margin # 499.0
    page_bottom = 790.0
    
    current_page = doc.new_page(width=595.32, height=841.92)
    current_page.insert_font(fontname="tahoma", fontfile=font_path)
    current_page.insert_font(fontname="tahoma-bold", fontfile=font_bold_path)
    current_page.insert_font(fontname="consola", fontfile=font_code_path)

    page_num = 1
    y = 45.0

    def add_page():
        nonlocal current_page, y, page_num
        # Footer
        current_page.insert_text(fitz.Point(265, 815), f"หน้า {page_num}", fontname="tahoma", fontsize=8, color=c_muted)
        
        current_page = doc.new_page(width=595.32, height=841.92)
        current_page.insert_font(fontname="tahoma", fontfile=font_path)
        current_page.insert_font(fontname="tahoma-bold", fontfile=font_bold_path)
        current_page.insert_font(fontname="consola", fontfile=font_code_path)
        page_num += 1
        y = 48.0

        # Header
        current_page.insert_text(fitz.Point(left_margin, 32), 
            "คู่มือทบทวนและเฉลยข้อสอบฉบับสมบูรณ์: LECTURE & LAB (Week 2 - 8) | Digital Circuit Design with Verilog HDL",
            fontname="tahoma", fontsize=7.0, color=c_secondary)
        shape = current_page.new_shape()
        shape.draw_line(fitz.Point(left_margin, 38), fitz.Point(right_margin, 38))
        shape.finish(color=(0.82, 0.85, 0.90), width=0.6)
        shape.commit()

    def ensure_space(needed):
        nonlocal y
        if y + needed > page_bottom:
            add_page()

    i = 0
    in_code = False
    code_buffer = []

    while i < len(lines):
        raw_line = lines[i]
        line = raw_line.rstrip()

        # Handle code blocks
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_buffer = []
                i += 1
                continue
            else:
                in_code = False
                # Render code buffer, chunking across pages if necessary
                c_idx = 0
                line_h = 10.5
                while c_idx < len(code_buffer):
                    available_h = page_bottom - y - 16
                    if available_h < 40:
                        add_page()
                        available_h = page_bottom - y - 16

                    lines_can_fit = int(available_h // line_h)
                    chunk = code_buffer[c_idx : c_idx + lines_can_fit]
                    chunk_h = len(chunk) * line_h + 10

                    # Draw code box
                    shape = current_page.new_shape()
                    shape.draw_rect(fitz.Rect(left_margin, y, right_margin, y + chunk_h))
                    shape.finish(fill=c_code_bg, color=c_code_border, width=0.5)
                    shape.commit()

                    cy = y + 9
                    for cl in chunk:
                        current_page.insert_text(fitz.Point(left_margin + 8, cy), cl[:92], fontname="consola", fontsize=7.2, color=(0.1, 0.15, 0.2))
                        cy += line_h

                    y += chunk_h + 6
                    c_idx += len(chunk)
                i += 1
                continue

        if in_code:
            code_buffer.append(line)
            i += 1
            continue

        # Skip anchor tags <a name="..."></a>
        if line.strip().startswith("<a name=") or line.strip() == "</a>":
            i += 1
            continue

        # Empty lines
        if not line.strip():
            y += 4
            i += 1
            continue

        # Horizontal rule
        if line.strip() == "---":
            ensure_space(10)
            shape = current_page.new_shape()
            shape.draw_line(fitz.Point(left_margin, y + 4), fitz.Point(right_margin, y + 4))
            shape.finish(color=(0.85, 0.88, 0.92), width=0.7)
            shape.commit()
            y += 10
            i += 1
            continue

        # Major Header H1 (# )
        if line.startswith("# "):
            h1_text = line[2:].strip().replace("**", "")
            ensure_space(38)
            # Full banner box
            banner_bg = c_primary
            shape = current_page.new_shape()
            shape.draw_rect(fitz.Rect(left_margin, y, right_margin, y + 26))
            shape.finish(fill=banner_bg, color=banner_bg)
            shape.commit()

            current_page.insert_text(fitz.Point(left_margin + 10, y + 17), h1_text, fontname="tahoma-bold", fontsize=11.0, color=(1, 1, 1))
            y += 33
            i += 1
            continue

        # Section Header H2 (## )
        if line.startswith("## "):
            h2_text = line[3:].strip().replace("**", "")
            ensure_space(28)
            col = c_accent if "LAB" in h2_text.upper() else c_secondary
            current_page.insert_text(fitz.Point(left_margin, y + 14), h2_text, fontname="tahoma-bold", fontsize=10.0, color=col)
            shape = current_page.new_shape()
            shape.draw_line(fitz.Point(left_margin, y + 18), fitz.Point(right_margin, y + 18))
            shape.finish(color=col, width=0.8)
            shape.commit()
            y += 25
            i += 1
            continue

        # Subsection Header H3 (### )
        if line.startswith("### "):
            h3_text = line[4:].strip().replace("**", "")
            ensure_space(22)
            current_page.insert_text(fitz.Point(left_margin, y + 13), h3_text, fontname="tahoma-bold", fontsize=9.0, color=c_secondary)
            y += 18
            i += 1
            continue

        # Sub-subsection H4 (#### )
        if line.startswith("#### "):
            h4_text = line[5:].strip().replace("**", "")
            ensure_space(18)
            current_page.insert_text(fitz.Point(left_margin, y + 11), h4_text, fontname="tahoma-bold", fontsize=8.2, color=c_dark)
            y += 15
            i += 1
            continue

        # Table Row (|)
        if line.startswith("|"):
            if "---" in line:
                i += 1
                continue
            cells = [c.strip() for c in line.split("|")[1:-1]]
            ensure_space(17)
            is_header = (i > 0 and i + 1 < len(lines) and "---" in lines[i+1])
            bg_col = c_table_hdr if is_header else ((0.98, 0.98, 0.99) if (i % 2 == 0) else (1.0, 1.0, 1.0))
            
            shape = current_page.new_shape()
            shape.draw_rect(fitz.Rect(left_margin, y, right_margin, y + 15))
            shape.finish(fill=bg_col, color=c_code_border, width=0.5)
            shape.commit()

            if cells:
                col_w = content_width / len(cells)
                for c_idx, cell_text in enumerate(cells):
                    cx = left_margin + 6 + c_idx * col_w
                    fname = "tahoma-bold" if is_header else "tahoma"
                    fsize = 7.0 if is_header else 6.8
                    fcol = c_primary if is_header else c_dark
                    clean_cell = cell_text.replace("**", "").replace("*", "")[:35]
                    current_page.insert_text(fitz.Point(cx, y + 10.5), clean_cell, fontname=fname, fontsize=fsize, color=fcol)
            y += 15
            i += 1
            continue

        # Bullet point or normal text
        is_bullet = line.startswith("- ") or line.startswith("* ") or line.startswith("• ")
        clean_line = line[2:].strip() if is_bullet else line.strip()
        clean_line = clean_line.replace("**", "").replace("*", "").replace("`", "")

        indent = left_margin + 12 if is_bullet else left_margin
        box_w = right_margin - indent
        
        # Word wrap estimate
        chars_per_line = int(box_w / 5.2)
        est_lines = max(1, len(clean_line) // chars_per_line + 1)
        block_h = est_lines * 11.5 + 2
        ensure_space(block_h)

        if is_bullet:
            current_page.insert_text(fitz.Point(left_margin + 2, y + 8.5), "-", fontname="tahoma-bold", fontsize=8.0, color=c_secondary)

        rect = fitz.Rect(indent, y, right_margin, y + block_h + 8)
        current_page.insert_textbox(rect, clean_line, fontname="tahoma", fontsize=7.8, color=c_dark)
        y += block_h
        i += 1

    # Final footer on last page
    current_page.insert_text(fitz.Point(265, 815), f"หน้า {page_num}", fontname="tahoma", fontsize=8, color=c_muted)

    doc.save(pdf_out)
    doc.close()
    print(f"Successfully generated {pdf_out}")
    print(f"Total pages: {page_num}")

if __name__ == "__main__":
    build_complete_guide_pdf()
