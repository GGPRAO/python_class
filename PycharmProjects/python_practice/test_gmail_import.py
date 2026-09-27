#!/usr/bin/env python3
import sys
import traceback
import os

# Add to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'anget_gmail_naukari_job_notifications'))

try:
    from gmail import get_chatbot_adapter
    adapter = get_chatbot_adapter()
    print("✅ Module import successful")
    print(f"Adapter: {adapter}")
    print(f"Adapter type: {type(adapter)}")

    # Try to get status
    status = adapter.get_status()
    print(f"\n✅ Status: {status}")

except Exception as e:
    print(f"❌ Error: {e}")
    traceback.print_exc()

