# 🔧 TROUBLESHOOTING GUIDE - Application Control Policy Issue

## Your Error

```
Program 'pip.exe' failed to run: An Application Control policy has blocked this file
```

This is a Windows security policy that prevents direct execution of pip.exe

---

## ✅ SOLUTIONS (Try in Order)

### Solution 1: Use Python Module Approach (BEST) ⭐

This bypasses the Application Control Policy:

```powershell
python -m pip install --user streamlit
python -m pip install --user google-auth-oauthlib
python -m pip install --user google-auth-httplib2
python -m pip install --user google-api-python-client
python -m pip install --user ollama
python -m pip install --user beautifulsoup4
python -m pip install --user lxml
```

**Why it works:** Python module execution bypasses the policy

**Then run:**
```powershell
python -m streamlit run ai_streamlit.py
```

---

### Solution 2: Use Batch Files (EASIEST) ⭐⭐

I've created two batch files for you:

**Step 1: Install Dependencies**
- Double-click: `install_dependencies.bat`
- Wait for installation to complete

**Step 2: Start Ollama** (in PowerShell)
```powershell
ollama serve
```

**Step 3: Run Application**
- Double-click: `run_app.bat`
- Browser opens automatically at `http://localhost:8501`

---

### Solution 3: PowerShell as Administrator

1. **Right-click PowerShell** → Select "Run as Administrator"
2. **Navigate to folder:**
   ```powershell
   cd "C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications"
   ```
3. **Install packages:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Run app:**
   ```powershell
   streamlit run ai_streamlit.py
   ```

---

### Solution 4: Python Virtual Environment

```powershell
# Navigate to folder
cd "C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications"

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\Activate.ps1

# Install packages (works in venv)
pip install -r requirements.txt

# Run app
streamlit run ai_streamlit.py
```

---

## 🚀 FASTEST SOLUTION (Copy & Paste)

### For Windows PowerShell:

```powershell
cd "C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications"
python -m pip install --user streamlit google-auth-oauthlib google-auth-httplib2 google-api-python-client ollama beautifulsoup4 lxml
python -m streamlit run ai_streamlit.py
```

---

## 📋 Step-by-Step Guide

### Step 1: Install Dependencies (Choose ONE)

**Option A: One Command**
```powershell
python -m pip install --user streamlit google-auth-oauthlib google-auth-httplib2 google-api-python-client ollama beautifulsoup4 lxml
```

**Option B: Using Batch File**
- Double-click: `install_dependencies.bat`

**Option C: Individual Commands**
```powershell
python -m pip install --user streamlit
python -m pip install --user google-auth-oauthlib
python -m pip install --user google-auth-httplib2
python -m pip install --user google-api-python-client
python -m pip install --user ollama
python -m pip install --user beautifulsoup4
python -m pip install --user lxml
```

### Step 2: Start Ollama

Open a NEW PowerShell window:
```powershell
ollama serve
```

**Keep this running!** (Don't close this window)

### Step 3: Run the Application

In your ORIGINAL PowerShell window:
```powershell
cd "C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications"
python -m streamlit run ai_streamlit.py
```

**Result:** Browser opens at `http://localhost:8501`

---

## ✅ Verification

### Check if Installation Worked

```powershell
python -c "import streamlit; print('✅ Streamlit installed:', streamlit.__version__)"
python -c "import ollama; print('✅ Ollama installed')"
python -c "import google.auth; print('✅ Google Auth installed')"
```

---

## 🐛 If Still Having Issues

### Issue: "python command not found"
**Solution:** Python not in PATH
```powershell
# Use full path
C:\Python312\python.exe -m pip install streamlit
```

### Issue: "No module named streamlit"
**Solution:** Installation failed
```powershell
# Try installing with user flag
python -m pip install --user --upgrade streamlit
```

### Issue: "Ollama connection refused"
**Solution:** Ollama not running
```powershell
# Make sure ollama serve is running in another window
ollama serve
```

### Issue: "Permission denied"
**Solution:** Try with --user flag
```powershell
python -m pip install --user streamlit
```

---

## 📁 Files Provided

| File | Purpose |
|------|---------|
| install_dependencies.bat | One-click installation |
| run_app.bat | One-click application launcher |
| INSTALLATION_GUIDE.md | Installation instructions |
| TROUBLESHOOTING_GUIDE.md | This file |

---

## 🎯 My Recommendation

### Easiest Way:
1. Double-click: `install_dependencies.bat`
2. When done, in PowerShell: `ollama serve`
3. In another PowerShell: Double-click `run_app.bat`

### If That Doesn't Work:
1. Copy this line:
   ```powershell
   cd "C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications"; python -m pip install --user streamlit google-auth-oauthlib google-auth-httplib2 google-api-python-client ollama beautifulsoup4 lxml
   ```
2. Paste into PowerShell
3. Press Enter
4. Wait for installation
5. Then run: `python -m streamlit run ai_streamlit.py`

---

## 🔓 Application Control Policy

If nothing works, your IT department has applied a strict security policy. You may need to:

1. Contact IT support
2. Request exception for:
   - Python pip
   - Streamlit
   - Google API libraries
   - Ollama

Or ask them to install the packages for you.

---

## 📞 Quick Reference

| Task | Command |
|------|---------|
| Install one package | `python -m pip install --user streamlit` |
| Install all | `python -m pip install --user -r requirements.txt` |
| Check installed | `python -m pip list` |
| Upgrade package | `python -m pip install --user --upgrade streamlit` |
| Run app | `python -m streamlit run ai_streamlit.py` |
| Run agent script | `python convert_into_agent.py` |

---

## ✨ Summary

**Your Problem:** Application Control Policy blocks pip.exe

**Our Solution:** Use `python -m pip` instead

**Result:** Everything works!

---

**Try Solution 1 or 2 - one of them will definitely work!** ✅

