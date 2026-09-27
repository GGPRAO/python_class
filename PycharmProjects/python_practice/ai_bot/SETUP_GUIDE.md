# 🤖 Qwen AI ChatGPT-Style UI - Complete Setup Guide

## ⚡ Quick Start (Choose One)

### 🥇 **RECOMMENDED: Simple HTTP Server** (Most Reliable)
This version has **NO PyArrow issues**!

**Option A: Using Batch File (Easiest)**
1. Double-click `run_simple_ui.bat`
2. Wait for "Server running at" message
3. Open http://localhost:5000 in your browser

**Option B: Manual Command**
```bash
python simple_http_ui.py
```

---

### 🥈 **Flask Version** (Feature-Rich)
If you prefer Flask but still get PyArrow errors, try this:

```bash
pip install flask ollama --force-reinstall
python flask_chatgpt_ui.py
```

Or use the batch file:
```
run_chatgpt_ui.bat
```

---

### 🥉 **Streamlit Version** (Original, May Have PyArrow Issues)
```bash
pip install streamlit --upgrade
streamlit run chatgpt_ui.py
```

---

## 🔧 Prerequisites

### 1. Python 3.7+
Check your version:
```bash
python --version
```

### 2. Ollama Running
Before starting the UI, make sure Ollama is serving:
```bash
ollama serve qwen2:1.5b
```

Or just run:
```bash
ollama run qwen2:1.5b
```

### 3. Install Ollama Python Package
```bash
pip install ollama
```

---

## 📁 File Structure

```
ai_bot/
├── test_agent.py                 # Original test script
├── chatgpt_ui.html              # HTML/CSS/JS frontend (shared)
├── simple_http_ui.py            # ⭐ Lightweight HTTP server (RECOMMENDED)
├── flask_chatgpt_ui.py          # Flask backend server
├── chatgpt_ui.py                # Streamlit version
├── run_simple_ui.bat            # ⭐ Quick launcher (RECOMMENDED)
├── run_chatgpt_ui.bat           # Flask launcher
├── README_FLASK_UI.md           # Flask documentation
└── SETUP_GUIDE.md               # This file
```

---

## 🚀 Three UI Options Explained

### 1. **Simple HTTP UI** ✅ RECOMMENDED
- **File**: `simple_http_ui.py`
- **Launcher**: `run_simple_ui.bat`
- **Pros**:
  - ✅ No PyArrow issues
  - ✅ No external dependencies (except ollama)
  - ✅ Pure Python standard library
  - ✅ Fastest startup
  - ✅ Lightest memory usage
- **Cons**: 
  - Fewer advanced features
- **Best For**: Users with AppControl policy issues

### 2. **Flask UI** 
- **File**: `flask_chatgpt_ui.py`
- **Launcher**: `run_chatgpt_ui.bat`
- **Pros**:
  - More features
  - Cleaner API structure
  - Extensible for future features
- **Cons**: 
  - Requires Flask (may have PyArrow conflicts)
- **Best For**: Advanced users who want customization

### 3. **Streamlit UI**
- **File**: `chatgpt_ui.py`
- **Launcher**: `streamlit run chatgpt_ui.py`
- **Pros**:
  - Rapid development
  - Beautiful built-in components
- **Cons**: 
  - PyArrow DLL loading issues on some systems
  - Slower startup
- **Best For**: Development and testing

---

## 🐛 Troubleshooting

### Problem: "DLL load failed while importing lib: Application Control policy"
**Solution**: Use the **Simple HTTP UI** (`simple_http_ui.py`)
- This version doesn't use PyArrow at all
- Run: `python simple_http_ui.py`

### Problem: "ModuleNotFoundError: No module named 'ollama'"
**Solution**:
```bash
pip install ollama
```

### Problem: "Connection refused" when clicking send
**Checklist**:
1. ✅ Is Ollama running? (Open new terminal, run: `ollama serve`)
2. ✅ Is the model downloaded? (Run: `ollama list`)
3. ✅ Is the UI running? (Check terminal window)
4. ✅ Can you reach http://localhost:5000? (Try in browser)

### Problem: "Port 5000 is already in use"
**Solution**: Change the port in the Python file

For `simple_http_ui.py`:
```python
PORT = 5001  # Change from 5000 to 5001
```

For `flask_chatgpt_ui.py`:
```python
app.run(port=5001)  # Change from 5000 to 5001
```

### Problem: Slow responses
**Checklist**:
1. Model size affects speed (1.5B = fast, 7B = slower)
2. CPU vs GPU (GPU is faster)
3. System resources available
4. Model still loading?

---

## 🎨 Customization Guide

### Change Model Name
**In `simple_http_ui.py`:**
```python
MODEL_NAME = "your-model"  # e.g., "mistral:7b", "llama2:7b"
```

**In `flask_chatgpt_ui.py`:**
```python
MODEL_NAME = "your-model"
```

### Available Models
```bash
# List installed models
ollama list

# Download new models
ollama pull mistral:7b
ollama pull llama2:7b
ollama pull neural-chat:7b
ollama pull dolphin-mixtral:latest
```

### Change Colors
Edit `chatgpt_ui.html`:

Find this line:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Try these color combinations:
- **Teal**: `linear-gradient(135deg, #00d4ff 0%, #0099ff 100%)`
- **Green**: `linear-gradient(135deg, #00d4aa 0%, #00aa55 100%)`
- **Orange**: `linear-gradient(135deg, #ff6b35 0%, #ff4500 100%)`
- **Pink**: `linear-gradient(135deg, #ff006e 0%, #fb5607 100%)`

### Change Font
Find in `chatgpt_ui.html`:
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', ...
```

Replace with:
```css
font-family: 'Arial', sans-serif;  /* Classic */
font-family: 'Courier New', monospace;  /* Code-style */
font-family: 'Georgia', serif;  /* Elegant */
```

---

## 📊 Performance Tips

### Speed Up Responses
1. **Use smaller model**: qwen2:1.5b (fastest)
2. **Use GPU**: Install CUDA or Metal for GPU acceleration
3. **Close other apps**: Free up RAM
4. **Reduce context**: Clear history occasionally

### Monitor Performance
- **CPU**: Check Task Manager (Windows)
- **Memory**: Look for RAM usage
- **GPU**: Check GPU usage in Task Manager

### Optimize Model Size
```bash
# Fastest (but less capable)
ollama run qwen2:1.5b

# Balanced (recommended)
ollama run qwen2:7b

# Most capable (slower)
ollama run qwen2:72b
```

---

## 🔐 Security & Privacy

✅ **All local**: No data sent to internet
✅ **Private**: Only you can access it
✅ **Secure**: No authentication needed for local use
⚠️ **Note**: Not suitable for public internet (add authentication first)

---

## 📈 Features

### Chat Interface
- ✅ Send/receive messages
- ✅ Full conversation history
- ✅ Beautiful animations
- ✅ Mobile responsive
- ✅ Dark/light friendly

### Backend Features
- ✅ JSON REST API
- ✅ Error handling
- ✅ Message history
- ✅ Model configuration

---

## 🆘 Getting Help

### Check Logs
Look at the terminal output when running:
```
python simple_http_ui.py
```

### Test Ollama Connection
```python
python
>>> import ollama
>>> response = ollama.chat(model='qwen2:1.5b', messages=[{"role": "user", "content": "Hi"}])
>>> print(response['message']['content'])
```

### Test Web Server
Open browser: http://localhost:5000

Should see:
- ✅ Purple gradient header
- ✅ "Start a Conversation" message
- ✅ Input box at bottom

---

## 📝 Common Commands

```bash
# Start Ollama service
ollama serve

# Run the lightweight UI (RECOMMENDED)
python simple_http_ui.py

# Run Flask UI
python flask_chatgpt_ui.py

# Run Streamlit UI
streamlit run chatgpt_ui.py

# Check installed models
ollama list

# Download a model
ollama pull mistral:7b

# Test direct chat (command line)
ollama run qwen2:1.5b
```

---

## 🎯 Next Steps

1. **Choose an option** above (Simple HTTP recommended)
2. **Install Ollama**: https://ollama.ai
3. **Run the UI**: Use batch file or Python command
4. **Start chatting!** 🚀

---

## ✨ Tips & Tricks

- Type quickly with Tab key support
- Use Shift+Enter for multi-line input (in advanced versions)
- Clear history from settings for fresh start
- Change model without restarting (in advanced versions)
- Use `/clear` command to reset (if implemented)

---

## 📄 Version Info

- **Python**: 3.7+
- **Ollama**: Latest
- **Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)
- **OS**: Windows, Mac, Linux

---

Enjoy chatting with your local AI! 🤖✨

