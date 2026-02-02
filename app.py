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
    <title>ถึงคนพิเศษของฉัน 💖</title>
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

        /* ดอกไม้ลอย */
        .flower {
            position: absolute;
            font-size: 2.5em;
            animation: float 10s linear infinite;
            opacity: 0.8;
        }

        h1 {
            font-size: 4em;
            color: #ff4d88;
            margin: 0;
            text-shadow: 0 0 10px rgba(255,255,255,0.7);
            animation: heartbeat 1.5s infinite;
        }

        p {
            font-size: 1.6em;
            color: #7a1f4a;
            margin-top: 20px;
        }

        .love {
            margin-top: 30px;
            font-size: 1.3em;
            color: #a1004f;
        }

        @keyframes heartbeat {
            0% { transform: scale(1); }
            25% { transform: scale(1.05); }
            50% { transform: scale(1); }
            75% { transform: scale(1.05); }
            100% { transform: scale(1); }
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
    <div class="flower" style="left:10%; animation-delay:0s;">🌸</div>
    <div class="flower" style="left:30%; animation-delay:2s;">🌷</div>
    <div class="flower" style="left:50%; animation-delay:4s;">🌺</div>
    <div class="flower" style="left:70%; animation-delay:1s;">💐</div>
    <div class="flower" style="left:90%; animation-delay:3s;">🌸</div>

    <h1>รักนะ 💖</h1>
    <p>ขอบคุณที่เข้ามาเป็นรอยยิ้มของเรา</p>
    <div class="love">
        อยู่ด้วยกันไปนานๆ นะ 🌷<br>
        เราดีใจมากที่มีเธออยู่ตรงนี้ 💕
    </div>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)