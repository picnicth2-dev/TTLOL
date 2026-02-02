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
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="theme-color" content="#ff9acb">
<title>ถึงที่ร๊ากกของเค้า 💖</title>

<style>
    * {
        box-sizing: border-box;
        -webkit-tap-highlight-color: transparent;
    }

    body {
        background: radial-gradient(circle at top, #ffd6e8, #ff9acb);
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
        margin: 0;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        overflow: hidden;
    }

    h1 {
        font-size: clamp(2.5em, 8vw, 4em);
        color: #ff4d88;
        margin-bottom: 20px;
        text-shadow: 0 0 10px rgba(255,255,255,0.7);
    }

    #text {
        font-size: clamp(1.1em, 4.5vw, 1.6em);
        color: #7a1f4a;
        max-width: 95%;
        line-height: 1.7;
        white-space: pre-line;
        min-height: 200px;
    }

    button {
        margin-top: 25px;
        padding: 14px 36px;
        font-size: 1.1em;
        border: none;
        border-radius: 40px;
        background: #ff4d88;
        color: white;
        cursor: pointer;
        transition: transform 0.15s;
    }

    button:active {
        transform: scale(0.92);
    }

    .heart {
        position: absolute;
        font-size: 2em;
        animation: floatUp 2s ease-out forwards;
        pointer-events: none;
    }

    @keyframes floatUp {
        from {
            transform: translateY(0) scale(1);
            opacity: 1;
        }
        to {
            transform: translateY(-140px) scale(1.5);
            opacity: 0;
        }
    }

    .flower {
        position: absolute;
        font-size: 2.2em;
        animation: float 12s linear infinite;
        opacity: 0.85;
    }

    @keyframes float {
        from { transform: translateY(110vh) rotate(0deg); }
        to { transform: translateY(-10vh) rotate(360deg); }
    }

    .credit {
        position: fixed;
        bottom: 8px;
        width: 100%;
        text-align: center;
        font-size: 0.75em;
        color: rgba(122,31,74,0.6);
    }
</style>
</head>

<body>

<!-- ดอกไม้ -->
<div class="flower" style="left:5%; animation-delay:0s;">😘</div>
<div class="flower" style="left:25%; animation-delay:3s;">🌹</div>
<div class="flower" style="left:50%; animation-delay:1s;">💮</div>
<div class="flower" style="left:75%; animation-delay:2s;">💐</div>
<div class="flower" style="left:90%; animation-delay:4s;">🌸</div>

<h1> ถึงที่ร๊ากของเค้า </h1>
<div id="text"></div>

<button onclick="loveBack()">บอกรักกลับ 💕</button>

<div class="credit">Created by Kitthiphan Janthilar</div>

<audio id="typeSound" src="https://assets.mixkit.co/sfx/preview/mixkit-keyboard-typing-1386.mp3"></audio>

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
const sound = document.getElementById("typeSound");
sound.volume = 0.12;

function typeWriter() {
    if (line < message.length) {
        if (char < message[line].length) {
            textDiv.innerHTML += message[line].charAt(char);
            sound.currentTime = 0;
            sound.play();
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

function loveBack() {
    for (let i = 0; i < 10; i++) {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.innerHTML = "💖";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.bottom = "120px";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 2000);
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