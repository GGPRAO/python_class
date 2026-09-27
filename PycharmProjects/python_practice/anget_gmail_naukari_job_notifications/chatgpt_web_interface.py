#!/usr/bin/env python3
"""
ChatGPT-Like Web Interface for Email Assistant
Flask-based web UI that looks and feels like ChatGPT
"""

import sys
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, List, Any
import os

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, render_template_string, request, jsonify, session
import uuid

# Handle flask-cors import with auto-install fallback
try:
    from flask_cors import CORS
except ImportError:
    print("⚠️  flask-cors not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask-cors==4.0.0'])
    from flask_cors import CORS

try:
    from gmail import get_chatbot_adapter
except ImportError:
    print("❌ Gmail module not found.")
    sys.exit(1)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-' + str(uuid.uuid4()))
CORS(app)

# Global state
conversations = {}
adapters = {}


class ConversationManager:
    """Manage conversation state."""

    def __init__(self, conversation_id: str):
        """Initialize conversation."""
        self.id = conversation_id
        self.messages = []
        self.created_at = datetime.now()
        self._adapter = None  # Lazy initialization
        self.settings = {
            'search_depth': 15,
            'auto_summarize': True
        }

    @property
    def adapter(self):
        """Lazy-initialize the Gmail adapter on first use."""
        if self._adapter is None:
            self._adapter = get_chatbot_adapter()
        return self._adapter

    def add_message(self, role: str, content: str):
        """Add message to conversation."""
        self.messages.append({
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        })

    def get_messages(self):
        """Get all messages."""
        return self.messages

    def process_query(self, query: str) -> Dict[str, Any]:
        """Process user query."""
        try:
            result = self.adapter.search_jobs(query, limit=self.settings['search_depth'])

            if result['status'] == 'success':
                emails = result.get('emails', [])
                return {
                    'status': 'success',
                    'message': f"Found {len(emails)} matching email(s)",
                    'count': len(emails),
                    'results': emails[:10]  # Limit to 10 for web display
                }
            else:
                return {
                    'status': 'error',
                    'message': result.get('message', 'Unknown error'),
                    'results': []
                }
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error: {str(e)}',
                'results': []
            }


# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChatGPT-Like Email Assistant</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif;
            background: #f7f7f7;
            color: #333;
        }
        
        .container {
            display: flex;
            height: 100vh;
        }
        
        .sidebar {
            width: 260px;
            background: #fff;
            border-right: 1px solid #e5e5e5;
            padding: 20px;
            overflow-y: auto;
        }
        
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            background: #fff;
        }
        
        .header {
            border-bottom: 1px solid #e5e5e5;
            padding: 20px;
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .header h1 {
            font-size: 24px;
            margin-bottom: 5px;
        }
        
        .header p {
            font-size: 12px;
            opacity: 0.9;
        }
        
        .chat-area {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 15px;
            background: #f7f7f7;
        }
        
        .message {
            display: flex;
            margin-bottom: 15px;
            animation: slideIn 0.3s ease-in-out;
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
        
        .message.assistant {
            justify-content: flex-start;
        }
        
        .message-content {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 12px;
            word-wrap: break-word;
        }
        
        .user .message-content {
            background: #10a37f;
            color: white;
            border-radius: 18px 4px 18px 18px;
        }
        
        .assistant .message-content {
            background: #f7f7f7;
            border: 1px solid #e5e5e5;
            border-radius: 4px 18px 18px 4px;
        }
        
        .email-result {
            background: white;
            border: 1px solid #e5e5e5;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
        }
        
        .email-subject {
            font-weight: 600;
            color: #667eea;
            margin-bottom: 8px;
        }
        
        .email-from {
            font-size: 12px;
            color: #999;
            margin-bottom: 8px;
        }
        
        .email-preview {
            font-size: 14px;
            color: #555;
            line-height: 1.5;
        }
        
        .input-area {
            border-top: 1px solid #e5e5e5;
            padding: 20px;
            background: white;
        }
        
        .input-wrapper {
            display: flex;
            gap: 10px;
        }
        
        input[type="text"] {
            flex: 1;
            padding: 12px 16px;
            border: 1px solid #e5e5e5;
            border-radius: 24px;
            font-size: 14px;
            outline: none;
            transition: border-color 0.2s;
        }
        
        input[type="text"]:focus {
            border-color: #667eea;
        }
        
        button {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 24px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: background 0.2s;
        }
        
        button:hover {
            background: #5568d3;
        }
        
        button:active {
            transform: scale(0.98);
        }
        
        .new-chat-btn {
            width: 100%;
            margin-bottom: 20px;
            background: #f7f7f7;
            color: #333;
            border: 1px solid #e5e5e5;
        }
        
        .new-chat-btn:hover {
            background: #f0f0f0;
        }
        
        .sidebar-title {
            font-size: 12px;
            font-weight: 600;
            color: #999;
            margin-top: 20px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        
        .sidebar-item {
            padding: 10px 12px;
            margin: 5px 0;
            background: #f7f7f7;
            border-radius: 8px;
            cursor: pointer;
            font-size: 13px;
            transition: background 0.2s;
        }
        
        .sidebar-item:hover {
            background: #e8e8e8;
        }
        
        .loading {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #999;
        }
        
        .loading::after {
            content: '';
            width: 8px;
            height: 8px;
            background: #999;
            border-radius: 50%;
            animation: bounce 1.5s infinite;
        }
        
        @keyframes bounce {
            0%, 80%, 100% { opacity: 0.4; }
            40% { opacity: 1; }
        }
        
        .error {
            background: #fee;
            border-left: 4px solid #f00;
            padding: 12px;
            border-radius: 4px;
            color: #c00;
        }
        
        .success {
            background: #efe;
            border-left: 4px solid #0a0;
            padding: 12px;
            border-radius: 4px;
            color: #0a0;
        }
        
        .chat-area::-webkit-scrollbar {
            width: 8px;
        }
        
        .chat-area::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        
        .chat-area::-webkit-scrollbar-thumb {
            background: #ccc;
            border-radius: 4px;
        }
        
        .chat-area::-webkit-scrollbar-thumb:hover {
            background: #999;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Sidebar -->
        <div class="sidebar">
            <button class="new-chat-btn">+ New Chat</button>
            
            <div class="sidebar-title">Commands</div>
            <div class="sidebar-item" onclick="sendMessage('help')">📚 Help</div>
            <div class="sidebar-item" onclick="sendMessage('examples')">💡 Examples</div>
            <div class="sidebar-item" onclick="sendMessage('settings')">⚙️ Settings</div>
            <div class="sidebar-item" onclick="sendMessage('clear')">🗑️ Clear History</div>
        </div>
        
        <!-- Main Chat Area -->
        <div class="main-content">
            <div class="header">
                <h1>💼 Email Assistant</h1>
                <p>Ask me anything about your emails - I'll fetch and search them for you!</p>
            </div>
            
            <div class="chat-area" id="chatArea">
                <div class="message assistant">
                    <div class="message-content">
                        👋 Hi! I'm your ChatGPT-like Email Assistant. Ask me anything about your emails!
                        <br><br>
                        Try:
                        <ul>
                            <li>"Show Python developer jobs"</li>
                            <li>"Find remote positions"</li>
                            <li>"Backend engineer 15-20 lpa"</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="input-area">
                <div class="input-wrapper">
                    <input type="text" id="userInput" placeholder="Ask me anything about your emails..." />
                    <button onclick="sendMessage()">Send</button>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        const chatArea = document.getElementById('chatArea');
        const userInput = document.getElementById('userInput');
        
        function scrollToBottom() {
            chatArea.scrollTop = chatArea.scrollHeight;
        }
        
        function addMessage(content, isUser = false) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'assistant'}`;
            messageDiv.innerHTML = `<div class="message-content">${escapeHtml(content)}</div>`;
            chatArea.appendChild(messageDiv);
            scrollToBottom();
        }
        
        function addEmailResult(email) {
            const resultDiv = document.createElement('div');
            resultDiv.className = 'message assistant';
            resultDiv.innerHTML = `
                <div class="message-content">
                    <div class="email-result">
                        <div class="email-subject">📧 ${escapeHtml(email.subject || 'No Subject')}</div>
                        <div class="email-from">From: ${escapeHtml(email.from || 'Unknown')}</div>
                        <div class="email-preview">${escapeHtml(email.preview || '')}</div>
                    </div>
                </div>
            `;
            chatArea.appendChild(resultDiv);
            scrollToBottom();
        }
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        function sendMessage(customText = null) {
            const message = customText || userInput.value.trim();
            
            if (!message) return;
            
            // Add user message to chat
            addMessage(message, true);
            userInput.value = '';
            userInput.focus();
            
            // Show loading indicator
            addMessage('🤔 Processing your request...');
            
            // Send to server
            fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message })
            })
            .then(r => r.json())
            .then(data => {
                // Remove loading message
                chatArea.removeChild(chatArea.lastChild);
                
                if (data.status === 'success') {
                    if (data.results && data.results.length > 0) {
                        addMessage(`✅ Found ${data.results.length} result(s):`);
                        data.results.forEach(email => addEmailResult(email));
                    } else {
                        addMessage(data.message || '✅ Done processing');
                    }
                } else {
                    addMessage(`❌ ${data.message || 'Error processing request'}`);
                }
            })
            .catch(err => {
                chatArea.removeChild(chatArea.lastChild);
                addMessage(`❌ Error: ${err.message}`);
            });
        }
        
        // Allow Enter to send
        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
        
        // Focus input on load
        userInput.focus();
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    """Render main chat interface."""
    return render_template_string(HTML_TEMPLATE)


@app.route('/api/chat', methods=['POST'])
def api_chat():
    """Handle chat API requests."""
    try:
        data = request.json
        query = data.get('message', '').strip()

        if not query:
            return jsonify({
                'status': 'error',
                'message': 'Empty message'
            })

        # Get or create conversation
        conv_id = session.get('conversation_id')
        if not conv_id or conv_id not in conversations:
            conv_id = str(uuid.uuid4())
            conversations[conv_id] = ConversationManager(conv_id)
            session['conversation_id'] = conv_id

        conv = conversations[conv_id]
        conv.add_message('user', query)

        # Handle special commands
        query_lower = query.lower()
        if query_lower == 'help':
            response_text = """
Available Commands:
• help - Show this help
• examples - Show example queries
• settings - Show settings
• clear - Clear history

Just ask naturally about your emails!
"""
            conv.add_message('assistant', response_text)
            return jsonify({
                'status': 'success',
                'message': response_text
            })
        elif query_lower == 'examples':
            response_text = """Example Queries:
1. "Python developer jobs"
2. "Remote positions in Bangalore"
3. "Backend engineer 15-20 lpa"
4. "Latest job notifications"
5. "Data scientist 5+ years"
"""
            conv.add_message('assistant', response_text)
            return jsonify({
                'status': 'success',
                'message': response_text
            })
        elif query_lower == 'clear':
            conv.messages = []
            return jsonify({
                'status': 'success',
                'message': '✅ History cleared'
            })
        else:
            # Process as email query
            result = conv.process_query(query)
            response_msg = result['message']
            conv.add_message('assistant', response_msg)

            return jsonify({
                'status': result['status'],
                'message': response_msg,
                'results': result.get('results', []),
                'count': result.get('count', 0)
            })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Server error: {str(e)}'
        }), 500


@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    """Get all conversations."""
    conv_list = []
    for conv_id, conv in conversations.items():
        conv_list.append({
            'id': conv_id,
            'created_at': conv.created_at.isoformat(),
            'message_count': len(conv.messages)
        })
    return jsonify(conv_list)


@app.route('/api/conversation/<conv_id>', methods=['GET'])
def get_conversation(conv_id):
    """Get specific conversation."""
    if conv_id not in conversations:
        return jsonify({'error': 'Conversation not found'}), 404

    conv = conversations[conv_id]
    return jsonify({
        'id': conv_id,
        'messages': conv.get_messages(),
        'created_at': conv.created_at.isoformat()
    })


def main():
    """Run the Flask app."""
    port = int(os.environ.get('PORT', 5000))
    print(f"\n{'='*70}")
    print("🚀 ChatGPT-Like Email Assistant - Web Version")
    print(f"{'='*70}")
    print(f"\n📱 Open your browser and go to: http://localhost:{port}")
    print(f"\n✅ Fetching emails from your Gmail")
    print(f"✅ All commands work naturally\n")
    print(f"{'='*70}\n")

    app.run(debug=False, host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()

