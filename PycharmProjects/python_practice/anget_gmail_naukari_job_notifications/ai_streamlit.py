import streamlit as st
from mail_config import fetch_naukri_emails
from clean_email import clean_emails
from summarize_emails import summarize_email

# Page config
st.set_page_config(page_title="📧 Naukri Job Mail Agent", layout="wide")

st.title("📧 Naukri Job Mail Agent")
st.markdown("---")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    email_input = st.text_input("Gmail Address", type="default")
    password_input = st.text_input("Gmail App Password", type="password")
    email_limit = st.slider("Number of emails to fetch", 1, 20, 5)

# Main content
col1, col2 = st.columns([3, 1])

with col2:
    fetch_button = st.button("🔄 Fetch Jobs", use_container_width=True)

if fetch_button:
    if not email_input or not password_input:
        st.error("❌ Please enter email and password")
    else:
        with st.spinner("Fetching emails..."):
            # Fetch emails
            emails_data = fetch_naukri_emails(email_input, password_input, email_limit)

            if not emails_data:
                st.warning("⚠️ No Naukri emails found")
            else:
                # Clean emails
                cleaned_emails = clean_emails(emails_data)

                st.success(f"✅ Found {len(cleaned_emails)} job notifications")

                # Display emails
                for i, mail in enumerate(cleaned_emails, 1):
                    with st.expander(f"📧 {i}. {mail['subject']}", expanded=(i == 1)):
                        st.markdown("**Subject:** " + mail["subject"])

                        # Get AI summary
                        with st.spinner("Generating summary..."):
                            summary = summarize_email(mail["body"])
                            st.markdown("**🧠 AI Summary:**")
                            st.write(summary)
