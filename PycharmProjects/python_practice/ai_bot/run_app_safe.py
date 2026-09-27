#!/usr/bin/env python3
"""
PyArrow-Safe Streamlit Launcher
Run this script instead of 'streamlit run chatgpt_ui.py'
It ensures PyArrow DLL error is prevented
"""

import os
import sys
import subprocess

def main():
    print("=" * 60)
    print("🚀 PyArrow-Safe Streamlit Launcher")
    print("=" * 60)

    # Step 1: Set environment variable
    print("\n1️⃣  Setting PyArrow environment variable...")
    os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'
    print("   ✅ PYARROW_IGNORE_TIMEZONE = '1'")

    # Step 2: Verify PyArrow
    print("\n2️⃣  Verifying PyArrow can be imported...")
    try:
        import pyarrow as pa
        print(f"   ✅ PyArrow {pa.__version__} imported successfully")
    except Exception as e:
        print(f"   ❌ PyArrow import failed: {e}")
        print("\n   🔧 Troubleshooting:")
        print("   - Try: pip install --upgrade pyarrow --no-cache-dir")
        print("   - Or: conda install -c conda-forge pyarrow")
        return 1

    # Step 3: Verify Streamlit
    print("\n3️⃣  Verifying Streamlit can be imported...")
    try:
        import streamlit as st
        print(f"   ✅ Streamlit {st.__version__} imported successfully")
    except Exception as e:
        print(f"   ❌ Streamlit import failed: {e}")
        print("\n   🔧 Troubleshooting:")
        print("   - Try: pip install --upgrade streamlit --no-cache-dir")
        return 1

    # Step 4: Verify Ollama
    print("\n4️⃣  Verifying Ollama can be imported...")
    try:
        import ollama
        print(f"   ✅ Ollama imported successfully")
    except Exception as e:
        print(f"   ⚠️  Ollama import failed: {e}")
        print("   (But this might be optional)")

    # Step 5: Launch Streamlit
    print("\n5️⃣  Launching Streamlit app...")
    print("   " + "=" * 56)
    print()

    try:
        # Run streamlit with the environment variable set
        result = subprocess.run(
            [sys.executable, "-m", "streamlit", "run", "chatgpt_ui.py"],
            env={**os.environ, 'PYARROW_IGNORE_TIMEZONE': '1'}
        )
        return result.returncode
    except Exception as e:
        print(f"   ❌ Failed to launch Streamlit: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

