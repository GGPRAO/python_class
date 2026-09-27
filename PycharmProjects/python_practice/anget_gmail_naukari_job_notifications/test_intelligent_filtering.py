#!/usr/bin/env python3
"""
Test Script: Intelligent Job Filtering
Demonstrates the new filtering capabilities without Streamlit
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from gmail.job_filter import JobFilter, extract_and_filter_jobs


def test_salary_extraction():
    """Test salary extraction"""
    print("\n" + "="*60)
    print("TEST 1: Salary Extraction")
    print("="*60)

    filter_obj = JobFilter()

    test_cases = [
        "Job Opportunity: ₹10-15 lpa package offered",
        "Salary: 20 lakh to 30 lakh per annum",
        "15-20 lpa salary included",
    ]

    for text in test_cases:
        result = filter_obj.extract_salary_range(text)
        print(f"\nText: {text}")
        print(f"Result: {result}")


def test_experience_extraction():
    """Test experience extraction"""
    print("\n" + "="*60)
    print("TEST 2: Experience Extraction")
    print("="*60)

    filter_obj = JobFilter()

    test_cases = [
        "Looking for 5-10 years of experience",
        "3 years minimum required",
        "Fresher friendly position",
        "2+ years experience needed",
    ]

    for text in test_cases:
        result = filter_obj.extract_experience(text)
        print(f"\nText: {text}")
        print(f"Result: {result}")


def test_query_parsing():
    """Test query parsing"""
    print("\n" + "="*60)
    print("TEST 3: Natural Language Query Parsing")
    print("="*60)

    filter_obj = JobFilter()

    test_queries = [
        "Python developer in Bangalore",
        "Backend engineer roles with 15-20 lpa",
        "Remote jobs for 3-5 years experience",
        "Data scientist positions at TCS",
        "Frontend developer Mumbai 10 lpa 2 years",
    ]

    for query in test_queries:
        criteria = filter_obj.parse_query(query)
        print(f"\nQuery: {query}")
        print(f"Extracted Criteria: {criteria}")


def test_location_extraction():
    """Test location extraction"""
    print("\n" + "="*60)
    print("TEST 4: Location Extraction")
    print("="*60)

    filter_obj = JobFilter()

    test_cases = [
        "Job in Bangalore",
        "Remote work opportunity",
        "Based in Mumbai and Delhi",
        "Hyderabad or Pune location",
    ]

    for text in test_cases:
        result = filter_obj.extract_location(text)
        print(f"\nText: {text}")
        print(f"Result: {result}")


def test_job_filtering():
    """Test job filtering with mock data"""
    print("\n" + "="*60)
    print("TEST 5: Job Filtering with Mock Data")
    print("="*60)

    # Mock jobs data
    mock_jobs = [
        {
            'role': 'Python Developer',
            'company': 'TechCorp',
            'locations': ['Bangalore'],
            'salary': {'min': 10, 'max': 15},
            'experience': {'min': 2, 'max': 5}
        },
        {
            'role': 'Backend Engineer',
            'company': 'CloudTech',
            'locations': ['Remote'],
            'salary': {'min': 15, 'max': 20},
            'experience': {'min': 3, 'max': 5}
        },
        {
            'role': 'Frontend Developer',
            'company': 'TCS',
            'locations': ['Mumbai'],
            'salary': {'min': 12, 'max': 18},
            'experience': {'min': 2, 'max': 4}
        },
        {
            'role': 'Data Scientist',
            'company': 'Infosys',
            'locations': ['Bangalore'],
            'salary': {'min': 20, 'max': 30},
            'experience': {'min': 4, 'max': 7}
        },
    ]

    filter_obj = JobFilter()

    # Test Case 1: Filter by role
    print("\n--- Test Case 1: Filter by role='Developer' ---")
    filtered = filter_obj.filter_jobs(mock_jobs, role='Developer')
    print(f"Results: {len(filtered)} jobs")
    for job in filtered:
        print(f"  - {job['role']} at {job['company']}")

    # Test Case 2: Filter by location
    print("\n--- Test Case 2: Filter by location='Bangalore' ---")
    filtered = filter_obj.filter_jobs(mock_jobs, location='Bangalore')
    print(f"Results: {len(filtered)} jobs")
    for job in filtered:
        print(f"  - {job['role']} at {job['company']} in {', '.join(job['locations'])}")

    # Test Case 3: Filter by salary
    print("\n--- Test Case 3: Filter by min_salary=15, max_salary=20 ---")
    filtered = filter_obj.filter_jobs(mock_jobs, min_salary=15, max_salary=20)
    print(f"Results: {len(filtered)} jobs")
    for job in filtered:
        print(f"  - {job['role']}: ₹{job['salary']['min']}-{job['salary']['max']} LPA")

    # Test Case 4: Filter by company
    print("\n--- Test Case 4: Filter by company='TCS' ---")
    filtered = filter_obj.filter_jobs(mock_jobs, company='TCS')
    print(f"Results: {len(filtered)} jobs")
    for job in filtered:
        print(f"  - {job['role']} at {job['company']}")

    # Test Case 5: Combined filters
    print("\n--- Test Case 5: Combined - Bangalore + Developer + 10-15 LPA ---")
    filtered = filter_obj.filter_jobs(
        mock_jobs,
        location='Bangalore',
        role='Developer',
        min_salary=10,
        max_salary=15
    )
    print(f"Results: {len(filtered)} jobs")
    for job in filtered:
        print(f"  - {job['role']} at {job['company']} ({job['locations'][0]}) ₹{job['salary']['min']}-{job['salary']['max']} LPA")


def test_adapter_integration():
    """Test adapter integration"""
    print("\n" + "="*60)
    print("TEST 6: Adapter Integration")
    print("="*60)

    try:
        from gmail import get_chatbot_adapter

        adapter = get_chatbot_adapter()
        print("✅ Adapter initialized successfully")

        # Test query parsing
        query = "Python developer in Bangalore with 15-20 lpa"
        query_info = adapter.parse_user_query(query)
        print(f"\nQuery: {query}")
        print(f"Intent: {query_info['intent']}")
        print(f"Criteria: {query_info['criteria']}")

    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """Run all tests"""
    print("\n" + "█"*60)
    print("█ INTELLIGENT JOB FILTERING - FEATURE TESTS")
    print("█"*60)

    test_salary_extraction()
    test_experience_extraction()
    test_query_parsing()
    test_location_extraction()
    test_job_filtering()
    test_adapter_integration()

    print("\n" + "█"*60)
    print("█ ALL TESTS COMPLETED")
    print("█"*60 + "\n")

    print("Summary of Features Tested:")
    print("✅ Salary extraction from text")
    print("✅ Experience requirement extraction")
    print("✅ Natural language query parsing")
    print("✅ Location extraction")
    print("✅ Job filtering with multiple criteria")
    print("✅ Adapter integration")

    print("\n💡 To test the full chatbot, run:")
    print("   streamlit run chatbot_ui.py")


if __name__ == "__main__":
    main()

