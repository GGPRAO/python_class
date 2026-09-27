# 📚 Gmail Chatbot - Complete Index

## 🎯 START HERE

**New user?** Read this first: [`SETUP_COMPLETE.md`](SETUP_COMPLETE.md)

**Want quick ref?** See: [`QUICK_START.md`](QUICK_START.md)

**3-second start:**
```bash
streamlit run simple_chatbot.py
```

---

## 📁 Files & Folders

### 🎨 UI Applications (Choose 1)
| File | Type | Best For | Start Command |
|------|------|----------|---|
| `simple_chatbot.py` | Streamlit | **Development, Easy** | `streamlit run simple_chatbot.py` |
| `flask_chatbot.py` | Flask + HTML | Production, Custom UI | `python flask_chatbot.py` |
| `simple_cli.py` | Terminal Menu | SSH, No Browser | `python simple_cli.py` |

### 📖 Documentation
| File | Purpose |
|------|---------|
| `SETUP_COMPLETE.md` | Complete setup summary ⭐ |
| `QUICK_START.md` | Quick reference card |
| `CHATBOT_SETUP_GUIDE.md` | Detailed guide for all UIs |
| `SIMPLE_CHATBOT_SETUP.md` | Streamlit-specific guide |
| `README.md` | General project info |

### 🔌 Gmail Module
| File | Purpose |
|------|---------|
| `gmail/__init__.py` | Package initialization |
| `gmail/gmail_config.py` | Hardcoded credentials |
| `gmail/gmail_service.py` | Email fetching logic |
| `gmail/chatbot_adapter.py` | Chatbot interface |
| `gmail/README.md` | Module documentation |
| `gmail/QUICK_REFERENCE.md` | API quick ref |

### 🛠️ Configuration
| File | Purpose |
|------|---------|
| `requirements.txt` | All dependencies |
| `mail_config.py` | Email configuration |
| `test_gmail_folder.py` | Setup verification |

---

## 🚀 Getting Started

### 1. Install (2 minutes)
```bash
cd anget_gmail_naukari_job_notifications
pip install -r requirements.txt
```

### 2. Choose Your UI
```bash
# Option A: Streamlit (Easiest) ⭐
streamlit run simple_chatbot.py

# Option B: Flask (Best UX)
python flask_chatbot.py

# Option C: CLI (Terminal)
python simple_cli.py
```

### 3. Use It!
- Click "Fetch Jobs"
- Select email limit
- View results
- Done! 🎉

---

## 📊 UI Comparison

| Feature | Streamlit | Flask | CLI |
|---------|-----------|-------|-----|
| Setup Time | 30s | 30s | 10s |
| UI Quality | Good | Excellent | Text |
| Best For | Dev | Prod | SSH |
| Browser | Yes | Yes | No |
| API | No | Yes | No |
| Code | 150 | 400 | 250 |

---

## 🎯 Which UI Should I Use?

### 👤 "I want the easiest setup"
→ **Streamlit** (`simple_chatbot.py`)
- Just run it
- Beautiful by default
- Auto-reloads

### 👤 "I want the best looking UI"
→ **Flask** (`flask_chatbot.py`)
- Custom HTML/CSS
- REST API included
- Production-ready

### 👤 "I'm on SSH / no browser"
→ **CLI** (`simple_cli.py`)
- Terminal menu
- No dependencies
- Works everywhere

---

## 🔐 Credentials (Hardcoded)

```
Email: ggpsmo@gmail.com
Password: lodqerzdhzjppwph
Location: gmail/gmail_config.py
Setup: ✅ Not needed!
```

---

## ✨ Features

All UIs support:
- ✅ Fetch Naukri job emails
- ✅ Filter by limit (1-20)
- ✅ View job details
- ✅ Check status
- ✅ See commands
- ✅ Error handling
- ✅ Timeout protection

Additional (Streamlit):
- ✅ Download as text

Additional (Flask):
- ✅ REST API
- ✅ Custom styling

---

## 🌐 URLs

After running:
- **Streamlit:** http://localhost:8501
- **Flask:** http://localhost:5000
- **Flask API:**
  - `/api/fetch?limit=5` - Fetch jobs
  - `/api/status` - Status
  - `/api/commands` - Commands

---

## 📚 Reading Order

**For Quick Setup:**
1. This file (index)
2. `QUICK_START.md` (reference)
3. Run your chosen UI

**For Detailed Learning:**
1. `SETUP_COMPLETE.md` (overview)
2. `CHATBOT_SETUP_GUIDE.md` (detailed)
3. `gmail/README.md` (Gmail module)

**For Development:**
1. `simple_chatbot.py` (read the code)
2. `gmail/chatbot_adapter.py` (understand adapter)
3. `gmail/gmail_service.py` (understand service)

---

## 🎨 Customization

### Change Credentials
Edit `gmail/gmail_config.py`:
```python
EMAIL = "your@email.com"
PASSCODE = "your-password"
```

### Change Search Query
Edit `gmail/gmail_config.py`:
```python
SEARCH_QUERY = 'FROM "naukri"'  # Change this
```

### Customize UI (Streamlit)
Edit `simple_chatbot.py`:
- Change colors/styling in CSS
- Add new buttons
- Modify layout

### Customize UI (Flask)
Edit `flask_chatbot.py`:
- Modify HTML in the route
- Add API endpoints
- Change styling

### Customize CLI
Edit `simple_cli.py`:
- Add menu options
- Change prompts
- Add features

---

## ❌ Troubleshooting

### Import Error
```bash
pip install -r requirements.txt
```

### Gmail Connection Failed
- Check internet
- Edit `gmail/gmail_config.py`
- Verify credentials

### Port in Use
- Streamlit auto-changes port
- Flask: Use different port

### No Jobs Found
- Check if you have Naukri emails
- Edit search query

See full guide: `CHATBOT_SETUP_GUIDE.md`

---

## 🔄 Workflow

```
Choose UI
   ↓
Install dependencies
   ↓
Run application
   ↓
Click "Fetch Jobs"
   ↓
View results
   ↓
Optional: Download/Export
```

---

## 📞 Support

### Quick Issues
- Error? Read the error message
- Port issue? Different port auto-used
- Gmail? Check credentials

### Deep Issues
- Read `CHATBOT_SETUP_GUIDE.md`
- Check `gmail/README.md`
- See `gmail/QUICK_REFERENCE.md`

### Want Modifications
- Edit the `.py` files directly
- They're well-commented
- Simple and readable

---

## 🎯 Next Steps

1. ✅ Read `SETUP_COMPLETE.md`
2. ✅ Install: `pip install -r requirements.txt`
3. ✅ Run: `streamlit run simple_chatbot.py`
4. ✅ Click "Fetch Jobs"
5. ✅ Enjoy! 🎉

---

## 📖 Document Map

```
START HERE (You are here!)
  ├─→ SETUP_COMPLETE.md (Complete overview)
  │     ├─→ QUICK_START.md (Reference card)
  │     ├─→ CHATBOT_SETUP_GUIDE.md (Detailed guide)
  │     └─→ SIMPLE_CHATBOT_SETUP.md (Streamlit only)
  │
  ├─→ simple_chatbot.py (Streamlit app)
  ├─→ flask_chatbot.py (Flask app)
  └─→ simple_cli.py (CLI app)

Gmail Module:
  ├─→ gmail/__init__.py
  ├─→ gmail/gmail_config.py
  ├─→ gmail/gmail_service.py
  ├─→ gmail/chatbot_adapter.py
  ├─→ gmail/README.md
  └─→ gmail/QUICK_REFERENCE.md
```

---

## 🎉 You're Ready!

Everything is set up. Just:
```bash
streamlit run simple_chatbot.py
```

Happy job hunting! 🚀

---

**Last Updated:** April 25, 2026  
**Status:** ✅ Complete & Ready to Use  
**Version:** 1.0

