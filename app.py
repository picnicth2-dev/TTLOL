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

<!-- แก้ vh มือถือ -->
<script>
function fixVH() {
  document.documentElement.style.height = window.innerHeight + "px";
}
window.addEventListener("resize", fixVH);
window.addEventListener("orientationchange", fixVH);
fixVH();
</script>

<style>
/* กันเลื่อน + กันบัคมือถือ */
html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    overscroll-behavior: none;
    touch-action: none;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background: radial-gradient(circle at top, #ffd6e8, #ff9acb);
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}

/* ลายดอกไม้พื้นหลัง */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background: url("https://www.transparenttextures.com/patterns/flowers.png");
    opacity: 0.18;
    pointer-events: none;
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

/* ซอง */
#envelope {
    font-size: 6em;
    animation: bounce 2s infinite;
}
@keyframes bounce {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
#plead { font-size: 2.5em; }

/* Loading */
#loading {
    font-size: 2em;
    animation: pulse 1.2s infinite;
}
@keyframes pulse {
    0% { opacity: 0.3; }
    50% { opacity: 1; }
    100% { opacity: 0.3; }
}

/* กรอบจดหมาย */
.letter-box {
    background: repeating-linear-gradient(
        45deg,
        #ffe0ee,
        #ffe0ee 10px,
        #ffd0e6 10px,
        #ffd0e6 20px
    );
    border: 4px solid #ff6fa5;
    border-radius: 22px;
    padding: 26px 22px;
    max-width: 92%;
    width: 600px;
    box-shadow: 0 12px 35px rgba(255,77,136,0.3);
}

#text {
    font-size: 1.25em;
    color: #7a1f4a;
    line-height: 1.7;
    min-height: 220px;
}

/* ป้ายครบรอบ */
#banner {
    position: fixed;
    top: 18px;
    background: rgba(255,255,255,0.9);
    color: #ff4d88;
    padding: 10px 26px;
    border-radius: 30px;
    font-size: 1.05em;
    box-shadow: 0 6px 20px rgba(255,77,136,0.3);
    animation: slideDown 0.8s ease forwards;
}
@keyframes slideDown {
    from { transform: translateY(-40px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

/* หัวใจจาง */
.heart-soft {
    position: absolute;
    font-size: 1.6em;
    opacity: 0.4;
    animation: floatSoft 4s linear forwards;
}
@keyframes floatSoft {
    from { transform: translateY(0); opacity: 0.4; }
    to { transform: translateY(-180px); opacity: 0; }
}

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

<div id="cover">
    <div id="envelope">💌</div>
    <div id="plead"></div>
    <div id="buttons">
        <button onclick="openLetter()">เปิด 💖</button>
        <button onclick="notYet()">ยังไม่เปิด 🙈</button>
    </div>
</div>

<div id="loading" class="hidden">กำลังเปิดจดหมาย… 💕</div>

<div id="content" class="hidden">
    <h1>💖 ถึงที่ร๊ากกของเค้า 💖</h1>
    <div class="letter-box">
        <div id="text"></div>
    </div>
    <button onclick="loveBack()">บอกรักกลับ 💕</button>
    <div class="credit">Created by Kitthiphan Janthilar</div>
</div>

<audio id="typeSound" src="https://assets.mixkit.co/sfx/preview/mixkit-keyboard-typing-1386.mp3"></audio>
<audio id="squishSound" src="https://assets.mixkit.co/sfx/preview/mixkit-squeeze-toy-3034.mp3"></audio>

<script>
let refuseCount = 0;
const pleadEmojis = ["🥺👉👈","😖💗 เปิดเถอะน้าา","😭💞 เค้าง้อแล้ว"];

function notYet(){
    refuseCount++;
    plead.innerHTML = pleadEmojis[Math.min(refuseCount-1,2)];
    if(refuseCount>=2){
        buttons.innerHTML = '<button onclick="openLetter()">เปิด 💖</button>';
    }
}

function openLetter(){
    cover.classList.add("hidden");
    loading.classList.remove("hidden");
    setTimeout(()=>{
        loading.classList.add("hidden");
        content.classList.remove("hidden");
        typeWriter();
    },2500);
}

const message = [
 "สวัสดีตอนเช้านะค้าบที่รัก 💕","",
 "จำได้ไหมวันนี้วันอะไรเอ่ย…",
 "วันครบรอบของเราไงค้าบ",
 "วันที่ 24 กุมภาพันธ์ ครบรอบ1M 🌸","",
 "ขอบคุณที่อยู่ข้างกันเสมอ",
 "อยู่ด้วยกันไปนานๆ นะจุ๊บมั่ววว 💖"
];

let line=0,char=0;
const sound=document.getElementById("typeSound");
sound.volume=0.12;

function typeWriter(){
 if(line<message.length){
  if(char<message[line].length){
   text.innerHTML+=message[line].charAt(char++);
   sound.currentTime=0; sound.play();
   setTimeout(typeWriter,50);
  } else {
   text.innerHTML+="<br>";
   line++; char=0;
   setTimeout(typeWriter,400);
  }
 } else showBanner();
}

function showBanner(){
 if(document.getElementById("banner")) return;
 const b=document.createElement("div");
 b.id="banner";
 b.innerText="สุขสันต์วันครบรอบนะค้าบที่ร๊ากก 💖";
 document.body.appendChild(b);

 setInterval(()=>{
  const h=document.createElement("div");
  h.className="heart-soft";
  h.innerHTML=["🤍","💗","💖"][Math.floor(Math.random()*3)];
  h.style.left=(45+Math.random()*10)+"%";
  h.style.bottom="60px";
  document.body.appendChild(h);
  setTimeout(()=>h.remove(),4000);
 },900);
}

function loveBack(){
 const s=document.getElementById("squishSound");
 s.volume=0.15; s.currentTime=0; s.play();
 showBanner();
}
</script>

</body>
</html>
"""
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)