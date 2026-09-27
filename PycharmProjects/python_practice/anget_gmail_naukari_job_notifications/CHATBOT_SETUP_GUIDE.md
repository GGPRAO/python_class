# ⚡ Gmail Chatbot Setup - Choose Your Approach

You have **3 simple options** to run a chatbot UI. Pick one! 👇

---

## 🎯 Option 1: Streamlit (Recommended - Easiest)

**Best for:** Quick setup, beautiful UI, minimal code

### Setup (2 minutes)
```bash
cd anget_gmail_naukari_job_notifications
pip install -r requirements.txt
streamlit run simple_chatbot.py
```

### What opens
- Beautiful web interface at `http://localhost:8501`
- Built-in Streamlit magic ✨
- No extra configuration needed

### Features
✅ Fetch jobs with one click  
✅ View service status  
✅ See available commands  
✅ Download jobs as text  
✅ Responsive design  

### Code
- **File:** `simple_chatbot.py` (150 lines, very readable)
- **No API needed** - Direct Python integration

---

## 🌐 Option 2: Flask (Better UX)

**Best for:** Custom HTML/CSS, better performance, API-based

### Setup (2 minutes)
```bash
cd anget_gmail_naukari_job_notifications
pip install flask
python flask_chatbot.py
```

### What opens
- Modern web interface at `http://localhost:5000`
- REST API backend
- Smooth animations

### Features
✅ Beautiful gradient UI  
✅ REST API (`/api/fetch`, `/api/status`)  
✅ Smooth animations  
✅ Lightweight (one HTML file)  

### Code
- **File:** `flask_chatbot.py` (one file, ~400 lines)
- **Backend:** Python Flask
- **Frontend:** Vanilla HTML/CSS/JS

---

## 📱 Option 3: Simple Python CLI

**Best for:** Terminal lovers, no browser needed

### Setup (immediate)
```bash
cd anget_gmail_naukari_job_notifications
python simple_cli.py
```

### What it does
- Terminal-based interface
- Simple menu system
- No extra dependencies

### Features
✅ Fetch jobs in terminal  
✅ View job details  
✅ Simple menu-driven  

---

## 📊 Comparison Table

| Feature | Streamlit | Flask | CLI |
|---------|-----------|-------|-----|
| Setup Time | 2 min | 2 min | 1 min |
| Learning Curve | Easy | Easy | Very Easy |
| UI Quality | Modern | Excellent | Text |
| Performance | Good | Excellent | Fast |
| Browser Needed | Yes | Yes | No |
| Code Complexity | Low | Low | Very Low |

---

## 🚀 I Recommend: Streamlit + Flask Combo

### Why?
- Streamlit for **development** (fast iteration)
- Flask for **production** (better performance)

### Setup both:
```bash
# Terminal 1 - Streamlit dev
streamlit run simple_chatbot.py

# Terminal 2 - Flask production
python flask_chatbot.py
```

---

## 📁 File Structure

```
anget_gmail_naukari_job_notifications/
│
├── simple_chatbot.py          ← Streamlit UI (recommended)
├── flask_chatbot.py           ← Flask API + HTML UI
├── simple_cli.py              ← CLI version (coming)
│
├── gmail/
│   ├── __init__.py
│   ├── gmail_config.py        (ggpsmo@gmail.com credentials)
│   ├── gmail_service.py       (fetches emails)
│   └── chatbot_adapter.py     (chatbot interface)
│
├── requirements.txt           (all dependencies)
└── SIMPLE_CHATBOT_SETUP.md   (detailed guide)
```

---

## 🔧 Installation

### 1. Install Python 3.8+
```bash
python --version  # Should be 3.8 or higher
```

### 2. Install Dependencies
```bash
cd anget_gmail_naukari_job_notifications
pip install -r requirements.txt
```

### 3. Choose & Run

#### Streamlit
```bash
streamlit run simple_chatbot.py
```

#### Flask
```bash
python flask_chatbot.py
```

---

## 🎯 Quick Start Examples

### Streamlit
```bash
streamlit run simple_chatbot.py
# Opens http://localhost:8501 automatically
# Click "Fetch Jobs" button
```

### Flask
```bash
python flask_chatbot.py
# Opens http://localhost:5000
# Click "Fetch Jobs" button
# Or use API: curl http://localhost:5000/api/fetch?limit=5
```

### Using as API
```bash
# Fetch jobs via API
curl "http://localhost:5000/api/fetch?limit=10"

# Check status
curl "http://localhost:5000/api/status"

# Get commands
curl "http://localhost:5000/api/commands"
```

---

## 🔐 Credentials

These are **hardcoded** in `gmail/gmail_config.py`:

- **Email:** `ggpsmo@gmail.com`
- **Password:** `lodqerzdhzjppwph`

No manual setup needed! ✅

---

## ❌ Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit
```

### "Gmail connection failed"
- Check internet connection
- Credentials in `gmail/gmail_config.py` might be wrong
- Gmail account might need app-specific password

### "Port already in use"
- Streamlit: Changes port automatically
- Flask: Kill process or use different port:
```bash
python -c "import socket; s=socket.socket(); s.bind(('',0)); print(s.getsockname()[1])"
python flask_chatbot.py --port=5001
```

### "No jobs found"
- You might not have Naukri emails
- Try different search query in `gmail/gmail_config.py`
- Change `SEARCH_QUERY = 'FROM "naukri"'`

---

## 📚 Learn More

### Streamlit Docs
https://docs.streamlit.io

### Flask Docs
https://flask.palletsprojects.com

### Gmail Setup
See `gmail/README.md` and `gmail/QUICK_REFERENCE.md`

---

## 🎉 You're All Set!

Pick one, run it, and start fetching jobs! 

**Questions?** Check the Gmail module docs or error messages.

**Want more features?** Edit the Python files - they're straightforward!

---

**Made with ❤️ for job hunters** 🚀

