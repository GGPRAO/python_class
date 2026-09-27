import ollama


def summarize_email(content):
    """
    Summarize email content using Ollama LLM (Qwen2 1.5B model).

    Args:
        content (str): Email body content

    Returns:
        str: AI-generated summary with job details
    """
    prompt = f"""
    Extract job details from this email:
    - Job Role
    - Company
    - Location
    - Experience

    Email:
    {content}
    """

    response = ollama.chat(
        model="qwen2:1.5b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


def process_and_summarize(cleaned_emails):
    """
    Process cleaned emails and generate summaries.

    Args:
        cleaned_emails (list): List of cleaned email dictionaries
    """
    if not cleaned_emails:
        print("❌ No emails to process")
        return

    for mail in cleaned_emails:
        summary = summarize_email(mail["body"])
        print("\n📧 Subject:", mail["subject"])
        print("🧠 Summary:\n", summary)


if __name__ == "__main__":
    # This script should be imported by other modules
    print("ℹ️ This module should be imported, not run directly")
