from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <body style="background:#1a1a1a; color:red; text-align:center; padding-top:100px; font-family:sans-serif;">
        <h1>อ่านทำไม? เข้ามาทำไม?</h1>
        <p style="color:white;">ว่างมากเหรอปิคนิค? ไปหาอะไรทำไป๊! 🤨</p>
    </body>
    """

if __name__ == "__main__":
    # Render ต้องการให้ใช้ Port จาก Environment Variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
