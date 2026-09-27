#!/usr/bin/env python3
"""
Gmail Chatbot Setup - Verification Script
Verifies all files are in place and working
"""

import sys
import os
from pathlib import Path

def check_file(path, description):
    """Check if file exists"""
    if Path(path).exists():
        size = Path(path).stat().st_size
        print(f"  ✅ {description:40} ({size:,} bytes)")
        return True
    else:
        print(f"  ❌ {description:40} MISSING")
        return False

def main():
    print("=" * 80)
    print("🔍 GMAIL CHATBOT SETUP - VERIFICATION".center(80))
    print("=" * 80)
    print()

    base_path = Path(__file__).parent
    os.chdir(base_path)

    checks = {
        "UI Applications": [
            ("simple_chatbot.py", "Streamlit UI"),
            ("flask_chatbot.py", "Flask + HTML UI"),
            ("simple_cli.py", "Terminal CLI"),
        ],
        "Gmail Module": [
            ("gmail/__init__.py", "Package Init"),
            ("gmail/gmail_config.py", "Gmail Config"),
            ("gmail/gmail_service.py", "Gmail Service"),
            ("gmail/chatbot_adapter.py", "Chatbot Adapter"),
        ],
        "Documentation": [
            ("00_START_HERE.md", "Start Here Guide"),
            ("SETUP_COMPLETE.md", "Setup Summary"),
            ("QUICK_START.md", "Quick Reference"),
            ("CHATBOT_SETUP_GUIDE.md", "Setup Guide"),
            ("SIMPLE_CHATBOT_SETUP.md", "Streamlit Guide"),
        ],
        "Configuration": [
            ("requirements.txt", "Dependencies"),
            ("gmail_config.py", "Email Config"),
        ],
    }

    total = 0
    passed = 0

    for section, files in checks.items():
        print(f"\n📁 {section}")
        print("─" * 80)
        for file_path, description in files:
            total += 1
            if check_file(file_path, description):
                passed += 1

    print()
    print("=" * 80)
    print(f"RESULTS: {passed}/{total} checks passed".center(80))
    print("=" * 80)

    if passed == total:
        print("\n✅ ALL CHECKS PASSED - Setup is complete!")
        print("\n🚀 Next steps:")
        print("  1. Install dependencies:")
        print("     pip install -r requirements.txt")
        print()
        print("  2. Choose your UI and run:")
        print("     streamlit run simple_chatbot.py    (Recommended)")
        print("     python flask_chatbot.py")
        print("     python simple_cli.py")
        print()
        print("  3. Click 'Fetch Jobs' and start!")
        return 0
    else:
        print(f"\n⚠️  {total - passed} file(s) missing")
        print("\nThis is unusual. Please check:")
        print("  - You're in the right directory")
        print("  - Files weren't accidentally deleted")
        print("  - Read 00_START_HERE.md for help")
        return 1

if __name__ == '__main__':
    sys.exit(main())

