#!/usr/bin/env python3
"""
GGPRAO AI Chat - Alternative Flask Web UI (No Streamlit/PyArrow)
Use this if Streamlit fails due to PyArrow DLL blocking

Run with: python app_flask_alternative.py
"""

import json
import os
from flask import Flask, render_template_string, request, jsonify
from datetime import datetime

# Try to import ollama, but continue if not available
try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False
    print("⚠️  Warning: Ollama not available. Chat will be in demo mode.")

app = Flask(__name__)

# In-memory chat history
chat_history = []

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GGPRAO AI Chat</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .container {
            width: 90%;
            max-width: 900px;
            height: 90vh;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
            border-bottom: 4px solid #764ba2;
        }

        .header h1 {
            font-size: 28px;
            margin-bottom: 5px;
        }

        .header p {
            font-size: 14px;
            opacity: 0.9;
        }

        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: #f8f9fa;
        }

        .message {
            margin-bottom: 15px;
            display: flex;
            animation: slideIn 0.3s ease;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .message.user {
            justify-content: flex-end;
        }

        .message-content {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 12px;
            word-wrap: break-word;
            line-height: 1.4;
        }

        .message.user .message-content {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-bottom-right-radius: 4px;
        }

        .message.assistant .message-content {
            background: #e9ecef;
            color: #333;
            border-bottom-left-radius: 4px;
        }

        .message-time {
            font-size: 12px;
            color: #999;
            margin-top: 5px;
        }

        .input-area {
            padding: 20px;
            border-top: 1px solid #ddd;
            background: white;
            display: flex;
            gap: 10px;
        }

        input[type="text"] {
            flex: 1;
            padding: 12px 16px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 14px;
            transition: border-color 0.3s;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: #667eea;
        }

        button {
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
        }

        button:active {
            transform: translateY(0);
        }

        .loading {
            text-align: center;
            color: #999;
            font-style: italic;
        }

        .status {
            text-align: center;
            padding: 10px;
            background: #fff3cd;
            color: #856404;
            font-size: 12px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 GGPRAO AI Chat</h1>
            <p>PyArrow-Free Alternative Web Interface</p>
        </div>

        {% if not ollama_available %}
        <div style="padding: 10px 20px; background: #fff3cd; color: #856404; font-size: 12px;">
            ⚠️ Ollama is not available. Chat is in demo mode (simulated responses).
        </div>
        {% endif %}

        <div class="chat-container" id="chatContainer">
            <div class="message assistant">
                <div>
                    <div class="message-content">
                        👋 Hello! I'm your AI assistant. How can I help you today?
                    </div>
                    <div class="message-time">{{ current_time }}</div>
                </div>
            </div>
        </div>

        <div class="input-area">
            <input 
                type="text" 
                id="messageInput" 
                placeholder="Type your message here..." 
                autocomplete="off"
            />
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        const chatContainer = document.getElementById('chatContainer');
        const messageInput = document.getElementById('messageInput');

        function formatTime(date) {
            return date.toLocaleTimeString('en-US', {
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            });
        }

        function sendMessage() {
            const message = messageInput.value.trim();
            if (!message) return;

            // Add user message to chat
            addMessageToChat(message, 'user');
            messageInput.value = '';

            // Add loading indicator
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'message assistant';
            loadingDiv.innerHTML = '<div class="message-content loading">⏳ Thinking...</div>';
            chatContainer.appendChild(loadingDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;

            // Send to server
            fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({message: message})
            })
            .then(response => response.json())
            .then(data => {
                loadingDiv.remove();
                addMessageToChat(data.response, 'assistant');
            })
            .catch(error => {
                loadingDiv.remove();
                addMessageToChat('Sorry, an error occurred: ' + error.message, 'assistant');
            });
        }

        function addMessageToChat(text, role) {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message ' + role;
            
            const time = new Date();
            messageDiv.innerHTML = `
                <div>
                    <div class="message-content">${escapeHtml(text)}</div>
                    <div class="message-time">${formatTime(time)}</div>
                </div>
            `;
            
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        function escapeHtml(text) {
            const map = {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#039;'
            };
            return text.replace(/[&<>"']/g, m => map[m]);
        }

        // Allow sending with Enter key
        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        // Focus on input
        messageInput.focus();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(
        HTML_TEMPLATE,
        current_time=datetime.now().strftime('%H:%M:%S'),
        ollama_available=OLLAMA_AVAILABLE
    )

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({'response': 'Please enter a message.'}), 400

    try:
        if OLLAMA_AVAILABLE:
            # Use Ollama for real AI responses
            try:
                response = ollama.chat(model='neural-chat', messages=[
                    {'role': 'user', 'content': user_message}
                ])
                ai_response = response.get('message', {}).get('content', 'No response received.')
            except Exception as e:
                ai_response = f"Ollama error: {str(e)}\n\nTrying demo mode..."
                # Fall back to demo mode
                ai_response = get_demo_response(user_message)
        else:
            # Demo mode with simulated responses
            ai_response = get_demo_response(user_message)

        # Store in history
        chat_history.append({
            'user': user_message,
            'assistant': ai_response,
            'timestamp': datetime.now().isoformat()
        })

        return jsonify({'response': ai_response})

    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'}), 500

def get_demo_response(message):
    """Generate demo responses"""
    demos = {
        'hello': "Hello! I'm a demo AI. In production, I would connect to Ollama for real AI responses.",
        'help': "I'm a demo AI assistant. You can ask me questions, but for real AI responses, please ensure Ollama is running.",
        'how are you': "I'm doing well, thank you for asking! I'm a demo AI ready to help.",
    }

    message_lower = message.lower()

    for key, value in demos.items():
        if key in message_lower:
            return value

    return f"Thank you for your message: '{message}'. In production mode with Ollama, I would provide intelligent responses."

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'OK',
        'ollama_available': OLLAMA_AVAILABLE,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("=" * 70)
    print("🚀 GGPRAO AI Chat - Flask Web Interface")
    print("=" * 70)
    print(f"\n✅ Ollama Status: {'Available' if OLLAMA_AVAILABLE else 'Not Available (Demo Mode)'}")
    print("\n🌐 Opening in browser: http://localhost:5000")
    print("\n💡 To stop the server, press Ctrl+C")
    print("\n" + "=" * 70 + "\n")

    app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)

