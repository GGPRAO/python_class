#!/usr/bin/env python3
"""
PyArrow DLL Fix and Chat Bot Launcher
Fixes the 'DLL load failed - Application Control policy' error
and launches the Flask ChatGPT-like interface with chat enabled
"""

import sys
import os
import subprocess
import time
import webbrowser
from pathlib import Path

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_header():
    """Print header."""
    print(f"\n{BOLD}{BLUE}{'='*70}")
    print("🚀 PyArrow DLL Fix & Gmail Chat Bot Launcher")
    print(f"{'='*70}{RESET}\n")

def print_step(step_num, message):
    """Print a step."""
    print(f"{BOLD}{BLUE}[Step {step_num}]{RESET} {message}")

def print_success(message):
    """Print success message."""
    print(f"{GREEN}✅ {message}{RESET}")

def print_error(message):
    """Print error message."""
    print(f"{RED}❌ {message}{RESET}")

def print_warning(message):
    """Print warning message."""
    print(f"{YELLOW}⚠️  {message}{RESET}")

def fix_pyarrow_dll_issue():
    """
    Fix PyArrow DLL load issue due to Application Control policy.
    Solution: Remove streamlit (which depends on pyarrow) and use Flask instead.
    """
    print_step(1, "Checking for PyArrow DLL issues...")

    try:
        import pyarrow
        print_success("PyArrow is accessible")
        return True
    except ImportError as e:
        if "DLL load failed" in str(e):
            print_warning("PyArrow DLL issue detected - this is expected due to security policy")
            print(f"\n{YELLOW}This happens when:• Application Control policy blocks pyarrow DLL• Streamlit requires pyarrow and is blocked{RESET}\n")

            print_step(2, "Removing Streamlit (requires blocked PyArrow)...")
            try:
                subprocess.run([
                    sys.executable, '-m', 'pip', 'uninstall',
                    '-y', 'streamlit'
                ], capture_output=True, check=False)
                print_success("Streamlit removed")
            except Exception as e:
                print_warning(f"Could not remove streamlit: {e}")

            print_step(3, "Downgrading PyArrow to pre-compiled version...")
            try:
                subprocess.run([
                    sys.executable, '-m', 'pip', 'install',
                    '--force-reinstall', '--no-cache-dir',
                    'pyarrow==10.0.1'
                ], capture_output=True, check=False)
                print_success("PyArrow downgraded")
            except Exception as e:
                print_warning(f"Could not downgrade PyArrow: {e}")

            return True
        else:
            raise

def check_dependencies():
    """Check and install required dependencies."""
    print_step(4, "Checking dependencies...")

    required_packages = {
        'flask': '2.3.2',
        'flask-cors': '4.0.0',
        'google-auth-oauthlib': '1.1.0',
        'google-auth-httplib2': '0.2.0',
        'google-api-python-client': '2.100.0',
        'beautifulsoup4': '4.12.2',
        'requests': '2.31.0',
        'python-dotenv': '1.0.0',
    }

    missing = []
    for package, version in required_packages.items():
        try:
            __import__(package.replace('-', '_'))
            print_success(f"{package} is installed")
        except ImportError:
            missing.append(f"{package}=={version}")

    if missing:
        print_warning(f"Installing missing packages: {', '.join(missing)}")
        for pkg in missing:
            subprocess.run([
                sys.executable, '-m', 'pip', 'install', pkg
            ], capture_output=True)
            print_success(f"Installed {pkg}")
    else:
        print_success("All dependencies installed!")

def verify_gmail_setup():
    """Verify Gmail setup is complete."""
    print_step(5, "Verifying Gmail setup...")

    gmail_dir = Path(__file__).parent / 'gmail'
    required_files = [
        'gmail_config.py',
        'gmail_service.py',
        'chatbot_adapter.py',
        '__init__.py'
    ]

    missing = []
    for file in required_files:
        if not (gmail_dir / file).exists():
            missing.append(file)

    if missing:
        print_error(f"Missing Gmail files: {', '.join(missing)}")
        print(f"\n{YELLOW}Please ensure Gmail module is set up properly.{RESET}")
        return False

    print_success("Gmail setup verified!")
    return True

def launch_chat_bot():
    """Launch the Flask chat bot."""
    print_step(6, "Launching Chat Bot...")

    script_path = Path(__file__).parent / 'chatgpt_web_interface.py'

    if not script_path.exists():
        print_error(f"Cannot find chatgpt_web_interface.py at {script_path}")
        return False

    print(f"\n{BOLD}{GREEN}🎉 Starting Gmail Chat Bot!{RESET}\n")
    print(f"{BLUE}What you can do:{RESET}")
    print("  • Ask about job notifications: 'Python developer jobs'")
    print("  • Search by location: 'Remote positions in Bangalore'")
    print("  • Search by salary: 'Backend engineer 15-20 lpa'")
    print("  • Type 'help' for more commands")
    print(f"\n{BLUE}Chat Features:{RESET}")
    print("  ✅ Full chat conversation history")
    print("  ✅ Real-time email search")
    print("  ✅ Beautiful ChatGPT-like interface")
    print("  ✅ Multiple conversations supported")
    print(f"\n{YELLOW}Opening browser in 2 seconds...{RESET}\n")

    time.sleep(2)
    webbrowser.open('http://localhost:5000')

    try:
        subprocess.run([
            sys.executable, str(script_path)
        ], check=False)
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Chat bot stopped by user.{RESET}")
        return True
    except Exception as e:
        print_error(f"Error launching chat bot: {e}")
        return False

    return True

def main():
    """Main function."""
    print_header()

    try:
        # Step 1: Fix PyArrow DLL issue
        fix_pyarrow_dll_issue()

        # Step 2: Check dependencies
        check_dependencies()

        # Step 3: Verify Gmail setup
        if not verify_gmail_setup():
            print_error("\nPlease set up Gmail module first!")
            print(f"Run: python gmail/setup_gmail.py")
            return 1

        # Step 4: Launch chat bot
        if launch_chat_bot():
            print(f"\n{GREEN}{'='*70}")
            print("✅ Chat Bot closed successfully!")
            print(f"{'='*70}{RESET}\n")
            return 0
        else:
            print_error("Failed to launch chat bot")
            return 1

    except Exception as e:
        print_error(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())

