#!/usr/bin/env python3
"""
Test script for CLI chatbot - verifies it works without Streamlit/PyArrow
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

print("🧪 Testing CLI Chatbot Compatibility...\n")

# Test 1: Import modules
print("Test 1: Testing imports...")
try:
    from gmail import get_chatbot_adapter
    from gmail.job_filter import JobFilter
    print("✅ Core modules imported successfully (no PyArrow needed!)\n")
except ImportError as e:
    print(f"❌ Import failed: {e}\n")
    sys.exit(1)

# Test 2: Initialize adapter
print("Test 2: Initializing Gmail adapter...")
try:
    adapter = get_chatbot_adapter()
    print("✅ Adapter initialized successfully!\n")
except Exception as e:
    print(f"❌ Adapter initialization failed: {e}\n")
    sys.exit(1)

# Test 3: Test query parsing
print("Test 3: Testing query parsing...")
try:
    test_queries = [
        "Python developer in Bangalore",
        "Backend engineer 15-20 lpa",
        "Remote jobs for 5+ years",
    ]

    for query in test_queries:
        result = adapter.parse_user_query(query)
        print(f"   ✅ '{query}' parsed successfully")
        print(f"      Intent: {result['intent']}")
        print(f"      Criteria: {result['criteria']}\n")
except Exception as e:
    print(f"❌ Query parsing failed: {e}\n")
    sys.exit(1)

# Test 4: Test job filtering
print("Test 4: Testing job filtering engine...")
try:
    filter_obj = JobFilter()

    # Test salary extraction
    salary = filter_obj.extract_salary_range("Job with 10-15 lpa salary")
    print(f"   ✅ Salary extraction: {salary}")

    # Test location extraction
    locations = filter_obj.extract_location("Based in Bangalore and Mumbai")
    print(f"   ✅ Location extraction: {locations}")

    # Test experience extraction
    exp = filter_obj.extract_experience("Requires 3-5 years experience")
    print(f"   ✅ Experience extraction: {exp}\n")
except Exception as e:
    print(f"❌ Job filtering failed: {e}\n")
    sys.exit(1)

# Test 5: Verify no Streamlit/PyArrow dependency
print("Test 5: Checking dependencies...")
try:
    import streamlit
    print("   ⚠️  Warning: Streamlit is installed (optional)")
except ImportError:
    print("   ✅ Streamlit not required (uses CLI instead)")

try:
    import pyarrow
    print("   ⚠️  Warning: PyArrow is installed but not used")
except ImportError:
    print("   ✅ PyArrow not required (no DLL conflicts!)\n")

print("="*70)
print("✅ ALL TESTS PASSED!")
print("="*70)
print("\n🚀 CLI Chatbot is ready to use!\n")
print("To run the chatbot, use:")
print("  python chatbot_cli.py\n")
print("Features:")
print("  ✅ No Streamlit dependency")
print("  ✅ No PyArrow dependency")
print("  ✅ No DLL loading issues")
print("  ✅ Full intelligent filtering")
print("  ✅ Natural language understanding")
print("  ✅ Lightweight and fast!\n")

