# ⚡ QUICK START GUIDE

## 🚀 Get Running in 5 Minutes

### Step 1: Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

### Step 2: Start Ollama (Required for AI)
```bash
# Pull the Qwen2 1.5B model (lightweight, fast)
ollama pull qwen2:1.5b

# Start Ollama service
ollama serve
```
Keep this terminal open!

### Step 3: Run the App (1 min)
```bash
streamlit run ai_streamlit.py
```

### Step 4: Open in Browser
- Automatically opens at `http://localhost:8501`
- Or manually visit that address

---

## 🔐 Configure Gmail (2 min)

### Get App Password:
1. Go to [Google Account](https://myaccount.google.com)
2. Click **Security** (left sidebar)
3. Enable **2-Step Verification** if not already
4. Click **App passwords**
5. Select "Mail" and "Windows Computer"
6. Copy the generated password

### In Streamlit App:
1. Enter your Gmail address
2. Paste the 16-character App Password
3. Click "🔄 Fetch Jobs"

---

## ✅ Verify Setup

Run this quick test:

```bash
# Test imports
python -c "import streamlit; import ollama; import mail_config; print('✅ All imports OK')"

# Test Ollama
ollama pull llama3
```

---

## 📊 Common Tasks

### Fetch 10 Latest Jobs
1. Set slider to "10" in sidebar
2. Click "🔄 Fetch Jobs"

### Read Job Summary
- Click any email row to expand
- See AI-extracted: Role, Company, Location, Experience

### Troubleshoot Issues

| Problem | Solution |
|---------|----------|
| "Connection failed" | Check Gmail password, enable IMAP |
| "Ollama error" | Ensure `ollama serve` is running |
| "No emails found" | Check Naukri emails exist, try 10+ limit |
| "Page not opening" | Check `http://localhost:8501` manually |

---

## 📁 File Overview

```
anget_gmail_naukari_job_notifications/
├── ai_streamlit.py       ← RUN THIS
├── mail_config.py        ← Gmail fetcher
├── clean_email.py        ← HTML cleaner
├── summarize_emails.py   ← AI summarizer
├── requirements.txt      ← Dependencies
├── README.md             ← Full documentation
└── NAVIGATION_GUIDE.md   ← Architecture guide
```

---

## 🎯 Next Steps

- [ ] Complete setup
- [ ] Run Ollama service
- [ ] Launch Streamlit app
- [ ] Configure Gmail
- [ ] Fetch your first job alerts
- [ ] Read full README.md for advanced features

---

**Need Help?** Check NAVIGATION_GUIDE.md or README.md

Happy job hunting! 🎉

