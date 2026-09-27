#!/usr/bin/env python3
"""
Direct PyArrow Fix - Unblock DLL at Windows Level
Run with: python fix_pyarrow_dll.py
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    print("=" * 70)
    print("🔧 PyArrow DLL Windows Unblock Utility")
    print("=" * 70)

    # Find all Python installations and their pyarrow modules
    python_paths = [
        Path(sys.prefix),  # Current Python
        Path.home() / "AppData" / "Roaming" / "Python",
        Path.home() / "AppData" / "Roaming" / "Python" / "Python310",
        Path("C:/Program Files/Python310"),
        Path("C:/Program Files/Python311"),
    ]

    print("\n🔍 Searching for PyArrow installations...\n")

    found_any = False
    for python_path in python_paths:
        if not python_path.exists():
            continue

        # Look for pyarrow in site-packages
        possible_locations = [
            python_path / "Lib" / "site-packages" / "pyarrow",
            python_path / "site-packages" / "pyarrow",
            python_path / "lib" / "site-packages" / "pyarrow",
            Path("c:/users/user/appdata/roaming/python/python310/site-packages/pyarrow"),  # Explicit user path
        ]

        for pyarrow_path in possible_locations:
            if pyarrow_path.exists():
                print(f"✅ Found PyArrow at: {pyarrow_path}")
                found_any = True

                # Find all .pyd files
                pyd_files = list(pyarrow_path.rglob("*.pyd"))
                print(f"   📦 Found {len(pyd_files)} .pyd files\n")

                for pyd_file in pyd_files:
                    print(f"   Unblocking: {pyd_file.name}...", end=" ", flush=True)
                    try:
                        # Use built-in Windows unblock
                        result = subprocess.run(
                            [
                                "powershell",
                                "-NoProfile",
                                "-Command",
                                f"Unblock-File -Path '{str(pyd_file)}'",
                            ],
                            capture_output=True,
                            timeout=5,
                        )

                        if result.returncode == 0:
                            print("✅")
                        else:
                            print(f"⚠️ (code: {result.returncode})")
                            if result.stderr:
                                print(f"      Error: {result.stderr.decode()}")
                    except subprocess.TimeoutExpired:
                        print("⏱️ (timeout)")
                    except Exception as e:
                        print(f"❌ ({e})")

                print()

    if not found_any:
        print("❌ No PyArrow installations found")
        print("\nTrying to install PyArrow...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "pyarrow"],
            capture_output=False,
        )
        return result.returncode

    # Test import
    print("\n" + "=" * 70)
    print("🧪 Testing PyArrow import...")
    print("=" * 70 + "\n")

    try:
        import pyarrow as pa
        print(f"✅ SUCCESS! PyArrow {pa.__version__} imported successfully!")
        print("\nYou can now run:")
        print("  python -m streamlit run chatgpt_ui.py")
        return 0
    except ImportError as e:
        print(f"❌ PyArrow import still failing: {e}")
        print("\nTroubleshooting steps:")
        print("1. Run this script as Administrator")
        print("2. Check if Windows Defender/Antivirus is blocking PyArrow")
        print("3. Try: pip uninstall pyarrow && pip install --upgrade pyarrow --no-cache-dir")
        print("4. Check System Security Policy: gpedit.msc (Group Policy)")
        return 1

if __name__ == "__main__":
    sys.exit(main())

