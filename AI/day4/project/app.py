from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message")
    if not message:
        return jsonify({"error": "Missing message"}), 400
    if not API_KEY:
        return jsonify({"error": "Missing GEMINI_API_KEY"}), 500

    try:
        model = genai.GenerativeModel(model_name="gemini-flash-latest")
        response = model.generate_content(message)

        if hasattr(response, "text"):
            answer = response.text
        elif getattr(response, "output", None):
            answer = response.output[0].content if response.output else str(response)
        elif getattr(response, "candidates", None):
            answer = response.candidates[0].content
        else:
            answer = str(response)

        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)