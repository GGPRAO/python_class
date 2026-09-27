# 🔬 Science Bot - Setup Guide

A complete step-by-step guide to set up and run the Science Formula & Concept Bot on your computer.

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Step-by-Step Installation](#step-by-step-installation)
3. [Installing Ollama](#installing-ollama)
4. [Launching the Bot](#launching-the-bot)
5. [First Time Usage](#first-time-usage)
6. [Troubleshooting](#troubleshooting)

---

## ⚙️ System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 3GB free (for Ollama model)
- **Python**: Version 3.8 or higher
- **Internet**: Required for setup

### Recommended Setup
- **RAM**: 8GB+
- **CPU**: Multi-core processor (4+ cores)
- **GPU**: Optional (for faster processing)
- **Disk**: SSD for faster model loading

---

## 📥 Step-by-Step Installation

### Step 1: Install Python (if not already installed)

1. **Download Python**
   - Visit: https://www.python.org/downloads/
   - Download Python 3.10 or 3.11 (latest stable version)

2. **Install Python**
   - Run the installer
   - ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
   - Click "Install Now"

3. **Verify Installation**
   - Open Command Prompt or PowerShell
   - Type: `python --version`
   - You should see: `Python 3.10.x` or similar

### Step 2: Install Required Python Packages

1. **Open Command Prompt or PowerShell**
   - Press `Win + R`
   - Type: `cmd` or `powershell`
   - Press Enter

2. **Navigate to Science Bot Directory**
   ```bash
   cd C:\Users\YOUR_USERNAME\PycharmProjects\ai_bots\science_bot
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   This will install:
   - Streamlit (UI framework)
   - Ollama (AI backend)
   - Python-dateutil (date utilities)

4. **Verify Installation**
   ```bash
   pip list
   ```
   You should see: streamlit, ollama, python-dateutil listed

---

## 🤖 Installing Ollama

### Windows Installation

1. **Download Ollama**
   - Visit: https://ollama.ai
   - Click "Download"
   - Select "Download for Windows"

2. **Install Ollama**
   - Run the downloaded `.exe` file
   - Follow the installation wizard
   - Complete the installation

3. **Start Ollama Service**
   - Ollama should start automatically
   - Look for the Ollama icon in system tray (bottom right)
   - If not running, search for "Ollama" and start it

4. **Pull the AI Model**
   - Open Command Prompt or PowerShell
   - Type: `ollama pull qwen2:1.5b`
   - Wait for download to complete (~1-2 GB)
   - You should see: "success" message

5. **Verify Ollama is Running**
   ```bash
   ollama list
   ```
   You should see: `qwen2:1.5b    ...`

### macOS Installation

1. Download from https://ollama.ai
2. Open the `.dmg` file
3. Drag Ollama to Applications
4. Launch from Applications
5. Run: `ollama pull qwen2:1.5b`

### Linux Installation

```bash
curl https://ollama.ai/install.sh | sh
ollama pull qwen2:1.5b
```

---

## 🚀 Launching the Bot

### Method 1: Using PowerShell Script (Windows)

1. **Open PowerShell as Administrator**
   - Right-click PowerShell
   - Select "Run as Administrator"

2. **Navigate to Science Bot Directory**
   ```powershell
   cd C:\Users\YOUR_USERNAME\PycharmProjects\ai_bots\science_bot
   ```

3. **Allow Script Execution** (if needed)
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Run the Launcher**
   ```powershell
   .\START_CHATBOT.ps1
   ```

### Method 2: Using Batch File (Windows)

1. **Navigate to Science Bot Directory**
   - Open File Explorer
   - Go to `C:\Users\YOUR_USERNAME\PycharmProjects\ai_bots\science_bot`

2. **Double-click `START_CHATBOT.bat`**
   - Command window will open
   - Bot will launch automatically
   - Browser will open at `http://localhost:8501`

### Method 3: Direct Command (All Platforms)

1. **Open Command Prompt or Terminal**
2. **Navigate to Science Bot Directory**
   ```bash
   cd C:\Users\YOUR_USERNAME\PycharmProjects\ai_bots\science_bot
   ```
3. **Run Streamlit**
   ```bash
   streamlit run app.py
   ```

---

## 🎓 First Time Usage

### On First Launch

1. **Browser Opens Automatically**
   - If not, visit: http://localhost:8501

2. **See the Science Bot Interface**
   - Title: "🔬 Science Formula & Concept Bot"
   - Left sidebar with preferences
   - Chat area in center
   - Example questions at bottom

3. **Configure Preferences**
   - Select **Difficulty Level** (e.g., "High School (9-12)")
   - Choose **Science Subject** (e.g., "🔋 Physics")
   - Pick **Learning Style** (e.g., "Detailed Theory")
   - Check/uncheck options for derivations and applications
   - (Optional) Enter current topic

4. **Ask Your First Question**
   - Type in the input field
   - Example: "What is Newton's Second Law?"
   - Press "Send" or hit Enter
   - Wait for response from AI

### Tips for Best Results

- **Be Specific**: "Explain E=mc²" is better than "physics"
- **Match Difficulty**: Select appropriate level for your knowledge
- **Use Follow-ups**: Ask "explain the variables" or "show an example"
- **Clear History**: Refresh page to start fresh conversation
- **Take Notes**: Copy important formulas and explanations

---

## 🔧 Troubleshooting

### Problem: "Ollama is not running"

**Solution A: Start Ollama**
- Search for "Ollama" in Windows Start menu
- Click to launch Ollama
- Wait 10 seconds, then refresh browser

**Solution B: Check Service**
- Look in system tray (bottom right)
- Click Ollama icon if present
- Wait for service to start

### Problem: "Module not found" or Import errors

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Problem: "Model not found"

**Solution:**
```bash
ollama pull qwen2:1.5b
```

Wait for download to complete, then try again.

### Problem: Port 8501 already in use

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

Or close other apps using port 8501.

### Problem: Very slow responses

**Causes & Solutions:**
- **Low RAM**: Close other applications
- **Internet Slow**: Check connection speed
- **Disk Full**: Check disk space (need 2GB+ free)
- **CPU Throttling**: Restart computer

### Problem: "Connection refused" error

**Solution:**
1. Ensure Ollama is running
2. Check: http://localhost:11434 in browser
3. Should see "Ollama is running"
4. If not, restart Ollama

### Problem: App crashes on launch

**Solution:**
1. Update Streamlit: `pip install --upgrade streamlit`
2. Clear cache: Delete `~/.streamlit/cache` folder
3. Restart computer
4. Try again

---

## 📞 Getting Help

### Common Resources
- **Ollama Help**: https://ollama.ai/help
- **Streamlit Docs**: https://docs.streamlit.io
- **Python Help**: https://python.org/help

### Checking System

**Verify Python**
```bash
python --version
```

**Verify Streamlit**
```bash
streamlit --version
```

**Verify Ollama**
```bash
ollama list
```

**Check Internet**
```bash
ping google.com
```

---

## ✅ Checklist

Before you start using the Science Bot, verify:

- [ ] Python 3.8+ installed
- [ ] Python added to PATH
- [ ] Requirements installed (`pip install -r requirements.txt`)
- [ ] Ollama downloaded and installed
- [ ] Ollama service running (check system tray)
- [ ] Model pulled (`ollama list` shows qwen2:1.5b)
- [ ] Port 8501 available (no other app using it)
- [ ] Internet connection active

If all checkboxes are done, you're ready to use the Science Bot!

---

## 🎉 Success!

You're all set! The Science Bot is ready to help you explore science formulas and concepts. Enjoy learning! 🔬✨

For more information, see:
- [README.md](README.md) - Features and usage guide
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Common questions and answers

