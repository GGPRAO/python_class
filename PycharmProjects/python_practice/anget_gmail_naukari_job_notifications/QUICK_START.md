# ⚡ Gmail Chatbot - Quick Reference Card

## 🚀 3-Second Start

```bash
# Option 1: Streamlit (recommended)
streamlit run simple_chatbot.py

# Option 2: Flask
python flask_chatbot.py

# Option 3: CLI (terminal)
python simple_cli.py
```

---

## 📁 What You Have

```
anget_gmail_naukari_job_notifications/
├── simple_chatbot.py       ← Streamlit UI ⭐ EASIEST
├── flask_chatbot.py        ← Flask + HTML (better UX)
├── simple_cli.py           ← Terminal UI
├── gmail/                  ← Gmail module
└── requirements.txt
```

---

## 🎯 Which One Should I Use?

| Need | Use |
|------|-----|
| **Easiest setup** | `streamlit run simple_chatbot.py` |
| **Best looking UI** | `python flask_chatbot.py` |
| **No browser** | `python simple_cli.py` |
| **API access** | Flask (has REST endpoints) |

---

## 🔧 Installation

```bash
# 1. Navigate to folder
cd anget_gmail_naukari_job_notifications

# 2. Install dependencies (one time only)
pip install -r requirements.txt

# 3. Run any of the above
streamlit run simple_chatbot.py
```

---

## 🌐 URLs

- **Streamlit:** http://localhost:8501
- **Flask:** http://localhost:5000
- **API endpoints:**
  - `GET /api/fetch?limit=5` - Fetch jobs
  - `GET /api/status` - Service status
  - `GET /api/commands` - Available commands

---

## 🔐 Credentials (Hardcoded)

```
Email: ggpsmo@gmail.com
Password: lodqerzdhzjppwph
```

No setup needed! ✅

---

## 💻 Commands

### Fetch Jobs
- **Streamlit:** Click "🔄 Fetch Jobs" button
- **Flask:** Click "🔄 Fetch Jobs" button
- **CLI:** Select option 1
- **API:** `curl "http://localhost:5000/api/fetch?limit=10"`

### Check Status
- **Streamlit:** Click "ℹ️ Service Status"
- **Flask:** Click "ℹ️ Service Status"
- **CLI:** Select option 2
- **API:** `curl "http://localhost:5000/api/status"`

### View Commands
- **Streamlit:** Click "🔧 Available Commands"
- **Flask:** (In UI under buttons)
- **CLI:** Select option 3
- **API:** `curl "http://localhost:5000/api/commands"`

---

## ❌ Common Issues

### Problem: "ModuleNotFoundError"
```bash
pip install streamlit  # or flask
```

### Problem: Port already in use
```bash
# Streamlit auto-changes port
# Flask: use different port
python -c "import socket; s=socket.socket(); s.bind(('',0)); print(s.getsockname()[1])"
```

### Problem: Gmail won't connect
- Check internet
- Edit `gmail/gmail_config.py` if credentials wrong
- Try different search term in `SEARCH_QUERY`

### Problem: No jobs found
- You might not have Naukri emails
- Check spam folder
- Edit search query in `gmail/gmail_config.py`

---

## 📚 Files Explained

### `simple_chatbot.py` (150 lines)
- Streamlit-based UI
- Easiest to understand
- Beautiful default styling
- **Best for:** Quick projects

### `flask_chatbot.py` (400 lines)
- Flask backend + HTML/CSS/JS frontend
- REST API included
- Custom styled interface
- **Best for:** Production use

### `simple_cli.py` (250 lines)
- Pure Python terminal UI
- No browser needed
- Simple menu system
- **Best for:** Server/SSH access

### `gmail/` folder
- `gmail_config.py` - Credentials
- `gmail_service.py` - Email fetching
- `chatbot_adapter.py` - Chatbot interface

---

## 🎨 Customization

### Change email limit (Streamlit)
- Use the slider in sidebar

### Change credentials
Edit `gmail/gmail_config.py`:
```python
EMAIL = "your@gmail.com"
PASSCODE = "your-app-password"
```

### Change search query
Edit `gmail/gmail_config.py`:
```python
SEARCH_QUERY = 'FROM "naukri"'  # Change this
```

---

## 🔗 API Examples

### Using curl
```bash
# Fetch 5 jobs
curl "http://localhost:5000/api/fetch?limit=5"

# Check status
curl "http://localhost:5000/api/status"

# Get commands
curl "http://localhost:5000/api/commands"
```

### Using Python
```python
import requests

# Fetch jobs
r = requests.get('http://localhost:5000/api/fetch?limit=5')
print(r.json())

# Check status
r = requests.get('http://localhost:5000/api/status')
print(r.json())
```

### Using JavaScript
```javascript
// Fetch jobs
fetch('http://localhost:5000/api/fetch?limit=5')
  .then(r => r.json())
  .then(data => console.log(data))

// Check status
fetch('http://localhost:5000/api/status')
  .then(r => r.json())
  .then(data => console.log(data))
```

---

## 📊 Feature Comparison

| Feature | Streamlit | Flask | CLI |
|---------|-----------|-------|-----|
| Setup time | 30s | 30s | 10s |
| UI quality | Good | Excellent | Text |
| Browser needed | Yes | Yes | No |
| REST API | No | Yes | No |
| Code lines | 150 | 400 | 250 |
| Performance | Good | Excellent | Fast |

---

## 🎯 Recommended Setup

1. **For development:** Use Streamlit
   ```bash
   streamlit run simple_chatbot.py
   ```

2. **For production:** Use Flask
   ```bash
   python flask_chatbot.py
   ```

3. **For SSH/server:** Use CLI
   ```bash
   python simple_cli.py
   ```

---

## 📖 More Info

- Full guide: `CHATBOT_SETUP_GUIDE.md`
- Streamlit only: `SIMPLE_CHATBOT_SETUP.md`
- Gmail module: `gmail/README.md`
- Gmail API: `gmail/QUICK_REFERENCE.md`

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Install Python 3.8+ | 5 min |
| Install dependencies | 2 min |
| Run Streamlit | 30 sec |
| Run Flask | 30 sec |
| Run CLI | 10 sec |
| Fetch first job | 3-5 sec |

---

## 🎉 Next Steps

1. ✅ Pick a UI (Streamlit/Flask/CLI)
2. ✅ Install dependencies: `pip install -r requirements.txt`
3. ✅ Run it: `streamlit run simple_chatbot.py`
4. ✅ Click "Fetch Jobs"
5. ✅ View your jobs!

**Done!** 🚀

---

## 💬 Support

- **Error?** Check the error message
- **Not working?** See troubleshooting above
- **Want features?** Edit the Python files
- **Questions?** Read the full guides

**Happy job hunting!** 🎯

