"""
Gmail Module - VERSION 5: Multiple Accounts Version
Handle multiple Gmail accounts simultaneously
"""

import imaplib
import email
from typing import List, Dict


class MultiAccountGmailService:
    """Service to handle multiple Gmail accounts."""

    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993
    DEFAULT_EMAIL_LIMIT = 5
    SEARCH_QUERY = 'FROM "naukri"'

    def __init__(self):
        """Initialize multi-account service."""
        self.accounts = {}  # {account_name: (email, password)}

    def add_account(self, name: str, email_addr: str, password: str):
        """
        Add a Gmail account.

        Args:
            name (str): Account nickname
            email_addr (str): Gmail email
            password (str): Gmail app password
        """
        self.accounts[name] = (email_addr, password)
        print(f"✅ Added account: {name}")

    def fetch_from_account(self, account_name: str, limit=None) -> Dict:
        """
        Fetch emails from specific account.

        Args:
            account_name (str): Account nickname
            limit (int, optional): Number of emails

        Returns:
            dict: {status, count, emails}
        """
        if account_name not in self.accounts:
            return {
                "status": "error",
                "message": f"Account '{account_name}' not found",
                "emails": []
            }

        if limit is None:
            limit = self.DEFAULT_EMAIL_LIMIT

        email_addr, password = self.accounts[account_name]

        try:
            mail = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT)
            mail.login(email_addr, password)
            mail.select("inbox")

            status, messages = mail.search(None, self.SEARCH_QUERY)
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

            return {
                "status": "success",
                "account": account_name,
                "count": len(emails_data),
                "emails": emails_data,
                "message": f"✅ Found {len(emails_data)} emails from {account_name}"
            }

        except Exception as e:
            return {
                "status": "error",
                "account": account_name,
                "message": f"❌ Error: {e}",
                "emails": []
            }

    def fetch_from_all_accounts(self, limit=None) -> Dict[str, Dict]:
        """
        Fetch from all accounts.

        Returns:
            dict: {account_name: results}
        """
        results = {}
        for account_name in self.accounts:
            results[account_name] = self.fetch_from_account(account_name, limit)
        return results

    def list_accounts(self) -> List[str]:
        """Get list of configured accounts."""
        return list(self.accounts.keys())


if __name__ == "__main__":
    print("Gmail Module - MULTIPLE ACCOUNTS VERSION")
    print("=" * 50 + "\n")

    service = MultiAccountGmailService()

    # Example: Add multiple accounts
    # service.add_account("personal", "personal@gmail.com", "password1")
    # service.add_account("work", "work@gmail.com", "password2")

    print("Example usage:")
    print("  service = MultiAccountGmailService()")
    print("  service.add_account('acc1', 'email@gmail.com', 'password')")
    print("  service.add_account('acc2', 'email2@gmail.com', 'password2')")
    print("  result = service.fetch_from_account('acc1', limit=5)")
    print("  all_results = service.fetch_from_all_accounts()")

