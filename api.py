from flask import Flask, request, jsonify

app = Flask(__name__)

questions = [
    "What's your name?",
    "How are you feeling today?",
    "Let's talk about this year 2024.",
    "How was your year?",
    "What is the most amazing memory of this year of yours?",
    "What is the one learning you got from this year?",
    "What is the one thing you liked the most about yourself this year?",
    "Have you captured the best memories of your life with you? If yes, I can give a suggestion to you.",
    "If you get a chance to write a book regarding the philosophy of living life, what would be the title?",
    "Do you pay gratitude to the higher for all the opportunities in your life?",
    "What one advice do you want to give yourself to be happier in life?"
]

responses = {}
current_question_index = 0
suggestion = (
    "Please convert them to physical copies; otherwise, you might lose them due to storage issues."
)

@app.route("/chat", methods=["POST"])
def chat():
    global current_question_index
    user_response = request.json.get("response", "").strip()

    if not user_response:
        return jsonify({"error": "Response cannot be empty!"}), 400

    if current_question_index < len(questions):
        question = questions[current_question_index]
        responses[question] = user_response
        current_question_index += 1

        if current_question_index == 7:  # Add suggestion
            responses["Suggestion"] = suggestion

        if current_question_index < len(questions):
            return jsonify({"question": questions[current_question_index]})

        else:
            name = responses.get(questions[0], "Friend")
            return jsonify(
                {
                    "message": f"Thank you for your responses, {name}! I appreciate your thoughtful answers and wish you the best for the future.",
                    "responses": responses,
                }
            )

    return jsonify({"error": "No more questions available."}), 400

if __name__ == "__main__":
    app.run(debug=True)
