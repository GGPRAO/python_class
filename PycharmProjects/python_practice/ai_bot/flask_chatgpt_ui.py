from flask import Flask, render_template, request, jsonify
import ollama
from datetime import datetime
import json
import os

app = Flask(__name__, template_folder='.', static_folder='.')

# Store conversation history
conversation_history = []
MODEL_NAME = "qwen2:1.5b"

@app.route('/')
def index():
    return render_template('chatgpt_ui.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Empty message'}), 400

        # Add user message to history
        conversation_history.append({
            'role': 'user',
            'content': user_message
        })

        # Get response from Ollama
        response = ollama.chat(
            model=MODEL_NAME,
            messages=conversation_history
        )

        assistant_message = response['message']['content']

        # Add assistant response to history
        conversation_history.append({
            'role': 'assistant',
            'content': assistant_message
        })

        return jsonify({
            'success': True,
            'response': assistant_message
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/clear', methods=['POST'])
def clear_history():
    global conversation_history
    conversation_history = []
    return jsonify({'success': True})

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify(conversation_history)

if __name__ == '__main__':
    print("🚀 Starting Flask ChatGPT UI...")
    print("📱 Open http://localhost:5000 in your browser")
    app.run(debug=True, host='localhost', port=5000)

