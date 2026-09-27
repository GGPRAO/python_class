# ✅ Launch Checklist - Maths Problem Solver Bot

Use this checklist to ensure everything is ready before launching the bot.

## Pre-Launch Checklist

### System Preparation
- [ ] Computer has 4GB+ RAM available
- [ ] Enough disk space (3GB for Ollama model)
- [ ] Internet connection is active and stable
- [ ] No system updates pending that require restart

### Python & Dependencies
- [ ] Python 3.8+ installed (`python --version`)
- [ ] Python added to system PATH
- [ ] Pip updated: `pip install --upgrade pip`
- [ ] requirements.txt dependencies installed: `pip install -r requirements.txt`

### Ollama Setup
- [ ] Ollama downloaded from https://ollama.ai
- [ ] Ollama installed successfully
- [ ] Ollama service started: `ollama serve` (running in background/terminal)
- [ ] Model pulled: `ollama pull qwen2:1.5b`
- [ ] Model verified: `ollama list` (shows qwen2:1.5b)

### Project Files
- [ ] Navigated to correct folder: `C:\Users\YOUR_USER\PycharmProjects\ai_bots\maths_bot`
- [ ] File `app.py` exists in folder
- [ ] File `requirements.txt` exists in folder
- [ ] File `START_CHATBOT.bat` or `START_CHATBOT.ps1` exists (Windows)

### System Ports
- [ ] Port 8501 is available (not used by other apps)
- [ ] Firewall allows localhost connections
- [ ] No VPN enabled that might block localhost

## Launch Steps

### Step 1: Prepare Environment
- [ ] Open Command Prompt or PowerShell
- [ ] Navigate to maths_bot folder
- [ ] Verify Ollama is running in another window

### Step 2: Choose Launch Method

**Option A: Easiest (Windows)**
- [ ] Double-click `START_CHATBOT.bat`
- [ ] Wait for "Opening in browser" message
- [ ] Go to Step 4

**Option B: PowerShell (Windows)**
- [ ] Open PowerShell in project folder
- [ ] Type: `.\START_CHATBOT.ps1`
- [ ] Wait for browser to open
- [ ] Go to Step 4

**Option C: Manual (All Systems)**
- [ ] Type: `streamlit run app.py`
- [ ] Wait for "You can now view your Streamlit app" message
- [ ] Go to Step 4

### Step 3: Browser Opening
- [ ] Browser opens automatically, OR
- [ ] Manually go to: `http://localhost:8501`
- [ ] Page loads successfully
- [ ] Title shows: "🧮 Maths Problem Solver Bot"

### Step 4: Verify Interface
- [ ] Left sidebar visible with preferences
- [ ] Chat area shows empty (ready for input)
- [ ] Input field visible at bottom
- [ ] "Send" button clickable

## Testing the Bot

### Quick Test
- [ ] Select a difficulty level from sidebar
- [ ] Select a math category
- [ ] Click one of the example problem buttons
- [ ] Wait for bot response (may take 10-20 seconds)
- [ ] Bot returns a solution with steps

### Full Test
- [ ] Type in input: "What is 2 + 3?"
- [ ] Click "Send" button
- [ ] Bot responds with answer
- [ ] Response appears in chat history
- [ ] Response is formatted properly

### Feature Test
- [ ] Enable "Verify answer with alternate method"
- [ ] Ask a problem and verify response includes verification
- [ ] Enable "Show practice problems"
- [ ] Ask a problem and verify it includes practice problems

## Troubleshooting During Launch

### Browser Won't Open
**Action**:
- [ ] Manually type: `http://localhost:8501` in browser
- [ ] If still not working, restart the bot

### Ollama Connection Error
**Action**:
- [ ] Stop current bot (Ctrl+C)
- [ ] Open new terminal/cmd window
- [ ] Type: `ollama serve`
- [ ] Wait 3 seconds for Ollama to start
- [ ] Go back to first terminal and restart bot

### Model Not Found Error
**Action**:
- [ ] Stop the bot (Ctrl+C)
- [ ] Type: `ollama pull qwen2:1.5b`
- [ ] Wait for download to complete
- [ ] Type: `ollama list` (verify model appears)
- [ ] Restart the bot

### Port Already in Use
**Action**:
- [ ] Stop the bot (Ctrl+C)
- [ ] Find what's using port 8501:
  - Windows: `netstat -ano | findstr 8501`
  - macOS/Linux: `lsof -i :8501`
- [ ] Close the application using that port
- [ ] Restart the bot

### Slow Responses
**Action**:
- [ ] Close other applications
- [ ] Check available RAM (need 4GB+)
- [ ] Check internet connection speed
- [ ] Restart the bot

## Post-Launch Checklist

### After First Successful Launch
- [ ] Chat with bot using different questions
- [ ] Test all difficulty levels
- [ ] Test all math categories
- [ ] Try all learning styles
- [ ] Enable/disable verification and practice problems
- [ ] Use quick example buttons

### Settings Verification
- [ ] Sidebar controls work smoothly
- [ ] Changing preferences shows in bot responses
- [ ] Chat history displays correctly
- [ ] Scrolling through chat works

### Performance Verification
- [ ] Response time is acceptable (under 30 seconds)
- [ ] UI is responsive (no freezing)
- [ ] No error messages in bot responses
- [ ] Chat history doesn't cause slowdown

## Daily Use Checklist

### Before Each Session
- [ ] Ollama is running: `ollama serve` (in separate terminal)
- [ ] Port 8501 is free
- [ ] Computer has adequate RAM

### Starting the Bot
- [ ] Run: `streamlit run app.py` OR double-click launcher
- [ ] Wait for "Local URL" message
- [ ] Open browser to http://localhost:8501

### During Use
- [ ] Set your difficulty level
- [ ] Select your topic
- [ ] Choose your learning style
- [ ] Ask clear, specific questions
- [ ] Review solutions carefully

### Ending Session
- [ ] Close browser tab (optional)
- [ ] Stop bot: Press Ctrl+C in terminal
- [ ] Ollama continues running (can be left on)

## Optional: Performance Optimization

### For Faster Responses
- [ ] Close all unnecessary applications
- [ ] Disable heavy browser extensions
- [ ] Use wired internet if possible
- [ ] Ensure 8GB+ RAM available

### For Better Accuracy
- [ ] Use more detailed difficulty levels
- [ ] Include more context in questions
- [ ] Enable "Detailed Explanation" learning style
- [ ] Enable "Verify answer" option

## Maintenance Checklist

### Weekly
- [ ] Restart computer
- [ ] Clear browser cache if needed
- [ ] Update Python packages: `pip install --upgrade -r requirements.txt`

### Monthly
- [ ] Check for Ollama updates: https://ollama.ai
- [ ] Check for Streamlit updates: `pip install --upgrade streamlit`
- [ ] Review any error messages in terminal

### Emergency Reset
If something isn't working:
1. [ ] Close the bot (Ctrl+C)
2. [ ] Restart Ollama: `ollama serve`
3. [ ] Restart the bot: `streamlit run app.py`

## Support Resources

### Quick Help
- [ ] Check QUICK_REFERENCE.md for common questions
- [ ] Review README.md for detailed information
- [ ] Check SETUP_GUIDE.md if setup issues

### Online Resources
- [ ] Streamlit docs: https://streamlit.io/docs
- [ ] Ollama docs: https://ollama.ai/
- [ ] Python docs: https://python.org/docs

## Success Indicators ✨

You'll know everything is working when:
✅ Browser opens automatically on launch
✅ Bot responds within 30 seconds
✅ Solutions are well-formatted
✅ Explanations are clear
✅ All sidebar features work
✅ No error messages appear
✅ Chat history displays properly

---

## Quick Reference: Common Commands

```bash
# Start Ollama service
ollama serve

# Pull AI model
ollama pull qwen2:1.5b

# List available models
ollama list

# Start the bot
streamlit run app.py

# Run with different port
streamlit run app.py --server.port 8502

# Check Python version
python --version

# Check installed packages
pip list

# Update packages
pip install --upgrade -r requirements.txt
```

---

**✅ All Set?** Great! Enjoy using the Maths Problem Solver Bot! 🎉

For issues, revisit the troubleshooting sections above.


