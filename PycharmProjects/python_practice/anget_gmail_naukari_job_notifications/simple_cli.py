#!/usr/bin/env python3
"""
Simple CLI Chatbot for Gmail Naukri Jobs
Terminal-based interface, no browser needed
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from datetime import datetime

def clear_screen():
    """Clear terminal screen"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print header"""
    print("=" * 70)
    print("💼 Naukri Job Assistant - Terminal Version".center(70))
    print("=" * 70)
    print()

def print_menu():
    """Print main menu"""
    print("\n📋 Main Menu:")
    print("  1) 🔄 Fetch Jobs")
    print("  2) ℹ️  Service Status")
    print("  3) 🎛️  Available Commands")
    print("  4) ❓ Help")
    print("  5) ❌ Exit")
    print()

def fetch_jobs_menu():
    """Menu for fetching jobs"""
    try:
        print("\n🔄 Fetch Jobs")
        print("-" * 70)

        limit_input = input("How many emails to fetch? (1-20, default 5): ").strip()
        limit = int(limit_input) if limit_input else 5

        if not 1 <= limit <= 20:
            print("❌ Limit must be between 1 and 20")
            return

        print(f"\n⏳ Fetching {limit} emails from Gmail...")

        from gmail import get_chatbot_adapter
        adapter = get_chatbot_adapter()
        result = adapter.fetch_jobs(limit=limit)

        if result['status'] == 'success':
            print(f"\n✅ Success! Found {result['count']} jobs:\n")

            for idx, job in enumerate(result['emails'], 1):
                print(f"\n{'─' * 70}")
                print(f"📧 Job #{idx}")
                print(f"{'─' * 70}")
                print(f"Subject: {job.get('subject', 'No Subject')}")
                print()

                body = job.get('body', 'No content')
                # Show first 500 chars
                if len(body) > 500:
                    print(f"Body: {body[:500]}...")
                    print("\n[Content truncated - see full email for more]")
                else:
                    print(f"Body: {body}")

            print(f"\n{'═' * 70}")
            print(f"Total: {result['count']} jobs found")
            print(f"{'═' * 70}")
        else:
            print(f"\n❌ {result.get('message', 'Error fetching jobs')}")

    except ValueError:
        print("❌ Please enter a valid number")
    except Exception as e:
        print(f"❌ Error: {e}")

def check_status():
    """Check service status"""
    try:
        print("\nℹ️  Service Status")
        print("-" * 70)

        from gmail import get_chatbot_adapter
        adapter = get_chatbot_adapter()
        status = adapter.get_status()

        print(f"\n📧 Email:          {status.get('email', 'N/A')}")
        print(f"🔗 Service:        {status.get('service', 'N/A')}")
        print(f"🔓 Authenticated:  {'✅ Yes' if status.get('authenticated') else '❌ No'}")
        print(f"✨ Available:      {'✅ Yes' if status.get('available') else '❌ No'}")
        print()

    except Exception as e:
        print(f"❌ Error: {e}")

def show_commands():
    """Show available commands"""
    try:
        print("\n🎛️  Available Commands")
        print("-" * 70)

        from gmail import get_chatbot_adapter
        adapter = get_chatbot_adapter()
        options = adapter.get_options()

        for idx, cmd in enumerate(options.get('options', []), 1):
            print(f"\n{idx}. {cmd['name']}")
            print(f"   ID: {cmd['id']}")
            print(f"   Description: {cmd['description']}")

            if cmd.get('parameters'):
                print("   Parameters:")
                for param, details in cmd['parameters'].items():
                    print(f"     - {param} ({details.get('type', 'any')}): {details.get('description', 'N/A')}")

        print()

    except Exception as e:
        print(f"❌ Error: {e}")

def show_help():
    """Show help information"""
    print("\n❓ Help & Information")
    print("-" * 70)
    print("""
This is a simple terminal-based Gmail Naukri Job chatbot.

Features:
  ✅ Fetch latest job notifications
  ✅ Check service status
  ✅ View available commands
  ✅ Display job details
  ✅ No browser needed

How to use:
  1. Select "Fetch Jobs" from main menu
  2. Enter number of emails to fetch
  3. View job details in terminal
  4. Go back to menu for more options

Credentials:
  Email: ggpsmo@gmail.com
  (Password is hardcoded in gmail_config.py)

Tips:
  • Limit is 1-20 emails per fetch
  • First fetch might take a moment
  • Ctrl+C to exit anytime

Need more help?
  See: CHATBOT_SETUP_GUIDE.md
       SIMPLE_CHATBOT_SETUP.md
       gmail/README.md
""")

def main():
    """Main loop"""
    try:
        while True:
            clear_screen()
            print_header()

            print("ℹ️  This is a terminal-based chatbot UI")
            print("📧 Email: ggpsmo@gmail.com (hardcoded)")
            print()

            print_menu()
            choice = input("👉 Enter your choice (1-5): ").strip()

            if choice == '1':
                fetch_jobs_menu()
                input("\nPress Enter to continue...")

            elif choice == '2':
                check_status()
                input("\nPress Enter to continue...")

            elif choice == '3':
                show_commands()
                input("\nPress Enter to continue...")

            elif choice == '4':
                clear_screen()
                show_help()
                input("Press Enter to continue...")

            elif choice == '5':
                print("\n👋 Goodbye!\n")
                break

            else:
                print("\n❌ Invalid choice. Please enter 1-5.")
                input("Press Enter to continue...")

    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

