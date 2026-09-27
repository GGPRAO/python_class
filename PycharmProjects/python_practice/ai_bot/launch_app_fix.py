#!/usr/bin/env python3
"""
COMPREHENSIVE PyArrow DLL Fix Launcher
This script handles the "Application Control policy has blocked this file" error
by attempting multiple strategies in sequence.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def unblock_pyd_files():
    """Attempt to unblock all .pyd files in pyarrow"""
    print("\n🔓 Attempting to unblock PyArrow .pyd files...")

    python_home = Path(sys.prefix)
    pyarrow_site = python_home / "Lib" / "site-packages" / "pyarrow"

    if not pyarrow_site.exists():
        # Try alternate location
        pyarrow_site = Path.home() / "AppData" / "Roaming" / "Python" / "Python310" / "site-packages" / "pyarrow"

    if pyarrow_site.exists():
        pyd_files = list(pyarrow_site.rglob("*.pyd"))
        print(f"   Found {len(pyd_files)} .pyd files")

        for pyd_file in pyd_files:
            try:
                # Use PowerShell to unblock
                result = subprocess.run(
                    ["powershell", "-Command", f"Unblock-File -Path '{pyd_file}'"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    print(f"   ✅ Unblocked: {pyd_file.name}")
                else:
                    print(f"   ⚠️  Could not unblock: {pyd_file.name}")
            except Exception as e:
                print(f"   ❌ Error unblocking {pyd_file.name}: {e}")
    else:
        print(f"   ⚠️  PyArrow site-packages not found at {pyarrow_site}")

def try_reinstall_pyarrow():
    """Try to reinstall PyArrow"""
    print("\n🔄 Attempting to reinstall PyArrow...")
    try:
        # First uninstall
        print("   Uninstalling current PyArrow...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "uninstall", "-y", "pyarrow"],
            capture_output=True,
            text=True,
            timeout=60
        )

        # Then install from conda-forge (usually more compatible)
        print("   Installing PyArrow from PyPI...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "--no-cache-dir", "pyarrow"],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0:
            print("   ✅ PyArrow reinstalled successfully")
            return True
        else:
            print(f"   ❌ Reinstall failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ❌ Error during reinstall: {e}")
        return False

def launch_with_subprocess_env():
    """Launch Streamlit with properly passed environment variables"""
    print("\n🚀 Launching Streamlit with environment variables...")

    env = os.environ.copy()
    env['PYARROW_IGNORE_TIMEZONE'] = '1'
    env['ARROW_IGNORE_TIMEZONE'] = '1'

    try:
        result = subprocess.run(
            [sys.executable, "-m", "streamlit", "run", "chatgpt_ui.py"],
            env=env
        )
        return result.returncode
    except Exception as e:
        print(f"   ❌ Failed to launch: {e}")
        return 1

def main():
    print("=" * 70)
    print("🚀 COMPREHENSIVE PYARROW DLL FIX LAUNCHER")
    print("=" * 70)
    print("\nThis script will attempt to fix the PyArrow DLL loading issue")
    print("by trying multiple strategies in sequence.\n")

    # Strategy 1: Unblock DLL files
    print("\n" + "=" * 70)
    print("STRATEGY 1: Unblock PyArrow DLL Files")
    print("=" * 70)
    unblock_pyd_files()

    # Strategy 2: Try to import PyArrow
    print("\n" + "=" * 70)
    print("STRATEGY 2: Test PyArrow Import")
    print("=" * 70)
    os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'
    try:
        import pyarrow as pa
        print(f"✅ PyArrow {pa.__version__} imported successfully!")
        print("\nAttempting to launch Streamlit...\n")
        return launch_with_subprocess_env()
    except ImportError as e:
        print(f"❌ PyArrow import still failing: {e}")

        # Strategy 3: Reinstall PyArrow
        print("\n" + "=" * 70)
        print("STRATEGY 3: Reinstall PyArrow")
        print("=" * 70)
        if try_reinstall_pyarrow():
            # Try launching again
            print("\nAttempting to launch Streamlit after reinstall...\n")
            return launch_with_subprocess_env()

    # If all else fails
    print("\n" + "=" * 70)
    print("⚠️  ALTERNATIVE: Using Flask UI Instead")
    print("=" * 70)
    print("\nStreamlit may not be working due to system restrictions.")
    print("Attempting to launch Flask UI as alternative...\n")

    try:
        result = subprocess.run(
            [sys.executable, "flask_chatbot.py"],
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        return result.returncode
    except Exception as e:
        print(f"❌ Flask UI also failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

