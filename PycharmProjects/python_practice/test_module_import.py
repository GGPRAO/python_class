#!/usr/bin/env python3
"""Test if the flask-cors auto-install works"""

import sys
import os
sys.path.insert(0, 'C:\\Users\\USER\\PycharmProjects\\python_practice\\anget_gmail_naukari_job_notifications')

try:
    print("Testing import of chatgpt_web_interface...")
    import chatgpt_web_interface
    print("SUCCESS: chatgpt_web_interface imported!")
    with open('C:\\Users\\USER\\PycharmProjects\\python_practice\\import_test.log', 'w') as f:
        f.write("SUCCESS: Module imported successfully\n")
except Exception as e:
    print(f"ERROR: {e}")
    with open('C:\\Users\\USER\\PycharmProjects\\python_practice\\import_test.log', 'w') as f:
        f.write(f"ERROR: {e}\n")

