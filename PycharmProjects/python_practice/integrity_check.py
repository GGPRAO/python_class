#!/usr/bin/env python3
"""Test script to check gmail module integrity"""
import sys
import os
from pathlib import Path

# Add the parent to path
module_dir = Path(__file__).parent / "anget_gmail_naukari_job_notifications"
sys.path.insert(0, str(module_dir))

print("=" * 60)
print("GMAIL FOLDER INTEGRITY TEST")
print("=" * 60)

# Test 1: Check file existence
print("\n1. Checking file existence...")
gmail_files = [
    "gmail/__init__.py",
    "gmail/gmail_config.py",
    "gmail/gmail_service.py",
    "gmail/chatbot_adapter.py",
]

for f in gmail_files:
    fp = module_dir / f
    exists = fp.exists()
    print(f"   {'✅' if exists else '❌'} {f}")

# Test 2: Import individual modules
print("\n2. Testing individual module imports...")
try:
    from gmail import gmail_config
    print("   ✅ gmail_config imported")
except Exception as e:
    print(f"   ❌ gmail_config: {e}")

try:
    from gmail import gmail_service
    print("   ✅ gmail_service imported")
except Exception as e:
    print(f"   ❌ gmail_service: {e}")

try:
    from gmail import chatbot_adapter
    print("   ✅ chatbot_adapter imported")
except Exception as e:
    print(f"   ❌ chatbot_adapter: {e}")

# Test 3: Import package functions
print("\n3. Testing package imports...")
try:
    from gmail import get_chatbot_adapter
    print("   ✅ get_chatbot_adapter imported")

    adapter = get_chatbot_adapter()
    print(f"   ✅ Adapter created: {type(adapter).__name__}")

except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("INTEGRITY CHECK COMPLETE")
print("=" * 60)

