#!/usr/bin/env python3
"""
Lightweight Gmail Chat Bot - Flask Version (No Streamlit)
Works without PyArrow dependency - solves the DLL issue completely
"""

import sys
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
import os
import uuid
from dataclasses import dataclass

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, request, jsonify, render_template_string, session
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Handle optional imports
try:
    from gmail import get_chatbot_adapter
    GMAIL_AVAILABLE = True
except (ImportError, Exception) as e:
    logger.warning(f"Gmail module not available: {e}")
    GMAIL_AVAILABLE = False

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', f'chat-bot-secret-{uuid.uuid4()}')

# Global conversation storage
conversations: Dict[str, 'ChatConversation'] = {}

@dataclass
class Message:
    """Represents a single message in the chat."""
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: str

    def to_dict(self):
        return {
            'role': self.role,
            'content': self.content,
            'timestamp': self.timestamp
        }

class ChatConversation:
    """Manages a single conversation."""

    def __init__(self, conversation_id: str):
        self.id = conversation_id
        self.messages: List[Message] = []
        self.created_at = datetime.now()
        self._adapter = None
        self.search_depth = 15
        self.auto_summarize = True

    @property
    def adapter(self):
        """Lazy-load Gmail adapter."""
        if self._adapter is None and GMAIL_AVAILABLE:
            self._adapter = get_chatbot_adapter()
        return self._adapter

    def add_message(self, role: str, content: str) -> Message:
        """Add a message to conversation."""
        msg = Message(
            role=role,
            content=content,
            timestamp=datetime.now().isoformat()
        )
        self.messages.append(msg)
        return msg

    def get_messages(self) -> List[Dict]:
        """Get all messages as dictionaries."""
        return [msg.to_dict() for msg in self.messages]

    def process_user_query(self, query: str) -> Dict[str, Any]:
        """Process user query and return results."""
        if not GMAIL_AVAILABLE or not self.adapter:
            return {
                'status': 'error',
                'message': 'Gmail module not available. Please set up Gmail credentials first.',
                'results': []
            }

        try:
            # Add user message
            self.add_message('user', query)

            # Handle special commands
            query_lower = query.lower().strip()

            if query_lower in ['help', '?']:
                response = self._get_help_text()
                self.add_message('assistant', response)
                return {
                    'status': 'success',
                    'message': response,
                    'results': [],
                    'is_command': True
                }

            elif query_lower in ['examples', 'example']:
                response = self._get_examples_text()
                self.add_message('assistant', response)
                return {
                    'status': 'success',
                    'message': response,
                    'results': [],
                    'is_command': True
                }

            elif query_lower in ['clear', 'clear history']:
                self.messages = []
                response = '✅ Chat history cleared'
                return {
                    'status': 'success',
                    'message': response,
                    'results': [],
                    'is_command': True
                }

            elif query_lower in ['status', 'settings']:
                response = self._get_status_text()
                self.add_message('assistant', response)
                return {
                    'status': 'success',
                    'message': response,
                    'results': [],
                    'is_command': True
                }

            else:
                # Normal email search query
                result = self.adapter.search_jobs(query, limit=self.search_depth)

                if result['status'] == 'success':
                    emails = result.get('emails', [])
                    message = f"✅ Found {len(emails)} matching email(s)"
                    self.add_message('assistant', message)

                    return {
                        'status': 'success',
                        'message': message,
                        'results': emails[:10],  # Limit display to 10
                        'count': len(emails)
                    }
                else:
                    message = result.get('message', 'Error searching emails')
                    self.add_message('assistant', f"❌ {message}")
                    return {
                        'status': 'error',
                        'message': message,
                        'results': []
                    }

        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            self.add_message('assistant', error_msg)
            logger.error(f"Error processing query: {e}", exc_info=True)
            return {
                'status': 'error',
                'message': error_msg,
                'results': []
            }

    @staticmethod
    def _get_help_text() -> str:
        """Get help text."""
        return """📚 **Help - Available Commands**

**Email Search:**
• "Python developer jobs" - Search for specific job titles
• "Remote positions" - Search by job type
• "Backend 15-20 lpa" - Search by salary range
• "Company name" - Search by company

**Chat Commands:**
• "help" or "?" - Show this help
• "examples" - Show example queries
• "settings" - Show current settings
• "clear" - Clear chat history
• "status" - Show current status

**Tips:**
✨ Be natural! Ask like you would to a friend
✨ Combine keywords: "Python remote 20+ lpa"
✨ Results show relevant job notifications"""

    @staticmethod
    def _get_examples_text() -> str:
        """Get examples text."""
        return """💡 **Example Queries**

**By Job Title:**
• "Show me Python developer jobs"
• "Find data scientist positions"
• "Backend engineer opportunities"

**By Location:**
• "Remote jobs in Bangalore"
• "Jobs in Mumbai"
• "Work from home positions"

**By Salary:**
• "Jobs 15-20 lpa"
• "Positions paying 5+ lakh"
• "High paying tech jobs"

**Combined Queries:**
• "Python developer remote 20+ lpa"
• "Data scientist Bangalore 10-15 lpa"
• "Backend engineer work from home"

**Latest:**
• "Recent job notifications"
• "Latest opportunities"
• "Today's jobs"

Try any of these in the chat! 🚀"""

    @staticmethod
    def _get_status_text() -> str:
        """Get status text."""
        status_info = f"""⚙️ **Current Status**

**Settings:**
• Search Depth: 15 results
• Auto-Summarize: Enabled
• Gmail Integration: {'✅ Connected' if GMAIL_AVAILABLE else '❌ Not Connected'}

**Features:**
✅ Chat history saved in session
✅ Multiple conversations supported
✅ Real-time Gmail search
✅ Email preview in chat
✅ Command history support

**Browser:**
• JavaScript: Enabled
• Cookies: Enabled (for session)
• Local Storage: Ready

You're all set! Start chatting! 💬"""
        return status_info

# HTML Template with enhanced chat UI
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gmail Job Notifications Chat</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body {
            height: 100%;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .container {
            width: 90%;
            max-width: 900px;
            height: 85vh;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            text-align: center;
            border-bottom: 3px solid rgba(255,255,255,0.1);
        }
        
        .header h1 {
            font-size: 28px;
            margin-bottom: 5px;
            font-weight: 700;
        }
        
        .header p {
            font-size: 14px;
            opacity: 0.9;
        }
        
        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 25px;
            background: #f8f9fa;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .message {
            display: flex;
            margin-bottom: 10px;
            animation: slideIn 0.3s ease-out;
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
        
        .message-bubble {
            max-width: 75%;
            padding: 12px 18px;
            border-radius: 18px;
            word-wrap: break-word;
            line-height: 1.4;
            font-size: 14px;
        }
        
        .user .message-bubble {
            background: #667eea;
            color: white;
            border-radius: 20px 4px 20px 20px;
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
        }
        
        .assistant .message-bubble {
            background: white;
            color: #333;
            border: 1px solid #e0e0e0;
            border-radius: 4px 20px 20px 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .assistant .message-bubble ul {
            margin-left: 20px;
            margin-top: 8px;
        }
        
        .assistant .message-bubble li {
            margin: 4px 0;
        }
        
        .email-card {
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin: 8px 0;
            border-left: 4px solid #667eea;
        }
        
        .email-subject {
            font-weight: 600;
            color: #667eea;
            margin-bottom: 8px;
            font-size: 15px;
        }
        
        .email-from {
            font-size: 12px;
            color: #999;
            margin-bottom: 6px;
        }
        
        .email-preview {
            font-size: 13px;
            color: #666;
            line-height: 1.5;
        }
        
        .input-area {
            border-top: 1px solid #e0e0e0;
            padding: 20px;
            background: white;
        }
        
        .input-wrapper {
            display: flex;
            gap: 10px;
        }
        
        input[type="text"] {
            flex: 1;
            padding: 14px 18px;
            border: 2px solid #e0e0e0;
            border-radius: 25px;
            font-size: 14px;
            outline: none;
            transition: all 0.3s;
        }
        
        input[type="text"]:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        input[type="text"]::placeholder {
            color: #aaa;
        }
        
        button {
            padding: 12px 28px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        button:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        button:disabled {
            background: #ccc;
            cursor: not-allowed;
            transform: none;
        }
        
        .typing-indicator {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .typing-dot {
            width: 8px;
            height: 8px;
            background: #999;
            border-radius: 50%;
            animation: typing 1.4s infinite;
        }
        
        .typing-dot:nth-child(2) {
            animation-delay: 0.2s;
        }
        
        .typing-dot:nth-child(3) {
            animation-delay: 0.4s;
        }
        
        @keyframes typing {
            0%, 60%, 100% { opacity: 0.5; }
            30% { opacity: 1; }
        }
        
        .error-message {
            color: #d32f2f;
            font-weight: 500;
            padding: 10px;
            background: #ffebee;
            border-left: 3px solid #d32f2f;
            border-radius: 4px;
        }
        
        .success-message {
            color: #388e3c;
            font-weight: 500;
            padding: 10px;
            background: #e8f5e9;
            border-left: 3px solid #388e3c;
            border-radius: 4px;
        }
        
        .chat-messages::-webkit-scrollbar {
            width: 8px;
        }
        
        .chat-messages::-webkit-scrollbar-track {
            background: transparent;
        }
        
        .chat-messages::-webkit-scrollbar-thumb {
            background: #ccc;
            border-radius: 4px;
        }
        
        .chat-messages::-webkit-scrollbar-thumb:hover {
            background: #999;
        }
        
        @media (max-width: 600px) {
            .container {
                width: 95%;
                height: 90vh;
                border-radius: 10px;
            }
            
            .message-bubble {
                max-width: 85%;
            }
            
            .header h1 {
                font-size: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💬 Gmail Job Chat</h1>
            <p>Ask me about your job notifications - powered by Flask & your Gmail</p>
        </div>
        
        <div class="chat-messages" id="chatMessages">
            <div class="message assistant">
                <div class="message-bubble">
                    👋 <strong>Welcome to Gmail Job Chat!</strong><br><br>
                    I can search your email for job notifications. Just ask naturally:
                    <ul>
                        <li>"Show Python developer jobs"</li>
                        <li>"Find remote positions"</li>
                        <li>"Backend engineer 15-20 lpa"</li>
                    </ul>
                    <br>Type <strong>"help"</strong> for more commands or <strong>"examples"</strong> to see more queries! 🚀
                </div>
            </div>
        </div>
        
        <div class="input-area">
            <div class="input-wrapper">
                <input 
                    type="text" 
                    id="userInput" 
                    placeholder="Ask about your job notifications... (or type 'help')"
                    autocomplete="off"
                />
                <button id="sendBtn" onclick="sendMessage()">Send</button>
            </div>
        </div>
    </div>
    
    <script>
        const chatMessages = document.getElementById('chatMessages');
        const userInput = document.getElementById('userInput');
        const sendBtn = document.getElementById('sendBtn');
        let isLoading = false;
        
        function scrollToBottom() {
            setTimeout(() => {
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }, 100);
        }
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        function formatText(text) {
            // Convert markdown-like formatting to HTML
            text = escapeHtml(text);
            text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            text = text.replace(/__(.*?)__/g, '<strong>$1</strong>');
            text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
            text = text.replace(/\n/g, '<br>');
            return text;
        }
        
        function addMessage(content, isUser = false, isHtml = false) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'assistant'}`;
            
            const bubble = document.createElement('div');
            bubble.className = 'message-bubble';
            bubble.innerHTML = isHtml ? content : formatText(content);
            
            messageDiv.appendChild(bubble);
            chatMessages.appendChild(messageDiv);
            scrollToBottom();
        }
        
        function addEmailResult(email) {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message assistant';
            
            const emailHtml = `
                <div class="email-card">
                    <div class="email-subject">📧 ${escapeHtml(email.subject || 'No Subject')}</div>
                    <div class="email-from">From: ${escapeHtml(email.from || 'Unknown')}</div>
                    <div class="email-preview">${escapeHtml(email.preview || '').substring(0, 200)}...</div>
                </div>
            `;
            
            messageDiv.innerHTML = emailHtml;
            chatMessages.appendChild(messageDiv);
            scrollToBottom();
        }
        
        function addLoadingIndicator() {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message assistant';
            messageDiv.id = 'loadingMessage';
            
            const bubble = document.createElement('div');
            bubble.className = 'message-bubble typing-indicator';
            bubble.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
            
            messageDiv.appendChild(bubble);
            chatMessages.appendChild(messageDiv);
            scrollToBottom();
        }
        
        function removeLoadingIndicator() {
            const loading = document.getElementById('loadingMessage');
            if (loading) loading.remove();
        }
        
        function sendMessage() {
            const message = userInput.value.trim();
            if (!message || isLoading) return;
            
            // Disable input
            isLoading = true;
            sendBtn.disabled = true;
            userInput.disabled = true;
            
            // Add user message
            addMessage(message, true);
            userInput.value = '';
            
            // Show loading
            addLoadingIndicator();
            
            // Send to server
            fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message })
            })
            .then(r => r.json())
            .then(data => {
                removeLoadingIndicator();
                
                if (data.status === 'success') {
                    // Add response message
                    addMessage(data.message || '✅ Done', false, true);
                    
                    // Add email results
                    if (data.results && data.results.length > 0) {
                        data.results.forEach(email => addEmailResult(email));
                    }
                } else {
                    addMessage(`❌ ${data.message || 'Error'}`, false, true);
                }
            })
            .catch(err => {
                removeLoadingIndicator();
                addMessage(`❌ Connection error: ${err.message}`, false, true);
            })
            .finally(() => {
                isLoading = false;
                sendBtn.disabled = false;
                userInput.disabled = false;
                userInput.focus();
            });
        }
        
        // Allow Enter to send
        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !isLoading) {
                sendMessage();
            }
        });
        
        // Focus input on load
        userInput.focus();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Main chat interface."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """Chat API endpoint."""
    try:
        data = request.get_json() or {}
        message = data.get('message', '').strip()

        if not message:
            return jsonify({
                'status': 'error',
                'message': 'Please enter a message'
            }), 400

        # Get or create conversation
        conv_id = session.get('conversation_id')
        if not conv_id or conv_id not in conversations:
            conv_id = str(uuid.uuid4())
            conversations[conv_id] = ChatConversation(conv_id)
            session['conversation_id'] = conv_id

        conv = conversations[conv_id]
        result = conv.process_user_query(message)

        return jsonify(result)

    except Exception as e:
        logger.error(f"API error: {e}", exc_info=True)
        return jsonify({
            'status': 'error',
            'message': f'Server error: {str(e)}'
        }), 500

@app.route('/api/conversations', methods=['GET'])
def get_all_conversations():
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

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'ok',
        'gmail_available': GMAIL_AVAILABLE,
        'conversations': len(conversations)
    })

def main():
    """Run the chat bot."""
    port = int(os.environ.get('PORT', 5000))

    print("\n" + "="*70)
    print("🚀 Gmail Job Chat Bot - Flask Version (No Streamlit)")
    print("="*70)
    print(f"\n✅ No PyArrow DLL issues!")
    print(f"✅ Full chat functionality with history")
    print(f"✅ Beautiful ChatGPT-like interface\n")
    print(f"📱 Open browser: http://localhost:{port}")
    print(f"💬 Start chatting about your job notifications!\n")
    print(f"💡 Commands: help, examples, clear, status")
    print(f"{"="*70}\n")

    app.run(debug=False, host='127.0.0.1', port=port, threaded=True)

if __name__ == '__main__':
    main()

