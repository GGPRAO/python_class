# 🤖 Qwen AI Chat - ChatGPT Style UI

A beautiful, modern ChatGPT-like interface for your local Ollama Qwen2 model.

## ✨ Features

✅ **Beautiful Modern UI**
- Gradient purple design (like ChatGPT)
- Smooth animations and transitions
- Responsive mobile-friendly layout
- Real-time message display

✅ **Full Chat Functionality**
- Send and receive messages
- Full conversation history
- Loading indicators
- Error handling

✅ **Fast & Local**
- Runs locally on your machine
- No internet required
- Direct connection to Ollama
- Privacy-friendly

## 🚀 Quick Start

### Option 1: Using the Batch File (Easiest)
1. Double-click `run_chatgpt_ui.bat`
2. Wait for the server to start
3. Open http://localhost:5000 in your browser
4. Start chatting!

### Option 2: Manual Setup
1. Install dependencies:
   ```bash
   pip install flask ollama
   ```

2. Make sure Ollama is running with your model:
   ```bash
   ollama serve qwen2:1.5b
   ```

3. Run the Flask app:
   ```bash
   python flask_chatgpt_ui.py
   ```

4. Open http://localhost:5000 in your browser

## 📋 Requirements

- Python 3.7+
- Flask
- Ollama (with qwen2:1.5b model)
- Modern web browser

## 🎯 How It Works

1. **Frontend**: Beautiful HTML/CSS/JavaScript interface
2. **Backend**: Flask server handles API requests
3. **Model**: Ollama with Qwen2 1.5B model
4. **Communication**: JSON REST API

## 🛠️ Configuration

To change the model, edit `flask_chatgpt_ui.py`:

```python
MODEL_NAME = "your-model-name"  # Change this
```

Supported Ollama models:
- qwen2:1.5b (default)
- qwen2:7b
- llama2:7b
- mistral:7b
- neural-chat:7b
- And many more!

## 📁 Files

- `flask_chatgpt_ui.py` - Flask backend server
- `chatgpt_ui.html` - Frontend interface (included in Flask app)
- `run_chatgpt_ui.bat` - Quick launch script
- `README.md` - This file

## 🐛 Troubleshooting

### PyArrow DLL Error
If you get: "ImportError: DLL load failed while importing lib"
- **Solution**: This Flask version avoids that issue entirely!

### Ollama Connection Error
If the chat doesn't work:
1. Check if Ollama is running: `ollama serve`
2. Verify the model: `ollama list`
3. Check if qwen2:1.5b is available

### Port Already in Use
If port 5000 is busy:
1. Edit `flask_chatgpt_ui.py`
2. Change `port=5000` to another port (e.g., 5001)

## 🎨 Customization

### Change Colors
Edit the CSS in `chatgpt_ui.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change Model Name
Edit `flask_chatgpt_ui.py`:
```python
MODEL_NAME = "your-model"
```

### Add Features
The app is built with:
- **Backend**: Python Flask (easy to extend)
- **Frontend**: Vanilla JavaScript (no dependencies)
- **API**: Simple JSON REST endpoints

## 📊 API Endpoints

### POST /api/chat
Send a message and get a response
```json
{
  "message": "Hello, how are you?"
}
```

### POST /api/clear
Clear conversation history

### GET /api/history
Get full conversation history

## ⚡ Performance

- **Response Time**: Depends on model size (1.5B is fast)
- **Memory**: ~4GB for qwen2:1.5b
- **CPU**: Works on CPU, better with GPU

## 📝 Notes

- The app stores conversation history in memory
- History is cleared when the app restarts
- Each user session has its own conversation
- No data is sent to external services

## 🤝 Support

If you encounter issues:
1. Check if Ollama is running
2. Verify the model is installed
3. Try restarting the app
4. Check browser console (F12) for errors

## 📄 License

Free to use and modify!

---

**Enjoy chatting with your local AI! 🚀**

