from flask import Flask, request, jsonify
import random

app = Flask(__name__)  # Corrected __name__ here

# Simple responses for demonstration
responses = [
    "Hello! How can I assist you today?",
    "I'm here to help! What do you need?",
    "Hi there! Feel free to ask me anything.",
]

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # For now, return a random response
    return jsonify({"response": random.choice(responses)})

if __name__ == '__main__':  # Corrected __name__ here
    app.run(debug=True)
