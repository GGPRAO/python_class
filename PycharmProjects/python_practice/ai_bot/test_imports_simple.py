#!/usr/bin/env python3
"""
Diagnostic Script - Test what imports work
"""

print("Testing imports...\n")

modules_to_test = [
    'flask',
    'ollama',
    'requests',
    'json',
    'sys',
    'os',
]

for module_name in modules_to_test:
    try:
        __import__(module_name)
        print(f"✅ {module_name:15} - Available")
    except ImportError as e:
        print(f"❌ {module_name:15} - Error: {e}")
    except Exception as e:
        print(f"⚠️  {module_name:15} - {type(e).__name__}: {e}")

print("\n" + "=" * 60)
print("Testing PyArrow specifically...")
try:
    import pyarrow
    print(f"✅ PyArrow imported successfully")
except Exception as e:
    print(f"❌ PyArrow failed: {e}")

print("\nDone!")

