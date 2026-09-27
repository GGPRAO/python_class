# 📧 Naukri Job Mail Agent

An AI-powered Streamlit application that fetches, cleans, and summarizes job notifications from Gmail using Ollama LLM.

## 🎯 Project Overview

This application automates the process of:
- 📩 Fetching job notifications from Naukri via Gmail
- 🧹 Cleaning HTML content and extracting text
- 🤖 Summarizing emails using AI (Ollama LLM)
- 🎨 Displaying results in an interactive web interface

---

## 📁 Project Structure

```
anget_gmail_naukari_job_notifications/
│
├── ai_streamlit.py              # Main Streamlit web application
├── mail_config.py               # Gmail IMAP configuration & email fetching
├── clean_email.py               # HTML cleaning & email text extraction
├── summarize_emails.py          # AI-powered email summarization
├── convert_into_agent.py        # Agent conversion utilities
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🔧 Setup Instructions

### Prerequisites
- **Python:** 3.8 or higher
- **Ollama:** Latest version (for LLM functionality)
- **Gmail Account:** With IMAP enabled

### Step 1: Create Virtual Environment

```bash
# Windows PowerShell
python -m venv venv
venv\Scripts\Activate.ps1

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies include:**
- `streamlit` - Web UI framework
- `google-auth-oauthlib` - Gmail authentication
- `google-auth-httplib2` - HTTP client
- `google-api-python-client` - Gmail API
- `ollama` - LLM integration
- `beautifulsoup4` - HTML parsing

### Step 3: Configure Gmail Access

#### Option A: Gmail App Password (Recommended)
1. Enable 2-Factor Authentication on your Google Account
2. Go to [Google Account Settings](https://myaccount.google.com)
3. Navigate to **Security** → **App passwords**
4. Select "Mail" and "Windows Computer"
5. Copy the generated 16-character password

#### Option B: Direct Gmail Password
⚠️ Less secure - use App Password instead

### Step 4: Run the Application

```bash
streamlit run ai_streamlit.py
```

The application will open at `http://localhost:8501`

---

## 🚀 Usage

### 1. **Configure Email & Password**
   - Enter your Gmail address in the sidebar
   - Paste your App Password
   - Adjust the number of emails to fetch (1-20)

### 2. **Click "Fetch Jobs"**
   - Application fetches latest Naukri emails
   - Shows loading spinner during processing

### 3. **View Summaries**
   - Expands each email with subject
   - Displays AI-generated summary with:
     - Job Role
     - Company Name
     - Location
     - Experience Required

---

## 📊 Navigation & Data Flow

```
┌─────────────────┐
│   ai_streamlit  │  ← User Interface (Streamlit Web App)
└────────┬────────┘
         │
         ├──→ mail_config.fetch_naukri_emails()
         │    ↓ (Fetches raw emails from Gmail via IMAP)
         │
         ├──→ clean_email.clean_emails()
         │    ↓ (Removes HTML, extracts text)
         │
         └──→ summarize_emails.summarize_email()
              ↓ (Sends to Ollama LLM for summarization)
              ↓
           Output to UI
```

---

## 🔑 API Reference

### `mail_config.py`

```python
fetch_naukri_emails(email_addr, password, limit=5)
```
**Returns:** List of email dictionaries with `subject` and `body` keys

### `clean_email.py`

```python
clean_emails(emails_data)
```
**Returns:** List of cleaned emails with HTML removed

```python
clean_html(html)
```
**Returns:** Plain text from HTML content

### `summarize_emails.py`

```python
summarize_email(content)
```
**Returns:** AI-generated summary with job details

```python
process_and_summarize(cleaned_emails)
```
**Prints:** Formatted summaries to console

---

## ⚙️ Configuration

### Gmail Settings
- Uses IMAP protocol on `imap.gmail.com`
- Searches for emails from "naukri" sender
- Default fetch limit: 5 emails

### Ollama Settings
- **Model:** `qwen2:1.5b` (Lightweight, fast, efficient)
- **Prompt:** Extracts Job Role, Company, Location, Experience
- **Performance:** ~2-5 seconds per email

Modify in `summarize_emails.py` if needed:
```python
response = ollama.chat(
    model="qwen2:1.5b",  # Change model here
    messages=[{"role": "user", "content": prompt}]
)
```

---

## 🐛 Troubleshooting

### ❌ "Gmail authentication failed"
- Verify email address is correct
- Use App Password, not Gmail password
- Ensure IMAP is enabled in Gmail settings

### ❌ "Ollama connection error"
- Start Ollama service: `ollama serve`
- Verify model exists: `ollama list`
- Check if running on correct port (default: 11434)

### ❌ "No emails found"
- Verify Naukri emails exist in your inbox
- Check Gmail search filter works: `FROM "naukri"`
- Increase email fetch limit

---

## 📦 Requirements File

```txt
streamlit==1.28.1
google-auth-oauthlib==1.1.0
google-auth-httplib2==0.2.0
google-api-python-client==2.100.0
ollama==0.1.0
beautifulsoup4==4.12.2
```

---

## 🎓 File Descriptions

| File | Purpose |
|------|---------|
| `ai_streamlit.py` | Main UI - handles user input and displays results |
| `mail_config.py` | Gmail IMAP connection and email fetching logic |
| `clean_email.py` | HTML parsing and text extraction |
| `summarize_emails.py` | LLM integration for email summarization |
| `convert_into_agent.py` | Utilities for agent conversion (future use) |

---

## 🔐 Security Notes

⚠️ **Important:** Never commit credentials to version control
- Store passwords as environment variables
- Use Gmail App Passwords, not your main password
- Consider using `.env` file with `python-dotenv`

### Using Environment Variables

```bash
# Set environment variable
$env:GMAIL_PASSWORD = "your-app-password"
```

Then update `ai_streamlit.py`:
```python
import os
password_input = os.getenv("GMAIL_PASSWORD", "")
```

---

## 🚦 Development Status

- ✅ Email fetching functional
- ✅ HTML cleaning working
- ✅ AI summarization integrated
- ✅ Streamlit UI complete
- 🔄 Agent conversion in progress

---

## 📝 License

This project is provided as-is for personal use.

---

## 💡 Future Enhancements

- [ ] Database storage for email history
- [ ] Advanced filtering options
- [ ] Email export (PDF/Excel)
- [ ] Scheduled automated fetching
- [ ] Multi-account support
- [ ] Custom LLM prompt templates

---

## 📞 Support

For issues or questions, check:
1. Gmail IMAP settings
2. Ollama service status
3. Python dependencies installed
4. Firewall/network restrictions

Happy job hunting! 🎉

