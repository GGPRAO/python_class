"""
Gmail module for chatbot integration.
Provides hardcoded credentials for automated email fetching.
"""

from .gmail_config import GmailConfig
from .gmail_service import GmailService, fetch_naukri_jobs, get_default_email
from .chatbot_adapter import (
    GmailChatbotAdapter,
    get_chatbot_adapter,
    fetch_jobs_for_chatbot,
    get_gmail_status,
    get_gmail_options
)

__all__ = [
    'GmailConfig',
    'GmailService',
    'GmailChatbotAdapter',
    'get_chatbot_adapter',
    'fetch_naukri_jobs',
    'get_default_email',
    'fetch_jobs_for_chatbot',
    'get_gmail_status',
    'get_gmail_options'
]

