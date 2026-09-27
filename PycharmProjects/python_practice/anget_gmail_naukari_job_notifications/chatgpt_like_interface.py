#!/usr/bin/env python3
"""
ChatGPT-Like Email Assistant v3.0
A conversational AI interface for fetching and querying emails from Gmail.
Works like ChatGPT but directly accesses your mailbox!
"""

import sys
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, List, Any
import webbrowser
import time
import subprocess
import os

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from gmail import get_chatbot_adapter
except ImportError:
    print("❌ Gmail module not found. Please ensure gmail package is properly installed.")
    sys.exit(1)


class ChatGPTLikeInterface:
    """ChatGPT-like conversational interface for email queries."""

    def __init__(self):
        """Initialize the ChatGPT-like interface."""
        self._adapter = None  # Lazy initialization
        self.conversation_history = []
        self.email_cache = {}
        self.settings = {
            'email_limit': 15,
            'show_details': True,
            'search_depth': 20,
            'auto_summarize': True
        }
        self.current_session_emails = []

    @property
    def adapter(self):
        """Lazy-initialize the Gmail adapter on first use."""
        if self._adapter is None:
            self._adapter = get_chatbot_adapter()
        return self._adapter

    def add_to_history(self, role: str, content: str):
        """Add message to conversation history."""
        self.conversation_history.append({
            'role': role,
            'timestamp': datetime.now().isoformat(),
            'content': content
        })

    def print_assistant_message(self, message: str, end: str = "\n"):
        """Print assistant message with formatting."""
        print(f"\n{self._color('OKBLUE')}🤖 Assistant:{self._color('ENDC')} {message}", end=end)

    def print_user_message(self, message: str):
        """Print user message with formatting."""
        print(f"{self._color('OKCYAN')}👤 You:{self._color('ENDC')} {message}")

    def print_system_message(self, message: str):
        """Print system message."""
        print(f"{self._color('WARNING')}📌 System:{self._color('ENDC')} {message}")

    def print_success(self, message: str):
        """Print success message."""
        print(f"{self._color('OKGREEN')}✅ {message}{self._color('ENDC')}")

    def print_error(self, message: str):
        """Print error message."""
        print(f"{self._color('FAIL')}❌ {message}{self._color('ENDC')}")

    @staticmethod
    def _color(color_name: str) -> str:
        """Get color code for terminal."""
        colors = {
            'HEADER': '\033[95m',
            'OKBLUE': '\033[94m',
            'OKCYAN': '\033[96m',
            'OKGREEN': '\033[92m',
            'WARNING': '\033[93m',
            'FAIL': '\033[91m',
            'ENDC': '\033[0m',
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m'
        }
        return colors.get(color_name, '')

    def format_email(self, email: Dict[str, Any]) -> str:
        """Format email for display."""
        output = []
        output.append(f"\n{'='*70}")

        # Subject
        subject = email.get('subject', 'No Subject')
        output.append(f"{self._color('BOLD')}📧 {subject}{self._color('ENDC')}")

        # From
        sender = email.get('from', 'Unknown')
        output.append(f"   From: {sender}")

        # Date
        date = email.get('date', 'Unknown')
        output.append(f"   Date: {date}")

        # Extracted Job Info (if available)
        if 'job_info' in email:
            job_info = email['job_info']
            output.append(f"\n   {self._color('OKGREEN')}Job Information:{self._color('ENDC')}")

            if job_info.get('role'):
                output.append(f"   • Role: {job_info['role']}")
            if job_info.get('company'):
                output.append(f"   • Company: {job_info['company']}")
            if job_info.get('location'):
                output.append(f"   • Location: {job_info['location']}")
            if job_info.get('salary'):
                output.append(f"   • Salary: {job_info['salary']}")
            if job_info.get('experience'):
                output.append(f"   • Experience: {job_info['experience']}")

        # Preview
        preview = email.get('preview', '')[:200] + "..." if email.get('preview') else "No preview available"
        output.append(f"\n   Preview: {preview}")
        output.append(f"{'='*70}")

        return '\n'.join(output)

    def fetch_emails_for_query(self, query: str) -> Dict[str, Any]:
        """Fetch emails and filter based on query."""
        try:
            self.print_system_message(f"Searching your emails for: '{query}'...")
            result = self.adapter.search_jobs(query, limit=self.settings['search_depth'])

            if result['status'] == 'success':
                self.current_session_emails = result.get('emails', [])
                return result
            else:
                return {
                    'status': 'error',
                    'message': result.get('message', 'Unknown error'),
                    'emails': []
                }
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error searching emails: {str(e)}',
                'emails': []
            }

    def process_query(self, user_input: str) -> str:
        """Process user query and generate response."""
        user_input = user_input.strip()

        # Add to history
        self.add_to_history('user', user_input)
        self.print_user_message(user_input)

        # Check for special commands
        if user_input.lower() in ['help', '?', 'commands']:
            return self.show_help()
        elif user_input.lower() == 'settings':
            return self.show_settings()
        elif user_input.lower() == 'status':
            return self.check_status()
        elif user_input.lower() == 'examples':
            return self.show_examples()
        elif user_input.lower() == 'history':
            return self.show_history()
        elif user_input.lower() == 'clear':
            return self.clear_history()
        elif user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            return 'EXIT'
        elif user_input.lower().startswith('limit '):
            try:
                limit = int(user_input.split()[1])
                if 1 <= limit <= 100:
                    self.settings['search_depth'] = limit
                    self.print_success(f"Search depth set to {limit}")
                    return f"✅ Search depth updated to {limit} emails"
                else:
                    self.print_error("Limit must be between 1 and 100")
                    return "❌ Invalid limit. Please use a number between 1 and 100"
            except (ValueError, IndexError):
                self.print_error("Invalid format. Use: limit <number>")
                return "❌ Invalid format. Use: limit <number>"
        elif user_input.lower().startswith('summarize'):
            return self.summarize_last_results()
        else:
            # It's a query - fetch emails
            return self.handle_email_query(user_input)

    def handle_email_query(self, query: str) -> str:
        """Handle email search query."""
        result = self.fetch_emails_for_query(query)

        if result['status'] == 'error':
            self.print_error(result['message'])
            response = f"❌ {result['message']}"
        else:
            count = result.get('count', 0)
            emails = result.get('emails', [])

            if count == 0:
                self.print_system_message("No matching emails found. Try different keywords.")
                response = f"📭 No emails found matching '{query}'. Try different keywords or increase the search limit with 'limit <number>'."
            else:
                self.print_success(f"Found {count} matching email(s)")
                response = f"✅ Found {count} email(s) matching your query:\n"

                # Display emails
                for i, email in enumerate(emails[:5], 1):  # Show max 5
                    response += self.format_email(email)

                if count > 5:
                    response += f"\n\n📝 Showing 5 of {count} results. Type 'show more' to see additional results."

        self.add_to_history('assistant', response)
        return response

    def show_help(self) -> str:
        """Show help information."""
        help_text = f"""
{self._color('BOLD')}🤖 ChatGPT-Like Email Assistant - Help{self._color('ENDC')}

{self._color('BOLD')}HOW TO USE:{self._color('ENDC')}
Simply type your query naturally! The AI will search your emails.

Examples:
  • "Show me Python developer jobs"
  • "Find remote positions with 15-20 lpa"
  • "Show backend engineer jobs at TCS in Bangalore"
  • "What are the latest job notifications from today?"
  • "Find jobs matching 5+ years experience"

{self._color('BOLD')}COMMANDS:{self._color('ENDC')}
  help              - Show this help message
  examples          - Show example queries
  settings          - Show current settings
  status            - Check Gmail connection
  history           - Show conversation history
  clear             - Clear history
  limit <num>       - Set search depth (1-100)
  summarize         - Summarize last results
  exit/quit         - Exit the assistant

{self._color('BOLD')}TIPS:{self._color('ENDC')}
  💡 Use natural language - be conversational!
  💡 Combine multiple criteria: "role + location + salary"
  💡 Increase results with "limit 50"
  💡 Type history to see past conversations
"""
        self.print_assistant_message(help_text.strip())
        response = help_text
        self.add_to_history('assistant', response)
        return response

    def show_examples(self) -> str:
        """Show example queries."""
        examples = [
            "Python developer jobs",
            "Remote positions in Bangalore",
            "Backend engineer 15-20 lpa",
            "Frontend developer 5+ years experience",
            "Data scientist at Google",
            "DevOps engineer Mumbai 20 lpa",
            "Jobs in tech startups",
            "Latest Naukri notifications",
            "High paying IT jobs (20+ lpa)",
            "Entry level positions for freshers"
        ]

        examples_text = f"\n{self._color('BOLD')}📋 Example Queries:{self._color('ENDC')}\n"
        for i, example in enumerate(examples, 1):
            examples_text += f"  {i}. \"{example}\"\n"

        self.print_assistant_message(examples_text.strip())
        self.add_to_history('assistant', examples_text)
        return examples_text

    def show_settings(self) -> str:
        """Show current settings."""
        settings_text = f"""
{self._color('BOLD')}⚙️ Current Settings:{self._color('ENDC')}
  • Email Search Depth: {self.settings['search_depth']}
  • Show Details: {self.settings['show_details']}
  • Auto Summarize: {self.settings['auto_summarize']}
  
{self._color('BOLD')}How to Change:{self._color('ENDC')}
  • limit <num>    - Change search depth
"""
        self.print_assistant_message(settings_text.strip())
        self.add_to_history('assistant', settings_text)
        return settings_text

    def check_status(self) -> str:
        """Check Gmail connection status."""
        try:
            # Try to get default email
            result = self.adapter.search_jobs("test", limit=1)
            if result['status'] == 'success':
                status_msg = f"✅ Gmail connection is working properly!"
            else:
                status_msg = f"⚠️ Gmail connection has issues: {result.get('message')}"
        except Exception as e:
            status_msg = f"❌ Gmail connection error: {str(e)}"

        self.print_system_message(status_msg)
        self.add_to_history('assistant', status_msg)
        return status_msg

    def show_history(self) -> str:
        """Show conversation history."""
        if not self.conversation_history:
            history_text = "📝 No conversation history yet. Start by asking me something!"
        else:
            history_text = f"\n{self._color('BOLD')}📜 Conversation History:{self._color('ENDC')}\n"
            for i, msg in enumerate(self.conversation_history[-10:], 1):  # Last 10
                role = msg['role'].upper()
                content = msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content']
                history_text += f"  {i}. [{role}] {content}\n"

        self.print_assistant_message(history_text.strip())
        return history_text

    def clear_history(self) -> str:
        """Clear conversation history."""
        self.conversation_history = []
        self.current_session_emails = []
        msg = "🗑️ Conversation history cleared!"
        self.print_success(msg)
        self.add_to_history('assistant', msg)
        return msg

    def summarize_last_results(self) -> str:
        """Summarize last search results."""
        if not self.current_session_emails:
            msg = "📭 No search results to summarize. Try searching first!"
            self.print_system_message(msg)
            return msg

        summary = f"\n{self._color('BOLD')}📊 Summary of Last Search:{self._color('ENDC')}\n"
        summary += f"Total Results: {len(self.current_session_emails)}\n\n"

        for i, email in enumerate(self.current_session_emails[:3], 1):
            summary += f"{i}. {email.get('subject', 'No Subject')[:60]}\n"

        if len(self.current_session_emails) > 3:
            summary += f"\n... and {len(self.current_session_emails) - 3} more results"

        self.print_assistant_message(summary.strip())
        self.add_to_history('assistant', summary)
        return summary

    def print_header(self):
        """Print welcome header."""
        header = f"""
{'='*70}
{self._color('BOLD')}{self._color('OKBLUE')}💼 CHATGPT-LIKE EMAIL ASSISTANT v3.0{self._color('ENDC')}
{'='*70}
{self._color('OKGREEN')}✅ Conversational AI Interface for Your Email{self._color('ENDC')}
{self._color('OKGREEN')}✅ Ask anything, get instant email results{self._color('ENDC')}
{self._color('OKGREEN')}✅ Works like ChatGPT but fetches from YOUR mailbox!{self._color('ENDC')}
{'='*70}

{self._color('OKCYAN')}Type 'help' for commands or just ask a question naturally!{self._color('ENDC')}
Type 'exit' to quit.

"""
        print(header)

    def run(self):
        """Run the interactive chatbot."""
        self.print_header()

        while True:
            try:
                # Get user input
                user_input = input(f"\n{self._color('OKCYAN')}You:{self._color('ENDC')} ").strip()

                if not user_input:
                    continue

                # Process query
                response = self.process_query(user_input)

                # Check for exit
                if response == 'EXIT':
                    print(f"\n{self._color('OKGREEN')}👋 Goodbye! Your conversation history has been saved.{self._color('ENDC')}\n")
                    break

                # Print response (already formatted by process_query methods)

            except KeyboardInterrupt:
                print(f"\n{self._color('WARNING')}⚠️ Interrupted by user{self._color('ENDC')}")
                break
            except Exception as e:
                self.print_error(f"Unexpected error: {str(e)}")
                continue


def main():
    """Main entry point - launches the web interface."""
    try:
        print("\n" + "="*70)
        print("🚀 ChatGPT-Like Email Assistant - Launching Web Interface")
        print("="*70)
        print("\n🔄 Starting web server...")
        print("   • Server will run on: http://localhost:5000")
        print("   • Browser will open automatically")
        print("   • Type 'Ctrl+C' in this window to stop the server\n")

        # Import the web interface
        from chatgpt_web_interface import app

        # Open browser after a small delay
        def open_browser():
            time.sleep(2)  # Wait 2 seconds for server to start
            print("📱 Opening browser...")
            webbrowser.open('http://localhost:5000')

        # Start browser in background
        browser_thread = subprocess.Popen([sys.executable, '-c',
            'import webbrowser, time; time.sleep(2); webbrowser.open("http://localhost:5000")'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)

        # Run Flask app
        print("✅ Web server started!")
        print("="*70 + "\n")
        app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)

    except ImportError as e:
        print(f"❌ Error: Could not import web interface: {e}")
        print("Make sure chatgpt_web_interface.py is in the same folder")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n\n{'='*70}")
        print("👋 Server stopped. Thank you for using ChatGPT-Like Email Assistant!")
        print("="*70 + "\n")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

