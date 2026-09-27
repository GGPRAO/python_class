#!/usr/bin/env python3
"""
Lightweight ChatGPT-like UI for Ollama
No external dependencies needed except ollama and a simple HTTP server
"""

import json
import os
import sys
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import ollama

# Configuration
MODEL_NAME = "qwen2:1.5b"
HOST = "localhost"
PORT = 5000
CONVERSATION_HISTORY = []

# Get the directory of this script
SCRIPT_DIR = Path(__file__).parent.resolve()
os.chdir(SCRIPT_DIR)

class ChatGPTHandler(SimpleHTTPRequestHandler):
    """Custom HTTP handler for the chat interface"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # Serve the HTML file
            html_file = SCRIPT_DIR / 'chatgpt_ui.html'
            if html_file.exists():
                with open(html_file, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b"<h1>chatgpt_ui.html not found</h1>")

        elif self.path == '/api/history':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(CONVERSATION_HISTORY).encode())

        else:
            super().do_GET()

    def do_POST(self):
        """Handle POST requests"""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body.decode('utf-8'))
        except:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Invalid JSON'}).encode())
            return

        if self.path == '/api/chat':
            self.handle_chat(data)
        elif self.path == '/api/clear':
            self.handle_clear()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())

    def handle_chat(self, data):
        """Handle chat message"""
        global CONVERSATION_HISTORY

        try:
            message = data.get('message', '').strip()

            if not message:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Empty message'}).encode())
                return

            # Add user message to history
            CONVERSATION_HISTORY.append({
                'role': 'user',
                'content': message
            })

            # Get response from Ollama
            try:
                response = ollama.chat(
                    model=MODEL_NAME,
                    messages=CONVERSATION_HISTORY,
                    stream=False
                )

                assistant_message = response['message']['content']

                # Add assistant response to history
                CONVERSATION_HISTORY.append({
                    'role': 'assistant',
                    'content': assistant_message
                })

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': True,
                    'response': assistant_message
                }).encode())

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': False,
                    'error': str(e)
                }).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': str(e)
            }).encode())

    def handle_clear(self):
        """Clear conversation history"""
        global CONVERSATION_HISTORY
        CONVERSATION_HISTORY = []

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'success': True}).encode())

    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

def run_server():
    """Start the HTTP server"""
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, ChatGPTHandler)

    print("\n" + "="*50)
    print("🤖 Qwen AI Chat - ChatGPT Style UI")
    print("="*50)
    print(f"\n✅ Server running at: http://{HOST}:{PORT}")
    print(f"📱 Open this URL in your browser")
    print(f"\n🚀 Model: {MODEL_NAME}")
    print(f"💾 Ensure Ollama is running: ollama serve")
    print("\n📌 Press Ctrl+C to stop the server\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✋ Server stopped.")
        sys.exit(0)

if __name__ == '__main__':
    # Check if ollama is available
    try:
        import ollama
    except ImportError:
        print("❌ Error: ollama package not found")
        print("Install it with: pip install ollama")
        sys.exit(1)

    # Check if chatgpt_ui.html exists
    html_file = SCRIPT_DIR / 'chatgpt_ui.html'
    if not html_file.exists():
        print(f"❌ Error: {html_file} not found")
        print("Make sure chatgpt_ui.html is in the same directory")
        sys.exit(1)

    # Run the server
    run_server()

