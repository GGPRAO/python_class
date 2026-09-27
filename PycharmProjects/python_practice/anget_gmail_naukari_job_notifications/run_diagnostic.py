#!/usr/bin/env python3
"""
Diagnostic and launcher script for ChatGPT-Like Email Assistant
"""

import sys
import os
import subprocess
from pathlib import Path

# Get the script directory
script_dir = Path(__file__).parent.absolute()
print(f"[DIAG] Working directory: {script_dir}")
print(f"[DIAG] Python executable: {sys.executable}")
print(f"[DIAG] Python version: {sys.version}")

# Step 1: Check if flask-cors is installed
print("\n[DIAG] Checking dependencies...")
try:
    import flask
    print("[OK] flask is installed")
except ImportError:
    print("[ERROR] flask not found - installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask==2.3.2'])

try:
    import flask_cors
    print("[OK] flask-cors is installed")
except ImportError:
    print("[ERROR] flask-cors not found - installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask-cors==4.0.0'])

try:
    from google.auth import oauthlib
    print("[OK] google-auth is installed")
except ImportError:
    print("[ERROR] google-auth not found - installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'google-auth-oauthlib==1.1.0'])

# Step 2: Try to import the web interface
print("\n[DIAG] Attempting to import chatgpt_web_interface...")
try:
    os.chdir(script_dir)
    sys.path.insert(0, str(script_dir))
    from chatgpt_web_interface import app
    print("[OK] chatgpt_web_interface imported successfully")
except Exception as e:
    print(f"[ERROR] Failed to import chatgpt_web_interface: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Step 3: Launch the application
print("\n[DIAG] Launching ChatGPT-Like Email Assistant...")
print("="*70)
print("🚀 ChatGPT-Like Email Assistant - Web Interface Starting")
print("="*70)
print("\nServer will run on: http://localhost:5000")
print("Press Ctrl+C to stop the server\n")

try:
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
except KeyboardInterrupt:
    print("\n\n" + "="*70)
    print("👋 Server stopped. Thank you for using ChatGPT-Like Email Assistant!")
    print("="*70)
except Exception as e:
    print(f"\n[ERROR] Fatal error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

