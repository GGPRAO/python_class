# 🚀 Simple Gmail Chatbot - Quick Start

## What You Have

A **super simple** Streamlit chatbot UI that fetches and displays your Naukri job notifications.

## Files

```
anget_gmail_naukari_job_notifications/
├── simple_chatbot.py         ← Run this to start the chatbot
├── gmail/
│   ├── __init__.py
│   ├── gmail_config.py       (hardcoded: ggpsmo@gmail.com)
│   ├── gmail_service.py      (fetches emails)
│   └── chatbot_adapter.py    (chatbot interface)
└── requirements.txt
```

## Installation

### 1. Install Dependencies
```bash
cd anget_gmail_naukari_job_notifications
pip install -r requirements.txt
```

### 2. Run the Chatbot
```bash
streamlit run simple_chatbot.py
```

This will:
- Open a browser window at `http://localhost:8501`
- Show you the chatbot interface
- Ready to fetch jobs!

## Features

✅ **Fetch Jobs** - Get latest Naukri notifications  
✅ **View Status** - Check Gmail connection status  
✅ **Commands** - See available operations  
✅ **Download** - Export jobs as text file  
✅ **Settings** - Adjust number of emails  

## How to Use

1. **Click "Fetch Jobs"** button
2. Select how many emails to fetch (1-20)
3. Wait for results
4. View jobs inline or download as text

## Credentials

- **Email:** ggpsmo@gmail.com
- **Password:** lodqerzdhzjppwph
- (These are hardcoded in `gmail_config.py`)

## Troubleshooting

### Problem: "ModuleNotFoundError"
```bash
pip install streamlit
```

### Problem: "Gmail connection failed"
- Check internet connection
- Gmail app password might be wrong
- Check `gmail/gmail_config.py`

### Problem: "No jobs found"
- You might not have Naukri emails
- Try searching for "naukri" in your inbox
- Adjust the search query in `gmail_config.py`

## File Structure

```
simple_chatbot.py          (Main UI file - 150 lines)
├── Page config
├── Custom styling
├── Session state
├── Sidebar settings
├── Action buttons
│   ├── Fetch Jobs
│   ├── Service Status
│   └── Available Commands
└── Job display & export
```

## Next Steps

### Option 1: Customize the UI
Edit `simple_chatbot.py` to:
- Change colors/styling
- Add more features
- Modify button labels

### Option 2: Advanced Chatbot
For a true conversational chatbot, use:
- LangChain + OpenAI
- Ollama (local LLM)
- Claude API

### Option 3: Deploy
```bash
# Using Streamlit Cloud
streamlit run simple_chatbot.py --logger.level=debug

# Using Docker
docker run -p 8501:8501 simple_chatbot
```

## Need Help?

1. Check `gmail/README.md` for Gmail module details
2. See `gmail/QUICK_REFERENCE.md` for API docs
3. Run the test: `python test_gmail_folder.py`

---

**That's it!** You now have a working Gmail chatbot UI. 🎉

