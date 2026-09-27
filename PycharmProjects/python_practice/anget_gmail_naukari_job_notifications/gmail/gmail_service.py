"""
Gmail Service Module
Provides methods to fetch and process emails using hardcoded credentials.
"""

import imaplib
import email
import socket
from .gmail_config import GmailConfig


class GmailService:
    """Service to handle Gmail operations with hardcoded credentials."""

    def __init__(self):
        """Initialize Gmail service with hardcoded credentials."""
        self.email_addr, self.password = GmailConfig.get_credentials()
        self.imap_server = GmailConfig.IMAP_SERVER
        self.imap_port = GmailConfig.IMAP_PORT
        self._connection_timeout = 10  # 10 second timeout for connections

    def fetch_naukri_emails(self, limit=None):
        """
        Fetch Naukri job notification emails using hardcoded credentials.

        Args:
            limit (int, optional): Number of recent emails to fetch.
                                   Defaults to GmailConfig.DEFAULT_EMAIL_LIMIT

        Returns:
            list: List of email dictionaries with subject and body
        """
        if limit is None:
            limit = GmailConfig.DEFAULT_EMAIL_LIMIT

        try:
            # Set socket timeout to prevent hanging
            socket.setdefaulttimeout(self._connection_timeout)

            # Connect to Gmail
            mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            mail.login(self.email_addr, self.password)

            # Select inbox
            mail.select("inbox")

            # Search for Naukri emails
            status, messages = mail.search(None, GmailConfig.SEARCH_QUERY)

            email_ids = messages[0].split()
            latest_emails = email_ids[-limit:]  # Get last N emails

            emails_data = []

            # Process each email
            for e_id in latest_emails:
                status, msg_data = mail.fetch(e_id, "(RFC822)")

                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject = msg["subject"]

                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/html":
                                    body = part.get_payload(decode=True).decode()
                        else:
                            body = msg.get_payload(decode=True).decode()

                        emails_data.append({
                            "subject": subject,
                            "body": body
                        })

            mail.close()
            mail.logout()
            return emails_data

        except socket.timeout:
            print(f"⏱️ Timeout: Gmail connection took too long (>{self._connection_timeout}s)")
            return []
        except Exception as e:
            print(f"❌ Error fetching emails: {e}")
            return []
        finally:
            # Reset socket timeout
            socket.setdefaulttimeout(None)

    def get_email_address(self):
        """
        Get the configured email address.

        Returns:
            str: Email address
        """
        return self.email_addr

    def get_email_count(self, limit=None):
        """
        Get count of recent Naukri emails.

        Args:
            limit (int, optional): Maximum number of emails to count

        Returns:
            int: Number of emails found
        """
        emails = self.fetch_naukri_emails(limit)
        return len(emails)


# Convenience functions for chatbot integration
def fetch_naukri_jobs(limit=None):
    """
    Fetch Naukri job emails using hardcoded credentials.

    Args:
        limit (int, optional): Number of emails to fetch

    Returns:
        list: List of email dictionaries
    """
    service = GmailService()
    return service.fetch_naukri_emails(limit)


def get_default_email():
    """
    Get the default Gmail address.

    Returns:
        str: Email address
    """
    return GmailConfig.EMAIL

