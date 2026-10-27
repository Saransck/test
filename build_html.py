import json

def build_standalone_html():
    with open(r"D:\vhdl\exam_questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    json_str = json.dumps(questions, ensure_ascii=False)

    c_count = sum(1 for q in questions if q['type'] == 'choice')
    cf_count = sum(1 for q in questions if q['type'] == 'code_fill')
    tf_count = sum(1 for q in questions if q['type'] == 'tf')

    lec_count = sum(1 for q in questions if q.get('origin') == 'lec')
    lab_count = sum(1 for q in questions if q.get('origin') == 'lab')
    both_count = sum(1 for q in questions if q.get('origin') == 'both')

    html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ระบบจำลองสอบ Digital Circuit Design with Verilog HDL (Week 2 - 8)</title>
    <style>
        :root {{
            --primary: #004085;
            --primary-light: #e8f0fe;
            --secondary: #17a2b8;
            --success: #28a745;
            --danger: #dc3545;
            --dark: #212529;
            --light: #f8f9fa;
            --border: #ced4da;
            --card-bg: #ffffff;
            --code-bg: #f8f9fa;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        body {{
            background-color: #f4f6f9;
            color: var(--dark);
            line-height: 1.6;
            padding: 20px;
        }}
        .container {{
            max-width: 960px;
            margin: 0 auto;
        }}
        header {{
            background: linear-gradient(135deg, var(--primary), #002752);
            color: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 25px;
            text-align: center;
        }}
        header h1 {{
            font-size: 22px;
            margin-bottom: 8px;
        }}
        header p {{
            font-size: 14px;
            opacity: 0.9;
        }}
        .filter-section {{
            background: white;
            padding: 16px 20px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }}
        .filter-label {{
            font-size: 13px;
            font-weight: bold;
            color: #495057;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .nav-tabs {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 12px;
        }}
        .nav-btn {{
            background: var(--light);
            border: 1.5px solid var(--border);
            padding: 7px 14px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            transition: all 0.2s ease;
        }}
        .nav-btn:hover {{
            background: var(--primary-light);
            border-color: var(--primary);
            color: var(--primary);
        }}
        .nav-btn.active {{
            background: var(--primary);
            border-color: var(--primary);
            color: white;
        }}
        .nav-btn.origin-btn.active {{
            background: #6f42c1;
            border-color: #6f42c1;
            color: white;
        }}
        .nav-btn.type-btn.active {{
            background: #20c997;
            border-color: #20c997;
            color: white;
        }}
        .score-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: white;
            padding: 14px 20px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            margin-bottom: 12px;
            font-weight: bold;
        }}
        .progress-container {{
            width: 100%;
            background-color: #e9ecef;
            border-radius: 6px;
            height: 10px;
            margin-bottom: 20px;
            overflow: hidden;
        }}
        .progress-bar {{
            height: 100%;
            background-color: var(--success);
            width: 0%;
            transition: width 0.3s ease;
        }}
        .question-card {{
            background: var(--card-bg);
            border-radius: 10px;
            padding: 22px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            border-left: 5px solid var(--primary);
        }}
        .question-card.code_fill {{
            border-left-color: #e83e8c;
        }}
        .question-card.tf {{
            border-left-color: #fd7e14;
        }}
        .q-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }}
        .badge-group {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .badge {{
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }}
        .badge-week {{
            background: var(--primary-light);
            color: var(--primary);
        }}
        .badge-origin {{
            font-weight: bold;
        }}
        .badge-origin.lec {{
            background: #e8eaf6;
            color: #283593;
            border: 1px solid #c5cae9;
        }}
        .badge-origin.lab {{
            background: #e0f2f1;
            color: #004d40;
            border: 1px solid #b2dfdb;
        }}
        .badge-origin.both {{
            background: #ede7f6;
            color: #4a148c;
            border: 1px solid #d1c4e9;
        }}
        .badge-type {{
            background: #e3f2fd;
            color: #0d47a1;
        }}
        .badge-type.code_fill {{
            background: #fce4ec;
            color: #c2185b;
        }}
        .badge-type.tf {{
            background: #fff3e0;
            color: #e65100;
        }}
        .q-title {{
            font-size: 15.5px;
            font-weight: 600;
            margin-bottom: 15px;
            color: #111;
        }}
        .code-box {{
            background: #282c34;
            color: #abb2bf;
            padding: 12px 16px;
            border-radius: 8px;
            font-family: Consolas, 'Courier New', monospace;
            font-size: 13.5px;
            line-height: 1.5;
            margin: 12px 0 16px 0;
            overflow-x: auto;
            border-left: 4px solid #61afef;
        }}
        .options-list {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 15px;
        }}
        .option-btn {{
            background: white;
            border: 1.5px solid var(--border);
            padding: 12px 16px;
            border-radius: 8px;
            cursor: pointer;
            text-align: left;
            font-size: 14px;
            transition: all 0.2s;
            display: flex;
            align-items: flex-start;
            gap: 10px;
            color: #212529;
        }}
        .option-btn:hover:not(:disabled) {{
            background: var(--primary-light);
            border-color: var(--primary);
        }}
        .option-btn.correct {{
            background: #d4edda !important;
            border-color: var(--success) !important;
            color: #155724 !important;
            font-weight: 600;
        }}
        .option-btn.incorrect {{
            background: #f8d7da !important;
            border-color: var(--danger) !important;
            color: #721c24 !important;
        }}
        .opt-label {{
            font-weight: bold;
            min-width: 24px;
        }}
        .explanation-card {{
            display: none;
            background: #f8f9fa;
            border-radius: 8px;
            padding: 15px;
            margin-top: 15px;
            border: 1px solid #e2e6ea;
            font-size: 13.5px;
        }}
        .explanation-card.show {{
            display: block;
            animation: fadeIn 0.3s ease;
        }}
        .source-tag {{
            display: inline-block;
            background: #e2e3e5;
            color: #383d41;
            padding: 5px 12px;
            border-radius: 4px;
            font-size: 12px;
            margin-top: 10px;
            font-weight: bold;
            border-left: 3px solid var(--primary);
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-5px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>ระบบจำลองสอบ Digital Circuit Design with Verilog HDL</h1>
            <p>ระบุแหล่งที่มาชัดเจนว่ามาจาก LECTURE (สไลด์บรรยาย) หรือ LAB (ใบงานปฏิบัติการ) 100%</p>
        </header>

        <div class="filter-section">
            <div class="filter-label">🏛️ กรองตามแหล่งที่มา (Origin: Lec / Lab):</div>
            <div class="nav-tabs" id="originTabs">
                <button class="nav-btn origin-btn active" id="btn_orig_all" onclick="filterByOrigin('all')">ทั้งหมด ({len(questions)} ข้อ)</button>
                <button class="nav-btn origin-btn" id="btn_orig_lec" onclick="filterByOrigin('lec')">📚 มาจาก LECTURE เท่านั้น [{lec_count} ข้อ]</button>
                <button class="nav-btn origin-btn" id="btn_orig_lab" onclick="filterByOrigin('lab')">🧪 มาจาก LAB เท่านั้น [{lab_count} ข้อ]</button>
                <button class="nav-btn origin-btn" id="btn_orig_both" onclick="filterByOrigin('both')">📘 มาจากทั้ง LECTURE & LAB [{both_count} ข้อ]</button>
            </div>

            <div class="filter-label" style="margin-top: 10px;">📌 กรองตามรูปแบบข้อสอบ (Question Types):</div>
            <div class="nav-tabs" id="typeTabs">
                <button class="nav-btn type-btn active" id="btn_type_all" onclick="filterByType('all')">ทุกรูปแบบ</button>
                <button class="nav-btn type-btn" id="btn_type_choice" onclick="filterByType('choice')">🔤 ปรนัย (A B C D) [{c_count}]</button>
                <button class="nav-btn type-btn" id="btn_type_code" onclick="filterByType('code_fill')">💻 เติมโค้ด (A B C D) [{cf_count}]</button>
                <button class="nav-btn type-btn" id="btn_type_tf" onclick="filterByType('tf')">⚖️ ถูก / ผิด [{tf_count}]</button>
            </div>

            <div class="filter-label" style="margin-top: 10px;">📅 หรือกรองตามสัปดาห์ (Weeks 2 - 8):</div>
            <div class="nav-tabs" id="weekTabs">
                <button class="nav-btn" id="btn_w_all" onclick="filterByWeek('all')">ทุกสัปดาห์</button>
                <button class="nav-btn" id="btn_w2" onclick="filterByWeek(2)">Week 2</button>
                <button class="nav-btn" id="btn_w3" onclick="filterByWeek(3)">Week 3</button>
                <button class="nav-btn" id="btn_w4" onclick="filterByWeek(4)">Week 4</button>
                <button class="nav-btn" id="btn_w5" onclick="filterByWeek(5)">Week 5</button>
                <button class="nav-btn" id="btn_w6" onclick="filterByWeek(6)">Week 6</button>
                <button class="nav-btn" id="btn_w7" onclick="filterByWeek(7)">Week 7</button>
                <button class="nav-btn" id="btn_w8" onclick="filterByWeek(8)">Week 8</button>
                <button class="nav-btn" id="btn_mock" onclick="startMockExam()" style="background: #28a745; color: white; border-color: #28a745; margin-left: auto;">🎯 สุ่มสอบ 20 ข้อ (Mock Exam)</button>
            </div>
        </div>

        <div class="score-bar">
            <div>คะแนนสะสม: <span id="scoreText">0 / 0</span> (<span id="scorePercent">0%</span>)</div>
            <button onclick="resetQuiz()" style="padding: 6px 14px; font-size: 13px; cursor: pointer; border-radius: 4px; border: 1px solid var(--border); background: white; font-weight: bold;">🔄 ทำรอบนี้ใหม่</button>
        </div>
        <div class="progress-container">
            <div class="progress-bar" id="progressBar"></div>
        </div>

        <div id="questionsContainer"></div>
    </div>

    <script>
        // Embedded Questions Database
        const allQuestions = {json_str};

        let currentQuestions = [];
        let answeredCount = 0;
        let scoreCount = 0;
        let currentFilterOrigin = 'all';
        let currentFilterType = 'all';
        let currentFilterWeek = 'all';

        function applyFilters() {{
            let res = [...allQuestions];
            if (currentFilterOrigin !== 'all') {{
                res = res.filter(q => q.origin === currentFilterOrigin);
            }}
            if (currentFilterType !== 'all') {{
                res = res.filter(q => q.type === currentFilterType);
            }}
            if (currentFilterWeek !== 'all') {{
                res = res.filter(q => q.week === currentFilterWeek);
            }}
            currentQuestions = res;
            renderQuestions();
        }}

        function filterByOrigin(originKey) {{
            currentFilterOrigin = originKey;
            document.querySelectorAll('.origin-btn').forEach(b => b.classList.remove('active'));
            const btn = document.getElementById('btn_orig_' + originKey);
            if (btn) btn.classList.add('active');
            applyFilters();
        }}

        function filterByType(typeKey) {{
            currentFilterType = typeKey;
            document.querySelectorAll('.type-btn').forEach(b => b.classList.remove('active'));
            const btn = document.getElementById('btn_type_' + (typeKey === 'code_fill' ? 'code' : typeKey));
            if (btn) btn.classList.add('active');
            applyFilters();
        }}

        function filterByWeek(weekKey) {{
            currentFilterWeek = weekKey;
            document.querySelectorAll('#weekTabs .nav-btn').forEach(b => b.classList.remove('active'));
            const btn = document.getElementById(weekKey === 'all' ? 'btn_w_all' : 'btn_w' + weekKey);
            if (btn) btn.classList.add('active');
            applyFilters();
        }}

        function startMockExam() {{
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            const btn = document.getElementById('btn_mock');
            if (btn) btn.classList.add('active');
            
            // Randomly shuffle and take 20 questions
            let shuffled = [...allQuestions].sort(() => 0.5 - Math.random());
            currentQuestions = shuffled.slice(0, 20);
            renderQuestions();
        }}

        function formatQuestionContent(text) {{
            if (text.includes('```verilog') || text.includes('```')) {{
                return text.replace(/```(?:verilog)?([\\s\\S]*?)```/g, (match, p1) => {{
                    return '<div class="code-box">' + p1.trim().replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</div>';
                }}).replace(/\\n/g, '<br>');
            }}
            return text.replace(/\\n/g, '<br>');
        }}

        function renderQuestions() {{
            answeredCount = 0;
            scoreCount = 0;
            updateScore();

            const container = document.getElementById('questionsContainer');
            container.innerHTML = '';

            if (currentQuestions.length === 0) {{
                container.innerHTML = '<p style="text-align: center; color: #6c757d; padding: 40px; font-weight: bold;">ไม่พบข้อสอบในเงื่อนไขที่เลือก</p>';
                return;
            }}

            currentQuestions.forEach((q, idx) => {{
                const card = document.createElement('div');
                card.className = 'question-card ' + q.type;
                card.id = 'card_' + q.id;

                const labels = (q.type === 'choice' || q.type === 'code_fill') ? ['A', 'B', 'C', 'D'] : ['1', '2'];

                let typeLabel = '🔤 ปรนัย (A B C D)';
                if (q.type === 'code_fill') typeLabel = '💻 เติมโค้ด Verilog (A B C D)';
                if (q.type === 'tf') typeLabel = '⚖️ ถูก / ผิด';

                let originLabel = '📚 มาจาก: LECTURE';
                let originClass = 'lec';
                if (q.origin === 'lab') {{
                    originLabel = '🧪 มาจาก: LAB';
                    originClass = 'lab';
                }} else if (q.origin === 'both') {{
                    originLabel = '📘 มาจาก: LECTURE & LAB';
                    originClass = 'both';
                }}

                let optionsHtml = '';
                q.options.forEach((opt, optIdx) => {{
                    optionsHtml += `
                        <button class="option-btn" onclick="selectAnswer('${{q.id}}', ${{optIdx}}, ${{q.answer_index}})">
                            <span class="opt-label">[${{labels[optIdx]}}]</span>
                            <span>${{opt}}</span>
                        </button>
                    `;
                }});

                card.innerHTML = `
                    <div class="q-header">
                        <div class="badge-group">
                            <span class="badge badge-week">Week ${{q.week}} • ${{q.topic}}</span>
                            <span class="badge badge-origin ${{originClass}}">${{originLabel}}</span>
                            <span class="badge badge-type ${{q.type}}">${{typeLabel}}</span>
                        </div>
                        <span style="font-size: 13px; color: #6c757d; font-weight: bold;">ข้อที่ ${{idx + 1}} จาก ${{currentQuestions.length}}</span>
                    </div>
                    <div class="q-title">${{formatQuestionContent(q.question)}}</div>
                    <div class="options-list" id="opts_${{q.id}}">
                        ${{optionsHtml}}
                    </div>
                    <div class="explanation-card" id="exp_${{q.id}}">
                        <div id="result_badge_${{q.id}}"></div>
                        <div style="margin-top: 8px; line-height: 1.6;"><strong>💡 คำอธิบายเชิงเทคนิค:</strong> ${{q.explanation}}</div>
                        <div class="source-tag">📌 แหล่งอ้างอิง: [${{q.origin_th}}]<br>รายละเอียด: ${{q.source}}</div>
                    </div>
                `;
                container.appendChild(card);
            }});
        }}

        function selectAnswer(qid, chosenIdx, correctIdx) {{
            const optContainer = document.getElementById('opts_' + qid);
            const buttons = optContainer.querySelectorAll('.option-btn');
            
            // Disable all buttons in this question card
            buttons.forEach(btn => btn.disabled = true);

            const isCorrect = (chosenIdx === correctIdx);
            buttons[chosenIdx].classList.add(isCorrect ? 'correct' : 'incorrect');
            if (!isCorrect) {{
                buttons[correctIdx].classList.add('correct');
            }}

            answeredCount++;
            if (isCorrect) scoreCount++;
            updateScore();

            // Show explanation
            const expCard = document.getElementById('exp_' + qid);
            const resultBadge = document.getElementById('result_badge_' + qid);
            resultBadge.innerHTML = isCorrect ? 
                '<span style="color: var(--success); font-weight: bold; font-size: 15px;">✓ ถูกต้อง! (CORRECT)</span>' : 
                '<span style="color: var(--danger); font-weight: bold; font-size: 15px;">✗ ไม่ถูกต้อง! (INCORRECT)</span>';
            expCard.classList.add('show');
        }}

        function updateScore() {{
            document.getElementById('scoreText').innerText = `${{scoreCount}} / ${{answeredCount}}`;
            const pct = answeredCount > 0 ? ((scoreCount / answeredCount) * 100).toFixed(0) : 0;
            document.getElementById('scorePercent').innerText = `${{pct}}%`;
            
            const prog = currentQuestions.length > 0 ? (answeredCount / currentQuestions.length) * 100 : 0;
            document.getElementById('progressBar').style.width = `${{prog}}%`;
        }}

        function resetQuiz() {{
            renderQuestions();
        }}

        // Run immediately when loaded
        window.addEventListener('DOMContentLoaded', () => {{
            currentQuestions = [...allQuestions];
            renderQuestions();
        }});
    </script>
</body>
</html>"""

    with open(r"D:\vhdl\exam_practice.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Successfully built D:\\vhdl\\exam_practice.html with Origin tags!")

if __name__ == "__main__":
    build_standalone_html()
