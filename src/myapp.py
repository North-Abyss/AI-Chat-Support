import webbrowser
import threading
from flask import Flask, request, jsonify, render_template
import ollama  

app = Flask(__name__)

def ask_ollama(prompt, model="tinyllama:1.1b"):
    formatted_prompt = (
        "Respond like a helpful customer support agent. Keep it short, friendly, and to the point. Avoid unnecessary details or stories. Example:\n"
        "User: My internet is slow.\n"
        "AI: I understand! Try restarting your router and checking for any large downloads. Let me know if that helps!\n\n"
        "Now, respond to this:\n" + prompt
    )
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": formatted_prompt}])
        return response.get("message", {}).get("content", "I'm here to help!")
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"error": "Message is empty"}), 400
        return jsonify({"response": ask_ollama(user_message)})
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

@app.route("/")
def home():
    return render_template("index.html")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(host="0.0.0.0", port=5000)

