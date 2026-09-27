#!/usr/bin/env python3
"""Test script to verify all imports work correctly."""

import sys
print(f"Python: {sys.executable}")
print(f"Version: {sys.version}")

try:
    import flask
    print("✓ flask imported successfully")
except ImportError as e:
    print(f"✗ flask import failed: {e}")

try:
    import flask_cors
    print("✓ flask_cors imported successfully")
except ImportError as e:
    print(f"✗ flask_cors import failed: {e}")

try:
    from google.auth import oauthlib
    print("✓ google.auth imported successfully")
except ImportError as e:
    print(f"✗ google.auth import failed: {e}")

try:
    import beautifulsoup4
    print("✓ beautifulsoup4 imported successfully")
except ImportError as e:
    print(f"✗ beautifulsoup4 import failed: {e}")

print("\nAll checks complete!")

