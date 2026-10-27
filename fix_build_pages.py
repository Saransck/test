def fix():
    with open(r"D:\vhdl\build_pages.py", "r", encoding="utf-8") as f:
        content = f.read()

    old_target = """    <script>
        document.addEventListener("DOMContentLoaded", () => {{
            hljs.highlightAll();
        }});
    </script>
</body>
</html>
\"\"\"
    with open(r"d:\\vhdl\\complete_guide_body.html", "r", encoding="utf-8") as bf:
        rendered_body = bf.read()

    html = html.replace('<div id="content" class="markdown-body">กำลังโหลดคู่มือ...</div>', '<div id="content" class="markdown-body">\\n' + rendered_body + '\\n</div>')

    with open(r"d:\\vhdl\\guide.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("guide.html created successfully with pre-rendered Complete_Study_Guide_Lec_and_Lab HTML.")"""

    new_repl = """    <script>
        const rawMarkdown = {md_json};

        document.addEventListener("DOMContentLoaded", () => {{
            marked.setOptions({{
                highlight: function(code, lang) {{
                    const language = hljs.getLanguage(lang) ? lang : 'plaintext';
                    return hljs.highlight(code, {{ language }}).value;
                }},
                gfm: true,
                breaks: true
            }});

            const html = marked.parse(rawMarkdown);
            document.getElementById('content').innerHTML = html;
            hljs.highlightAll();
        }});
    </script>
</body>
</html>
\"\"\"
    with open(r"d:\\vhdl\\guide.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("guide.html created successfully with Complete_Study_Guide_Lec_and_Lab.md content.")"""

    content = content.replace(old_target, new_repl)
    with open(r"D:\vhdl\build_pages.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed build_pages.py successfully!")

if __name__ == "__main__":
    fix()
