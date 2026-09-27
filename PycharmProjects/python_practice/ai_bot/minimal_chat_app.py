#!/usr/bin/env python3
"""
ABSOLUTE MINIMAL WORKING AI CHAT - No Dependencies Whatsoever
This is the most minimal version possible

Run: python minimal_chat_app.py
Then: Open http://127.0.0.1:5000 in browser
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

# Minimal HTML
HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AI Chat</title>
<style>
body { font-family: Arial; background: #667eea; margin: 0; height: 100vh; display: flex; justify-content: center; align-items: center; }
.container { background: white; border-radius: 10px; width: 90%; max-width: 700px; height: 80vh; display: flex; flex-direction: column; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }
.header { background: #667eea; color: white; padding: 20px; text-align: center; }
.chat { flex: 1; overflow-y: auto; padding: 15px; background: #f5f5f5; }
.msg { margin: 10px 0; }
.msg.user { text-align: right; }
.msg.bot { text-align: left; }
.bubble { display: inline-block; padding: 10px 15px; border-radius: 10px; max-width: 80%; word-wrap: break-word; }
.user .bubble { background: #667eea; color: white; }
.bot .bubble { background: #e0e0e0; color: #333; }
.input { padding: 15px; border-top: 1px solid #ddd; display: flex; gap: 10px; }
input { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
button { padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer; }
button:hover { background: #5568d3; }
</style>
</head>
<body>
<div class="container">
<div class="header"><h2>🤖 AI Chat</h2></div>
<div class="chat" id="chat"></div>
<div class="input">
<input type="text" id="msg" placeholder="Type message..." autocomplete="off">
<button onclick="send()">Send</button>
</div>
</div>
<script>
const chat = document.getElementById('chat');
const input = document.getElementById('msg');

function send() {
  const text = input.value.trim();
  if (!text) return;
  
  addMsg(text, 'user');
  input.value = '';
  
  fetch('/api/chat', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({msg: text})
  })
  .then(r => r.json())
  .then(d => addMsg(d.reply, 'bot'))
  .catch(e => addMsg('Error: ' + e, 'bot'));
}

function addMsg(text, role) {
  const div = document.createElement('div');
  div.className = 'msg ' + role;
  div.innerHTML = '<div class="bubble">' + escapeHtml(text) + '</div>';
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

function escapeHtml(text) {
  const map = {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;'};
  return text.replace(/[&<>"']/g, m => map[m]);
}

input.addEventListener('keypress', e => { if (e.key === 'Enter') send(); });
window.addEventListener('load', () => addMsg('Hi! Type your message below.', 'bot'));
</script>
</body>
</html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML.encode())

    def do_POST(self):
        if self.path == '/api/chat':
            length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(length))
            msg = data.get('msg', '')

            # Simple responses
            if not msg:
                reply = "Please type something"
            elif any(w in msg.lower() for w in ['hi', 'hello', 'hey']):
                reply = "Hello! How can I help?"
            elif any(w in msg.lower() for w in ['how', 'you']):
                reply = "I'm doing well! How are you?"
            else:
                reply = f"You said: {msg}"

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'reply': reply}).encode())

    def log_message(self, format, *args):
        pass  # Silent

if __name__ == '__main__':
    print("Starting AI Chat Server...")
    print("Open: http://127.0.0.1:5000")
    print("Press Ctrl+C to stop")
    HTTPServer(('127.0.0.1', 5000), Handler).serve_forever()

