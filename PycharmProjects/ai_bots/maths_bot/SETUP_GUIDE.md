# 📖 Setup Guide - Maths Problem Solver Bot

Complete step-by-step guide to set up and run the Maths Solver Bot on your system.

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 7+, macOS 10.12+, or Linux (Ubuntu 18.04+)
- **RAM**: 4GB
- **Disk Space**: 3GB (for Ollama model)
- **Internet**: Broadband connection (for model download)
- **Python**: 3.8 or higher

### Recommended Requirements
- **RAM**: 8GB+
- **Disk Space**: 5GB
- **Processor**: Multi-core processor (Intel i5/Ryzen 5 or better)
- **Internet**: High-speed connection

## Step 1: Install Python

### Windows
1. Go to https://www.python.org/downloads
2. Click "Download Python 3.11" (or latest 3.x version)
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete

### Verify Python Installation
Open Command Prompt and type:
```bash
python --version
```
Should show: `Python 3.8.0` or higher

### macOS
Using Homebrew (recommended):
```bash
brew install python3
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

## Step 2: Install Ollama

Ollama provides the AI model that powers the bot.

### Windows
1. Download from https://ollama.ai
2. Run the installer (.exe file)
3. Follow installation prompts
4. Ollama will run in the background

### macOS
1. Download from https://ollama.ai
2. Open the .dmg file
3. Drag Ollama to Applications
4. Launch from Applications folder

### Linux
```bash
curl https://ollama.ai/install.sh | sh
```

### Verify Ollama Installation

Open a new Command Prompt/Terminal and run:
```bash
ollama --version
```

Should show version information.

## Step 3: Pull the AI Model

The bot uses the Qwen 2 1.5B model. Download it:

```bash
ollama pull qwen2:1.5b
```

This will:
- Download ~900MB model file
- Setup the model for use
- Take 5-10 minutes depending on internet speed

**Wait until download completes before proceeding!**

### Verify Model
```bash
ollama list
```

Should show: `qwen2:1.5b` in the list

### Start Ollama Service

Keep Ollama running in background. On Windows, it starts automatically. On macOS/Linux:

```bash
ollama serve
```

Leave this terminal open while using the bot.

## Step 4: Clone/Navigate to Project

### Option A: If starting fresh
Create a folder and copy the `maths_bot` folder into it.

### Option B: Navigate to existing folder
```bash
cd C:\Users\YOUR_USERNAME\PycharmProjects\ai_bots\maths_bot
```

Replace `YOUR_USERNAME` with your actual username.

## Step 5: Install Python Dependencies

### Windows Command Prompt
```bash
pip install -r requirements.txt
```

### macOS/Linux Terminal
```bash
pip3 install -r requirements.txt
```

This installs:
- **streamlit** (Web interface)
- **ollama** (AI connection)
- **python-dateutil** (Date handling)

Wait for all packages to install (may take 2-3 minutes).

## Step 6: Verify Installation

Create a test file to verify everything works. In the project folder, create `test.py`:

```python
import streamlit as st
import ollama

st.write("Testing imports...")
print("✓ Streamlit works")
print("✓ Ollama library works")
```

Run it:
```bash
streamlit run test.py
```

If a web page opens, installation is successful!

## Step 7: Launch the Bot

### Windows - Easiest Method (Recommended)
Simply double-click: **START_CHATBOT.bat**

It will:
1. Check prerequisites
2. Install dependencies
3. Launch the bot
4. Open browser automatically

### Windows - PowerShell Method
```powershell
.\START_CHATBOT.ps1
```

### Manual Start (All Systems)
```bash
streamlit run app.py
```

## Step 8: Access the Bot

Once launched, your default browser will open to:
```
http://localhost:8501
```

If not, open your browser and go to that URL.

## Configuration

### Adjust Streamlit Settings (Optional)

Create `.streamlit/config.toml` in the project folder:

```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[client]
showErrorDetails = true

[server]
port = 8501
headless = true
runOnSave = true
```

### Change AI Model (Advanced)

Edit `app.py`, find line 140:
```python
model="qwen2:1.5b"
```

Change to another Ollama model:
```python
model="llama2"  # For better accuracy but slower
```

First pull the new model:
```bash
ollama pull llama2
```

## Troubleshooting

### Issue: "Python not found"
**Solution**:
1. Reinstall Python
2. During installation, CHECK "Add Python to PATH"
3. Restart computer
4. Verify: `python --version`

### Issue: "Ollama service not responding"
**Solution**:
1. Make sure Ollama is installed
2. Open new terminal/cmd and run: `ollama serve`
3. Keep that terminal open
4. The bot will now work

### Issue: "Model qwen2:1.5b not found"
**Solution**:
1. Pull the model: `ollama pull qwen2:1.5b`
2. Wait for download to complete
3. Verify: `ollama list`
4. Restart the bot

### Issue: "Port 8501 already in use"
**Solution 1** - Close other Streamlit apps

**Solution 2** - Use different port:
```bash
streamlit run app.py --server.port 8502
```

### Issue: "Connection refused" or "404 errors"
**Solution**:
1. Stop the bot (Ctrl+C)
2. Make sure Ollama is running in another terminal
3. Restart the bot

### Issue: Very slow responses
**Solution**:
1. Close other applications
2. Ensure at least 4GB RAM available
3. Check internet connection
4. Reduce other CPU-heavy tasks

### Issue: "SSL: CERTIFICATE_VERIFY_FAILED"
**Solution** (macOS):
1. Applications → Python 3.x → Install Certificates.command
2. Run it and wait for completion

## Performance Tips

1. **Close Unnecessary Apps**: More RAM available for bot
2. **Use Wired Internet**: More stable connection
3. **Keep Ollama Running**: Don't close its terminal
4. **Adequate RAM**: 8GB+ recommended for smooth operation
5. **SSD Disk**: Faster model loading

## Advanced: Using Different Models

### Faster but Less Accurate
```bash
ollama pull orca-mini
ollama pull mistral
```

### Slower but More Accurate
```bash
ollama pull llama2
ollama pull neural-chat
```

Edit `app.py` line 140 to change the model.

## Uninstall

### Remove Ollama
- Windows: Settings → Apps → Remove Ollama
- macOS: Applications → Drag Ollama to Trash
- Linux: `sudo apt-get remove ollama`

### Remove Python Packages
```bash
pip uninstall streamlit ollama python-dateutil
```

## Next Steps

1. ✅ **Read QUICK_REFERENCE.md** for quick examples
2. ✅ **Try Example Problems** in the quick buttons
3. ✅ **Adjust Preferences** in the sidebar
4. ✅ **Explore Different Categories** 
5. ✅ **Read Full README.md** for detailed documentation

## Getting Help

### Common Resources
- Python: https://www.python.org/
- Ollama: https://ollama.ai/
- Streamlit: https://streamlit.io/
- Documentation: See README.md in project

### Check Logs
Look at the terminal where you launched the bot for error messages.

---

**Installation Complete!** 🎉

You're now ready to use the Maths Problem Solver Bot. Have fun learning!


