from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI API is LIVE!"

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return "Use POST to send message"

    data = request.json
    msg = data.get("message", "")

    return jsonify({
        "reply": f"You said: {msg}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)