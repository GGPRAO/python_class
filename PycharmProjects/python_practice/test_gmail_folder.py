#!/usr/bin/env python3
"""
Comprehensive Gmail Folder Fix and Test
"""
import sys
import os

# Setup path
gmail_path = os.path.join(os.path.dirname(__file__), 'anget_gmail_naukari_job_notifications')
sys.path.insert(0, gmail_path)

def test_imports():
    """Test all imports work correctly"""
    results = {}

    # Test 1: GmailConfig
    try:
        from gmail.gmail_config import GmailConfig
        results['GmailConfig'] = ('✅', GmailConfig.EMAIL)
    except Exception as e:
        results['GmailConfig'] = ('❌', str(e))

    # Test 2: GmailService
    try:
        from gmail.gmail_service import GmailService
        results['GmailService'] = ('✅', 'Imported')
    except Exception as e:
        results['GmailService'] = ('❌', str(e))

    # Test 3: ChatbotAdapter
    try:
        from gmail.chatbot_adapter import GmailChatbotAdapter
        results['GmailChatbotAdapter'] = ('✅', 'Imported')
    except Exception as e:
        results['GmailChatbotAdapter'] = ('❌', str(e))

    # Test 4: Package __init__
    try:
        from gmail import get_chatbot_adapter
        results['get_chatbot_adapter'] = ('✅', 'Imported')
    except Exception as e:
        results['get_chatbot_adapter'] = ('❌', str(e))

    return results

def test_functionality():
    """Test basic functionality"""
    results = {}

    try:
        from gmail import get_chatbot_adapter
        adapter = get_chatbot_adapter()
        results['Adapter Creation'] = ('✅', f'Type: {type(adapter).__name__}')
    except Exception as e:
        results['Adapter Creation'] = ('❌', str(e))
        return results

    # Test methods
    try:
        status = adapter.get_status()
        results['get_status()'] = ('✅', f"Status: {status.get('status', 'unknown')}")
    except Exception as e:
        results['get_status()'] = ('❌', str(e))

    try:
        options = adapter.get_options()
        results['get_options()'] = ('✅', f"Options: {len(options.get('options', []))} available")
    except Exception as e:
        results['get_options()'] = ('❌', str(e))

    return results

def main():
    print("=" * 70)
    print("GMAIL FOLDER INTEGRITY AND FUNCTIONALITY TEST")
    print("=" * 70)

    print("\n1. IMPORT TESTS")
    print("-" * 70)
    imports = test_imports()
    for module, (status, info) in imports.items():
        print(f"  {status} {module:25} {info}")

    print("\n2. FUNCTIONALITY TESTS")
    print("-" * 70)
    functionality = test_functionality()
    for test, (status, info) in functionality.items():
        print(f"  {status} {test:25} {info}")

    # Summary
    all_tests = list(imports.values()) + list(functionality.values())
    passed = sum(1 for status, _ in all_tests if status == '✅')
    total = len(all_tests)

    print("\n" + "=" * 70)
    print(f"RESULTS: {passed}/{total} tests passed")
    print("=" * 70)

    if passed == total:
        print("\n✅ GMAIL FOLDER IS FULLY OPERATIONAL!")
        return 0
    else:
        print(f"\n❌ {total - passed} test(s) failed")
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)

