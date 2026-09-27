# Gmail Module - Quick Reference

## 📦 What's Included

The new `gmail` folder contains a complete, production-ready Gmail integration module with **hardcoded credentials** for your chatbot.

### Files:
- ✅ `gmail_config.py` - Credentials & Configuration
- ✅ `gmail_service.py` - Email Fetching Service
- ✅ `chatbot_adapter.py` - Chatbot Integration
- ✅ `__init__.py` - Package Exports
- ✅ `README.md` - Full Documentation
- ✅ `test_gmail_module.py` - Test Suite
- ✅ `SETUP_SUMMARY.md` - Setup Details
- ✅ `INTEGRATION_EXAMPLES.py` - Integration Examples

## 🔐 Hardcoded Credentials

```
Email: ggpsmo@gmail.com
Passcode: lodqerzdhzjppwph
```

**No user input needed!** Credentials are automatically used.

## 🚀 Get Started (30 seconds)

### Option 1: Fetch Jobs Directly
```python
from gmail import fetch_jobs_for_chatbot

jobs = fetch_jobs_for_chatbot(limit=5)
print(f"Found {jobs['count']} jobs")
```

### Option 2: Use Chatbot Adapter
```python
from gmail import get_chatbot_adapter

adapter = get_chatbot_adapter()
result = adapter.fetch_jobs(limit=5)
print(result['message'])
```

### Option 3: Execute Commands
```python
from gmail import get_chatbot_adapter

adapter = get_chatbot_adapter()

# Get options
options = adapter.get_options()

# Fetch jobs
result = adapter.execute_command('fetch_jobs', limit=5)

# Get status
status = adapter.execute_command('get_status')
```

## 📊 Response Format

### Successful Response
```python
{
    "status": "success",
    "count": 5,
    "emails": [
        {
            "subject": "Naukri Job Title",
            "body": "Email content..."
        },
        # ... more emails
    ],
    "message": "✅ Found 5 job notifications"
}
```

### Error Response
```python
{
    "status": "error",
    "message": "❌ Connection failed",
    "emails": []
}
```

## 🤖 Available Commands

### 1. Fetch Jobs
```python
adapter.execute_command('fetch_jobs', limit=5)
# Returns: {'status': 'success', 'count': 5, 'emails': [...], 'message': '✅ Found 5 job notifications'}
```

### 2. Get Status
```python
adapter.execute_command('get_status')
# Returns: {'status': 'connected', 'email': '...', 'authenticated': True, ...}
```

### 3. Get Options
```python
adapter.execute_command('get_options')
# Returns: {'options': [{...}, ...], 'email': '...'}
```

## 💡 Common Use Cases

### Display in Menu
```python
from gmail import get_gmail_options

options = get_gmail_options()
print("Available Options:")
for opt in options['options']:
    print(f"- {opt['name']}: {opt['description']}")
```

### Handle User Selection
```python
from gmail import get_chatbot_adapter

adapter = get_chatbot_adapter()

if user_choice == "fetch_jobs":
    limit = user_input("How many? (default 5): ") or 5
    result = adapter.fetch_jobs(limit=int(limit))
    print(result['message'])
```

### Check Service Status
```python
from gmail import get_gmail_status

status = get_gmail_status()
if status['authenticated']:
    print("✅ Gmail service is ready!")
else:
    print("❌ Gmail service not available")
```

### Fetch and Display
```python
from gmail import fetch_jobs_for_chatbot

jobs = fetch_jobs_for_chatbot(limit=10)

if jobs['status'] == 'success':
    for i, job in enumerate(jobs['emails'], 1):
        print(f"{i}. {job['subject']}")
        print(f"   {job['body'][:100]}...\n")
else:
    print(f"Error: {jobs['message']}")
```

## 🔧 Configuration

Edit `gmail_config.py` to customize:

```python
# Number of emails to fetch by default
DEFAULT_EMAIL_LIMIT = 5

# Email search filter
SEARCH_QUERY = 'FROM "naukri"'

# IMAP server settings
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993
```

## 📂 Project Integration

### In Your Main App:
```python
from anget_gmail_naukari_job_notifications.gmail import (
    get_chatbot_adapter,
    fetch_jobs_for_chatbot,
    get_gmail_status
)

# Use in your chatbot
gmail_adapter = get_chatbot_adapter()
```

### In Streamlit:
```python
import streamlit as st
from gmail import get_chatbot_adapter

adapter = get_chatbot_adapter()
limit = st.slider("Jobs to fetch", 1, 20, 5)

if st.button("Fetch Jobs"):
    result = adapter.fetch_jobs(limit)
    st.success(result['message'])
```

### In Menu Loop:
```python
from gmail import get_chatbot_adapter

adapter = get_chatbot_adapter()
commands = adapter.get_options()['options']

print("Commands:")
for cmd in commands:
    print(f"- {cmd['name']}")

choice = input("Select: ")
result = adapter.execute_command(choice.split()[0])
```

## ✨ Key Features

✅ **Zero Setup Required** - Just import and use  
✅ **Hardcoded Credentials** - No user input needed  
✅ **Error Handling** - Graceful failure management  
✅ **Async Ready** - Can be used in async contexts  
✅ **Well Tested** - Includes test suite  
✅ **Fully Documented** - Comprehensive API docs  

## 🧪 Run Tests

```bash
python anget_gmail_naukari_job_notifications/gmail/test_gmail_module.py
```

## 📚 Documentation Files

- **README.md** - Full API documentation
- **SETUP_SUMMARY.md** - Setup and configuration details
- **INTEGRATION_EXAMPLES.py** - 8 integration examples
- **test_gmail_module.py** - Working test cases

## ⚠️ Important Notes

1. **Gmail Account Setup:**
   - IMAP must be enabled
   - App Password is used (not regular password)

2. **Automatic Credentials:**
   - Email and passcode are hardcoded
   - No prompts or input required
   - Suitable for automated/service use

3. **Error Handling:**
   - All errors are caught and reported
   - Module won't crash on failures
   - Errors included in response

## 🎯 Next Steps

1. ✅ Module is ready to use
2. 🔄 Import in your chatbot application
3. 📋 Display options from `get_gmail_options()`
4. 🎮 Handle user commands with `execute_command()`
5. 📊 Display results to users

---

**Ready to Use!** 🚀

Start using the Gmail module in your chatbot now.

