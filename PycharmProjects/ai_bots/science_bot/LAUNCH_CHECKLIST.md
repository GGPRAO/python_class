# 🔬 Science Bot - Launch Checklist

Pre-launch verification checklist to ensure everything is properly configured.

## ✅ System Requirements Verification

Before launching, verify your system meets the requirements:

### Operating System
- [ ] Windows 10/11, macOS 10.15+, or Linux
- [ ] System has at least 4GB RAM
- [ ] At least 3GB free disk space

### Python Installation
- [ ] Python 3.8+ is installed
- [ ] Python is in system PATH
  ```bash
  python --version  # Should show 3.8 or higher
  ```

### Internet Connection
- [ ] Internet is working
- [ ] Can access https://ollama.ai
- [ ] Can access localhost:8501

---

## 📦 Installation Verification

### Python Packages
Run each command and verify success:

```bash
# Check Streamlit
streamlit --version  # Should show 1.28.1 or compatible

# Check Python packages
pip list | findstr streamlit  # Windows
pip list | grep streamlit      # Mac/Linux
```

- [ ] Streamlit installed
- [ ] Ollama package installed
- [ ] python-dateutil installed

Run this to verify all:
```bash
pip install -r requirements.txt --upgrade
```

- [ ] All packages installed successfully
- [ ] No error messages shown

---

## 🤖 Ollama Verification

### Ollama Installation
```bash
ollama --version  # Should show version number
```
- [ ] Ollama is installed

### Ollama Service Running
Check in multiple ways:

**Method 1 - Check System Tray**
- [ ] Look for Ollama icon in system tray (bottom right)
- [ ] Ollama icon is visible

**Method 2 - Browser Test**
- [ ] Open http://localhost:11434 in browser
- [ ] You should see "Ollama is running"

**Method 3 - Command Test**
```bash
ollama serve  # Should show "Listening on..."
```
- [ ] Ollama is running on port 11434

### Model Download
```bash
ollama list  # Should show qwen2:1.5b
```

If not listed, download:
```bash
ollama pull qwen2:1.5b  # Wait for complete message
```

- [ ] qwen2:1.5b model is listed
- [ ] Model file downloaded (1+ GB)
- [ ] Model is ready to use

---

## 🔧 Configuration Verification

### Port Availability

**Check if port 8501 is available:**

**Windows:**
```powershell
netstat -ano | findstr :8501  # Should show nothing
```

**Mac/Linux:**
```bash
lsof -i :8501  # Should show nothing
```

- [ ] Port 8501 is available
- [ ] No other application using port 8501

If port 8501 is busy, you can use a different port:
```bash
streamlit run app.py --server.port 8502
```

### File Structure

Check that all files exist:
```
C:\Users\YOUR_NAME\PycharmProjects\ai_bots\science_bot\
├── app.py                    [ ]
├── requirements.txt          [ ]
├── START_CHATBOT.ps1        [ ]
├── START_CHATBOT.bat        [ ]
├── README.md                [ ]
├── SETUP_GUIDE.md           [ ]
├── QUICK_REFERENCE.md       [ ]
├── PROJECT_INDEX.md         [ ]
├── FILE_INDEX.md            [ ]
├── LAUNCH_CHECKLIST.md      [ ]
└── CUSTOMER_GUIDE.md        [ ]
```

- [ ] All required files present
- [ ] No missing files

---

## 🚀 Pre-Launch Verification

### Run Ollama First
1. Open Command Prompt or Terminal
2. Run: `ollama serve`
3. Wait for message: "Listening on..."
4. Leave it running in background

- [ ] Ollama service started
- [ ] Service listening on localhost:11434

### Navigate to Project Directory
```bash
cd C:\Users\YOUR_NAME\PycharmProjects\ai_bots\science_bot
```

- [ ] Working directory is correct
- [ ] All files visible with `ls` or `dir`

### Test Ollama Connection

**PowerShell Test:**
```powershell
Invoke-WebRequest -Uri "http://localhost:11434"
```

**Command Prompt Test:**
```cmd
curl http://localhost:11434
```

Should show "Ollama is running"

- [ ] Can connect to Ollama service
- [ ] Response received: "Ollama is running"

---

## 🎯 Launch Verification

### Choose Launch Method

**Option A - PowerShell Script (Windows)**
```powershell
.\START_CHATBOT.ps1
```

- [ ] Script runs without errors
- [ ] Browser opens automatically
- [ ] App visible at http://localhost:8501

**Option B - Batch File (Windows)**
```cmd
START_CHATBOT.bat
```

- [ ] Batch file runs
- [ ] Browser opens to http://localhost:8501
- [ ] App loads successfully

**Option C - Direct Command**
```bash
streamlit run app.py
```

- [ ] Streamlit starts
- [ ] Shows: "You can now view your Streamlit app..."
- [ ] Browser opens or go to http://localhost:8501

### App Loads Successfully
In your browser at http://localhost:8501:

- [ ] Page title shows "🔬 Science Formula & Concept Bot"
- [ ] Sidebar visible on left with:
  - [ ] Difficulty Level dropdown
  - [ ] Science Subject dropdown
  - [ ] Learning Style options
  - [ ] Checkboxes for derivations and applications
  - [ ] Topic input field
- [ ] Chat area in center with message input
- [ ] Example questions at bottom

---

## ⚠️ Troubleshooting During Launch

### Issue: "Ollama is not running"

**Quick Fix:**
1. Open new terminal/command prompt
2. Run: `ollama serve`
3. Wait 10 seconds
4. Refresh browser (F5)

- [ ] Ollama started
- [ ] Error resolved

### Issue: "Connection refused" Error

**Fix:**
1. Verify Ollama running (see above)
2. Check: http://localhost:11434
3. If not responding, restart Ollama

- [ ] Ollama connection verified
- [ ] Error resolved

### Issue: "Streamlit: command not found"

**Fix:**
```bash
pip install streamlit==1.28.1
```

- [ ] Streamlit installed
- [ ] Try launch again

### Issue: Port 8501 already in use

**Fix Option 1 - Stop other app using port:**
```powershell
netstat -ano | findstr :8501  # Find process ID
taskkill /PID [ID] /F         # Kill the process
```

**Fix Option 2 - Use different port:**
```bash
streamlit run app.py --server.port 8502
```

- [ ] Port available or alternate port used
- [ ] App launches successfully

### Issue: "Model not found" Error

**Fix:**
```bash
ollama pull qwen2:1.5b
```

- [ ] Model downloaded
- [ ] Try launching again

### Issue: App runs but slow

**Possible Causes:**
- [ ] Other programs using RAM - close them
- [ ] Slow internet - check connection
- [ ] Disk full - free up space
- [ ] Ollama overwhelmed - restart it

---

## ✨ Success Indicators

After launching, verify these success indicators:

### UI Elements
- [ ] 🔬 Title displays correctly
- [ ] Sidebar loads with all options
- [ ] Chat area ready for input
- [ ] Example questions displayed
- [ ] Send button functional

### Functionality
- [ ] Can select difficulty level
- [ ] Can select science subject
- [ ] Can select learning style
- [ ] Can input chat message
- [ ] Can click Send button

### AI Response
1. Type a test question: "What is F=ma?"
2. Click Send
3. Wait for response (may take 5-30 seconds)

- [ ] Bot responds with answer
- [ ] Response contains relevant information
- [ ] No error messages shown
- [ ] Response appears in chat history

### Full Success
- [ ] App launches without errors
- [ ] All UI elements present
- [ ] Can configure preferences
- [ ] Can ask questions
- [ ] Receives AI responses

---

## 📋 Final Checklist Before Using

### Environment Ready
- [ ] Ollama running in background
- [ ] Internet connection active
- [ ] Port 8501 available
- [ ] Enough disk space (>500MB free)
- [ ] System has adequate RAM

### Application Ready
- [ ] Python 3.8+ installed
- [ ] All packages installed
- [ ] All project files present
- [ ] No error messages on startup
- [ ] UI displays correctly

### Features Ready
- [ ] Difficulty level selector works
- [ ] Science subject selector works
- [ ] Learning style selection works
- [ ] Chat input field functional
- [ ] Send button responsive

### AI Ready
- [ ] Ollama connected
- [ ] Model (qwen2:1.5b) available
- [ ] Can ask questions
- [ ] Receives responses
- [ ] Responses are relevant

### All Green?
- [ ] Yes → You're ready! Start using the Science Bot! 🚀
- [ ] No → Review "Troubleshooting" section above

---

## 🎓 Ready to Use!

If all items are checked, your Science Bot is ready!

### Next Steps
1. **First Question**: Try asking "What is Newton's Second Law?"
2. **Explore Subjects**: Try different science subjects
3. **Adjust Style**: Try different learning styles
4. **Check Help**: See [CUSTOMER_GUIDE.md](CUSTOMER_GUIDE.md) for tips

### Support
If issues occur:
1. Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
2. See [SETUP_GUIDE.md](SETUP_GUIDE.md) troubleshooting
3. Review [CUSTOMER_GUIDE.md](CUSTOMER_GUIDE.md) for usage tips

---

**Status**: ✅ Ready to Launch
**Version**: 1.0
**Last Updated**: April 2026

Enjoy learning science! 🔬✨

