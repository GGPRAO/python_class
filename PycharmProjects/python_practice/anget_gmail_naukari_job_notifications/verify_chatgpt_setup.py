#!/usr/bin/env python3
"""
ChatGPT-Like Email Assistant - Installation Verification
Checks if everything is installed and configured correctly
"""

import sys
import os
from pathlib import Path

# Colors for output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_header():
    """Print header."""
    print("\n" + "="*70)
    print(f"{Colors.BOLD}{Colors.OKBLUE}ChatGPT-Like Email Assistant - Verification{Colors.ENDC}")
    print("="*70 + "\n")


def check_python():
    """Check Python version."""
    version = sys.version_info
    print(f"{Colors.OKBLUE}1. Checking Python version...{Colors.ENDC}")

    if version.major == 3 and version.minor >= 8:
        print(f"   {Colors.OKGREEN}✅ Python {version.major}.{version.minor}.{version.micro}{Colors.ENDC}")
        return True
    else:
        print(f"   {Colors.FAIL}❌ Python {version.major}.{version.minor} (require 3.8+){Colors.ENDC}")
        return False


def check_pip():
    """Check pip is available."""
    print(f"\n{Colors.OKBLUE}2. Checking pip...{Colors.ENDC}")
    try:
        import pip
        print(f"   {Colors.OKGREEN}✅ pip is installed{Colors.ENDC}")
        return True
    except ImportError:
        print(f"   {Colors.FAIL}❌ pip is not installed{Colors.ENDC}")
        return False


def check_dependencies():
    """Check required packages."""
    print(f"\n{Colors.OKBLUE}3. Checking required packages...{Colors.ENDC}")

    required = {
        'flask': 'Flask',
        'requests': 'Requests',
        'beautifulsoup4': 'BeautifulSoup4',
    }

    all_ok = True
    for module, name in required.items():
        try:
            __import__(module)
            print(f"   {Colors.OKGREEN}✅ {name}{Colors.ENDC}")
        except ImportError:
            print(f"   {Colors.FAIL}❌ {name} (not installed){Colors.ENDC}")
            all_ok = False

    return all_ok


def check_files():
    """Check if main files exist."""
    print(f"\n{Colors.OKBLUE}4. Checking main files...{Colors.ENDC}")

    files = [
        ('chatgpt_like_interface.py', 'CLI Interface'),
        ('chatgpt_web_interface.py', 'Web Interface'),
        ('gmail/chatbot_adapter.py', 'Email Adapter'),
        ('gmail/job_filter.py', 'Job Filter'),
        ('requirements.txt', 'Dependencies'),
    ]

    all_ok = True
    for filename, description in files:
        path = Path(__file__).parent / filename
        if path.exists():
            print(f"   {Colors.OKGREEN}✅ {description}{Colors.ENDC}")
        else:
            print(f"   {Colors.FAIL}❌ {description} (not found){Colors.ENDC}")
            all_ok = False

    return all_ok


def check_gmail_module():
    """Check if Gmail module is importable."""
    print(f"\n{Colors.OKBLUE}5. Checking Gmail module...{Colors.ENDC}")

    sys.path.insert(0, str(Path(__file__).parent))

    try:
        from gmail import get_chatbot_adapter
        print(f"   {Colors.OKGREEN}✅ Gmail module is working{Colors.ENDC}")
        return True
    except Exception as e:
        print(f"   {Colors.FAIL}❌ Gmail module error: {str(e)[:50]}{Colors.ENDC}")
        return False


def check_env():
    """Check if .env file exists."""
    print(f"\n{Colors.OKBLUE}6. Checking environment configuration...{Colors.ENDC}")

    env_file = Path(__file__).parent / '.env'
    if env_file.exists():
        print(f"   {Colors.OKGREEN}✅ .env file found{Colors.ENDC}")
        return True
    else:
        print(f"   {Colors.WARNING}⚠️  .env file not found (optional){Colors.ENDC}")
        print(f"      You can create one with:")
        print(f"      GMAIL_USER=your_email@gmail.com")
        print(f"      GMAIL_PASSWORD=your_app_password")
        return None  # Optional


def print_summary(results):
    """Print verification summary."""
    print("\n" + "="*70)
    print(f"{Colors.BOLD}Verification Summary:{Colors.ENDC}")
    print("="*70 + "\n")

    total = len(results)
    passed = sum(1 for r in results.values() if r is True)
    warnings = sum(1 for r in results.values() if r is None)
    failed = sum(1 for r in results.values() if r is False)

    for check, result in results.items():
        if result is True:
            status = f"{Colors.OKGREEN}✅ PASS{Colors.ENDC}"
        elif result is False:
            status = f"{Colors.FAIL}❌ FAIL{Colors.ENDC}"
        else:
            status = f"{Colors.WARNING}⚠️  WARNING{Colors.ENDC}"
        print(f"  {status} - {check}")

    print("\n" + "="*70)

    if failed == 0:
        if warnings == 0:
            print(f"{Colors.OKGREEN}{Colors.BOLD}✅ ALL CHECKS PASSED!{Colors.ENDC}")
            print(f"\nYou're ready to use the ChatGPT-Like Email Assistant!")
            print(f"\nTo start:")
            print(f"  python chatgpt_like_interface.py")
            return True
        else:
            print(f"{Colors.OKGREEN}{Colors.BOLD}✅ READY TO USE (with warnings){Colors.ENDC}")
            print(f"\nYou can still use the assistant.")
            return True
    else:
        print(f"{Colors.FAIL}{Colors.BOLD}❌ SOME CHECKS FAILED{Colors.ENDC}")
        print(f"\nPlease fix the issues above and try again.")
        print(f"\nTo install dependencies:")
        print(f"  pip install -r requirements.txt")
        return False


def main():
    """Run all checks."""
    print_header()

    results = {
        'Python Version': check_python(),
        'pip Package Manager': check_pip(),
        'Required Packages': check_dependencies(),
        'Main Files': check_files(),
        'Gmail Module': check_gmail_module(),
        'Environment Config': check_env(),
    }

    success = print_summary(results)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Verification cancelled by user{Colors.ENDC}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.FAIL}Error during verification: {str(e)}{Colors.ENDC}\n")
        sys.exit(1)

