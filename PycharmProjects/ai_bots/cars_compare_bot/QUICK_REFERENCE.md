# 🚗 Cars Compare Bot - Quick Reference

Quick commands and common tasks for the Cars Compare Bot.

## Quick Start (30 seconds)

1. **Open two terminals**
   - Terminal 1: Run `ollama serve`
   - Terminal 2: Run `streamlit run app.py`

2. **Open browser**: http://localhost:8501

3. **Try a comparison**: "Compare Tesla Model 3 vs BMW 3 Series"

## Common Commands

### Terminal Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama
ollama serve

# Start the bot
streamlit run app.py

# Pull a model
ollama pull qwen2:1.5b

# List available models
ollama list

# Delete a model
ollama rm model-name
```

## Example Queries

### Car Comparisons
- "Compare Tesla Model 3 vs BMW 3 Series"
- "Honda Civic vs Toyota Corolla"
- "Which is faster: Ford Mustang or Tesla Model 3?"

### Price Queries
- "Best cars under $30,000"
- "Which luxury car is most affordable?"
- "Compare prices of electric vehicles"

### Performance Queries
- "Which car has the fastest 0-60 time?"
- "Compare horsepower: Model 3 vs Mustang"
- "What's the top speed of BMW 3 Series?"

### Efficiency Queries
- "Best fuel-efficient cars"
- "Compare fuel consumption"
- "Longest range electric vehicles"

### Feature Queries
- "What features does Tesla Model 3 have?"
- "Compare seating and cargo space"
- "Which car is safest?"

## Sidebar Options Explained

| Option | What It Does |
|--------|-------------|
| Comparison Type | Chooses what aspect to focus on |
| Vehicle Category | Filters cars by type |
| Price Range | Sets budget constraints |
| Top Priorities | Highlights what matters to you |
| Table Format | Shows specs in organized tables |
| Recommendations | AI suggests best choice for you |

## Available Car Models

- 🔋 **Tesla Model 3** - Electric, Premium
- 💎 **BMW 3 Series** - Luxury Sedan
- 🏎️ **Ford Mustang** - Sports Car
- 🚗 **Honda Civic** - Compact, Reliable
- 🌱 **Toyota Corolla** - Hybrid, Efficient

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Enter | Send message |
| R | Refresh page |
| C | Clear chat history |
| S | Toggle sidebar |

## File Locations

```
cars_compare_bot/
├── app.py ..................... Main application
├── requirements.txt ........... Dependencies
├── START_CHATBOT.bat .......... Windows batch launcher
├── START_CHATBOT.ps1 .......... PowerShell launcher
├── README.md .................. Full documentation
├── SETUP_GUIDE.md ............. Installation guide
├── QUICK_REFERENCE.md ......... This file
└── CUSTOMER_GUIDE.md .......... User guide
```

## Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| "Can't connect to Ollama" | Run `ollama serve` in another terminal |
| "Module not found" | Run `pip install -r requirements.txt` |
| "Slow responses" | Close other apps, restart Ollama |
| "Port already in use" | Run on different port: `streamlit run app.py --server.port 8502` |
| "Model not found" | Run `ollama pull qwen2:1.5b` |

## Common Errors & Solutions

```
Error: "ConnectionRefusedError"
→ Solution: Make sure Ollama is running (ollama serve)

Error: "ModuleNotFoundError: No module named 'streamlit'"
→ Solution: pip install streamlit

Error: "The port 8501 is already in use"
→ Solution: streamlit run app.py --server.port 8502

Error: "Model 'qwen2:1.5b' not found"
→ Solution: ollama pull qwen2:1.5b
```

## Configuration Quick Tips

### Change Model
Edit line in `app.py`:
```python
model="qwen2:1.5b"  # Change to mistral:7b, etc.
```

### Change Port
```bash
streamlit run app.py --server.port 8502
```

### Change Theme
Edit CSS in `app.py` for colors, fonts, etc.

### Add Car Models
Edit `cars_database` dictionary in `app.py`

## Performance Tips

- ⚡ Use lighter models for faster responses
- 🖥️ Allocate more RAM for better performance
- 📱 Close other apps to free resources
- 🔄 Keep Ollama running in background
- 💾 Clear chat history if experiencing lag

## Terminal Tips

### Windows PowerShell
```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Deactivate
deactivate
```

### Mac/Linux
```bash
# Activate virtual environment
source venv/bin/activate

# Deactivate
deactivate
```

## Feature Overview

✅ **Available**
- Side-by-side comparisons
- Specification tables
- Performance analysis
- Price comparisons
- AI recommendations
- Quick action buttons

🔄 **In Development**
- Real-time market data
- User reviews
- Trade-in calculator
- Insurance estimator

## Browser Compatibility

| Browser | Status |
|---------|--------|
| Chrome | ✅ Full Support |
| Firefox | ✅ Full Support |
| Safari | ✅ Full Support |
| Edge | ✅ Full Support |

## System Requirements Quick Check

```bash
# Check Python version
python --version  # Should be 3.8+

# Check pip
pip --version

# Check Ollama
ollama --version

# Check model installed
ollama list
```

## Getting Help

1. **README.md** - Full documentation
2. **SETUP_GUIDE.md** - Installation help
3. **CUSTOMER_GUIDE.md** - Usage guide
4. **FILE_INDEX.md** - File descriptions

## Useful Links

- 🌐 Streamlit: https://streamlit.io
- 🤖 Ollama: https://ollama.ai
- 📚 Python: https://python.org
- 🚗 Car Data Sources: (Add your sources here)

## Pro Tips

💡 **Tip 1**: Keep Ollama running in a separate terminal for faster responses

💡 **Tip 2**: Use Chrome for best performance and features

💡 **Tip 3**: Ask follow-up questions to refine comparisons

💡 **Tip 4**: Use specific car names for accurate specs

💡 **Tip 5**: Set price range in sidebar to focus results

---

**Quick reference complete! Happy comparing! 🚗**

