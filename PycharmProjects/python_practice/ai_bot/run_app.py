#!/usr/bin/env python3
"""
PyArrow-Safe Launcher using subprocess module
"""
import os
import subprocess
import sys
from pathlib import Path

def main():
    env = os.environ.copy()
    env['PYARROW_IGNORE_TIMEZONE'] = '1'
    env['ARROW_IGNORE_TIMEZONE'] = '1'
    
    # Try streamlit
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'chatgpt_ui.py'], env=env)
    except Exception as e:
        print(f"Streamlit failed: {e}")
        print("\nTrying Flask alternative...")
        try:
            subprocess.run([sys.executable, 'app_flask_alternative.py'], env=env)
        except Exception as e2:
            print(f"Flask also failed: {e2}")
            print("\nPlease run this from within the ai_bot directory")

if __name__ == '__main__':
    main()
