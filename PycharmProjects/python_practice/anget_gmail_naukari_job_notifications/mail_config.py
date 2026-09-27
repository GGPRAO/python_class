import imaplib
import email


def fetch_naukri_emails(email_addr, password, limit=5):
    """
    Fetch Naukri job notification emails from Gmail.

    Args:
        email_addr (str): Gmail email address
        password (str): Gmail password/app password
        limit (int): Number of recent emails to fetch

    Returns:
        list: List of email dictionaries with subject and body
    """
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_addr, password)

        mail.select("inbox")

        # Search Naukri emails
        status, messages = mail.search(None, '(FROM "naukri")')

        email_ids = messages[0].split()

        latest_emails = email_ids[-limit:]  # last N emails

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


if __name__ == "__main__":
    print("ℹ️ This module should be imported by other modules")
