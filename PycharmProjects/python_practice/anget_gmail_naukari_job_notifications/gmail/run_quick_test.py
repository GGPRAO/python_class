#!/usr/bin/env python3
"""
Quick Gmail Module Runner
Execute this file to test and run the Gmail module immediately.
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import gmail module
# __file__ is run_quick_test.py in gmail folder
# We need to add the parent of that (the anget_gmail_naukari_job_notifications folder)
sys.path.insert(0, str(Path(__file__).parent.parent))

print("\n" + "="*70)
print("GMAIL MODULE - QUICK RUNNER")
print("="*70)

try:
    # Import the module
    print("\n1️⃣ Importing Gmail module...")
    from gmail import (
        get_chatbot_adapter,
        fetch_jobs_for_chatbot,
        get_gmail_status,
        get_gmail_options
    )
    print("✅ Module imported successfully!")

    # Create adapter
    print("\n2️⃣ Creating chatbot adapter...")
    adapter = get_chatbot_adapter()
    print("✅ Adapter created!")

    # Check status
    print("\n3️⃣ Checking Gmail status...")
    status = adapter.get_status()
    print(f"✅ Status: {status['status']}")
    print(f"   Email: {status['email']}")
    print(f"   Authenticated: {status['authenticated']}")

    # Get available options
    print("\n4️⃣ Getting available commands...")
    options = adapter.get_options()
    print(f"✅ Available commands:")
    for opt in options['options']:
        print(f"   • {opt['name']}: {opt['description']}")

    # Try to fetch jobs
    print("\n5️⃣ Fetching Naukri job emails (limit=3)...")
    result = adapter.fetch_jobs(limit=3)
    print(f"✅ Status: {result['status']}")
    print(f"   Message: {result['message']}")
    print(f"   Count: {result['count']}")

    if result['emails']:
        print(f"\n   📧 Sample emails:")
        for i, email in enumerate(result['emails'][:2], 1):
            subject = email['subject'][:60]
            print(f"      {i}. {subject}...")

    # Execute command directly
    print("\n6️⃣ Testing command execution...")
    cmd_result = adapter.execute_command('get_status')
    print(f"✅ Command executed: {cmd_result['status']}")

    print("\n" + "="*70)
    print("✅ ALL TESTS PASSED!")
    print("="*70)
    print("\n🎉 Gmail module is working correctly!")
    print("\n📝 Next steps:")
    print("   1. Read: gmail/QUICK_REFERENCE.md")
    print("   2. Use in your chatbot:")
    print("      from gmail import get_chatbot_adapter")
    print("      adapter = get_chatbot_adapter()")
    print("      result = adapter.fetch_jobs(limit=5)")
    print("\n" + "="*70 + "\n")

except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    print("\nMake sure you're running this from the anget_gmail_naukari_job_notifications directory")

except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n✨ Done!\n")

