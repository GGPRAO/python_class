"""
Gmail Module - VERSION 4: Config File Version
Reads credentials from a JSON/YAML config file
"""

import json
import os
import imaplib
import email
from pathlib import Path


class GmailConfigFile:
    """Gmail configuration from config file."""

    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993
    DEFAULT_EMAIL_LIMIT = 5
    SEARCH_QUERY = 'FROM "naukri"'
    CONFIG_FILE = "gmail_config.json"

    @classmethod
    def load_from_file(cls, config_file=None):
        """
        Load credentials from JSON config file.

        Config file format:
        {
            "email": "user@gmail.com",
            "password": "app_password"
        }

        Args:
            config_file (str, optional): Path to config file

        Returns:
            tuple: (email, password)
        """
        if config_file is None:
            config_file = cls.CONFIG_FILE

        config_path = Path(config_file)

        if not config_path.exists():
            raise FileNotFoundError(
                f"❌ Config file not found: {config_file}\n"
                f"Create it with: {{'email': 'your@email.com', 'password': 'app_password'}}"
            )

        try:
            with open(config_path, 'r') as f:
                config = json.load(f)

            email_addr = config.get('email')
            password = config.get('password')

            if not email_addr or not password:
                raise ValueError("Config file missing 'email' or 'password'")

            return (email_addr, password)

        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in config file")


class GmailServiceConfigFile:
    """Gmail service using config file credentials."""

    def __init__(self, config_file=None):
        """Initialize with credentials from config file."""
        self.email_addr, self.password = GmailConfigFile.load_from_file(config_file)
        self.imap_server = GmailConfigFile.IMAP_SERVER
        self.imap_port = GmailConfigFile.IMAP_PORT

    def fetch_naukri_emails(self, limit=None):
        """Fetch Naukri emails from config file credentials."""
        if limit is None:
            limit = GmailConfigFile.DEFAULT_EMAIL_LIMIT

        try:
            mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            mail.login(self.email_addr, self.password)
            mail.select("inbox")

            status, messages = mail.search(None, GmailConfigFile.SEARCH_QUERY)
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
def fetch_naukri_jobs_config_file(config_file=None, limit=None):
    """Fetch jobs using config file credentials."""
    service = GmailServiceConfigFile(config_file)
    return service.fetch_naukri_emails(limit)


# Helper function to create sample config
def create_sample_config(config_file="gmail_config.json"):
    """Create a sample config file."""
    sample_config = {
        "email": "your_email@gmail.com",
        "password": "your_app_password"
    }

    with open(config_file, 'w') as f:
        json.dump(sample_config, f, indent=2)

    print(f"✅ Created sample config: {config_file}")
    print("   Update it with your credentials!")


if __name__ == "__main__":
    print("Gmail Module - CONFIG FILE VERSION")
    print("=" * 50)

    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "create":
        create_sample_config()
    else:
        try:
            service = GmailServiceConfigFile()
            emails = service.fetch_naukri_emails(limit=5)
            print(f"✅ Found {len(emails)} emails")
            for i, e in enumerate(emails, 1):
                print(f"{i}. {e['subject']}")
        except FileNotFoundError as e:
            print(f"❌ {e}")
            print("\nCreate config file with: python VERSION_4_config_file.py create")

