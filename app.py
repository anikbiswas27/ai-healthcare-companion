from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are an AI healthcare companion.

Rules:
- Do not act like a doctor.
- Give educational information only.
- Mention possible causes.
- Suggest basic home remedies.
- Recommend doctor consultation for severe symptoms.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.json

        user_message = data["message"]

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({
            "reply": reply
        })

    except Exception as e:

        return jsonify({
            "reply": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)