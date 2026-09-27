# 🔧 Installation Guide - Blocked by Application Control Policy

## Problem

Your system has an **Application Control Policy** that blocks `pip.exe` from running.

```
Program 'pip.exe' failed to run: An Application Control policy has blocked this file
```

---

## Solution Options

### ✅ Option 1: Use Python's Built-in Module Installer (RECOMMENDED)

```powershell
python -m pip install --user streamlit
python -m pip install --user google-auth-oauthlib
python -m pip install --user google-auth-httplib2
python -m pip install --user google-api-python-client
python -m pip install --user ollama
python -m pip install --user beautifulsoup4
python -m pip install --user lxml
```

### ✅ Option 2: Run PowerShell as Administrator

1. Right-click PowerShell
2. Select "Run as Administrator"
3. Then run:
```powershell
pip install -r requirements.txt
```

### ✅ Option 3: Use Python Interactive

```powershell
python -c "import subprocess; subprocess.run(['python', '-m', 'pip', 'install', 'streamlit'])"
```

### ✅ Option 4: Create a Batch File

Create file `install.bat`:
```batch
@echo off
python -m pip install --user streamlit
python -m pip install --user google-auth-oauthlib
python -m pip install --user google-auth-httplib2
python -m pip install --user google-api-python-client
python -m pip install --user ollama
python -m pip install --user beautifulsoup4
python -m pip install --user lxml
echo Installation complete!
pause
```

Then run:
```powershell
.\install.bat
```

---

## Running Streamlit

### ✅ Option 1: Direct Python Module

```powershell
python -m streamlit run ai_streamlit.py
```

### ✅ Option 2: Full Path

```powershell
python -m streamlit run "C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications\ai_streamlit.py"
```

### ✅ Option 3: Create a Batch File

Create `run_streamlit.bat`:
```batch
@echo off
cd C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications
python -m streamlit run ai_streamlit.py
pause
```

Then double-click the batch file.

---

## Step-by-Step (Easiest)

### Step 1: Install Dependencies
```powershell
cd C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications
python -m pip install --user streamlit google-auth-oauthlib google-auth-httplib2 google-api-python-client ollama beautifulsoup4 lxml
```

### Step 2: Start Ollama (in separate PowerShell)
```powershell
ollama serve
```

Keep this running!

### Step 3: Run Application (in main PowerShell)
```powershell
python -m streamlit run ai_streamlit.py
```

Your browser should open at `http://localhost:8501`

---

## If Still Having Issues

### Check Python is Working
```powershell
python --version
```

### Check if pip Works with --user
```powershell
python -m pip --version
```

### Try Installation without --user
```powershell
python -m pip install streamlit
```

### Check if Streamlit Can be Run
```powershell
python -c "import streamlit; print(streamlit.__version__)"
```

---

## Alternative: Use Python's venv

```powershell
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\Activate.ps1

# Install packages (should work in venv)
pip install -r requirements.txt

# Run Streamlit
streamlit run ai_streamlit.py
```

---

## If Your IT Department Blocks Everything

Contact your IT department and request they whitelist:
- Python package installer (pip)
- Streamlit
- Google API libraries
- Ollama

Or ask them to create an exception for your user account.

---

## Quick Reference

| Task | Command |
|------|---------|
| Install packages | `python -m pip install --user streamlit` |
| Install all | `python -m pip install --user -r requirements.txt` |
| Run app | `python -m streamlit run ai_streamlit.py` |
| Check installation | `python -c "import streamlit; print('OK')"` |
| Create batch file | See examples above |

---

## Status

- Application Control Policy: ⚠️ BLOCKING
- Workaround: ✅ AVAILABLE
- Recommended: `python -m pip install --user`
- Then: `python -m streamlit run ai_streamlit.py`

---

**Try Option 1 first - it should work!**

