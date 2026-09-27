from bs4 import BeautifulSoup


def clean_html(html):
    """
    Remove HTML tags from email body.

    Args:
        html (str): HTML content

    Returns:
        str: Cleaned text content
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def clean_emails(emails_data):
    """
    Clean and extract text from email data.

    Args:
        emails_data (list): List of email dictionaries with subject and body

    Returns:
        list: Cleaned emails with HTML removed
    """
    cleaned_emails = []

    for mail in emails_data:
        cleaned_emails.append({
            "subject": mail["subject"],
            "body": clean_html(mail["body"])
        })

    return cleaned_emails


if __name__ == "__main__":
    print("ℹ️ This module should be imported by other modules")
