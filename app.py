from flask import Flask, request, jsonify, render_template
import random
import os

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML file

if __name__ == '__main__':
    app.run(debug=True)
