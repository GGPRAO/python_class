# ChatGPT-Like Email Assistant - Complete Setup Guide

## 🎯 Overview

This is a **ChatGPT-like conversational AI interface** that directly accesses your Gmail. Ask it anything about your emails, and it will fetch, search, and analyze them for you!

### Key Features:
- ✅ **Natural Language Interface** - Talk to it like ChatGPT
- ✅ **Email Search & Filtering** - Searches your mailbox intelligently
- ✅ **Multi-Interface Support** - CLI, Web, and native options
- ✅ **Job Extraction** - Pulls job details from Naukri emails
- ✅ **Conversation History** - Remembers your chat history
- ✅ **No PyArrow Issues** - Lightweight and optimized

---

## 📦 Installation

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Gmail Access

Gmail requires authentication. You have two options:

#### Option A: Use App Password (Recommended ✅)
1. Enable 2-Factor Authentication on your Google Account
2. Go to https://myaccount.google.com/apppasswords
3. Select "Mail" and "Windows Computer"
4. Copy the generated 16-character password
5. Save it safely

#### Option B: Create Environment File
Create a `.env` file in the project directory:
```
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password
```

---

## 🚀 How to Run

### Option 1: CLI Interface (Command Line) ⭐ BEST FOR QUICK USE
```bash
python chatgpt_like_interface.py
```

**Features:**
- Lightweight
- No browser needed
- Instant results
- Full color support

**Example session:**
```
You: Python developer jobs in Bangalore
🤖 Assistant: Found 3 matching emails...

You: Show remote positions
🤖 Assistant: Found 5 remote positions...

You: limit 50
✅ Search depth updated to 50

You: exit
👋 Goodbye!
```

---

### Option 2: Web Interface (Browser) 🌐 BEST FOR VISUAL USE
```bash
python chatgpt_web_interface.py
```

Then open: http://localhost:5000

**Features:**
- Beautiful ChatGPT-like UI
- Email previews
- Sidebar navigation
- Real-time updates

---

### Option 3: Streamlit Interface (Alternative)
```bash
streamlit run ai_streamlit.py
```

---

## 💬 How to Use

### Natural Language Queries
Just type naturally! The AI understands context:

```
"Show me Python developer jobs"
"Find remote positions in Bangalore with 15-20 lpa"
"What are the latest backend engineer positions?"
"Data scientist jobs at Google"
"5+ years experience roles"
```

### Special Commands

| Command | Purpose |
|---------|---------|
| `help` | Show all commands |
| `examples` | Show 10 example queries |
| `settings` | Show current settings |
| `status` | Check Gmail connection |
| `history` | Show chat history |
| `clear` | Clear chat history |
| `limit <num>` | Set search depth (1-100) |
| `exit` / `quit` | Exit the assistant |

---

## 🎯 Example Queries

### Simple Queries
```
"Python jobs"
"Remote positions"
"Bangalore jobs"
"20 lpa salary"
"5+ years"
```

### Intermediate
```
"Python developer in Bangalore"
"Backend engineer remote 15-20 lpa"
"Frontend jobs 3-5 years"
```

### Advanced (All Criteria)
```
"Python developer in Bangalore with 15-20 lpa and 3-5 years"
"Backend engineer remote 20 lpa 5+ years at TCS"
"Data scientist Mumbai 25 lpa 2-4 years"
```

---

## ⚙️ Configuration

### Adjust Search Settings

In CLI:
```
limit 10   → Quick search (10 emails)
limit 30   → Detailed search (30 emails)
limit 50   → Comprehensive search (50 emails)
```

In Web UI:
- Use sidebar to change settings
- Adjusts in real-time

---

## 🔍 Advanced Features

### Search Filters

The system automatically extracts:
- **Job Role** (Python, Backend, Frontend, Data Scientist, etc.)
- **Location** (Bangalore, Mumbai, Remote, Pune, etc.)
- **Salary Range** (10-15 lpa, 15-20 lpa, 20+ lpa, etc.)
- **Experience** (Fresher, 2-4 years, 5+ years, etc.)
- **Company** (TCS, Infosys, Google, Amazon, etc.)

### Examples:
```
"Python developer Bangalore 15-20 lpa 3-5 years"
↓
Role: Python Developer
Location: Bangalore
Salary: 15-20 lpa
Experience: 3-5 years

"Frontend engineer at Google remote 20 lpa 5+ years"
↓
Role: Frontend Engineer
Company: Google
Location: Remote
Salary: 20 lpa
Experience: 5+ years
```

---

## 🧪 Testing

### Test the CLI:
```bash
python chatgpt_like_interface.py
```
Type: `examples` to see what it can do

### Test the Web Interface:
```bash
python chatgpt_web_interface.py
```
Visit: http://localhost:5000

---

## ❌ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Gmail connection error" | Check your App Password in .env file |
| "No emails found" | Use `limit 50` to search more emails |
| "Module not found" | Run `pip install -r requirements.txt` |
| "Port already in use" | Change port in code or close other apps |
| "SSL Error" | Update certificates: `pip install --upgrade certifi` |

---

## 📊 File Structure

```
anget_gmail_naukari_job_notifications/
├── chatgpt_like_interface.py    ← CLI Interface (RUN THIS!)
├── chatgpt_web_interface.py     ← Web Interface
├── ai_streamlit.py              ← Streamlit Interface
├── gmail/
│   ├── chatbot_adapter.py       ← Email fetching & filtering
│   ├── job_filter.py            ← Job extraction logic
│   ├── gmail_service.py         ← Gmail API wrapper
│   └── __init__.py
├── requirements.txt             ← Dependencies
└── README.md
```

---

## 🚀 Quick Start (Copy-Paste)

### For CLI:
```bash
cd C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications
pip install -r requirements.txt
python chatgpt_like_interface.py
```

### For Web:
```bash
cd C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications
pip install -r requirements.txt
python chatgpt_web_interface.py
```

Then open: http://localhost:5000

---

## 💡 Tips & Tricks

### Tip 1: Combine Multiple Filters
```
❌ Bad: "Python" "Bangalore" "15-20"
✅ Good: "Python developer in Bangalore 15-20 lpa"
```

### Tip 2: Use Natural Language
```
❌ Bad: "developer backend remote bangalore"
✅ Good: "Backend developer in remote locations"
```

### Tip 3: Increase Results
```
limit 50   ← Search more emails for better results
```

### Tip 4: Save Important Results
```
history    ← Shows all your queries and results
```

---

## 🔐 Security Notes

- ✅ Never share your App Password
- ✅ Keep `.env` file secure (add to .gitignore)
- ✅ Use 2-Factor Authentication on Google
- ✅ App Passwords are safer than actual passwords

---

## 📈 Performance

- **CLI**: Lightning fast, minimal memory
- **Web**: Slightly slower but beautiful UI
- **Search Time**: 2-5 seconds average
- **Email Processing**: Optimized for 100+ emails

---

## 🎉 Features Checklist

- [x] Natural language understanding
- [x] Email fetching from Gmail
- [x] Intelligent job filtering
- [x] Multi-interface support (CLI, Web, Streamlit)
- [x] Conversation history
- [x] Advanced search criteria
- [x] Real-time results
- [x] Error handling
- [x] Configuration options
- [x] ChatGPT-like experience

---

## 📞 Support

If you encounter issues:

1. Check `.env` file is properly configured
2. Verify Gmail App Password is correct
3. Try: `python -m pip install -r requirements.txt --upgrade`
4. Check console output for error messages
5. Try `status` command to verify Gmail connection

---

## 📝 Version

- **Version**: 3.0
- **Status**: ✅ Production Ready
- **Last Updated**: April 25, 2026
- **Interfaces**: CLI, Web (Flask), Streamlit

---

## 🎯 Next Steps

1. ✅ Install requirements
2. ✅ Set up Gmail App Password
3. ✅ Run `python chatgpt_like_interface.py`
4. ✅ Start asking questions!

**That's it! Happy job hunting! 🎉**

---

**Happy Emailing! 📧**

