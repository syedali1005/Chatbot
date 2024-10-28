from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Simple responses for demonstration
responses = [
    "Hello! How can I assist you today?",
    "I'm here to help! What do you need?",
    "Hi there! Feel free to ask me anything.",
]

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML file

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # For now, return a random response
    return jsonify({"response": random.choice(responses)})

if __name__ == '__main__':
    app.run(debug=True)
