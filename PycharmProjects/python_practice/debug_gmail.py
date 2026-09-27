#!/usr/bin/env python3
"""Debug script to identify the bottleneck"""
import sys
from pathlib import Path

# Add to path
sys.path.insert(0, str(Path(__file__).parent / "anget_gmail_naukari_job_notifications"))

print("Step 1: Starting import tests...")

try:
    print("  - Importing gmail_config...")
    from gmail.gmail_config import GmailConfig
    print("    ✅ Success")
except Exception as e:
    print(f"    ❌ Failed: {e}")
    sys.exit(1)

try:
    print("  - Importing gmail_service...")
    from gmail.gmail_service import GmailService
    print("    ✅ Success")
except Exception as e:
    print(f"    ❌ Failed: {e}")
    sys.exit(1)

try:
    print("  - Importing chatbot_adapter...")
    from gmail.chatbot_adapter import GmailChatbotAdapter
    print("    ✅ Success")
except Exception as e:
    print(f"    ❌ Failed: {e}")
    sys.exit(1)

print("\nStep 2: Testing instantiation...")

try:
    print("  - Creating GmailService (this connects to Gmail)...")
    service = GmailService()
    print("    ✅ Service created")
except Exception as e:
    print(f"    ⚠️  Service creation issue (expected if Gmail unavailable): {e}")

try:
    print("  - Creating GmailChatbotAdapter...")
    adapter = GmailChatbotAdapter()
    print("    ✅ Adapter created")
except Exception as e:
    print(f"    ⚠️  Adapter creation issue: {e}")

print("\n✅ Debug complete!")

