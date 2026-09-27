"""
Gmail Module - VERSION 2: User Input Version
Allows users to provide their own email and password
"""

import imaplib
import email


class GmailConfigUserInput:
    """Gmail configuration with user-provided credentials."""

    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993
    DEFAULT_EMAIL_LIMIT = 5
    SEARCH_QUERY = 'FROM "naukri"'

    @staticmethod
    def get_credentials_from_user():
        """
        Get email and password from user input.

        Returns:
            tuple: (email, password)
        """
        email_addr = input("📧 Enter Gmail address: ")
        password = input("🔐 Enter Gmail app password: ")
        return (email_addr, password)


class GmailServiceUserInput:
    """Gmail service with user-provided credentials."""

    def __init__(self, email_addr=None, password=None):
        """Initialize with user credentials."""
        if email_addr and password:
            self.email_addr = email_addr
            self.password = password
        else:
            self.email_addr, self.password = GmailConfigUserInput.get_credentials_from_user()

        self.imap_server = GmailConfigUserInput.IMAP_SERVER
        self.imap_port = GmailConfigUserInput.IMAP_PORT

    def fetch_naukri_emails(self, limit=None):
        """Fetch Naukri emails with user-provided credentials."""
        if limit is None:
            limit = GmailConfigUserInput.DEFAULT_EMAIL_LIMIT

        try:
            mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            mail.login(self.email_addr, self.password)
            mail.select("inbox")

            status, messages = mail.search(None, GmailConfigUserInput.SEARCH_QUERY)
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


# Convenience functions
def fetch_naukri_jobs_user_input(email_addr=None, password=None, limit=None):
    """Fetch jobs with optional user credentials."""
    service = GmailServiceUserInput(email_addr, password)
    return service.fetch_naukri_emails(limit)


if __name__ == "__main__":
    print("Gmail Module - USER INPUT VERSION")
    print("=" * 50)

    service = GmailServiceUserInput()
    emails = service.fetch_naukri_emails(limit=5)

    print(f"Found {len(emails)} emails")
    for i, e in enumerate(emails, 1):
        print(f"{i}. {e['subject']}")

