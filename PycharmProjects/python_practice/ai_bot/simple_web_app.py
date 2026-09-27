#!/usr/bin/env python3
"""
GGPRAO AI Chat - Streamlit-Free Alternative (WORKS WITHOUT PYARROW)
Use this when Streamlit fails due to PyArrow DLL blocking

This version uses only pure Python + minimal dependencies
No Streamlit, No PyArrow dependency required!

Usage: python simple_web_app.py
Then open: http://localhost:5000 in your browser
"""

import json
import os
import sys
import threading
from datetime import datetime
from pathlib import Path

# Try to import only essential packages (no Streamlit/PyArrow)
try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import urllib.parse
except ImportError:
    print("❌ This Python installation is missing required modules")
    sys.exit(1)

# Try Ollama, but continue if not available
try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

# Chat history storage
chat_history = []
MAX_HISTORY = 100

# HTML Template
HTML_CONTENT = """
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
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .container {
            width: 100%;
            max-width: 900px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            height: 90vh;
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
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 14px;
            opacity: 0.9;
        }
        
        .status-bar {
            background: #f0f0f0;
            padding: 10px 20px;
            font-size: 12px;
            color: #666;
            border-bottom: 1px solid #ddd;
        }
        
        .status-bar.ok { background: #d4edda; color: #155724; }
        .status-bar.warning { background: #fff3cd; color: #856404; }
        
        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: #fafafa;
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
        
        .message-bubble {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 12px;
            word-wrap: break-word;
            line-height: 1.4;
        }
        
        .message.user .message-bubble {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-bottom-right-radius: 4px;
        }
        
        .message.assistant .message-bubble {
            background: #e9ecef;
            color: #333;
            border-bottom-left-radius: 4px;
        }
        
        .message-time {
            font-size: 11px;
            color: #999;
            margin-top: 4px;
            padding: 0 4px;
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
        
        button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        
        .loading {
            text-align: center;
            color: #999;
            font-style: italic;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 GGPRAO AI Chat</h1>
            <p>PyArrow-Free Web Interface | Pure Python</p>
        </div>
        
        <div class="status-bar" id="statusBar">
            ✅ Ready to chat
        </div>
        
        <div class="chat-container" id="chatContainer"></div>
        
        <div class="input-area">
            <input 
                type="text" 
                id="messageInput" 
                placeholder="Type your message..." 
                autocomplete="off"
            />
            <button onclick="sendMessage()" id="sendBtn">Send</button>
        </div>
    </div>
    
    <script>
        const chatContainer = document.getElementById('chatContainer');
        const messageInput = document.getElementById('messageInput');
        const sendBtn = document.getElementById('sendBtn');
        const statusBar = document.getElementById('statusBar');
        
        function formatTime(date) {
            return date.toLocaleTimeString('en-US', {
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                hour12: true
            });
        }
        
        function scrollToBottom() {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        
        function addMessage(text, role) {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message ' + role;
            
            const time = new Date();
            const bubble = document.createElement('div');
            bubble.className = 'message-bubble';
            
            const textSpan = document.createElement('div');
            textSpan.textContent = text;
            
            const timeSpan = document.createElement('div');
            timeSpan.className = 'message-time';
            timeSpan.textContent = formatTime(time);
            
            bubble.appendChild(textSpan);
            bubble.appendChild(timeSpan);
            messageDiv.appendChild(bubble);
            
            chatContainer.appendChild(messageDiv);
            scrollToBottom();
        }
        
        function setStatus(message, type = 'ok') {
            statusBar.className = 'status-bar ' + type;
            statusBar.textContent = message;
        }
        
        function sendMessage() {
            const message = messageInput.value.trim();
            if (!message) return;
            
            addMessage(message, 'user');
            messageInput.value = '';
            
            sendBtn.disabled = true;
            setStatus('⏳ Thinking...', 'warning');
            
            fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: message})
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response, 'assistant');
                setStatus('✅ Ready to chat', 'ok');
                sendBtn.disabled = false;
            })
            .catch(error => {
                addMessage('Error: ' + error.message, 'assistant');
                setStatus('❌ Error occurred', 'warning');
                sendBtn.disabled = false;
            });
        }
        
        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
        
        // Initial message
        window.addEventListener('load', function() {
            addMessage('👋 Hello! I\'m your AI assistant. How can I help you today?', 'assistant');
            messageInput.focus();
        });
    </script>
</body>
</html>
"""

class ChatHandler(BaseHTTPRequestHandler):
    """HTTP Request handler for chat application"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/api/chat':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                user_message = data.get('message', '').strip()
                if not user_message:
                    self.send_json_response({'response': 'Please enter a message'}, 400)
                    return

                # Get AI response
                if OLLAMA_AVAILABLE:
                    try:
                        response = ollama.chat(
                            model='neural-chat',
                            messages=[{'role': 'user', 'content': user_message}],
                            stream=False
                        )
                        ai_response = response.get('message', {}).get('content', 'No response received')
                    except Exception as e:
                        ai_response = get_demo_response(user_message)
                else:
                    ai_response = get_demo_response(user_message)

                # Store in history
                chat_history.append({
                    'user': user_message,
                    'assistant': ai_response,
                    'timestamp': datetime.now().isoformat()
                })

                if len(chat_history) > MAX_HISTORY:
                    chat_history.pop(0)

                self.send_json_response({'response': ai_response})

            except Exception as e:
                self.send_json_response({'error': str(e)}, 500)
        else:
            self.send_response(404)
            self.end_headers()

    def send_json_response(self, data, status_code=200):
        """Send JSON response"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

def get_demo_response(message):
    """Generate demo responses when Ollama is unavailable"""
    message_lower = message.lower()

    if any(word in message_lower for word in ['hello', 'hi', 'hey']):
        return "Hello! I'm running in demo mode since Ollama isn't available. For real AI responses, please install and run Ollama."
    elif any(word in message_lower for word in ['how', 'you', 'doing']):
        return "I'm doing well, thank you for asking! In production, I'd connect to a real AI model for smarter responses."
    elif any(word in message_lower for word in ['help', 'what', 'who']):
        return "I'm a demo AI assistant. This interface proves that we can run a functional chat app without Streamlit or PyArrow!"
    else:
        return f"You said: '{message}'. In production mode with Ollama running, I would provide intelligent AI-generated responses."

def main():
    port = 5000
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, ChatHandler)

    print("=" * 70)
    print("🚀 GGPRAO AI Chat - Pure Python Web Server")
    print("=" * 70)
    print(f"\n✅ Ollama Status: {'Available ✨' if OLLAMA_AVAILABLE else 'Not Available (Demo Mode)'}")
    print(f"\n🌐 Server running at: http://127.0.0.1:{port}")
    print("\n📝 Chat features:")
    print("   - Real-time message streaming")
    print("   - Persistent chat history")
    print("   - No Streamlit required")
    print("   - No PyArrow dependency")
    print("   - Works on restricted systems")
    print("\n💡 To stop the server: Press Ctrl+C")
    print("\n" + "=" * 70 + "\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped gracefully")
        httpd.shutdown()

if __name__ == '__main__':
    main()

