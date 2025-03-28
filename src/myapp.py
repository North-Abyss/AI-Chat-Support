import os
from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__)

# Function to query Ollama
def ask_ollama(prompt, model="tinyllama:1.1b"):
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

# Multi-Agent AI System
def customer_support(query):
    agents = {}

    # Summarizer Agent
    summary_prompt = f"""
    You are an AI support assistant. A customer reported the following issue: '{query}'. 
    Explain in simple terms what the problem is, as if speaking to someone with no technical knowledge.
    """
    agents["Summary"] = ask_ollama(summary_prompt)

    # Router Agent
    route_prompt = f"""
    Based on this issue: '{agents['Summary']}', determine which team should handle it and explain why.
    """
    agents["Department"] = ask_ollama(route_prompt)

    # Resolver Agent
    resolve_prompt = f"""
    Given this issue: '{agents['Summary']}', suggest a step-by-step solution in easy terms.
    """
    agents["Suggested Resolution"] = ask_ollama(resolve_prompt)

    # Estimator Agent
    estimate_prompt = f"""
    Estimate how long this issue might take to resolve: '{agents['Summary']}'. 
    Explain in a way a non-technical person can understand.
    """
    agents["Estimated Resolution Time"] = ask_ollama(estimate_prompt)

    return agents

# Home Route (UI)
@app.route("/")
def home():
    return render_template("index.html")

# API Route for AI Query Processing
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")
    
    if not query:
        return jsonify({"error": "No query provided"}), 400

    response = customer_support(query)
    return jsonify(response)

# Run Flask App
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
