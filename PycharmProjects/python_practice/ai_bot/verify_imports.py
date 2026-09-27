"""
PyArrow DLL Error Fix - Run this FIRST before any other commands
This script fixes the PyArrow DLL blocking issue on Windows
"""

import os
import sys

# FIX #1: Set environment variable FIRST
os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'

# FIX #2: Add PyArrow to path if needed
try:
    import pyarrow
    print("✅ PyArrow imported successfully!")
except ImportError as e:
    print(f"❌ PyArrow import failed: {e}")
    sys.exit(1)

# FIX #3: Verify Streamlit works
try:
    import streamlit
    print("✅ Streamlit imported successfully!")
except ImportError as e:
    print(f"❌ Streamlit import failed: {e}")
    sys.exit(1)

print("\n✅ All imports successful!")
print("Now you can run: streamlit run chatgpt_ui.py")

