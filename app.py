from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# 从环境变量读取 API Key（推荐做法）
API_KEY = os.getenv("API_KEY", "替换成你的API_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    # 调用 OpenAI API（可以换成其他 AI 平台的接口）
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_msg}]
    }
    resp = requests.post(url, headers=headers, json=data)
    reply = resp.json()["choices"][0]["message"]["content"]

    return jsonify({"reply": reply})


if __name__ == "__main__":
    # Render 要求监听 0.0.0.0:10000 或 PORT 环境变量
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
