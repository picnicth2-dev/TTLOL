from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>ถึงที่ร๊ากกของเค้า 💖</title>
    <style>
        body {
            background: radial-gradient(circle at top, #ffd6e8, #ff9acb);
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }

        h1 {
            font-size: 4em;
            color: #ff4d88;
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(255,255,255,0.7);
        }

        #text {
            font-size: 1.6em;
            color: #7a1f4a;
            max-width: 80%;
            line-height: 1.6;
            white-space: pre-line;
        }

        /* ดอกไม้ลอย */
        .flower {
            position: absolute;
            font-size: 2.5em;
            animation: float 10s linear infinite;
            opacity: 0.8;
        }

        @keyframes float {
            from {
                transform: translateY(100vh) rotate(0deg);
            }
            to {
                transform: translateY(-10vh) rotate(360deg);
            }
        }
    </style>
</head>
<body>

    <!-- ดอกไม้ -->
    <div class="flower" style="left:10%; animation-delay:0s;">😘</div>
    <div class="flower" style="left:30%; animation-delay:2s;">😍</div>
    <div class="flower" style="left:50%; animation-delay:4s;">🌺</div>
    <div class="flower" style="left:70%; animation-delay:1s;">💐</div>
    <div class="flower" style="left:90%; animation-delay:3s;">🌸</div>

    <h1>💖 ถึงที่ร๊ากของเค้า 💖</h1>
    <div id="text"></div>

<script>
    const message = [
        "สวัสดีตอนเช้านะค้าบที่รัก 💕",
        "",
        "จำได้ไหมวันนี้วันอะไรเอ่ย…",
        "วันครบรอบของเราไงค้าบ",
        "วันที่ 24 กุมภาพันธ์ ครบรอบ1M 🌸",
        "",
        "ขอบคุณที่อยู่ข้างกันเสมอ",
        "อยู่ด้วยกันไปนานๆ นะจุ๊บมั่ววว 💖"
    ];

    let line = 0;
    let char = 0;
    const speed = 50;
    const textDiv = document.getElementById("text");

    function typeWriter() {
        if (line < message.length) {
            if (char < message[line].length) {
                textDiv.innerHTML += message[line].charAt(char);
                char++;
                setTimeout(typeWriter, speed);
            } else {
                textDiv.innerHTML += "<br>";
                line++;
                char = 0;
                setTimeout(typeWriter, 500);
            }
        }
    }

    typeWriter();
</script>

</body>
</html>
"""
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)