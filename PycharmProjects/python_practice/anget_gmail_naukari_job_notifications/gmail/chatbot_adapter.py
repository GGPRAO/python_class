"""
Chatbot Integration Module
Provides chatbot-compatible interface for Gmail operations with intelligent filtering.
"""

from .gmail_service import GmailService, fetch_naukri_jobs, get_default_email
from .gmail_config import GmailConfig
from .job_filter import JobFilter, extract_and_filter_jobs
from typing import Dict, Any
import re


class GmailChatbotAdapter:
    """Adapter to provide chatbot-compatible interface for Gmail operations."""

    def __init__(self):
        """Initialize the chatbot adapter."""
        self.service = GmailService()
        self.name = "Gmail Assistant"
        self.description = "Fetch and summarize Naukri job notification emails"
        self.job_filter = JobFilter()
        self.last_fetched_emails = []
        self.last_extracted_jobs = []

    def fetch_jobs(self, limit=None, query=None):
        """
        Fetch Naukri job emails with optional intelligent filtering.

        Args:
            limit (int, optional): Number of emails to fetch
            query (str, optional): Natural language query to filter jobs

        Returns:
            dict: Response with status and emails data
        """
        try:
            emails = self.service.fetch_naukri_emails(limit)
            self.last_fetched_emails = emails

            if query:
                # Extract and filter jobs based on query
                extracted, criteria, filtered = extract_and_filter_jobs(emails, query)
                self.last_extracted_jobs = extracted

                return {
                    "status": "success",
                    "count": len(filtered),
                    "total_found": len(emails),
                    "emails": filtered,
                    "criteria": criteria,
                    "message": f"✅ Found {len(filtered)} matching job(s) out of {len(emails)} total"
                }
            else:
                # Extract job details for all emails
                extracted = [self.job_filter.extract_job_details(email) for email in emails]
                self.last_extracted_jobs = extracted

                return {
                    "status": "success",
                    "count": len(extracted),
                    "emails": extracted,
                    "message": f"✅ Found {len(extracted)} job notification(s)"
                }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Error fetching emails: {e}",
                "emails": []
            }

    def search_jobs(self, query, limit=None):
        """
        Search for jobs matching query criteria.

        Args:
            query (str): Natural language query
            limit (int, optional): Number of emails to fetch

        Returns:
            dict: Response with matching jobs
        """
        # First fetch emails
        fetch_result = self.fetch_jobs(limit=limit or 20, query=query)

        if fetch_result["status"] == "error":
            return fetch_result

        return fetch_result

    def parse_user_query(self, query: str) -> Dict[str, Any]:
        """
        Parse user query to understand intent and extract criteria.

        Args:
            query (str): User's natural language query

        Returns:
            dict: Query intent and extracted criteria
        """
        query_lower = query.lower()
        intent = "search"
        criteria = self.job_filter.parse_query(query)

        # Determine intent
        if any(word in query_lower for word in ['status', 'check', 'connected', 'working']):
            intent = "status"
        elif any(word in query_lower for word in ['help', 'what', 'can', 'command']):
            intent = "help"
        elif any(word in query_lower for word in ['search', 'find', 'filter', 'get', 'show']):
            intent = "search"

        return {
            "intent": intent,
            "query": query,
            "criteria": criteria
        }


    def get_status(self):
        """
        Get current status and credentials info.

        Returns:
            dict: Status information
        """
        return {
            "status": "connected",
            "email": get_default_email(),
            "service": "Gmail",
            "authenticated": True,
            "available": True
        }

    def get_options(self):
        """
        Get available chatbot options for Gmail.

        Returns:
            dict: Available options and commands
        """
        return {
            "options": [
                {
                    "id": "fetch_jobs",
                    "name": "Fetch Naukri Jobs",
                    "description": "Fetch latest Naukri job notifications",
                    "parameters": {
                        "limit": {
                            "type": "integer",
                            "default": 5,
                            "description": "Number of emails to fetch"
                        }
                    }
                },
                {
                    "id": "get_status",
                    "name": "Get Status",
                    "description": "Check Gmail service status",
                    "parameters": {}
                }
            ],
            "email": get_default_email()
        }

    def execute_command(self, command, **kwargs):
        """
        Execute a chatbot command.

        Args:
            command (str): Command to execute
            **kwargs: Additional parameters

        Returns:
            dict: Command execution result
        """
        commands = {
            "fetch_jobs": self.fetch_jobs,
            "get_status": self.get_status,
            "get_options": self.get_options
        }

        if command not in commands:
            return {
                "status": "error",
                "message": f"Unknown command: {command}"
            }

        try:
            return commands[command](**kwargs)
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error executing command: {e}"
            }


# Global chatbot adapter instance
_chatbot_adapter = None


def get_chatbot_adapter():
    """
    Get or create the global chatbot adapter instance.

    Returns:
        GmailChatbotAdapter: Chatbot adapter instance
    """
    global _chatbot_adapter
    if _chatbot_adapter is None:
        _chatbot_adapter = GmailChatbotAdapter()
    return _chatbot_adapter


def fetch_jobs_for_chatbot(limit=None):
    """
    Convenience function to fetch jobs for chatbot.

    Args:
        limit (int, optional): Number of emails to fetch

    Returns:
        dict: Response with emails
    """
    adapter = get_chatbot_adapter()
    return adapter.fetch_jobs(limit)


def get_gmail_status():
    """
    Convenience function to get Gmail status for chatbot.

    Returns:
        dict: Status information
    """
    adapter = get_chatbot_adapter()
    return adapter.get_status()


def get_gmail_options():
    """
    Convenience function to get available options for chatbot.

    Returns:
        dict: Available options
    """
    adapter = get_chatbot_adapter()
    return adapter.get_options()

