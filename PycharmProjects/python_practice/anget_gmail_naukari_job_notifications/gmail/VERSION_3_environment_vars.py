"""
Gmail Module - VERSION 3: Environment Variables Version
Uses environment variables for credentials (more secure)
"""

import os
import imaplib
import email


class GmailConfigEnvVars:
    """Gmail configuration using environment variables."""

    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993
    DEFAULT_EMAIL_LIMIT = 5
    SEARCH_QUERY = 'FROM "naukri"'

    @classmethod
    def get_credentials_from_env(cls):
        """
        Get email and password from environment variables.

        Environment variables:
            GMAIL_EMAIL - Gmail email address
            GMAIL_PASSWORD - Gmail app password

        Returns:
            tuple: (email, password)
        """
        email_addr = os.getenv('GMAIL_EMAIL')
        password = os.getenv('GMAIL_PASSWORD')

        if not email_addr or not password:
            raise ValueError(
                "❌ Environment variables not set!\n"
                "Set: GMAIL_EMAIL and GMAIL_PASSWORD\n"
                "Example: set GMAIL_EMAIL=user@gmail.com"
            )

        return (email_addr, password)


class GmailServiceEnvVars:
    """Gmail service using environment variables for credentials."""

    def __init__(self):
        """Initialize with credentials from environment variables."""
        self.email_addr, self.password = GmailConfigEnvVars.get_credentials_from_env()
        self.imap_server = GmailConfigEnvVars.IMAP_SERVER
        self.imap_port = GmailConfigEnvVars.IMAP_PORT

    def fetch_naukri_emails(self, limit=None):
        """Fetch Naukri emails from environment credentials."""
        if limit is None:
            limit = GmailConfigEnvVars.DEFAULT_EMAIL_LIMIT

        try:
            mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            mail.login(self.email_addr, self.password)
            mail.select("inbox")

            status, messages = mail.search(None, GmailConfigEnvVars.SEARCH_QUERY)
            email_ids = messages[0].split()
            latest_emails = email_ids[-limit:]

            emails_data = []
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

        except Exception as e:
            print(f"❌ Error fetching emails: {e}")
            return []


# Convenience function
def fetch_naukri_jobs_env_vars(limit=None):
    """Fetch jobs using environment variable credentials."""
    service = GmailServiceEnvVars()
    return service.fetch_naukri_emails(limit)


if __name__ == "__main__":
    print("Gmail Module - ENVIRONMENT VARIABLES VERSION")
    print("=" * 50)
    print("\nSetup instructions:")
    print("  Windows: set GMAIL_EMAIL=your@email.com")
    print("  Windows: set GMAIL_PASSWORD=yourpassword")
    print("  Linux/Mac: export GMAIL_EMAIL=your@email.com")
    print("  Linux/Mac: export GMAIL_PASSWORD=yourpassword")
    print("\n" + "=" * 50 + "\n")

    try:
        service = GmailServiceEnvVars()
        emails = service.fetch_naukri_emails(limit=5)
        print(f"✅ Found {len(emails)} emails")
        for i, e in enumerate(emails, 1):
            print(f"{i}. {e['subject']}")
    except ValueError as e:
        print(f"❌ {e}")

