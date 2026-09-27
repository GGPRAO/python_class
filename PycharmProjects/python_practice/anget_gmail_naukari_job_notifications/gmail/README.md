# Gmail Module - Chatbot Integration

This folder contains the Gmail integration module with **hardcoded credentials** for automated email fetching in the chatbot.

## 📁 Folder Structure

```
gmail/
├── __init__.py              # Package initialization and exports
├── gmail_config.py          # Gmail configuration with hardcoded credentials
├── gmail_service.py         # Gmail service for fetching emails
├── chatbot_adapter.py       # Chatbot integration adapter
└── README.md               # This file
```

## 🔐 Hardcoded Credentials

**Email:** `ggpsmo@gmail.com`  
**Passcode:** `lodqerzdhzjppwph`

These credentials are automatically used by the Gmail service and do not need to be provided by users.

## 📦 Module Components

### 1. **GmailConfig** (gmail_config.py)
Configuration class with hardcoded credentials and IMAP settings.

```python
from gmail import GmailConfig

email, passcode = GmailConfig.get_credentials()
settings = GmailConfig.get_imap_connection_settings()
```

### 2. **GmailService** (gmail_service.py)
Service class for fetching Naukri job notification emails.

```python
from gmail import GmailService

service = GmailService()
emails = service.fetch_naukri_emails(limit=5)
```

### 3. **GmailChatbotAdapter** (chatbot_adapter.py)
Adapter class providing chatbot-compatible interface for Gmail operations.

```python
from gmail import GmailChatbotAdapter

adapter = GmailChatbotAdapter()
result = adapter.fetch_jobs(limit=5)
options = adapter.get_options()
status = adapter.get_status()
```

## 🚀 Usage Examples

### Basic Usage - Fetch Jobs
```python
from gmail import fetch_jobs_for_chatbot

# Fetch jobs using hardcoded credentials
jobs = fetch_jobs_for_chatbot(limit=5)
print(jobs)
# Output: {'status': 'success', 'count': 5, 'emails': [...], 'message': '✅ Found 5 job notifications'}
```

### Get Gmail Status
```python
from gmail import get_gmail_status

status = get_gmail_status()
print(status)
# Output: {'status': 'connected', 'email': 'ggpsmo@gmail.com', 'authenticated': True, ...}
```

### Get Available Chatbot Options
```python
from gmail import get_gmail_options

options = get_gmail_options()
for option in options['options']:
    print(f"- {option['name']}: {option['description']}")
```

### Direct Service Usage
```python
from gmail import GmailService

service = GmailService()

# Fetch emails
emails = service.fetch_naukri_emails(limit=10)

# Get email count
count = service.get_email_count(limit=5)

# Get configured email
email = service.get_email_address()
```

## 🤖 Chatbot Integration

The module provides a complete chatbot adapter with the following commands:

### Available Commands

1. **fetch_jobs**
   - Description: Fetch latest Naukri job notifications
   - Parameters: `limit` (optional, default: 5)
   - Returns: Dictionary with email count and data

2. **get_status**
   - Description: Check Gmail service status
   - Parameters: None
   - Returns: Status information including authentication status

3. **get_options**
   - Description: Get available chatbot options
   - Parameters: None
   - Returns: List of available commands and parameters

### Executing Commands via Adapter

```python
from gmail import get_chatbot_adapter

adapter = get_chatbot_adapter()

# Execute fetch_jobs command
result = adapter.execute_command('fetch_jobs', limit=5)

# Execute get_status command
status = adapter.execute_command('get_status')

# Execute get_options command
options = adapter.execute_command('get_options')
```

## 📧 Features

✅ Hardcoded email and passcode (no user input needed)  
✅ Automatic IMAP connection to Gmail  
✅ Filters Naukri job notification emails  
✅ Returns clean, structured email data  
✅ Error handling and logging  
✅ Chatbot-compatible interface  
✅ Configurable email limit  

## 🔧 Configuration Options

In `gmail_config.py`, you can customize:

- `DEFAULT_EMAIL_LIMIT`: Number of emails to fetch (default: 5)
- `SEARCH_QUERY`: Email search filter (default: `FROM "naukri"`)
- `IMAP_SERVER`: Gmail IMAP server (default: `imap.gmail.com`)
- `IMAP_PORT`: IMAP port (default: 993)

## 🔗 Integration with Main Application

Import and use in your main chatbot application:

```python
from anget_gmail_naukari_job_notifications.gmail import get_chatbot_adapter

# Get the adapter
gmail_adapter = get_chatbot_adapter()

# Use in chatbot menu
options = gmail_adapter.get_options()

# Execute user commands
result = gmail_adapter.execute_command('fetch_jobs', limit=10)
```

## ⚠️ Important Notes

- Credentials are hardcoded for automated operation
- Gmail account must have IMAP enabled
- App password (not regular password) is used for security
- Emails are filtered to show only Naukri job notifications
- Module handles authentication errors gracefully

## 📝 License

Part of the Naukri Gmail Job Notifications Agent project.

