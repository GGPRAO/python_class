#!/usr/bin/env python3
"""
Gmail Chatbot - Flask Chat Interface
A conversational chatbot UI for fetching and discussing Naukri jobs
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, render_template_string, request, jsonify, session
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'gmail-chatbot-secret-key'

# Try to import gmail module
try:
    from gmail import get_chatbot_adapter, get_gmail_status, get_gmail_options
    gmail_available = True
except ImportError:
    gmail_available = False

# Chat history storage (in-memory for demo)
chat_history = []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Naukri Job Assistant - Chat</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .chat-container {
            display: flex;
            flex-direction: column;
            width: 100%;
            max-width: 700px;
            height: 90vh;
            max-height: 800px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }
        
        .chat-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .chat-header h1 {
            font-size: 1.5rem;
            margin-bottom: 5px;
        }
        
        .chat-header p {
            font-size: 0.9rem;
            opacity: 0.9;
        }
        
        .chat-messages {
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
        
        .message.bot {
            justify-content: flex-start;
        }
        
        .message-content {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 12px;
            line-height: 1.5;
        }
        
        .message.user .message-content {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-bottom-right-radius: 2px;
        }
        
        .message.bot .message-content {
            background: #e9ecef;
            color: #333;
            border-bottom-left-radius: 2px;
        }
        
        .message.bot .message-content strong {
            color: #667eea;
        }
        
        .message.error .message-content {
            background: #f8d7da;
            color: #721c24;
        }
        
        .job-card {
            background: white;
            border-left: 4px solid #667eea;
            padding: 12px;
            margin: 8px 0;
            border-radius: 6px;
            font-size: 0.9rem;
        }
        
        .job-card h4 {
            color: #667eea;
            margin-bottom: 5px;
        }
        
        .job-card p {
            color: #666;
            font-size: 0.85rem;
        }
        
        .typing-indicator {
            display: flex;
            align-items: center;
            gap: 4px;
        }
        
        .typing-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #667eea;
            animation: typing 1.4s infinite;
        }
        
        .typing-dot:nth-child(2) {
            animation-delay: 0.2s;
        }
        
        .typing-dot:nth-child(3) {
            animation-delay: 0.4s;
        }
        
        @keyframes typing {
            0%, 60%, 100% {
                transform: translateY(0);
                opacity: 0.7;
            }
            30% {
                transform: translateY(-10px);
                opacity: 1;
            }
        }
        
        .chat-input-area {
            padding: 15px;
            background: white;
            border-top: 1px solid #e9ecef;
            display: flex;
            gap: 10px;
        }
        
        .input-group {
            display: flex;
            width: 100%;
            gap: 10px;
        }
        
        #messageInput {
            flex: 1;
            padding: 10px 15px;
            border: 1px solid #ddd;
            border-radius: 25px;
            font-size: 0.95rem;
            outline: none;
            transition: border-color 0.3s;
        }
        
        #messageInput:focus {
            border-color: #667eea;
        }
        
        #sendBtn {
            padding: 10px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        #sendBtn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        #sendBtn:active {
            transform: translateY(0);
        }
        
        .suggestions {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 10px;
        }
        
        .suggestion-btn {
            padding: 8px 12px;
            background: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.85rem;
            transition: all 0.3s;
        }
        
        .suggestion-btn:hover {
            background: #e0e0e0;
            border-color: #667eea;
        }
        
        .welcome-message {
            text-align: center;
            padding: 20px;
        }
        
        .welcome-message h2 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .loading-spinner {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(102, 126, 234, 0.3);
            border-top-color: #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .commands-list {
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 10px;
            margin: 8px 0;
            font-size: 0.9rem;
        }
        
        .commands-list ul {
            list-style: none;
            padding-left: 10px;
        }
        
        .commands-list li {
            padding: 5px 0;
            color: #666;
        }
        
        .status-badge {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        
        .status-badge.online {
            background: #d4edda;
            color: #155724;
        }
        
        .status-badge.offline {
            background: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h1>💼 Naukri Job Assistant</h1>
            <p>Chat with your job notification bot</p>
        </div>
        
        <div class="chat-messages" id="chatMessages">
            <div class="message bot">
                <div class="message-content">
                    <div class="welcome-message">
                        <h2>👋 Hello! I'm your Naukri Job Assistant</h2>
                        <p>I can help you fetch and view your latest job notifications from Gmail.</p>
                        <br>
                        <p>Try these commands:</p>
                        <div class="suggestions">
                            <button class="suggestion-btn" onclick="sendMessage('fetch jobs')">
                                🔄 Fetch jobs
                            </button>
                            <button class="suggestion-btn" onclick="sendMessage('check status')">
                                ℹ️ Check status
                            </button>
                            <button class="suggestion-btn" onclick="sendMessage('show commands')">
                                🎛️ Commands
                            </button>
                            <button class="suggestion-btn" onclick="sendMessage('help')">
                                ❓ Help
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="chat-input-area">
            <div class="input-group">
                <input 
                    type="text" 
                    id="messageInput" 
                    placeholder="Type a command... (e.g., 'fetch jobs', 'check status')"
                    autocomplete="off"
                />
                <button id="sendBtn" onclick="sendMessage()">Send</button>
            </div>
        </div>
    </div>
    
    <script>
        const chatMessages = document.getElementById('chatMessages');
        const messageInput = document.getElementById('messageInput');
        const sendBtn = document.getElementById('sendBtn');
        
        // Focus on input on load
        window.addEventListener('load', () => messageInput.focus());
        
        // Send on Enter key
        messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
        
        function sendMessage(text = null) {
            const message = text || messageInput.value.trim();
            
            if (!message) return;
            
            // Clear input
            messageInput.value = '';
            
            // Add user message to chat
            addMessage(message, 'user');
            
            // Show typing indicator
            showTypingIndicator();
            
            // Send to backend
            fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            })
            .then(res => res.json())
            .then(data => {
                removeTypingIndicator();
                
                if (data.success) {
                    addMessage(data.response, 'bot');
                    
                    // Add jobs if available
                    if (data.jobs && data.jobs.length > 0) {
                        addJobsToChat(data.jobs);
                    }
                } else {
                    addMessage(data.error || 'Error processing request', 'error');
                }
            })
            .catch(error => {
                removeTypingIndicator();
                addMessage(`Error: ${error.message}`, 'error');
            });
            
            messageInput.focus();
        }
        
        function addMessage(text, type = 'bot') {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${type}`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.innerHTML = text;
            
            messageDiv.appendChild(contentDiv);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function addJobsToChat(jobs) {
            const jobsContainer = document.createElement('div');
            jobsContainer.className = 'message bot';
            
            const jobsHtml = jobs.map((job, idx) => `
                <div class="job-card">
                    <h4>#${idx + 1} - ${job.subject || 'No Subject'}</h4>
                    <p>${(job.body || 'No content').substring(0, 200)}...</p>
                </div>
            `).join('');
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.innerHTML = jobsHtml;
            
            jobsContainer.appendChild(contentDiv);
            chatMessages.appendChild(jobsContainer);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function showTypingIndicator() {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot';
            messageDiv.id = 'typing-indicator';
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.innerHTML = `
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            `;
            
            messageDiv.appendChild(contentDiv);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function removeTypingIndicator() {
            const indicator = document.getElementById('typing-indicator');
            if (indicator) indicator.remove();
        }
    </script>
</body>
</html>
'''

def process_command(message):
    """Process user commands and return response"""
    message_lower = message.lower().strip()

    if not gmail_available:
        return {
            'success': False,
            'error': '❌ Gmail module not available. Please check installation.'
        }

    try:
        adapter = get_chatbot_adapter()

        # Fetch jobs command
        if 'fetch' in message_lower or 'jobs' in message_lower or 'email' in message_lower:
            # Extract limit if provided
            limit = 5
            if 'limit' in message_lower or 'fetch' in message_lower:
                import re
                match = re.search(r'\d+', message)
                if match:
                    limit = min(int(match.group()), 20)

            result = adapter.fetch_jobs(limit=limit)

            if result['status'] == 'success':
                return {
                    'success': True,
                    'response': f"✅ <strong>Found {result['count']} Naukri jobs!</strong>",
                    'jobs': result['emails']
                }
            else:
                return {
                    'success': False,
                    'error': f"❌ {result.get('message', 'Could not fetch jobs')}"
                }

        # Status command
        elif 'status' in message_lower or 'check' in message_lower:
            status = adapter.get_status()
            response = f"""
            <strong>📊 Gmail Service Status</strong><br>
            📧 Email: {status.get('email')}<br>
            🔗 Service: {status.get('service')}<br>
            🔓 Authenticated: {'✅ Yes' if status.get('authenticated') else '❌ No'}<br>
            ✨ Available: {'✅ Yes' if status.get('available') else '❌ No'}
            """
            return {
                'success': True,
                'response': response
            }

        # Commands list
        elif 'commands' in message_lower or 'help' in message_lower or 'what' in message_lower:
            options = adapter.get_options()
            cmd_html = '<strong>🎛️ Available Commands:</strong><div class="commands-list"><ul>'

            for cmd in options.get('options', []):
                cmd_html += f"<li><strong>{cmd['name']}</strong> - {cmd['description']}</li>"

            cmd_html += '</ul></div>'

            return {
                'success': True,
                'response': cmd_html
            }

        # Help command
        elif message_lower in ['help', '?', 'hi', 'hello', 'start']:
            return {
                'success': True,
                'response': """
                <strong>📖 Here's what I can do:</strong><br><br>
                💼 <strong>Fetch Jobs</strong> - Get your latest Naukri notifications<br>
                ℹ️ <strong>Check Status</strong> - See Gmail connection status<br>
                🎛️ <strong>Show Commands</strong> - List available commands<br>
                ❓ <strong>Help</strong> - Show this help message
                """
            }

        else:
            return {
                'success': True,
                'response': f"""
                I didn't understand '{message}'. <br><br>
                Try: <br>
                • "fetch jobs" - Get job notifications<br>
                • "check status" - Check Gmail status<br>
                • "show commands" - See available commands<br>
                • "help" - Get help
                """
            }

    except Exception as e:
        return {
            'success': False,
            'error': f'❌ Error: {str(e)}'
        }

@app.route('/')
def index():
    """Serve the chat UI"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.json
    message = data.get('message', '').strip()

    if not message:
        return jsonify({
            'success': False,
            'error': 'Please enter a message'
        })

    result = process_command(message)
    return jsonify(result)

if __name__ == '__main__':
    print("=" * 70)
    print("🤖 Gmail Chatbot - Chat Interface")
    print("=" * 70)
    print("\n📱 Open your browser to: http://localhost:5500")
    print("💬 Start chatting with your job assistant!")
    print("\nPress Ctrl+C to stop\n")

    app.run(debug=True, port=5500, use_reloader=False)

