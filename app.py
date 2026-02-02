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
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ถึงที่ร๊ากกของเค้า 💌</title>

<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: radial-gradient(circle at top, #ffd6e8, #ff9acb);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    overflow: hidden;
    text-align: center;
}

.hidden { display: none; }

button {
    padding: 14px 36px;
    margin: 10px;
    font-size: 1.1em;
    border: none;
    border-radius: 40px;
    background: #ff4d88;
    color: white;
    cursor: pointer;
}

button:active { transform: scale(0.92); }

/* ---------- ซองจดหมาย ---------- */
#envelope {
    font-size: 6em;
    cursor: pointer;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

#plead {
    font-size: 2.5em;
    margin: 15px 0;
}

/* ---------- Loading ---------- */
#loading {
    font-size: 2em;
    animation: pulse 1.2s infinite;
}

@keyframes pulse {
    0% { opacity: 0.3; }
    50% { opacity: 1; }
    100% { opacity: 0.3; }
}

/* ---------- หน้าเว็บหลัก ---------- */
.credit {
    position: fixed;
    bottom: 8px;
    width: 100%;
    font-size: 0.75em;
    color: rgba(122,31,74,0.6);
}
</style>
</head>

<body>

<!-- หน้า ซอง -->
<div id="cover">
    <div id="envelope">💌</div>
    <div id="plead"></div>
    <div id="buttons">
        <button onclick="openLetter()">เปิด 💖</button>
        <button onclick="notYet()">ยังไม่เปิด 🙈</button>
    </div>
</div>

<!-- Loading -->
<div id="loading" class="hidden">กำลังเปิดจดหมาย… 💕</div>

<!-- หน้าเว็บจริง -->
<div id="content" class="hidden">
    <h1>💖 ถึงที่ร๊ากของเค้า 💖</h1>
    <div id="text"></div>
    <button onclick="loveBack()">บอกรักกลับ 💕</button>
    <div class="credit">Created by Kitthiphan Janthilar</div>
</div>

<audio id="typeSound" src="https://assets.mixkit.co/sfx/preview/mixkit-keyboard-typing-1386.mp3"></audio>

<script>
let refuseCount = 0;

const pleadEmojis = [
    "🥺👉👈",
    "😖💗 เปิดเถอะน้าา",
    "😭💞 เค้าขอละ"
];

function notYet() {
    refuseCount++;
    const plead = document.getElementById("plead");
    plead.innerHTML = pleadEmojis[Math.min(refuseCount-1, pleadEmojis.length-1)];

    if (refuseCount >= 2) {
        document.getElementById("buttons").innerHTML =
            '<button onclick="openLetter()">เปิด 💖</button>';
    }
}

function openLetter() {
    document.getElementById("cover").classList.add("hidden");
    document.getElementById("loading").classList.remove("hidden");

    setTimeout(() => {
        document.getElementById("loading").classList.add("hidden");
        document.getElementById("content").classList.remove("hidden");
        typeWriter();
    }, 2500);
}

/* ---------- Typewriter ---------- */
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

let line = 0, char = 0;
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
            setTimeout(typeWriter, 400);
        }
    }
}

function loveBack() {
    for (let i = 0; i < 8; i++) {
        const heart = document.createElement("div");
        heart.innerHTML = "💖";
        heart.style.position = "absolute";
        heart.style.left = Math.random()*100 + "vw";
        heart.style.bottom = "100px";
        heart.style.fontSize = "2em";
        heart.style.animation = "floatUp 2s ease-out forwards";
        document.body.appendChild(heart);
        setTimeout(()=>heart.remove(),2000);
    }
}
</script>

<style>
@keyframes floatUp {
    from { transform: translateY(0); opacity: 1; }
    to { transform: translateY(-140px); opacity: 0; }
}
</style>

</body>
</html>
"""
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)