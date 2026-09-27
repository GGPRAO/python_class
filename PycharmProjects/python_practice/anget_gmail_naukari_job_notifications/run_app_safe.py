#!/usr/bin/env python3
"""
Dependency installer and launcher for ChatGPT-Like Email Assistant
"""

import subprocess
import sys
import os

def install_requirements():
    """Install all required packages."""
    requirements = [
        'streamlit==1.28.1',
        'flask==2.3.2',
        'flask-cors==4.0.0',
        'google-auth-oauthlib==1.1.0',
        'google-auth-httplib2==0.2.0',
        'google-api-python-client==2.100.0',
        'ollama==0.1.0',
        'beautifulsoup4==4.12.2',
        'lxml==4.9.3',
        'requests==2.31.0',
        'python-dotenv==1.0.0'
    ]

    print("Installing dependencies...")
    for package in requirements:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

    print("All dependencies installed!")

def verify_imports():
    """Verify all critical imports work."""
    critical_packages = ['flask', 'flask_cors', 'google.auth', 'bs4']

    print("\nVerifying imports...")
    for package in critical_packages:
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError as e:
            print(f"✗ {package}: {e}")
            return False

    return True

if __name__ == "__main__":
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Install requirements
    try:
        install_requirements()
    except Exception as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

    # Verify imports
    if not verify_imports():
        print("Critical imports failed!")
        sys.exit(1)

    # Launch the app
    print("\nLaunching ChatGPT-Like Email Assistant...")
    os.system('python chatgpt_like_interface.py')

