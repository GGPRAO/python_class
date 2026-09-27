#!/usr/bin/env python3
"""
Diagnostic script to verify your ChatGPT UI setup
Run this to troubleshoot any issues
"""

import sys
import subprocess
import socket
from pathlib import Path

def print_header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def print_result(check_name, status, details=""):
    icon = "✅" if status else "❌"
    print(f"{icon} {check_name}")
    if details:
        print(f"   {details}")

def check_python():
    print_header("1. Python Check")
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    status = sys.version_info >= (3, 7)
    print_result("Python Version", status, f"Found: Python {version}")
    return status

def check_package(package_name, import_name=None):
    try:
        if import_name is None:
            import_name = package_name
        __import__(import_name)
        return True
    except ImportError:
        return False

def check_dependencies():
    print_header("2. Dependencies Check")

    deps = [
        ("ollama", "ollama"),
        ("Flask", "flask"),
    ]

    results = {}
    for package, import_name in deps:
        found = check_package(package, import_name)
        results[package] = found
        print_result(f"{package}", found, "Installed" if found else "NOT installed")

    return all(results.values())

def check_ollama_service():
    print_header("3. Ollama Service Check")

    try:
        import ollama
        # Try to get available models
        models = ollama.list()
        print_result("Ollama Connection", True, "Connected successfully")

        # Check for qwen2 model
        model_names = [m['name'] for m in models.get('models', [])]
        has_qwen = any('qwen' in name for name in model_names)

        print_result("Models Available", len(model_names) > 0, f"Found {len(model_names)} models")
        print_result("Qwen2 Model", has_qwen, f"Models: {', '.join(model_names[:3])}")

        return True
    except Exception as e:
        print_result("Ollama Connection", False, str(e))
        return False

def check_port(port=5000):
    print_header("4. Port Availability Check")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        sock.close()

        if result == 0:
            print_result(f"Port {port}", False, "Port is already in use!")
            return False
        else:
            print_result(f"Port {port}", True, "Port is available")
            return True
    except Exception as e:
        print_result(f"Port {port}", False, str(e))
        return False

def check_files():
    print_header("5. Required Files Check")

    required_files = [
        'simple_http_ui.py',
        'chatgpt_ui.html',
        'flask_chatgpt_ui.py',
        'test_agent.py',
    ]

    script_dir = Path(__file__).parent.resolve()
    all_found = True

    for filename in required_files:
        filepath = script_dir / filename
        found = filepath.exists()
        all_found = all_found and found
        print_result(f"File: {filename}", found, f"Location: {filepath}")

    return all_found

def test_chat():
    print_header("6. Chat Function Test")

    try:
        import ollama
        response = ollama.chat(
            model="qwen2:1.5b",
            messages=[{"role": "user", "content": "Say 'Hello from diagnostic test' and nothing else"}],
            stream=False
        )
        print_result("Chat Test", True, f"Response: {response['message']['content'][:50]}...")
        return True
    except Exception as e:
        print_result("Chat Test", False, str(e))
        return False

def show_next_steps():
    print_header("Next Steps")
    print("""
If all checks passed ✅:
  1. Run: python simple_http_ui.py
  2. Open: http://localhost:5000
  3. Start chatting!

If Ollama Connection failed ❌:
  1. Download Ollama: https://ollama.ai
  2. Install and run: ollama serve
  3. Download model: ollama pull qwen2:1.5b
  4. Run diagnostic again

If Dependencies Failed ❌:
  pip install ollama flask

If Port Already in Use ❌:
  Edit simple_http_ui.py:
  Change: PORT = 5000
  To: PORT = 5001 (or another number)

For more help:
  See: SETUP_GUIDE.md
  See: QUICK_START.txt
""")

def main():
    print("\n" + "🔍 "*20)
    print("  CHATGPT UI - DIAGNOSTIC TEST")
    print("🔍 "*20)

    results = []

    # Run all checks
    results.append(("Python", check_python()))
    results.append(("Dependencies", check_dependencies()))
    results.append(("Files", check_files()))
    results.append(("Port", check_port()))

    # Try Ollama and Chat only if dependencies are OK
    if results[1][1]:  # If dependencies passed
        results.append(("Ollama", check_ollama_service()))
        if results[-1][1]:  # If Ollama passed
            results.append(("Chat", test_chat()))

    # Summary
    print_header("SUMMARY")
    for check_name, passed in results:
        icon = "✅" if passed else "❌"
        print(f"{icon} {check_name}")

    # Final verdict
    all_passed = all(result[1] for result in results)
    print("\n" + "="*60)
    if all_passed:
        print("✅ ALL CHECKS PASSED - Your system is ready!")
    else:
        print("❌ Some checks failed - See recommendations below")
    print("="*60)

    show_next_steps()

if __name__ == "__main__":
    main()

