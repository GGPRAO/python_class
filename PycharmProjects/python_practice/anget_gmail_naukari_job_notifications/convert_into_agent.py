from mail_config import fetch_naukri_emails
from clean_email import clean_emails
from summarize_emails import summarize_email


def naukri_agent(email_address, password, email_limit=5):
    """
    Autonomous agent that fetches, cleans, and summarizes Naukri emails.

    Args:
        email_address (str): Gmail address
        password (str): Gmail app password
        email_limit (int): Number of emails to fetch
    """
    print("🔍 Fetching latest Naukri emails...")

    # Fetch emails from Gmail
    emails_data = fetch_naukri_emails(email_address, password, email_limit)

    if not emails_data:
        print("❌ No Naukri emails found")
        return

    # Clean emails
    cleaned_emails = clean_emails(emails_data)
    print(f"✅ Found {len(cleaned_emails)} emails")

    # Process each email
    for mail in cleaned_emails:
        try:
            summary = summarize_email(mail["body"])

            print("\n" + "="*50)
            print("📧", mail["subject"])
            print("="*50)
            print(summary)
            print()
        except Exception as e:
            print(f"❌ Error processing email: {e}")
            continue


if __name__ == "__main__":
    # Example usage
    email = input("Enter your Gmail address: ")
    password = input("Enter your Gmail app password: ")
    limit = int(input("Number of emails to fetch (default 5): ") or "5")

    naukri_agent(email, password, limit)
