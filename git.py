from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI API is LIVE 🚀"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    msg = data.get("message", "")

    return jsonify({
        "reply": f"You said: {msg}"
    })

if __name__ == "__main__":
    app.run()