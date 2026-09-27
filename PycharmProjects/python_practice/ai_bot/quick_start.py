#!/usr/bin/env python3
"""
GGPRAO AI Chat - Quick Start Launcher
Automatically detects best available solution and launches it

Usage: python quick_start.py
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 18 + "GGPRAO AI CHAT - QUICK START" + " " * 22 + "║")
    print("╚" + "=" * 68 + "╝\n")

    # Test what's available
    print("Analyzing your system...\n")

    # Check for pure Python web app
    try:
        from http.server import HTTPServer
        import json
        pure_python_available = True
        print("✅ Pure Python web app: AVAILABLE")
    except ImportError:
        pure_python_available = False
        print("❌ Pure Python web app: NOT AVAILABLE")

    # Check for Streamlit
    try:
        import streamlit
        streamlit_available = True
        print("✅ Streamlit: AVAILABLE")
    except ImportError as e:
        streamlit_available = False
        if "DLL load failed" in str(e):
            print("🔒 Streamlit: BLOCKED (PyArrow DLL issue)")
        else:
            print("❌ Streamlit: NOT INSTALLED")

    # Check for Flask
    try:
        import flask
        flask_available = True
        print("✅ Flask: AVAILABLE")
    except ImportError:
        flask_available = False
        print("❌ Flask: NOT AVAILABLE")

    print("\n" + "=" * 70 + "\n")

    # Launch best option
    if pure_python_available:
        print("🚀 Launching Pure Python Web App (Recommended)\n")
        print("This requires NO external dependencies!")
        print("Starting server...\n")

        try:
            os.system("python simple_web_app.py")
        except KeyboardInterrupt:
            print("\n✅ Application closed")
            return 0

    elif streamlit_available:
        print("🚀 Launching Streamlit\n")

        try:
            os.system("python -m streamlit run chatgpt_ui.py")
        except KeyboardInterrupt:
            print("\n✅ Application closed")
            return 0

    elif flask_available:
        print("🚀 Launching Flask Alternative\n")

        try:
            os.system("python app_flask_alternative.py")
        except KeyboardInterrupt:
            print("\n✅ Application closed")
            return 0

    else:
        print("❌ No suitable framework available\n")
        print("Available options:")
        print("1. python diagnose_system.py (Run diagnostic)")
        print("2. python ultimate_pyarrow_fix.py (Try to fix Streamlit)")
        print("3. Use WSL: wsl python -m streamlit run chatgpt_ui.py")
        return 1

if __name__ == '__main__':
    sys.exit(main())

