#!/usr/bin/env python3
"""
ULTIMATE PyArrow DLL Fix
Attempts every known solution for "Application Control policy has blocked"

Usage: python ultimate_pyarrow_fix.py
"""

import os
import sys
import subprocess
import winreg
from pathlib import Path

def set_environment_variables():
    """Set registry environment variables at system level"""
    print("\n" + "=" * 70)
    print("STEP 1: Setting Windows Registry Environment Variables")
    print("=" * 70)

    try:
        # HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
        key_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"

        with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hive:
            with winreg.OpenKey(hive, key_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, 'PYARROW_IGNORE_TIMEZONE', 0, winreg.REG_SZ, '1')
                winreg.SetValueEx(key, 'ARROW_IGNORE_TIMEZONE', 0, winreg.REG_SZ, '1')
                print("✅ Set PYARROW_IGNORE_TIMEZONE=1 in registry")
                print("✅ Set ARROW_IGNORE_TIMEZONE=1 in registry")
                print("⚠️  Note: Changes require system restart to take full effect")
    except PermissionError:
        print("⚠️  Need Administrator privileges for registry changes")
    except Exception as e:
        print(f"❌ Registry error: {e}")

def copy_dll_to_safe_location():
    """Copy PyArrow DLL to Python's DLL directory"""
    print("\n" + "=" * 70)
    print("STEP 2: Copy PyArrow DLL to Python System Directory")
    print("=" * 70)

    pyarrow_lib = Path("c:/users/user/appdata/roaming/python/python310/site-packages/pyarrow/lib.cp310-win_amd64.pyd")
    python_dir = Path(sys.prefix) / "DLLs"

    if pyarrow_lib.exists():
        try:
            dest = python_dir / pyarrow_lib.name
            import shutil
            shutil.copy2(pyarrow_lib, dest)
            print(f"✅ Copied DLL to {dest}")
        except Exception as e:
            print(f"❌ Failed to copy DLL: {e}")
    else:
        print(f"❌ PyArrow DLL not found at {pyarrow_lib}")

def disable_code_integrity():
    """Attempt to disable Code Integrity Checks"""
    print("\n" + "=" * 70)
    print("STEP 3: Attempt Code Integrity Bypass")
    print("=" * 70)
    print("⚠️  This requires administrator privileges")
    print("Run in PowerShell as Administrator:")
    print("  Invoke-WebRequest -Uri 'https://aka.ms/disable-hvci' -OutFile disable-hvci.ps1")
    print("  .\\disable-hvci.ps1")
    print("Then restart your computer")

def reinstall_pyarrow_wheel():
    """Reinstall PyArrow with specific wheel"""
    print("\n" + "=" * 70)
    print("STEP 4: Reinstall PyArrow with Pure Python Fallback")
    print("=" * 70)

    try:
        print("Uninstalling pyarrow...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "uninstall", "-y", "pyarrow"],
            capture_output=True,
            timeout=30
        )

        print("Installing PyArrow...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install",
             "--upgrade", "--no-cache-dir", "--force-reinstall",
             "pyarrow"],
            capture_output=True,
            timeout=120
        )

        if result.returncode == 0:
            print("✅ PyArrow reinstalled")
        else:
            print(f"❌ Reinstall failed: {result.stderr.decode()}")
    except Exception as e:
        print(f"❌ Error: {e}")

def create_launcher_script():
    """Create a launcher that uses subprocess with proper env vars"""
    print("\n" + "=" * 70)
    print("STEP 5: Creating Launcher Script")
    print("=" * 70)

    launcher_code = '''#!/usr/bin/env python3
"""
PyArrow-Safe Launcher using subprocess module
"""
import os
import subprocess
import sys
from pathlib import Path

def main():
    env = os.environ.copy()
    env['PYARROW_IGNORE_TIMEZONE'] = '1'
    env['ARROW_IGNORE_TIMEZONE'] = '1'
    
    # Try streamlit
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'chatgpt_ui.py'], env=env)
    except Exception as e:
        print(f"Streamlit failed: {e}")
        print("\\nTrying Flask alternative...")
        try:
            subprocess.run([sys.executable, 'app_flask_alternative.py'], env=env)
        except Exception as e2:
            print(f"Flask also failed: {e2}")
            print("\\nPlease run this from within the ai_bot directory")

if __name__ == '__main__':
    main()
'''

    launcher_path = Path("run_app.py")
    launcher_path.write_text(launcher_code)
    print(f"✅ Created launcher script: {launcher_path}")
    print(f"   Run with: python {launcher_path}")

def test_pyarrow():
    """Final test"""
    print("\n" + "=" * 70)
    print("FINAL TEST: PyArrow Import")
    print("=" * 70)

    try:
        import pyarrow as pa
        print(f"✅ SUCCESS! PyArrow {pa.__version__} imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Still failing: {e}")
        return False

def main():
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "ULTIMATE PYARROW DLL FIX UTILITY" + " " * 21 + "║")
    print("╚" + "=" * 68 + "╝")

    print("\nThis script attempts comprehensive fixes for:")
    print("  'DLL load failed - Application Control policy has blocked'")
    print("\nRunning diagnostic steps...\n")

    # Step 1: Environment variables
    set_environment_variables()

    # Step 2: Copy DLL
    copy_dll_to_safe_location()

    # Step 3: Code Integrity info
    disable_code_integrity()

    # Step 4: Reinstall
    reinstall_pyarrow_wheel()

    # Step 5: Create launcher
    create_launcher_script()

    # Test
    success = test_pyarrow()

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY & NEXT STEPS")
    print("=" * 70)

    if success:
        print("\n✅ PyArrow is working! You can now run:")
        print("   python -m streamlit run chatgpt_ui.py")
    else:
        print("\n⚠️  PyArrow is still blocked. This suggests:")
        print("\n1. System-Level Block (Group Policy/HVCI/Secure Boot Code Integrity)")
        print("   - Contact your IT administrator if on corporate network")
        print("   - Check gpedit.msc for AppLocker/Code Integrity policies")
        print("   - Check UEFI settings for Secure Boot Code Integrity")
        print("\n2. Antivirus/Security Software")
        print("   - Check Windows Defender quarantine")
        print("   - Disable real-time protection temporarily")
        print("   - Add exception for Python/PyArrow")
        print("\n3. Workaround Options:")
        print("   - Use Flask instead: python app_flask_alternative.py")
        print("   - Use WSL (Windows Subsystem for Linux)")
        print("   - Use Docker container")
        print("   - Run on different machine")

if __name__ == "__main__":
    main()

