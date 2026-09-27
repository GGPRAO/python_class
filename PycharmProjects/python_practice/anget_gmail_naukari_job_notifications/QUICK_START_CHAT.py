#!/usr/bin/env python3
"""
🎯 QUICK START - Run Gmail Chat Bot (NO PyArrow Issues!)

This script:
1. Removes Streamlit dependency (which causes PyArrow DLL issues)
2. Sets up lightweight Flask chat bot
3. Launches the browser with full chat functionality

NO admin rights needed!
"""

import sys
import subprocess
import time
import webbrowser
from pathlib import Path

print("""
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║         🎉 Gmail Job Notifications Chat Bot - Quick Start            ║
║                                                                        ║
║  ✨ Features:                                                         ║
║     • Full chat conversation history                                  ║
║     • Real-time Gmail search                                          ║
║     • Beautiful modern UI (ChatGPT-like)                              ║
║     • NO PyArrow DLL issues!                                          ║
║     • NO Streamlit dependency!                                        ║
║     • Works on Windows with security policies                         ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
""")

def run_command(cmd, desc):
    """Run command with description."""
    print(f"\n📌 {desc}...")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            print(f"   ✅ Success")
            return True
        else:
            print(f"   ⚠️  Warning: {result.stderr[:100]}")
            return True  # Continue anyway
    except Exception as e:
        print(f"   ⚠️  {str(e)[:100]}")
        return True

def main():
    print("\n" + "="*70)
    print("SETUP STEPS")
    print("="*70)

    # Step 1: Remove Streamlit
    run_command(
        f"{sys.executable} -m pip uninstall -y streamlit",
        "Step 1: Removing Streamlit (fixes PyArrow issue)"
    )

    # Step 2: Install Flask and dependencies
    run_command(
        f"{sys.executable} -m pip install flask flask-cors",
        "Step 2: Installing Flask web framework"
    )

    # Step 3: Verify Gmail setup
    print("\n📌 Step 3: Verifying Gmail module...")
    gmail_dir = Path(__file__).parent / 'gmail'
    if (gmail_dir / '__init__.py').exists():
        print("   ✅ Gmail module found")
    else:
        print("   ⚠️  Gmail module not found - some features may be limited")

    # Step 4: Launch chat bot
    print("\n" + "="*70)
    print("LAUNCHING CHAT BOT")
    print("="*70)

    chat_script = Path(__file__).parent / 'lightweight_chat_bot.py'

    if not chat_script.exists():
        print(f"❌ Error: Cannot find {chat_script}")
        return 1

    print(f"\n✅ Starting chat bot...")
    print(f"📱 Opening browser in 3 seconds...\n")

    time.sleep(3)

    try:
        # Open browser
        webbrowser.open('http://localhost:5000')
        time.sleep(1)

        # Run chat bot
        subprocess.run([sys.executable, str(chat_script)])
    except KeyboardInterrupt:
        print("\n\n✅ Chat bot stopped by user.")
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

    print("\n" + "="*70)
    print("Thank you for using Gmail Job Chat! 👋")
    print("="*70 + "\n")
    return 0

if __name__ == '__main__':
    sys.exit(main())

