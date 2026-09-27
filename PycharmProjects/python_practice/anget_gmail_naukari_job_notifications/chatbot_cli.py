#!/usr/bin/env python3
"""
CLI Chatbot: Naukri Job Assistant v2.0
Simple command-line interface without Streamlit/PyArrow dependencies
Lightweight and fully functional!
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from gmail import get_chatbot_adapter
from datetime import datetime
import json

# Color codes for terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header():
    """Print welcome header"""
    print("\n" + "="*70)
    print(Colors.BOLD + Colors.OKBLUE +
          "💼 NAUKRI JOB ASSISTANT v2.0 - CLI Edition" +
          Colors.ENDC)
    print("="*70)
    print(Colors.OKGREEN + "✅ ChatGPT-Like Intelligent Job Search Assistant" + Colors.ENDC)
    print(Colors.OKGREEN + "✅ No Streamlit/PyArrow Limitations!" + Colors.ENDC)
    print("="*70 + "\n")


def print_help():
    """Print help information"""
    print(Colors.BOLD + "💡 AVAILABLE COMMANDS:" + Colors.ENDC)
    print("""
  help           - Show this help message
  status         - Check Gmail connection status
  examples       - Show example queries
  settings       - Show current settings
  limit <num>    - Set email search limit (1-50)
  clear          - Clear chat history
  exit/quit      - Exit the chatbot
  
  Or just type your job query naturally!
  
💬 EXAMPLE QUERIES:
  - "Python developer in Bangalore"
  - "Backend engineer 15-20 lpa"
  - "Remote jobs for 5+ years"
  - "Frontend developer at TCS"
  - "Data scientist Mumbai 20 lpa 3-5 years"
""")


def print_examples():
    """Print example queries"""
    examples = [
        ("Simple Role", "Python developer jobs"),
        ("Location Filter", "Jobs in Bangalore"),
        ("Salary Filter", "Jobs with 15-20 lpa"),
        ("Experience", "5+ years experience jobs"),
        ("Company", "TCS jobs"),
        ("Role + Location", "Backend engineer in Mumbai"),
        ("Role + Salary", "Python developer 15-20 lpa"),
        ("Remote Work", "Remote positions"),
        ("Multiple Criteria", "Python in Bangalore 15-20 lpa 3-5 years"),
        ("Complex Query", "Frontend developer remote 20 lpa 2+ years"),
    ]

    print(Colors.BOLD + "\n📚 EXAMPLE QUERIES:\n" + Colors.ENDC)
    for category, query in examples:
        print(f"  {Colors.OKCYAN}{category:20}{Colors.ENDC} → {query}")
    print()


def print_status(adapter):
    """Print connection status"""
    try:
        status = adapter.get_status()
        print(Colors.BOLD + "\n🔗 CONNECTION STATUS:\n" + Colors.ENDC)
        print(f"  Email:         {Colors.OKGREEN}{status['email']}{Colors.ENDC}")
        print(f"  Service:       {Colors.OKGREEN}{status['service']}{Colors.ENDC}")
        print(f"  Status:        {Colors.OKGREEN}{status['status'].upper()}{Colors.ENDC}")
        print(f"  Authenticated: {Colors.OKGREEN}{status['authenticated']}{Colors.ENDC}")
        print()
    except Exception as e:
        print(f"{Colors.FAIL}❌ Error: {e}{Colors.ENDC}\n")


def format_job_result(job, index):
    """Format a job result nicely"""
    result = f"\n  {Colors.BOLD}{index}. {job.get('role', 'Position Not Found')}{Colors.ENDC}\n"

    company = job.get('company', 'Unknown')
    result += f"     {Colors.OKCYAN}🏢 Company:{Colors.ENDC} {company}\n"

    locations = job.get('locations', ['Not Specified'])
    locations_str = ", ".join(locations) if isinstance(locations, list) else locations
    result += f"     {Colors.OKCYAN}📍 Location:{Colors.ENDC} {locations_str}\n"

    if job.get('salary'):
        salary = job['salary']
        result += f"     {Colors.WARNING}💰 Salary:{Colors.ENDC} ₹{salary['min']:,} - ₹{salary['max']:,} LPA\n"

    if job.get('experience'):
        exp = job['experience']
        result += f"     {Colors.WARNING}📊 Experience:{Colors.ENDC} {exp['min']}-{exp['max']} years\n"

    return result


def process_query(adapter, query, email_limit):
    """Process a user query"""
    if not query.strip():
        return

    try:
        # Parse query intent
        query_info = adapter.parse_user_query(query)
        intent = query_info["intent"]
        criteria = query_info["criteria"]

        if intent == "status":
            print_status(adapter)

        elif intent == "help":
            print_help()

        elif intent == "search":
            print(f"\n{Colors.OKCYAN}🔍 Searching through {email_limit} emails...{Colors.ENDC}")

            result = adapter.search_jobs(query=query, limit=email_limit)

            if result["status"] == "success":
                jobs = result.get("emails", [])
                total = result.get("total_found", 0)
                matched = result.get("count", 0)
                criteria_dict = result.get("criteria", {})

                if not jobs:
                    print(f"\n{Colors.FAIL}❌ No jobs found matching your criteria!{Colors.ENDC}")
                    print(f"\n   Searched: {total} emails")
                    if criteria_dict:
                        print("   Filters Applied:")
                        for key, val in criteria_dict.items():
                            print(f"     • {key.replace('_', ' ').title()}: {val}")
                    print(f"\n   {Colors.WARNING}💡 Tips:{Colors.ENDC}")
                    print("   - Try increasing the email limit")
                    print("   - Remove one filter condition")
                    print("   - Try a more general search")

                else:
                    print(f"\n{Colors.OKGREEN}✅ Found {matched} matching job(s)!{Colors.ENDC}")
                    print(f"   Searched: {total} emails")

                    if criteria_dict:
                        print(f"\n   {Colors.BOLD}Filters Applied:{Colors.ENDC}")
                        for key, val in criteria_dict.items():
                            print(f"     • {key.replace('_', ' ').title()}: {val}")

                    print(f"\n   {Colors.BOLD}Job Opportunities:{Colors.ENDC}")

                    for i, job in enumerate(jobs[:10], 1):
                        print(format_job_result(job, i))

                    if matched > 10:
                        print(f"\n   {Colors.WARNING}📌 Showing 10 out of {matched} matches{Colors.ENDC}")

                    print(f"\n   {Colors.BOLD}💬 Next:{Colors.ENDC}")
                    print("   - Refine the search with additional criteria")
                    print("   - Adjust email limit to find more opportunities")
                    print("   - Ask another question")

            else:
                print(f"{Colors.FAIL}❌ Error: {result.get('message', 'Unable to fetch jobs')}{Colors.ENDC}")

        else:
            # Default: treat as search
            result = adapter.search_jobs(query=query, limit=email_limit)
            if result["status"] == "success" and result.get("count", 0) > 0:
                jobs = result.get("emails", [])
                print(f"\n{Colors.OKGREEN}✅ Found {len(jobs)} matching job(s)!{Colors.ENDC}\n")
                for i, job in enumerate(jobs[:5], 1):
                    print(format_job_result(job, i))
            else:
                print(f"\n{Colors.FAIL}❌ No jobs found. Try a different search!{Colors.ENDC}\n")

    except Exception as e:
        print(f"\n{Colors.FAIL}❌ Error: {str(e)}{Colors.ENDC}\n")


def main():
    """Main CLI loop"""
    print_header()

    # Initialize adapter
    try:
        adapter = get_chatbot_adapter()
        print(f"{Colors.OKGREEN}✅ Gmail Service Connected!{Colors.ENDC}\n")
    except Exception as e:
        print(f"{Colors.FAIL}❌ Failed to connect to Gmail: {e}{Colors.ENDC}")
        return

    # Settings
    email_limit = 15
    chat_history = []

    print(f"Type {Colors.BOLD}'help'{Colors.ENDC} for commands or ask a query naturally!")
    print(f"Type {Colors.BOLD}'examples'{Colors.ENDC} to see query examples!")
    print(f"Type {Colors.BOLD}'exit'{Colors.ENDC} to quit.\n")

    # Chat loop
    while True:
        try:
            # Get user input
            user_input = input(f"{Colors.OKBLUE}You:{Colors.ENDC} ").strip()

            if not user_input:
                continue

            # Store in history
            chat_history.append({
                "role": "user",
                "content": user_input,
                "timestamp": datetime.now()
            })

            # Handle commands
            if user_input.lower() in ['exit', 'quit']:
                print(f"\n{Colors.OKGREEN}👋 Thank you for using Naukri Job Assistant!{Colors.ENDC}")
                print(f"{Colors.OKGREEN}Happy Job Hunting! 🚀{Colors.ENDC}\n")
                break

            elif user_input.lower() == 'help':
                print_help()

            elif user_input.lower() == 'examples':
                print_examples()

            elif user_input.lower() == 'status':
                print_status(adapter)

            elif user_input.lower() == 'clear':
                chat_history = []
                print(f"\n{Colors.OKGREEN}✅ Chat history cleared!{Colors.ENDC}\n")

            elif user_input.lower() == 'settings':
                print(f"\n{Colors.BOLD}⚙️ CURRENT SETTINGS:{Colors.ENDC}")
                print(f"  Email Limit: {Colors.OKCYAN}{email_limit}{Colors.ENDC} emails")
                print(f"  Chat Messages: {Colors.OKCYAN}{len(chat_history)}{Colors.ENDC}\n")

            elif user_input.lower().startswith('limit'):
                try:
                    new_limit = int(user_input.split()[1])
                    if 1 <= new_limit <= 50:
                        email_limit = new_limit
                        print(f"\n{Colors.OKGREEN}✅ Email limit set to {email_limit}!{Colors.ENDC}\n")
                    else:
                        print(f"\n{Colors.FAIL}❌ Please use a limit between 1 and 50{Colors.ENDC}\n")
                except (IndexError, ValueError):
                    print(f"\n{Colors.FAIL}❌ Usage: limit <number> (1-50){Colors.ENDC}\n")

            else:
                # Process as query
                print()
                process_query(adapter, user_input, email_limit)

        except KeyboardInterrupt:
            print(f"\n\n{Colors.OKGREEN}👋 Goodbye!{Colors.ENDC}\n")
            break
        except Exception as e:
            print(f"\n{Colors.FAIL}❌ Error: {e}{Colors.ENDC}\n")


if __name__ == "__main__":
    main()

