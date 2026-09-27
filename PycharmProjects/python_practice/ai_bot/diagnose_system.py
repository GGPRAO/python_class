#!/usr/bin/env python3
"""
GGPRAO AI Chat - System Diagnostic Tool
Analyzes your system and recommends the best solution

Usage: python diagnose_system.py
"""

import os
import sys
import subprocess
import ctypes
from pathlib import Path

def is_admin():
    """Check if running as administrator"""
    try:
        return ctypes.windll.shell.IsUserAnAdmin()
    except:
        return False

def test_import(module_name):
    """Test if a module can be imported"""
    try:
        __import__(module_name)
        return True, None
    except ImportError as e:
        return False, str(e)
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"

def check_pyarrow_dlls():
    """Check if PyArrow DLL files exist and are accessible"""
    pyarrow_path = Path("c:/users/user/appdata/roaming/python/python310/site-packages/pyarrow")

    if not pyarrow_path.exists():
        return "NOT_FOUND", 0

    pyd_files = list(pyarrow_path.rglob("*.pyd"))
    if not pyd_files:
        return "EMPTY", 0

    accessible = 0
    for pyd_file in pyd_files:
        try:
            with open(pyd_file, 'rb'):
                accessible += 1
        except:
            pass

    return "FOUND", accessible, len(pyd_files)

def test_python_features():
    """Test if Python has required built-in features"""
    features = {
        'http.server': False,
        'json': False,
        'urllib': False,
        'threading': False,
    }

    for feature in features:
        try:
            __import__(feature)
            features[feature] = True
        except:
            features[feature] = False

    return features

def main():
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 14 + "GGPRAO AI CHAT - SYSTEM DIAGNOSTIC TOOL" + " " * 14 + "║")
    print("╚" + "=" * 68 + "╝")

    print("\n" + "=" * 70)
    print("SYSTEM INFORMATION")
    print("=" * 70)

    print(f"\n🖥️  Operating System: {sys.platform}")
    print(f"📍 Python Location: {sys.executable}")
    print(f"🐍 Python Version: {sys.version.split()[0]}")
    print(f"👤 Admin Mode: {'Yes ✅' if is_admin() else 'No ⚠️'}")
    print(f"📁 Working Directory: {os.getcwd()}")

    # Test PyArrow
    print("\n" + "=" * 70)
    print("MODULE AVAILABILITY")
    print("=" * 70)

    modules_to_test = [
        ('streamlit', 'Streamlit Web Framework'),
        ('pyarrow', 'PyArrow Data Library'),
        ('ollama', 'Ollama AI Integration'),
        ('flask', 'Flask Web Framework'),
        ('requests', 'HTTP Requests Library'),
    ]

    for module, desc in modules_to_test:
        success, error = test_import(module)
        if success:
            print(f"✅ {module:15} - {desc:30} AVAILABLE")
        else:
            if "DLL load failed" in str(error):
                print(f"🔒 {module:15} - {desc:30} BLOCKED (DLL)")
            else:
                print(f"❌ {module:15} - {desc:30} NOT INSTALLED")

    # Test built-in features
    print("\n" + "=" * 70)
    print("BUILT-IN PYTHON FEATURES")
    print("=" * 70)

    features = test_python_features()
    for feature, available in features.items():
        status = "✅" if available else "❌"
        print(f"{status} {feature:20} {'AVAILABLE' if available else 'MISSING'}")

    # Check PyArrow DLLs
    print("\n" + "=" * 70)
    print("PYARROW DLL STATUS")
    print("=" * 70)

    result = check_pyarrow_dlls()
    if result[0] == "NOT_FOUND":
        print("❌ PyArrow not installed")
    elif result[0] == "EMPTY":
        print("⚠️  PyArrow installed but no .pyd files found")
    else:
        status, accessible, total = result
        print(f"📦 PyArrow .pyd files: {total} total, {accessible} accessible")

    # Recommendations
    print("\n" + "=" * 70)
    print("RECOMMENDED SOLUTIONS")
    print("=" * 70)

    success, _ = test_import('pyarrow')
    success_streamlit, _ = test_import('streamlit')
    success_http, _ = test_import('http.server')
    admin = is_admin()

    print("\n🎯 SOLUTION RANKINGS:\n")

    if success_http and features.get('json'):
        print("1. ⭐ USE PURE PYTHON WEB APP (BEST)")
        print("   Command: python simple_web_app.py")
        print("   Pros: No admin needed, works everywhere, fast")
        print("   Opens: http://127.0.0.1:5000\n")

    if success:
        print("2. ✅ Streamlit is available!")
        print("   Command: python -m streamlit run chatgpt_ui.py")
        print("   May work, or may have DLL issues\n")
    else:
        if admin:
            print("2. ⚙️  RUN FIX UTILITY (Admin Available)")
            print("   Command: python ultimate_pyarrow_fix.py")
            print("   Then: python -m streamlit run chatgpt_ui.py\n")
        else:
            print("2. ⚠️  RUN AS ADMINISTRATOR (Requires Admin)")
            print("   Right-click Command Prompt → Run as administrator")
            print("   Then: python ultimate_pyarrow_fix.py\n")

    print("3. 🐧 USE WSL (Windows Subsystem for Linux)")
    print("   Command: wsl")
    print("   Then: python -m streamlit run chatgpt_ui.py")
    print("   Bypasses Windows DLL restrictions entirely\n")

    # Final recommendation
    print("=" * 70)
    print("FINAL RECOMMENDATION")
    print("=" * 70)

    if success_http:
        print("\n✅ RECOMMENDED: Use solution #1 - pure Python web app")
        print("   - No dependencies")
        print("   - No admin required")
        print("   - Works with all security policies")
        print("   - Fast and lightweight")
        print("\n   Quick start:")
        print("   python simple_web_app.py")
        print("   Then open: http://127.0.0.1:5000")
    elif admin:
        print("\n✅ RECOMMENDED: Run fix utility as administrator")
        print("   python ultimate_pyarrow_fix.py")
        print("   Then try: python -m streamlit run chatgpt_ui.py")
    else:
        print("\n⚠️  LIMITED OPTIONS (No Admin Access)")
        print("   1. Use pure Python solution (if http.server available)")
        print("   2. Request admin access to run fix utilities")
        print("   3. Use WSL if installed")
        print("   4. Use different machine")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    main()

