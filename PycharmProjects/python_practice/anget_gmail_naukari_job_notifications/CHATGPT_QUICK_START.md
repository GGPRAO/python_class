# ChatGPT-Like Email Assistant - Quick Start Guide

## 🚀 START HERE - Choose Your Interface

### **Option 1: CLI (Command Line) ⭐ FASTEST**
```bash
Double-click: run_chatgpt_cli.bat
Or command: python chatgpt_like_interface.py
```
✅ Fast • Lightweight • No browser needed

### **Option 2: Web Browser 🌐 BEAUTIFUL**
```bash
Double-click: run_chatgpt_web.bat
Or command: python chatgpt_web_interface.py
Then open: http://localhost:5000
```
✅ Beautiful UI • Email previews • Real-time chat

---

## 💬 Example Conversations

### Simple Query
```
You: Python developer jobs
Bot: ✅ Found 3 matching emails...
```

### Complex Query
```
You: Remote backend engineer with 15-20 lpa and 5+ years
Bot: ✅ Found 2 matching emails...
```

### Command
```
You: limit 50
Bot: ✅ Search depth updated to 50
```

---

## 📋 All Commands

| Command | What It Does |
|---------|-------------|
| `help` | Show all commands |
| `examples` | Show 10 example queries |
| `settings` | Show current settings |
| `status` | Check Gmail connection |
| `history` | Show chat history |
| `clear` | Clear chat history |
| `limit <num>` | Set email limit (1-100) |
| `summarize` | Summarize last results |
| `exit` / `quit` | Exit the assistant |

---

## 🎯 Quick Queries

**Single Filter:**
```
Python jobs
Remote positions
Bangalore locations
15-20 lpa
5+ years experience
TCS jobs
```

**Two Filters:**
```
Python developer in Bangalore
Backend engineer remote
Data scientist 20 lpa
```

**All Filters:**
```
Python developer in Bangalore with 15-20 lpa and 3-5 years
Backend engineer remote 20 lpa 5+ years
Frontend developer Mumbai 10-15 lpa 2 years
```

---

## ⚙️ Setup in 3 Steps

### 1️⃣ Get Gmail App Password
- Go: https://myaccount.google.com/apppasswords
- Select: "Mail" + "Windows Computer"
- Copy: 16-character password

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run!
```bash
python chatgpt_like_interface.py
```

---

## 📁 Files You'll Use

| File | Purpose |
|------|---------|
| `chatgpt_like_interface.py` | CLI chatbot (MAIN) |
| `chatgpt_web_interface.py` | Web interface |
| `run_chatgpt_cli.bat` | One-click CLI launcher |
| `run_chatgpt_web.bat` | One-click web launcher |
| `requirements.txt` | All dependencies |
| `CHATGPT_SETUP_GUIDE.md` | Full guide |

---

## 🔥 Most Common Uses

### Use Case 1: Quick Job Search
```bash
# Start CLI
python chatgpt_like_interface.py

# Ask
Python developer Bangalore

# Done!
```

### Use Case 2: Browse Emails Web UI
```bash
# Start Web
python chatgpt_web_interface.py

# Open: http://localhost:5000

# Chat in browser
```

### Use Case 3: Complex Search
```bash
# Set limit high
limit 50

# Search
Backend engineer 20 lpa 5+ years remote

# Get results!
```

---

## ✅ Checklist Before Starting

- [ ] Python 3.8+ installed
- [ ] Gmail App Password ready
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] You're ready to go!

---

## 🆘 Quick Fixes

| Problem | Solution |
|---------|----------|
| "Gmail error" | Verify app password in console |
| "No results" | Try `limit 50` |
| "Port in use" | Close other apps using port 5000 |
| "Module not found" | Run `pip install -r requirements.txt` |

---

## 🎉 That's It!

You now have a **ChatGPT-like interface that fetches from your Gmail!**

### What You Can Do:
✅ Ask naturally about your emails
✅ Search by role, location, salary, experience
✅ Get instant job notifications
✅ Manage conversation history
✅ Use web or CLI interface

### Start Now:
```bash
python chatgpt_like_interface.py
```

Then ask:
```
Python developer in Bangalore 15-20 lpa
```

**Happy job hunting! 🎉**

---

**Version 3.0 | Ready to Use ✅**

