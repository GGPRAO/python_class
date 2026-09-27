# 🚗 Cars Compare Bot - Setup Guide

A complete step-by-step guide to set up and run the Cars Compare Bot.

## Prerequisites

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **Ollama** ([Download](https://ollama.ai))
- **Windows 10+, Mac, or Linux**

## Step 1: Install Python

### Windows
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. ⚠️ **Important**: Check "Add Python to PATH"
4. Click Install Now

Verify installation:
```powershell
python --version
```

### Mac
```bash
brew install python3
```

### Linux
```bash
sudo apt-get install python3 python3-pip
```

## Step 2: Install Ollama

### All Platforms
1. Visit https://ollama.ai
2. Download and install for your OS
3. Follow the installation wizard
4. After installation, Ollama will run in the background

### Verify Ollama Installation
```bash
ollama --version
```

## Step 3: Pull the Required Model

Open a terminal and run:
```bash
ollama pull qwen2:1.5b
```

This will download the AI model (approximately 1GB). Wait for it to complete.

Verify the model is installed:
```bash
ollama list
```

## Step 4: Set Up the Project

### Navigate to Project Directory
```powershell
cd C:\Users\USER\PycharmProjects\ai_bots\cars_compare_bot
```

### Create Virtual Environment (Optional but Recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- streamlit (Web interface)
- ollama (AI integration)
- pandas (Data handling)
- python-dateutil (Date utilities)

## Step 5: Start the Application

### Make sure Ollama is Running

Open a terminal and ensure Ollama is running:
```bash
ollama serve
```

Keep this terminal open while using the chatbot.

### Start the Cars Compare Bot

**Windows - Option 1 (Easiest):**
Double-click `START_CHATBOT.bat`

**Windows - Option 2 (PowerShell):**
```powershell
.\START_CHATBOT.ps1
```

**Windows - Option 3 (Manual):**
```bash
streamlit run app.py
```

**Mac/Linux:**
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Step 6: Verify Everything Works

1. You should see the Cars Compare Bot interface
2. Click on "Compare Tesla Model 3 vs BMW 3 Series" quick button
3. You should get a response with car comparisons

✅ If you see the response, the setup is successful!

## Troubleshooting

### Issue: "ollama: command not found" or "ollama is not recognized"

**Solution:**
- Reinstall Ollama from https://ollama.ai
- Make sure Ollama is in your system PATH
- Restart your terminal after installation

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
pip install streamlit==1.28.1
```

### Issue: "Connection refused" or "Cannot connect to Ollama"

**Solution:**
1. Make sure Ollama is running in a separate terminal
2. Run: `ollama serve`
3. Wait a few seconds before starting the chatbot
4. Make sure nothing else is using port 11434 (Ollama's default port)

### Issue: Slow responses or hanging

**Solution:**
1. Check your system has at least 8GB RAM
2. Close other applications
3. Make sure your internet connection is stable
4. Try restarting Ollama

### Issue: Model not found

**Solution:**
```bash
ollama pull qwen2:1.5b
```

## Configuration

### Change AI Model

Edit `app.py` and change this line:
```python
response = ollama.chat(
    model="qwen2:1.5b",  # Change this
```

To a different model like:
- `ollama2:7b` (Larger, better quality)
- `mistral:7b` (Alternative model)

First pull the model:
```bash
ollama pull mistral:7b
```

### Change Port

By default, Streamlit runs on port 8501. To use a different port:
```bash
streamlit run app.py --server.port 8502
```

### Disable Browser Auto-Open

```bash
streamlit run app.py --logger.level=error
```

## Production Deployment

For deploying on a server:

1. Install dependencies on the server
2. Use a process manager like `pm2` or `systemd`
3. Set up Ollama to run as a service
4. Configure a reverse proxy (nginx/Apache)
5. Use SSL/TLS for security

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 4GB | 8GB+ |
| Disk Space | 2GB | 5GB+ |
| Python | 3.8 | 3.10+ |
| Ollama | Latest | Latest |

## Performance Tips

1. **Increase RAM for faster responses**
   - More RAM = faster model execution
   - Minimum 8GB recommended

2. **Use GPU if available**
   - CUDA for NVIDIA GPUs
   - Metal for Mac

3. **Close background apps**
   - Free up system resources
   - Faster response times

4. **Use lighter models if needed**
   - Smaller models = faster but less detailed responses
   - Larger models = slower but more accurate

## Getting Help

1. Check README.md for features and usage
2. Review QUICK_REFERENCE.md for common commands
3. Verify Ollama is running with: `ollama serve`
4. Check system resources with Task Manager (Windows) or Activity Monitor (Mac)

## Next Steps

1. Explore the chatbot features
2. Try different car comparisons
3. Customize the car database
4. Adjust UI colors and styling
5. Add more car models to the database

---

**Setup Complete! Enjoy using the Cars Compare Bot! 🚗**

