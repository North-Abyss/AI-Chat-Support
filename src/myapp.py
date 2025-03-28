import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Your Flask App is Running 🚀"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Get the PORT from Render
    app.run(debug=True, host="0.0.0.0", port=port)
