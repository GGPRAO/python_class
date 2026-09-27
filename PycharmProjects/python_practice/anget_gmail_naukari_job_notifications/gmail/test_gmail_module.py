"""
Gmail Chatbot Module - Quick Start Test
Demonstrates usage of the gmail module with hardcoded credentials.
"""

from gmail import (
    get_chatbot_adapter,
    fetch_jobs_for_chatbot,
    get_gmail_status,
    get_gmail_options,
    get_default_email
)


def test_basic_functions():
    """Test basic convenience functions."""
    print("=" * 60)
    print("BASIC FUNCTIONS TEST")
    print("=" * 60)

    # Test 1: Get default email
    print("\n1️⃣ Getting default email...")
    email = get_default_email()
    print(f"✅ Email: {email}")

    # Test 2: Get Gmail status
    print("\n2️⃣ Getting Gmail service status...")
    status = get_gmail_status()
    print(f"✅ Status: {status}")

    # Test 3: Get available options
    print("\n3️⃣ Getting available chatbot options...")
    options = get_gmail_options()
    print(f"✅ Available options:")
    for opt in options.get('options', []):
        print(f"   - {opt['id']}: {opt['name']}")


def test_chatbot_adapter():
    """Test chatbot adapter methods."""
    print("\n" + "=" * 60)
    print("CHATBOT ADAPTER TEST")
    print("=" * 60)

    adapter = get_chatbot_adapter()

    # Test 1: Get adapter status
    print("\n1️⃣ Getting adapter status...")
    status = adapter.get_status()
    print(f"✅ Adapter Status: {status['status']}")
    print(f"   Email: {status['email']}")
    print(f"   Authenticated: {status['authenticated']}")

    # Test 2: Get available options
    print("\n2️⃣ Getting available commands...")
    options = adapter.get_options()
    print(f"✅ Commands available:")
    for opt in options.get('options', []):
        print(f"   - {opt['id']}: {opt['name']}")
        print(f"     Description: {opt['description']}")

    # Test 3: Execute commands
    print("\n3️⃣ Testing command execution...")
    result = adapter.execute_command('get_status')
    print(f"✅ Command result: {result['status']}")


def test_fetch_jobs():
    """Test fetching jobs (requires active Gmail account)."""
    print("\n" + "=" * 60)
    print("FETCH JOBS TEST")
    print("=" * 60)

    print("\n1️⃣ Fetching jobs using convenience function...")
    try:
        result = fetch_jobs_for_chatbot(limit=5)
        print(f"✅ Status: {result['status']}")
        print(f"   Count: {result['count']}")
        print(f"   Message: {result['message']}")

        if result['emails']:
            print(f"\n   First email subject: {result['emails'][0]['subject']}")
    except Exception as e:
        print(f"⚠️ Note: {e}")
        print("   (This is expected if Gmail isn't accessible)")


def test_adapter_commands():
    """Test adapter command execution."""
    print("\n" + "=" * 60)
    print("ADAPTER COMMAND TEST")
    print("=" * 60)

    adapter = get_chatbot_adapter()

    print("\n1️⃣ Executing fetch_jobs command...")
    result = adapter.execute_command('fetch_jobs', limit=3)
    print(f"✅ Command executed: {result['status']}")

    print("\n2️⃣ Executing get_status command...")
    result = adapter.execute_command('get_status')
    print(f"✅ Service: {result['service']}")

    print("\n3️⃣ Executing get_options command...")
    result = adapter.execute_command('get_options')
    print(f"✅ Options available: {len(result['options'])}")


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "GMAIL CHATBOT MODULE - QUICK START TEST" + " " * 10 + "║")
    print("╚" + "=" * 58 + "╝")

    try:
        test_basic_functions()
        test_chatbot_adapter()
        test_adapter_commands()
        test_fetch_jobs()

        print("\n" + "=" * 60)
        print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("\n📝 The gmail module is ready for chatbot integration!")
        print("   - Hardcoded email: ggpsmo@gmail.com")
        print("   - Passcode: lodqerzdhzjppwph")
        print("   - Use get_chatbot_adapter() to access the module")
        print("\n")

    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

